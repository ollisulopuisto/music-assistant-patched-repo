# Handoff — Music Assistant fork, A–Z library jump

Written 2026-09-24. Everything below is the state as of the last push.

---

## 1. The setup: three repos, three roles

| Path in this container | Repo | Branch | Pushable? |
| --- | --- | --- | --- |
| `/home/user/ma-server` | `music-assistant/server` fork | `library-first-letter-filter` | yes (`origin` is the fork) |
| `/home/user/music-assistant/frontend` | `music-assistant/frontend` | `library-first-letter-filter` | **no** — no fork exists yet, the git proxy refuses it |
| `/home/user/music-assistant-patched-repo` | `ollisulopuisto/music-assistant-patched-repo` | `main` | yes |

The frontend work lives only as local commits plus a `git format-patch` dump inside the
patched repo. **That patch file is the shipping artifact.** If you change the frontend,
you must regenerate it or nothing reaches a build:

```bash
cd /home/user/music-assistant/frontend
git format-patch --stdout 367878c..HEAD -- src/ \
  > /home/user/music-assistant-patched-repo/patches/frontend/0003-alphabet-jump.patch
```

`367878c` is the upstream commit the series is based on. `-- src/` is deliberate: the
Vitest files would append to a test file that has moved since the tag the build checks
out, and the build only typechecks the frontend anyway.

### How a build happens

`music-assistant-patched-repo/.github/workflows/build-patched.yml` runs daily at 04:17 UTC
and on any push touching `patches/**`. It checks out upstream's latest **stable** server
release plus the frontend version that release pins (`music-assistant-frontend==2.17.318`
right now), applies every patch with plain `git apply --verbose` (no 3-way, no fuzz),
builds a frontend wheel, builds the server image to
`ghcr.io/ollisulopuisto/ma-server-patched`, and bumps `config.yaml` to
`<upstream>-upnext.<n>`.

Because `git apply` is strict, **a patch that no longer applies fails the whole build.**
That is intentional — it is the signal that upstream moved.

Current published version: `2.10.4-upnext.5`. The push made just now
(`e2fc055`) should be producing `upnext.6`.

---

## 2. What the feature is

A big library (this user has tens of thousands of artists) was unreachable past the first
few pages: listings page 50 at a time and the search box matches *anywhere* in a name, so
it cannot stand in for "take me to T".

### Server side — `/home/user/ma-server`, one commit `20c5d768a`

Two new filters on library listings, `starts_from` and `starts_before`, threaded through
`library_items` / `get_library_items_by_query` in
`music_assistant/controllers/music/media/base.py` and each of the six subclass overrides
(`albums`, `artists`, `audiobooks`, `genres`, `podcasts`, `tracks`).

The interesting part is `_letter_bound_clause()` in `base.py`. It follows *the ordering's
own column*:

```python
name_column = "search_name" if order_by in ("name", "name_desc") else "search_sort_name"
```

Sorted by sort name, "The Beatles" is filed under B, not T — jumping on the wrong column
would land somewhere the list does not agree with. Both columns are already indexed
(`artists_search_sort_name_idx`), and there is a test asserting the query plan still uses
the index rather than scanning.

`starts_before` exists so the frontend can page *upward*: ask for "before this letter"
with the ordering reversed, and you get the items that precede the jump, nearest first.

Tests: `tests/controllers/music/test_library_first_letter_jump.py`, 20 of them. They cover
sort-column following, diacritic folding (`Ätna` folds to `atna`), case, an empty letter
falling through to the next one, composition with the other filters, `ValueError` on a
non-letter, and the two bounds partitioning the library exactly.

### Frontend side — `/home/user/music-assistant/frontend`, three commits

1. `9282c06` **Put an A-Z strip above every library listing** — new
   `src/components/AlphabetJumpBar.vue` (a `#` bucket then A–Z), new
   `src/helpers/alphabet_jump.ts` (`bucketOf`, `reverseSortKey`, `earlierPageParams`),
   `startsFrom`/`startsBefore` plumbed through `ItemsListing.vue`, `plugins/api/index.ts`
   and the eight `views/Library*.vue`, plus upward paging with manual scroll compensation.
