# Progress Model

## Purpose

The progress model is the persistent state of the learning journey. It exists so that progress can be understood and continued without depending on the memory of a specific chat, tutor, agent, or AI model.

The repository remains the source of truth. `progress/progress.json` is a compact index of the current state, while mission files, projects, reflections, pull requests, and Git history provide the detailed evidence behind that state.

## Design Principles

The progress state should be:

- small enough to inspect manually;
- explicit enough for a future tutor to continue the journey;
- evidence-based rather than motivationally inflated;
- version-controlled;
- easy to extend when the learning system becomes more detailed;
- independent of a particular AI provider or application.

## Accepted State and Active Mission State

Protected `main` represents the last accepted learning state.

A real mission is performed on a dedicated branch and normally has an open draft or review pull request. While that mission is active, its branch may contain a newer `progress/progress.json` than `main`.

A future tutor must therefore inspect open mission Issues and pull requests before concluding from `main` that no mission is active. The active mission branch contains the working state; `main` remains the last accepted baseline until review and merge.

This model avoids a separate administrative pull request merely to announce that a mission has started.

The detailed workflow is defined in `mission-system.md`.

## State Fields

The initial state contains the following top-level fields.

### `schema_version`

Version of the progress-state structure. This allows the format to evolve later without ambiguity.

### `current_level`

The active roadmap level.

Before the first real learning mission begins, this remains `0` even if a curriculum already exists. Activating the first mission is the point at which the mission branch changes this to `1`.

Later level changes should likewise represent actual learning progression rather than curriculum availability alone.

### `current_mission`

Canonical identifier of the mission currently being worked on, or `null` when no learning mission is active in that state.

Canonical mission identifiers are defined in `mission-system.md`, for example `L01-M001`.

During an active mission, the branch copy of this field identifies the mission. After accepted review, the mission branch clears it before merge.

### `completed_missions`

Ordered list of completed canonical mission identifiers.

This is an index, not the full history. Detailed completion evidence belongs with the relevant mission and project artifacts.

Normal and review missions use this list. Boss/challenge completion is additionally represented in the challenge fields below.

### `skills`

Object keyed by stable skill identifiers. Each skill may later store a status and concise evidence references.

The initial repository contains no skill entries because no learning work has started.

### `review_queue`

Ordered list of skills or topics that require targeted review before or during further progression.

Entries should be created because repository evidence justifies review, not merely because time has passed.

A completed review mission should update the relevant queue entry according to the new evidence rather than automatically assuming the gap was resolved.

### `open_challenges`

Canonical identifiers for boss challenges or larger assessments that have been started or assigned but not completed.

### `completed_challenges`

Canonical identifiers for completed boss challenges.

### `recent_reflections`

References to the most relevant recent learner reflections. The full reflection content lives in durable mission records rather than being duplicated into this state file.

### `next_recommended_action`

A concise repository-state instruction for the next tutor. It is not a substitute for reading the relevant files.

When no mission is active, it should identify the next appropriate repository action, such as instantiating the next curriculum mission or addressing a blocking review need.

When a mission is active on a branch, that branch's value should normally point to continuing or reviewing the active mission.

## Skill Entries

When skills begin to be tracked, a minimal skill entry should follow this shape:

```json
{
  "status": "practicing",
  "evidence": [
    "L01-M003",
    "missions/level-01/L01-M003-text-normalizer.md"
  ],
  "note": "Can use the concept independently in familiar cases; needs more transfer practice."
}
```

Allowed initial statuses are defined in `learning-model.md`:

- `not_started`
- `introduced`
- `practicing`
- `demonstrated`
- `review_needed`

Evidence references should point to repository artifacts whenever possible.

Mission completion does not automatically promote every target skill. Status changes must follow the evidence recorded during review.

## Artifact Evidence and Evolution

Artifacts may evolve across several missions according to `artifact-lifecycle.md`.

Because of that, the latest contents of a project path are not always sufficient evidence for an earlier mission. Later refactoring or extension may substantially change what the learner originally produced.

When an evolving artifact matters to progress evidence, the detailed mission record should make the relevant historical state recoverable. Suitable references may include the mission identifier, artifact path, pull request, commit or merge commit, and the relationship to the preceding artifact or mission.

`progress/progress.json` should remain compact. It does not need to duplicate this full artifact history; concise evidence references may point to the mission records that preserve it.

A future tutor assessing a skill should distinguish:

- capability newly demonstrated in the referenced mission;
- capability merely inherited from reused code; and
- capability demonstrated by understanding, refactoring, extending, or replacing existing learner-written work.

Reuse alone is not evidence that the learner can reproduce a skill independently in a fresh context.

## Mission Activation

When a mission is instantiated and learner work begins, the mission branch updates progress according to `mission-system.md`.

At minimum:

- `current_level` identifies the mission's level;
- `current_mission` contains its canonical identifier;
- an active boss is also represented in `open_challenges` where applicable;
- `next_recommended_action` points to continuing the active mission.

This working state does not reach `main` until the mission is accepted and merged.

## Mission Completion

Before an accepted mission branch is merged:

- clear `current_mission`;
- add the canonical mission identifier to `completed_missions` for normal/review missions;
- move boss identifiers from `open_challenges` to `completed_challenges` when applicable;
- update skill evidence/statuses only where review justifies it;
- update the review queue according to unresolved or resolved gaps;
- reference the most relevant new reflection when useful;
- set `next_recommended_action` from the accepted evidence and curriculum.

The completed mission record remains the detailed source for reflection, assistance, review findings, and artifact history.

## Updating Progress

Progress should be updated when meaningful evidence changes the learning state, for example:

- a mission becomes active on its working branch;
- a mission is completed;
- a boss challenge is reviewed;
- a skill is demonstrated independently;
- deliberate artifact evolution provides new evidence about understanding, reuse, or refactoring;
- a recurring gap is identified;
- a review mission resolves or changes a previous gap;
- progression to a new level is justified.

Progress should not be changed simply to make the learner appear further along.

## Source of Truth and Conflicts

`progress/progress.json` summarizes the current state but does not override contradictory evidence in committed work.

If the state file says a mission is complete but the expected mission record, artifact, or review does not exist, a tutor should treat that as a state inconsistency and resolve it rather than assuming completion.

Likewise, chat memory must not silently override committed repository state.

For an evolving artifact, the current project contents also must not silently replace historical mission evidence. The relevant Git or pull-request state should be inspected when later changes make the earlier evidence ambiguous.

During active work, an open mission branch may intentionally contain a newer state than `main`. This is not a conflict; it is the working lifecycle defined in `mission-system.md`.

## Initial State

Until the first actual learning mission is activated, the state represents a journey whose learning execution has not yet started:

- level `0`;
- no active mission;
- no completed missions;
- no tracked skills;
- no challenges;
- no review queue;
- no learner reflections.

After the framework and Level 1 curriculum are ready, the next step is to instantiate and activate **`L01-M001` — Fuel Cost Estimator** according to `mission-system.md`.

## Future Extension

Possible future additions include timestamps, level completion records, richer evidence metadata, assessment history, explicit artifact relationships, or generated dashboards. They are intentionally excluded until a real need appears.
