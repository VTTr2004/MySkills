---
name: vinuni-ai-project
description: Build repeatable VinUni AI-in-action projects through guided intake, flexible scope shaping, AI-agent-first architecture, lightweight backend/frontend wrappers, logging, docs, evaluation, and optional modular team/workflow discipline. Use when starting a new practical AI course project, turning a rough idea into a structured AI agent app, creating project scaffolding, or asking a coding agent to interview the user before implementation.
---

# VinUni AI Project

Use this skill to guide a new AI-in-action project from rough idea to a usable, documented prototype. Prioritize the AI workflow, evaluation, logs, and future maintainability. Treat backend and frontend as thin wrappers unless the selected level requires more.

## Core Rule

Do not start coding immediately.

First run the intake workflow, shape the project scope, draft the required artifacts, ask for user confirmation, then implement only the approved scope.

Use advisory judgment during intake. If the user's answer is vague, risky, too broad, or mismatched with the selected scope shape, explain why, offer practical options, recommend one default, and ask the user to choose. Never silently decide important product, architecture, or scope choices for the user.

## Workflow

1. Read [references/intake-questions.md](references/intake-questions.md).
2. Read [references/decision-guidance.md](references/decision-guidance.md).
3. Ask the user 1-3 intake questions at a time.
4. After each meaningful user answer, evaluate fit, risks, and missing decisions. Offer options when helpful.
5. Read [references/level-system.md](references/level-system.md) and recommend a scope shape. Treat levels as presets, not rigid categories.
6. Before writing the intake summary, ask whether the user wants to add anything not covered by the questions.
7. Incorporate the user's additions, then produce an intake summary using `assets/templates/INTAKE_SUMMARY.md`. Include assumptions, user choices, additional notes, unresolved decisions, recommended level, and what will not be built.
8. Ask the user to confirm or correct the intake summary before planning or scaffolding.
9. Draft these artifacts from [assets/templates](assets/templates):
   - `CONTEXT_SUMMARY.md` when the project may continue across sessions
   - `PROJECT_BRIEF.md`
   - `ARCHITECTURE.md`
   - `EVALUATION_PLAN.md`
   - `IMPLEMENTATION_PLAN.md`
   - `SPECS.md`, `CONTRACT.md`, or `DEFINITION_OF_DONE.md` when the scope requires them
10. Ask the user to approve or revise the plan.
11. Scaffold and implement according to [references/workflow.md](references/workflow.md) and [references/folder-structure-by-level.md](references/folder-structure-by-level.md).
12. Keep `WORKLOG.md` and `DECISION_LOG.md` updated as the project changes.

## Modular Extension

This skill can run as a lightweight standalone workflow. When this repository's modular skills are available, read [references/modular-skill-integration.md](references/modular-skill-integration.md) and load only the modules needed for the current project.

For subagent-assisted workflows, read [references/subagent-guidance.md](references/subagent-guidance.md). Use subagents for independent review, context summarization, scope shaping, evaluation design, architecture review, coding, or review only when they reduce bias or context noise.

## Default Level

If the user is doing a daily VinUni course project and does not specify a level, choose **Level 1 - Course Demo**.

If the user says the project may be reused, extended, or presented seriously, choose **Level 2 - Structured Agent**.

Treat Level 0-4 as presets, not a rigid classifier. If the project does not fit one level cleanly, describe a scope profile such as "Level 1 UI + Level 2 evaluation" or "simple implementation + work-grade handoff".

## Priorities

Use this priority order:

1. Problem clarity and success criteria
2. Agent architecture, state, tools, memory/RAG decisions
3. Evaluation plan and test cases
4. Logging, traces, worklog, decision log
5. Project structure
6. Agent implementation
7. Backend wrapper
8. Frontend/demo UI
9. Docker, CI/CD, deploy only when selected level requires them

## Output Standards

Create concise, UTF-8 Markdown artifacts. Avoid one giant plan file. Keep project knowledge in stable files so a new coding agent can continue later.

For most projects, create this minimum structure:

```text
project-root/
├── README.md
├── docs/
│   ├── PROJECT_BRIEF.md
│   ├── ARCHITECTURE.md
│   ├── DECISION_LOG.md
│   └── WORKLOG.md
├── eval/
│   └── EVALUATION_PLAN.md
├── src/
│   ├── agent/
│   ├── api/
│   ├── core/
│   └── models/
└── tests/
```

For multi-agent projects, use `src/agents/` instead of `src/agent/`.

For explicit backend/frontend separation by scope shape or preset, read [references/folder-structure-by-level.md](references/folder-structure-by-level.md) before scaffolding.

## Guardrails

- Keep backend and frontend intentionally thin unless the user asks otherwise.
- Never hardcode secrets.
- Do not create Docker, CI/CD, auth, database, or deployment files below Level 3 unless needed.
- Always define "done" with observable behavior and evaluation cases.
- Advise, critique, and recommend, but let the user make final choices.
- Prefer Streamlit for fast demo UI unless the project explicitly needs Next.js.
- Prefer FastAPI for backend only when an API wrapper is useful.
- Log agent steps, tool calls, errors, and notable decisions.

## Tool Adapters

For tool-specific installation notes, read [references/tool-adapters.md](references/tool-adapters.md). Adapter templates are in [assets/adapters](assets/adapters).
