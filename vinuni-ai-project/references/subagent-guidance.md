# Subagent Guidance

Use subagents only when they reduce bias, context pollution, role confusion, or parallel exploration time.

## Input Pattern

Send a subagent:
1. clean context summary;
2. narrow task payload;
3. expected output format.

Do not send the whole conversation when a concise payload is enough.

## Available Roles

- `planning-advisor`: coordinate planning and user-facing decisions.
- `context-summarizer`: maintain concise context summary.
- `scope-shaper`: review scope flexibly, not as a fixed Level 0-4 classifier.
- `spec-analyst`: turn ideas into specs and contract needs.
- `architecture-advisor`: review architecture, ADRs, boundaries, and risks.
- `eval-designer`: design eval cases, acceptance criteria, and DoD.
- `coder`: implement approved tasks only.
- `reviewer`: review correctness, regressions, missing tests, and contract drift.

## Model Policy

Model choice is configurable per subagent.
Use a faster mini model for summarization and narrow implementation.
Use a stronger reasoning model for scope, architecture, evaluation, and review.

## Limitation

Codex subagents are useful for context management, but they are not a strict data-isolation boundary.
