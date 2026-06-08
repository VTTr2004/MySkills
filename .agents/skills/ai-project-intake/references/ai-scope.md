# AI Scope

Treat the AI workflow as the core. UI and backend are wrappers unless the project goal says otherwise.

Clarify:
- Single-step LLM call, multi-step agent, or multi-agent workflow
- Prompt-only, tool-using, RAG, API-backed, or database-backed
- Required logging: prompt, tool call, retrieved context, errors, final answer
- Output contract: what shape the answer must have
- Safety and privacy constraints

Defaults:
- Course demo: thin Streamlit or CLI, simple logs, 5+ eval cases
- Reusable prototype: separated agent modules, tests, context summary, 10+ eval cases
- Demo/work project: contracts, ADRs, stronger eval evidence, review checklist
