---
title: Review in a fresh context
tags: [practices, verification, review]
status: verified
updated: 2026-10-18
---

# Review in a fresh context

The agent that wrote the change does not grade it. A review reads the diff and the done condition, not the author's chain of thought.

Claude Code's best-practices guide says a fresh context improves review "since Claude won't be biased toward code it just wrote," and that the agent doing the work should not be the one grading it. See [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices).

## Ask the reviewer to check

- The diff against the task, not against the author's explanation.
- Behavior that would break, data that would leak, and files outside the task's scope.
- Evidence: a `file:line` citation, a failing command, or a missing requirement. Not a guess from a name.

## What the review is not

An agent review does not merge, approve, or replace the check you named. A person still accepts the change. See [Verify and record](05-verify-and-record.md).

Hand the review to a subagent or a second session so the parent transcript stays out of the judgment. See [Delegate to a subagent](10-delegate-to-a-subagent.md). If that reviewer will edit, give it a separate checkout. See [Isolate parallel edits](19-isolate-parallel-edits.md).
