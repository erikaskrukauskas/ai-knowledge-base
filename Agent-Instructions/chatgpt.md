---
title: ChatGPT
tags: [agents, chatgpt]
status: verified
updated: 2026-10-17
---

# ChatGPT

ChatGPT uses the same practices and lessons. The connection method differs.

## Now

Work that starts in ChatGPT can still use this library:

- Retrieve the relevant page locally with `Search-Index/search.py`.
- Paste the relevant section into the ChatGPT task, with the file path.
- Ask ChatGPT to follow that section.

That keeps one canonical copy. A summary pasted into a chat is not a second source of truth.

## Later

Remote use needs an authenticated connector or API, and an explicit decision about which documents are exposed. Company content stays in an approved store. Personal notes stay in a personal store. This repo's remote index should include only documents cleared for that channel.

Product capabilities and organizational approval determine whether a ChatGPT connector is available. Do not assume a local MCP config on this PC is visible to ChatGPT.

## Same rules

ChatGPT output that will be reused is still subject to [Verify and record](../Best-Practices/05-verify-and-record.md). A suggestion becomes a lesson after a check, not when the chat ends.
