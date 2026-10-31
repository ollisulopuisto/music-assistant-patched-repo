from unittest.mock import patch

from scripts.changelog import upstream_notes


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
