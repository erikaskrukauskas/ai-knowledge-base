---
title: One chat per outcome
tags: [practices, context, workflow]
status: verified
updated: 2026-10-18
---

# One chat per outcome

Keep one chat for one coherent outcome. Stay in that chat while the work is still the same problem. Fork when the work branches. Start a new chat when the outcome is different.

Codex's best-practices guide says to keep one chat per coherent unit of work, because staying in the same chat preserves the reasoning trail, and to fork only when the work truly branches. Using one chat for an entire project "leads to bloated context and worse results over time." See [Best practices](https://developers.openai.com/codex/learn/best-practices).

## Stay

- A follow-up that corrects the same change.
- A review of the diff the chat just produced.
- A test run for the outcome this chat owns.

## Fork or start over

- Fork when you want to try a second design without losing the first transcript.
- Start a new chat when the next task has a different done condition. See [Specify the task](02-specify-the-task.md).
- Hand a long side investigation to a subagent instead of pasting it into the parent. See [Delegate to a subagent](10-delegate-to-a-subagent.md).

When the same chat is still the right one but the transcript is long, compact it. In Codex, `/compact` summarizes earlier context. Durable instructions belong in `AGENTS.md` or `CLAUDE.md`, which are read again after compaction, not in the old transcript. See [Context and retrieval](03-context-and-retrieval.md).

Name the session after the outcome so you can resume it later. A side question that should not stay in the transcript uses a side channel such as `/btw`, which answers without adding to the conversation. See [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices).
