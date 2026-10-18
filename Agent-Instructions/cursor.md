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

## Rules and skills

Create a Cursor rule or skill in a project only when that project needs a repeated local behavior. If the guidance applies to every project, add it under `Best-Practices/` and link it.
