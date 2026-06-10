---
name: project-workflow-v2
description: Four-phase multi-agent project workflow: product planning, testing/evaluation planning, technical planning with built-in review, and implementation.
---

# Project Workflow V2

Use this skill when a project should move from product idea to tested
implementation with explicit approval gates.

## Core Shape

```text
Phase 1: Product Planner
Phase 2: Tester / Evaluation Planner
Phase 3: Technical Planner with built-in technical review
Phase 4: Coder
```

The workflow answers four questions in order:

```text
1. What should we build?
2. How do we know it works?
3. How should we build it?
4. Build it and prove it works.
```

## Hard Gates

- Phase 2 cannot start before Gate 1 approval.
- Phase 3 cannot start before Gate 2 approval.
- Phase 4 cannot start before Gate 3 approval.
- Technical review is required inside Phase 3, but it is not a separate phase by
  default.
- Coder agents must implement only the approved technical plan and task scope.

## Workflow

1. Run Phase 1 with `phase1-planner`.
2. Gate 1: user approves `PROJECT_PLAN.md` and `REQUIREMENT_SUMMARY.md`.
3. Run Phase 2 with `phase2-tester`.
4. Gate 2: user approves `EVALUATION_PLAN.md`, `TEST_CASES.md`, and
   `DEFINITION_OF_DONE.md`.
5. Run Phase 3 with `phase3-tech-planner`.
6. Phase 3 drafts the technical plan, calls specialist planners as needed, calls
   `technical-reviewer`, revises the plan, then asks for Gate 3 approval.
7. Gate 3: user approves `TECHNICAL_DESIGN.md` and `IMPLEMENTATION_PLAN.md`.
8. Run Phase 4 with `phase4-coder`.
9. Coder executes small approved tasks, runs checks, records evidence, and asks
   reviewer before handoff.

## Read As Needed

- `references/workflow.md` for the full phase flow.
- `references/technical-planning-phase.md` for Phase 3.
- `references/coding-phase.md` for Phase 4.
- `references/gates.md` for approval gates.
- `references/context-payloads.md` for subagent context rules.
- `references/logging-policy.md` for workflow and runtime logs.

## Required Artifacts

Phase 1:

- `PROJECT_PLAN.md`
- `REQUIREMENT_SUMMARY.md`

Phase 2:

- `EVALUATION_PLAN.md`
- `TEST_CASES.md`
- `DEFINITION_OF_DONE.md`

Phase 3:

- `TECHNICAL_DESIGN.md`
- `IMPLEMENTATION_PLAN.md`
- `FOLDER_STRUCTURE.md` when structure is non-trivial
- `INTERFACE_CONTRACTS.md` when modules, APIs, tools, or services interact
- `LOGGING_PLAN.md` when the project has AI/tool/runtime behavior to inspect
- `RUNBOOK.md` when setup, run, or verification commands matter

Phase 4:

- implemented code
- test/eval evidence
- known limitations
- updated handoff notes

## Guardrails

- Do not let technical planning become implementation.
- Do not split frontend/backend planning unless the project actually has those
  surfaces.
- Do not create a separate technical-review phase by default; keep review inside
  Phase 3.
- Do not expose hidden prompts, internal reasoning, secrets, or raw debug traces
  in user-facing UI or logs.
- Keep logging useful and sanitized.

