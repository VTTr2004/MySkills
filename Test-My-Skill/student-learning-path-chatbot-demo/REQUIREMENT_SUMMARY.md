# Requirement Summary

## Product Goal

Create a small demo chatbot that helps students generate personalized learning paths across multiple subjects using available course content.

## Target User

Students who need help deciding what to study next in one or more courses.

## Main User Flow

1. Student opens the chatbot.
2. Student selects or states a subject/course.
3. Student describes a learning goal, current level or weak topics, and available study time.
4. Chatbot asks clarifying questions if required information is missing.
5. Chatbot uses available course content to recommend an ordered learning path.
6. Student can ask follow-up questions or request adjustments to the plan.

## Inputs

- Available course content for multiple subjects.
- Student's selected subject or course.
- Student's learning goal.
- Student's current level, known weak topics, or recent difficulties.
- Student's available study time or target timeline.
- Optional student preferences, such as review-first, practice-first, exam preparation, or project preparation.

## Expected Outputs

- A personalized learning path with ordered steps.
- Recommended course topics or materials to review.
- Suggested practice activities or exercises.
- Short reasoning for each recommended step.
- Clarifying questions when the chatbot lacks enough information.
- Optional adjustments when the student changes subject, goal, timeline, or weak topic.

## Required Behavior

- The chatbot must behave as a student-facing learning assistant.
- The chatbot must ground recommendations in available course content.
- The chatbot must support multiple subjects at the demo concept level.
- The chatbot must ask for missing information before producing a detailed plan.
- The chatbot must keep recommendations realistic for the student's available study time.
- The chatbot must separate content between subjects and avoid mixing unrelated materials.
- The chatbot must state limitations when course content is insufficient.
- The chatbot must avoid promising guaranteed grade improvement or official academic outcomes.

## Constraints

- The first version is a 1-day demo.
- The product form is a chatbot.
- The target user is the student.
- The main capability is personalized learning-path recommendation.
- The knowledge source is available course content.
- No implementation code should be written in planner-tester-v1.

## Non-Goals

- No teacher/admin dashboard in the first demo.
- No user accounts or authentication.
- No long-term progress tracking.
- No automatic grading.
- No production deployment requirement.
- No integration with school systems or learning management systems in the first demo.

## Assumptions

- A small sample set of course content will be available for the demo.
- The demo can use a limited number of subjects to prove multi-subject behavior.
- The chatbot may ask students to self-report their level and weak topics.
- The learning path can be topic-based unless the user later requests a calendar-style plan.
- The first demo prioritizes clarity and usefulness over full automation.

## Notes For Tester

- Evaluate whether the chatbot produces specific, actionable learning paths rather than vague advice.
- Check that recommendations refer to or align with the provided course content.
- Check that the chatbot asks clarifying questions when the student's goal, subject, or timeline is missing.
- Check that multi-subject behavior does not mix content from unrelated courses.
- Check that the chatbot avoids unsupported guarantees about grades or learning outcomes.
