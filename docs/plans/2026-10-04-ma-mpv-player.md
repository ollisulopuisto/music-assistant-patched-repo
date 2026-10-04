# MA MPV Player Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Package the tested MPD-to-MPV bridge as an independent macOS service that Music Assistant can control through its built-in MPD Players provider.

**Architecture:** MA continues to own the queue and stream generation. A small native Mac process exposes the MPD commands MA needs and controls a local MPV process over its private Unix socket; MPV fetches MA's reachable stream URL and sends decoded audio to CoreAudio. A per-user LaunchAgent supervises the bridge, credentials are stored in the macOS Keychain, and Navidrome, Audio Format Guard, and HA input switching remain companion projects.

**Tech Stack:** Python 3 standard library, MPV, macOS Keychain (`security` CLI), launchd LaunchAgent, shell installer, plist template, GitHub Actions.

---

### Task 1: Establish the clean repository skeleton

**Files:**
- Create: `README.md`
- Create: `.gitignore`
- Create: `.github/workflows/ci.yml`
- Copy: current `bridge.py` into `bridge.py`
- Create: `config.example.json`
- Create: `launchd/com.ollisulopuisto.ma-mpv-player.plist.example`
- Create: `scripts/generate-launch-agent.py`

1. Keep only the runtime bridge and package-owned deployment assets in this repository.
2. Document the MA → MPD protocol bridge → MPV → CoreAudio path and companion-project boundaries.
3. Add CI for Python syntax and protocol tests; do not require Docker or a physical audio device.

### Task 2: Make bridge credentials independent of MPD

**Files:**
- Modify: `src/ma_mpv_player/bridge.py`
- Create: `scripts/store-password.sh`
- Test: `tests/test_bridge.py`

1. Replace `~/.mpd/mpd.conf` dependency with macOS Keychain lookup keyed by service/account.
2. Require a password at startup and never log it or the complete MA stream URL.
3. Keep Keychain service/account configurable for multiple bridge instances.

### Task 3: Add service lifecycle and configuration

**Files:**
- Create: `launchd/com.ollisulopuisto.ma-mpv-player.plist.example`
- Create: `scripts/install.sh`
- Create: `scripts/uninstall.sh`
- Create: `scripts/status.sh`

1. Configure MPV executable, CoreAudio device UID, MPD listen address/port, IPC socket, and Keychain identity outside the code.
2. Install a user LaunchAgent with `RunAtLoad` and `KeepAlive`, stable logs, and a controlled PATH.
3. Ensure uninstall stops/removes only this LaunchAgent and leaves user audio settings intact.

### Task 4: Add protocol regression tests

**Files:**
- Create: `tests/test_protocol.py`
- Modify: `.github/workflows/ci.yml`

1. Use a fake MPV client to cover MPD auth, status, `clear/add/play`, pause, stop, seek, volume, idle notification, and current-song URL protection.
2. Verify incorrect passwords are rejected and secret/URL paths are not emitted in logs.
3. Run tests locally and in CI without connecting to CoreAudio.

### Task 5: Verify install artifacts and publish-ready state

**Files:**
- Review: all repository files

1. Validate shell scripts with `bash -n`, plist with `plutil -lint`, and tests with `python3 -m unittest`.
2. Confirm install instructions configure MA's existing MPD Players provider and state the required MA stream URL reachability.
3. Initialize a dedicated local git repository in `~/Documents/koodi/ma-mpv-player`; do not create or publish a GitHub repository unless separately requested. Leave the license decision for publication.
