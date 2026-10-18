---
title: Codex
tags: [agents, codex]
status: verified
updated: 2026-10-17
---

# Codex

Codex should use the same library as Cursor and Claude. Put the shared steps in Codex's global `AGENTS.md`, and point that file at this checkout.

## Global instructions

Include the [consultation protocol](consultation-protocol.md) in the global agent instructions so every new project inherits the search habit.

Add the [project-start checklist](project-start-checklist.md) in projects that need a required search at kickoff.

## What Codex reads

- This repo for how to research, compare, verify, and record.
- The domain knowledge repo for that stack's engineering practices.
- The project for requirements and local decisions.

Codex should not copy this repo into each project.

## MCP

When the local MCP server from [MCP-Server/README.md](../MCP-Server/README.md) exists, register it in the global Codex configuration. Until then, run `Search-Index/search.py`.
