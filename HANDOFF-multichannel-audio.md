# Handoff — Multichannel Audio, DSD Playback & Native MPD

Written 2026-09-26. Covers the architecture, patches, current system state, and immediate next steps for multichannel 5.1 and DSD playback to the Denon AVR via HDMI.

---

## 1. System Architecture & Repositories

| Component / Repo | Location / Endpoint | Branch / Service | Role / Status |
| :--- | :--- | :--- | :--- |
| **`music-assistant-patched-repo`** | `/Users/dst/Documents/koodi/music-assistant-patched-repo` | `main` | Orchestration repo, patch source (`patches/`), test media, add-on specs. |
| **`MPD` fork** | `/Users/dst/Documents/koodi/mpd`<br>`https://github.com/ollisulopuisto/MPD` | `macos-multichannel` | Fork of `MusicPlayerDaemon/MPD` with macOS CoreAudio multichannel fixes. Pushed to GitHub. |
| **Native MPD Daemon** | Mac Studio host (`192.168.1.222:6600` / `localhost:6600`) | `fi.sulopuisto.mpd-native` (PID 5307) | Runs native MPD 0.24.15 talking directly to `DENON-AVR` over HDMI via CoreAudio. |
| **HAOS VM** | Home Assistant OS VM (`192.168.1.202`) | Test Add-on on `:18095` | `local_haos_hdmi_mpd` **uninstalled & removed**. `local_ma_multichannel_test` has server wheel `.14`. |

---

## 2. Why Native MPD on Mac Studio?

Initial attempts routed audio from Music Assistant through a HAOS add-on (`haos-hdmi-mpd`) using PulseAudio and ALSA over the VM sound card. This introduced:
* Inconsistent speaker routing and channel mapping ambiguities.
* Crackling on ALSA continuous sine tones and PulseAudio stream-restore configuration drift.
* Additional resampling and mixer layers.

To eliminate VM audio layers entirely:
* **HAOS MPD was uninstalled**: `ha apps uninstall local_haos_hdmi_mpd` was executed, and `/addons/haos-hdmi-mpd` was deleted from the VM.
* **Native MPD on macOS was deployed**: MPD runs natively on the Mac Studio, outputting directly to CoreAudio device `DENON-AVR` over HDMI. macOS currently detects the Denon AVR with **6 output channels** at 96 kHz.

