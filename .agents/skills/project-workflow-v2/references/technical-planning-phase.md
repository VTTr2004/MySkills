# Phase 3 Technical Planning

## Goal

Decide how to build the approved product before coding starts.

Phase 3 is not a coding phase. It converts product and testing artifacts into an
approved technical design, implementation sequence, logging plan, and runbook.

## Inputs

- `PROJECT_PLAN.md`
- `REQUIREMENT_SUMMARY.md`
- `EVALUATION_PLAN.md`
- `TEST_CASES.md`
- `DEFINITION_OF_DONE.md`

## Supervisor

`phase3-tech-planner` owns the user-facing conversation and decides which
specialist planners are needed.

## Specialist Planners

Call only the specialists that match the project:

- `architecture-planner`: architecture, module boundaries, data flow
- `frontend-planner`: screens, components, user-facing states, client state
- `backend-planner`: API, services, database, auth, config, background jobs
- `ai-core-planner`: prompts, RAG, tools, model boundary, eval hooks
- `contract-planner`: API contracts, schemas, tool/event contracts
- `logging-planner`: workflow logs, runtime logs, evidence, redaction
- `task-planner`: implementation tasks, order, dependencies
- `technical-reviewer`: risk, mismatch, overbuild, missing contracts, missing
  logs, missing run/test commands

## Required Internal Review

Technical review is required inside Phase 3. It should check:

- technical plan matches requirements
- technical plan supports test cases and DoD
- architecture is not overbuilt
- folder structure is understandable
- frontend/backend/API contracts are consistent
- logging is useful and does not expose secrets
- implementation tasks are ordered safely
- run/test commands are known
- user decisions are flagged before coding

## Gate 3

Gate 3 passes only when the user approves:

- technical design
- implementation plan
- required folder/contracts/logging/runbook artifacts
- any important tradeoffs or deferred items

