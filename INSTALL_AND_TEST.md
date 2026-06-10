# Install And Test

This repository is designed to be used as local Codex skills and subagents.

## Smoke Test Prompt

Use this prompt in a fresh Codex session:

```text
Use the planner-tester-v1 workflow from K:\AI_IN_ACTION\vinuni-ai-project-skill.
I want to build a small AI assistant for student course advising.
Run Phase 1 and Phase 2 only. Do not code.
```

## Pass Criteria

The assistant should:

- activate Planner Agent first
- on the first response, ask 1-3 intake questions and stop
- not create `PROJECT_PLAN.md`, `REQUIREMENT_SUMMARY.md`, `project_summary`, or
  testing artifacts from the first short idea alone
- review scope before accepting the plan
- produce or propose `PROJECT_PLAN.md`
- produce or propose `REQUIREMENT_SUMMARY.md`
- wait for user approval before Tester Agent
- activate Tester Agent after Gate 1
- ask about expected outputs and important failures
- produce or propose `EVALUATION_PLAN.md`
- produce or propose `TEST_CASES.md`
- produce or propose `DEFINITION_OF_DONE.md`
- stop before implementation

## Fail Criteria

The workflow fails if the assistant:

- creates any project summary or artifact in the first response to the smoke test
- starts coding in version 1
- sends the full conversation to every subagent by default
- treats vague success criteria like "good answer" as testable
- skips user approval between Planner and Tester
- lets a subagent make final product decisions without supervisor approval
