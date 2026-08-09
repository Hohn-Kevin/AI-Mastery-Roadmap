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

## State Fields

The initial state contains the following top-level fields.

### `schema_version`

Version of the progress-state structure. This allows the format to evolve later without ambiguity.

### `current_level`

The active roadmap level. Before the first learning curriculum is initialized, this is `0`.

### `current_mission`

Identifier of the mission currently being worked on, or `null` when no learning mission is active.

### `completed_missions`

Ordered list of completed mission identifiers.

This is an index, not the full history. Detailed completion evidence belongs with the relevant mission and project artifacts.

### `skills`

Object keyed by stable skill identifiers. Each skill may later store a status and concise evidence references.

The initial repository contains no skill entries because no learning work has started.

### `review_queue`

Ordered list of skills or topics that require targeted review before or during further progression.

Entries should be created because repository evidence justifies review, not merely because time has passed.

### `open_challenges`

Identifiers for boss challenges or larger assessments that have been started or assigned but not completed.

### `completed_challenges`

Identifiers for completed boss challenges.

### `recent_reflections`

References to the most relevant recent learner reflections. The full reflection content should live with durable mission or project documentation rather than being duplicated into this state file.

### `next_recommended_action`

A concise repository-state instruction for the next tutor. It is not a substitute for reading the relevant files.

Before learning begins, the value points to curriculum initialization rather than inventing a mission.

## Skill Entries

When skills begin to be tracked, a minimal skill entry should follow this shape:

```json
{
  "status": "practicing",
  "evidence": [
    "missions/003",
    "projects/example-project"
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

## Updating Progress

Progress should be updated when meaningful evidence changes the learning state, for example:

- a mission is completed;
- a boss challenge is reviewed;
- a skill is demonstrated independently;
- deliberate artifact evolution provides new evidence about understanding, reuse, or refactoring;
- a recurring gap is identified;
- a review mission resolves a previous gap;
- progression to a new level is justified.

Progress should not be changed simply to make the learner appear further along.

## Source of Truth and Conflicts

`progress/progress.json` summarizes the current state but does not override contradictory evidence in committed work.

If the state file says a mission is complete but the expected artifact or review does not exist, a tutor should treat that as a state inconsistency and resolve it rather than assuming completion.

Likewise, chat memory must not silently override committed repository state.

For an evolving artifact, the current project contents also must not silently replace historical mission evidence. The relevant Git or pull-request state should be inspected when later changes make the earlier evidence ambiguous.

## Initial State

The initial state deliberately represents a journey that has not started:

- level `0`;
- no active mission;
- no completed missions;
- no tracked skills;
- no challenges;
- no review queue;
- no learner reflections.

The next step after the framework phase is to define the first detailed curriculum before assigning Mission 1.

## Future Extension

Possible future additions include timestamps, level completion records, richer evidence metadata, assessment history, explicit artifact relationships, or generated dashboards. They are intentionally excluded from the initial model until a real need appears.
