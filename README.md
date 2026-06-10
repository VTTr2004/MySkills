# VinUni Planner Tester Skill Pack

This repository contains a version 1 workflow for building projects with a
planning phase and a testing/evaluation phase before implementation.

The core rule is simple:

```text
Do not code before planning artifacts and testing artifacts are approved.
```

## Version 1 Scope

Version 1 includes:

- Phase 1 Planner Agent
- Phase 2 Tester Agent
- Specialist subagents for scope, specs, summary, evaluation, test cases, DoD,
  and test review
- Role-specific context payload rules
- Artifact approval gates
- Templates for planning and testing artifacts

Version 1 does not include:

- Coder Agent implementation workflow
- Production deployment workflow
- Team sprint or merge workflow

## Main Workflow

```text
User
 -> Phase 1: Planner Agent
    -> Scope Shaper
    -> Spec Analyst
    -> Requirement Summary Writer
 -> Gate 1: user approves PROJECT_PLAN.md and REQUIREMENT_SUMMARY.md
 -> Phase 2: Tester Agent
    -> Eval Designer
    -> Test Case Designer
    -> DoD Writer
    -> Test Reviewer
 -> Gate 2: user approves EVALUATION_PLAN.md, TEST_CASES.md, and DEFINITION_OF_DONE.md
 -> Stop before code
```

## Skill Entry Point

Use:

```text
K:\AI_IN_ACTION\vinuni-ai-project-skill\.agents\skills\planner-tester-v1\SKILL.md
```

Start a new project with:

```text
Use planner-tester-v1. Run Phase 1 and Phase 2 only. Do not code.
```

## Artifacts

Phase 1 creates:

- `PROJECT_PLAN.md`
- `REQUIREMENT_SUMMARY.md`

Phase 2 creates:

- `EVALUATION_PLAN.md`
- `TEST_CASES.md`
- `DEFINITION_OF_DONE.md`

Optional workflow state:

- `WORKFLOW_STATE.md`
- `SUBAGENT_CALL_LOG.md`

## Subagent Principle

Subagents should not receive the full conversation by default. The phase
supervisor sends each subagent a role-specific context payload with:

- confirmed decisions
- relevant constraints
- a narrow task
- expected output format
- forbidden decisions

The supervisor owns final user-facing decisions.

