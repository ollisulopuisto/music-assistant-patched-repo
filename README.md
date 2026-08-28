# Patched Music Assistant add-ons

A Home Assistant add-on repository. It serves two add-ons:

- **Music Assistant (Pocket Casts Up Next)** — Music Assistant **stable** with a set
  of Pocket Casts patches applied, rebuilt automatically as upstream releases.
- **Audiobookshelf** — upstream's own image, wrapped as an add-on. Nothing is
  rebuilt; see [Audiobookshelf](#audiobookshelf) below.

Add it to Home Assistant under **Settings → Add-ons → Add-on Store → ⋮ →
Repositories**:

```
https://github.com/ollisulopuisto/music-assistant-patched-repo
```

## What is patched

| Patch | What it does |
| --- | --- |
| `patches/server/0001-up-next-queue-as-podcast.patch` | Surfaces the Pocket Casts Up Next queue as a podcast in the library, with resume positions, so an episode started on the phone continues on a speaker |
| `patches/server/0002-status-refetch.patch` | Stops re-fetching the account-wide in-progress/history lists once per podcast during a sync |
| `patches/server/0003-show-notes.patch` | Gives episodes in the mixed browse folders their show notes |
| `patches/server/0100-install-patched-frontend.patch` | Installs the locally built frontend wheel over the one upstream pins |
| `patches/frontend/0001-forbid-forms.patch` | Stops provider metadata rendering form controls (a feed-supplied `<form>` was a working phishing box) |
| `patches/frontend/0002-show-notes.patch` | Shows an episode's notes in the list subtitle and in the fullscreen player's side panel, where lyrics go |

Every one of these is also open as a pull request upstream. **When one is merged,
delete its patch file and push** — the next build picks up the change from
upstream instead, and the pipeline carries on unchanged.

## Bundled credentials, and why Spotify needs a file

Upstream injects shared API credentials into its own builds at release time, from a
private repository. A build that is not upstream's does not get them, so
`app_var()` returns an empty string for every provider that relies on one:

```
spotify  qobuz  tidal  apple_music  deezer  lastfm_scrobble
lastfm_recommendations  theaudiodb  fanarttv  acoustid_lookup
```

For Spotify this is fatal rather than degraded. Its setup flow authenticates a
mandatory "global" session with `app_var("spotify_client_id")` *before* it offers
the developer-key step, so an empty value is a dead end - you never reach the
place where you would enter your own.

`patches/server/0110-app-vars-from-data-dir.patch` makes the server read
`/data/app_vars.json`, so **your own** credentials can live beside the rest of the
add-on data and survive rebuilds:

```json
{
  "spotify_client_id": "a client id from your own Spotify app",
  "lastfm_api_key": "your own Last.fm key",
  "lastfm_api_secret": "your own Last.fm secret"
}
```

Register the Spotify app yourself at developer.spotify.com with
`https://music-assistant.io/callback` as a redirect URI. It uses PKCE, so it needs
no client secret.

Two things worth knowing. The file is read once per process (`_read_json_map` is
cached), so **restart the add-on after editing it**. And it is plaintext, unlike
`settings.json`, which is encrypted - so it rides along in backups as written. A
Spotify client id is a public OAuth identifier and fine there; a Last.fm *secret*
is better placed in the Last.fm provider's own settings field, which is encrypted.

Do not put Music Assistant's own bundled keys in this file. They are shared
community credentials, rate-limited across every user of the project, and get
throttled or revoked when they are scraped - which breaks Music Assistant for
everyone, not just whoever copied them.

## How the build works

`.github/workflows/build-patched.yml`, weekly on Mondays plus manual dispatch,
and immediately on any push that touches `patches/`.

1. Resolve the newest upstream `x.y.z` release tag.
2. Check out the frontend at the version that release pins, apply the frontend
   patches, typecheck, build the bundle, build a wheel.
3. Check out the server at that tag, apply the server patches, **run the Pocket
   Casts tests against the patched tree**, build the wheel.
4. Build and push both architectures, join them under one tag.
5. Bump this repository's `config.yaml`, which is what makes Home Assistant offer
   the update.

Published as `ghcr.io/ollisulopuisto/ma-server-patched:<upstream>-upnext.<n>`,
e.g. `2.10.0-upnext.1`. The version says what it was built from, and sorts above
the upstream release it carries.

### When it breaks

It will, eventually — upstream reworks the Pocket Casts provider and a patch
stops applying. Two things are built in for that:

- **Nothing is published.** `config.yaml` is bumped in the last step, so a failure
  anywhere before it leaves the last good image installed and running. You are
  never handed a half-patched build.
- **An issue is opened**, labelled `build-failure`, reopened and commented on
  rather than duplicated. The workflow this replaced failed every night from May
  2026 onward and nobody noticed for three months; silence is the actual hazard
  here, not the breakage.

To fix: re-roll the failing patch against the release named in the run, and push.

## Notes

- The add-on's slug is still `music_assistant_upnext_test`, from when this was a
  throwaway test build. Renaming a slug is an uninstall and reinstall, so it stays
  as it is — the display name is what you actually see.
- `music-assistant-custom/` is the older "Music Assistant (Patched)" add-on, built
  for variable playback speed. That feature is in upstream now, so it is
  superseded; its nightly workflow has been removed. The folder is left in place
  so anyone still running it does not have the add-on vanish from their store.

## Audiobookshelf

A thin wrapper around upstream's published multi-architecture image
(`ghcr.io/advplyr/audiobookshelf`). No build step — the add-on's `version` is
simply the Audiobookshelf release it installs, so updating means bumping that
line to a newer tag.

**Why bother, when Music Assistant can read a filesystem directly?** Progress.
Music Assistant's Audiobookshelf provider both reports position back
(`on_played`) and subscribes to a socket that pushes changes the other way
(`on_user_item_progress_updated`). Two Music Assistant instances pointed at one
Audiobookshelf therefore share a single, live resume position. With a filesystem
provider, position lives in each server's own `playlog` table and the two
silently drift apart.

It is also far kinder to a remote link: Music Assistant talks HTTP to
Audiobookshelf, which survives Tailscale and a flaky connection in a way SMB
does not.

### Notes

- It listens on **13378**. Deliberately a real port rather than ingress: the
  point is for Music Assistant — including an instance somewhere else entirely —
  to reach it, and ingress only ever serves a browser.
- `CONFIG_PATH` and `METADATA_PATH` are pointed into `/data`, because that is the
  only directory an add-on keeps. The image defaults them to `/config` and
  `/metadata`, which would not survive a restart.
- Add your library under `/media/...`; the add-on maps Home Assistant's `media`
  and `share` directories.
- It does **not** give Audiobookshelf access to storage that Home Assistant
  cannot already see. A drive attached to some other machine still has to be
  mounted — Settings → System → Storage, or passed through to the VM.
