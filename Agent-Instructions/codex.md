---
title: Codex
tags: [agents, codex]
status: verified
updated: 2026-10-17
---

# Codex

Codex should use the same library as Cursor and Claude. Put the shared steps in Codex's global `AGENTS.md`, and point that file at this checkout.

## Global instructions

Include the [consultation protocol](consultation-protocol.md) in the global agent instructions so every new project inherits the search habit. Codex stops adding instruction files once their combined size reaches `project_doc_max_bytes`, which is 32 KiB by default. Keep the global file short and point at this repo. See [Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md).

Add the [project-start checklist](project-start-checklist.md) in projects that need a required search at kickoff.

## What Codex reads

- This repo for how to research, compare, verify, and record.
- The domain knowledge repo for that stack's engineering practices.
- The project for requirements and local decisions.

Codex should not copy this repo into each project.

## Current product behavior

Checked 2026-10-17 against the [Codex changelog](https://developers.openai.com/codex/changelog).

GPT-5.5 retired from Codex on October 14, 2026 for sessions signed in with ChatGPT. The changelog says: "The OpenAI API and Codex sessions authenticated with an API key aren't affected." Use `gpt-6.1-sol` when that model is available, and update saved defaults, custom agents, and scripts that still select `gpt-5.5`. Some other Codex pages still name GPT-5.5. Check the model picker in the client before you change a saved default.

Codex CLI 0.163.0 can take a follow-up while a turn is still running. That steers the current response instead of waiting for it to finish.

## MCP

When the local MCP server from [MCP-Server/README.md](../MCP-Server/README.md) exists, register it in the global Codex configuration. Until then, run `Search-Index/search.py`.
