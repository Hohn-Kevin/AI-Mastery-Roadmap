# Project Principles

## Repository Before Chat Memory

Durable project and learning state belongs in the repository.

Chats, tutors, and agents may help interpret or update that state, but they are not the authoritative long-term memory of the project.

A future contributor or tutor should be able to inspect the repository and determine what the project is, how it is operated, where the learner is, and what should happen next.

## Build to Learn

The learning journey should connect theory to practical work quickly. Missions should produce something concrete and meaningful rather than becoming a long sequence of isolated syntax exercises.

## Understanding Before Completion

Working output alone is not enough evidence of learning. Where relevant, the learner should be able to explain the important concepts, decisions, failure modes, and trade-offs involved.

## AI as Tutor, Not Substitute

Repository setup, documentation, curriculum design, templates, and progress infrastructure may be created directly with AI assistance.

During actual learning missions, the learner writes the core learning solution unless the mission explicitly states otherwise.

AI may explain, ask questions, provide hints, debug, review, suggest tests, and challenge decisions. It should not silently replace the learner by producing the complete core solution before a genuine learner attempt.

Detailed learning behavior is defined in `../learning/learning-model.md`.

## Evidence-Based Progress

Progress is based on repository evidence, not elapsed time, motivational XP, or arbitrary percentages.

Skill status may improve, remain unchanged, or return to review when later work exposes a gap.

## Real Development Workflow

Git and GitHub are part of the learning environment rather than merely storage.

Meaningful work should normally follow the issue → branch → commit → pull request → review → merge workflow defined in `github-workflow.md` and `../../CONTRIBUTING.md`.

## Scope Discipline

Work should remain inside the active issue's scope.

Useful discoveries outside that scope should become separate issues rather than silently expanding the current task.

## Prefer the Smallest Sufficient System

Do not introduce complexity only because it may become useful later. Add structure, automation, dependencies, and governance mechanisms when the project has a concrete need for them.

## Honest Public History

The repository should document genuine growth rather than manufacture a perfect-looking history. Mistakes and revisions are acceptable when the accepted state remains understandable and the learning evidence is honest.