2. `f09a98a` **Follow the scroll with the A-Z strip** — highlights the letter you are
   actually looking at, by hit-testing what sits just under the strip
   (`document.elementFromPoint`) rather than tracking the items.
3. `fe6cc69` **Send the listing back to the top when a letter is picked, and pin its
   header** — today's fixes, see below.

`#` is the top of the listing, not a letter: names starting with a digit, and names like
`!!!` that reduce to nothing once punctuation is stripped, all sort above `a`.

Helper tests: `tests/helpers/alphabet_jump.test.ts`, 11 of them. The full suite is
**4393 passing**. Two `ai_radio` tests failed once and passed on a re-run — flaky,
unrelated.

---

## 3. What was broken today, and what the fix was

The user pressed **R** and got a screen full of **T** artists, with R highlighted.

Cause: `jumpToLetter()` replaced the listing's contents but never touched the scroll
position. The reader was already scrolled deep; the new listing (R onwards) rendered under
that same offset, which lands in S/T. The highlight was right and the content was wrong.

Fixes in `fe6cc69`, all in `src/components/ItemsListing.vue`:

- `jumpToLetter` is now `async`, awaits `loadData`, then calls `scrollListingIntoView()`,
  which scrolls the `<section>` root (new `listingRef`) back to the top of the scroll
  container. It uses `getBoundingClientRect` deltas rather than the strip's own position,
  because a sticky element reports its *stuck* position and would compute a delta of zero.
- A `jumpGeneration` counter. `loadEarlierPage()` captures it before its await and bails if
  it changed — otherwise a page fetched for the letter you just left gets `unshift`ed onto
  the letter you just picked. `loadEarlierPage` does not set `loading`, so the strip is not
  disabled while it runs and this race was reachable.
- The whole listing header (toolbar + divider + tabs + mobile search row + the strip) is
  now wrapped in `div.listing-header`, made `position: sticky` when the strip is shown.
  Previously only the strip pinned itself, so search and the overflow menu scrolled away —
  the user's second complaint. The strip's own `position: sticky` is neutralised inside a
  pinned header (`:deep(.alphabet-jump-bar) { position: static; }`) or it would lift itself
  over the toolbar.

The pinning is deliberately scoped to `alphabetJumpAvailable && expanded`, i.e. the eight
library views. `ItemsListing` is also embedded mid-page (album lists inside artist details)
where a header pinning to the viewport top would look wrong.

**Verified:** `vue-tsc --noEmit` clean, `oxlint` + `eslint --max-warnings=0` clean,
prettier applied, 4393/4393 Vitest pass.

**Not verified:** none of the scroll behaviour has been exercised in a browser from here.
There is no MA server with a real library in this container, and the Vitest harness does
not render `v-infinite-scroll` at all (I probed it — `hasInfinite: false`), so the upward
paging, the `elementFromPoint` probe and now the scroll-reset and the sticky header are all
**untested wiring**. The testable logic was extracted into `helpers/alphabet_jump.ts`
precisely because the rest could not be. Judge these by looking at the running add-on, not
by the test count.

---

## 4. Known gaps, in the order worth caring about

1. **The strip shows every letter, even empty ones.** Greying out letters with no items
   needs per-letter counts, which needs refactoring each controller's inline
   `extra_query_parts`. Not started.
2. **Scroll-spy under a pinned header.** `readLetterUnderStrip()` probes at
   `strip.getBoundingClientRect().bottom + 4`. That still points just below the strip now
   that the strip sits at the bottom of a taller pinned block, so it should be fine — but
   it has not been seen working with the new header. Check it first if the highlight
   misbehaves.
3. **The sticky header eats vertical space on a phone.** Toolbar + strip pinned is a lot of
   chrome on a small screen. Worth looking at in the mobile layout.
