---
title: Verify and record
tags: [practices, verification, lessons]
status: verified
updated: 2026-10-17
---

# Verify and record

A change is done when the check you named has been run and the result matches the task. A lesson is reusable when that check succeeded and the write-up says so.

## Verify

- Run the test, command, query, or review that the task called done.
- Cover the path you changed and the nearby path that shares its state or data.
- For a documentation change in this repo, search for the old wording and an existing page on the same topic.
- Report the command and the result. If a check could not be run, say which check and why.

## Record a lesson when

- The diagnosis took real investigation.
- An approach failed for a reason a later agent would repeat.
- The working approach is reusable beyond this one edit.
- A practice page was wrong or incomplete for a current tool version.

Skip the lesson when the fix was obvious and local.

## What the lesson must contain

Follow [Lessons-Learned/_template.md](../Lessons-Learned/_template.md).

- Problem and environment, including tool and version when that matters.
- Approaches that failed, and the evidence.
- The working solution.
- The check you ran and what it showed.
- Links to docs or practice pages.
- Scope: global AI practice, or a pointer to a project or domain repo.

## Lifecycle

| Status | Meaning |
| --- | --- |
| `candidate` | Captured, not yet re-checked |
| `tested` | Reproduced or reviewed in this environment |
| `verified` | Reliable enough for other sessions to apply |
| `superseded` | Replaced by a named newer document |

Move status forward with evidence. Do not delete a superseded lesson. Set `superseded_by` so old links still explain themselves.

Promote a repeated verified lesson into `Best-Practices/` when it has become a general rule. Leave the lesson in place as the evidence.
