# Phase 4 Coding

## Goal

Implement the approved technical plan and prove the result meets the approved
tests and Definition of Done.

## Inputs

- approved Phase 1 artifacts
- approved Phase 2 artifacts
- approved Phase 3 artifacts

## Supervisor

`phase4-coder` owns implementation coordination.

## Specialist Coders

Call only what the project needs:

- `frontend-coder`: UI, screens, components, client state, loading/error states
- `backend-coder`: API, services, persistence, auth/config, server behavior
- `ai-core-coder`: prompts, model interface, RAG, tools, AI routing, eval hooks
- `integration-coder`: joins frontend/backend/AI core, config, scripts
- `test-runner`: runs approved checks and records evidence
- `implementation-reviewer`: reviews bugs, missing tests, contract drift, DoD
  gaps, handoff quality

## Implementation Loop

```text
Pick approved task
 -> implement
 -> run relevant checks
 -> record evidence
 -> review
 -> fix or continue
```

## Must Not

- change product scope without returning to the proper phase
- change technical architecture without updating Phase 3 artifacts and asking
  for approval when the change is material
- hide failing tests or known limitations

