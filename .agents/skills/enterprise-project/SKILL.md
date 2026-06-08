---
name: enterprise-project
description: Work-grade and enterprise project governance. Use only when a project needs production intent, security, compliance, traceability, ownership, risk management, release discipline, auditability, long-term maintainability, or workplace-ready software process.
---

# Enterprise Project

Use this module only when lightweight project discipline is not enough.

## Workflow

1. Confirm why enterprise/work-grade process is needed.
2. Identify stakeholders, owners, risk areas, and release expectations.
3. Require traceable decisions, contracts, tests, and handoff.
4. Add security, privacy, cost, data, and operational concerns when relevant.
5. Keep the process proportional to actual risk.

## Read As Needed

- Read `references/governance.md` for governance and traceability.
- Read `references/risk-checklist.md` for security, data, cost, and operational risk.
- Read `references/release-handoff.md` for release and handoff expectations.

## Guardrails

- Do not apply enterprise process to quick spikes unless the user asks.
- Do not add auth, database, monitoring, CI/CD, or deployment without a reason.
- Do not let governance language hide unresolved product decisions.
