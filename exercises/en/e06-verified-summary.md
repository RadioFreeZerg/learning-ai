---
id: e06
slug: e06-verified-summary
lang: en
title: Verified summary
translationOf: exercises/es/e06-verified-summary.md
version: 3
sourceVersion: 3
week: 7
estimatedHours: 2
lesson: l06
deliverable: Summary of a document checked against the original
rubric: rubrics/en/general.md
requiredItems:
  - id: e6-prep
    text: Describes how the text was prepared, with trimming and replacement of personal data by placeholders.
  - id: e6-summary
    text: Includes a summary of five points or fewer generated with the assistant.
  - id: e6-check
    text: Checks each point and each figure against the original and records the result.
  - id: e6-issues
    text: Points out at least one failure, omission or change found, or explains how they checked that there was none.
  - id: e6-final
    text: Submits a final corrected version of the summary.
---

# E6 · Verified summary

## Purpose

Show that you can request a summary from the assistant with well-prepared material and check it against the original before using it.

## Task

Choose a text of 500 to 800 words that is public or that you can anonymize. Prepare it, ask for a summary of five points or fewer and compare it with the original. Correct what is needed and submit the final version with the record of the check.

Variant for your field: use a type of document you handle often (report, regulation, long email, minutes).

## Deliverable and format

A document of one to two pages, pasted as text, with four parts: preparation (maximum 80 words), initial summary, check table (point, where it appears in the original, result) and corrected final summary. Do not paste the whole original text, only the cited fragments. If you work with files, save it as `submissions/e06/attempt-1.md`.

## Required items

- [ ] **e6-prep** · Describes how the text was prepared, with trimming and replacement of personal data by placeholders.
- [ ] **e6-summary** · Includes a summary of five points or fewer generated with the assistant.
- [ ] **e6-check** · Checks each point and each figure against the original and records the result.
- [ ] **e6-issues** · Points out at least one failure, omission or change found, or explains how they checked that there was none.
- [ ] **e6-final** · Submits a final corrected version of the summary.

## Criteria by dimension

| Dimension | For a 2 | For a 3 |
| --- | --- | --- |
| Conceptual understanding | Understands that a summary can omit, change or add information and reflects it in the check. | Explains what kind of content is most prone to fail and adapts the check to it. |
| Clarity and structure | The four parts are complete and the initial summary is distinguishable from the final one. | A reader understands the result without seeing the original and sees what changed. |
| Verification and rigor | Checks each point and each figure against the original and records the result. | Detects lost conditions and exceptions and checks that nothing was added. |
| Ethics and risks | Includes no personal data and explains how they were replaced. | Weighs which data in the text would have been sensitive even if anonymized. |
| Applicability | The procedure can be repeated with another document from their work. | Sums up their preparation and checking method in a few lines as a reusable list. |

## Review prompt for your assistant

```text
Act as the reviewing tutor for the course "AI Fundamentals for Everyone", exercise E6: Verified summary (lesson L6). Answer in English, in plain language and short sentences.

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
- e6-prep: Describes how the text was prepared, with trimming and replacement of personal data by placeholders.
- e6-summary: Includes a summary of five points or fewer generated with the assistant.
- e6-check: Checks each point and each figure against the original and records the result.
- e6-issues: Points out at least one failure, omission or change found, or explains how they checked that there was none.
- e6-final: Submits a final corrected version of the summary.

CRITERIA FOR THIS EXERCISE
- Conceptual understanding — 2: Understands that a summary can omit, change or add information and reflects it in the check. 3: Explains what kind of content is most prone to fail and adapts the check to it.
- Clarity and structure — 2: The four parts are complete and the initial summary is distinguishable from the final one. 3: A reader understands the result without seeing the original and sees what changed.
- Verification and rigor — 2: Checks each point and each figure against the original and records the result. 3: Detects lost conditions and exceptions and checks that nothing was added.
- Ethics and risks — 2: Includes no personal data and explains how they were replaced. 3: Weighs which data in the text would have been sensitive even if anonymized.
- Applicability — 2: The procedure can be repeated with another document from their work. 3: Sums up their preparation and checking method in a few lines as a reusable list.

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
- Passed for the first time: exercise "passed", lesson l06 "completed" with completedAt, and current {"lesson":"l07","exercise":"e07"}.
- Passed when reopening a warned exercise: exercise "passed", lesson l06 "completed", the warning gets resolvedAt with the date, and current does not change.
- I choose B: exercise "passed_with_warning" ("skipped" if I did not submit), lesson "completed_with_warning", one warning with type "advanced_without_pass" ("exercise_skipped" if I did not submit), revisit true and resolvedAt null, and current {"lesson":"l07","exercise":"e07"}.
- I choose A or have not passed yet: exercise "in_progress".
Each attempt: {"n":1,"date":"YYYY-MM-DD","result":"pass|fail","requiredItemsMet":true,"scores":{"concept":0,"clarity":0,"verification":0,"ethics":0,"applicability":0}}.
End with a continuity card of at most 150 words (Profile, Progress, Current point, Next step).
```

## If you do not pass

You will receive feedback by dimension and 2 to 3 concrete actions. Fix it and submit attempt 2. If the second attempt does not pass either, you choose between reviewing again or advancing with a warning that you can revisit later.

## Optional

Repeat with a document twice as long, splitting it into parts, and note what was lost when joining the summaries.
