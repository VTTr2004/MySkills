# Implementation Workflow

## Step 1 - Draft Stable Artifacts

Before coding, create or draft:

- `INTAKE_SUMMARY.md` or an equivalent in-chat intake summary
- `docs/PROJECT_BRIEF.md`
- `docs/ARCHITECTURE.md`
- `eval/EVALUATION_PLAN.md`
- `docs/DECISION_LOG.md`
- `docs/WORKLOG.md`
- `IMPLEMENTATION_PLAN.md` or a concise task list

Use templates from `assets/templates`.

Do not scaffold until the user confirms the intake summary.

## Step 2 - Scaffold By Level

Read `folder-structure-by-level.md` before scaffolding. It defines when to keep everything in one simple app and when to split `backend/` and `frontend/`.

## Step 3 - Implement AI Core First

Build the smallest working AI workflow before polishing API/UI.

For single-agent:
- Define state
- Define nodes
- Define tools
- Define routing
- Add logging
- Run 3-5 sample inputs

For multi-agent:
- Define supervisor/router
- Define each agent role
- Define shared state
- Define handoff rules
- Add logs for each handoff

## Step 4 - Wrap With Backend And Frontend

Add FastAPI only when external interaction is useful.

Add frontend only when demo experience matters.

Default demo UI:
- Streamlit for Level 1
- Streamlit or Next.js for Level 2
- Next.js only when UI/UX is a grading factor

## Step 5 - Evaluate

Run the eval cases from `EVALUATION_PLAN.md`.

Update:
- pass/fail notes
- failure examples
- next fixes

Do not claim the project is complete until at least the minimum eval cases are run.

## Step 6 - Handoff

Before stopping, update:

- `README.md`
- `docs/WORKLOG.md`
- `docs/DECISION_LOG.md`
- any known TODOs or limitations
