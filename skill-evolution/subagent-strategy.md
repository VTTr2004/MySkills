# Subagent Strategy

Subagents are optional specialist reviewers or workers.
Use them to reduce bias, context pollution, and role confusion.

## Input Pattern

Send each subagent:
1. role-specific instructions from its custom agent file;
2. a clean context summary;
3. a narrow task payload;
4. the expected output format.

Do not send the whole conversation when a concise payload is enough.

## Recommended Roles

`planning-advisor`
: User-facing planner. Clarify goals, propose workflow, and coordinate other agents.

`context-summarizer`
: Maintain concise rolling context summary with confirmed decisions, assumptions, open questions, and superseded ideas.

`scope-shaper`
: Evaluate scope flexibly across AI, data, UI, backend, evaluation, maturity, and timebox. Use Level 0-4 only as presets.

`spec-analyst`
: Turn ideas into specs, user stories, domain requirements, and contract needs.

`architecture-advisor`
: Review architecture, ADRs, folder structure, boundaries, and technical risks.

`eval-designer`
: Define evaluation cases, acceptance criteria, failure modes, and evidence.

`coder`
: Implement approved tasks only. Do not make product decisions.

`reviewer`
: Review correctness, regressions, missing tests, contract drift, and handoff quality.

## Model Policy

Model choice is configurable per subagent.
Default tradeoff:
- use a fast mini model for summarization and narrow coding tasks;
- use a stronger reasoning model for scope, architecture, evaluation, and review;
- adjust based on budget, latency, and observed quality.

## Limitation

Codex subagents reduce context pollution but are not a strict security or context-isolation boundary.
