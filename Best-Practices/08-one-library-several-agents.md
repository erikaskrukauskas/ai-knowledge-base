---
title: One library, several agents
tags: [practices, agents, mcp]
status: verified
updated: 2026-10-17
---

# One library, several agents

Codex, Claude, Cursor, and ChatGPT should read the same practices and the same lessons. Agent-specific files tell that product how to connect. They do not fork the guidance.

## Shared facts

- `Best-Practices/` is the canonical guidance.
- `Lessons-Learned/` is the canonical memory of session findings.
- `SCOPE.md` is the canonical boundary.

## Agent-specific files

Keep these short. They should point here and mention only what that product needs, such as a global `AGENTS.md`, `CLAUDE.md`, or a connector setting.

| Agent | Instruction file in this repo |
| --- | --- |
| Any project agent | [consultation-protocol.md](../Agent-Instructions/consultation-protocol.md) |
| Cursor | [cursor.md](../Agent-Instructions/cursor.md) |
| Codex | [codex.md](../Agent-Instructions/codex.md) |
| Claude Code | [claude.md](../Agent-Instructions/claude.md) |
| ChatGPT | [chatgpt.md](../Agent-Instructions/chatgpt.md) |

## Consistency rules

- A new practice is added once, then linked.
- A disagreement between agents is resolved by editing the canonical page, not by adding a second opinion beside it.
- Product limits stay in the agent file. Example: ChatGPT may need an approved remote connector, while Codex and Claude can use a later local MCP server.
- When a product cannot search this repo directly, the person or the other agent retrieves the page and includes the relevant excerpt in the task.

## Global instructions and hard checks

Put the consultation steps in the global instructions for each agent so new projects inherit them. Add the project-start checklist in projects that need a required search at the beginning of work.
