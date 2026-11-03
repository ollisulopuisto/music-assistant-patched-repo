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
_SUBJECT_RE = re.compile(r"^Subject: \[PATCH[^\]]*\] (.+)$")
# Maximum response size allowed when reading upstream release notes (2 MiB)
# to protect against denial-of-service via memory exhaustion from oversized responses.
_MAX_RESPONSE_BYTES = 2 * 1024 * 1024
# Security: Allowed pattern for versions and release tags/refs to prevent header injection,
# path traversal, SSRF, or markdown structure breaking.
_REF_PATTERN = re.compile(r"^[a-zA-Z0-9_\.\-]+$")


class SafeRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Strip Authorization header when redirected to a different host to prevent credential leakage."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        new_req = super().redirect_request(req, fp, code, msg, headers, newurl)
        if new_req and req.host.lower() != new_req.host.lower():
            for key in list(new_req.headers.keys()):
                if key.lower() == "authorization":
                    del new_req.headers[key]
            for key in list(new_req.unredirected_hdrs.keys()):
                if key.lower() == "authorization":
                    del new_req.unredirected_hdrs[key]
        return new_req


def is_valid_ref(ref: str) -> bool:
    """Check that a tag, ref, or version string contains only safe alphanumeric/punctuation characters."""
    return bool(_REF_PATTERN.fullmatch(ref) and ".." not in ref)


def patch_title(path: pathlib.Path) -> str:
    """
    Return the one-line description of a patch file.

    :param path: The patch file to describe.
    """
    # Optimization: stream line-by-line rather than reading and regex-searching
    # entire files (which can be >100KB). Stop as soon as the Subject header or
    # the start of the diff contents is reached.
    first_non_empty: str | None = None
    with path.open("r", encoding="utf-8", errors="replace") as file:
        for line in file:
            stripped = line.strip()
            if not stripped:
                continue
            if first_non_empty is None:
                first_non_empty = stripped
            if stripped.startswith("Subject:"):
                if match := _SUBJECT_RE.match(stripped):
                    return match.group(1).strip()
            elif line.startswith("diff --git "):
                break
    return first_non_empty or path.stem


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
    # Security: validate tag to prevent path traversal or SSRF in the GitHub API endpoint
    if not is_valid_ref(tag):
        print(f"invalid upstream release tag format: {tag!r}", file=sys.stderr)
        return None

    request = urllib.request.Request(
        f"https://api.github.com/repos/{SERVER_REPO}/releases/tags/{tag}",
        headers={"Accept": "application/vnd.github+json"},
    )
    if token := os.environ.get("GH_TOKEN"):
        request.add_header("Authorization", f"Bearer {token}")
    opener = urllib.request.build_opener(SafeRedirectHandler)
    try:
        with opener.open(request, timeout=30) as response:
            # Bound response reading to prevent DoS via unbounded memory allocation
            payload = response.read(_MAX_RESPONSE_BYTES + 1)
            if len(payload) > _MAX_RESPONSE_BYTES:
                print(
                    f"upstream notes for {tag} exceeded {_MAX_RESPONSE_BYTES} bytes",
                    file=sys.stderr,
                )
                return None
            body = (
                json.loads(payload.decode("utf-8", errors="replace")).get("body") or ""
            )
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

    # Security: Validate version and server-ref arguments to prevent markdown header
    # injection, path traversal, or SSRF in upstream release note lookups.
    if not is_valid_ref(args.version):
        raise SystemExit(f"invalid version format: {args.version!r}")
    if not is_valid_ref(args.server_ref):
        raise SystemExit(f"invalid server-ref format: {args.server_ref!r}")

    # Performance: Check if this version has already been recorded before
    # running expensive patch directory scans and GitHub API release note requests.
    existing = ""
    if args.changelog.exists():
        existing = args.changelog.read_text(encoding="utf-8")
        existing = existing.removeprefix(HEADER).lstrip("\n")
        if existing.startswith(f"## {args.version}\n"):
            raise SystemExit(
                f"{args.changelog} already has an entry for {args.version}"
            )

    entry = build_entry(args.version, args.server_ref, args.patches)
    args.changelog.write_text(
        HEADER + "\n" + entry + ("\n" + existing if existing else ""), encoding="utf-8"
    )
    print(f"wrote the {args.version} entry to {args.changelog}")


if __name__ == "__main__":
    main()
