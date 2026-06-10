# VinUni AI Project Workflow Skill Pack

This repository contains phased multi-agent workflows for building AI and
software projects with explicit gates before implementation.

The core rule is:

```text
Do not code before planning, testing, and technical planning artifacts are approved.
```

## Available Workflows

### `planner-tester-v1`

Use when you want to stop before coding.

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

### `project-workflow-v2`

Use when you want the full gated path:

```text
Phase 1: Product Planner
Phase 2: Tester / Evaluation Planner
Phase 3: Technical Planner with built-in technical review
Phase 4: Coder
```

Version 2 includes:

- Phase 3 technical planning
- built-in technical review inside Phase 3
- frontend/backend/AI/contract/logging/task planning specialists
- Phase 4 implementation coordination
- specialist coder agents
- test runner and implementation reviewer

Technical review is not a separate phase by default. It is a required internal
review step inside Phase 3.

## Version 1 Workflow

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

## Version 2 Workflow

```text
User
 -> Phase 1: Product Planner
 -> Gate 1: approve planning artifacts
 -> Phase 2: Tester / Evaluation Planner
 -> Gate 2: approve testing artifacts
 -> Phase 3: Technical Planner + Technical Reviewer
 -> Gate 3: approve technical artifacts
 -> Phase 4: Coder
 -> Final verification and handoff
```

## Skill Entry Points

Planner/Tester only:

```text
K:\AI_IN_ACTION\vinuni-ai-project-skill\.agents\skills\planner-tester-v1\SKILL.md
```

Full workflow:

```text
K:\AI_IN_ACTION\vinuni-ai-project-skill\.agents\skills\project-workflow-v2\SKILL.md
```

Start a Planner/Tester project with:

```text
Use planner-tester-v1. Run Phase 1 and Phase 2 only. Do not code.
```

Start a full project workflow with:

```text
Use project-workflow-v2. Run the gated workflow. Do not start Phase 4 until Gate 3 is approved.
```

## Artifacts

Phase 1 creates:

- `PROJECT_PLAN.md`
- `REQUIREMENT_SUMMARY.md`

Phase 2 creates:

- `EVALUATION_PLAN.md`
- `TEST_CASES.md`
- `DEFINITION_OF_DONE.md`

Phase 3 creates:

- `TECHNICAL_DESIGN.md`
- `IMPLEMENTATION_PLAN.md`
- optional `FOLDER_STRUCTURE.md`
- optional `INTERFACE_CONTRACTS.md`
- optional `LOGGING_PLAN.md`
- optional `RUNBOOK.md`

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
