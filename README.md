# Music Assistant, patched

A Home Assistant add-on repository serving Music Assistant **stable** with a set
of Pocket Casts patches applied, rebuilt automatically as upstream releases.

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
