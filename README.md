# VinUni AI Project Skill Pack

Bộ này giúp bạn bắt đầu một project AI thực chiến theo cách có cấu trúc: agent-first, evaluation-first, log-first. Backend/frontend chỉ là wrapper, không phải trọng tâm.

## Dùng Nhanh

Với bất kỳ coding agent nào, nói:

```text
Đọc K:\AI_IN_ACTION\vinuni-ai-project-skill\vinuni-ai-project\SKILL.md
rồi bắt đầu intake cho project AI mới của tôi. Hỏi từng nhóm câu hỏi trước khi code.
```

Agent nên:

1. Hỏi bạn về đề tài, user, AI job, dữ liệu, demo goal.
2. Đánh giá câu trả lời của bạn: nếu quá rộng, mơ hồ, rủi ro hoặc chưa hợp level thì giải thích lý do.
3. Đưa vài lựa chọn, khuyến nghị một option mặc định, nhưng để bạn chốt.
4. Trước khi tổng kết, hỏi bạn có muốn bổ sung điều gì chưa được hỏi tới không.
5. Tổng kết lại phần phỏng vấn: mục tiêu, scope, non-goals, assumptions, level, user choices, additional notes, unresolved decisions.
6. Hỏi bạn xác nhận phần tổng kết.
7. Chọn level phù hợp.
8. Tạo các artifact: `PROJECT_BRIEF.md`, `ARCHITECTURE.md`, `EVALUATION_PLAN.md`, `IMPLEMENTATION_PLAN.md`.
9. Hỏi bạn duyệt kế hoạch.
10. Sau khi bạn duyệt, mới scaffold và implement.

## Các Level

| Level | Khi dùng | Có gì | Không cần mặc định |
|-------|----------|-------|--------------------|
| 0 - Spike | Test ý tưởng 1-3 giờ | 1 script/app nhỏ, README, sample I/O | BE, FE, Docker |
| 1 - Course Demo | Bài thực hành hằng ngày | AI agent, `src/api` BE mỏng, `app.py` Streamlit nếu cần | Docker, CI/CD, tách FE/BE |
| 2 - Structured Agent | Muốn phát triển tiếp | Cấu trúc agent chuẩn, docs, logs, tests cơ bản, eval 10-20 cases | Deploy phức tạp |
| 3 - Demo Day | Cần chấm điểm/present | `backend/`, `frontend/`, Docker, CI/CD, deploy, eval evidence | Product hardening |
| 4 - Product Ready | Muốn thành sản phẩm | `backend/`, `frontend/`, infra, auth, DB, monitoring, cost, security | Không phù hợp daily work |

Default đề xuất:

- Daily VinUni project: Level 1
- Project có thể reuse/extend: Level 2
- Final/Demo Day: Level 3

## Cách Dùng Với Codex

Cách đơn giản nhất: yêu cầu Codex đọc `SKILL.md` theo path ở trên.

Nếu muốn auto-load trong một project, copy adapter này vào root project:

```text
vinuni-ai-project\assets\adapters\codex\AGENTS.md
```

thành:

```text
your-project\AGENTS.md
```

## Cách Dùng Với Claude Code

Copy folder skill:

```text
vinuni-ai-project
```

vào:

```text
your-project\.claude\skills\vinuni-ai-project
```

Sau đó gọi:

```text
/vinuni-ai-project Start a new VinUni AI project
```

Bạn cũng có thể dùng adapter ngắn tại:

```text
vinuni-ai-project\assets\adapters\claude\SKILL.md
```

## Cách Dùng Với Cursor

Copy:

```text
vinuni-ai-project\assets\adapters\cursor\vinuni-ai-project.mdc
```

vào:

```text
your-project\.cursor\rules\vinuni-ai-project.mdc
```

Sau đó trong Cursor chat, nhắc rule này hoặc yêu cầu agent bắt đầu VinUni AI Project intake.

## Cấu Trúc Bộ Skill

```text
vinuni-ai-project/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── intake-questions.md
│   ├── decision-guidance.md
│   ├── folder-structure-by-level.md
│   ├── level-system.md
│   ├── workflow.md
│   └── tool-adapters.md
└── assets/
    ├── templates/
    └── adapters/
```

## Prompt Khởi Động Gợi Ý

```text
Tôi muốn bắt đầu một project AI thực chiến mới.
Hãy dùng VinUni AI Project skill ở K:\AI_IN_ACTION\vinuni-ai-project-skill\vinuni-ai-project.
Đừng code ngay. Hãy hỏi tôi intake từng bước, đề xuất level, tạo brief/eval/architecture/plan, rồi chờ tôi duyệt.
Nếu câu trả lời của tôi còn quá rộng hoặc chưa hợp lý, hãy giải thích lý do, đưa option, khuyến nghị một hướng, nhưng để tôi chốt.
Sau khi phỏng vấn xong, hãy tổng kết lại những gì bạn hiểu và chờ tôi xác nhận trước khi scaffold.
Trước khi tổng kết, hãy hỏi tôi có muốn bổ sung điều gì chưa được hỏi tới không.
```

## Ghi Chú

Bộ này đang ở bản thử nghiệm. Sau 2-3 project, nên chỉnh lại câu hỏi intake, level defaults, templates và adapter theo cách bạn thực sự dùng.
