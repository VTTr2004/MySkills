---
name: ai-project-intake
description: AI project intake and planning workflow. Use when starting or reshaping an AI agent, RAG, LLM app, chatbot, tool-using workflow, AI course project, or AI demo and Codex should ask questions before coding, define the AI job, data/tools, evaluation cases, demo behavior, and implementation plan.
---

# AI Project Intake

Use this skill when the core risk is AI behavior, not just app UI.

## Workflow

1. Ask 1-3 intake questions at a time.
2. Clarify the AI job, target user, demo behavior, data sources, tools, and constraints.
3. Evaluate vague, risky, or overbroad answers before accepting them.
4. Recommend a scope shape, not only a fixed level.
5. Define evaluation cases before implementation.
6. Draft the project brief, architecture, evaluation plan, and implementation plan.
7. Ask for confirmation before scaffolding or coding.

## Read As Needed

- Read `references/intake-flow.md` for question groups.
- Read `references/ai-scope.md` when choosing the AI core and wrapper size.
- Read `references/eval-first.md` when designing AI evaluation.

## Defaults

- Prefer the AI workflow, logs, evaluation, and handoff over UI polish.
- Prefer thin backend/frontend wrappers unless the project goal requires more.
- Prefer Streamlit for quick demos unless another UI is explicitly useful.
- Never hardcode secrets or private credentials.
