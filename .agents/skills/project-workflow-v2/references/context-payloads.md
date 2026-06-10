# Context Payloads

Subagents receive role-specific payloads, not the full conversation by default.

Every payload should include:

- confirmed decisions
- relevant artifacts
- narrow task
- expected output format
- forbidden decisions

## Phase 3 Payload Examples

### Frontend Planner

```text
Requirement summary:
Approved test cases:
Target user:
Expected user-facing states:

Task:
Plan screens/components/state/loading/error/result display.

Forbidden:
Do not choose backend architecture or implement code.
```

### Backend Planner

```text
Requirement summary:
Data needs:
Integration needs:
Approved test cases:

Task:
Plan API/service/storage/config boundaries.

Forbidden:
Do not implement code or change product scope.
```

### Logging Planner

```text
AI/tool/runtime behaviors:
Evaluation evidence needs:
Privacy/secrets constraints:

Task:
Define workflow logs, runtime logs, redaction, and evidence fields.
```

### Technical Reviewer

```text
Technical design:
Implementation plan:
Testing artifacts:
Definition of Done:

Task:
Find mismatches, missing contracts, overbuild, underbuild, missing logs, missing
commands, and risks before Gate 3.
```

## Phase 4 Payload Examples

### Specialist Coder

```text
Approved task:
Relevant technical design section:
Relevant contracts:
Relevant test cases:

Task:
Implement only this task and report files changed plus checks to run.
```

### Test Runner

```text
Approved test cases:
Changed files summary:
Run commands:

Task:
Run checks, record results, and identify failures or missing evidence.
```

