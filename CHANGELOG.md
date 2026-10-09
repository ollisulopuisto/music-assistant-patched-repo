# Changelog

What each published version of the **Music Assistant+** add-on changed, for whoever
promotes it. Versions follow the add-on's own scheme, `<upstream>-upnext.<build>`.
The add-on's per-release patch list and upstream notes are in
[`music-assistant-upnext-test/CHANGELOG.md`](music-assistant-upnext-test/CHANGELOG.md),
which the build writes.

## [Unreleased]

Upstream 2.10.6 (9.10.2026): `0122-preserve-dsd-stereo-downmix.patch` re-based, its `test_ffmpeg.py` hunk no longer applied; all 14 server and 4 frontend patches apply and the affected tests pass on 2.10.6.

Waiting for the next publish build (patches are committed, not pushed):

- A-Z strip on a playlist's tracks when sorted by name (jump to a letter, scroll up and down from it), same strip as artists and albums.

- Opening a big playlist no longer loads every track at once. The contents load 50 at a
  time from a new server command, `music/playlists/playlist_tracks_page`, in the chosen
  order and with the search text. Untested in a browser: the scroll loading needs a look
  on the running add-on. Not covered: "select all" on a paged playlist skips its
  confirmation prompt (the total is unknown), and album-disc grouping is off in that view.

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
