---
title: Connect only the tools the task needs
tags: [practices, mcp, context, tools]
status: verified
updated: 2026-10-17
---

# Connect only the tools the task needs

Add an MCP server when the fact the agent needs lives outside the repo and changes often. Do not connect every server you own.

Codex's best-practices guide says: "Add tools only when they unlock a real workflow. Do not start by wiring in every tool you use. Start with one or two tools that clearly remove a manual loop you already do often, then expand from there." See [Best practices](https://developers.openai.com/codex/learn/best-practices).

## Add a server when

- The data is not in the repository, and pasting it would be stale by the next session.
- The same lookup is a manual loop you already repeat.
- The server is the approved path for that system. See [Security and data separation](07-security-and-data-separation.md).

## Leave it disconnected when

- The answer is already in the repo or in this library. Search first. See [Consult before building](01-consult-before-building.md).
- The server is for a different project. Extra tool definitions sit in the prompt and crowd out the task. See [Context and retrieval](03-context-and-retrieval.md).
- You have not used the workflow by hand yet. A server does not make an unclear task clear.

Disable a server when the task does not need it. Turn it back on for the session that does. The design for this library's own server stays in [MCP-Server/README.md](../MCP-Server/README.md). Until that server exists, use `Search-Index/search.py`.
