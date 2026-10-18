---
title: Scope of this repository
tags: [scope, governance]
status: verified
updated: 2026-10-17
---

# Scope

This repository is the AI knowledge base. Other projects read it for practices, agent instructions, and verified lessons about working with AI tools.

## In this repo

- How to brief an agent, limit a change, and define done.
- How to search existing knowledge before implementing.
- How to compare approaches for significant AI-assisted changes.
- How to verify work and record a reusable lesson.
- How Codex, Claude, Cursor, and ChatGPT should share one library.
- MCP usage patterns for knowledge retrieval.
- Context discipline: what to load, what to leave in the source document.
- Separation of global AI practice from project-specific decisions.
- Separation of personal knowledge from proprietary company information.

## In other repos

| Topic | Where it lives |
| --- | --- |
| Data engineering | Its own knowledge repo |
| Data science | Its own knowledge repo |
| Application development | Its own knowledge repo |
| CI/CD | Its own knowledge repo |
| A single project's requirements, environments, and architecture decisions | That project |

A lesson about a Power BI refresh, a Fabric pipeline, a mobile screen, or a deployment workflow is recorded in the matching domain or project repo. If that work also produced a reusable AI-tooling lesson (for example, a better way to make an agent verify a fix), write only the AI-tooling lesson here and link to the domain write-up.

## Where a new note goes

Ask what a future agent in an unrelated project could reuse.

- If the answer is a way of working with AI tools, add it here.
- If the answer depends on a product, dataset, codebase, or release process outside AI tooling, add it to that domain repo or project.
- If both are true, split the note. This repo keeps the AI practice. The other repo keeps the domain solution.

## Global and project knowledge

Global knowledge in this repo applies across projects: prompting patterns, verification habits, lesson format, retrieval rules.

Project knowledge stays in the project: requirements, credentials locations, environment versions, local architecture choices, and test results that only make sense there.

Do not copy a project decision into this repo to make it feel official. Promote it only after it is stated as a practice that still holds without that project's constraints.
