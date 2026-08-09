# Mission System

## Purpose

This document defines how learning missions are represented and operated across AI Mastery Roadmap.

A mission is both a learning unit and a durable evidence record. The system must let a future human or AI tutor understand what was assigned, what the learner built, how much assistance was required, what was demonstrated, and what should happen next without relying on chat history.

The system is intentionally small. It should provide enough structure for reliable handoff and evidence tracking without turning learning into metadata maintenance.

## Core Model

One instantiated mission normally maps to one complete GitHub work cycle:

1. one GitHub Issue;
2. one dedicated issue branch;
3. one canonical mission file under `missions/`;
4. one learner artifact or a deliberate relationship to an existing artifact;
5. one pull request, normally opened as a draft while learning is active;
6. one review and completion decision;
7. one accepted merge that preserves the mission evidence and updates progress.

A separate issue or pull request is not required merely to create the mission definition. Mission definition, learner work, reflection, review metadata, and final progress update can all evolve on the same mission branch.

This keeps the operational unit aligned with the learning unit: **one mission = one scoped learning cycle**.

## Canonical Mission Identifier

Every instantiated mission has a repository-wide unique identifier.

Format:

```text
L<level>-<type><sequence>
```

The initial type codes are:

- `M` — normal mission;
- `R` — review mission;
- `B` — boss / challenge.

Sequences use three digits and are independent within a level and type.

Examples:

```text
L01-M001
L01-R001
L01-B001
L04-M012
```

Curricula may use shorter working labels such as `M001` when the surrounding level is unambiguous. The canonical mission file, progress state, evidence references, and cross-level references should use the full identifier.

Identifiers are never reused for a different mission after they have entered repository history.

## Mission File Location and Naming

Mission files live under a level-specific directory:

```text
missions/level-01/L01-M001-fuel-cost-estimator.md
missions/level-01/L01-B001-control-flow-transfer-challenge.md
missions/level-03/L03-R002-function-decomposition-review.md
```

File names use:

```text
<canonical-id>-<short-kebab-case-title>.md
```

The mission file is the durable source of truth for the mission definition and its completed learning record.

GitHub Issues, branches, pull requests, commits, Project status, and `progress/progress.json` support the workflow but do not replace the mission file.

## Mission Types

### Normal mission

A normal mission introduces or strengthens a focused set of skills through concrete work.

It should remain small enough to review as one coherent learning unit and should normally produce a meaningful artifact or artifact increment.

### Review mission

A review mission exists because evidence exposed a specific weakness, forgotten skill, or excessive dependence on assistance.

It should target the demonstrated gap rather than repeat an entire earlier mission without reason.

A review mission receives its own canonical identifier and evidence record because the fact that review was needed is part of the learning history.

### Boss / challenge

A boss is a larger transfer assessment combining several previously introduced skills.

It should require more independent planning and should use fresh work when existing artifacts would weaken the transfer evidence. Reuse is valid only when maintaining, refactoring, extending, evaluating, or integrating existing work is itself part of the assessment objective.

Boss artifact choices remain governed by `artifact-lifecycle.md`.

## Mission Status

Mission files use a small status vocabulary:

- `planned` — instantiated and defined, but learner work has not started;
- `active` — learner work is currently in progress;
- `review` — learner work and reflection are ready for review;
- `completed` — review accepted the mission and final evidence has been recorded.

A blocked mission remains `active` and records the blocker in the mission file or GitHub Issue rather than introducing a separate permanent status.

If a mission becomes obsolete before learning begins, the GitHub Issue may be closed as not planned and the mission file may remain `planned` with a short retirement note if it already entered repository history. A completed or meaningfully attempted mission is never rewritten into a different mission merely to keep numbering tidy.

## Canonical Mission File Structure

Every mission file should contain the following sections. Exact wording may vary when a mission type benefits from it, but the information should remain recoverable.

### 1. Metadata

At minimum:

- mission ID;
- title;
- level;
- mission type;
- status;
- curriculum reference;
- GitHub Issue;
- artifact role;
- artifact path when known;
- artifact relationship when reuse or evolution is intended.

### 2. Learning Objective

A concise capability statement describing what the learner is expected to learn or demonstrate.

