# DSD and multichannel playback status

## DSD findings

- The local volume has 21 `.dsf` files; all 21 probed as stereo
  `dsd_lsbf_planar` at 352.8 kHz. FFmpeg defines a DSD sample as one packed byte,
  so that rate is one eighth of the DSD bit rate; its decoder filters the DSD
  stream into floating-point PCM at that sample rate. The patch then selects
  176.4 kHz as the PCM output target for DSD64 and FFmpeg resamples to it. This
  is a 2:1 conversion from FFmpeg's 352.8 kHz decoded rate, not a claim that the
  PCM output retains DSD's 64x bit rate ([FFmpeg DSD decoder](https://github.com/FFmpeg/FFmpeg/blob/master/libavcodec/dsd.c),
  [FFmpeg DSD sample format](https://github.com/FFmpeg/FFmpeg/blob/master/libavutil/samplefmt.h)).
- MA already recognizes `.dsf` and `.dff` in the local music provider. Its PCM
  buffer previously treated FFprobe's 8-bit packed DSD storage unit as an 8-bit
  PCM sample. FFmpeg actually emits the selected PCM encoding, so this made MA's
  PCM depth and buffer byte accounting disagree. The server patch converts DSD64
  into 176.4 kHz PCM before it enters the shared buffer. Stereo DSD uses 24-bit
  integer PCM; multichannel DSD stays in 32-bit float PCM through the buffer so a
  later stereo downmix keeps its direct DSD-to-stereo gain. A follow-up patch maps `.dff` to the available DSF marker in MA's
  shared format model, which has no separate DFF/DST value. This makes
  DST-compressed DFF take the DSD depth and rate path too. Real uncompressed
  and DST-compressed DFF samples were extracted and decoded with local FFmpeg,
  but the patched MA path has not yet played them.
- FFprobe rejected the SACD `.iso` files in this library as invalid input. MA's
  file provider does not scan ISO files as audio. Those images need their tracks
  extracted to DSF/DFF or PCM/FLAC before MA can index them. FFmpeg has a DST
  decoder, but this patch does not add SACD ISO demuxing or native disc navigation.
- The practical extraction route is `sacd_extract`: its CLI supports selecting
  multichannel tracks (`-m`), writing DSF (`-s`) or DFF (`-p`), and expanding DST
  (`-c`). I built it locally from the complete `sacd-ripper` source tree; the
  standalone `dregula/sacd_extract` repository is only the tool subproject and
  does not include the libraries required by its CMake project. From the
  extracted tool, this command writes track 1 from the Can SACD's six-channel
  area to a temporary DSF file:
  `sacd_extract -m -s -c -t 1 -i "Can_5.1_Promo.iso" -y /private/tmp/sacd-extract-sample`.
  A matching `-p -c` run produced uncompressed DFF, while `-p` without `-c`
  preserved the SACD's DST-compressed audio in DFF. FFprobe identifies that file
  as `dst`, 352.8 kHz, six-channel `5.1(side)`. FFmpeg decoded five seconds of
  DSF, uncompressed DFF, and DST-compressed DFF to six-channel 24-bit, 176.4 kHz
  PCM. The first second of DSF and uncompressed DFF output was byte-identical;
  the first five seconds of DST and uncompressed DFF output was byte-identical.
  The DSF demuxer reports `5.1`, while both DFF files report `5.1(side)`. These
  local FFmpeg conversions establish decode support, but are not yet playback
  through MA.
- This path is DSD-to-PCM playback. Native DSD / DoP passthrough to an external
  DAC needs separate capability negotiation and is not claimed here.
- The extracted DSF, DFF, and DST-in-DFF sources have not yet been played through
  the patched server build. Very high DSD rates have not been checked against a
  real file. The extraction and PCM conversion were performed with the Mac's
  FFmpeg, not the FFmpeg binary running in the HAOS add-on.

## Multichannel design

MA previously limited shared buffers and internal queue formats to two channels.
The patch preserves up to eight channels in the shared buffer, then chooses each
player's output channel count at the final conversion stage. Stereo stays the
default; an explicit per-player multichannel opt-in preserves source channels,
while stereo/mono players continue receiving FFmpeg's standard downmix. MP3
output remains stereo. Queue flow streams have one fixed channel count, so a
channel-count change between tracks restarts the stream. Crossfade and
stereo-specific DSP filters remain stereo-only. Per-channel front-left/front-right
preamp is skipped on multichannel output because the current setting only defines
those two channels; any global preamp still applies. Disable crossfade for the
multichannel check; enabling it keeps the stream stereo. The shared playback buffer
keeps the surround signal, while the analysis reader makes a separate FFmpeg stereo
downmix before feeding analyzers, preserving the prior Chromaprint-compatible input
without changing what the player receives.

The pinned `music-assistant-models==1.1.205` `AudioFormat` carries a channel
count but has no named channel-layout field. The shared buffer is raw PCM, so
its bytes also cannot retain the layout name. The patch now uses FFmpeg's
`5.1(side)` as the canonical layout whenever it reads or writes six-channel
PCM. This keeps `5.1(side)` SACD/DTS sources correctly identified across the
buffer boundary and rematrixes back-surround `5.1` sources to the side-surround
order used by this 5.1 setup. The spoken test FLAC is tagged as FFmpeg `5.1`
(BL/BR), while the real DTS source probes as `5.1(side)` (SL/SR); confirm the
physical receiver routing with the test sample. Other multichannel counts remain
unnamed because their possible layouts are ambiguous. Multichannel support is an
explicit opt-in because MA does not currently negotiate a maximum channel count
with each HTTP-based player; stereo remains the safe default.

The new choice is exposed on HTTP-based player protocols. AirPlay, Sendspin, and
Snapcast are excluded because they use separate output paths. The MA player you
use for the HDMI route must expose the new setting for this patch to reach it.

Each PCM buffer is capped at 256 MiB. When a high-resolution multichannel format
would exceed that limit at the selected buffer duration, seek-back history is
shorter than the configured preset. This prevents one queue from retaining
hundreds of megabytes to multiple gigabytes of decoded PCM. A regression test checks
that 192 kHz, 8-channel, 24-bit PCM is clamped below the maximum-duration preset.

For a typical 2.1 system, send stereo PCM and let the AVR do bass management.
MA already has a Crossfeed DSP filter for stereo output. It remains a headphone
effect, separate from speaker downmixing, and does not affect the shared
multichannel HDMI/speaker path.

A small 5.1 channel-identification FLAC is in `test-media/`; its README lists the
channel order and tone sequence for the first physical playback check.

## Verification limits

FFmpeg decoded a real local DSF file at its probed 352.8 kHz DSD byte/sample rate
and emitted 176.4 kHz PCM when asked. The included 5.1 FLAC decoded to both
six-channel and stereo 24-bit/48 kHz PCM for 18 seconds, with the expected byte
counts. On the target HAOS VM, direct ALSA `speaker-test` output has been heard
through HDMI and the Denon. The listener reported inconsistent physical speaker
routing across channel tests; a finite built-in WAV test had much less crackling
than continuous sine tests. This bypasses Music Assistant, so it does not validate
the patch and locates the mapping question below MA (HAOS/VMware/HDMI/AVR route).
On 2026-09-25, a read-only `ha audio info` check showed the default PulseAudio
output as `HD-Audio Generic Analog Surround 5.1`, with the `output:analog-surround-51`
profile active. On 2026-09-26, Music Assistant+ was running `2.10.4-upnext.11`.
The experimental HDMI MPD app was built by Supervisor on its native `aarch64` runtime
(HAOS 18.3), installed as `local_haos_hdmi_mpd`, and is stopped. The separate local
`local_ma_multichannel_test` app uses bridge networking and port `18095`. Its original
`0.1.1` container had exited with code 255; after rebuilding from the `.13` wheel and
starting it manually, Supervisor reported `started` and HAOS returned HTTP 200 on port
`18095`. Supervisor still labels the installed app `.1.1`, although its image reports
server package `2.10.4+upnext.13`; the staged `.1.2` manifest has not propagated to that
version field. Recent logs no longer show the earlier Home Assistant WebSocket 502. No
MA playback test has run.
A one-shot check of the MPD image shows the `pulse` output
plugin is compiled in. As part of the image build, the aarch64 target image's own
`get_ffmpeg_stream` helper decoded the real DST-compressed DFF to six-channel float PCM,
then downmixed it to stereo. Direct and staged stereo outputs were both 2,116,800 bytes;
gain was 1.000000001, correlation 0.999999999999, maximum difference 1 LSB, and 98.59%
of samples were byte-identical. The short report is retained at
`/usr/share/doc/ma-dsd-verification.txt` inside the local image; the 167 MB DFF source
was excluded from the final image. The spoken FLAC also passed inside the image: its own `get_ffmpeg_stream`
helper converted the generated 35-second spoken FLAC to 30,240,000 bytes of six-channel
PCM, then downmixed that PCM to 10,080,000 bytes of stereo. That stereo output matched
the direct FLAC-to-stereo conversion byte for byte (SHA-256
`f11c0b0a9641696d6c5e030bd8bc5a77b46a52a55e04d4a2bfd40ef95ff5ead4`). This exercises
the packaged server's DSD decode, multichannel buffer, and stereo downmix code on the
actual HAOS aarch64 image without starting the server or playing audio. The generated
spoken 5.1 FLAC is also now in
`/media/MA_multichannel_test/5.1-spoken-channel-identification.flac` with SHA-256
`39293a1c2757a768dfe555b70a00a45ed782e87ab3aba6d90e3be0639c6d0bb1`. The apps were
built without Docker on the Mac, but neither has been exercised with audio; MPD remains
stopped.
The standard 5.1 sample went through MA's actual `get_ffmpeg_stream` helper for
both stages: FLAC to 15,552,000 bytes of six-channel raw PCM, then raw PCM to
5,184,000 bytes of stereo. The two-stage stereo output matched direct helper
output byte for byte.
Real-library probes found a 24-bit/96 kHz, six-channel FLAC (“Waiting in Vain”)
and a DTS-in-WAV AC/DC source that FFprobe identifies as six-channel, 44.1 kHz
DTS. FFmpeg decoded two seconds of the DTS source to six-channel PCM and then to
stereo PCM. Comparing that two-stage downmix with direct DTS-to-stereo output gave
the same 176,400 signed-32 samples within 16 integer LSB; explicit raw-input layouts
`5.1` and `5.1(side)` produced identical stereo bytes in this FFmpeg build. This small
difference is from the extra PCM conversion stage. MA's `get_ffmpeg_stream` helper
reproduced the same two-second, 705,600-byte stereo result from the six-channel PCM.
It also decoded a real stereo DSF through MA's input/output format path to two seconds
of 24-bit/176.4 kHz PCM (2,116,800 bytes); the source probes as DSD64 with a 352.8 kHz
packed rate. Separately, one six-channel DSF, one uncompressed DFF, and one
DST-compressed DFF track were extracted from the Can SACD ISO. FFmpeg decoded all
three to 5.1 PCM at 24-bit/176.4 kHz. The DSF and uncompressed DFF outputs matched
byte for byte for one second; the DST-compressed and uncompressed DFF outputs
matched byte for byte for five seconds. The pinned server's `get_ffmpeg_stream`
wrapper decoded five seconds of DST-in-DFF to 15,876,000 bytes of six-channel
24-bit/176.4 kHz PCM, byte-identical to direct FFmpeg with `5.1(side)` explicitly
selected. The patched wrapper then read the raw buffer and wrote a 5.1(side) WAV
whose PCM payload was byte-identical to the buffer. I also ran the wrapper's full
conversion command from the pinned server's `get_ffmpeg_args`
builder using the DFF-to-DSD marker format (`DSF`, 352.8 kHz, 8-bit packed, six
channels); it emitted 594,016,416 bytes for the full 3:07 track.

An exploratory second-stage conversion from six-channel integer PCM to stereo
initially produced a gain ratio of 0.414214 (about −7.7 dB) compared with direct
DSD-to-stereo conversion. The cause was FFmpeg's clip-safe normalization when it
rematrixed integer multichannel PCM. Patch `0122` keeps multichannel DSD in float
PCM and explicitly disables that normalization for the later float-to-stereo
rematrix. On the extracted DST-in-DFF sample, the patched wrapper's buffered
stereo output now has gain ratio 1.0 and correlation 1.0 versus direct conversion,
with at most 1 LSB difference and 98.63% of samples byte-identical. Integer PCM
continues using FFmpeg's clip-safe downmix. This still does not prove how every
player endpoint handles a multichannel stream.
The wrapper and conversion builder were exercised locally, but the shared
playback buffer, player endpoint, and HAOS playback were not.

The focused server suite passed 232 tests before the DFF marker follow-up,
including the updated expectation that the shared buffer retains surround
channels. Ruff, Python compilation, and whitespace checks also passed before that
follow-up. After the six-channel layout change, the stream, FFmpeg, DSP, buffer,
analysis and filesystem-provider test files pass together: 306 passed. With patch `0122`, that focused set passes 308 tests. The full
patch series strictly applies in CI order to a fresh `2.10.4`
(`e30a4974ba951f38e21bea8d502af3b903df992c`) checkout. A local FFmpeg conversion
of the 5.1 test file to `5.1(side)` raw PCM and back produced byte-identical
samples (30,240,000 bytes); FFprobe identified the intermediate WAV as six-channel
`5.1(side)`. The earlier `.11` versioned wheel is at
`/private/tmp/ma-dist/music_assistant-2.10.4+upnext.11-py3-none-any.whl`
(SHA-256 `3fc9f9d16d49398aa88c4bf882d5366c55aec4a593ad5759a8c0241707afd51e`).
The earlier `0.0.0` wheel was only a packaging check; the versioned wheel is suitable
for assembling a local image, but it is not itself an installable HA app or container
image. That wheel contains the canonical `5.1(side)` mapping and patch
`0122`'s DSD float-buffer/downmix behavior. The focused suite passes 308 tests.
Ruff (excluding the repository's existing copyright and ISC004 rules for these
focused files), Python compilation, and whitespace checks passed before the latest A–Z
patch correction.

The live test-app log exposed a bug in the existing A–Z patch: its random query helper
forwarded `order_by` without declaring that parameter, causing periodic `NameError`
failures in metadata tasks. I added the missing optional parameter to the local
`0004-library-first-letter-jump.patch`. The complete patch series still applies cleanly
to a fresh pinned `2.10.4` checkout. I built a new local wheel at
`/private/tmp/ma-dist/music_assistant-2.10.4+upnext.13-py3-none-any.whl` (SHA-256
`96ec86bb28a693b8608b1fa648a79b43869edbecb430bb5f06bab787f726fb45`). The local HAOS
build context uses this wheel on the `.11` base. Supervisor rebuilt the installed `.1.1`
image with it; the app is started again. The patch correction remains local and has not
been pushed.

The generated 5.1 sample is copied to HAOS media storage and the test instance has an
isolated admin account. Add the Filesystem provider to the test instance, set a password
for the MPD app and start it, then configure MPD as the test instance's player. No audio
has played through MA; the earlier direct ALSA test bypassed MA and physical channel
mapping was uncertain.

## Listening order

1. **Multichannel PCM from HAOS/MA.** Index the already copied
   `5.1-spoken-channel-identification.flac` in the test instance's library. Disable crossfade and set the
   HDMI-connected player to multichannel. Check the front left/right, center,
   LFE, and surround left/right announcements. Then switch back to stereo and
   confirm that the same track downmixes correctly.
2. **DTS (optional).** The AC/DC folder has a CUE sheet whose source is
   `AC-DC - Back In Black.wav.dts`; FFprobe identifies it as six-channel DTS in a
   WAV container. The local provider now also scans standalone `.dts` files. MA
   decodes this to six-channel PCM, so this check does not depend on AVR DTS
   decoding and can still be downmixed by MA.
3. **High-resolution PCM.** Play a known 24-bit/96 kHz track through the same
   player. The local library has 5.1/96 kHz FLAC, for example “Waiting in Vain”
   from the Bob Marley *Legend* 5.1 folder. Confirm the AVR's input rate/format
   and listen for dropouts. In the MPD player's advanced MA settings, add the
   `96000 / 24` sample-rate option first; MA otherwise defaults this MPD player
   to only 44.1/48 kHz at 16-bit. Add `192000 / 24` to test 192 kHz PCM, and
   `176400 / 24` for DSD64's PCM conversion. The Audio MIDI Setup device rate
   does not automatically update MA's advertised sample-rate list.
4. **DSD.** Start with an indexed stereo DSF track. MA decodes DSD to PCM; for
   this DSD64 material the selected output is 24-bit/176.4 kHz. SACD ISO files
   must first be extracted to multichannel DSF/DFF or PCM/FLAC. After extraction,
   test one six-channel track and confirm both the AVR's rate and speaker routing.

On 2026-09-26, I narrowed the DSD downmix gain exception to multichannel DSD buffers explicitly. Ordinary float multichannel audio retains FFmpeg's clip-safe downmix, while multichannel DSD retains the measured direct-conversion gain in both playback and analyzer downmix paths. The full patch series through `0122` applies cleanly to a fresh pinned `2.10.4` checkout. I built a local `.14` wheel (SHA-256 `4badbd83528eba4a7e707c6c21c9bf62fc61c0546a6f612d551c043f88618af0`) and staged it in the isolated HAOS test app source. Focused Ruff checks passed with only the repository's existing `CPY001` and `ISC004` rules excluded, and Python compilation passed. The home router advertises Tailscale routes for `192.168.1.0/24` and `192.168.10.0/24`; this Mac initially did not accept subnet routes. I enabled route acceptance and SSH reached `192.168.1.202` through the router, but initially the HAOS SSH server rejected the key with `Permission denied (publickey)`. The user subsequently added the public key and restarted the HAOS SSH add-on, allowing the `.14` image to be installed.

After the user added this Mac's public key to the HAOS SSH add-on and restarted it, SSH access worked over the accepted Tailscale subnet route. I copied the `.14` wheel and updated local-app build files to `/addons/haos-ma-multichannel-test/`, then ran `ha apps rebuild local_ma_multichannel_test`. HAOS reports the test app started and HTTP `18095` returns 200. The actual image `local/aarch64-addon-ma_multichannel_test:0.1.2` contains server package `2.10.4+upnext.14`; its embedded aarch64 DSD conversion check reports gain `1.000000001`, correlation `0.999999999999`, maximum difference 1 LSB, and 98.59% exact samples. The local manifest is now `0.1.3`, but Supervisor still reports `0.1.2`; this metadata mismatch does not change the verified wheel installed in the image. The HDMI MPD app remains stopped, and no audio has played through MA.

The user set an MPD password and asked about the port/output. The MPD control port is `6600` (the app manifest maps host `6600` to container `6600`); its output is named `HAOS HDMI` and uses the default PulseAudio server/device. The first start exposed `init: true` injected by Supervisor because the MPD app manifest lacked `init: false`; adding that flag removed the PID-1 s6-overlay error. The Alpine MPD user belongs to group `audio`, not `mpd`, so the launcher now uses `mpd:audio`. Its Pulse feature check also needed to avoid `grep -q` on a `pipefail` pipeline; capturing `mpd --version` first avoids SIGPIPE. Supervisor is now on app version `0.1.1` and the rebuilt image has `docker_init=false`. The remaining startup failure is that Supervisor reports the saved `mpd_password` option as an empty string (length 0). I have not changed that option or repeated the password; the user needs to re-enter and save it before MPD can start. No audio has played.

On 2026-09-27, the user confirmed that macOS Audio MIDI Setup shows the Denon AVR as
connected with six channels, 24-bit, 192 kHz. The host-side format watcher had also
logged selecting `192000/24/6` earlier that day. A CoreAudio probe and
`system_profiler SPAudioDataType` run from this assistant shell returned no devices,
so shell-level device enumeration does not agree with the user's GUI session; it is
not evidence that the Denon is disconnected. Actual MA-to-MPD playback remains to be
tested.

The native Mac MPD LaunchAgent is currently reported running and targets the
`DENON-AVR` CoreAudio device. Its MPD log records completed playback of the 5.1
channel test and six-channel 48 kHz and 96 kHz validation tracks on 2026-09-26; the
real 96 kHz test file was indexed shortly after midnight on 2026-09-27. This proves
the native MPD path has processed multichannel/high-resolution items, but the log
does not establish the physical speaker mapping or confirm that Music Assistant
served those tracks to MPD. A read-only TCP check on 2026-09-27 received the live
greeting `OK MPD 0.24.0` from `192.168.1.222:6600`. At the same time, the isolated
MA endpoint `192.168.1.202:18095` returned `No route to host`, so the MA test server
was not reachable from this Mac during the check.

The MA+ build workflow now includes a focused config regression test: MPD must
expose the `multichannel` output option and configurable 96/192 kHz, 24-bit rates.
Patch `0123-test-mpd-multichannel-config.patch` applies cleanly to the current
pinned source checkout, and the resulting test module compiles. Running pytest
locally is blocked because the checkout requires Git-hosted Python dependencies
and this environment has network access disabled; CI is configured to run this
case on the next build.

A final strict audit exported pristine tag `2.10.4` at commit
`e30a4974ba951f38e21bea8d502af3b903df992c` and applied every `patches/server/*.patch`
in filename order with `git apply --check` followed by plain `git apply`. All ten
patches, including `0123`, applied. `python3 -m compileall -q music_assistant tests`
then passed on the assembled tree. The live MA+ endpoint still reports `.11`; the
published repo is at `.12`, so hardware playback through patched MA remains pending
the update of that running add-on.

The alternate HA/MA host at `192.168.10.245:8095` is reachable and its public
`/info` endpoint reports `2.10.4+upnext.11`. Fetching the public repository's
current `main` shows `2.10.4-upnext.12`; that published tree contains patches
`0120`–`0122`, while the additional test-only patch `0123` remains local. Therefore
the running MA+ instance has not yet picked up the multichannel/DSD server patch.
