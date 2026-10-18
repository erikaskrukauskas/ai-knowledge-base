---
id: LL-0001
title: Keep this repo to AI knowledge
tags: [lessons, scope, governance]
status: verified
updated: 2026-10-17
environment: "Cursor, Windows, ai-knowledge-base repo"
scope: global
superseded_by:
---

# Keep this repo to AI knowledge

## Problem

The original knowledge-base proposal covered Power BI, Microsoft Fabric, SAP HANA, data engineering, software engineering, and systems analysis in one library. Domain notes in this repo would be copied into unrelated AI sessions and would duplicate repos that are meant to own those subjects.

## Approaches that failed

- Approach: Plan one engineering library that holds every domain plus AI workflow.
- Why it failed: Data engineering, data science, app development, and CI/CD are each getting their own repo. Mixing them here makes search results noisier and encourages agents to apply a domain decision outside its project.
- Evidence: Scope decision for this repository, 2026-10-17.

## Working solution

Use this repository only for AI engineering knowledge: agent practices, retrieval, verification, lesson capture, and multi-agent setup.

Put domain practices in the domain repo. Put requirements, environments, and architecture decisions in the project. When one effort produces both a domain fix and an AI-tooling lesson, write both and link them. See [SCOPE.md](../SCOPE.md).

## Verification

- Check run: Scope review against the repository decision and the folder layout.
- Result: Root docs and best-practice pages describe AI workflow only. Domain systems appear as examples of what belongs elsewhere.

## Scope

`global` for any future knowledge repo or project that consults this one.

## References

- [SCOPE.md](../SCOPE.md)
- [Global and project knowledge](../Best-Practices/06-global-and-project-knowledge.md)
