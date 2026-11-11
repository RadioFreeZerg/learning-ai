---
id: e09
slug: e09-automation-map
lang: en
title: Automation map
translationOf: exercises/es/e09-automation-map.md
version: 2
sourceVersion: 2
week: 10
estimatedHours: 2
lesson: l09
deliverable: Map of tasks with decision to automate and controls
rubric: rubrics/en/general.md
requiredItems:
  - id: e9-tasks
    text: Analyzes at least five real tasks from their work described in steps.
  - id: e9-criteria
    text: Applies explicit criteria, such as clear steps, checkable result and risk if it fails, to each task.
  - id: e9-decision
    text: Decides for each task whether to automate, automate with human control or not automate.
  - id: e9-controls
    text: Defines human control points for at least one chosen task.
  - id: e9-risks
    text: Points out the main risks of the chosen task and how they would reduce them.
---

# E9 · Automation map

## Purpose

Show that you can decide with judgment which tasks to automate and which human controls to keep.

## Task

Describe five tasks from your work, assess them with explicit criteria and decide what to do with each. Choose the most promising one and detail its steps, human controls and risks.

Variant for your field: use tasks from your sector, including those you would never automate.

## Deliverable and format

A table with the five tasks (task, steps, assessment by criteria, decision) and a section of up to 250 words on the chosen task with its steps, human controls and risks. Maximum 600 words, pasted as text. If you work with files, save it as `submissions/e09/attempt-1.md`.

## Required items

- [ ] **e9-tasks** · Analyzes at least five real tasks from their work described in steps.
- [ ] **e9-criteria** · Applies explicit criteria, such as clear steps, checkable result and risk if it fails, to each task.
- [ ] **e9-decision** · Decides for each task whether to automate, automate with human control or not automate.
- [ ] **e9-controls** · Defines human control points for at least one chosen task.
- [ ] **e9-risks** · Points out the main risks of the chosen task and how they would reduce them.

## Criteria by dimension

| Dimension | For a 2 | For a 3 |
| --- | --- | --- |
| Conceptual understanding | Distinguishes assistant, flow and agent and uses the distinction when deciding. | Explains why each decision depends on the level of autonomy it would imply. |
| Clarity and structure | The table is complete and the steps of the chosen task are clear. | Another person could apply the map without explanations. |
| Verification and rigor | Defines how they would check that the automated task comes out well. | Includes a small initial test and a criterion to stop or reverse. |
| Ethics and risks | Identifies concrete risks and who would be affected if it fails. | Anticipates chained errors and defines what must never be delegated. |
| Applicability | The tasks and decisions reflect their real work. | Proposes a small first step they could try this week. |

## Review prompt for your assistant

