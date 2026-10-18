---
title: Cursor
tags: [agents, cursor]
status: verified
updated: 2026-10-17
---

# Cursor

Cursor is the day-to-day editor for this library and for projects that read it.

## This repo

`AGENTS.md` at the root tells agents how to maintain the library: AI knowledge only, frontmatter, lesson status, and no secrets or copied books.

## Other projects

Add the [consultation protocol](consultation-protocol.md) to the project's `AGENTS.md`. That file is the durable place for project rules. A chat reminder disappears with the session.

Keep the protocol short. Link here for the full practice instead of pasting every best-practice page into the project.

## Search from a project

From any working directory:

```powershell
python "<path-to-ai-knowledge-base>\Search-Index\search.py" "verify and record"
```

Phase 2 can replace that command with an MCP tool. The protocol text can then say "call the knowledge search tool" without changing the practices.

## Current product behavior

Checked 2026-10-17 against the [Cursor release notes](https://cursor.com/docs/release-notes).

IDE 3.24 and CLI v2026.10.08 ask for approval before a recursive, force, wildcard, or mirror delete whose target could resolve differently than written.

`/skills` warns when a skill exceeds Agent Skills limits, including a description over 1,024 characters or a body over about 5,000 tokens.

## Rules and skills

Create a Cursor rule or skill in a project only when that project needs a repeated local behavior. If the guidance applies to every project, add it under `Best-Practices/` and link it.
