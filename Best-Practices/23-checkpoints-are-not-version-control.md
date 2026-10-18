---
title: Checkpoints are not version control
tags: [practices, verification, workflow]
status: verified
updated: 2026-10-17
---

# Checkpoints are not version control

Use a checkpoint or rewind to undo the agent’s recent file edits in this session. Use Git when the history has to last, be shared, or survive a command the checkpoint does not track.

Claude Code’s checkpointing docs say checkpoints are "for quick, session-level recovery" and are "not a replacement for version control." Rewind can restore code, the conversation, or both, or summarize part of the transcript. It does not track files changed by shell commands such as `rm`, `mv`, or `cp`. Subagent edits outside a foreground forked skill are often left in place. Symlinked and hard-linked paths are skipped. See [Checkpointing](https://code.claude.com/docs/en/checkpointing).

Cursor’s agent overview says restoring a checkpoint reverts files only and does not remove messages. Checkpoints are local and separate from Git. See [Cursor Agent](https://cursor.com/docs/agent/overview).

## Restore from a checkpoint when

- An experiment in this session went the wrong way and Git does not yet contain it.
- You want the conversation back at the prompt that started the bad turn.

## Use Git when

- The change should be reviewed, shared, or kept.
- A shell command, another session, or a subagent changed files the rewind will not put back.
- You are isolating parallel edits. See [Isolate parallel edits](19-isolate-parallel-edits.md).

Summarizing the transcript does not change files on disk. Compact or summarize when the chat is still the right one and only the context is too long. See [One chat per outcome](17-one-chat-per-outcome.md).
