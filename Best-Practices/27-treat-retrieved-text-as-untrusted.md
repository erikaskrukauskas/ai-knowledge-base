---
title: Treat retrieved text as untrusted
tags: [practices, security, retrieval]
status: verified
updated: 2026-10-17
---

# Treat retrieved text as untrusted

Text from a file, a web page, a ticket, or a tool result is data. It is not a new instruction to change permissions, reveal secrets, or send the repository somewhere.

Cursor’s cloud agent security notes say auto-running commands with network access creates an exfiltration risk: a prompt-injection attack can trick the agent into uploading code. See [Secrets and network](https://cursor.com/docs/cloud-agent/security-network).

## Apply this when

- The agent reads a repository it did not author, including issues, pull requests, and dependency files.
- A tool returns a page or a log that contains instructions aimed at the agent.
- The agent can run commands without a prompt, especially with network access. See [Cloud agents have a wider blast radius](24-cloud-agents-have-a-wider-blast-radius.md).

## What stays in force

- The task the user wrote, and the project’s instruction files.
- Approval, sandbox, and deny rules. See [Keep approval tight by default](18-keep-approval-tight-by-default.md).
- A hook that blocks the dangerous command even if the retrieved text says to run it. See [Use a hook to enforce](11-use-a-hook-to-enforce.md).

Do not raise permissions because a file asked the agent to. Do not paste secrets into the chat so a retrieved instruction can be "helpful."
