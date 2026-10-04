# HAOS and Navidrome Multichannel Playback Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Establish a standalone Home Assistant playback path, then make Navidrome reliably index and serve multichannel source files without converting them to stereo unless the client requests it.

**Architecture:** Add an independent MPD app that uses HAOS's PulseAudio bridge and is controlled by Home Assistant's built-in MPD integration. Keep Navidrome changes separate from the Music Assistant image patches. Preserve original files for direct streams; let client capability profiles govern any transcoding.

**Tech Stack:** Home Assistant app framework, MPD with PulseAudio output, Home Assistant MPD integration, Navidrome Go server and its FFmpeg/ffprobe adapter.

---

### Task 1: Add a standalone HAOS MPD playback app

**Files:** Create `haos-hdmi-mpd/config.yaml`, `Dockerfile`, `run.sh`, `mpd.conf`, and `README.md`.

1. Grant the app access to the internal audio system and expose MPD on the LAN for Home Assistant's MPD integration.
2. Mount `/media` read-only and keep the app stopped by default so creating/installing it cannot start playback.
3. Disable ReplayGain and MPD software volume control; use PulseAudio output and preserve incoming rate and channel count where the HAOS sink allows it.
4. Leave PulseAudio channel remixing available so a stereo-only sink can receive a downmix; document that a typical 2.1 receiver should use stereo PCM plus AVR bass management.
5. Require an MPD password and document that the shared PulseAudio mixer can still resample or mix streams.

### Task 2: Map current Navidrome playback behavior

**Files:** Read `core/stream/decider.go`, `core/stream/legacy_client.go`, `adapters/gotaglib/gotaglib.go`, and `resources/mime_types.yaml` in the Navidrome checkout.

1. Confirm the raw stream path returns the source unchanged.
2. Confirm client profiles can express channel limits that select either six-channel direct playback or a stereo downmix.
3. Record which source formats are already indexed and which fail metadata extraction.

### Task 3: Repair raw DTS indexing

**Files:** Modify Navidrome's tag metadata adapter and MIME type list only if inspection confirms raw DTS is currently skipped.

1. Keep taglib as the normal path.
2. For raw `.dts` only, use the existing ffprobe adapter to get duration, bitrate, sample rate, bit depth, channel count, and codec when tags cannot be read.
3. Use the filename as the track title fallback; do not alter the audio bytes.
4. Permit an explicitly requested DTS-to-FLAC transcode; retain source rate and use the client's channel cap, including stereo downmix when requested.

### Task 4: Preserve as a separate local Navidrome patch

**Files:** Create a standalone patch artifact under `patches/navidrome/` in the working copy.

1. Generate a patch against the checked-out Navidrome upstream base.
2. Keep it outside the Music Assistant build workflow, which does not consume Navidrome patches.
3. Build the Navidrome binary to catch compilation errors. Do not push or open an upstream PR.
