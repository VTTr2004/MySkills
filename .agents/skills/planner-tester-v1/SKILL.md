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

Do not create planning or testing artifacts from the user's first short project
idea alone. If the user gives only a high-level idea, the correct first response
is 1-3 intake questions and then stop for the user's answer.

The phrase "run Phase 1 and Phase 2" means start and follow the workflow gates;
it does not mean infer missing answers and complete every artifact in one turn.

## Workflow

1. Start Phase 1 with `phase1-planner`.
2. Ask 1-3 user questions at a time. On the first turn, ask questions only; do
   not draft `PROJECT_PLAN.md`, `REQUIREMENT_SUMMARY.md`, or any project summary.
3. Use `scope-shaper` when scope is vague, broad, risky, or timebox-mismatched.
4. Use `spec-analyst` to turn clarified answers into requirements and specs.
5. Use `requirement-summary-writer` to create a clean handoff summary for Tester.
6. Gate 1: user approves `PROJECT_PLAN.md` and `REQUIREMENT_SUMMARY.md`.
7. Start Phase 2 with `phase2-tester` only after explicit Gate 1 approval.
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
- First response for a new project must be intake questions, not artifacts.
- Do not fabricate missing requirements, expected outputs, constraints, or test
  cases just to complete the workflow.
- Do not advance from Planner to Tester in the same turn unless the user has
  explicitly approved the Phase 1 artifacts.
- Subagents receive role-specific context payloads, not full conversation by
  default.
- Subagents recommend; the supervisor aggregates and asks the user to confirm.
- Vague success criteria must be converted into observable acceptance criteria.
- Testing rigor should match project risk; do not force product-grade tests on a
  small demo.
