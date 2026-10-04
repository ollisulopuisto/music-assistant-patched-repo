import AudioToolbox
import CoreAudio
import Foundation

private let targetName = "DENON-AVR"
private let targetRate = 192_000.0
private let targetChannels: UInt32 = 6
private let targetBits: UInt32 = 24

private var watchedProperties = Set<String>()
private var configuredSignature = ""

private func log(_ message: String) {
    let formatter = ISO8601DateFormatter()
    print("\(formatter.string(from: Date())) \(message)")
    fflush(stdout)
}

private func address(_ selector: AudioObjectPropertySelector,
                     scope: AudioObjectPropertyScope = kAudioObjectPropertyScopeGlobal)
    -> AudioObjectPropertyAddress {
    AudioObjectPropertyAddress(mSelector: selector,
                               mScope: scope,
                               mElement: kAudioObjectPropertyElementMain)
}

private func readUInt32(_ object: AudioObjectID,
                        _ property: AudioObjectPropertyAddress) -> UInt32? {
    var property = property
    var value: UInt32 = 0
    var size = UInt32(MemoryLayout<UInt32>.size)
    let status = AudioObjectGetPropertyData(object, &property, 0, nil, &size, &value)
    return status == noErr && size == MemoryLayout<UInt32>.size ? value : nil
}

private func readCFString(_ object: AudioObjectID,
                          _ property: AudioObjectPropertyAddress) -> String? {
    var property = property
    var value: Unmanaged<CFString>?
    var size = UInt32(MemoryLayout<Unmanaged<CFString>?>.size)
    let status = withUnsafeMutablePointer(to: &value) {
        AudioObjectGetPropertyData(object, &property, 0, nil, &size, $0)
    }
    guard status == noErr, let value else { return nil }
    return value.takeUnretainedValue() as String
}

private func readArray<T>(_ object: AudioObjectID,
                          _ property: AudioObjectPropertyAddress,
                          as: T.Type = T.self) -> [T] {
    var property = property
    var size: UInt32 = 0
    guard AudioObjectGetPropertyDataSize(object, &property, 0, nil, &size) == noErr,
          size >= MemoryLayout<T>.size else { return [] }
    let count = Int(size) / MemoryLayout<T>.stride
    var values = [T](unsafeUninitializedCapacity: count) { buffer, initializedCount in
        var returnedSize = size
        let status = AudioObjectGetPropertyData(object, &property, 0, nil,
                                                &returnedSize, buffer.baseAddress!)
        initializedCount = status == noErr ? Int(returnedSize) / MemoryLayout<T>.stride : 0
    }
    if values.count > count { values = Array(values.prefix(count)) }
    return values
}

private func allDevices() -> [AudioDeviceID] {
    readArray(AudioObjectID(kAudioObjectSystemObject),
              address(kAudioHardwarePropertyDevices), as: AudioDeviceID.self)
}

private func findDenon() -> AudioDeviceID? {
    allDevices().first { readCFString($0, address(kAudioObjectPropertyName)) == targetName }
}

private func scheduleRefresh() {
    DispatchQueue.main.asyncAfter(deadline: .now() + .milliseconds(250)) {
        refresh()
    }
}

private let propertyChanged: AudioObjectPropertyListenerProc = { _, _, _, _ in
    scheduleRefresh()
    return noErr
}

private func watch(_ object: AudioObjectID,
                   _ selector: AudioObjectPropertySelector,
                   scope: AudioObjectPropertyScope = kAudioObjectPropertyScopeGlobal) {
    let key = "\(object):\(selector):\(scope)"
    guard watchedProperties.insert(key).inserted else { return }
    var property = address(selector, scope: scope)
    let status = AudioObjectAddPropertyListener(object, &property, propertyChanged, nil)
    if status != noErr {
        watchedProperties.remove(key)
        log("Could not watch CoreAudio property \(selector): OSStatus \(status)")
    }
}

private func deviceIsAlive(_ device: AudioDeviceID) -> Bool {
    readUInt32(device, address(kAudioDevicePropertyDeviceIsAlive)) == 1
}

