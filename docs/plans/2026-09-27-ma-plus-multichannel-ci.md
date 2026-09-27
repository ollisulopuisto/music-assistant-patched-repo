# MA+ Multichannel Audio CI Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make MA+ CI exercise the regression tests shipped with its multichannel and DSD server patches before an image can be published.

**Architecture:** Keep the existing strict patch-application gate, then run the patch series' focused pytest modules in the existing `verify` job after dependencies are installed. Keep the Home Assistant packaging workflow unchanged outside that test gate.

**Tech Stack:** GitHub Actions, Python, pytest.

---

### Task 1: Add a targeted multichannel/DSD test step

**Files:**
- Modify: `.github/workflows/build-patched.yml`

**Steps:**
1. Preserve the existing Pocket Casts test step.
2. Install FFmpeg in the hosted runner because `tests/helpers/test_ffmpeg.py` invokes the executable directly.
3. Add a pytest step for the eight test modules modified by patches `0120`–`0122`.
4. Check workflow formatting and diff whitespace.
5. Run the equivalent pytest command against the exact upstream release once that source is available; until then, let strict patch application and hosted CI validate the release checkout.

### Task 2: Review and publish

**Files:**
- Review only: `patches/server/0120-dsd-multichannel-pcm.patch`
- Review only: `patches/server/0121-dff-dsd-marker.patch`
- Review only: `patches/server/0122-preserve-dsd-stereo-downmix.patch`
- Review only: `README.md`

**Steps:**
1. Confirm only intended MA+ files are staged; leave unrelated working-tree changes untouched.
2. Commit and push the patch series and CI gate only after reviewing the resulting diff and the upstream apply/test status.
