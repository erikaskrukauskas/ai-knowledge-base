---
title: Compare, then implement
tags: [practices, design, workflow]
status: verified
updated: 2026-10-17
---

# Compare, then implement

For a significant change, state the realistic options, the constraint that decides among them, and the option you will implement. Then implement that option.

## When to compare

Compare when more than one design could satisfy the task and the wrong choice is expensive to unwind: a public interface, a storage choice, an agent tool contract, a security boundary, or a workflow other projects will copy.

## What a comparison contains

- Two or three options that could actually be built here.
- The constraint that matters for this task: operability, reversibility, verification, scope fit, or current product support.
- The option you will implement.
- What you looked at: a practice page, a lesson, official docs, or the existing code.

Skip the comparison write-up for a local fix with one obvious edit. For a large or unclear change, get the plan approved before editing. See [Plan before a large change](12-plan-before-a-large-change.md).

## Check the version

If an option depends on a product feature, confirm it in current official documentation and in the version this environment runs. A blog post or an older lesson is a lead, not proof that the feature exists here.

## Then implement

After the choice is made, change the code or docs to match that choice. Do not leave two half-implemented designs in the tree.

Record the comparison in the project decision log when it is project-specific. Record it in this repo only when the chosen practice should apply to later AI-assisted work in other projects.
