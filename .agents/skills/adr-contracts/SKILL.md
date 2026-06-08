---
name: adr-contracts
description: Architecture decision and contract-first workflow. Use when defining ADRs, architecture, tech stack, module boundaries, domain split, API contracts, event contracts, folder structure, coding conventions, or when multiple agents/teams must work without implicit dependencies.
---

# ADR Contracts

Use this module when architecture or boundaries matter.

## Workflow

1. Identify decisions that need to be recorded.
2. Draft ADRs for architecture, tech stack, conventions, test strategy, and domain split.
3. Define contracts before parallel implementation.
4. Keep contracts small, explicit, and testable.
5. Update ADRs or contracts when decisions change.

## Read As Needed

- Read `references/adr-guidance.md` when drafting decisions.
- Read `references/contract-first.md` when defining APIs, events, schemas, or module boundaries.
- Use templates in `assets/templates/` when creating ADR or contract files.

## Guardrails

- Do not create ADRs for trivial choices.
- Do not let agents rely on implicit assumptions between domains.
- Do not change contracts without noting the consequence.
