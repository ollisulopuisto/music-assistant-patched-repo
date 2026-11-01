from unittest.mock import patch

from scripts.changelog import patch_title, upstream_notes


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
    with patch("urllib.request.urlopen") as mock_urlopen:
        mock_response = mock_urlopen.return_value.__enter__.return_value
        mock_response.read.return_value = b'{"body": "## Notes"}'
        # Using json.load on response
        with patch("json.load", return_value={"body": "## Notes"}):
            notes = upstream_notes("2.10.9")
            assert notes is not None
            assert "#### Notes" in notes


def test_upstream_notes_rejects_path_traversal():
    with patch("urllib.request.urlopen") as mock_urlopen:
        assert upstream_notes("../../tags") is None
        assert upstream_notes("foo/../../bar") is None
        assert upstream_notes("..") is None
        mock_urlopen.assert_not_called()


def test_upstream_notes_rejects_invalid_characters():
    with patch("urllib.request.urlopen") as mock_urlopen:
        assert upstream_notes("tag;evil") is None
        assert upstream_notes("tag with spaces") is None
        assert upstream_notes("tag?query=1") is None
        assert upstream_notes("tag#hash") is None
        assert upstream_notes("tag@other") is None
        mock_urlopen.assert_not_called()
