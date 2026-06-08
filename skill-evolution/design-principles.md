# Design Principles

## Core Philosophy

This skill pack is a personal AI project operating system, not only a course-demo helper.

Use the lightest process that still protects quality.
Escalate process maturity only when risk, reuse, team size, grading pressure, or production intent requires it.

## Stable Principles

- Plan before code.
- Maintain a clean context summary.
- Separate confirmed decisions from assumptions.
- Use specs as shared truth for team and AI.
- Use ADRs to prevent each agent from inventing a new architecture.
- Use contracts to let agents and teammates work in parallel.
- Define evaluation and Definition of Done before declaring completion.
- Keep backend and frontend thin unless the project goal demands more.
- Treat AI agent behavior, logs, evaluation, and handoff as core project assets.

## Bias And Context Control

Reduce context pollution by:
- splitting skills into modules;
- using references loaded only when needed;
- delegating narrow review tasks to subagents;
- sending subagents minimal payload plus clean context summary;
- returning distilled findings instead of raw logs.

## Flexibility Rule

The old Level 0-4 system is a preset rubric, not a fixed classifier.
Prefer multi-dimensional scope profiles when a project does not fit one level cleanly.
