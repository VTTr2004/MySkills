# Context Summary

Create `docs/CONTEXT_SUMMARY.md` for any project that may continue across sessions.

Required sections:
- Confirmed decisions
- Project goal
- Target user
- Scope
- Non-goals
- Current plan
- Assumptions
- Open questions
- Superseded or rejected ideas
- Next checkpoint

Rules:
- Keep confirmed facts separate from assumptions.
- Remove or mark stale decisions when the user changes direction.
- Keep the summary concise enough to pass to subagents.
- If the task payload conflicts with the summary, stop and ask for clarification.
