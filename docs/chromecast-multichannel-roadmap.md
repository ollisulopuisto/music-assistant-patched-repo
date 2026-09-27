# Multichannel Playback Roadmap: Chromecast Support

> **Status (2026-09-27):** exploration from March 2026, moved here from a local working copy. None of the hypotheses in §6 were run to a recorded result. The harness is `scripts/chromecast-multichannel/multichannel_tester.py`. The current multichannel path is native MPD over HDMI, not Chromecast.

## 1. Objective
Enable true multichannel (5.1, 7.1) audio playback from Music Assistant to supported Google Cast devices (Chromecast Ultra, Chromecast with Google TV, etc.) and compatible Audio Groups.

## 2. Technical Context & Constraints
*   **Chromecast Receiver:** Music Assistant uses a custom Web Receiver (HTML5 app) to play streams. The browser environment (Chrome/Cast) must support the codec and channel layout.
*   **FFmpeg Pipeline:** MA uses FFmpeg to transcode source files into a format the receiver can ingest.
*   **Protocol:** Currently, most streams are served as FLAC or PCM over HTTP.

## 3. Potential Approaches

### Approach A: Multichannel FLAC (PCM)
*   **Theory:** Stream 6-channel FLAC directly. Many modern Chromecasts support high-resolution multichannel FLAC.
*   **Pros:** Lossless, high quality.
*   **Cons:** High bandwidth; Google Cast receiver might downmix to stereo if not explicitly handled.

### Approach B: AC3/EAC3 Passthrough (Bitstream)
*   **Theory:** Encode the audio as AC3 (Dolby Digital) or EAC3 (Dolby Digital Plus).
*   **Pros:** Industry standard for surround; lower bandwidth than FLAC.
*   **Cons:** Requires HDMI-connected device (TV/AVR) to decode.

### Approach C: Matroska (MKV) Container
*   **Theory:** Wrap the audio in an MKV container, which is robust for multichannel metadata.
*   **Pros:** Better metadata handling for channel mapping.
*   **Cons:** Cast receiver might need MSE (MediaSource Extensions) to handle MKV.

### Approach D: Custom Receiver Logic
*   **Theory:** Update the `cast-receiver/index.html` to ensure it detects and requests multichannel capabilities.

## 4. References & Documentation
*   [Google Cast: Supported Media](https://developers.google.com/cast/docs/media)
*   [FFmpeg Audio Channel Manipulation](https://trac.ffmpeg.org/wiki/AudioChannelManipulation)

## 5. Failed/Reverted Approaches (Log)

| Date | Approach | Result | Reason for Failure |
| :--- | :--- | :--- | :--- |
| 2026-03-10 | Generic `pan` filter for all >2ch | **REVERTED** | Forced downmixing, lost true multichannel. |
| 2026-03-10 | Adding `ac3/eac3` MIME types | **REVERTED** | "Queue not available" errors; registry not updated. |
| 2026-03-10 | Defaulting `matroska` output | **REVERTED** | Broke standard stereo playback. |

## 6. Test Hypotheses (Target: Ultracast TV)

We will use a custom test script `scripts/chromecast-multichannel/multichannel_tester.py` to test the following hypotheses on "Ultracast TV" (192.168.1.205):

### Hypothesis 1: Native Multichannel FLAC
*   **Method:** Stream 5.1 FLAC file directly.
*   **MIME Type:** `audio/flac`
*   **Success Criteria:** AVR detects 5.1 PCM or FLAC signal.

### Hypothesis 2: AC-3 (Dolby Digital) Passthrough
*   **Method:** Transcode 5.1 FLAC to AC-3 on-the-fly.
*   **MIME Type:** `audio/mp4; codecs="ac-3"`
*   **Success Criteria:** AVR detects "Dolby Digital" signal.

### Hypothesis 3: E-AC-3 (Dolby Digital Plus) Passthrough
*   **Method:** Transcode 5.1 FLAC to E-AC-3 on-the-fly.
*   **MIME Type:** `audio/mp4; codecs="ec-3"`
*   **Success Criteria:** AVR detects "Dolby Digital Plus" signal.

### Hypothesis 4: Matroska "Video Trick"
*   **Method:** Wrap 5.1 audio in a Matroska (MKV) container (no video).
*   **MIME Type:** `video/x-matroska`
*   **Success Criteria:** Chromecast handles the MKV container better than raw audio for multichannel.
