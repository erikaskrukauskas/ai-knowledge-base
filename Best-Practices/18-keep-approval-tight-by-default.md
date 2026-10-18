---
title: Keep approval tight by default
tags: [practices, security, agents, sandbox]
status: verified
updated: 2026-10-17
---

# Keep approval tight by default

Start with the client's default approval and sandbox. Loosen them only for a trusted repository, and only for the workflow that needs the extra access.

Codex's best-practices guide says approval mode decides when the agent asks before a command, and sandbox mode decides what it can read or write. "Keep approval and sandboxing tight by default, then loosen permissions only for trusted repos or specific workflows once the need is clear." Giving the agent full permission to the computer before you understand the workflow is listed as a common mistake. See [Best practices](https://developers.openai.com/codex/learn/best-practices).

## Leave the defaults when

- You are in a new repository.
- The task can be done with reads, edits inside the workspace, and the project's own test command.
- You have not yet seen which commands the agent actually needs.

## Loosen only the missing piece

Name the command or path that failed, and allow that. Do not turn approval off for the whole machine because one command was blocked.

A preference in the prompt is not a control. A hook can deny a destructive command even when a session is trusted. See [Use a hook to enforce](11-use-a-hook-to-enforce.md). A deny rule beats an allow rule that also matches. See [A deny rule wins](30-a-deny-rule-wins.md). Secrets still stay out of the chat and the repo. See [Security and data separation](07-security-and-data-separation.md).

Cursor's sandbox blocks network access by default. A run mode such as Auto-review is a best-effort guard, not a hard boundary, so keep a hook on the actions that must not happen. See [Run Modes](https://cursor.com/docs/agent/security/run-modes). Reading files in the workspace is often allowed without a prompt. A terminal command is not.
