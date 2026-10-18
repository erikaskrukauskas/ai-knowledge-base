---
title: Project-start checklist
tags: [agents, workflow, retrieval]
status: verified
updated: 2026-10-17
---

# Project-start checklist

Global instructions encourage a search. This checklist is the stronger version: run it at the start of a project and again before a large change.

## Checklist

- [ ] Project agent instructions include the [consultation protocol](consultation-protocol.md) and the correct path to this repo.
- [ ] Domain knowledge repos for this stack are linked from the project README or `AGENTS.md`.
- [ ] Searched this repo for practices that match the work (`verification`, `retrieval`, `security`, or the tool name).
- [ ] Searched `Lessons-Learned/` for verified lessons in a similar environment.
- [ ] Confirmed product behavior that the design depends on, using current official docs and the versions in this environment.
- [ ] Stated where new lessons will go: AI tooling here, domain design in the domain repo, project facts in the project.

## After the work

- [ ] The named verification was run, and the result is recorded in the session notes.
- [ ] A lesson was added only if a later session would otherwise repeat the same investigation.
- [ ] No secrets, proprietary dumps, or copyrighted sources were copied into either knowledge repo.

## Optional later command

A `/review-best-practices` command can eventually walk a project against this library. Until that exists, this checklist is the review.
