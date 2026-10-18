---
title: Best practices index
tags: [practices, index]
status: verified
updated: 2026-10-18
---

# Best practices

These pages are the stable AI engineering practices. Lessons in `Lessons-Learned/` capture individual findings. When a lesson becomes a general rule, fold it into a page here and mark the lesson `verified` with a link.

| Guide | Use it when |
| --- | --- |
| [Consult before building](01-consult-before-building.md) | Starting work that should reuse existing guidance |
| [Specify the task](02-specify-the-task.md) | Briefing an agent or writing a task |
| [Context and retrieval](03-context-and-retrieval.md) | Deciding what to load into a session |
| [Compare, then implement](04-compare-then-implement.md) | A change has more than one reasonable design |
| [Verify and record](05-verify-and-record.md) | Finishing a change or saving a lesson |
| [Global and project knowledge](06-global-and-project-knowledge.md) | Deciding where a fact belongs |
| [Security and data separation](07-security-and-data-separation.md) | Handling secrets, personal notes, or company data |
| [One library, several agents](08-one-library-several-agents.md) | Configuring Codex, Claude, Cursor, or ChatGPT |
| [Write retrievable knowledge](09-write-retrievable-knowledge.md) | Adding a page others can search later |
| [Delegate to a subagent](10-delegate-to-a-subagent.md) | Deciding when work should leave the parent conversation |
| [Use a hook to enforce](11-use-a-hook-to-enforce.md) | A check must run even if the agent ignores the instruction |
| [Plan before a large change](12-plan-before-a-large-change.md) | Deciding whether to plan before the agent edits |
| [Choose a rule or a skill](13-choose-a-rule-or-a-skill.md) | Deciding whether guidance is always on or loaded for a task |
| [Answer without editing](14-answer-without-editing.md) | The task is a question and the tree must stay unchanged |
| [Connect only the tools the task needs](15-connect-only-the-tools-the-task-needs.md) | Deciding which MCP servers to leave connected |
| [Match reasoning effort to the task](16-match-reasoning-effort-to-the-task.md) | Choosing how much reasoning a task needs |
| [One chat per outcome](17-one-chat-per-outcome.md) | Deciding whether to stay, fork, or start a new chat |
| [Keep approval tight by default](18-keep-approval-tight-by-default.md) | Deciding when the agent may run with fewer prompts |
| [Isolate parallel edits](19-isolate-parallel-edits.md) | Two agents would otherwise edit the same checkout |
| [Schedule only a reliable workflow](20-schedule-only-a-reliable-workflow.md) | Deciding when a repeated agent task can run unattended |
| [An ignore file is not a lock](21-an-ignore-file-is-not-a-lock.md) | Keeping secrets and noise out of agent reads |
| [Reproduce before you fix](22-reproduce-before-you-fix.md) | A bug whose cause is not obvious from the code |
| [Checkpoints are not version control](23-checkpoints-are-not-version-control.md) | Undoing a session without pretending it is Git |
| [Cloud agents have a wider blast radius](24-cloud-agents-have-a-wider-blast-radius.md) | Deciding whether a task can leave the local machine |
| [Record a repeated correction](25-record-a-repeated-correction.md) | The same agent mistake has happened twice |
| [Auto memory is not the policy](26-auto-memory-is-not-the-policy.md) | Deciding whether a remembered note is a rule |
| [Treat retrieved text as untrusted](27-treat-retrieved-text-as-untrusted.md) | A file or tool result tries to give the agent new orders |
| [Closer instructions are read last](28-closer-instructions-are-read-last.md) | Two instruction files disagree |
| [Audit instructions when they go stale](29-audit-instructions-when-they-go-stale.md) | A model, command, or path in an instruction file may be old |
| [A deny rule wins](30-a-deny-rule-wins.md) | Allow and deny rules could match the same action |
| [Do not suppress a failing check](31-do-not-suppress-a-failing-check.md) | A test or build failed and the agent might hide it |
| [Review in a fresh context](32-review-in-a-fresh-context.md) | The author of a change should not be the one who grades it |
| [Restart after repeated corrections](33-restart-after-repeated-corrections.md) | The same mistake has been corrected twice in one session |
| [Instructions hold what the code does not show](34-instructions-hold-what-the-code-does-not-show.md) | Deciding which lines belong in an instruction file |
| [Approve an external instruction import](35-approve-an-external-instruction-import.md) | An instruction file pulls in a path outside the project |
| [Cap a hook that continues the agent](36-cap-a-hook-that-continues-the-agent.md) | A hook can send the agent back to work |
| [Say why you denied](37-say-why-you-denied.md) | You are about to block an agent action |
| [Compare models in separate checkouts](38-compare-models-in-separate-checkouts.md) | More than one model might do the same task |
| [Prefer the service CLI](39-prefer-the-service-cli.md) | A service already has a command-line tool |
| [Review a plugin before you install it](40-review-a-plugin-before-you-install-it.md) | A plugin would add hooks, skills, or servers |
