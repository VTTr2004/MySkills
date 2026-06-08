# Implementation Workflow

## Step 1 - Draft Stable Artifacts

Before coding, create or draft the smallest useful artifact set.

Minimum for lightweight AI projects:
- `INTAKE_SUMMARY.md` or an equivalent in-chat intake summary
- `docs/CONTEXT_SUMMARY.md` when the project may continue across sessions
- `docs/PROJECT_BRIEF.md`
- `docs/ARCHITECTURE.md`
- `eval/EVALUATION_PLAN.md`
- `docs/DECISION_LOG.md`
- `docs/WORKLOG.md`
- `IMPLEMENTATION_PLAN.md` or a concise task list

For team/work projects, add only when useful:
- `specs/` or `SPECS.md`
- `docs/adr/`
- `contracts/`
- `DEFINITION_OF_DONE.md`
- task/backlog files

Use templates from `assets/templates` and optional modular skills.
Do not scaffold until the user confirms the intake summary and plan.

## Step 2 - Scaffold By Scope Shape

Read `folder-structure-by-level.md` for preset structures, but treat them as starting points.
Choose the lightest structure that fits the confirmed scope profile.

## Step 3 - Implement AI Core First

Build the smallest working AI workflow before polishing API/UI.

For single-agent:
- Define state
- Define nodes or steps
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
Add frontend only when demo or user workflow requires it.

Default demo UI:
- Streamlit for quick demos
- Streamlit or Next.js for reusable prototypes
- Next.js only when UI/UX is a grading or product factor

## Step 5 - Evaluate

Run the eval cases from `EVALUATION_PLAN.md`.
Update:
- pass/fail notes
- failure examples
- next fixes
- evaluation evidence

Do not claim the project is complete until the minimum eval or test cases are run, or until the limitation is clearly documented.

## Step 6 - Review And Handoff

Before stopping, update:

- `README.md`
- `docs/CONTEXT_SUMMARY.md` if present
- `docs/WORKLOG.md`
- `docs/DECISION_LOG.md`
- relevant specs, ADRs, contracts, or DoD
- known TODOs or limitations