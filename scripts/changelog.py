#!/usr/bin/env python3
"""
Prepend an entry to the add-on's CHANGELOG.md.

Home Assistant shows that file verbatim in the update dialog, so it is the only
place a user sees what an update actually contains. Without it the dialog is
blank and the version string is the whole story.

Two things go into an entry: what upstream release the build carries, with
upstream's own notes for it, and which of our patches are on top. The patch list
is read from the files rather than written by hand, so a patch that gets merged
upstream and deleted stops being claimed here on the very next build.

Usage:
    changelog.py --version 2.10.1-upnext.1 --server-ref 2.10.1
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request

SERVER_REPO = "music-assistant/server"
HEADER = """# Changelog

Music Assistant, rebuilt from upstream's own release with the patches in
[`patches/`](https://github.com/ollisulopuisto/music-assistant-patched-repo/tree/main/patches)
applied. Each entry names the upstream release it carries and the patches on top
of it.
"""


def patch_title(path: pathlib.Path) -> str:
    """
    Return the one-line description of a patch file.

    :param path: The patch file to describe.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    # git format-patch output; the rest are hand-written diffs that open with a
    # title line, which is the same thing without the ceremony
    if match := re.search(r"^Subject: \[PATCH[^\]]*\] (.+)$", text, re.MULTILINE):
        return match.group(1).strip()
    for line in text.splitlines():
        if line.strip():
            return line.strip()
    return path.stem


def patch_lines(patches_dir: pathlib.Path) -> list[str]:
    """
    Return a markdown bullet per patch, grouped by the tree it applies to.

    :param patches_dir: The directory holding the per-tree patch subdirectories.
    """
    lines: list[str] = []
    for tree in ("server", "frontend"):
        for patch in sorted((patches_dir / tree).glob("*.patch")):
            lines.append(f"- **{tree}** — {patch_title(patch)}")
    return lines


def upstream_notes(tag: str) -> str | None:
    """
    Return upstream's own release notes for a tag, or None if they cannot be read.

    :param tag: The upstream release tag.
    """
    request = urllib.request.Request(
        f"https://api.github.com/repos/{SERVER_REPO}/releases/tags/{tag}",
        headers={"Accept": "application/vnd.github+json"},
    )
    if token := os.environ.get("GH_TOKEN"):
        request.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = json.load(response).get("body") or ""
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as err:
        # a missing set of notes is not worth failing a build that otherwise worked
        print(f"could not read upstream notes for {tag}: {err}", file=sys.stderr)
        return None
    if not body.strip():
        return None
    # upstream writes its notes as a standalone document starting at "##", which
    # would sit level with our version headings; push everything two levels down
    # so it nests under the entry it belongs to
    return re.sub(
        r"(?m)^(#{1,4})(?= )", lambda m: "#" * min(len(m.group(1)) + 2, 6), body.strip()
    )


def build_entry(version: str, server_ref: str, patches_dir: pathlib.Path) -> str:
    """
    Return the complete markdown entry for one published version.

    :param version: The add-on version being published.
    :param server_ref: The upstream release this build carries.
    :param patches_dir: The directory holding the patches applied to it.
    """
    release_url = f"https://github.com/{SERVER_REPO}/releases/tag/{server_ref}"
    parts = [
        f"## {version}",
        "",
        f"Built from [Music Assistant {server_ref}]({release_url}), with these "
        "patches applied:",
        "",
        *patch_lines(patches_dir),
    ]
    if notes := upstream_notes(server_ref):
        parts += ["", f"### Upstream release notes for {server_ref}", "", notes]
    return "\n".join(parts) + "\n"


def main() -> None:
    """Prepend the entry for this build to the add-on's changelog."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True)
    parser.add_argument("--server-ref", required=True)
    parser.add_argument("--patches", default="patches", type=pathlib.Path)
    parser.add_argument(
        "--changelog",
        default="music-assistant-upnext-test/CHANGELOG.md",
        type=pathlib.Path,
    )
    args = parser.parse_args()

    entry = build_entry(args.version, args.server_ref, args.patches)
    existing = ""
    if args.changelog.exists():
        existing = args.changelog.read_text(encoding="utf-8")
        existing = existing.removeprefix(HEADER).lstrip("\n")
    if existing.startswith(f"## {args.version}\n"):
        raise SystemExit(f"{args.changelog} already has an entry for {args.version}")

    args.changelog.write_text(
        HEADER + "\n" + entry + ("\n" + existing if existing else ""), encoding="utf-8"
    )
    print(f"wrote the {args.version} entry to {args.changelog}")


if __name__ == "__main__":
    main()
