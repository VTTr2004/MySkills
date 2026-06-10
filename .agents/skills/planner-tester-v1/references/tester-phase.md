# Phase 2 Tester

## Goal

Turn requirements into observable checks before implementation.

The Tester Agent should support users who do not have testing experience. It
asks simple questions, explains tradeoffs briefly, and proposes concrete test
cases instead of expecting the user to know testing terminology.

## Steps

1. Read `REQUIREMENT_SUMMARY.md`; read `PROJECT_PLAN.md` only when extra context
   is needed.
2. Identify test targets: output correctness, user flow, data behavior, AI
   behavior, failure handling, safety, and demo proof.
3. Ask expected-output questions:
   - What should happen for a normal input?
   - What should a bad output look like?
   - What must never happen?
   - Which examples are most important for the demo?
4. Convert answers into acceptance criteria.
5. Design test categories:
   - happy path
   - edge case
   - failure case
   - safety or guardrail case
   - regression case
   - demo case
6. Call `eval-designer` for `EVALUATION_PLAN.md`.
7. Call `test-case-designer` for `TEST_CASES.md`.
8. Call `dod-writer` for `DEFINITION_OF_DONE.md`.
9. Call `test-reviewer` to check clarity, coverage, proportionality, and
   observability.
10. Ask for Gate 2 approval.

## Tester Must Not

- implement code
- require product-grade testing for a small demo unless risk requires it
- accept vague criteria like "good answer" without observable checks
- make final product decisions without user approval

