---
title: Claude Code
tags: [agents, claude]
status: verified
updated: 2026-10-17
---

# Claude Code

Claude Code should follow the same consultation steps as Codex. The global file is `CLAUDE.md`.

## Global instructions

Add the [consultation protocol](consultation-protocol.md) to the global `CLAUDE.md`. Use the project's `CLAUDE.md` for constraints that are true only in that repository.

Do not paste a second copy of the best-practice guides into `CLAUDE.md`. Link to the page in this repo.

## MCP

Claude Code can use the same local MCP server as Codex once Phase 2 is built. Register that server in Claude's MCP configuration, not a separate knowledge store.

Until the server exists, search with:

```powershell
python "<path-to-ai-knowledge-base>\Search-Index\search.py" --status verified "<keywords>"
```

## Lessons

When Claude finds a reusable AI-tooling result, it writes the lesson here with status `candidate` or `tested`, using the template. It does not mark the lesson `verified` until the check in the lesson has been run.
