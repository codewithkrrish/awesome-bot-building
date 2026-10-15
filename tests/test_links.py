"""Tests for scripts/check_links.py.

Only the URL extraction is tested here. The network checks are
deliberately untested -- hitting real servers in unit tests is slow,
flaky, and rude.
"""
import sys
from pathlib import Path

# check_links.py is a standalone script, not a package, so import it
# the scrappy way.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from check_links import extract_urls


def test_extracts_bare_and_markdown_urls_in_order():
    md = (
        "See https://example.com/a and [docs](https://example.com/b) "
        "then https://example.com/a again."
    )
    assert extract_urls(md) == [
        "https://example.com/a",
        "https://example.com/b",
    ]


def test_deduplicates_repeated_urls():
    md = "https://example.com/x then https://example.com/x"
    assert extract_urls(md) == ["https://example.com/x"]


def test_strips_trailing_punctuation():
    md = "Visit https://example.com/page, or https://example.com/other."
    assert extract_urls(md) == [
        "https://example.com/page",
        "https://example.com/other",
    ]


def test_ignores_non_urls():
    assert extract_urls("no links here, just words") == []


def test_empty_input():
    assert extract_urls("") == []
