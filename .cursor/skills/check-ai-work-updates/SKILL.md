---
name: check-ai-work-updates
description: >-
  Check Cursor, OpenAI, Anthropic, Claude Code, Codex, MCP, Stack Overflow,
  and Reddit for updates that change how to work with AI agents. Use when the
  user asks what changed in Cursor, Claude, Codex, ChatGPT, MCP, or agent
  workflows, or asks to scan changelogs, release notes, docs, and top
  community posts.
---

# Check AI work updates

Scan the source list and report changes that affect how agents and people work with AI. Ignore funding, partnerships, and benchmark news that does not change a workflow.

To add a topic this repo does not yet cover, use [add-uncovered-ai-topic](../add-uncovered-ai-topic/SKILL.md). To recheck claims already written down, use [review-covered-ai-topics](../review-covered-ai-topics/SKILL.md).

## Run

From this repository:

```bash
python .cursor/skills/check-ai-work-updates/scripts/fetch_updates.py --days 14
```

Use `--days 7` for a shorter pass. Use `--tier primary` to skip Reddit and Stack Overflow. The source URLs live in [sources.md](sources.md).

Then open every `page` line with WebFetch. Read the item, not just the title, before you call it a workflow change.

When a `community` feed fails, search the web for recent posts from that community about agent workflows, rules, skills, or MCP. For Stack Overflow, open the tagged questions page. Keep posts from the same window. A failed community feed is not an empty community.

On the first check, use 14 days. On a later check, start at the date of the newest file in `Official-Documentation/updates/`.

## Keep an item when it changes

- Agent instructions, rules, skills, hooks, or MCP tool behavior
- Cursor, Codex, Claude Code, or ChatGPT workflows
- Context, retrieval, verification, or lesson-capture habits
- A model or API default that changes how a task should be prompted or checked
- A deprecation or removal of a feature this library documents

Drop an item when it is a launch announcement, a benchmark, a funding note, or a domain topic owned by another knowledge repo.

Treat Reddit and other `community` items as leads. Confirm the claim on a `primary` page before you edit a practice.

## Report

Put this in the chat:

```markdown
# AI work updates
Checked: YYYY-MM-DD
Window: YYYY-MM-DD to YYYY-MM-DD

## Changes a documented practice
- **Source — title** (date) — what changed — page to edit — [url](url)

## Worth knowing
- **Source — title** (date) — why it matters — [url](url)

## Checked and quiet
- Source names with no workflow change, plus any feed that failed
```

Quote only the sentence needed to support the decision, with the URL. Do not paste release notes into the repo.

## Update this library

Write the same report to `Official-Documentation/updates/YYYY-MM-DD.md` with the usual frontmatter (`title`, `tags: [documentation, updates]`, `status: verified`, `updated`).

Edit a page in `Best-Practices/` or `Agent-Instructions/` only when a primary source contradicts or extends that page. Set its `updated` date. Leave `status` as it was unless the page is now wrong enough to mark `superseded`.

A changelog is not a lesson. Add a lesson only when this environment was tested against the change.

Dedupe items that appear in more than one feed. Prefer the official changelog URL.
