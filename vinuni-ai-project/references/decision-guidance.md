# Decision Guidance

Use this reference when the user answers intake questions or makes scope/product/architecture choices.

## Principle

The coding agent may advise, critique, and recommend. The user decides.

Do not blindly accept vague or risky answers. Do not overrule the user silently. Make tradeoffs visible.

## Response Pattern

When a user gives an answer, classify it:

- **Clear and level-fit**: accept it and move on.
- **Vague**: ask a sharper follow-up and provide examples.
- **Too broad**: explain why it may not fit the timebox/level, then offer narrower options.
- **Too narrow or weak for the course goal**: explain what learning/evaluation value may be missing, then suggest stronger variants.
- **Technically risky**: explain the risk and suggest safer alternatives.
- **Mismatch with selected level**: recommend raising/lowering the level or trimming scope.

Use this structure:

```text
Mình thấy hướng này [ổn/chưa ổn/rủi ro] vì ...

Bạn có vài lựa chọn:
1. Option A - ...
2. Option B - ...
3. Option C - ...

Khuyến nghị của mình: Option ...
Lý do: ...

Bạn muốn chọn option nào, hay giữ ý tưởng ban đầu?
```

## Example - Travel Topic

User: "Làm chủ đề du lịch."

Good agent response:

```text
Chủ đề du lịch làm được, nhưng hiện còn quá rộng. Nếu giữ chung chung, agent dễ thành chatbot hỏi đáp du lịch bình thường, khó có evaluation rõ.

Bạn có vài hướng hẹp hơn:
1. Trip planner theo ngân sách - user nhập budget, ngày đi, sở thích; agent tạo lịch trình.
2. Travel document assistant - agent đọc chính sách visa/hành lý/booking và trả lời có nguồn.
3. Local itinerary recommender - agent gợi ý lịch trình theo thành phố, thời tiết, thời gian rảnh.

Khuyến nghị của mình: Option 1 nếu đây là bài demo một ngày, vì dễ demo và dễ tạo eval cases.

Bạn muốn chọn option nào, hay vẫn muốn giữ chủ đề du lịch tổng quát?
```

## Option Quality

Good options should be:

- Mutually different
- Small enough for the selected level
- Connected to agent behavior, not only UI
- Easy to evaluate with sample cases
- Honest about tradeoffs

## Never Do

- Do not say "I will choose X" for a major decision without user approval.
- Do not bury risks in a long plan.
- Do not keep asking generic questions when examples would help.
- Do not push Level 3/4 complexity into daily course demos.
