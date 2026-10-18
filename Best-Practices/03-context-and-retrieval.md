---
title: Context and retrieval
tags: [practices, retrieval, context]
status: verified
updated: 2026-10-17
---

# Context and retrieval

Load the slice that can change the decision. Leave the rest in the source file until a search shows it is relevant.

## What to retrieve

- The practice or lesson whose tags match the decision.
- The project's local rules and the files the change will touch.
- The current official page when the answer depends on a product's present behavior.
- A question that must not change files. Use a read-only mode for that pass. See [Answer without editing](14-answer-without-editing.md).

## What to avoid loading

- Whole books, whole manuals, or every lesson "for context."
- Superseded lessons, unless you need to understand why they were replaced.
- Project-specific decisions from an unrelated repository.
- Secrets, tokens, or private data that the task does not require.
- A long investigation that a subagent can return as a short result. See [Delegate to a subagent](10-delegate-to-a-subagent.md).

## Order of trust

1. The code, config, and tests in the project you are changing.
2. Current official documentation for the product version in use.
3. Verified lessons and best-practice pages.
4. Candidate lessons and model memory, which still need a check.

A verified lesson can be wrong after a product update. When the lesson and the current docs disagree, trust the docs for product behavior and mark the lesson for review.

## Search before pasting

Use keyword search in this repo first:

```powershell
python Search-Index/search.py --status verified "retrieval"
```

Semantic search, when the MCP service exists, supplements keywords. It does not replace reading the page that comes back.

## Citations

When a recommendation comes from this library or from official docs, name the file or page in the work notes. A later session can re-check the source instead of inheriting a paraphrase.