private func outputStreams(_ device: AudioDeviceID) -> [AudioStreamID] {
    readArray(device,
              address(kAudioDevicePropertyStreams,
                      scope: kAudioDevicePropertyScopeOutput), as: AudioStreamID.self)
}

private func selectTargetFormat(on stream: AudioStreamID) -> String? {
    let formats = readArray(stream,
                            address(kAudioStreamPropertyAvailablePhysicalFormats,
                                    scope: kAudioObjectPropertyScopeOutput),
                            as: AudioStreamRangedDescription.self)

    guard let ranged = formats.first(where: { candidate in
        let format = candidate.mFormat
        let range = candidate.mSampleRateRange
        let supportsRate = format.mSampleRate == kAudioStreamAnyRate ||
            (range.mMinimum <= targetRate && targetRate <= range.mMaximum)
        let isIntegerPCM = format.mFormatID == kAudioFormatLinearPCM &&
            format.mFormatFlags & kAudioFormatFlagIsSignedInteger != 0 &&
            format.mFormatFlags & kAudioFormatFlagIsFloat == 0
        return supportsRate && isIntegerPCM &&
            format.mChannelsPerFrame == targetChannels &&
            format.mBitsPerChannel == targetBits
    }) else { return nil }

    var desired = ranged.mFormat
    desired.mSampleRate = targetRate
    var property = address(kAudioStreamPropertyPhysicalFormat,
                           scope: kAudioObjectPropertyScopeOutput)
    var settable = DarwinBoolean(false)
    guard AudioObjectIsPropertySettable(stream, &property, &settable) == noErr,
          settable.boolValue else {
        return "192000/24/6 is available but the stream format is not writable"
    }

    var current = AudioStreamBasicDescription()
    var size = UInt32(MemoryLayout<AudioStreamBasicDescription>.size)
    let readStatus = AudioObjectGetPropertyData(stream, &property, 0, nil, &size, &current)
    if readStatus == noErr && current.mSampleRate == targetRate &&
        current.mChannelsPerFrame == targetChannels &&
        current.mBitsPerChannel == targetBits && current.mFormatID == desired.mFormatID {
        return "already 192000/24/6"
    }

    let status = AudioObjectSetPropertyData(stream, &property, 0, nil,
                                            UInt32(MemoryLayout<AudioStreamBasicDescription>.size),
                                            &desired)
    guard status == noErr else {
        return "failed to select 192000/24/6 (OSStatus \(status))"
    }
    return "selected 192000/24/6"
}

private func refresh() {
    guard let device = findDenon() else {
        if configuredSignature != "missing" { log("DENON-AVR is not present; waiting") }
        configuredSignature = "missing"
        return
    }
    watch(device, kAudioDevicePropertyDeviceIsAlive)
    watch(device, kAudioDevicePropertyStreams, scope: kAudioDevicePropertyScopeOutput)

    guard deviceIsAlive(device) else {
        if configuredSignature != "offline" { log("DENON-AVR is present but offline; waiting") }
        configuredSignature = "offline"
        return
    }

    let streams = outputStreams(device)
    for stream in streams {
        watch(stream, kAudioStreamPropertyAvailablePhysicalFormats,
              scope: kAudioObjectPropertyScopeOutput)
        watch(stream, kAudioStreamPropertyPhysicalFormat,
              scope: kAudioObjectPropertyScopeOutput)
    }

    guard !streams.isEmpty else {
        if configuredSignature != "no-streams" { log("DENON-AVR has no output streams yet; waiting") }
        configuredSignature = "no-streams"
        return
    }

    let results = streams.map { selectTargetFormat(on: $0) }
    let summary = results.enumerated().map { "stream \($0.offset): \($0.element ?? "192000/24/6 unavailable")" }
        .joined(separator: "; ")
    if summary != configuredSignature {
        log("DENON-AVR available; \(summary)")
        configuredSignature = summary
    }
}

watch(AudioObjectID(kAudioObjectSystemObject), kAudioHardwarePropertyDevices)
refresh()
dispatchMain()
