# Denon CoreAudio Format Watcher Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Restore the Mac Studio HDMI stream to six-channel 192 kHz PCM when the Denon AVR becomes available.

**Architecture:** A small user-session helper listens for CoreAudio device and stream-format changes. It discovers `DENON-AVR`, checks that the receiver is alive and advertises a compatible six-channel 192 kHz PCM format, then selects that physical stream format. A LaunchAgent keeps the helper running and logs every decision; unavailable formats are left untouched.

**Tech Stack:** Swift, CoreAudio HAL, launchd.

---

### Task 1: Implement and compile the CoreAudio watcher

**Files:**
- Create: `native-mpd/denon-audio-format-watcher.swift`
- Test: Compile with `swiftc` and run once while the Denon is off; expect a safe “device unavailable / format unavailable” log and no format writes.

### Task 2: Add the LaunchAgent installer and documentation

**Files:**
- Create: `native-mpd/install-denon-audio-format-watcher.sh`
- Create: `native-mpd/fi.sulopuisto.denon-audio-format-watcher.plist`
- Modify: `native-mpd/README.md`
- Verify: Install and inspect the loaded LaunchAgent; confirm it is monitoring without changing playback.

### Task 3: Verify on AVR reconnect

**Files:** None.
- With the AVR on, verify CoreAudio exposes six channels and 192 kHz.
- Confirm the watcher selects the supported format and logs success.
- Play the prepared multichannel sample and verify audible mapping separately.
