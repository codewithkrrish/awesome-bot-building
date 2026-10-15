#!/usr/bin/env python3
"""Check every link in the markdown files and report the dead ones.

I run this before pushing list updates so the list never rots.
Network checks are slow and flaky by nature, so they stay out of the
unit tests -- tests/ only covers the URL extraction, which is the
part that can break silently.
"""
from __future__ import annotations

import re
import sys
import urllib.request
from pathlib import Path

URL_RE = re.compile(r"https?://[^\s)<>\"]+")
TIMEOUT = 15
ROOT = Path(__file__).resolve().parent.parent
FILES = [ROOT / "README.md", ROOT / "CONTRIBUTING.md"]
# Some sites block non-browser user agents; a 403 usually means
# "alive but rude", so it counts as fine here.
OK_CODES = {200, 301, 302, 403}


def extract_urls(markdown: str) -> list[str]:
    """Pull unique http(s) URLs out of markdown, in order of appearance."""
    seen: set[str] = set()
    urls: list[str] = []
    for match in URL_RE.finditer(markdown):
        # Trailing punctuation after a bare URL isn't part of the URL.
        url = match.group(0).rstrip(".,;!?:")
        if url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def check_url(url: str) -> int | None:
    """Return the HTTP status for url, or None if it's unreachable."""
    req = urllib.request.Request(
        url, headers={"User-Agent": "awesome-bot-building link check"}
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status
    except Exception:
        return None


def main() -> int:
    failures: list[str] = []
    total = 0
    for path in FILES:
        for url in extract_urls(path.read_text(encoding="utf-8")):
            total += 1
            status = check_url(url)
            mark = "ok" if status in OK_CODES else "BROKEN"
            print(f"[{mark}] {status} {url}")
            if status not in OK_CODES:
                failures.append(url)
    print(f"\n{total - len(failures)}/{total} links alive")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
