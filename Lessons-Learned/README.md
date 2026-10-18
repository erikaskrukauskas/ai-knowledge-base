---
title: Lessons learned
tags: [lessons, index]
status: verified
updated: 2026-10-17
---

# Lessons learned

Lessons are findings from real sessions. Best-practice pages are the stable rules. A lesson graduates into a practice page only after it holds up beyond the original case.

## Lifecycle

`candidate` → `tested` → `verified` → reusable knowledge

| Status | Set it when |
| --- | --- |
| `candidate` | You wrote down the finding and it is not re-checked yet |
| `tested` | You reproduced the result or reviewed the evidence in this environment |
| `verified` | Another session can apply it without re-discovering the dead ends |
| `superseded` | A newer lesson or practice page replaces it |

Superseded files stay in the folder. Set `superseded_by` to the replacement path. Do not silently delete them.

## File names

`LL-0001-short-slug.md`

Increment the number. Do not reuse an id.

## What to record

Use [_template.md](_template.md). A useful lesson includes the environment, the failed approaches, the working approach, and the check that showed it worked.

Record an AI-tooling lesson here. Record a domain solution in the domain repo, and link it from the lesson if both exist.

## Current lessons

| ID | Title | Status |
| --- | --- | --- |
| [LL-0001](LL-0001-scope-ai-knowledge-only.md) | Keep this repo to AI knowledge | verified |
