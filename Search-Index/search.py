#!/usr/bin/env python3
"""Keyword search across the AI knowledge base.

Examples:
  python Search-Index/search.py --list
  python Search-Index/search.py "lesson status"
  python Search-Index/search.py --tag security
  python Search-Index/search.py --status verified retrieval
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".venv", "__pycache__", "Search-Index"}
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        data[key.strip().lower()] = value.strip().strip("\"'")
    return data


def iter_docs() -> list[Path]:
    docs: list[Path] = []
    for path in ROOT.rglob("*.md"):
        relative_parts = path.relative_to(ROOT).parts
        if any(part in SKIP_DIRS for part in relative_parts):
            continue
        docs.append(path)
    return sorted(docs)


def matches_meta(meta: dict[str, str], tag: str | None, status: str | None) -> bool:
    if tag and tag.lower() not in meta.get("tags", "").lower():
        return False
    if status and meta.get("status", "").lower() != status.lower():
        return False
    return True


def find_snippets(text: str, terms: list[str], limit: int = 2) -> list[str]:
    if not terms:
        return []
    lowered = text.lower()
    snippets: list[str] = []
    for term in terms:
        start = 0
        term_lower = term.lower()
        while len(snippets) < limit:
            index = lowered.find(term_lower, start)
            if index < 0:
                break
            left = max(0, index - 70)
            right = min(len(text), index + len(term) + 110)
            snippets.append(" ".join(text[left:right].split()))
            start = index + len(term_lower)
    return snippets[:limit]


def list_docs() -> int:
    docs = iter_docs()
    for path in docs:
        text = path.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        relative = path.relative_to(ROOT).as_posix()
        status = meta.get("status", "-")
        tags = meta.get("tags", "-")
        title = meta.get("title") or path.stem
        print(f"{relative}\t{status}\t{title}\t{tags}")
    print(f"{len(docs)} documents.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Search the AI knowledge base")
    parser.add_argument("query", nargs="*", help="Keywords that must all appear")
    parser.add_argument("--tag", help="Require this frontmatter tag")
    parser.add_argument("--status", help="Require this frontmatter status")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--list", action="store_true", help="List documents and exit")
    args = parser.parse_args()

    if args.list:
        return list_docs()

    terms = [term for term in args.query if term.strip()]
    if not terms and not args.tag and not args.status:
        parser.error("Provide keywords, --tag, --status, or --list")

    hits: list[tuple[str, str, str, list[str]]] = []
    for path in iter_docs():
        text = path.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        if not matches_meta(meta, args.tag, args.status):
            continue
        haystack = text.lower()
        if terms and not all(term.lower() in haystack for term in terms):
            continue
        hits.append(
            (
                path.relative_to(ROOT).as_posix(),
                meta.get("title") or path.stem,
                meta.get("status", ""),
                find_snippets(text, terms),
            )
        )

    if not hits:
        print("No matches.")
        return 0

    for relative, title, status, snippets in hits[: args.limit]:
        status_label = f" [{status}]" if status else ""
        print(f"{relative}{status_label}")
        print(f"  {title}")
        for snippet in snippets:
            print(f"  ... {snippet}")
        print()

    shown = min(len(hits), args.limit)
    print(f"{shown} shown, {len(hits)} matched.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
