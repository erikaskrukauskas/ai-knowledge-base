---
title: Schedule only a reliable workflow
tags: [practices, skills, automation]
status: verified
updated: 2026-10-17
---

# Schedule only a reliable workflow

Schedule a task after you have run it by hand and the result is predictable. A skill defines the method. A schedule only defines when that method runs.

Codex's best-practices guide says: "If a workflow still needs a lot of steering, turn it into a skill first. Once it’s predictable, scheduling it can save time." Scheduling a recurring task before it is reliable manually is listed as a common mistake. See [Best practices](https://developers.openai.com/codex/learn/best-practices).

## Schedule when

- The same prompt, or a skill, has produced the right result more than once.
- The done check is a command or a review a later run can repeat. See [Verify and record](05-verify-and-record.md).
- The output is a summary, a scan, or a draft a person still accepts. Do not schedule an unreviewed write to a shared branch.

## Do not schedule when

- You are still changing the prompt every run.
- The workflow has no skill or written method. See [Choose a rule or a skill](13-choose-a-rule-or-a-skill.md).
- The run needs secrets, a production system, or a judgment you have not specified.

Keep the scheduled prompt short and point it at the skill. Put the steps in the skill, not in a new copy of the instructions on the schedule.
