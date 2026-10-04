# MPV backend for Music Assistant

This prototype exposes the small MPD protocol subset used by Music Assistant's
MPD player provider, then sends playback commands to a native `mpv` process over
mpv's private Unix JSON IPC socket. MPV opens the Mac's CoreAudio device directly.

The bridge does not decode audio, resample it, or expose mpv's IPC socket to the
network. It is not a general MPD server: the library browsing and playlist
commands are intentionally absent.

## Requirements

- macOS with `mpv` installed
- The existing native MPD config at `~/.mpd/mpd.conf`, containing the password
  already configured in Music Assistant
- A CoreAudio output device UID; the default value is the Denon AVR UID used in
  this setup

## Run locally

```sh
python3 native-mpv-bridge/bridge.py \
  --listen 127.0.0.1 \
  --port 6601 \
  --audio-device 11EE6600-0000-0000-001D-010380502D78
```

For a local protocol check, point an MPD client to `127.0.0.1:6601`. Use the same
password that is stored in `~/.mpd/mpd.conf`. The bridge reads that credential
from the private file and never logs it.

The bridge currently implements the commands Music Assistant uses: `password`,
`status`, `idle`, `clear`, `add`, `play`, `pause`, `stop`, `seekcur`, `setvol`,
`currentsong`, and `close`. It reports playback state and audio format from MPV.

## Music Assistant network path

Music Assistant sends its stream URL to the MPD endpoint; MPV on the Mac then
fetches that URL. The Mac must be able to reach the advertised stream address
and port from the MA add-on. A container-private URL such as `172.30.33.4:8097`
will not work from the Mac. Expose the MA stream port on the HA host and set its
advertised address to the HA host's LAN address before testing MA playback.

For LAN use, bind the bridge to the Mac's LAN interface and keep the MPD
password enabled. Do not expose the MPV JSON IPC socket: mpv documents that IPC
as unauthenticated and intended for local control.

For this setup, the Mac is `192.168.1.222` and the running MA+ server is
`192.168.1.202`. Start the bridge from the Mac's Terminal session:

```sh
cd ~/Documents/koodi/music-assistant-patched-repo
python3 native-mpv-bridge/bridge.py \
  --listen 192.168.1.222 --port 6601 --verbose
```

In MA+, add `192.168.1.222:6601` under **Settings → Providers → MPD Players**.
Then open the discovered player, complete its password setup, and select it as
the active output. MPV must be able to fetch MA+'s stream from the Mac.

## Current integration check

MA+ has connected to the bridge and authenticated; it sends `clear`, `add`, and
`play`. The MPD control path is therefore working. The bridge's managed agent
session could not fetch the MA stream (`No route to host` for `192.168.1.202:8097`),
even though a direct, header-only `curl` request from the Mac received HTTP 200.
A silent MPV probe from Terminal connected to that host and port successfully;
the root path returned the expected 404. This isolates the failure to the managed
execution session. The bridge is now running from Terminal; retry MA playback
there. The bridge redacts full HTTP URLs from MPV diagnostics.

This is still a prototype and has not been packaged as a LaunchAgent. The MA
connection and MPD control commands are verified; actual MA stream playback
needs a retry through the Terminal-launched bridge.
