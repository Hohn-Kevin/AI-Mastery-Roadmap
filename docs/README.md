# Documentation

This directory contains the durable documentation for AI Mastery Roadmap.

The repository is intended to remain understandable without relying on the memory of a particular chat, tutor, agent, or AI model. Documentation is therefore organized by responsibility rather than by conversation history.

## Structure

### `project/`

Project-wide documentation and governance.

- `scope.md` — purpose, boundaries, and long-term direction of the repository.
- `principles.md` — foundational project and learning-integrity principles.
- `github-workflow.md` — how GitHub features are used to operate the project.
- `decisions.md` — concise record of durable project decisions.

### `learning/`

Documentation for the learning system itself.

- `roadmap.md` — high-level progression from Python foundations to AI research practice.
- `learning-model.md` — missions, challenges, projects, skill evidence, and tutor behavior.
- `progress-model.md` — persistent learning-state model and evidence rules.

## Repository Sources of Truth

Different information belongs in different locations:

| Information | Source of truth |
| --- | --- |
| Project purpose and boundaries | `docs/project/` |
| Contribution workflow | `CONTRIBUTING.md` |
| High-level learning roadmap | `docs/learning/roadmap.md` |
| Learning and assessment rules | `docs/learning/learning-model.md` |
| Progress-state semantics | `docs/learning/progress-model.md` |
| Detailed level curricula | `levels/` |
| Active and completed mission definitions | `missions/` |
| Durable learner-built artifacts | `projects/` |
| Current compact learning state | `progress/` |
| Supporting learning references | `resources/` |
| Reusable repository/learning templates | `templates/` and `.github/` as appropriate |

## Documentation Rule

Do not duplicate the same rule across several documents unless a short cross-reference is necessary for clarity. When a durable decision changes, update its source-of-truth document rather than relying on chat history.