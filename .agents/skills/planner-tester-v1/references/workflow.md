# Planner Tester V1 Workflow

## Overview

```text
Start
 -> Phase 0: intent check
 -> Phase 1: Planner Agent
 -> Gate 1: planning approval
 -> Phase 2: Tester Agent
 -> Gate 2: testing approval
 -> Stop before code
```

## Phase 0: Intent Check

Classify the request:

- new project
- existing project improvement
- brainstorm only
- continue previous workflow

If the user asks to code immediately, explain that version 1 requires planning
and testing artifacts first.

## Phase 1: Planner Agent

Planner creates:

- `PROJECT_PLAN.md`
- `REQUIREMENT_SUMMARY.md`

Planner may call:

- `scope-shaper`
- `spec-analyst`
- `requirement-summary-writer`

## Gate 1

Gate 1 passes only when the user accepts:

- project goal
- target users
- scope and non-goals
- assumptions and constraints
- `PROJECT_PLAN.md`
- `REQUIREMENT_SUMMARY.md`

## Phase 2: Tester Agent

Tester creates:

- `EVALUATION_PLAN.md`
- `TEST_CASES.md`
- `DEFINITION_OF_DONE.md`

Tester may call:

- `eval-designer`
- `test-case-designer`
- `dod-writer`
- `test-reviewer`

## Gate 2

Gate 2 passes only when the user accepts:

- success criteria
- acceptance criteria
- test cases
- failure modes
- Definition of Done

## Stop Condition

After Gate 2, report that the project is ready for a future Coder phase.
Do not implement code in version 1.

