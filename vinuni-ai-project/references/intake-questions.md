# Intake Questions

Ask questions in small batches. Do not ask all questions at once unless the user requests a form.

After each answer, use `decision-guidance.md`: evaluate whether the answer is clear, scoped, and level-fit. If it is vague or risky, explain why, offer options, recommend a default, and ask the user to choose.

## Phase 1 - Project Identity

1. What is the project idea or assignment brief?
2. Who is the target user?
3. What should the user be able to do in the demo?

## Phase 2 - AI Core

4. What is the AI agent's main job?
5. Does the agent need private documents, external APIs, web search, a database, or tools?
6. Is this single-agent, multi-step single-agent, or multi-agent?

## Phase 3 - Data And Evaluation

7. What are 5-10 sample questions or inputs?
8. What makes an answer good or bad?
9. What metrics or checks should be used: accuracy, relevance, faithfulness, latency, cost, or human rating?

## Phase 4 - Constraints

10. How much time is available?
11. Is this a one-day course demo, a reusable prototype, or Demo Day material?
12. Is a frontend required, or is API/CLI enough?

## Phase 5 - Level Selection

Recommend a level using `level-system.md`. If the user is unsure:

- Choose Level 1 for daily course work.
- Choose Level 2 for projects the user may continue.
- Choose Level 3 only for final/demo-day projects.

## Phase 6 - Open Addition Check

Before writing the intake summary, ask:

```text
Trước khi mình tổng kết lại, có điều gì bạn muốn bổ sung không?
Ví dụ: yêu cầu từ giảng viên, constraint về deadline, style demo, dữ liệu bắt buộc dùng, ý tưởng feature, hoặc điều bạn không muốn làm.
```

If the user adds new information, evaluate it with `decision-guidance.md` before summarizing. If it changes level/scope, explain the tradeoff and ask the user to confirm.

## Approval Prompt

After intake, summarize:

```text
Intake summary:
Recommended level:
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

Ask: "Bạn xác nhận phần tổng kết này đúng chưa? Có điểm nào mình hiểu sai, cần sửa scope/level, hay cần thêm/bớt trước khi mình lập plan và scaffold không?"

If the user has not explicitly chosen between important options, do not proceed. Ask them to choose or confirm the recommended default.
