import sys
from unittest.mock import patch

import pytest

from scripts.changelog import (
    HEADER,
    SafeRedirectHandler,
    has_top_entry,
    is_valid_ref,
    main,
    patch_title,
    prepend_entry,
    upstream_notes,
)


def test_patch_title_format_patch(tmp_path):
    patch_file = tmp_path / "0001-test.patch"
    patch_file.write_text(
        "From abc Mon Sep 17 00:00:00 2001\n"
        "From: Test User <test@example.com>\n"
        "Date: Fri, 23 Oct 2026 21:51:41 +0000\n"
        "Subject: [PATCH] Extract this title properly\n"
        "\n"
        "---\n"
        " file.py | 1 +\n"
        "diff --git a/file.py b/file.py\n"
        "+line\n"
    )
    assert patch_title(patch_file) == "Extract this title properly"


def test_patch_title_non_format_patch(tmp_path):
    patch_file = tmp_path / "0002-custom.patch"
    patch_file.write_text(
        "\n"
        "Custom one-line description\n"
        "\n"
        "Additional details\n"
        "diff --git a/file.py b/file.py\n"
    )
    assert patch_title(patch_file) == "Custom one-line description"


def test_patch_title_empty_fallback(tmp_path):
    patch_file = tmp_path / "0003-empty.patch"
    patch_file.write_text("\n\n   \n")
    assert patch_title(patch_file) == "0003-empty"


def test_patch_title_unicode_and_special_characters(tmp_path):
    patch_file = tmp_path / "0003-unicode.patch"
    patch_file.write_bytes(
        b"From abc Mon Sep 17 00:00:00 2001\n"
        b"Subject: [PATCH] Handle Caf\xc3\xa9, \xe2\x80\x94 em-dash, and \xf0\x9f\x9a\x80 emoji\n"
        b"\n"
        b"diff --git a/file.py b/file.py\n"
    )
    assert patch_title(patch_file) == "Handle Café, — em-dash, and 🚀 emoji"


def test_patch_title_large_file_stops_early(tmp_path):
    patch_file = tmp_path / "0004-large.patch"
    # Large diff body after header
    lines = [
        "Subject: [PATCH 1/2] Big patch title",
        "diff --git a/file.py b/file.py",
    ] + ["+large content line" for _ in range(10000)]
    patch_file.write_text("\n".join(lines))
    assert patch_title(patch_file) == "Big patch title"


def test_upstream_notes_valid_tag():
    with patch("urllib.request.OpenerDirector.open") as mock_open:
        mock_response = mock_open.return_value.__enter__.return_value
        mock_response.read.return_value = b'{"body": "## Notes"}'
        notes = upstream_notes("2.10.9")
        assert notes is not None
        assert "#### Notes" in notes


def test_safe_redirect_handler_strips_auth_on_cross_host():
    import urllib.request

    handler = SafeRedirectHandler()
    req = urllib.request.Request("https://api.github.com/repos/test/releases")
    req.add_header("Authorization", "Bearer secret-token")
    # Redirect to another host
    new_req = handler.redirect_request(
        req, None, 302, "Found", {}, "https://external.example.com/notes"
    )
    assert new_req is not None
    assert "Authorization" not in new_req.headers
    assert "Authorization" not in new_req.unredirected_hdrs


def test_safe_redirect_handler_preserves_auth_on_same_host():
    import urllib.request

    handler = SafeRedirectHandler()
    req = urllib.request.Request("https://api.github.com/repos/test/releases")
    req.add_header("Authorization", "Bearer secret-token")
    # Redirect to same host and scheme
    new_req = handler.redirect_request(
        req, None, 302, "Found", {}, "https://api.github.com/repos/test/releases/page2"
    )
    assert new_req is not None
    assert new_req.headers.get("Authorization") == "Bearer secret-token"


def test_safe_redirect_handler_strips_auth_on_scheme_downgrade():
    import urllib.request

    handler = SafeRedirectHandler()
    req = urllib.request.Request("https://api.github.com/repos/test/releases")
    req.add_header("Authorization", "Bearer secret-token")
    # Downgrade from HTTPS to HTTP on same host
    new_req = handler.redirect_request(
        req, None, 302, "Found", {}, "http://api.github.com/repos/test/releases/page2"
    )
    assert new_req is not None
    assert "Authorization" not in new_req.headers
    assert "Authorization" not in new_req.unredirected_hdrs


def test_safe_redirect_handler_strips_auth_on_port_change():
    import urllib.request

    handler = SafeRedirectHandler()
    req = urllib.request.Request("https://api.github.com/repos/test/releases")
    req.add_header("Authorization", "Bearer secret-token")
    # Redirect to different port on same host
    new_req = handler.redirect_request(
        req, None, 302, "Found", {}, "https://api.github.com:8443/repos/test/releases"
    )
    assert new_req is not None
    assert "Authorization" not in new_req.headers
    assert "Authorization" not in new_req.unredirected_hdrs


