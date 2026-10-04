# 5.1 channel identification samples

## Spoken labels

`5.1-spoken-channel-identification.flac` is a 35-second, 24-bit/48 kHz FLAC
with the `5.1` layout (`FL`, `FR`, `FC`, `LFE`, `BL`, `BR`). Each speaker name
is spoken from its corresponding channel. The front left and front right
channels announce the subwoofer test together, followed by four moderate LFE-only
tones: 50, 60, 70 and 80 Hz.

| Starts at | Channel | Audio |
| --- | --- | --- |
| 0 s | Front left (`FL`) | “Front left speaker channel.” |
| 5 s | Front right (`FR`) | “Front right speaker channel.” |
| 10 s | Center (`FC`) | “Center speaker channel.” |
| 15 s | Front left + front right (`FL` + `FR`) | “Front left and front right. Next will be the subwoofer.” |
| 20–23 s | LFE | 50, 60, 70 and 80 Hz, in 0.75-second steps at −18 dBFS |
| 25 s | Surround left (`BL` in standard 5.1 order) | “Back left speaker channel.” |
| 30 s | Surround right (`BR` in standard 5.1 order) | “Back right speaker channel.” |

The file labels the last two channels as back left/right because that is the
standard 5.1 channel order. In a 5.1 speaker setup, these are the left and
right surround channels and the AVR routes them to the side surrounds. There is
no separate rear speaker pair in this setup.

## Sine tones

`5.1-channel-identification.flac` is an 18-second, 24-bit/48 kHz FLAC with a
5.1 channel layout. It plays a quiet sine tone on one channel at a time, in this
order:

| Time | Channel | Tone |
| --- | --- | --- |
| 0–3 s | Front left | 440 Hz |
| 3–6 s | Front right | 494 Hz |
| 6–9 s | Center | 523 Hz |
| 9–12 s | LFE | 50 Hz |
| 12–15 s | Surround left (`BL`) | 587 Hz |
| 15–18 s | Surround right (`BR`) | 659 Hz |

Both files are for copying into a Music Assistant indexed folder for playback
checks. They were generated offline and were not played during generation.
