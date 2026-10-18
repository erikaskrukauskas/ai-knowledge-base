---
title: Cloud agents have a wider blast radius
tags: [practices, security, agents, cloud]
status: verified
updated: 2026-10-17
---

# Cloud agents have a wider blast radius

A cloud agent is not a local agent with a longer runtime. It can auto-run commands and reach the network. Treat that as a different permission decision.

Cursor’s cloud agent security notes say the agent auto-runs terminal commands, unlike the foreground agent, which asks for approval. The agent has internet access by default. Auto-running "introduces data exfiltration risk" because a prompt-injection attack can trick the agent into uploading code. See [Secrets and network](https://cursor.com/docs/cloud-agent/security-network).

## Send work to the cloud when

- The task is safe to run on a copy of the repo without local secrets.
- Egress is restricted to the domains that task needs.
- Credentials are short-lived. Prefer federation over a long-lived cloud key. See [Security and data separation](07-security-and-data-separation.md).

## Keep it local when

- The workspace holds secrets, customer data, or a credential the agent could read.
- You have not yet seen which commands the task needs. See [Keep approval tight by default](18-keep-approval-tight-by-default.md).
- The policy hook lives only in your user directory. A cloud agent does not see that file. See [Use a hook to enforce](11-use-a-hook-to-enforce.md).

Text inside the repo or a web page is not a new instruction to raise permissions. See [Treat retrieved text as untrusted](27-treat-retrieved-text-as-untrusted.md).
