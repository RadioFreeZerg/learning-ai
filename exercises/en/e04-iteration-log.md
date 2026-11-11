---
id: e04
slug: e04-iteration-log
lang: en
title: Iteration log
translationOf: exercises/es/e04-iteration-log.md
version: 2
sourceVersion: 2
week: 5
estimatedHours: 2
lesson: l04
deliverable: Record of a conversation improved over 3 rounds
rubric: rubrics/en/general.md
requiredItems:
  - id: e4-three
    text: Records at least three rounds with the instruction or correction for each.
  - id: e4-change
    text: Each round describes what changed in the result.
  - id: e4-concrete
    text: The corrections are concrete, say what to change and are not general.
  - id: e4-template
    text: Ends with a reusable final instruction with blanks for what changes.
  - id: e4-nodata
    text: Includes no personal data or confidential data of third parties.
---

# E4 · Iteration log

## Purpose

Show that you can improve a result with method, in few rounds, and write down what worked.

## Task

Pick a real task in your field (a text, a plan, a short analysis). Work on it with your assistant in at least three rounds and record each one. End with the final instruction that would have given you the best result from the start, written as a template with blanks.

Variant for your field: choose a task you repeat often, so the template is useful to you later.

## Deliverable and format

A table with one row per round and these columns: round, instruction or correction you gave, what changed in the result and decision (accept, correct or discard). Below it, the final template and three lines of conclusion. Maximum 600 words, pasted as text; do not paste the assistant's full answers, summarize the essentials. If you work with files, save it as `submissions/e04/attempt-1.md`.

## Required items

- [ ] **e4-three** · Records at least three rounds with the instruction or correction for each.
- [ ] **e4-change** · Each round describes what changed in the result.
- [ ] **e4-concrete** · The corrections are concrete, say what to change and are not general.
- [ ] **e4-template** · Ends with a reusable final instruction with blanks for what changes.
- [ ] **e4-nodata** · Includes no personal data or confidential data of third parties.

## Criteria by dimension

| Dimension | For a 2 | For a 3 |
| --- | --- | --- |
| Conceptual understanding | The rounds show they understand how context and examples change the result. | Explains why each correction produced the observed effect and anticipates what another would do. |
| Clarity and structure | The table is complete and the template stands on its own. | The log can be read in a minute and the template separates fixed from variable parts. |
| Verification and rigor | States the criterion used to accept or correct each result. | Wrote the criterion before the round and applied it consistently. |
| Ethics and risks | Used placeholders instead of real data and included no information about third parties. | Points out which data would have been risky to paste and how they avoided it. |
| Applicability | The template works for a real task they repeat. | The template includes a checking line and could be shared with a colleague. |

## Review prompt for your assistant

```text
Act as the reviewing tutor for the course "AI Fundamentals for Everyone", exercise E4: Iteration log (lesson L4). Answer in English, in plain language and short sentences.

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
- e4-three: Records at least three rounds with the instruction or correction for each.
- e4-change: Each round describes what changed in the result.
- e4-concrete: The corrections are concrete, say what to change and are not general.
- e4-template: Ends with a reusable final instruction with blanks for what changes.
- e4-nodata: Includes no personal data or confidential data of third parties.

CRITERIA FOR THIS EXERCISE
- Conceptual understanding — 2: The rounds show they understand how context and examples change the result. 3: Explains why each correction produced the observed effect and anticipates what another would do.
- Clarity and structure — 2: The table is complete and the template stands on its own. 3: The log can be read in a minute and the template separates fixed from variable parts.
- Verification and rigor — 2: States the criterion used to accept or correct each result. 3: Wrote the criterion before the round and applied it consistently.
- Ethics and risks — 2: Used placeholders instead of real data and included no information about third parties. 3: Points out which data would have been risky to paste and how they avoided it.
- Applicability — 2: The template works for a real task they repeat. 3: The template includes a checking line and could be shared with a colleague.

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
- Passed: exercise "passed", lesson l04 "completed" with completedAt, and current {"lesson":"l05","exercise":"e05"}.
- I choose B: exercise "passed_with_warning" ("skipped" if I did not submit), lesson "completed_with_warning", one warning with type "advanced_without_pass" ("exercise_skipped" if I did not submit), revisit true and resolvedAt null, and current {"lesson":"l05","exercise":"e05"}.
- I choose A or have not passed yet: exercise "in_progress".
Each attempt: {"n":1,"date":"YYYY-MM-DD","result":"pass|fail","requiredItemsMet":true,"scores":{"concept":0,"clarity":0,"verification":0,"ethics":0,"applicability":0}}.
End with a continuity card of at most 150 words (Profile, Progress, Current point, Next step).
```

## If you do not pass

You will receive feedback by dimension and 2 to 3 concrete actions. Fix it and submit attempt 2. If the second attempt does not pass either, you choose between reviewing again or advancing with a warning that you can revisit later.

## Optional

Use your template on a new task and note how many rounds you needed this time.
