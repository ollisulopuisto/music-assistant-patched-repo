# Mac Audio Format Guard Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the one-off Denon watcher with a configurable macOS menu bar app that can restore selected output formats for any CoreAudio device.

**Architecture:** A SwiftUI app presents a compact menu bar status and a device/profile window. A CoreAudio manager discovers output devices and their advertised physical PCM modes, applies user-selected modes, and optionally reapplies them when the chosen device reconnects or its stream capabilities change. Device identity uses CoreAudio UIDs, while profile preferences live in UserDefaults.

**Tech Stack:** Swift 5.9+, SwiftUI, AppKit, CoreAudio, AudioToolbox, Swift Package Manager.

---

### Task 1: Create the Swift package and CoreAudio model

**Files:** Create `native-mpd/AudioFormatGuard/Package.swift`, `native-mpd/AudioFormatGuard/Sources/AudioFormatGuard/AudioDeviceManager.swift`.

Discover devices by UID, name, alive state, output streams, current physical format, and supported PCM combinations. Add apply-format support using the exact advertised `AudioStreamBasicDescription` and rate range. Observe system device-list, device-alive, output-stream, and stream-format properties.

### Task 2: Add user profile persistence and safe automatic behavior

**Files:** Create `native-mpd/AudioFormatGuard/Sources/AudioFormatGuard/AudioProfile.swift`, modify `AudioDeviceManager.swift`.

Persist a selected device UID, desired rate/bit depth/channel count, and an explicit “Automatically restore when device reconnects” toggle. Keep automation off until enabled. Report unsupported modes and CoreAudio errors without retry loops; retry after device/capability notifications.

### Task 3: Build the SwiftUI menu bar interface

**Files:** Create `native-mpd/AudioFormatGuard/Sources/AudioFormatGuard/AudioFormatGuardApp.swift`, `MainWindow.swift`, and `MenuBarView.swift`.

Use SwiftUI with a restrained audio-console visual style: clear device status, current and target format, device picker, supported format controls, manual Apply action, auto-restore toggle, recent activity, and settings access from a menu bar icon. Show unavailable controls as unsupported rather than accepting impossible settings.

### Task 4: Build, document, and retire the one-off installer

**Files:** Modify `native-mpd/README.md`; create `native-mpd/AudioFormatGuard/README.md` and build/install scripts.

Build the app with Swift Package Manager, install it under `~/Applications`, and register it as a login item using a per-user LaunchAgent or the app’s launch-at-login support. Update MPD docs to point to this configurable app and retain a migration/uninstall path for the Denon-only watcher.

### Task 5: Verify locally

Run `swift build` and the available Swift tests. Check device discovery and supported modes without changing any selected format; apply/reconnect behavior requires a receiver-connected listening session.
