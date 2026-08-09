# Artifact Lifecycle

## Purpose

This document defines how learner-created artifacts are treated across the AI Mastery Roadmap.

Learning work should produce durable evidence, but durable does not mean frozen. A program, experiment, implementation, report, model, or other meaningful result created during one mission may later be reused, extended, refactored, integrated into a larger project, or deliberately left as a standalone artifact.

The purpose of the artifact lifecycle is to teach both sides of real technical work:

- creating something new from a problem statement; and
- understanding, changing, and improving work that already exists.

The tutor should choose the artifact relationship that best supports the current learning objective. Maximizing reuse is not a goal by itself.

## Artifact

An artifact is a durable learner-produced result that can serve as learning evidence.

Depending on the level and mission, an artifact may be code, a runnable program, a library, a data-processing tool, an experiment, a model implementation, an evaluation, a technical report, a research reproduction, or another concrete result appropriate to the learning objective.

Not every artifact needs to be a polished portfolio highlight. Small artifacts may document specific steps in the journey, while larger and more mature artifacts may become portfolio projects.

## Artifact Roles

Artifact roles describe the relationship between a mission and its work. They are not permanent classifications of a repository directory.

An artifact can change role over time. A small standalone program may later become a project seed, and a project seed may later receive several milestones.

### Standalone artifact

A mission creates a new artifact intended primarily to solve its own problem.

Standalone artifacts are useful when:

- a new problem context provides important transfer practice;
- the learner needs to demonstrate a skill without relying on an existing codebase;
- reuse would hide whether the learner can independently design the required solution;
- a compact, self-contained result is the clearest evidence for the mission.

A standalone artifact may still be reused later if a future learning objective gives a good reason.

### Evolving artifact

A mission deliberately changes an existing learner-created artifact.

Evolution may include:

- adding a new capability;
- changing requirements;
- refactoring weak structure;
- replacing an earlier implementation with a better-understood one;
- adding persistence, testing, packaging, evaluation, or other capabilities introduced at a later stage;
- adapting the artifact to a new but related use case.

The learner is expected to understand the reused code. Blindly copying or preserving code that cannot be explained is not meaningful reuse evidence.

### Project seed

A project seed is an artifact intentionally suitable for later growth into a larger project.

A seed should still be useful and complete enough for its current mission. It must not be an intentionally broken or unfinished placeholder created only because later missions are expected.

Future missions may extend the seed when doing so creates a natural reason to apply newly learned skills.

### Project milestone

A project milestone is a meaningful stage in the development of a larger artifact or project that spans more than one mission.

A milestone should leave the project in an understandable and reviewable state. The learning evidence for that mission should identify what changed at that milestone rather than treating the latest version of the project as evidence for every earlier mission.

## Choosing New Work or Reuse

The tutor should make the choice from the learning objective and available evidence.

### Prefer a new artifact when

- the learner needs fresh transfer evidence in a new context;
- the target skill is central enough that existing code would do too much of the work;
- the learner has not yet demonstrated the ability to plan the relevant solution independently;
- a boss or assessment is intended to test independent composition of previously learned skills;
- the existing artifact is a poor fit and extending it would create artificial complexity.

### Prefer evolution or reuse when

- the learning objective includes reading and understanding existing code;
- a new skill naturally solves a limitation in an earlier artifact;
- refactoring is itself part of the intended learning evidence;
- preserving a meaningful domain lets the learner focus on a newly introduced technical concern;
- the learner should practice changing requirements without rebuilding everything from zero;
- an earlier project seed provides a natural base for a larger integrated result.

The tutor should not preserve an artifact merely because it already exists. Replacing weak code can be the correct learning outcome when the learner can explain why replacement is better than extension.

## Reuse and Learning Integrity

Reuse must never become a shortcut around the skill being assessed.

When an artifact is reused, the learner should be able to:

- identify which parts are being preserved and why;
- explain the relevant existing behavior;
- make the new changes themselves under the normal AI-assistance rules;
- distinguish reused capability from newly demonstrated capability;
- recognize when earlier design decisions no longer fit the new requirement.

Tutor-provided code and externally copied solutions do not become learner evidence merely because they are placed inside an evolving artifact.

## Bosses and Transfer Assessments

Boss challenges normally need stronger transfer evidence than ordinary missions.

A boss should therefore use a fresh artifact or a deliberately constrained reuse scenario when fresh implementation is necessary to show that the learner can combine the relevant skills independently.

Reuse is still valid in a boss when the assessment objective explicitly includes maintaining, refactoring, extending, evaluating, or integrating an existing codebase. The artifact relationship should match what the boss is actually intended to test.

## Preserving Evolution as Evidence

An evolving artifact must not erase the evidence produced by earlier missions.

Repository history is the primary mechanism for preserving evolution. The project does not need duplicated copies of every historical version when Git history already preserves them.

Mission and progress evidence should make an earlier state recoverable by referencing the relevant repository evidence, such as:

- the mission identifier;
- artifact or project path;
- the mission's pull request;
- a relevant commit or merge commit;
- the preceding mission or artifact relationship when reuse occurred.

A reference only to the current artifact path may be insufficient after later missions have changed that artifact substantially.

The exact metadata fields and mission-file syntax are defined by the mission system. The durable rule is that a future tutor must be able to determine what existed at the time of the mission and how later work relates to it.

## Cross-Level Reuse

Artifact evolution is not limited to one roadmap level.

A useful artifact from an earlier level may become a later learning vehicle when the new level introduces a natural engineering or research concern. For example, later work might add stronger structure, automated tests, packaging, richer data handling, machine-learning capability, evaluation, or experimental methodology to an earlier learner-built project.

Cross-level reuse should remain selective. A later curriculum must not become dependent on preserving beginner code that no longer serves the learning objective.

The tutor may refactor, migrate, split, archive, or replace an artifact when that produces better evidence and a clearer learning path.

## Portfolio Relationship

The repository records the full learning journey, while the portfolio value of artifacts may differ.

Some artifacts exist mainly as evidence of a specific skill. Others may grow through several missions into substantial projects suitable for long-term presentation.

The learning system should not optimize every mission for superficial portfolio polish. Genuine progression, understandable history, and demonstrated capability come first. Strong portfolio artifacts should emerge from meaningful work and deliberate evolution rather than from hiding early learning stages.

## Tutor Responsibilities

When designing or selecting a mission, the tutor should:

1. identify the skill evidence the mission is supposed to create;
2. inspect relevant existing learner artifacts;
3. decide whether a new artifact or deliberate reuse produces stronger evidence;
4. make any important artifact relationship explicit in the mission definition;
5. preserve fresh transfer opportunities where needed;
6. ensure reused code is understood rather than merely carried forward;
7. record enough evidence that the artifact's state at that mission remains recoverable later.

Artifact strategy may change when real learning evidence shows that the planned relationship is no longer appropriate.