### Patches Applied to MPD (Branch `macos-multichannel`)
1. **`output/osx: write complete audio frames`** ([`2a7a993`](https://github.com/ollisulopuisto/MPD/commit/2a7a99386)):
   * *Problem*: The stock CoreAudio plugin wrote arbitrary byte chunks to its ring buffer, slicing interleaved multichannel frames and triggering an assertion crash (`PlayChunk: nbytes % frame_size == 0`).
   * *Fix*: Uses `ring_buffer.WriteFramesFrom(input, asbd.mBytesPerFrame)` and checks complete frame availability.
2. **`output/osx: prefer matching channel count`** ([`ec80e49`](https://github.com/ollisulopuisto/MPD/commit/ec80e49c5)):
   * *Problem*: MPD's default format scorer picked the highest available hardware channel count, unnecessarily upmixing 6-channel (5.1) content to 8 channels on HDMI.
   * *Fix*: Adds score weight (+100) for exact channel count matches while preserving sample rate priority.

### Native MPD Service Details
* **Binary**: `~/.local/opt/mpd-native/bin/mpd` (built with `native-mpd/build.sh`)
* **Config**: `~/.mpd/mpd.conf` (mode 0600)
* **Output configuration**:
  ```
  audio_output {
      type "osx"
      name "Mac Studio HDMI — Denon"
      device "DENON-AVR"
      hog_device "no"
      mixer_type "none"
      dop "no"
  }
  ```
* **Control command**:
  ```bash
  launchctl kickstart -k "gui/$(id -u)/fi.sulopuisto.mpd-native"
  ```
* **Music directory**: `~/.mpd/music/`

---

## 3. Music Assistant Core Patches

The following patches have been developed and tested in the MA server pipeline:

1. **`patches/server/0120-dsd-multichannel-pcm.patch`**:
   * Extends shared buffer and queue format limits from 2 channels up to 8 channels.
   * Exposes an explicit per-player `multichannel` output channel option on HTTP player protocols.
   * Standardizes 6-channel PCM on `5.1(side)` as the canonical intermediate layout to preserve correct mapping across buffer boundaries.
   * Decodes DSD64 to 176.4 kHz PCM.
   * Caps raw PCM buffer allocations at 256 MiB.
2. **`patches/server/0121-dff-dsd-marker.patch`**:
   * Identifies `.dff` files (including DST compression) as DSD format in local file provider so buffer byte accounting treats them as DSD rather than 8-bit PCM.
3. **`patches/server/0122-preserve-dsd-stereo-downmix.patch`**:
   * Retains multichannel DSD in 32-bit float PCM through the shared buffer and disables FFmpeg clip-safe normalization during stereo downmixing, matching direct DSD-to-stereo gain.
4. **`patches/server/0004-library-first-letter-jump.patch` (Bugfix)**:
   * Fixed runtime `NameError: name 'order_by' is not defined` in random query helper by adding `order_by: str | None = None` to method parameters.

### Packaging & Staging
* Built wheels: `music_assistant-2.10.4+upnext.11`, `.13`, and latest `.14` located in `haos-ma-multichannel-test/`.
* Test add-on `local_ma_multichannel_test` on HAOS (`192.168.1.202:18095`) was rebuilt with `.14`. Server package verification verified gain `1.000000001` and correlation `0.999999999999` on DST DFF decodes.

---

## 4. Navidrome Multichannel & DTS Support

Documented in `docs/plans/2026-09-25-navidrome-multichannel-serving.md`:
* Patch [`patches/navidrome/0001-dts-multichannel-streaming.patch`](file:///Users/dst/Documents/koodi/music-assistant-patched-repo/patches/navidrome/0001-dts-multichannel-streaming.patch) adds an `ffprobe` fallback to Navidrome's `gotaglib` adapter when scanning raw `.dts` files without standard tags.

---

## 5. Physical Channel Verification Guide

The test file `test-media/5.1-spoken-channel-identification.flac` is already copied to `~/.mpd/music/` and indexed in native MPD.

### Playback Command
```bash
mpc clear && mpc add 5.1-spoken-channel-identification.flac && mpc play
```

### Channel Order Verification Table
| Timestamp | Channel | Expected Spoken Announcement / Signal |
| :--- | :--- | :--- |
| **0–5 s** | **Front Left (FL)** | *"Front left speaker channel."* |
| **5–10 s** | **Front Right (FR)** | *"Front right speaker channel."* |
| **10–15 s** | **Center (FC)** | *"Center speaker channel."* |
| **15–20 s** | **Front Left + Front Right (FL + FR)** | *“Front left and front right. Next will be the subwoofer.”* |
| **20–23 s** | **Subwoofer (LFE)** | 50, 60, 70 and 80 Hz steps (−18 dBFS) |
| **25–30 s** | **Surround Left (SL)** | *"Back left speaker channel."* |
| **30–35 s** | **Surround Right (SR)** | *"Back right speaker channel."* |

*(Note: The file announces "back left/right" according to standard 5.1 channel nomenclature, which routes to side surrounds on a 5.1 AVR setup).*

---

## 6. Immediate Next Steps

1. **Conduct the Listening Test**:
   * Switch the Denon AVR input to Mac Studio HDMI.
   * Adjust AVR volume knob to a moderate level (software volume is disabled).
   * Run `mpc play` and confirm each channel speaks from the correct physical speaker.
2. **Connect Music Assistant to Native MPD**:
   * Add the MPD player provider in Music Assistant (`local_ma_multichannel_test` on `http://192.168.1.202:18095`).
   * Point to host `192.168.1.222` port `6600`.
   * Configure MA's advertised stream address/port so MPD can reach MA stream URLs over the LAN (avoid container internal `172.30.33.4`).
3. **Commit MA Server Changes**:
   * When ready to publish to production add-on (`music-assistant-upnext-test`), commit the modified `README.md`, `patches/server/0004-*`, and untracked `0120*` through `0122*` patches to `main` (which will trigger CI build `build-patched.yml`).

## 7. MPV Bridge — 2026-09-28 overnight check

> **Superseded 2026-10-04:** the prototype `native-mpv-bridge/` was removed from this
> repo. The bridge now lives in its own repo, `~/Documents/koodi/ma-mpv-player`, and
> runs as a LaunchAgent on the Mac (port 6601). The notes below are historical.

The local MPV → CoreAudio route played the 96 kHz/24-bit 5.1 Bob Marley file cleanly.
To let MA control that route, `native-mpv-bridge/bridge.py` now exposes the MPD
commands MA uses and drives MPV over its private Unix IPC socket. The bridge was
reachable at `192.168.1.222:6601`, and MA+ (`27d294da_music_assistant_upnext_test`,
version `.13`, `host_network: true`) connected and authenticated successfully.
On Play, MA sent `clear`, `add`, and `play`; the protocol bridge is functioning.

MPV then failed to load MA+'s stream. Its URL host/port (logged without its path
or token) was `192.168.1.202:8097`. MPV/FFmpeg in the managed agent execution
returned `No route to host`. A header-only `curl` request to the same stream URL
returned `200 audio/wav`; a direct `curl` to the base endpoint returned `404` as
expected. A silent MPV probe launched from macOS Terminal connected to the same
host and port successfully and received the expected 404 at the base path. This
isolates the fetch failure to the managed agent execution environment; MA+ and
the Mac's LAN route are reachable from Terminal.

The bridge is now running idle from a macOS Terminal at
`192.168.1.222:6601`. MA+'s two MPD connections initially stayed disconnected
after the bridge restart, so I restarted MA+ at 00:32 local; it came back on
`.13` and both MPD connections re-established. The player is idle and no audio
is active. Retry the track from MA+ to verify the Terminal-launched MPV can fetch
the stream. The command to restart the bridge later:

```sh
cd ~/Documents/koodi/music-assistant-patched-repo
python3 native-mpv-bridge/bridge.py \
  --listen 192.168.1.222 --port 6601 --verbose
```

The MPV bridge disables yt-dlp fallback and redacts HTTP URLs from its logs.
The last header-only request reported `176400 Hz`, 24-bit, 2-channel audio; verify that
the selected MA item is the local multichannel file and that the MPD player's
channel mode is set to multichannel. Do not treat the stereo headers as a
channel-mapping result until that is confirmed.
