---
title: Official documentation
tags: [documentation, sources]
status: verified
updated: 2026-10-17
---

# Official documentation

Product behavior changes. Link to the current official page and record the version you checked. Do not paste manuals into this repo.

When a practice page and an official page disagree about a product feature, the official page for the version you run wins. Update or supersede the practice page afterward.

## AI tools and protocols

| Source | Entry | Use for |
| --- | --- | --- |
| Model Context Protocol | https://modelcontextprotocol.io/introduction | Tool contracts for the future knowledge server |
| Cursor docs | https://cursor.com/docs | Rules, agents, and editor behavior |
| Anthropic docs | https://docs.anthropic.com | Claude and Claude Code |
| OpenAI docs | https://platform.openai.com/docs | OpenAI API and agent products |

Confirm the exact page before you rely on a feature. These entry points are starting URLs, not a frozen specification.

## Update check

`check-ai-work-updates` scans Cursor, OpenAI, Anthropic, Claude Code, Codex, MCP, Stack Overflow, and Reddit for recent workflow changes. `review-covered-ai-topics` rechecks topics this library already documents. `add-uncovered-ai-topic` adds a topic that has no page yet. Source URLs and the fetch command are in `.cursor/skills/check-ai-work-updates/`. Checks write reports under `Official-Documentation/updates/`.

## How to add a source

Add a row with the official entry URL, the date you checked it, and the decision it supports. Keep domain product docs (warehouses, BI tools, mobile SDKs, CI vendors) in the domain knowledge repo that owns that subject.

## Local notes

If you need a short note about a documentation page, add a file next to this README:

- Name it for the topic, not the whole product.
- State the version and the date checked.
- Quote only the minimum needed to support a decision, with the URL.
- Link the note from the practice or lesson that depends on it.
