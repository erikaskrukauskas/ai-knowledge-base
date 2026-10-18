---
title: An ignore file is not a lock
tags: [practices, security, context, retrieval]
status: verified
updated: 2026-10-17
---

# An ignore file is not a lock

Use an ignore file to keep secrets and irrelevant trees out of agent reads and `@` mentions. Do not treat it as the control that stops a shell command or an MCP tool.

Cursor's ignore-file docs say `.cursorignore` blocks code used by Agent, Tab, Inline Edit, and `@` mentions. "The terminal and MCP server tools used by Agent cannot block access to code governed by `.cursorignore`." The safety docs also say it "is not a security boundary." See [Ignore file](https://cursor.com/docs/reference/ignore-file).

## Ignore

- Secret files, credentials, and keys. See [Security and data separation](07-security-and-data-separation.md).
- Generated output, lockfiles you do not want searched, and trees that drown retrieval. See [Context and retrieval](03-context-and-retrieval.md).

## Still required

- File-system permissions or encryption for data the agent must not be able to read.
- Approval, a sandbox, or a hook for shell and MCP, because those tools do not honor the ignore file. See [Use a hook to enforce](11-use-a-hook-to-enforce.md).

A global ignore pattern is useful for `.env` and key files in every project. A project ignore file is for that repository's layout.
