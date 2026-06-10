---
name: planner-tester-v1
description: Planner and Tester multi-agent workflow for project planning, requirements, evaluation design, test cases, and Definition of Done before coding.
---

# Planner Tester V1

Use this skill when a user wants to start, reshape, or define a software or AI
project and the workflow must create planning and testing artifacts before any
implementation.

## Core Rule

Do not code in version 1.

Implementation is blocked until all required planning and testing artifacts are
approved and the user explicitly starts a later Coder phase.

## Workflow

1. Start Phase 1 with `phase1-planner`.
2. Ask 1-3 user questions at a time.
3. Use `scope-shaper` when scope is vague, broad, risky, or timebox-mismatched.
4. Use `spec-analyst` to turn clarified answers into requirements and specs.
5. Use `requirement-summary-writer` to create a clean handoff summary for Tester.
6. Gate 1: user approves `PROJECT_PLAN.md` and `REQUIREMENT_SUMMARY.md`.
7. Start Phase 2 with `phase2-tester`.
8. Use `eval-designer` to define success criteria, metrics, and evaluation plan.
9. Use `test-case-designer` to create concrete test cases.
10. Use `dod-writer` to define completion criteria.
11. Use `test-reviewer` to check that tests are observable and proportional.
12. Gate 2: user approves `EVALUATION_PLAN.md`, `TEST_CASES.md`, and
    `DEFINITION_OF_DONE.md`.
13. Stop before code.

## Read As Needed

- `references/workflow.md` for the full phased flow.
- `references/planner-phase.md` for Phase 1 behavior.
- `references/tester-phase.md` for Phase 2 behavior.
- `references/context-payloads.md` for subagent context rules.
- `references/gates.md` for approval gates and stop conditions.

## Required Artifacts

Phase 1:

- `PROJECT_PLAN.md`
- `REQUIREMENT_SUMMARY.md`

Phase 2:

- `EVALUATION_PLAN.md`
- `TEST_CASES.md`
- `DEFINITION_OF_DONE.md`

Optional:

- `WORKFLOW_STATE.md`
- `SUBAGENT_CALL_LOG.md`

## Guardrails

- The phase supervisor owns conversation with the user.
- Subagents receive role-specific context payloads, not full conversation by
  default.
- Subagents recommend; the supervisor aggregates and asks the user to confirm.
- Vague success criteria must be converted into observable acceptance criteria.
- Testing rigor should match project risk; do not force product-grade tests on a
  small demo.