def test_upstream_notes_rejects_path_traversal():
    with patch("urllib.request.OpenerDirector.open") as mock_open:
        assert upstream_notes("../../tags") is None
        assert upstream_notes("foo/../../bar") is None
        assert upstream_notes("..") is None
        mock_open.assert_not_called()


def test_upstream_notes_rejects_invalid_characters():
    with patch("urllib.request.OpenerDirector.open") as mock_open:
        assert upstream_notes("tag;evil") is None
        assert upstream_notes("tag with spaces") is None
        assert upstream_notes("tag?query=1") is None
        assert upstream_notes("tag#hash") is None
        assert upstream_notes("tag@other") is None
        mock_open.assert_not_called()


def test_upstream_notes_rejects_oversized_response():
    with patch("urllib.request.OpenerDirector.open") as mock_open:
        mock_response = mock_open.return_value.__enter__.return_value
        # Exceed 2 MiB limit
        mock_response.read.return_value = b"x" * (2 * 1024 * 1024 + 1)
        assert upstream_notes("2.10.9") is None


def test_is_valid_ref():
    assert is_valid_ref("2.10.9")
    assert is_valid_ref("2.10.9-upnext.1")
    assert is_valid_ref("v1.0.0_beta-2")
    assert not is_valid_ref("../escape")
    assert not is_valid_ref("2.10.9\n## Injected")
    assert not is_valid_ref("tag;rm -rf /")
    assert not is_valid_ref("tag with spaces")
    assert not is_valid_ref("")


def test_main_rejects_invalid_version(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "changelog.py",
            "--version",
            "2.10.9\n## Injected",
            "--server-ref",
            "2.10.9",
        ],
    )
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert "invalid version format" in str(exc_info.value)


def test_main_rejects_invalid_server_ref(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "changelog.py",
            "--version",
            "2.10.9-upnext.1",
            "--server-ref",
            "../../escape",
        ],
    )
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert "invalid server-ref format" in str(exc_info.value)


def test_has_top_entry_when_matching(tmp_path):
    changelog = tmp_path / "CHANGELOG.md"
    changelog.write_text(
        f"{HEADER}\n## 2.10.9-upnext.1\n\nSome notes\n## 2.10.9-upnext.0\n"
    )
    assert has_top_entry(changelog, "2.10.9-upnext.1") is True
    assert has_top_entry(changelog, "2.10.9-upnext.0") is False
    assert has_top_entry(changelog, "2.10.9-upnext.2") is False


def test_has_top_entry_nonexistent_or_empty(tmp_path):
    changelog = tmp_path / "CHANGELOG.md"
    assert has_top_entry(changelog, "2.10.9-upnext.1") is False
    changelog.write_text("")
    assert has_top_entry(changelog, "2.10.9-upnext.1") is False


def test_main_exits_early_when_entry_exists(tmp_path, monkeypatch):
    changelog = tmp_path / "CHANGELOG.md"
    changelog.write_text(f"{HEADER}\n## 2.10.9-upnext.1\n\nSome notes\n")
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "changelog.py",
            "--version",
            "2.10.9-upnext.1",
            "--server-ref",
            "2.10.9",
            "--changelog",
            str(changelog),
        ],
    )
    with patch("scripts.changelog.build_entry") as mock_build_entry:
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert str(changelog) in str(exc_info.value)
        assert "already has an entry" in str(exc_info.value)
        mock_build_entry.assert_not_called()


def test_prepend_entry_nonexistent_file(tmp_path):
    changelog = tmp_path / "CHANGELOG.md"
    entry = "## 2.10.9-upnext.1\n\nFirst entry\n"
    prepend_entry(changelog, entry)
    assert changelog.read_text(encoding="utf-8") == f"{HEADER}\n{entry}"


def test_prepend_entry_multiple_entries(tmp_path):
    changelog = tmp_path / "CHANGELOG.md"
    entry1 = "## 2.10.9-upnext.1\n\nFirst entry\n"
    entry2 = "## 2.10.10-upnext.1\n\nSecond entry\n"
    prepend_entry(changelog, entry1)
    prepend_entry(changelog, entry2)
    expected = f"{HEADER}\n{entry2}\n{entry1}"
    assert changelog.read_text(encoding="utf-8") == expected


def test_prepend_entry_header_only_file(tmp_path):
    changelog = tmp_path / "CHANGELOG.md"
    changelog.write_text(HEADER, encoding="utf-8")
    entry = "## 2.10.9-upnext.1\n\nFirst entry\n"
    prepend_entry(changelog, entry)
    assert changelog.read_text(encoding="utf-8") == f"{HEADER}\n{entry}"
