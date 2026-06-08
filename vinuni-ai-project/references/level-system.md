# Level System

Use levels to prevent overbuilding. A higher level includes the expectations of lower levels unless explicitly scoped out.

## Level 0 - Spike

Use for a 1-3 hour idea test.

Must have:
- One working AI script, notebook, or minimal app
- Short README
- 3-5 sample inputs and outputs

Do not add:
- Full backend
- Full frontend
- Docker
- CI/CD
- Complex project structure

## Level 1 - Course Demo

Use for daily VinUni practical projects.

Must have:
- One AI agent or agent workflow
- Thin backend if useful, usually FastAPI
- Thin frontend if useful, usually Streamlit
- Basic logs
- README
- `PROJECT_BRIEF.md`
- `EVALUATION_PLAN.md` with at least 5 test cases

Do not add by default:
- Docker
- CI/CD
- Auth
- Production database
- Full deploy pipeline

## Level 2 - Structured Agent

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

## Level 3 - Demo Day

Use for serious presentation or grading deliverables.

Must have:
- Everything from Level 2
- Dockerfile
- CI/CD
- Deployable live URL
- Architecture diagram
- Evaluation evidence report
- Video/demo notes
- Robust README

Optional:
- Docker Compose
- Monitoring dashboard
- LangSmith traces

## Level 4 - Product Ready

Use only when the project is intended to become a real product.

Must have:
- Auth if user-specific data exists
- Persistent database
- Environment-specific config
- Cost monitoring
- Observability
- Rate limiting
- Security review
- Production deployment checklist

Avoid Level 4 during daily course work unless explicitly requested.
