# Upgrade Protocol

Use this protocol whenever the user adds workshop notes or asks to evolve the skill pack.

## Intake

1. Read this folder first.
2. Read only the relevant new files from `knowledge-from-workshop/`.
3. Classify each new lesson as one of:
   - `principle`: stable belief that should guide many projects.
   - `heuristic`: useful default, but context-dependent.
   - `template`: reusable output format.
   - `agent-role`: a new or changed subagent behavior.
   - `skill-module`: a workflow that deserves its own skill.
   - `example`: useful illustration, not a rule.
4. Ask the user before turning ambiguous lessons into hard rules.

## Update

Prefer small, targeted changes:
- Update a reference file before expanding a `SKILL.md`.
- Add a new skill module only when the trigger is distinct.
- Add a new subagent only when a separate role reduces context, bias, or conflict.
- Keep enterprise and team-process details optional.

## Validation

After editing:
- Run skill validation for changed skills.
- Check that descriptions trigger only when useful.
- Check that diagrams and indexes link to new modules.
- Summarize what changed and what remains intentionally unchanged.

## Guardrails

- Do not make every project enterprise-grade.
- Do not force all projects into fixed levels.
- Do not treat subagents as strict data-isolation boundaries.
- Do not let a summary hide user-confirmed changes or open questions.
- Do not let coder agents make product decisions.
