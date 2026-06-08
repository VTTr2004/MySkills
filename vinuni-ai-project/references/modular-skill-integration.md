# Modular Skill Integration

This portable skill remains usable on its own, but the repository now has modular skills for larger workflows.

Use the modular skills when available:

- `project-core`: base planning, context summary, scope shaping, handoff.
- `ai-project-intake`: AI-specific intake, agent job, data/tools/RAG, eval-first planning.
- `team-workflow`: specs, team planning, tasks, review/merge, parallel AI execution.
- `enterprise-project`: work-grade governance, traceability, risk, release discipline.
- `adr-contracts`: ADRs, domain split, API/event/module contracts.
- `eval-and-dod`: evaluation strategy, acceptance criteria, Definition of Done.
- `continuous-learning`: evolve the skill pack from workshop notes and retrospectives.

## Rule

Do not load every module by default.
Load the smallest module set that matches the project risk and user request.

## Suggested Mapping

Daily AI demo:
- `project-core`
- `ai-project-intake`
- optionally `eval-and-dod`

Reusable AI prototype:
- `project-core`
- `ai-project-intake`
- `adr-contracts`
- `eval-and-dod`

Team or work project:
- `project-core`
- `team-workflow`
- `adr-contracts`
- `eval-and-dod`
- optionally `enterprise-project`

Skill upgrade:
- `continuous-learning`
- read `skill-evolution/README.md` first
