# Approval Gates

## Gate 1: Planning Approval

Gate 1 passes only when the user accepts:

- `PROJECT_PLAN.md`
- `REQUIREMENT_SUMMARY.md`
- project goal
- target user
- scope
- non-goals
- assumptions
- constraints

If the user changes the product idea, return to Planner intake or scope review.
If the user changes only wording, update the artifacts and ask for approval
again.

## Gate 2: Testing Approval

Gate 2 passes only when the user accepts:

- `EVALUATION_PLAN.md`
- `TEST_CASES.md`
- `DEFINITION_OF_DONE.md`
- success criteria
- acceptance criteria
- failure modes
- minimum pass threshold

If tests are too vague, return to Tester expected-output questions.
If tests are too heavy for the project maturity, simplify them.

## Coding Block

In version 1, coding is blocked even after Gate 2.

The final response should say:

```text
Planning and testing artifacts are ready. Implementation is blocked until the
user explicitly starts Phase 3.
```