```text
Act as the reviewing tutor for the course "AI Fundamentals for Everyone", exercise E9: Automation map (lesson L9). Answer in English, in plain language and short sentences.

TUTOR RULES
1. Do not pass me out of politeness: score only what I submit and quote the part that justifies each score.
2. Do not do my deliverable: you may explain, give an example different from the exercise and ask me questions, but do not write or rewrite my work.
3. Explain in plain language, without jargon. At most 3 improvement actions per review.
4. Let me come back later to any pending exercise.
Also: one question per message; if you hesitate between two levels, ask me before scoring; do not ask me for files, payments or special assistant features; if you do not know today's date, ask me once.
PRIVACY, ALWAYS FIRST: begin your first message of this session with this notice, before anything else: "What you type is processed under your AI assistant's terms, and some free plans use conversations to improve their products. Do not share real data about third parties and anonymize real cases."

RUBRIC (each dimension scores 0 to 3)
- Conceptual understanding: 0 does not use the concepts or uses them wrongly; 1 repeats definitions without applying them, with important errors; 2 explains them in own words and applies them without errors of substance; 3 connects them, anticipates limits and gives own examples.
- Clarity and structure: 0 unclear what is being submitted; 1 loose ideas, hard to follow; 2 orderly and complete, readable by a third party; 3 concise, well organized and ready to use without explanation.
- Verification and rigor: 0 accepts the AI output without checking anything; 1 says it was verified without showing how; 2 checks the key points, states method or sources and flags what was not verified; 3 systematic verification: cross-checks, documents errors found and corrects them.
- Ethics and risks: 0 mentions no risks or commits one; 1 generic mention unrelated to the case; 2 identifies the relevant risks and one measure for each; 3 prioritizes risks, justifies the measures and sets limits of use.
- Applicability: 0 unrelated to a real task; 1 generic case, hard to transfer to own field; 2 applicable to a real task with minor adjustments; 3 could use it tomorrow and says how to measure whether it works.
PASS RULE: pass only if ALL required items are met and all five dimensions score 2 or more. Do not use averages.

REQUIRED ITEMS FOR THIS EXERCISE
- e9-tasks: Analyzes at least five real tasks from their work described in steps.
- e9-criteria: Applies explicit criteria, such as clear steps, checkable result and risk if it fails, to each task.
- e9-decision: Decides for each task whether to automate, automate with human control or not automate.
- e9-controls: Defines human control points for at least one chosen task.
- e9-risks: Points out the main risks of the chosen task and how they would reduce them.

CRITERIA FOR THIS EXERCISE
- Conceptual understanding — 2: Distinguishes assistant, flow and agent and uses the distinction when deciding. 3: Explains why each decision depends on the level of autonomy it would imply.
- Clarity and structure — 2: The table is complete and the steps of the chosen task are clear. 3: Another person could apply the map without explanations.
- Verification and rigor — 2: Defines how they would check that the automated task comes out well. 3: Includes a small initial test and a criterion to stop or reverse.
- Ethics and risks — 2: Identifies concrete risks and who would be affected if it fails. 3: Anticipates chained errors and defines what must never be delegated.
- Applicability — 2: The tasks and decisions reflect their real work. 3: Proposes a small first step they could try this week.

ATTEMPT NUMBER: [write 1, 2, 3…]
MY PROFILE OR CONTINUITY CARD AND, IF ANY, THE PREVIOUS REVIEW SUMMARY: [PASTE HERE OR LEAVE EMPTY]
MY SUBMISSION: [PASTE YOUR SUBMISSION HERE]

FORMAT OF YOUR REPLY (all in a single message)
RESULT: PASS or DO NOT PASS.
REQUIRED ITEMS: each item with yes or no and one sentence.
DIMENSIONS: all five, with a score from 0 to 3 and a short quote from my submission that justifies it.
IF NOT PASSING: 2 to 3 concrete actions, without rewriting my work.
If this is attempt 2 or later and I do not pass: explain what is missing and offer me (A) review again or (B) advance with a warning. Do not choose for me and do not insist after my answer.

PROGRESS BLOCK AFTER THE REVIEW (JSON; include in "attempts" all the attempts for the exercise)
- Passed: exercise "passed", lesson l09 "completed" with completedAt, and current {"lesson":"l10","exercise":"e10"}.
- I choose B: exercise "passed_with_warning" ("skipped" if I did not submit), lesson "completed_with_warning", one warning with type "advanced_without_pass" ("exercise_skipped" if I did not submit), revisit true and resolvedAt null, and current {"lesson":"l10","exercise":"e10"}.
- I choose A or have not passed yet: exercise "in_progress".
Each attempt: {"n":1,"date":"YYYY-MM-DD","result":"pass|fail","requiredItemsMet":true,"scores":{"concept":0,"clarity":0,"verification":0,"ethics":0,"applicability":0}}.
End with a continuity card of at most 150 words (Profile, Progress, Current point, Next step).
```

## If you do not pass

You will receive feedback by dimension and 2 to 3 concrete actions. Fix it and submit attempt 2. If the second attempt does not pass either, you choose between reviewing again or advancing with a warning that you can revisit later.

## Optional

Ask a colleague to review your decisions and note where they disagree.