4. **`loadData` early-returns while `loading` is true.** The strip is `:disabled="loading"`
   so a letter click cannot hit it today, but it is a silent drop if that guard ever
   changes.

---

## 5. Guardrails that are not optional

From `CLAUDE.md` in the server repo:

- **Never reply on GitHub** (PRs, discussions) without the developer's explicit consent.
- **Usage policy**: do not write anything that exposes a provider's own audio URL outside
  the server, decodes protected audio beyond the account's entitlement, calls a provider API
  without throttling, writes decoded provider audio to disk, bypasses a subscription tier or
  `max_concurrent_streams`, or adds downloading/exporting/archiving of provider audio. The
  readrate pacing on the stream endpoints and the filesystem-only restriction on background
  audio analysis exist for this reason and read as removable if you do not know that —
  **leave them**.
- **Only SELECT queries** against a live `library.db`.
- **Data changes need migrations.** If a change touches a config entry or a database row,
  ask the developer with an `AskUserQuestion` popup before treating it as done.
- All PRs target `dev`, not `stable`.

From MA's `helpers/app_vars.py`: the bundled credentials are shared, rate-limited keys
registered to the open-source project. Do not extract them. I refused to and so should you.

From the OHF AI policy: **autonomous-agent PRs get closed.** The upstream PRs for this work
are the user's to open, under their own review. Do not open them.

Branch discipline for this session: develop on `claude/pocket-casts-up-next-yax9xw` unless
told otherwise; the branches above were granted explicitly.

---

## 6. Unfinished work outside the A–Z feature

### The second Home Assistant box ("mökki", `192.168.10.245`)

The library was migrated from the official add-on to Music Assistant+ by copying
`/mnt/data/supervisor/apps/data/d5369777_music_assistant` →
`27d294da_music_assistant_upnext_test` (1.1G source, 198.5M after copy; the absent
`-wal`/`-shm` files confirm a clean close, not a gap). Still to do:

1. Write `app_vars.json` into the add-on's `/data` with **`spotify_client_id`** (the
   Last.fm keys can go in the provider UI instead — see below). Our build has no
   `app_secrets.json` because upstream injects it from a private repo at release time;
   that file is the *only* thing missing from an otherwise-complete migration.
2. Turn the SSH add-on's protection mode back **on**.
3. Start Music Assistant+ and watch the first-start log.
4. Point the HA `music_assistant` integration at `http://192.168.10.245:8095`.
5. Re-run the Spotify setup — the migrated refresh token was issued against upstream's
   client id and will not validate against a different one. Soloist pairing is per-box.
   Note Spotify's one-stream-per-account limit: `max_concurrent_streams` returns 1 on the
   Soloist backend and **nothing coordinates that across two servers**.
6. Add the Audiobookshelf provider pointing at the home tailnet IP.

### Last.fm credentials

Last.fm shows the shared secret exactly once, on the confirmation page after you create the
app. The accounts page does not list it and there is no API to retrieve it — the user
confirmed this. Registering a fresh app is free and instant and loses nothing, because
scrobbles belong to the Last.fm *user* account, not the API app.

They do **not** need to go in `app_vars.json`: `lastfm_scrobble/setup_flow.py` exposes
`_api_key` and `_api_secret` as advanced config entries, and `_resolve_credentials` in
`__init__.py` prefers them, falling back to `app_var()` only when **both** are blank (it
raises on a half-filled pair). Note that changing the API key invalidates the stored
`_api_session_key` and forces a re-authorise — so do not touch the home box's key.

### Upstream PRs

The user's to open, not an agent's. Before they do: fork `music-assistant/frontend`, decide
commit authorship (every commit here is `Claude <noreply@anthropic.com>`), and re-rebase —
the branches are about four weeks behind their bases now.

### Offered, not taken up

- `Link: rel="next"` pagination in the Audiobookshelf version tracker. The user already
  fixed the acute bug (`?n=1000` on the GHCR tags endpoint, commit `acee8b1`) after finding
  that it had been silently reporting success on a stale version for months.
- Per-letter counts, per gap 1 above.
