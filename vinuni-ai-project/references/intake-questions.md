# Intake Questions

Ask questions in small batches. Do not ask all questions at once unless the user requests a form.

After each meaningful answer, use `decision-guidance.md`: evaluate whether the answer is clear, scoped, and fit for the user's timebox and delivery goal. If it is vague or risky, explain why, offer options, recommend a default, and ask the user to choose.

## Phase 1 - Project Identity

1. What is the project idea or assignment brief?
2. Who is the target user?
3. What should the user be able to do in the demo or first usable version?

## Phase 2 - AI Core

4. What is the AI agent's main job?
5. Does the agent need private documents, external APIs, web search, a database, tools, or RAG?
6. Is this single-agent, multi-step single-agent, or multi-agent?

## Phase 3 - Data And Evaluation

7. What are 5-10 sample questions, inputs, or scenarios?
8. What makes an answer or behavior good or bad?
9. What metrics or checks should be used: correctness, relevance, faithfulness, latency, cost, human rating, or task completion?

## Phase 4 - Constraints

10. How much time is available?
11. Is this a quick spike, course demo, reusable prototype, Demo Day material, team/work project, or product candidate?
12. Is a frontend required, or is API/CLI enough?
13. Are specs, ADRs, contracts, DoD, review, or handoff required?

## Phase 5 - Scope Shaping

Use `level-system.md` as preset guidance, not as a rigid classifier.

If a preset fits, say so. If not, propose a scope profile such as:

- Level 1 UI + Level 2 evaluation
- simple implementation + work-grade handoff
- course-demo engineering + strong RAG evaluation

For larger or team/work projects, consider loading the modular skills listed in `modular-skill-integration.md`.

## Phase 6 - Open Addition Check

Before writing the intake summary, ask:

```text
Truoc khi minh tong ket lai, co dieu gi ban muon bo sung khong?
Vi du: yeu cau tu giang vien, deadline, style demo, du lieu bat buoc, feature idea, dieu ban khong muon lam, yeu cau spec/ADR/contract/DoD, hoac constraint khi di lam.
```

If the user adds new information, evaluate it with `decision-guidance.md` before summarizing. If it changes scope shape, explain the tradeoff and ask the user to confirm.

## Approval Prompt

After intake, summarize:

```text
Intake summary:
Recommended scope shape:
Closest preset, if useful:
Project scope:
Non-goals:
Core agent design:
User choices:
Additional user notes:
Assumptions:
Unresolved decisions:
Required artifacts:
First implementation milestone:
```

Ask: "Ban xac nhan phan tom tat nay dung chua? Co diem nao minh hieu sai, can sua scope, hay can them/bot truoc khi minh lap plan va scaffold khong?"

If the user has not explicitly chosen between important options, do not proceed. Ask them to choose or confirm the recommended default.