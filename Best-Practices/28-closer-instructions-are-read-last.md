---
title: Closer instructions are read last
tags: [practices, instructions, agents]
status: verified
updated: 2026-10-17
---

# Closer instructions are read last

When two instruction files disagree, the one closer to the working directory is the one the agent reads last. Do not leave both in place and hope the root file wins.

Claude Code loads instruction files from the root down toward the working directory, so "instructions closer to where you launched Claude are read last." See [How Claude remembers your project](https://code.claude.com/docs/en/memory). Codex concatenates `AGENTS.md` the same way: "Files closer to your current directory override earlier guidance because they appear later in the combined prompt." See [Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md).

## Write it at the narrowest true level

- A habit for every project stays in the global file and in this library.
- A rule for one directory lives in that directory.
- A personal preference that must not be committed stays in a local file that Git ignores.

## When they conflict

Delete or rewrite the stale line. Claude may pick either side of a contradiction. Nested files are combined, not a full replacement, so an old root rule still occupies context. See [Context and retrieval](03-context-and-retrieval.md).

Codex also stops adding files at `project_doc_max_bytes` (32 KiB by default). A closer file that never loads cannot correct the root file. See [Codex](../Agent-Instructions/codex.md).
