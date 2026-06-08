# Folder Structure By Level

Use this file before scaffolding. The main decision is whether backend/frontend should be wrappers inside one simple project or separated into a monorepo.

## Rule Of Thumb

- Level 0-1: do not split `backend/` and `frontend/` unless the user explicitly asks.
- Level 2: split only if frontend is meaningful or the project may continue.
- Level 3-4: split `backend/` and `frontend/` by default.

## Level 0 - Spike

No backend/frontend separation.

```text
project-root/
├── README.md
├── src/
│   └── main.py
└── samples/
```

Use when the goal is to prove an AI idea quickly.

## Level 1 - Course Demo

Backend is a thin API inside `src/api`. Frontend is optional and usually `app.py` for Streamlit.

```text
project-root/
├── README.md
├── app.py                  # optional Streamlit demo UI
├── docs/
│   ├── PROJECT_BRIEF.md
│   ├── WORKLOG.md
│   └── DECISION_LOG.md
├── eval/
│   └── EVALUATION_PLAN.md
├── src/
│   ├── agent/
│   │   ├── graph.py
│   │   ├── state.py
│   │   ├── nodes.py
│   │   └── tools.py
│   ├── api/
│   │   └── main.py         # optional FastAPI wrapper
│   └── core/
│       └── config.py
└── tests/
```

Use this for daily VinUni projects. Keep it fast.

## Level 2 - Structured Agent

Default: keep one repo, but make modules cleaner. Use `frontend/` only if UI matters.

```text
project-root/
├── README.md
├── docs/
├── eval/
├── src/
│   ├── agent/              # or agents/ for multi-agent
│   ├── api/
│   ├── core/
│   ├── models/
│   └── services/
├── tests/
└── frontend/               # optional, only if UI is not just Streamlit
```

If the user says the project will continue or the frontend is substantial, use a monorepo split:

```text
project-root/
├── README.md
├── backend/
│   ├── src/
│   │   ├── agent/          # or agents/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   └── services/
│   └── tests/
├── frontend/
│   └── README.md
├── docs/
└── eval/
```

Ask the user before choosing the monorepo split.

## Level 3 - Demo Day

Use backend/frontend split by default.

```text
project-root/
├── README.md
├── backend/
│   ├── src/
│   │   ├── agent/          # or agents/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   └── services/
│   ├── tests/
│   └── Dockerfile
├── frontend/
│   ├── src/
│   └── package.json
├── docs/
│   ├── PROJECT_BRIEF.md
│   ├── ARCHITECTURE.md
│   ├── DECISION_LOG.md
│   └── WORKLOG.md
├── eval/
│   ├── EVALUATION_PLAN.md
│   └── EVALUATION_REPORT.md
├── infra/
│   └── docker-compose.yml
└── .github/
    └── workflows/
```

Use this for grading, presentation, or a project that needs deploy evidence.

## Level 4 - Product Ready

Use backend/frontend split plus infra and operations.

```text
project-root/
├── backend/
├── frontend/
├── infra/
├── docs/
│   ├── adr/
│   └── runbooks/
├── eval/
├── monitoring/
└── .github/
```

Only use Level 4 when the user explicitly wants a product-grade system.
