---
title: Covered topic review 2026-10-17
tags: [documentation, updates]
status: verified
updated: 2026-10-17
---

# Covered topic review

Checked: 2026-10-17

## Updated

- **Agent-Instructions/claude.md** — After idle compaction, project-root `CLAUDE.md` is read from disk again. Instructions that lived only in the conversation are not. Idle compaction can also be turned off with `"idleCompaction": false` on Claude Code 2.1.290 or later. [What survives compaction](https://code.claude.com/docs/en/context-window)
- **Agent-Instructions/codex.md** — Codex stops merging `AGENTS.md` files at `project_doc_max_bytes`, 32 KiB by default. [Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md)
- **Agent-Instructions/codex.md** — The October 14 changelog still retires GPT-5.5 for ChatGPT sign-in and leaves API-key sessions unchanged. Other Codex pages still name GPT-5.5, so the page now says to check the model picker before changing a saved default. [Changelog](https://developers.openai.com/codex/changelog)

## Still current

- Best-Practices/01 through 09 — library rules for consulting, specifying, retrieving, comparing, verifying, separating scope, keeping secrets out of git, sharing one library, and writing searchable pages. No primary source contradicted them.
- Best-Practices/03-context-and-retrieval.md — order of trust still matches the library. A pointer to the new subagent page was added while covering that missing topic.
- Agent-Instructions/cursor.md — `AGENTS.md`, rules, and skills remain the Cursor instruction mechanisms. [Rules](https://cursor.com/docs/rules) and [Agent Skills](https://cursor.com/docs/skills). No newer changelog item reversed the auto-review or `/skills` limit notes.
- Agent-Instructions/claude.md — `CLAUDE.md` is still the Claude Code instruction file. [CLAUDE.md](https://code.claude.com/docs/en/claude-md). The file-mention environment variable is unchanged in the changelog.
- Agent-Instructions/codex.md — Codex still reads `AGENTS.md` before work. Steering in CLI 0.163.0 was not reversed.
- Agent-Instructions/chatgpt.md — release notes since October 15 are voice and Sites limits, not a knowledge-base connector.
- Agent-Instructions/consultation-protocol.md and project-start-checklist.md — still match the library boundary.
- Lessons-Learned/LL-0001-scope-ai-knowledge-only.md — this repo is still AI knowledge only.
- MCP-Server/README.md — the draft changelog is still empty, and this repo still has no MCP server.

## Unconfirmed

- Reddit r/ClaudeAI, r/OpenAI, and r/ChatGPTCoding returned HTTP 429. No community lead was confirmed on a primary page, so no practice was changed from those feeds.
- Codex speed and pricing pages still list GPT-5.5, which disagrees with the retirement changelog. The client model picker is the check before a saved default is changed.
