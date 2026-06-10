# Role-Specific Context Payloads

Subagents should not receive the full conversation by default.

Each subagent receives:

- role-specific context summary
- narrow task
- expected output format
- confirmed decisions
- relevant constraints
- forbidden decisions

## Scope Shaper Payload

```text
Project idea:
Known users:
Known constraints:
Timebox:
Current scope proposal:

Task:
Assess scope fit, overbuild risk, underbuild risk, recommended scope, and
questions to ask next.

Forbidden:
Do not make final product decisions.
```

## Spec Analyst Payload

```text
Confirmed goal:
Confirmed users:
Confirmed scope:
Known features:
Constraints:
Open questions:

Task:
Create structured requirements, assumptions, non-goals, and unresolved
decisions.
```

## Requirement Summary Writer Payload

```text
Approved project plan:
Confirmed decisions:
Non-goals:
Constraints:

Task:
Create a concise requirement summary for Tester. Exclude conversation history
and implementation details unless they affect expected behavior.
```

## Eval Designer Payload

```text
Requirement summary:
Target users:
Expected product behavior:
Known risks:
Project maturity:

Task:
Create success criteria, metrics, evaluation cases, and failure modes.
```

## Test Case Designer Payload

```text
Requirement summary:
Acceptance criteria:
Known examples:
Known risks:

Task:
Create concrete test cases with input, expected behavior, pass criteria,
failure mode watched, and priority.
```

## DoD Writer Payload

```text
Project maturity:
Required artifacts:
Acceptance criteria:
Required tests/evals:

Task:
Create a proportional Definition of Done.
```

## Test Reviewer Payload

```text
Evaluation plan:
Test cases:
Definition of Done:
Project maturity:

Task:
Find vague, missing, excessive, or unobservable checks.
```

