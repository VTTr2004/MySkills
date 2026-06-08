# Scope Presets

Use these presets to prevent overbuilding, but do not force every project into a rigid level.
A project may combine dimensions, such as "Level 1 UI + Level 2 evaluation".

## Preset 0 - Spike

Use for a 1-3 hour idea test.

Must have:
- One working AI script, notebook, or minimal app
- Short README
- 3-5 sample inputs and outputs

Avoid by default:
- Full backend
- Full frontend
- Docker
- CI/CD
- Complex project structure

## Preset 1 - Course Demo

Use for daily VinUni practical projects.

Must have:
- One AI agent or agent workflow
- Thin backend if useful, usually FastAPI
- Thin frontend if useful, usually Streamlit
- Basic logs
- README
- `PROJECT_BRIEF.md`
- `EVALUATION_PLAN.md` with at least 5 test cases

Avoid by default:
- Docker
- CI/CD
- Auth
- Production database
- Full deploy pipeline

## Preset 2 - Structured Prototype

Use for projects worth continuing after the class day.

Must have:
- Clean `src/agent` or `src/agents` structure
- State, nodes, tools, prompts separated
- `ARCHITECTURE.md`
- `DECISION_LOG.md`
- `WORKLOG.md`
- Basic tests for agent logic or API
- Evaluation plan with 10-20 cases
- Logging for requests, tool calls, and errors

Optional:
- FastAPI backend
- Streamlit or Next.js frontend
- Local vector store for RAG
- Context summary
- ADRs or contracts if multiple agents/people are involved

## Preset 3 - Demo Day / Serious Presentation

Use for serious presentation or grading deliverables.

Often includes:
- Everything from Preset 2
- Architecture diagram
- Evaluation evidence report
- Demo script or video notes
- Robust README
- Deployable live URL, Docker, or CI/CD only if required

## Preset 4 - Product / Work-Grade

Use only when the project is intended to become a real product or workplace deliverable.

May require:
- Auth if user-specific data exists
- Persistent database
- Environment-specific config
- Cost monitoring
- Observability
- Rate limiting
- Security review
- Production deployment checklist
- Specs, ADRs, contracts, DoD, review, and handoff

## Scope Profile Dimensions

When no preset fits cleanly, describe:
- Delivery mode
- AI complexity
- Data/tool complexity
- UI/backend complexity
- Evaluation rigor
- Engineering maturity
- Timebox fit
- Must include / should include / defer / non-goals