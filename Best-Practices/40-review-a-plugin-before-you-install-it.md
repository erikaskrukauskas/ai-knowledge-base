---
title: Review a plugin before you install it
tags: [practices, plugins, security, mcp]
status: verified
updated: 2026-10-18
---

# Review a plugin before you install it

A plugin can add skills, hooks, subagents, and MCP servers in one install. Read what it adds before you trust it.

Claude Code's best-practices guide says plugins bundle those pieces into a single installable unit. See [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices). Cursor's hardening guide says to govern plugins and MCP servers by reviewing what they install and approving trusted sources. See [Security and Privacy Hardening](https://cursor.com/docs/enterprise/security-hardening).

## Install when

- You need that bundle, and you have looked at the hooks and servers it registers.
- The source is one you already trust for code that runs on the agent loop.

## Skip when

- You only needed one procedure. Copy or write that skill instead. See [Choose a rule or a skill](13-choose-a-rule-or-a-skill.md).
- The plugin's hook can run commands or its server can read data you have not approved. See [Use a hook to enforce](11-use-a-hook-to-enforce.md) and [Connect only the tools the task needs](15-connect-only-the-tools-the-task-needs.md).

A plugin is not a substitute for a practice in this library. If the behavior should apply to every project, write the practice here and keep the plugin's instructions short.
