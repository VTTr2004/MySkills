# Tool Adapters

The core skill is tool-agnostic. Use these adapters when you want a specific coding tool to auto-load the workflow.

## Codex

Use `AGENTS.md`.

Options:

1. Copy `assets/adapters/codex/AGENTS.md` into a project root.
2. Or tell Codex: "Read `K:\\AI_IN_ACTION\\vinuni-ai-project-skill\\vinuni-ai-project` and start intake."

## Claude Code

Use a skill folder.

Options:

1. Copy the `vinuni-ai-project` skill folder into `.claude/skills/vinuni-ai-project`.
2. Or copy it into the personal skills folder so it is available across projects.
3. Then ask: `/vinuni-ai-project Start a new VinUni AI project`.

## Cursor

Use Project Rules.

Options:

1. Copy `assets/adapters/cursor/vinuni-ai-project.mdc` into `.cursor/rules/`.
2. Mention the rule in chat, or let Cursor attach it when relevant.

## Generic Coding Agent

Tell the agent:

```text
Read K:\AI_IN_ACTION\vinuni-ai-project-skill\vinuni-ai-project\SKILL.md.
Then follow the workflow and ask me intake questions before coding.
```
