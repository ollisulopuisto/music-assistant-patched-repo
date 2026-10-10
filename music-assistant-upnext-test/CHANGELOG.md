# Changelog

Music Assistant, rebuilt from upstream's own release with the patches in
[`patches/`](https://github.com/ollisulopuisto/music-assistant-patched-repo/tree/main/patches)
applied. Each entry names the upstream release it carries and the patches on top
of it.

## 2.10.6-upnext.2

Built from [Music Assistant 2.10.6](https://github.com/music-assistant/server/releases/tag/2.10.6), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Let a layout file drop duplicate recommendation rows, hide
- **server** — Add a paged playlist contents command
- **server** — Let loudness analysis be disabled
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **server** — Preserve multichannel PCM and convert DSD safely
- **server** — Recognize DFF streams as DSD for PCM buffer accounting
- **server** — Preserve direct DSD stereo downmix gain
- **server** — Test MPD high-resolution multichannel settings
- **server** — Add HVSC SID rendering provider with stereo widening
- **server** — Build the upstream sidplayfp CLI with SIDLite for the runtime image
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings
- **frontend** — Page a playlist's tracks from the server, with an A-Z strip

### Upstream release notes for 2.10.6

#### 📦 Stable Release

_Changes since [2.10.5](https://github.com/music-assistant/server/releases/tag/2.10.5)_

##### 🚀 Features and enhancements

- Run manually triggered tasks next in the background task queue (by @OzGav in #6764)

##### 🐛 Bugfixes

- Fix queue stalling after one track when current item is briefly unset (by @bcl79 in #6110)
- Pause, resume and skip Spotify Connect on DLNA speakers (by @MarvinSchenkel in #6609)
- Keep HEOS players playing while they restart on a new stream (by @MarvinSchenkel in #6611)
- Fix parsing of artists in YouTube Music recommendations (by @NasaGeek in #6677)
- Pick provider mappings by availability and priority in _select_provider_id (stable) (by @OzGav in #6679)
- Stop placeholder ISRCs from merging unrelated tracks (by @OzGav in #6691)
- Keep the last played position when a player pauses (by @fmunkes in #6693)
- Stop Apple Music from adding empty duplicates of albums that lack a catalog link (by @MarvinSchenkel in #6702)
- Fix sync group picking a lights-only member as leader (by @MarvinSchenkel in #6707)
- Play Sendspin audio at the music's own sample rate (by @marcelveldt in #6709)
- Drop thumbnails from YouTube Music less frequently (by @NasaGeek in #6721)
- Keep favorite tracks of multiple Tidal accounts apart in the library (by @MarvinSchenkel in #6726)
- Fix audiobooks not starting when resuming deep into a long mp3 (by @MarvinSchenkel in #6727)
- Fix personalized NetEase endpoints returning wrong data on some NCM API backends (by @Kiranwin in #6730)
- Revoke guest access when the party or music quiz plugin is disabled (by @MarvinSchenkel in #6747)
- Bind the playlog lookup parameters (by @MarvinSchenkel in #6751)
- Deezer: Fix Family profiles showing the admin's library (by @jdaberkow in #6753)
- Refuse CIFS usernames and shares that would add mount options (by @MarvinSchenkel in #6756)
- Fix Sendspin players not marking items played when playback starts near the end (by @maximmaxim345 in #6770)
- Restrict what the image loader hands to ffmpeg (by @MarvinSchenkel in #6771)
- Require the Supervisor as peer for Home Assistant Ingress requests (by @MarvinSchenkel in #6772)
- Show Apple Music names in the user's language (by @MarvinSchenkel in #6775)
- Stop a Sonos from playing music again after the queue has finished (by @marcelveldt in #6782)
- Fix album covers not loading when archive.org is slow or down (by @OzGav in #6787)

##### Other Changes

- Only allow releases to be started from the dev branch (stable) (by @marcelveldt in #6674)

##### 🧰 Maintenance and dependency bumps

- Fix release notes listing changes that did not ship in a stable patch release (by @marcelveldt in #6672)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@Kiranwin, @MarvinSchenkel, @NasaGeek, @OzGav, @bcl79, @fmunkes, @jdaberkow, @marcelveldt, @maximmaxim345

## 2.10.6-upnext.1

Built from [Music Assistant 2.10.6](https://github.com/music-assistant/server/releases/tag/2.10.6), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Let a layout file drop duplicate recommendation rows, hide
- **server** — Add a paged playlist contents command
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **server** — Preserve multichannel PCM and convert DSD safely
- **server** — Recognize DFF streams as DSD for PCM buffer accounting
- **server** — Preserve direct DSD stereo downmix gain
- **server** — Test MPD high-resolution multichannel settings
- **server** — Add HVSC SID rendering provider with stereo widening
- **server** — Build the upstream sidplayfp CLI with SIDLite for the runtime image
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings
- **frontend** — Page a playlist's tracks from the server, with an A-Z strip

### Upstream release notes for 2.10.6

#### 📦 Stable Release

_Changes since [2.10.5](https://github.com/music-assistant/server/releases/tag/2.10.5)_

##### 🚀 Features and enhancements

- Run manually triggered tasks next in the background task queue (by @OzGav in #6764)

##### 🐛 Bugfixes

- Fix queue stalling after one track when current item is briefly unset (by @bcl79 in #6110)
- Pause, resume and skip Spotify Connect on DLNA speakers (by @MarvinSchenkel in #6609)
- Keep HEOS players playing while they restart on a new stream (by @MarvinSchenkel in #6611)
- Fix parsing of artists in YouTube Music recommendations (by @NasaGeek in #6677)
- Pick provider mappings by availability and priority in _select_provider_id (stable) (by @OzGav in #6679)
- Stop placeholder ISRCs from merging unrelated tracks (by @OzGav in #6691)
- Keep the last played position when a player pauses (by @fmunkes in #6693)
- Stop Apple Music from adding empty duplicates of albums that lack a catalog link (by @MarvinSchenkel in #6702)
- Fix sync group picking a lights-only member as leader (by @MarvinSchenkel in #6707)
- Play Sendspin audio at the music's own sample rate (by @marcelveldt in #6709)
- Drop thumbnails from YouTube Music less frequently (by @NasaGeek in #6721)
- Keep favorite tracks of multiple Tidal accounts apart in the library (by @MarvinSchenkel in #6726)
- Fix audiobooks not starting when resuming deep into a long mp3 (by @MarvinSchenkel in #6727)
- Fix personalized NetEase endpoints returning wrong data on some NCM API backends (by @Kiranwin in #6730)
- Revoke guest access when the party or music quiz plugin is disabled (by @MarvinSchenkel in #6747)
- Bind the playlog lookup parameters (by @MarvinSchenkel in #6751)
- Deezer: Fix Family profiles showing the admin's library (by @jdaberkow in #6753)
- Refuse CIFS usernames and shares that would add mount options (by @MarvinSchenkel in #6756)
- Fix Sendspin players not marking items played when playback starts near the end (by @maximmaxim345 in #6770)
- Restrict what the image loader hands to ffmpeg (by @MarvinSchenkel in #6771)
- Require the Supervisor as peer for Home Assistant Ingress requests (by @MarvinSchenkel in #6772)
- Show Apple Music names in the user's language (by @MarvinSchenkel in #6775)
- Stop a Sonos from playing music again after the queue has finished (by @marcelveldt in #6782)
- Fix album covers not loading when archive.org is slow or down (by @OzGav in #6787)

##### Other Changes

- Only allow releases to be started from the dev branch (stable) (by @marcelveldt in #6674)

##### 🧰 Maintenance and dependency bumps

- Fix release notes listing changes that did not ship in a stable patch release (by @marcelveldt in #6672)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@Kiranwin, @MarvinSchenkel, @NasaGeek, @OzGav, @bcl79, @fmunkes, @jdaberkow, @marcelveldt, @maximmaxim345

## 2.10.5-upnext.4

Built from [Music Assistant 2.10.5](https://github.com/music-assistant/server/releases/tag/2.10.5), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Let a layout file drop duplicate recommendation rows, hide
- **server** — Add a paged playlist contents command
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **server** — Preserve multichannel PCM and convert DSD safely
- **server** — Recognize DFF streams as DSD for PCM buffer accounting
- **server** — Preserve direct DSD stereo downmix gain
- **server** — Test MPD high-resolution multichannel settings
- **server** — Add HVSC SID rendering provider with stereo widening
- **server** — Build the upstream sidplayfp CLI with SIDLite for the runtime image
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings
- **frontend** — Page a playlist's tracks from the server, with an A-Z strip

### Upstream release notes for 2.10.5

#### 📦 Stable Release

_Changes since [2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4)_

##### 🐛 Bugfixes

- Fix OpenSubsonic credential preservation during reconfiguration (by @teancom in #6376)
- Stop the audio analysis background scan from spawning a task per track (by @balloobbot in #6384)
- Update py-opensonic to 10.4.1 (by @khers in #6388)
- Fix announcements on a speaker group playing out of sync (by @marcelveldt in #6392)
- Remove stale author/narrator links when an audiobook is overwritten (by @fmunkes in #6397)
- Fix shuffle/repeat failing on players playing a dynamic mix (by @marcelveldt in #6404)
- Move the ibroadcast item mapping to strings only (by @robsonke in #6405)
- Fix false permission error opening an artist page (by @marcelveldt in #6411)
- Updates token management to allow PlexHome users to import their own libraries (by @romain38 in #6426)
- Keep the stale mapping pass from emptying a library on mismatched ids (by @RyanAtTanagra in #6427)
- Fix resume position after fallback announcements (by @sickkick in #6429)
- Fix Snapcast volume/mute routing to idle native player when Sendspin is active (by @tortfeaser in #6432)
- Fix YTMusic album resolution crash on null audioPlaylistId (by @frosty-geek in #6435)
- Fix external auth consent banner being hidden by ad-blocker filters (by @lanquarden in #6443)
- Keep one failing provider from aborting album, artist and genre playback (by @teancom in #6446)
- Attribute synced progress to the reporting provider instance (by @fmunkes in #6450)
- Stop a group's queue when it is powered off outside Music Assistant (by @marcelveldt in #6452)
- Skip CUE sheets with a missing audio file when browsing (by @OzGav in #6463)
- Reconnect radio streams that go silent before playback gives up (by @OzGav in #6466)
- Allow a speaker to rejoin a group right after the group broke up (by @marcelveldt in #6473)
- Fix a speaker group going silent when one room is powered off while another joins (by @marcelveldt in #6474)
- Link ARD Audiothek episodes to their own podcast (by @OzGav in #6488)
- Fix Spotify dropping out on Sonos after resuming near the end of a track (by @marcelveldt in #6497)
- Keep manually linked genres when a music provider syncs (by @MarvinSchenkel in #6499)
- Only defer the next-track preload for realtime single-stream sources (by @marcelveldt in #6500)
- Fix an idle sync group dissolving in the middle of a member change (by @marcelveldt in #6501)
- Stop Apple Music from adding empty albums whose songs were withdrawn from the catalog (by @MarvinSchenkel in #6502)
- Resume audiobooks and podcast episodes at their saved position when the queue moves on (by @MarvinSchenkel in #6503)
- Acquire the narrators from book metadata in Audiobookshelf (by @fmunkes in #6504)
- Fix an announcement or play command on a grouped speaker locking up during a group change (by @marcelveldt in #6505)
- Fix a play command on a synced speaker locking up during a group change (by @marcelveldt in #6510)
- Fix Nicovideo feed artists not matching library items (by @marcelveldt in #6511)
- Fix Plex login for users the server is shared with (by @aevans0001 in #6513)
- Keep the library's housekeeping state when the music settings are saved (by @marcelveldt in #6514)
- Stop Cast flow playback from skipping an extra track after pressing next (by @MarvinSchenkel in #6518)
- Keep task schedules and run history when saving the Tasks settings (by @marcelveldt in #6522)
- Keep a group playing when the speaker leading it is powered off (by @marcelveldt in #6525)
- Fix static on Squeezelite sync groups when playing live sources like the AirPlay Receiver (by @MarvinSchenkel in #6529)
- Fix external playback not tracked after a player leaves a Sendspin group (by @MarvinSchenkel in #6530)
- Keep the WiiM queue on the right track when an event is missed (by @MarvinSchenkel in #6532)
- Keep filling a seed pool past one unproductive radio batch (by @balloob in #6535)
- Don't flag cleanly finished HTTP audio streams as failed (by @MarvinSchenkel in #6536)
- Fix filesystem sync not removing deleted files with an uppercase extension (by @OzGav in #6539)
- Fix scrobblers submitting a track twice (by @MarvinSchenkel in #6556)
- Keep DLNA players available when firmware sends a wrong Content-Length (by @MarvinSchenkel in #6557)
- Fix YouTube Music album versions failing on a zero-height thumbnail (by @MarvinSchenkel in #6561)
- Fix crossfades turning into hard cuts on players that buffer far ahead (by @marcelveldt in #6569)
- Honor HTTP proxy environment variables (by @MarvinSchenkel in #6572)
- Fix a stopped queue keeping a stream open at the music source (by @marcelveldt in #6573)
- Keep a track playable when its music source has no free stream (by @marcelveldt in #6576)
- Fix a paused player keeping its music source busy for minutes (by @marcelveldt in #6577)
- Fix Spotify app pairing not finding the device on hosts with Docker networks (by @MarvinSchenkel in #6578)
- Show Spotify top tracks when a custom client ID is set (by @marcelveldt in #6583)
- Fix Bandcamp requests returning an HTML challenge page instead of JSON (by @MarvinSchenkel in #6592)
- Deezer: fix resume from other devices and a missing timeout (by @jdaberkow in #6596)
- Resolve the current TuneIn stream url at playback time (by @MarvinSchenkel in #6606)
- Stop playback jumping back to the first track when a player reconnects (by @marcelveldt in #6608)
- Fix a universal player getting a new id on every restart (by @MarvinSchenkel in #6610)
- Show Spotify new releases and genres when a custom client ID is set (by @marcelveldt in #6615)
- Keep YouTube Music searches out of your YouTube search history (by @MarvinSchenkel in #6643)

##### Other Changes

- Fix Sonos speakers getting stuck on the wrong playback state (by @marcelveldt in #6395)

##### 🧰 Maintenance and dependency bumps

- Update various code owners (by @OzGav in #6485)
- Update aioslimproto to 3.2.3 (by @MarvinSchenkel in #6570)
- Update airplay-cli to v0.5.5 (by @musicassistant-bot[bot] in #6637)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @RyanAtTanagra, @aevans0001, @balloob, @balloobbot, @fmunkes, @frosty-geek, @jdaberkow, @khers, @lanquarden, @marcelveldt, @robsonke, @romain38, @sickkick, @teancom, @tortfeaser

## 2.10.5-upnext.3

Built from [Music Assistant 2.10.5](https://github.com/music-assistant/server/releases/tag/2.10.5), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Let a layout file drop duplicate recommendation rows, hide
- **server** — Add a paged playlist contents command
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **server** — Preserve multichannel PCM and convert DSD safely
- **server** — Recognize DFF streams as DSD for PCM buffer accounting
- **server** — Preserve direct DSD stereo downmix gain
- **server** — Test MPD high-resolution multichannel settings
- **server** — Add HVSC SID rendering provider with stereo widening
- **server** — Build the upstream sidplayfp CLI with SIDLite for the runtime image
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings
- **frontend** — Page a playlist's tracks from the server

### Upstream release notes for 2.10.5

#### 📦 Stable Release

_Changes since [2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4)_

##### 🐛 Bugfixes

- Fix OpenSubsonic credential preservation during reconfiguration (by @teancom in #6376)
- Stop the audio analysis background scan from spawning a task per track (by @balloobbot in #6384)
- Update py-opensonic to 10.4.1 (by @khers in #6388)
- Fix announcements on a speaker group playing out of sync (by @marcelveldt in #6392)
- Remove stale author/narrator links when an audiobook is overwritten (by @fmunkes in #6397)
- Fix shuffle/repeat failing on players playing a dynamic mix (by @marcelveldt in #6404)
- Move the ibroadcast item mapping to strings only (by @robsonke in #6405)
- Fix false permission error opening an artist page (by @marcelveldt in #6411)
- Updates token management to allow PlexHome users to import their own libraries (by @romain38 in #6426)
- Keep the stale mapping pass from emptying a library on mismatched ids (by @RyanAtTanagra in #6427)
- Fix resume position after fallback announcements (by @sickkick in #6429)
- Fix Snapcast volume/mute routing to idle native player when Sendspin is active (by @tortfeaser in #6432)
- Fix YTMusic album resolution crash on null audioPlaylistId (by @frosty-geek in #6435)
- Fix external auth consent banner being hidden by ad-blocker filters (by @lanquarden in #6443)
- Keep one failing provider from aborting album, artist and genre playback (by @teancom in #6446)
- Attribute synced progress to the reporting provider instance (by @fmunkes in #6450)
- Stop a group's queue when it is powered off outside Music Assistant (by @marcelveldt in #6452)
- Skip CUE sheets with a missing audio file when browsing (by @OzGav in #6463)
- Reconnect radio streams that go silent before playback gives up (by @OzGav in #6466)
- Allow a speaker to rejoin a group right after the group broke up (by @marcelveldt in #6473)
- Fix a speaker group going silent when one room is powered off while another joins (by @marcelveldt in #6474)
- Link ARD Audiothek episodes to their own podcast (by @OzGav in #6488)
- Fix Spotify dropping out on Sonos after resuming near the end of a track (by @marcelveldt in #6497)
- Keep manually linked genres when a music provider syncs (by @MarvinSchenkel in #6499)
- Only defer the next-track preload for realtime single-stream sources (by @marcelveldt in #6500)
- Fix an idle sync group dissolving in the middle of a member change (by @marcelveldt in #6501)
- Stop Apple Music from adding empty albums whose songs were withdrawn from the catalog (by @MarvinSchenkel in #6502)
- Resume audiobooks and podcast episodes at their saved position when the queue moves on (by @MarvinSchenkel in #6503)
- Acquire the narrators from book metadata in Audiobookshelf (by @fmunkes in #6504)
- Fix an announcement or play command on a grouped speaker locking up during a group change (by @marcelveldt in #6505)
- Fix a play command on a synced speaker locking up during a group change (by @marcelveldt in #6510)
- Fix Nicovideo feed artists not matching library items (by @marcelveldt in #6511)
- Fix Plex login for users the server is shared with (by @aevans0001 in #6513)
- Keep the library's housekeeping state when the music settings are saved (by @marcelveldt in #6514)
- Stop Cast flow playback from skipping an extra track after pressing next (by @MarvinSchenkel in #6518)
- Keep task schedules and run history when saving the Tasks settings (by @marcelveldt in #6522)
- Keep a group playing when the speaker leading it is powered off (by @marcelveldt in #6525)
- Fix static on Squeezelite sync groups when playing live sources like the AirPlay Receiver (by @MarvinSchenkel in #6529)
- Fix external playback not tracked after a player leaves a Sendspin group (by @MarvinSchenkel in #6530)
- Keep the WiiM queue on the right track when an event is missed (by @MarvinSchenkel in #6532)
- Keep filling a seed pool past one unproductive radio batch (by @balloob in #6535)
- Don't flag cleanly finished HTTP audio streams as failed (by @MarvinSchenkel in #6536)
- Fix filesystem sync not removing deleted files with an uppercase extension (by @OzGav in #6539)
- Fix scrobblers submitting a track twice (by @MarvinSchenkel in #6556)
- Keep DLNA players available when firmware sends a wrong Content-Length (by @MarvinSchenkel in #6557)
- Fix YouTube Music album versions failing on a zero-height thumbnail (by @MarvinSchenkel in #6561)
- Fix crossfades turning into hard cuts on players that buffer far ahead (by @marcelveldt in #6569)
- Honor HTTP proxy environment variables (by @MarvinSchenkel in #6572)
- Fix a stopped queue keeping a stream open at the music source (by @marcelveldt in #6573)
- Keep a track playable when its music source has no free stream (by @marcelveldt in #6576)
- Fix a paused player keeping its music source busy for minutes (by @marcelveldt in #6577)
- Fix Spotify app pairing not finding the device on hosts with Docker networks (by @MarvinSchenkel in #6578)
- Show Spotify top tracks when a custom client ID is set (by @marcelveldt in #6583)
- Fix Bandcamp requests returning an HTML challenge page instead of JSON (by @MarvinSchenkel in #6592)
- Deezer: fix resume from other devices and a missing timeout (by @jdaberkow in #6596)
- Resolve the current TuneIn stream url at playback time (by @MarvinSchenkel in #6606)
- Stop playback jumping back to the first track when a player reconnects (by @marcelveldt in #6608)
- Fix a universal player getting a new id on every restart (by @MarvinSchenkel in #6610)
- Show Spotify new releases and genres when a custom client ID is set (by @marcelveldt in #6615)
- Keep YouTube Music searches out of your YouTube search history (by @MarvinSchenkel in #6643)

##### Other Changes

- Fix Sonos speakers getting stuck on the wrong playback state (by @marcelveldt in #6395)

##### 🧰 Maintenance and dependency bumps

- Update various code owners (by @OzGav in #6485)
- Update aioslimproto to 3.2.3 (by @MarvinSchenkel in #6570)
- Update airplay-cli to v0.5.5 (by @musicassistant-bot[bot] in #6637)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @RyanAtTanagra, @aevans0001, @balloob, @balloobbot, @fmunkes, @frosty-geek, @jdaberkow, @khers, @lanquarden, @marcelveldt, @robsonke, @romain38, @sickkick, @teancom, @tortfeaser

## 2.10.5-upnext.2

Built from [Music Assistant 2.10.5](https://github.com/music-assistant/server/releases/tag/2.10.5), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Let a layout file drop duplicate recommendation rows, hide
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **server** — Preserve multichannel PCM and convert DSD safely
- **server** — Recognize DFF streams as DSD for PCM buffer accounting
- **server** — Preserve direct DSD stereo downmix gain
- **server** — Test MPD high-resolution multichannel settings
- **server** — Add HVSC SID rendering provider with stereo widening
- **server** — Build the upstream sidplayfp CLI with SIDLite for the runtime image
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.5

#### 📦 Stable Release

_Changes since [2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4)_

##### 🐛 Bugfixes

- Fix OpenSubsonic credential preservation during reconfiguration (by @teancom in #6376)
- Stop the audio analysis background scan from spawning a task per track (by @balloobbot in #6384)
- Update py-opensonic to 10.4.1 (by @khers in #6388)
- Fix announcements on a speaker group playing out of sync (by @marcelveldt in #6392)
- Remove stale author/narrator links when an audiobook is overwritten (by @fmunkes in #6397)
- Fix shuffle/repeat failing on players playing a dynamic mix (by @marcelveldt in #6404)
- Move the ibroadcast item mapping to strings only (by @robsonke in #6405)
- Fix false permission error opening an artist page (by @marcelveldt in #6411)
- Updates token management to allow PlexHome users to import their own libraries (by @romain38 in #6426)
- Keep the stale mapping pass from emptying a library on mismatched ids (by @RyanAtTanagra in #6427)
- Fix resume position after fallback announcements (by @sickkick in #6429)
- Fix Snapcast volume/mute routing to idle native player when Sendspin is active (by @tortfeaser in #6432)
- Fix YTMusic album resolution crash on null audioPlaylistId (by @frosty-geek in #6435)
- Fix external auth consent banner being hidden by ad-blocker filters (by @lanquarden in #6443)
- Keep one failing provider from aborting album, artist and genre playback (by @teancom in #6446)
- Attribute synced progress to the reporting provider instance (by @fmunkes in #6450)
- Stop a group's queue when it is powered off outside Music Assistant (by @marcelveldt in #6452)
- Skip CUE sheets with a missing audio file when browsing (by @OzGav in #6463)
- Reconnect radio streams that go silent before playback gives up (by @OzGav in #6466)
- Allow a speaker to rejoin a group right after the group broke up (by @marcelveldt in #6473)
- Fix a speaker group going silent when one room is powered off while another joins (by @marcelveldt in #6474)
- Link ARD Audiothek episodes to their own podcast (by @OzGav in #6488)
- Fix Spotify dropping out on Sonos after resuming near the end of a track (by @marcelveldt in #6497)
- Keep manually linked genres when a music provider syncs (by @MarvinSchenkel in #6499)
- Only defer the next-track preload for realtime single-stream sources (by @marcelveldt in #6500)
- Fix an idle sync group dissolving in the middle of a member change (by @marcelveldt in #6501)
- Stop Apple Music from adding empty albums whose songs were withdrawn from the catalog (by @MarvinSchenkel in #6502)
- Resume audiobooks and podcast episodes at their saved position when the queue moves on (by @MarvinSchenkel in #6503)
- Acquire the narrators from book metadata in Audiobookshelf (by @fmunkes in #6504)
- Fix an announcement or play command on a grouped speaker locking up during a group change (by @marcelveldt in #6505)
- Fix a play command on a synced speaker locking up during a group change (by @marcelveldt in #6510)
- Fix Nicovideo feed artists not matching library items (by @marcelveldt in #6511)
- Fix Plex login for users the server is shared with (by @aevans0001 in #6513)
- Keep the library's housekeeping state when the music settings are saved (by @marcelveldt in #6514)
- Stop Cast flow playback from skipping an extra track after pressing next (by @MarvinSchenkel in #6518)
- Keep task schedules and run history when saving the Tasks settings (by @marcelveldt in #6522)
- Keep a group playing when the speaker leading it is powered off (by @marcelveldt in #6525)
- Fix static on Squeezelite sync groups when playing live sources like the AirPlay Receiver (by @MarvinSchenkel in #6529)
- Fix external playback not tracked after a player leaves a Sendspin group (by @MarvinSchenkel in #6530)
- Keep the WiiM queue on the right track when an event is missed (by @MarvinSchenkel in #6532)
- Keep filling a seed pool past one unproductive radio batch (by @balloob in #6535)
- Don't flag cleanly finished HTTP audio streams as failed (by @MarvinSchenkel in #6536)
- Fix filesystem sync not removing deleted files with an uppercase extension (by @OzGav in #6539)
- Fix scrobblers submitting a track twice (by @MarvinSchenkel in #6556)
- Keep DLNA players available when firmware sends a wrong Content-Length (by @MarvinSchenkel in #6557)
- Fix YouTube Music album versions failing on a zero-height thumbnail (by @MarvinSchenkel in #6561)
- Fix crossfades turning into hard cuts on players that buffer far ahead (by @marcelveldt in #6569)
- Honor HTTP proxy environment variables (by @MarvinSchenkel in #6572)
- Fix a stopped queue keeping a stream open at the music source (by @marcelveldt in #6573)
- Keep a track playable when its music source has no free stream (by @marcelveldt in #6576)
- Fix a paused player keeping its music source busy for minutes (by @marcelveldt in #6577)
- Fix Spotify app pairing not finding the device on hosts with Docker networks (by @MarvinSchenkel in #6578)
- Show Spotify top tracks when a custom client ID is set (by @marcelveldt in #6583)
- Fix Bandcamp requests returning an HTML challenge page instead of JSON (by @MarvinSchenkel in #6592)
- Deezer: fix resume from other devices and a missing timeout (by @jdaberkow in #6596)
- Resolve the current TuneIn stream url at playback time (by @MarvinSchenkel in #6606)
- Stop playback jumping back to the first track when a player reconnects (by @marcelveldt in #6608)
- Fix a universal player getting a new id on every restart (by @MarvinSchenkel in #6610)
- Show Spotify new releases and genres when a custom client ID is set (by @marcelveldt in #6615)
- Keep YouTube Music searches out of your YouTube search history (by @MarvinSchenkel in #6643)

##### Other Changes

- Fix Sonos speakers getting stuck on the wrong playback state (by @marcelveldt in #6395)

##### 🧰 Maintenance and dependency bumps

- Update various code owners (by @OzGav in #6485)
- Update aioslimproto to 3.2.3 (by @MarvinSchenkel in #6570)
- Update airplay-cli to v0.5.5 (by @musicassistant-bot[bot] in #6637)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @RyanAtTanagra, @aevans0001, @balloob, @balloobbot, @fmunkes, @frosty-geek, @jdaberkow, @khers, @lanquarden, @marcelveldt, @robsonke, @romain38, @sickkick, @teancom, @tortfeaser

## 2.10.5-upnext.1

Built from [Music Assistant 2.10.5](https://github.com/music-assistant/server/releases/tag/2.10.5), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **server** — Preserve multichannel PCM and convert DSD safely
- **server** — Recognize DFF streams as DSD for PCM buffer accounting
- **server** — Preserve direct DSD stereo downmix gain
- **server** — Add HVSC SID rendering provider with stereo widening
- **server** — Build the upstream sidplayfp CLI with SIDLite for the runtime image
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.5

#### 📦 Stable Release

_Changes since [2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4)_

##### 🚀 Features and enhancements

- Link existing libraries to MusicBrainz in the background (by @marcelveldt in #6496)

##### 🐛 Bugfixes

- Fix OpenSubsonic credential preservation during reconfiguration (by @teancom in #6376)
- Stop the audio analysis background scan from spawning a task per track (by @balloobbot in #6384)
- Update py-opensonic to 10.4.1 (by @khers in #6388)
- Fix announcements on a speaker group playing out of sync (by @marcelveldt in #6392)
- Remove stale author/narrator links when an audiobook is overwritten (by @fmunkes in #6397)
- Fix shuffle/repeat failing on players playing a dynamic mix (by @marcelveldt in #6404)
- Move the ibroadcast item mapping to strings only (by @robsonke in #6405)
- Fix false permission error opening an artist page (by @marcelveldt in #6411)
- Updates token management to allow PlexHome users to import their own libraries (by @romain38 in #6426)
- Keep the stale mapping pass from emptying a library on mismatched ids (by @RyanAtTanagra in #6427)
- Fix resume position after fallback announcements (by @sickkick in #6429)
- Fix Snapcast volume/mute routing to idle native player when Sendspin is active (by @tortfeaser in #6432)
- Fix YTMusic album resolution crash on null audioPlaylistId (by @frosty-geek in #6435)
- Fix external auth consent banner being hidden by ad-blocker filters (by @lanquarden in #6443)
- Keep one failing provider from aborting album, artist and genre playback (by @teancom in #6446)
- Attribute synced progress to the reporting provider instance (by @fmunkes in #6450)
- Stop a group's queue when it is powered off outside Music Assistant (by @marcelveldt in #6452)
- Skip CUE sheets with a missing audio file when browsing (by @OzGav in #6463)
- Reconnect radio streams that go silent before playback gives up (by @OzGav in #6466)
- Allow a speaker to rejoin a group right after the group broke up (by @marcelveldt in #6473)
- Fix a speaker group going silent when one room is powered off while another joins (by @marcelveldt in #6474)
- Link ARD Audiothek episodes to their own podcast (by @OzGav in #6488)
- Fix Spotify dropping out on Sonos after resuming near the end of a track (by @marcelveldt in #6497)
- Keep manually linked genres when a music provider syncs (by @MarvinSchenkel in #6499)
- Only defer the next-track preload for realtime single-stream sources (by @marcelveldt in #6500)
- Fix an idle sync group dissolving in the middle of a member change (by @marcelveldt in #6501)
- Stop Apple Music from adding empty albums whose songs were withdrawn from the catalog (by @MarvinSchenkel in #6502)
- Resume audiobooks and podcast episodes at their saved position when the queue moves on (by @MarvinSchenkel in #6503)
- Acquire the narrators from book metadata in Audiobookshelf (by @fmunkes in #6504)
- Fix an announcement or play command on a grouped speaker locking up during a group change (by @marcelveldt in #6505)
- Fix a play command on a synced speaker locking up during a group change (by @marcelveldt in #6510)
- Fix Nicovideo feed artists not matching library items (by @marcelveldt in #6511)
- Fix Plex login for users the server is shared with (by @aevans0001 in #6513)
- Keep the library's housekeeping state when the music settings are saved (by @marcelveldt in #6514)
- Stop Cast flow playback from skipping an extra track after pressing next (by @MarvinSchenkel in #6518)
- Keep task schedules and run history when saving the Tasks settings (by @marcelveldt in #6522)
- Keep a group playing when the speaker leading it is powered off (by @marcelveldt in #6525)
- Fix static on Squeezelite sync groups when playing live sources like the AirPlay Receiver (by @MarvinSchenkel in #6529)
- Fix external playback not tracked after a player leaves a Sendspin group (by @MarvinSchenkel in #6530)
- Keep the WiiM queue on the right track when an event is missed (by @MarvinSchenkel in #6532)
- Keep filling a seed pool past one unproductive radio batch (by @balloob in #6535)
- Don't flag cleanly finished HTTP audio streams as failed (by @MarvinSchenkel in #6536)
- Fix filesystem sync not removing deleted files with an uppercase extension (by @OzGav in #6539)
- Fix scrobblers submitting a track twice (by @MarvinSchenkel in #6556)
- Keep DLNA players available when firmware sends a wrong Content-Length (by @MarvinSchenkel in #6557)
- Fix YouTube Music album versions failing on a zero-height thumbnail (by @MarvinSchenkel in #6561)
- Fix crossfades turning into hard cuts on players that buffer far ahead (by @marcelveldt in #6569)
- Honor HTTP proxy environment variables (by @MarvinSchenkel in #6572)
- Fix a stopped queue keeping a stream open at the music source (by @marcelveldt in #6573)
- Keep a track playable when its music source has no free stream (by @marcelveldt in #6576)
- Fix a paused player keeping its music source busy for minutes (by @marcelveldt in #6577)
- Fix Spotify app pairing not finding the device on hosts with Docker networks (by @MarvinSchenkel in #6578)
- Show Spotify top tracks when a custom client ID is set (by @marcelveldt in #6583)
- Fix Bandcamp requests returning an HTML challenge page instead of JSON (by @MarvinSchenkel in #6592)
- Deezer: fix resume from other devices and a missing timeout (by @jdaberkow in #6596)
- Resolve the current TuneIn stream url at playback time (by @MarvinSchenkel in #6606)
- Stop playback jumping back to the first track when a player reconnects (by @marcelveldt in #6608)
- Fix a universal player getting a new id on every restart (by @MarvinSchenkel in #6610)
- Show Spotify new releases and genres when a custom client ID is set (by @marcelveldt in #6615)
- Keep YouTube Music searches out of your YouTube search history (by @MarvinSchenkel in #6643)

##### 🎨 Frontend Changes

- Use Escape for back navigation (by @teancom in [#2850](https://github.com/music-assistant/frontend/pull/2850))
- Press Space to play or pause (by @pierosavi in [#2714](https://github.com/music-assistant/frontend/pull/2714))
- Keep TanStack Form packages on the same version (by @marcelveldt in [#2858](https://github.com/music-assistant/frontend/pull/2858))
- Bump vue-i18n from 11.4.10 to 11.4.12 (by @[dependabot[bot]](https://github.com/apps/dependabot) in [#2819](https://github.com/music-assistant/frontend/pull/2819))
- Bump typescript-eslint from 8.68.0 to 8.70.1 (by @[dependabot[bot]](https://github.com/apps/dependabot) in [#2816](https://github.com/music-assistant/frontend/pull/2816))
- Pick where your music lives: folder picker and Storage settings (by @marcelveldt in [#2860](https://github.com/music-assistant/frontend/pull/2860))
- Open the start page after logging out (by @marcelveldt in [#2873](https://github.com/music-assistant/frontend/pull/2873))

##### Other Changes

- Fix Sonos speakers getting stuck on the wrong playback state (by @marcelveldt in #6395)

##### 🧰 Maintenance and dependency bumps

<details>
<summary>8 changes</summary>

- Request Copilot review only after CI passes (by @chrisuthe in #6462)
- Update various code owners (by @OzGav in #6485)
- Keep runtime state of core modules when saving their settings (by @marcelveldt in #6519)
- Tell Copilot the frontend ships in lockstep with the server (by @marcelveldt in #6523)
- Update aioslimproto to 3.2.3 (by @MarvinSchenkel in #6570)
- Fix missing Local files tracks in folders named like the source folder (by @marcelveldt in #6581)
- Bind the Sendspin server to a free port in full-server test fixtures (by @teancom in #6590)
- Update airplay-cli to v0.5.5 (by @musicassistant-bot[bot] in #6637)

</details>

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @RyanAtTanagra, @aevans0001, @balloob, @balloobbot, @chrisuthe, @fmunkes, @frosty-geek, @jdaberkow, @khers, @lanquarden, @marcelveldt, @pierosavi, @robsonke, @romain38, @sickkick, @teancom, @tortfeaser

## 2.10.4-upnext.20

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **server** — Preserve multichannel PCM and convert DSD safely
- **server** — Recognize DFF streams as DSD for PCM buffer accounting
- **server** — Preserve direct DSD stereo downmix gain
- **server** — Add HVSC SID rendering provider with stereo widening
- **server** — Build the upstream sidplayfp CLI with SIDLite for the runtime image
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.19

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **server** — Preserve multichannel PCM and convert DSD safely
- **server** — Recognize DFF streams as DSD for PCM buffer accounting
- **server** — Preserve direct DSD stereo downmix gain
- **server** — Add HVSC SID rendering provider with stereo widening
- **server** — Build the upstream sidplayfp CLI with SIDLite for the runtime image
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.18

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **server** — Preserve multichannel PCM and convert DSD safely
- **server** — Recognize DFF streams as DSD for PCM buffer accounting
- **server** — Preserve direct DSD stereo downmix gain
- **server** — Add HVSC SID rendering provider with stereo widening
- **server** — Build the upstream sidplayfp CLI with SIDLite for the runtime image
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.17

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **server** — Preserve multichannel PCM and convert DSD safely
- **server** — Recognize DFF streams as DSD for PCM buffer accounting
- **server** — Preserve direct DSD stereo downmix gain
- **server** — Add High Voltage SID Collection (HVSC) music provider
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.16

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **server** — Preserve multichannel PCM and convert DSD safely
- **server** — Recognize DFF streams as DSD for PCM buffer accounting
- **server** — Preserve direct DSD stereo downmix gain
- **server** — Add High Voltage SID Collection (HVSC) music provider
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.15

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **server** — Preserve multichannel PCM and convert DSD safely
- **server** — Recognize DFF streams as DSD for PCM buffer accounting
- **server** — Preserve direct DSD stereo downmix gain
- **server** — Add High Voltage SID Collection (HVSC) music provider
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.14

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **server** — Preserve multichannel PCM and convert DSD safely
- **server** — Recognize DFF streams as DSD for PCM buffer accounting
- **server** — Preserve direct DSD stereo downmix gain
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.13

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **server** — Preserve multichannel PCM and convert DSD safely
- **server** — Recognize DFF streams as DSD for PCM buffer accounting
- **server** — Preserve direct DSD stereo downmix gain
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.12

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **server** — Preserve multichannel PCM and convert DSD safely
- **server** — Recognize DFF streams as DSD for PCM buffer accounting
- **server** — Preserve direct DSD stereo downmix gain
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.11

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.10

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.9

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.8

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.7

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Add an A-Z strip to selected library listings

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.6

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Put an A-Z strip above every library listing

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.5

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Put an A-Z strip above every library listing

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.4

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Put an A-Z strip above every library listing

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.3

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing start at a first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Put an A-Z strip above every library listing

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.2

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Let a library listing be narrowed to one first letter
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go
- **frontend** — Offer a jump to a first letter in every library listing

### Upstream release notes for 2.10.4

#### 📦 Stable Release

_Changes since [2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3)_

##### 🚀 Features and enhancements

- Let the sample rates setting apply to Sonos players (by @RyanAtTanagra in #6356)

##### 🐛 Bugfixes

- Keep provider item lookups scoped to their own media type (by @jdaberkow in #6203)
- Keep the duplicate track walk from freezing the library database (by @OzGav in #6236)
- Stop a hostname in the Published IP address setting from breaking playback (by @marcelveldt in #6305)
- Fill in unplayable album tracks from another provider (by @OzGav in #6310)
- Fix Squeezelite players sometimes playing static instead of music (by @marcelveldt in #6311)
- Fix Squeezelite players going silent when switching tracks quickly (by @marcelveldt in #6316)
- Keep retrying YouTube Music when the PO Token server is not up yet (by @CodeCommander in #6326)
- Log an unavailable player at debug level while polling (by @balloob in #6336)
- Let users control their own connected client player (by @MarvinSchenkel in #6340)
- Show Qobuz tracks played outside the library in Recently played (by @chrisuthe in #6347)
- Drop provider mappings for items the provider no longer has (by @RyanAtTanagra in #6355)
- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6362)
- Ensure that the in-library view doesn't "lose" media items during a socket update in Audiobookshelf (by @fmunkes in #6363)
- Return HTTP 400 instead of 500 for a non-JSON login request body (by @MarvinSchenkel in #6371)
- Treat YouTube Music as a realtime source (by @MarvinSchenkel in #6373)

##### Other Changes

- Fix library artists and albums picking up an invalid provider link (by @marcelveldt in #6366)

##### 🧰 Maintenance and dependency bumps

- Fix memory build-up when a crossfade gets interrupted (by @marcelveldt in #6341)
- Clarify that manual button presses are needed for Spotify setup flow (by @remon1496 in #6383)

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @RyanAtTanagra, @balloob, @chrisuthe, @fmunkes, @jdaberkow, @marcelveldt, @remon1496

## 2.10.4-upnext.1

Built from [Music Assistant 2.10.4](https://github.com/music-assistant/server/releases/tag/2.10.4), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go

## 2.10.3-upnext.1

Built from [Music Assistant 2.10.3](https://github.com/music-assistant/server/releases/tag/2.10.3), with these patches applied:

- **server** — Surface the Pocket Casts Up Next queue as a podcast
- **server** — Stop re-asking Pocket Casts for the same account-wide status
- **server** — Give the browse folders their episodes' show notes
- **server** — Install the patched frontend wheel over the pinned one
- **server** — Look for a user-supplied app_vars.json in the add-on data directory
- **frontend** — Refuse to render form controls from metadata markdown
- **frontend** — Show a podcast episode's show notes where lyrics go

### Upstream release notes for 2.10.3

#### 📦 Stable Release

_Changes since [2.10.2](https://github.com/music-assistant/server/releases/tag/2.10.2)_

##### 🚀 Features and enhancements

- Align party and music quiz plugin icons with the frontend menu (by @MarvinSchenkel in #6258)
- Default the global autoplay setting to off (by @MarvinSchenkel in #6276)

##### 🐛 Bugfixes

- Play the newest episode when you ask for the latest one (by @OzGav in #6178)
- Show ARD Audiothek episodes in the right order (by @OzGav in #6179)
- Deezer: keep cover art and artist on user-uploaded tracks (by @jdaberkow in #6202)
- Play a plain URL instead of a random track for users with a provider filter (by @MarvinSchenkel in #6205)
- Fix sidebar shortcuts stuck after a provider was removed (by @OzGav in #6207)
- Fix Deezer account isolation and clarify authentication failures (by @jdaberkow in #6213)
- Fix Plex Connect starting the wrong track in large queues (by @MarvinSchenkel in #6217)
- Fix Sonic Similarity not loading when the database holds a corrupt analysis row (by @MarvinSchenkel in #6218)
- Sort Apple Music library by the date you actually added items (by @MarvinSchenkel in #6219)
- Fix players not regrouping after an announcement on a synced player (by @MarvinSchenkel in #6220)
- Route generic LinkPlay OEM devices to the generic WiiM backend (by @OzGav in #6223)
- Plex provider - incorrectly accepts empty media container as lyrics (by @caraar12345 in #6229)
- Keep local playlist covers in subfolders instead of replacing them with a collage (by @OzGav in #6230)
- Stop TuneIn sync treating non-favourite stations as failed items (by @OzGav in #6231)
- Keep Sonos S1 playback events from blocking the event loop (by @OzGav in #6235)
- Skip corrupt audio files instead of crashing the play request (by @OzGav in #6242)
- Tidal: fix playback of tracks that have a Dolby Atmos version (by @jozefKruszynski in #6244)
- Fix Jellyfin 12 playback and artwork (by @MarvinSchenkel in #6251)
- Fix a single-track Endless Mix looping over the same few songs (by @MarvinSchenkel in #6254)
- Show the station logo instead of the previous track's artwork when a radio starts (by @OzGav in #6256)
- Fix preset slot assignment and xml encoding in Bose Soundtouch (by @fmunkes in #6260)
- Fix the Profiler plugin leaking memory during CPU profiling (by @marcelveldt in #6266)
- Keep the MilkDrop visualizer alive on tracks longer than the audio buffer (by @jozefKruszynski in #6272)
- Stop Sonos speakers cutting out a couple of tracks in (by @marcelveldt in #6278)

##### 🧰 Maintenance and dependency bumps

<details>
<summary>7 changes</summary>

- Rename the DI provider to Digitally Imported (by @OzGav in #6197)
- Use the coloured Sendspin logo for the provider icon (by @MarvinSchenkel in #6225)
- Pace a stream by what is being served (by @marcelveldt in #6237)
- BBC Sounds: remove duplicated function (by @kieranhogg in #6245)
- Say so when a Sonos speaker cannot play a track (by @marcelveldt in #6246)
- Keep Sonos playing an album of short tracks (by @marcelveldt in #6247)
- Enabling debug logging no longer slows the server down (by @marcelveldt in #6265)

</details>

#### :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @caraar12345, @fmunkes, @jdaberkow, @jozefKruszynski, @kieranhogg, @marcelveldt

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
