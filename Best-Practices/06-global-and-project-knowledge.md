---
title: Global and project knowledge
tags: [practices, scope, lessons]
status: verified
updated: 2026-10-17
---

# Global and project knowledge

Keep two levels, and write each fact at the level where it stays true.

## Global AI knowledge

Lives in this repo when it still holds in another project:

- How to search, compare, verify, and record.
- How to configure agents to share one library.
- Patterns for MCP tools, prompts, and context limits.
- Verified lessons about AI tools that name their environment clearly enough to reuse.

## Project knowledge

Lives in the project:

- Requirements and acceptance checks.
- Environment names, URLs, and where secrets are stored (never the secret values in git).
- Architecture decisions that depend on that product's constraints.
- Test outputs and benchmarks for that codebase.

## Domain knowledge

Lives in the domain repo:

- Data engineering practices.
- Data science practices.
- Application development practices.
- CI/CD practices.

## Promotion rule

A project solution becomes global AI knowledge only after you remove the project-specific parts and the remaining statement is still useful. If nothing remains, keep it in the project.

## Application rule

Before applying a lesson from this repo, check its environment and status. A verified lesson about one agent version is a hypothesis for a different version until you confirm it.
