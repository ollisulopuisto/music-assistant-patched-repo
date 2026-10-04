# HAOS / MPD channel-routing investigation — 2026-09-26

## Findings

PulseAudio's remapper changes the actual samples, and the installed MPD
0.24.15 Pulse output honors an explicit `sink` setting. Both were verified
with recorded audio through silent virtual sinks on this HAOS installation.
The earlier claim that Pulse remapping did not work was unsupported.

The running MPD output template selects `type "pulse"` but contains no `sink`
setting. A temporary virtual sink was created and one active MPD sink-input
was moved to it. That move was confirmed in Pulse, but it was not a persistent
MPD configuration change. The remapper was subsequently removed when playback
changed to stereo. Later playback therefore had no remapper to use. A live
move may also be remembered by Pulse's stream-restore module, so it is not a
reliable way to scope a correction to multichannel playback alone.

The inferred correction was not based on a complete physical channel map.
The older spoken sample placed the subwoofer announcement in CENTER. The
current sample duplicates its cue in FL and FR and steps through 50, 60, 70
and 80 Hz only in LFE, so these can be checked as independent source channels. The
physical routing still requires an end-to-end listening check.

## File verification

The local test FLAC, the test-app copy, and the file mounted in HAOS all have
SHA-256 `ac5f5b8353abe72065da77e931cb2171dbc940a8e61b2942ba44370f7dbad4df`.
Decoded sample energy confirms the following channel isolation:

| Time | Channel containing audio |
| --- | --- |
| 0–5 s | FL |
| 5–10 s | FR |
| 10–15 s | FC |
| 15–20 s | FL + FR — announces the upcoming subwoofer test |
| 20–23 s | LFE — 50, 60, 70, 80 Hz stepped tones |
| 25–30 s | BL |
| 30–35 s | BR |

Channel labels in a live Pulse stream alone do not establish where the actual
spoken samples or physical speakers are routed.

## Sample-level verification

Two seconds of 16-bit, 48 kHz PCM carried a distinct frequency on each source
channel: FL 311 Hz, FR 419 Hz, FC 557 Hz, LFE 683 Hz, BL 809 Hz, BR 947 Hz.
These signals were sent only to a silent null sink, never the HDMI speakers.
The null sink's monitor was recorded and each channel's spectral content was
measured. The baseline preserved all six channels.

The previous trial permutation used:

```
channel_map=front-left,front-right,front-center,lfe,rear-left,rear-right
master_channel_map=front-center,lfe,front-right,front-left,rear-left,rear-right
remix=no
```

Both `paplay` and a separate MPD process using `sink "ma_probe_remap"`
produced the following recorded result:

| Output channel | Source signal |
| --- | --- |
| FL | LFE |
| FR | FC |
| FC | FL |
| LFE | FR |
| BL | BL |
| BR | BR |

The diagnostic MPD used its own temporary database/configuration, listened
only on container loopback port 16661, and did not control the running player.
Its selected sink was verified live. Diagnostic processes, temporary files,
and virtual sinks were removed and the original default sink restored.

These checks prove the software remap and explicit MPD sink selection work.
They do not validate that this particular permutation corrects the physical
HDMI speakers, nor do they test the full MA streaming pipeline.

## Requirements for the next physical check

Select a named diagnostic sink explicitly in MPD before starting playback,
and keep that route in place for the entire spoken track. Verify the active
sink before interpreting the listening results. Start with a known mapping
and record all six actual destinations; distinguish the center announcement
from the LFE tone. Keep stereo behavior a separate verification: a fixed
six-channel remap can also affect stereo streams routed through it.

For a lasting solution, both creation of the named sink and MPD's selection
of it must survive restarts, with clear handling when the sink is unavailable.
Do not ship the previously guessed permutation as a confirmed hardware fix.
