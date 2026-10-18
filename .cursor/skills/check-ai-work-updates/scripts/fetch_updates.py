#!/usr/bin/env python3
"""Fetch recent AI-work updates from the source list.

Prints feed items and page URLs. Does not decide which items matter.
"""

from __future__ import annotations

import argparse
import email.utils
import html
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

USER_AGENT = "ai-knowledge-base-update-check/1.0"
SOURCES_PATH = Path(__file__).resolve().parent.parent / "sources.md"
TAG = re.compile(r"\{.*\}")


def configure_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def load_sources(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"```sources\n(.*?)```", text, re.DOTALL)
    if not match:
        raise SystemExit(f"No sources block in {path}")
    sources: list[dict[str, str]] = []
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        kind, name, url, tier = [part.strip() for part in line.split("\t")]
        sources.append({"kind": kind, "name": name, "url": url, "tier": tier})
    return sources


def local(tag: str) -> str:
    return TAG.sub("", tag)


def text_of(node: ET.Element | None) -> str:
    if node is None or node.text is None:
        return ""
    return " ".join(node.text.split())


def strip_markup(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"<[^>]+>", " ", value)
    return " ".join(value.split())


def parse_date(value: str) -> datetime | None:
    value = value.strip()
    if not value:
        return None
    try:
        parsed = email.utils.parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except (TypeError, ValueError, IndexError):
        pass
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except ValueError:
        return None


def child_text(parent: ET.Element, names: set[str]) -> str:
    matches: list[str] = []
    for child in parent:
        if local(child.tag) not in names:
            continue
        value = " ".join("".join(child.itertext()).split())
        if value:
            matches.append(value)
    if not matches:
        return ""
    return max(matches, key=len)


def link_of(parent: ET.Element) -> str:
    for child in parent:
        if local(child.tag) != "link":
            continue
        href = child.attrib.get("href")
        if href:
            return href
        if child.text and child.text.strip():
            return child.text.strip()
    return ""


def items_from_xml(payload: str) -> list[dict[str, str]]:
    root = ET.fromstring(payload)
    nodes = [node for node in root.iter() if local(node.tag) in {"item", "entry"}]
    items: list[dict[str, str]] = []
    for node in nodes:
        title = strip_markup(child_text(node, {"title"})) or "(untitled)"
        link = link_of(node)
        published = child_text(node, {"pubDate", "published", "updated", "date"})
        summary = child_text(node, {"description", "summary", "content", "encoded"})
        items.append(
            {
                "title": title,
                "link": link,
                "published": published,
                "summary": strip_markup(summary)[:500],
            }
        )
    return items


def fetch(url: str, timeout: int) -> tuple[int, str]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    delays = (0, 5)
    last_error: urllib.error.HTTPError | None = None
    for delay in delays:
        if delay:
            time.sleep(delay)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                body = response.read().decode("utf-8", errors="replace")
                return response.status, body
        except urllib.error.HTTPError as error:
            last_error = error
            if error.code != 429:
                raise
    if last_error is not None:
        raise last_error
    raise RuntimeError(f"Failed to fetch {url}")


def within_window(published: str, cutoff: datetime) -> bool:
    parsed = parse_date(published)
    if parsed is None:
        return True
    return parsed >= cutoff


def main() -> int:
    configure_stdout()
    parser = argparse.ArgumentParser(description="Fetch AI work update sources")
    parser.add_argument("--days", type=int, default=14, help="Primary feed window")
    parser.add_argument("--limit", type=int, default=8, help="Max items per source")
    parser.add_argument("--tier", choices=["primary", "community", "all"], default="all")
    args = parser.parse_args()

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    sources = load_sources(SOURCES_PATH)
    failures: list[str] = []

    print(f"Window start (UTC): {cutoff.date().isoformat()}")
    print(f"Days: {args.days}")
    print()

    for index, source in enumerate(sources):
        if args.tier != "all" and source["tier"] != args.tier:
            continue
        if index:
            time.sleep(8 if "reddit.com" in source["url"] else 0.5)
        print(f"## {source['name']} [{source['tier']}]")
        print(source["url"])
        if source["kind"] == "page":
            print("Open this page and keep items inside the window.")
            print()
            continue
        try:
            status, body = fetch(source["url"], timeout=25)
        except urllib.error.HTTPError as error:
            failures.append(f"{source['name']}: HTTP {error.code}")
            print(f"FAILED HTTP {error.code}")
            if "reddit.com" in source["url"] and "/top/" in source["url"]:
                page = source["url"].split("/top/")[0] + "/top/?t=week"
                print(f"Open {page}")
            if "stackoverflow.com/feeds/tag" in source["url"]:
                print(
                    "Open https://stackoverflow.com/questions/tagged/"
                    "openai+or+claude+or+anthropic+or+chatgpt+or+codex+"
                    "or+model-context-protocol?sort=newest"
                )
            print()
            continue
        except Exception as error:  # noqa: BLE001 - report and continue
            failures.append(f"{source['name']}: {error}")
            print(f"FAILED {error}")
            print()
            continue
        try:
            items = sorted(
                items_from_xml(body),
                key=lambda item: parse_date(item["published"]) or datetime.min.replace(tzinfo=timezone.utc),
                reverse=True,
            )
        except ET.ParseError as error:
            failures.append(f"{source['name']}: XML parse error")
            print(f"FAILED XML ({status}): {error}")
            print()
            continue

        shown = 0
        for item in items:
            if not within_window(item["published"], cutoff):
                continue
            published = item["published"] or "date unknown"
            print(f"- {published} | {item['title']}")
            if item["link"]:
                print(f"  {item['link']}")
            if item["summary"]:
                print(f"  {item['summary']}")
            shown += 1
            if shown >= args.limit:
                break
        if shown == 0:
            print("- No items in the window.")
        print()

    if failures:
        print("## Failures")
        for failure in failures:
            print(f"- {failure}")
        print("Open a failed source's page directly before treating it as empty.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