The objective should describe capability, not merely syntax coverage or task completion.

### 3. Target Skills

Stable skill identifiers or clearly named skills that this mission is intended to introduce, practice, review, or demonstrate.

The mission should not claim that every listed skill becomes `demonstrated` merely because the mission is completed. Final skill status is determined from evidence during review.

### 4. Prerequisites

Skills, missions, or prior evidence that should exist before the mission begins.

Prerequisites should be minimal and justified. They are not a place to list every earlier mission mechanically.

### 5. Mission Brief

The concrete learner-facing task.

It should explain the problem and required behavior without revealing the complete implementation plan. The learner should still need to decompose the problem and write the core solution.

### 6. Constraints

Important boundaries such as allowed or deferred concepts, required environment assumptions, limitations on libraries, or independence requirements.

Constraints should protect the intended learning objective rather than create artificial difficulty.

### 7. Acceptance Criteria

Observable conditions that indicate the requested artifact behavior is complete enough for review.

Acceptance criteria verify the work. They are not by themselves proof of understanding or skill mastery.

### 8. Artifact Relationship

Record whether the mission:

- creates a new standalone artifact;
- creates a project seed;
- evolves an existing artifact;
- contributes a project milestone;
- uses another relationship justified by `artifact-lifecycle.md`.

When existing work is reused, identify the preceding mission or artifact state that provides the base.

### 9. Evidence

Filled as the mission progresses and is reviewed.

Evidence should normally include enough of the following to make the mission state recoverable:

- artifact path;
- GitHub Issue;
- pull request;
- relevant commit or final merge commit;
- preceding mission/artifact reference for evolving work;
- review findings that materially affect skill assessment.

A current project path alone is not sufficient historical evidence when later missions substantially change that project.

### 10. Tutor Assistance Record

Record assistance that materially affects interpretation of the evidence, for example:

- strong implementation hints;
- debugging interventions that identified the decisive defect;
- partial code supplied after a genuine learner attempt;
- architectural guidance that substantially shaped the solution.

Routine explanations, encouragement, or every small question do not need exhaustive logging. The purpose is evidence quality, not surveillance.

### 11. Learner Reflection

After implementation, the learner records or supplies enough information to capture:

- what was built or changed;
- what they can now explain or do;
- important mistakes or difficulties;
- what they would approach differently;
- anything that still feels uncertain.

The learner's own explanation matters. A tutor-generated reflection is not evidence of learner understanding.

### 12. Review Outcome

The tutor records:

- review result;
- important findings;
- evidence-supported skill status changes;
- remaining gaps;
- whether targeted review is required;
- whether the mission can be considered completed.

The review may require further learner changes before the status becomes `completed`.

## Artifact Paths

Learner-built durable artifacts live under `projects/`.

A common path for a new level-specific artifact is:

```text
projects/level-01/fuel-cost-estimator/
```

The mission system does not require one directory per mission. When a mission deliberately evolves an earlier artifact, it should normally continue using that artifact's existing project path rather than creating artificial copies such as `project-v2` and `project-v3`.

Git history and mission evidence preserve the earlier states.

## GitHub Mission Workflow

### 1. Instantiate the mission

Create a GitHub Issue for the mission using the canonical ID and title, for example:

```text
L01-M001 — Fuel Cost Estimator
```

The issue is the operational work item. It should identify the mission goal and link or refer to the durable mission definition once the branch exists.

### 2. Create the branch

Create a branch from accepted `main` using:

```text
issue-<issue-number>-<canonical-id-lowercase>-<short-title>
```

Example:

```text
issue-12-l01-m001-fuel-cost-estimator
```

### 3. Activate repository state

On the mission branch, create the mission file from `templates/mission.md` and set its status to `active` when learner work begins.

Update the branch copy of `progress/progress.json` so:

- `current_level` identifies the active learning level;
- `current_mission` contains the canonical mission ID;
- `next_recommended_action` describes continuing the active mission.

For the first real mission, this is the point at which `current_level` changes from `0` to `1`.

### 4. Open a draft pull request

Open the mission pull request early, normally as a draft.

The draft PR is the visible review surface for the complete learning cycle and makes the active branch easy for a future tutor to discover.

