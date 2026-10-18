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

## Current product behavior

Checked 2026-10-17 against the [Claude Code changelog](https://code.claude.com/docs/en/changelog).

From version 2.1.299, a terminal conversation over 200K tokens that sits idle for about 54 minutes is compacted before the one-hour prompt cache expires. The next message may not see the full transcript. Project-root `CLAUDE.md` is read from disk again after compaction. Instructions that existed only in the conversation are not. Turn this off with the Idle compaction row in `/config`, or with `"idleCompaction": false` in settings.json on version 2.1.290 or later. See [What survives compaction](https://code.claude.com/docs/en/context-window).

`CLAUDE_CODE_DISABLE_FILE_MENTIONS` is optional. When it is set, an `@` file mention passes the path for Claude to read, not the file contents.

## MCP

Claude Code can use the same local MCP server as Codex once Phase 2 is built. Register that server in Claude's MCP configuration, not a separate knowledge store.

Until the server exists, search with:

```powershell
python "<path-to-ai-knowledge-base>\Search-Index\search.py" --status verified "<keywords>"
```

## Lessons

When Claude finds a reusable AI-tooling result, it writes the lesson here with status `candidate` or `tested`, using the template. It does not mark the lesson `verified` until the check in the lesson has been run.
