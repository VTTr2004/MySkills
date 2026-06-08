---
name: project-core
description: Core project planning workflow for any software or AI project. Use when starting, restructuring, resuming, or handing off a project and Codex should clarify goals, shape scope, maintain clean context, plan before code, avoid overbuilding, and keep decisions traceable.
---

# Project Core

Use this as the base workflow for all project work. Keep it lightweight unless the project risk demands more process.

## Workflow

1. Clarify the user's goal, target user, success criteria, timebox, and constraints.
2. Create or update a clean context summary before deep work.
3. Shape scope with the lightest process that protects quality.
4. Separate confirmed decisions, assumptions, open questions, and non-goals.
5. Draft a plan before implementation.
6. Ask for confirmation before major product, architecture, or scope decisions.
7. Implement only approved scope.
8. End with handoff notes: what changed, how to verify, limitations, and next steps.

## Context Summary

For projects that may continue across sessions, create or update `docs/CONTEXT_SUMMARY.md`.
Read `references/context-summary.md` when writing or refreshing it.

## Scope

Do not force fixed maturity levels. Use presets only as shortcuts.
Read `references/scope-shaping.md` when the project is ambiguous, too large, too weak, or mismatched with its timebox.

## Optional Modules

Load only when needed:
- Use `ai-project-intake` for AI agent, RAG, tools, prompts, or AI evaluation.
- Use `team-workflow` for team execution, sprint planning, owners, PR/review, or parallel AI work.
- Use `enterprise-project` for work-grade governance, security, auditability, or release discipline.
- Use `adr-contracts` for architecture decisions, contracts, boundaries, or conventions.
- Use `eval-and-dod` for acceptance criteria, tests, eval evidence, or Definition of Done.
- Use `continuous-learning` when updating this skill pack from workshop notes or retrospectives.