The PR may use `Closes #<issue-number>` because it should close the mission issue only when the accepted mission work is actually merged.

### 5. Perform learner work

The learner writes the core solution and commits meaningful progress to the mission branch.

Tutor interaction follows the assistance boundaries in `learning-model.md`. Framework metadata, mission administration, and progress bookkeeping may be updated by the tutor; the learner's core mission solution remains learner-authored.

### 6. Prepare for review

When the learner believes the mission is complete:

- acceptance criteria have been checked;
- the learner reflection is recorded;
- material tutor assistance is recorded;
- the mission status becomes `review`;
- the draft PR is marked ready for review.

### 7. Review

The tutor reviews the complete evidence, not just whether the program runs.

The tutor may request learner changes, ask for explanations, require an additional test or modification, or identify a review need.

Only evidence actually demonstrated should affect skill status.

### 8. Complete and merge

After review is accepted:

- set mission status to `completed`;
- record the review outcome;
- update `progress/progress.json` on the branch;
- clear `current_mission`;
- add the canonical ID to `completed_missions` or the appropriate challenge list;
- update skill evidence/statuses only where justified;
- update review queue and next recommended action;
- preserve relevant PR/commit/artifact references.

The accepted PR is then merged according to the normal repository workflow. The merge makes the completed mission record and resulting progress state part of `main`.

## Active State and `main`

Protected `main` represents the last accepted repository state.

During an active mission, the newest learning state necessarily exists on the mission branch until its PR is accepted. Therefore a future tutor must not conclude that no mission is active solely because `main` has `current_mission: null`.

When resuming work, inspect open mission Issues and draft/open mission pull requests in addition to `main`. The active mission branch's `progress/progress.json` and mission file represent the working state; `main` remains the last accepted baseline.

This avoids a second administrative pull request merely to announce that a mission started.

## Progress Semantics

`progress/progress.json` remains a compact index rather than a duplicate mission database.

Use canonical mission IDs in progress fields.

For a normal mission:

- active: `current_mission = "L01-M001"` on the mission branch;
- completed: add `L01-M001` to `completed_missions` and clear `current_mission` before merge.

Bosses additionally use `open_challenges` and `completed_challenges` as appropriate.

Review missions use `completed_missions` like other learning missions and should also update the relevant `review_queue` entry when the gap is resolved or changed.

Detailed evidence, reflection, artifact history, and tutor assistance remain in the mission record and Git history rather than being copied wholesale into `progress.json`.

## Skill Evidence

Mission completion and skill mastery are separate decisions.

During review, each target skill may remain `introduced`, move to `practicing`, become `demonstrated`, or become `review_needed` according to actual evidence.

A tutor should consider:

- independence of implementation;
- quality of learner explanation;
- amount and type of assistance;
- transfer to a new context;
- ability to debug or modify the work;
- whether relevant code was newly implemented or inherited from an evolving artifact.

Artifact reuse follows `artifact-lifecycle.md` and must not inflate evidence.

## Tutor and Learner Authorship

Before learner work begins, the tutor may create:

- the mission Issue;
- mission definition and acceptance criteria;
- branch and draft PR;
- mission metadata;
- progress-state activation;
- setup guidance and learning explanations.

During learner work, the learner is responsible for the core solution and for explaining their own understanding.

The tutor may review, ask questions, provide progressively stronger hints, explain errors, and update administrative/evidence metadata. The tutor should not silently replace the learner's core implementation with an AI-written solution.

After review, the tutor may record review findings and update progress evidence because those are assessment and state-maintenance tasks rather than learner solution work.

## Mission Creation Rules

A mission should be instantiated only when it is reasonably ready to begin.

Do not pre-create every future mission file merely because a curriculum contains a planned sequence. Curricula hold the plan; `missions/` holds instantiated learning work.

This distinction keeps future missions adaptable to evidence from earlier work.

A future mission may be split, replaced, reordered, or supplemented before instantiation without rewriting a large collection of unused mission files.

## Template

`templates/mission.md` is the reusable starting point for instantiated mission files.

The template is intentionally generic across roadmap levels. Level-specific curricula determine the actual learning content.
