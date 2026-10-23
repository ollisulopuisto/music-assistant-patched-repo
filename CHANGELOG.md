# Changelog

What each published version of the **Music Assistant+** add-on changed, for whoever
promotes it. Versions follow the add-on's own scheme, `<upstream>-upnext.<build>`.
The add-on's per-release patch list and upstream notes are in
[`music-assistant-upnext-test/CHANGELOG.md`](music-assistant-upnext-test/CHANGELOG.md),
which the build writes.

## [Unreleased]

- Upstream 2.10.7: `0011-now-playing-details.patch` re-based on `music_assistant/controllers/player_queues/controller.py` where upstream refactored media item handling into `if media_item := queue_item.media_item:` and added podcast/album handling; all server and frontend patches apply cleanly.
- Build workflow: automatically comment on and close any open `build-failure` issue when the publish job succeeds, and set `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"` across workflows.

Upstream 2.10.6 (9.10.2026): `0122-preserve-dsd-stereo-downmix.patch` re-based, its `test_ffmpeg.py` hunk no longer applied; all 14 server and 4 frontend patches apply and the affected tests pass on 2.10.6.

Waiting for the next publish build (patches are committed, not pushed):

- An album from a media server (Navidrome) showed a blank cover after the server's library was rescanned. The rescan gave the album a new id, the library item matched by name kept the old cover id next to the new one (images were merged into one list), and the dead old id came first: the server answered "not found" for every size that was not already cached (the 80 px thumbnail still showed, from the image cache). A provider's new artwork now replaces the artwork it gave before; other providers' artwork is kept (server 0125). The stored list is corrected the next time the provider's albums are synced; a queue built before the rescan keeps the old ids until it is cleared and filled again. Not tried against a live Navidrome.

- Multichannel changes (0120) broke 19 upstream stream tests on 2.10.7: `arriving_audio_format` assumed every stream record has `decoded_audio_format`, and a record that is not a full `StreamDetails` raised `AttributeError` in the flow format and restart checks. It now falls back to the claimed format (server 0124). Two `test_audio_analysis` tests still fail with 0120 (they hand the analysis worker a mock buffer whose `pcm_format` cannot be compared); `test_filtergraph_complex_runs_in_ffmpeg` fails without our patches too (the local FFmpeg lacks `afir irnorm`).

- Performance pass over our own patches (server 0015-0017, frontend 0011-0013); upstream code untouched:
  - A big playlist is read once per visit instead of once per 50-item page. For 5000 Spotify tracks each page cost about 0.2 s of server event loop plus a database read per provider page, so scrolling to the end cost about 16 s; the count sent with the first page read it once more, and a refresh fetched the playlist from Spotify twice. Items are now kept in memory for 90 s (two playlists at most), overlapping requests share one read, sorted views are built once, and editing a playlist clears what was kept.
  - Sleep timer: paused near a track end, a boundary timer re-armed itself about twice a second and sent a player update to every client each time. Paused, it now checks back every 5 s quietly; stopped playback ends it. The queue is read only as far as the mode needs.
  - Now-playing dashboard: idle close now watches the player the dashboard shows. A dashboard showing a group or another speaker was timed against the Cast device's own (idle) playback and would have closed mid-music. With idle close at 0 the dashboards no longer follow player updates.
  - Now-playing dashboard: without an artist portrait the cover was loaded twice and drawn over itself; the 60 fps lyrics clock ran for every track, lyrics or not (a constant load on a Chromecast); a late lyrics answer after a skip could replace the current track's lyrics.
  - Listings: plain-text descriptions (radio, playlist, podcast episode rows) were re-parsed through markdown, DOMPurify and a DOM parser on every row render, about a millisecond each; now kept per text.
  - After an A-Z jump the list view keeps every loaded page in the document; off-screen rows are now skipped by the browser (`content-visibility: auto`). Not tried in a browser.

- Sleep timer can stop at a boundary instead of after a fixed time: the end of the playing track (or chapter, in an audiobook), the end of the playing album, or "finish within" 15 to 120 minutes, which stops after the last track or chapter that ends inside that time (a 30 minute budget over four-minute tracks stops after seven). If no boundary fits the time, it is an ordinary countdown. A pause during the countdown moves the stop; the timer looks again when it fires. Server command `players/sleep_timer/set` takes a new `mode` (`duration`, `track_end`, `album_end`, `fit`); the countdown shows the expected stop. Server 0014, frontend 0010. Not tried on a device: the stop may cut up to about a second off the end of the track.

