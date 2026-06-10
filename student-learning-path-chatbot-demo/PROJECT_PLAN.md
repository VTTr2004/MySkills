# Project Plan

## Objective

Build a small demo chatbot that helps students create a personalized learning path across multiple subjects using available course content.

The demo should show how a student can describe their goal, current level, and available study time, then receive a practical sequence of topics, resources, and next steps grounded in course materials.

## Target Users

Students who are taking one or more courses and want guidance on what to study next.

## Problem And Context

Students often have access to course content but may not know how to turn it into a clear personal study plan. They may be unsure which topics to prioritize, how to address weak areas, or how to schedule learning across multiple subjects.

This project is a 1-day demo, so the first version should prove the core advising interaction rather than become a full learning management system.

## Scope

### Must Include

- Chatbot interface for students.
- Support for multiple subjects or courses.
- Ability for the student to ask for a personalized learning path.
- Use of available course content as the main knowledge source.
- A simple intake flow asking about subject, learning goal, current level or weak topics, and available study time.
- Output that recommends a short learning path with ordered steps.
- Clear recommendations for what to review, practice, and do next.

### Should Include

- A concise explanation for why each step is recommended.
- Follow-up questions when student input is incomplete.
- A way to show which course content each recommendation is based on.
- Support for adjusting the plan when the student changes their goal, timeline, or subject.

### Defer

- User accounts and authentication.
- Long-term progress tracking.
- Teacher/admin dashboard.
- Automatic grading.
- Calendar integration.
- Full production deployment.
- Complex analytics across many students.

### Non-Goals

- The chatbot will not replace a teacher or academic advisor.
- The demo will not guarantee perfect learning outcomes.
- The demo will not create new official course requirements.
- The demo will not support every possible file format or external learning platform.
- The demo will not implement code during the planner-tester-v1 workflow.

## Key Requirements

- The chatbot must respond as a course learning assistant for students.
- The chatbot must base recommendations on provided course content rather than generic advice alone.
- The chatbot must ask clarifying questions when the student's request is too vague.
- The chatbot must produce a structured learning path with ordered steps.
- The chatbot must keep the plan realistic for the student's stated available study time.
- The chatbot must support more than one subject at the product concept level, even if the demo uses a small sample set.
- The chatbot must avoid giving unsupported claims about grades, certification, or guaranteed improvement.

## Data, Tools, Or Integrations

- Input data: available course content, such as lesson summaries, syllabus sections, topic lists, readings, notes, or practice exercises.
- Student-provided data: subject, goal, current level, weak topics, preferred timeline, and available study time.
- Likely demo setup: a small curated course-content dataset for several subjects.
- AI behavior: retrieve or reference relevant course content, then generate a personalized plan.
- No required external integrations for the 1-day demo.

## Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Course content is incomplete or poorly structured | Recommendations may be generic or inaccurate | Use a small, curated sample dataset for the demo and show source references where possible |
| Student gives vague goals | Chatbot may produce an unfocused plan | Require clarifying questions before generating a full path |
| Scope becomes too large for 1 day | Demo may remain unfinished | Limit to core chatbot flow, sample data, and learning-path output |
| AI gives unsupported academic advice | Student may trust inaccurate guidance | Add guardrails: explain limits, ground advice in course content, and avoid guarantees |
| Multi-subject support becomes complex | Demo may overbuild subject management | Use a small number of sample subjects and a simple subject selector or prompt intake |

## Open Questions

- Which sample subjects and course contents should be used for the demo?
- What format will the available course content be in for the first demo?
- Should the chatbot answer in Vietnamese, English, or both?
- Should the learning path be formatted as daily steps, weekly steps, or topic-based steps?

## Handoff To Tester

Tester should focus on:

- Whether the chatbot asks useful clarifying questions when student input is incomplete.
- Whether the chatbot uses course content in its recommendations.
- Whether the generated learning path is ordered, actionable, and realistic for the student's available time.
- Whether the chatbot handles multiple subjects without mixing unrelated content.
- Whether the chatbot avoids overclaiming outcomes or giving unsupported academic guarantees.
