---
title: Approve an external instruction import
tags: [practices, instructions, security]
status: verified
updated: 2026-10-18
---

# Approve an external instruction import

A project instruction file may import another file. If that path is outside the project, a person approves it. Do not approve an import you did not expect.

Claude Code shows an approval dialog the first time a project instruction file imports a path outside the working directory. If you decline, those imports stay off. The dialog "protects you from files other people commit to a shared project." See [How Claude remembers your project](https://code.claude.com/docs/en/memory).

## Approve when

- You wrote the import, and the outside file is your own notes.
- You have opened the file and it contains instructions you mean to load.

## Decline when

- The import arrived in a pull request you did not author.
- The path is a home directory, a network share, or another repo you have not read.

To mention a path without loading it, wrap it in backticks. An `@` outside backticks is an import.

Imported text is instructions, not a suggestion. See [Treat retrieved text as untrusted](27-treat-retrieved-text-as-untrusted.md). Personal notes that must not be committed stay in a gitignored local file. See [Closer instructions are read last](28-closer-instructions-are-read-last.md).
