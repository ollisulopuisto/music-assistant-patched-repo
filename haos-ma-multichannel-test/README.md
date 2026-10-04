# Local Music Assistant multichannel test image

This HAOS local app overlays the locally built server wheel `2.10.4+upnext.14`
onto the patched Music Assistant+ image `2.10.4-upnext.11`. It reuses the
existing image's dependencies and patched frontend; the wheel replaces the
server Python package without resolving or changing dependencies.

The app is `boot: manual`. Installing it only builds and stores a separate image;
it does not stop or replace the installed Music Assistant+ app. It uses bridge
networking and maps its web/API port to HAOS host port `18095`, so it can run
alongside Music Assistant+ on its standard ports. Its app data is separate, so
it needs its own first-run setup. Open `http://<HAOS-IP>:18095` for that setup.

Supervisor builds this app on HAOS's native aarch64 engine. The current build
context uses package `2.10.4+upnext.14`. After rebuilding, verify the installed app
metadata with `ha apps info local_ma_multichannel_test` and the package version in
the running container.
No Docker installation is needed on the Mac. The wheel is intentionally a local build
artifact and is excluded from git. The generated spoken 5.1 FLAC is included
under `/tmp` in this test image for offline conversion checks; it is also copied
to HAOS `/media/MA_multichannel_test/` for later library playback. The build
runs `verify_dsd_wrapper.py` in a temporary verification stage against a real
DST-compressed DFF track: direct DSD-to-stereo must match buffered six-channel
float PCM-to-stereo within 1 LSB. The aarch64 HAOS build passed: 2,116,800-byte
direct and staged stereo outputs, gain 1.000000001, correlation 0.999999999999,
maximum difference 1 LSB, 98.59% exactly equal. Only the short verification
report is copied into the final image; the 167 MB DFF source stays out of it.

## Playback setup

1. Open `http://<HAOS-IP>:18095/setup` and create an admin account for this
   isolated test instance. It has its own data directory and does not use the
   Music Assistant+ login.
2. In the test instance, add the **Filesystem** music provider and set its
   folder to `/media/MA_multichannel_test`. The spoken sample is
   `5.1-spoken-channel-identification.flac` in that folder.
3. In the **HAOS HDMI MPD** app options, set a password at least 24 characters
   long, save, then start the app. It listens on the HAOS host at port `6600`.
4. In the test instance, add the **MPD Players** provider using host
   `<HAOS-IP>`, port `6600`, and the app password. Set its output codec to WAV,
   allow 48 kHz / 24-bit, and choose `multichannel` for the player's output
   channel mode. Disable crossfade for the first surround test.
5. Play the spoken sample with the Denon ready. Then switch that player's output
   mode to stereo and replay to check MA's stereo downmix.
