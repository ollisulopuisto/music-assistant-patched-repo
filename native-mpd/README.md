# Native MPD on the Mac Studio

Installed on 2026-09-26: native Apple Silicon MPD 0.24.15 with two local CoreAudio
fixes. MPD talks directly to `DENON-AVR` through CoreAudio. Playback uses no VM
sound card, PulseAudio, or local container runtime.

## Running service

- MPD endpoint: `192.168.1.222:6600` (also localhost).
- Password: the existing HAOS MPD test password, reused without placing it here.
- Configuration: `~/.mpd/mpd.conf` (mode 0600).
- Executable: `~/.local/opt/mpd-native/bin/mpd`.
- Login service: `~/Library/LaunchAgents/fi.sulopuisto.mpd-native.plist`.
- Log: `~/.mpd/mpd.log`; launch output: `~/.mpd/service.log`.
- Test music: `~/.mpd/music/5.1-spoken-channel-identification.flac`.
- Homebrew's unpatched MPD service is stopped; `mpc` remains available as a client.

The service starts at login. It is currently idle with an empty queue.
The output has no forced format, software mixer, ReplayGain, normalization,
DoP, or exclusive-device mode. Stereo and multichannel input select matching
hardware channel counts when the device supports them. Native PCM playback
does not establish bit-perfect output or validate physical speaker assignments.

Restart the native service:

```sh
launchctl kickstart -k "gui/$(id -u)/fi.sulopuisto.mpd-native"
```

Do not use `brew services start mpd`: that starts the unpatched package and
would conflict on port 6600. Keep the private config and credentials out of Git.

## Why a patched build is installed

The unmodified Homebrew package reproducibly crashed during a one-second
silent six-channel WAV with:

```
Assertion failed: (nbytes % output->out_audio_format.GetFrameSize() == 0)
function PlayChunk, file Thread.cxx, line 282.
```

Its CoreAudio output wrote arbitrary byte counts into a ring buffer and could
return part of an interleaved frame. Patch `0001` uses the existing
`WriteFramesFrom` API and waits when fewer than one complete frame fits.
The regression reproduces a 65,536-byte write for a 12-byte frame, then checks
complete frames and sample identity through repeated buffer wraparound.

The stock format scorer also preferred the largest hardware channel count,
changing this HDMI device from six to eight channels even for 5.1 content.
Patch `0002` gives an exact channel-count match preference while retaining
sample-rate matching as the higher priority.

## Verification

Both patches apply strictly to the released MPD 0.24.15 source and reproduce
the installed build's source. The buffer regression fails with the old write
operation and passes with the frame-aware operation.

Silent FLAC tests finished naturally, without restarting MPD:

| Input | MPD stream | CoreAudio hardware during playback |
| --- | --- | --- |
| Stereo, 96 kHz / 24 bit | `96000:24:2` | 2 channels, 96 kHz |
| 5.1, 48 kHz / 24 bit | `48000:24:6` | 6 channels, 48 kHz |
| 5.1, 96 kHz / 24 bit | `96000:24:6` | 6 channels, 96 kHz |

These were digital silence: the physical speaker mapping and audible playback
quality still need a listening check. HAOS reached the Mac's MPD port. The test
MA container also reached it earlier in setup; that container was subsequently
absent during a later check, so no test apps were restarted automatically.

## Music Assistant connection

Use the Mac address above in the MPD Players provider, with the same test
password. The stream must also travel back from MA to the Mac. At inspection,
the isolated test MA exposed only `8095 -> 18095`, and advertised streams on a
container-private address (`172.30.33.4:8097`). That address is unsuitable for
the Mac player. Before testing MA playback, expose a dedicated stream port
and configure MA's advertised address/port to match the HAOS LAN endpoint.
This native installation has not changed the MA app's networking or providers.
The local spoken FLAC can be tested through MPD independently of that setup.

## Rebuild

Install dependencies with Homebrew if needed:

```sh
brew install mpd mpc meson ninja pkgconf
```

Run `native-mpd/build.sh` from this repository. It downloads the pinned release,
checks its SHA-256, strictly applies both patches, runs the frame regression,
and builds/installs the private binary. It does not restart the service.
Its default prefix is `~/.local/opt/mpd-native`; an alternate prefix may be
passed as the first argument. The patches are local artifacts, not an upstream
submission or a configured CI workflow.

## Restore an output format when a device reconnects

The recommended helper is the native **Audio Format Guard** menu bar app in
[`AudioFormatGuard/`](AudioFormatGuard/README.md). It can target any CoreAudio
output device, shows the integer PCM combinations that device advertises, and can
optionally restore one selected rate, bit depth, and channel count after reconnects.
Automation is disabled until the user selects a device and enables it in the app.

For the living-room Denon, the working selection was 192 kHz / 24-bit / 6-channel
PCM. The old `denon-audio-format-watcher.swift` and installer remain as a legacy
command-line fallback. Do not run the old watcher and Audio Format Guard's
automatic restore against the same device; both write the physical CoreAudio format.

Changing CoreAudio's physical output mode does not change MPD's input format, force
every track to a fixed rate, or configure speaker-to-channel assignments in Audio
MIDI Setup. MPD still chooses formats from each track, and the MPD CoreAudio plugin
uses its channel-count preference when playback opens. A listening test is needed
to validate audible channel routing.

CoreAudio plugin reference:
https://mpd.readthedocs.io/en/stable/plugins.html#osx
