---
title: Restart after repeated corrections
tags: [practices, context, workflow]
status: verified
updated: 2026-10-18
---

# Restart after repeated corrections

If you correct the same mistake more than twice in one session, clear the session and start again with a tighter prompt. The failed attempts are now in the context.

Claude Code's best-practices guide says that after more than two corrections on the same issue, "the context is cluttered with failed approaches." `/clear` and a more specific prompt "almost always outperforms a long session with accumulated corrections." See [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices).

## Start the new session with

- The outcome and the constraint that was missing.
- The check that failed.
- What not to retry.

Leave the old transcript. Do not paste it in. See [One chat per outcome](17-one-chat-per-outcome.md).

If the same correction shows up in a later session, put it in the instruction file. See [Record a repeated correction](25-record-a-repeated-correction.md). A rewind is for undoing edits in this session, not for carrying a cluttered conversation forward. See [Checkpoints are not version control](23-checkpoints-are-not-version-control.md).
