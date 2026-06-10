# Project Workflow V2

## Flow

```text
Start
 -> Phase 1: Product Planner
 -> Gate 1: planning approval
 -> Phase 2: Tester / Evaluation Planner
 -> Gate 2: testing approval
 -> Phase 3: Technical Planner + built-in technical review
 -> Gate 3: technical approval
 -> Phase 4: Coder
 -> Final verification and handoff
```

## Phase 1

Define what should be built.

Outputs:

- `PROJECT_PLAN.md`
- `REQUIREMENT_SUMMARY.md`

## Phase 2

Define how to know the project works.

Outputs:

- `EVALUATION_PLAN.md`
- `TEST_CASES.md`
- `DEFINITION_OF_DONE.md`

## Phase 3

Define how to build it.

Outputs:

- `TECHNICAL_DESIGN.md`
- `IMPLEMENTATION_PLAN.md`
- optional `FOLDER_STRUCTURE.md`
- optional `INTERFACE_CONTRACTS.md`
- optional `LOGGING_PLAN.md`
- optional `RUNBOOK.md`

Technical review happens inside this phase before Gate 3.

## Phase 4

Implement only the approved technical plan. Work in small tasks, run checks,
record evidence, and review before handoff.