- A-Z strip on the library playlists listing (Soittolistat), like artists and albums. Playlists mirrored from Spotify number in the hundreds. Not tried in a browser.

- Loudness Analysis can now be disabled (Settings > Audio analysis > Loudness Analysis > Disable). It reads whole files through the media server, and the user does not use volume normalisation. Tracks that already have stored loudness keep it.

- A-Z strip on a playlist's tracks when sorted by name (jump to a letter, scroll up and down from it), same strip as artists and albums.

- Opening a big playlist no longer loads every track at once. The contents load 50 at a
  time from a new server command, `music/playlists/playlist_tracks_page`, in the chosen
  order and with the search text. Untested in a browser: the scroll loading needs a look
  on the running add-on. Album-disc grouping is off in that view.

- Spotify Soloist: a capture that goes quiet is logged at debug level after 5 s (engine
  state, sink state, cushion fill), and again when the silence ends. Diagnostic only; playback
  is unchanged. Adds a test that Soloist's own 30 s stall guard fires before the stream's
  20 s watchdog. That test fails until the timeout is decided. Not tried on the add-on.

- A now-playing dashboard on a Chromecast is closed, and the receiver app quit, once nothing has
  played on the device for 30 minutes (server 0013). A Cast receiver loops its keepalive video
  for as long as a dashboard is open, and each restart of it woke an amplifier wired to the
  bedroom device all night. The time is a Chromecast provider setting, "Close the now-playing
  dashboard when idle (minutes)", default 30, and 0 keeps dashboards open. Party and quiz
  dashboards are left alone. Taking effect needs a provider reload. The keepalive itself is
  played by the receiver app (hosted by Music Assistant), so it cannot be switched off from the
  server. Not tried on a device.

- A-Z strip on a playlist sorted by artist or album (frontend 0009, server 0012): a jump to K means
  artists (or albums) starting with K, not track titles. The server files each item under the
  name the order follows, with the same accent folding as the sort, and gets the descending
  forms artist_desc and album_desc so the listing can page upwards from a jump. Library
  listings keep to the name orders. Not tried in a browser.

- Now-playing dashboard redesign (frontend 0008): the portrait fills the left half of the screen
  edge to edge and fades into the background, with the album cover as a thumbnail on it; text,
  lyrics and timeline sit on the right. The picture is requested at 1024 px so it is sharp, the
  lyrics are scaled to the column, and titles use Syne with Outfit for the rest (both embedded,
  SIL OFL 1.1). Needs an HTTPS Base URL on the MA server for the Cast dashboard to load this
  frontend at all (Settings > Core > Web server > Internal URL); through Remote Access the
  Chromecast loads the official dashboard instead. Layout checked in a static render, not on a TV.

- Now-playing dashboard: the artwork is the artist's portrait (album art when there is none),
  sized to cover about half a 16:9 screen, with the text and timeline beside it in landscape.
  Under the title it shows the stream format (codec, sample rate, bit depth for lossless,
  bitrate), and it shows the track's lyrics, fetched once per track. Needs server patch 0011,
  which puts the format and artist image into the media's custom data. Not tried on a TV yet;
  the lyrics clock is untested in a browser.

- Numbered jump strip on a playlist sorted by position: 1  51  101 and so on, one chip per
  page of 50. A tap loads from that offset and scrolls to it, and scrolling on continues
  from there. Shown only for playlists longer than 50 items, and hidden while a search is
  active. The default sort stays position. Needs a new server command,
  `music/playlists/playlist_tracks_count`, which reads the whole playlist once to count it.
  Not tried in a browser. Known gaps: the strip shows every chip in one scrolling row, not
  a shortened "+" form; the lit chip is the last one tapped, not the one in view; and
  "select all" after a jump selects only from that page onwards.

- "Select all" on a paged playlist now asks for confirmation above 250 items, because the
  playlist's total is known. Not tried in a browser.

Repository and tooling only; none of this changes the add-on image.

- Licensed under Apache-2.0 (matching upstream). Patches to Navidrome stay GPL-3.0
  and patches to MPD stay GPL-2.0-or-later, as derivative works.
- Navidrome patch for serving DTS multichannel files with correct metadata
  (`patches/navidrome/`).
- The publish build now rebases before pushing the version bump, so a push to
  `main` during a build no longer leaves the add-on on the previous version.
