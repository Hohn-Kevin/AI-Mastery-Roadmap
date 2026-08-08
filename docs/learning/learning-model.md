# Learning Model

## Purpose

This document defines how learning work is represented in AI Mastery Roadmap. It describes the units of work and the rules future tutors should follow when selecting, reviewing, and adapting learning tasks.

## Mission

A mission is the primary unit of learning work.

A mission should:

- teach or strengthen a small, coherent set of skills;
- require the learner to produce something concrete;
- have a clear objective and completion criteria;
- be large enough to feel meaningful but small enough to review as one unit;
- connect theory to implementation as quickly as practical;
- end with reflection on what was learned, what was difficult, and what should be revisited.

A mission is not considered complete merely because the final program works. The learner should also be able to explain the important concepts and decisions involved.

## Boss / Challenge

A boss or challenge is a larger assessment that combines skills from several previous missions.

Its purpose is to test transfer rather than repetition. A boss should not simply restate earlier exercises with different names.

A boss should:

- combine multiple previously introduced skills;
- require more independent planning than an ordinary mission;
- avoid step-by-step implementation instructions unless the learner is blocked;
- produce a meaningful project or project milestone;
- expose gaps that may trigger review missions before progression.

Completing a boss is a strong signal that the learner is ready to advance, but it is not an automatic guarantee. Review findings and unresolved skill gaps still matter.

## Review Mission

A review mission is a targeted return to a skill that has proven weak, forgotten, or insufficiently understood.

Review missions are created when evidence in the repository shows that a learner repeatedly struggles with a concept, cannot explain it, or depends on excessive assistance to use it.

Review is part of progression, not a failure state.

## Projects

Projects are durable artifacts produced during the journey. A project may belong to one mission, span several missions, or serve as a boss challenge.

Projects should be useful enough to demonstrate real understanding rather than existing only as filler. Where practical, they should be independently runnable, documented, and suitable for later portfolio review.

## Skill Evidence

Skills are not measured by arbitrary completion percentages.

A skill should be tracked through evidence such as:

- missions in which it was introduced;
- missions in which it was used successfully;
- boss challenges in which it was transferred to a new context;
- review comments and recurring mistakes;
- learner explanations and reflections;
- whether substantial tutor intervention was required.

The progress model stores a concise status, while the repository history and completed artifacts provide the detailed evidence.

## Skill Status

The initial status vocabulary is intentionally small:

- `not_started` — no meaningful evidence yet;
- `introduced` — the concept has been taught and used with guidance;
- `practicing` — the learner can use it but still needs repetition or occasional help;
- `demonstrated` — the learner has shown independent understanding in meaningful work;
- `review_needed` — later work exposed a gap that should be addressed.

These statuses describe evidence, not permanent ability. A previously demonstrated skill may return to `review_needed` if later work reveals a meaningful gap.

## Role of the AI Tutor

During actual learning work, the AI tutor acts as a mentor and reviewer rather than a ghostwriter.

The tutor may:

- explain concepts;
- ask diagnostic questions;
- provide hints;
- clarify errors and error messages;
- review learner-written code;
- suggest tests;
- challenge design decisions;
- identify gaps and recommend review work;
- update or propose updates to repository learning state after evidence exists.

The tutor should not normally provide the complete core solution to an active learning mission before the learner has made a genuine attempt.

Repository setup, documentation, templates, curriculum design, and progress infrastructure are not learner-solution work and may be created with AI assistance.

## Determining the Next Mission

A future tutor should determine the next step from repository evidence, not from chat memory.

The tutor should, in order:

1. Read the current progress state.
2. Check for an active mission and continue it before creating unrelated work.
3. Check for skills marked `review_needed` and decide whether they block progression.
4. Review recently completed mission reflections and review findings.
5. Check the current level and its curriculum once that curriculum exists.
6. Select the next planned mission or create a targeted review mission when justified by evidence.
7. Avoid skipping prerequisites solely because the learner wants faster progression.
8. Avoid repeating already demonstrated material without a reason recorded in the repository.

If repository state and chat statements conflict, the tutor should inspect the relevant committed artifacts and clarify the discrepancy before changing progress.

## Completion and Reflection

Each completed mission should eventually record at least:

- what was built;
- which skills were exercised;
- what the learner can now explain or do;
- important mistakes or difficulties;
- any remaining gap;
- whether a review mission is needed.

The exact mission file format will be defined with the mission system in a later scoped issue.
