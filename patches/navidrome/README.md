# Navidrome patch

`0001-dts-multichannel-streaming.patch` is a local patch against Navidrome
`1011457` (the upstream checkout used for this build). It is kept separate from
the Music Assistant patches because the MA image workflow does not build or
install Navidrome.

The patch recognizes raw `.dts` and DTS-in-WAV (`.wav.dts`) files. ffprobe is
authoritative for their codec and audio properties, even when TagLib succeeds
with generic WAV properties; TagLib's existing embedded tags are retained.
Files with a `.dts` suffix are omitted if ffprobe cannot confirm a DTS stream.
The patch also allows an explicitly requested DTS-to-FLAC transcode. That
transcode decodes DTS to PCM and encodes the resulting samples as FLAC at the
source rate and the client's allowed channel count. A six-channel capable
client can receive 5.1; a stereo-only client can request a stereo downmix. It
does not preserve the original DTS bitstream or recover information lost in
DTS encoding. Existing direct play still serves the original file unchanged.

Subsonic profiles currently describe a maximum channel count, not an exact
speaker layout. A conventional 2.1 receiver should therefore be treated as a
stereo endpoint and use its own bass management, rather than assuming three
discrete PCM channels mean left, right, and LFE.

The regression test reproduces TagLib successfully reading a WAV payload under
a `.dts` extension, then verifies that six-channel ffprobe properties replace
the misleading WAV properties while title and album tags remain intact. It
also verifies rejection of non-DTS content with a `.dts` suffix. The actual
`02_Shoot to Thrill.wav.dts` file was probed as DTS, 6 channels, 44.1 kHz, and
the local Navidrome multichannel library was fully rescanned with the fix.

The locally installed binary is `/Users/dst/Applications/navidrome-dts-patched`
and its LaunchAgent uses that binary. The patch applies cleanly to Navidrome
v0.64.2 (`1011457`). It has not been pushed or published; rebase it against a
full Navidrome history before maintaining or offering it upstream.
