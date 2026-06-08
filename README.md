# VinUni AI Project Skill Pack

This repository is evolving from a lightweight VinUni AI demo helper into a personal AI project operating system.

It supports two modes:

1. Lightweight AI course/demo projects.
2. Larger work-style projects that need specs, ADRs, contracts, evaluation, Definition of Done, subagents, and continuous improvement.

The core philosophy is:

- context first
- plan before code
- AI/eval/logs first
- backend/frontend as thin wrappers unless needed
- scope shaped by project reality, not a rigid level label
- reusable knowledge kept in small modules, not one huge file

## Quick Start

For a lightweight AI project, ask an agent:

```text
Read K:\AI_IN_ACTION\vinuni-ai-project-skill\vinuni-ai-project\SKILL.md
and start intake for my new AI project. Ask questions in small batches before coding.
```

For the newer modular workflow, ask Codex:

```text
Use the skills under K:\AI_IN_ACTION\vinuni-ai-project-skill\.agents\skills.
Start with project-core. Load only the extra modules needed for this project.
Do not code until scope, evaluation, architecture, and implementation plan are confirmed.
```

For future upgrades to this skill pack, ask:

```text
Read K:\AI_IN_ACTION\vinuni-ai-project-skill\skill-evolution first,
then read the relevant files in knowledge-from-workshop,
and update the skill pack modularly.
```

## Main Folders

```text
vinuni-ai-project-skill/
|-- README.md
|-- WORKFLOW_DIAGRAM.md
|-- workflow/                  # Mermaid diagrams for VS Code preview
|-- skill-evolution/           # Read first when upgrading the skill pack
|-- knowledge-from-workshop/   # Raw workshop notes and personal lessons
|-- .agents/skills/            # Modular Codex skills
|-- .codex/agents/             # Custom subagent definitions
|-- vinuni-ai-project/         # Portable legacy/lightweight skill pack
|-- template-manage-project/   # External project management templates
```

## Modular Skills

The modular skills live in `.agents/skills/`:

| Skill | Use when |
|-------|----------|
| `project-core` | Any project needs goal clarity, scope shaping, context summary, plan, or handoff. |
| `ai-project-intake` | The project includes an AI agent, RAG, LLM app, chatbot, tools, prompts, or AI evaluation. |
| `team-workflow` | Multiple people/agents, tasks, sprint planning, review, merge, or shared context are needed. |
| `enterprise-project` | The project needs work-grade governance, traceability, risk, security, or release discipline. |
| `adr-contracts` | Architecture decisions, contracts, domain boundaries, or conventions matter. |
| `eval-and-dod` | You need acceptance criteria, tests, evaluation evidence, or Definition of Done. |
| `continuous-learning` | You are updating this skill pack from workshop notes or project retrospectives. |

Codex should load only the modules that match the current task.

## Custom Subagents

Custom subagents live in `.codex/agents/`:

| Agent | Role |
|-------|------|
| `planning-advisor` | User-facing planning coordinator. |
| `context-summarizer` | Maintains a clean rolling context summary. |
| `scope-shaper` | Reviews scope flexibly across timebox, AI/data/UI/backend/eval/maturity. |
| `spec-analyst` | Turns ideas into specs, user stories, and contract needs. |
| `architecture-advisor` | Reviews ADRs, boundaries, architecture, and risks. |
| `eval-designer` | Designs eval cases, acceptance criteria, and DoD. |
| `coder` | Implements approved, well-scoped tasks. |
| `reviewer` | Reviews correctness, missing tests, contract drift, and handoff quality. |

Subagents should receive a minimal task payload plus a clean context summary, not the whole conversation when avoidable.

## Scope Shaping

The old Level 0-4 system still exists as a useful preset rubric:

- Spike
- Course demo
- Structured prototype
- Demo day
- Product-ready

But it is not a rigid classifier. A project can use a custom scope profile such as:

- Level 1 UI + Level 2 evaluation
- Simple implementation + work-grade handoff
- Course demo engineering + strong RAG evaluation

## Visual Workflow

Open this in VS Code Markdown Preview:

```text
K:\AI_IN_ACTION\vinuni-ai-project-skill\WORKFLOW_DIAGRAM.md
```

Diagrams are split into small files in `workflow/`.

## Portable Skill

`vinuni-ai-project/` remains a portable skill pack for agents that cannot load `.agents/skills` directly.
It now includes references to the modular extension and subagent workflow.

## Update Policy

Raw notes go into `knowledge-from-workshop/`.
Before turning them into rules, read `skill-evolution/` and classify each lesson as:

- principle
- heuristic
- template
- agent role
- skill module
- example

Do not grow one giant skill file. Prefer small references, templates, or module-specific updates.