- Only `patches/server/` and `patches/frontend/` changes start a publish build.
- New publish gate: a regression test that MPD players offer multichannel output
  and 96/192 kHz 24-bit rates (patch 0123).
- Native MPD build for the Mac, Denon audio-format watcher, HAOS multichannel
  test app, 5.1 channel-identification test media, and multichannel docs.
- The prototype MPD-to-mpv bridge moved to its own repo, `ma-mpv-player`.

## [2.10.5-upnext.2] - 2026-10-04

Image published, but the add-on was never pointed at it (the build's push lost a
race). Identical to 2.10.5-upnext.1; skip it.

## [2.10.5-upnext.1] - 2026-10-02

- Upstream 2.10.5.
- HVSC: tracks carry scrobble-ready metadata.
- DSD multichannel patch rebased onto 2.10.5.

## [2.10.4-upnext.20] - 2026-10-02

- HVSC: the SID fade-out stream is now included in the provider.

## [2.10.4-upnext.19] - 2026-10-02

- HVSC renders at 48 kHz and lets MA adapt to each player; sample rate is a setting.
- HVSC local SID path is optional.
- Looped SID tunes fade out at the configured track limit; disabling fade is honoured.

## [2.10.4-upnext.18] - 2026-10-02

- HVSC tunes render with upstream SIDLite; configurable stereo widening.

## [2.10.4-upnext.17] - 2026-10-02

- HVSC browse paths fixed.

## [2.10.4-upnext.16] - 2026-10-01

- HVSC provider no longer fails on a ConfigEntry attribute error.

## [2.10.4-upnext.15] - 2026-10-01

- New High Voltage SID Collection (HVSC) music provider.

## [2.10.4-upnext.14] - 2026-09-28

- MPD players can be set to multichannel output.

## [2.10.4-upnext.13] - 2026-09-27

- Random-ordered library listings no longer fail with a NameError.

## [2.10.4-upnext.12] - 2026-09-27

- Multichannel PCM is preserved end to end, and DSD is converted safely
  (stereo and multichannel).

## [2.10.4-upnext.11] - 2026-09-25

- The Music Assistant panel is shown to standard (non-admin) HA users.

## [2.10.4-upnext.10] - 2026-09-25

- A-Z browsing for podcasts.

## [2.10.4-upnext.9] - 2026-09-25

- Scrolling back up in a jumped A-Z list view loads the earlier pages correctly.

## [2.10.4-upnext.8] - 2026-09-25

- A-Z paging disabled for audiobooks, where it was unreliable.

## [2.10.4-upnext.7] - 2026-09-24

- Radio A-Z jump fixed; views where the jump was unreliable no longer show the strip.

## [2.10.4-upnext.6] - 2026-09-24

- The A-Z jump lands on the letter's first item, also in descending order; the
  listing header stays pinned.

## [2.10.4-upnext.5] - 2026-09-24

- The A-Z strip follows the scroll. The add-on is renamed Music Assistant+.

## [2.10.4-upnext.4] - 2026-09-24

- A jumped listing can be scrolled back up; the A-Z strip is pinned.

## [2.10.4-upnext.3] - 2026-09-23

- Picking a letter jumps to it instead of filtering the list.

## [2.10.4-upnext.2] - 2026-09-23

- First-letter navigation for library listings.

## [2.10.4-upnext.1] - 2026-09-18

- Upstream 2.10.4.

## [2.10.3-upnext.1] - 2026-09-12

- Upstream 2.10.3.

## [2.10.2-upnext.1] - 2026-09-04

- Upstream 2.10.2. HA's update dialog now shows what is in each update.

## [2.10.1-upnext.1] - 2026-08-29

- Upstream 2.10.1. The build checks for upstream releases daily instead of weekly.

## [2.10.0-upnext.4] - 2026-08-28

- Podcast episode subtitles no longer show raw feed markup.

## [2.10.0-upnext.3] - 2026-08-28

- A user-supplied `app_vars.json` in the add-on data directory is used.

## [2.10.0-upnext.2] - 2026-08-28

- Ingress sign-in fixed; the add-on has an icon.

## [2.10.0-upnext.1] - 2026-08-27

- First build from upstream stable 2.10.0 with the Pocket Casts Up Next patches.

## Audiobookshelf add-on

- 2.37.1 (2026-09-30), 2.37.0 (2026-09-29), 2.36.1 (2026-09-17), and 2.36.0
  (2026-08-29, first version).
