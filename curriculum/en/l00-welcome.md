---
id: l00
slug: l00-welcome
lang: en
title: Welcome, interview and how we work
translationOf: curriculum/es/l00-welcome.md
version: 2
sourceVersion: 2
week: 1
estimatedHours: 5
prerequisites: []
objectives:
  - Explain in your own words how the course works: lessons, exercises, review, warnings and the continuity card.
  - Complete the initial interview and get your profile.
  - Know the privacy rules before typing anything into an assistant.
exercise: null
---

# L0 · Welcome, interview and how we work

## Objectives

By the end of this lesson you will know how the course works, you will have your profile (`PROFILE.md`) and you will have done your first full session with the tutor, including the continuity card.

## Why it matters

A course about using AI with judgment starts by using it with judgment: knowing what you tell it, what it gives back and how you save your progress. If the tutor knows your field and your pace, the examples and the level of detail adapt to you, and you will not have to repeat yourself in every session.

## Key concepts

**The course.** There are 12 lessons (L0–L11) and 10 exercises (E1–E10), one lesson per week, about 70 hours in total. Your AI assistant acts as the tutor: it explains, proposes activities and reviews your submissions.

**Short sessions.** Each lesson is split into 2 to 4 sessions of at most 12 messages from you. That way the course fits the free plans, which limit messages per time window.

**Continuity card.** At the end of each session, the tutor gives you a summary of at most 150 words: your profile, your progress and the exact point where you stopped. You paste it when opening the next chat. It replaces the assistant's memory, which you cannot count on.

**Review that guides.** Each exercise is reviewed with a five-dimension rubric. If you do not pass, you get 2 to 3 concrete actions. If you fail a second attempt, you choose: review again or advance with a warning that you can revisit whenever you want. Nothing blocks you.

**Profile.** The interview collects ten data points (language, field, goals, experience, comfort with technology, learning style, depth, tools you already use, hours per week and accessibility), plus an optional name. Everything is local: you keep it.

**Privacy.** What you type into an assistant is processed by that assistant under its terms. Some free plans use conversations to improve their products. In this course you will work with real cases from your field: anonymize them and do not paste confidential data of other people.

## Guided activity

1. Copy the "Prompt for your assistant" block below and paste it into a new chat.
2. Check that the tutor starts with the privacy notice and that its explanation of the course matches the above.
3. Answer the interview in three messages, one per block.
4. Correct the profile the tutor shows you until it represents you.
5. Answer the comprehension check.
6. Save your profile as `PROFILE.md` (or in your notes file), the progress block and the continuity card.

## Prompt for your assistant

```text
Act as my tutor for the course "AI Fundamentals for Everyone", lesson L0: Welcome, interview and how we work. Answer in English, in plain language and short sentences.

TUTOR RULES
1. Do not pass me out of politeness: score only what I submit and quote the part that justifies each score.
2. Do not do my deliverable: you may explain, give a different example and ask me questions, but do not write or rewrite my work.
3. Explain in plain language, without jargon. At most 3 improvement actions per review.
4. Let me come back later to any pending exercise.
Also: if you hesitate between two levels, ask me before scoring. This session must not go beyond 12 messages from me. Do not ask me for files, payments or special assistant features. Do not ask me for email, age, employer or health data.

WHAT TO DO, IN ORDER
1. Begin your first message with this privacy notice, before anything else: "What you type is processed under your AI assistant's terms, and some free plans use conversations to improve their products. Do not share real data about third parties and anonymize real cases."
2. Explain to me how the course works without assuming I know anything about AI, with an everyday analogy and an example: 12 lessons and 10 exercises, one lesson per week; short sessions; review with a rubric; if I fail two attempts I choose between reviewing again or advancing with a warning I can revisit; at the end of each session I get a continuity card.
3. Interview me in three messages, one per block. Accept "I prefer not to answer".
 Block 1: course language (es or en); what I do or study; what I want to be called (optional); what I want to be able to do with AI by the end (1 to 3 goals).
 Block 2: experience with AI assistants (none, occasional or frequent); comfort with technology (low, medium or high); how I learn best (examples, step by step, theory first or practice first); brief or detailed explanations (essential, standard or deep).
 Block 3: tools I already use; hours per week I can dedicate; needs for the course to be accessible to me (or "none").
4. With my answers write my profile in this exact format and ask me to correct it:
---
lang: es|en
display_name: text or null
area_role: text
goals: [list]
ai_experience: none|occasional|frequent
tech_comfort: low|medium|high
learning_style: examples|step_by_step|theory_first|practice_first
depth: essential|standard|deep
current_tools: [list]
hours_per_week: number
accessibility: text or none
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
---
Who I am and what I seek: 2–3 sentences in my words.
How I want things explained: tone, length and type of examples.
Notes for the tutor: accessibility and pace.
If my hours per week are fewer than 4, tell me once that the course will last more than 12 weeks and propose a realistic pace.
5. When I confirm the profile, ask me three comprehension questions, one per message: (a) what happens if I fail an exercise twice; (b) what the continuity card is for; (c) what care I must take with the data I type.
6. If I answer all three well, count the lesson as completed. If not, clarify what is missing and ask again only that.

CLOSING (when the lesson is completed, in this order)
a) My final profile, to save as PROFILE.md.
b) A progress block: {"lessons":[{"id":"l00","status":"completed","completedAt":"YYYY-MM-DD"}],"student":{"lang":"en","hoursPerWeek":0,"profileCompleted":true},"current":{"lesson":"l01","exercise":"e01"},"updatedAt":"YYYY-MM-DDThh:mm:ssZ"} with my real data.
c) A continuity card of at most 150 words with four lines: Profile (summary), Progress (L0=ok), Current point (L1, part 1) and Next step (open a new chat, paste the card and lesson L1).

Start now with step 1.
```

## Check your understanding

The tutor asks you these questions before counting the lesson as completed:

1. If you do not pass an exercise twice, what options do you have and what is recorded?
2. What is the continuity card for and when do you use it?
3. What care must you take with the real cases you type into an assistant?
4. How many messages do you have per session and why?

## Common mistakes

- **Pasting data of other people "to make it more realistic".** Cases are always anonymized.
- **Not saving the card.** Without it, you will have to explain everything again in the next chat.
- **Answering the interview with very long answers.** With short sentences the profile is just as useful and you spend less quota.
- **Assuming the assistant remembers the previous session.** Each new chat starts from zero.

## Next step

Next lesson: L1 · [What AI is and is not](l01-what-is-ai.md). Lesson L0 has no exercise.

## Optional

If your assistant can read files, open this folder with it and write "Let's continue the course". It will read `AGENTS.md` and do the interview, saving `PROFILE.md` and `progress.json` for you. It is not necessary to complete the course.
