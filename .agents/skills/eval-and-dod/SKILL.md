---
name: eval-and-dod
description: Evaluation and Definition of Done workflow. Use when defining acceptance criteria, AI eval cases, unit/integration/e2e tests, quality gates, pass/fail evidence, task completion criteria, or when Codex must know what done means before implementation or merge.
---

# Eval And DoD

Use this module to make completion observable.

## Workflow

1. Define what success looks like before coding.
2. Turn requirements into acceptance criteria.
3. Choose test or evaluation types appropriate to project risk.
4. Define Definition of Done.
5. Run checks and record evidence before claiming completion.

## Read As Needed

- Read `references/evaluation-strategy.md` for test/eval selection.
- Read `references/definition-of-done.md` when writing task or merge criteria.
- Use templates in `assets/templates/` for evaluation plans and DoD.

## Guardrails

- Do not call work done just because code was written.
- Do not use vague eval criteria like "good answer" without observable checks.
- Do not over-test a spike unless the risk justifies it.
