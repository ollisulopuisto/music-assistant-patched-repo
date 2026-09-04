# Changelog

Music Assistant, rebuilt from upstream's own release with the patches in
[`patches/`](https://github.com/ollisulopuisto/music-assistant-patched-repo/tree/main/patches)
applied. Each entry names the upstream release it carries and the patches on top
of it.

## 2.10.2-upnext.1

Built from [Music Assistant 2.10.2](https://github.com/music-assistant/server/releases/tag/2.10.2), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go

### Upstream release notes for 2.10.2

#### 📦 Stable Release

_Changes since [2.10.1](https://github.com/music-assistant/server/releases/tag/2.10.1)_

##### 🚀 Features and enhancements

- Align smart playlists similar music with Endless Mixes (by @MarvinSchenkel in #6121)
- Set a global default for the Autoplay and Crossfade switches (by @MarvinSchenkel in #6130)
- Clarify the global Autoplay and crossfade default toggles (by @MarvinSchenkel in #6187)

##### 🐛 Bugfixes

- Fix filesystem scan crash on non-decimal digits in names (by @OzGav in #6102)
- Attach the parent album to imported album tracks (by @OzGav in #6111)
- Default the Fully Kiosk output codec to AAC (by @OzGav in #6112)
- Spotify: skip empty entries when syncing library albums (by @MarvinSchenkel in #6114)
- Fix missing tracks on albums for collaboration tracks in YouTube Music (by @MarvinSchenkel in #6115)
- Sonos speakers now play tracks you add to the queue (by @marcelveldt in #6116)
- Fix BBC Sounds recommendations not loading (by @MarvinSchenkel in #6117)
- Restore pairing token support in Sendspin setup flow (by @meiser79 in #6122)
- Apple Music: don't report purchase-only library items as available (by @anthonws in #6123)
- Clean up sidebar shortcuts when a music provider is removed (by @OzGav in #6124)
- Crossfades no longer shrink to a few seconds on slower sources (by @marcelveldt in #6128)
- Newly created tokens now show up in the token list (by @marcelveldt in #6131)
- Fix various issues with enqueuing the next track (by @marcelveldt in #6132)
- Fix raw PCM input being decoded with the source codec (by @OzGav in #6137)
- Fix crossfade on enqueue-capable speakers (like Sonos) when audio source is Spotify through Soloist (by @marcelveldt in #6141)
- AI DJ no longer goes quiet after the queue is cleared (by @MarvinSchenkel in #6142)
- Crossfade setting changes now apply at the next track on flow mode players (by @MarvinSchenkel in #6143)
- Keep core/tasks parsable when the scheduler persists its state (by @OzGav in #6145)
- Show why a Podcast Index login or episode lookup failed (by @OzGav in #6146)
- Fix BBC Sounds sometimes using library ID instead of provider ID for listenting status update (by @kieranhogg in #6150)
- Use artist top tracks when sampling genre and dynamic radio seeds (by @jozefKruszynski in #6155)
- Fix Internet Archive search missing Live Music Archive content (by @OzGav in #6157)
- Seeking within a track on Sonos now takes effect right away (by @marcelveldt in #6158)
- Allow up to 3 concurrent YouTube Music streams (by @MarvinSchenkel in #6160)
- Show library tracks in the Recently played playlist (by @MarvinSchenkel in #6161)
- Fix leaked aiohttp session when an AirPlay control connection drops (by @MarvinSchenkel in #6162)
- Fix broken nl-NL Alexa invocation phrase (by @R3inoudR in #6164)
- Deezer: fix multiple instances sharing the same account (by @jdaberkow in #6169)
- Skip a Spotify track Spotify refuses, instead of logging a crash (by @marcelveldt in #6171)
- Cheaper track changes: Spotify Soloist advertises its real single-stream limit (by @marcelveldt in #6172)
- Deezer: fix seeking landing short of the requested position (by @jdaberkow in #6174)
- Fix spotify soloist new download (by @aauren in #6176)
- AirPlay: fall back to the default port when discovery has no port (by @MarvinSchenkel in #6185)
- Make Music Trivia title questions answerable (by @MarvinSchenkel in #6189)
- Set Home for PulseAudio (by @aauren in #6190)

##### 🧰 Maintenance and dependency bumps

- Treat the iBroadcast library the same as others that contain a user's tracks (by @OzGav in #6147)
- Quieter track changes: don't warn when the next track has to wait for a free Spotify slot (by @marcelveldt in #6170)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @R3inoudR, @aauren, @anthonws, @chrisuthe, @jdaberkow, @jozefKruszynski, @kieranhogg, @marcelveldt, @meiser79

## 2.10.1-upnext.1

Built from [Music Assistant 2.10.1](https://github.com/music-assistant/server/releases/tag/2.10.1), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go

## 2.10.0-upnext.4

Built from [Music Assistant 2.10.0](https://github.com/music-assistant/server/releases/tag/2.10.0), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
