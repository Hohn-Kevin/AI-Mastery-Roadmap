# Project Decisions

This file records concise, durable decisions that affect how AI Mastery Roadmap is maintained or taught. Detailed procedures belong in their dedicated source-of-truth documents.

## Repository and Documentation

- The repository is the durable source of project and learning state; chat memory is not authoritative.
- Project/governance documentation lives under `docs/project/`.
- Learning-system documentation lives under `docs/learning/`.
- Detailed level curricula live under `levels/`, not under general project documentation.
- Mission definitions live under `missions/`.
- Learner-built durable artifacts live under `projects/`.
- Compact current learning state lives under `progress/`.
- The GitHub Wiki is not used for now; documentation remains version-controlled in the repository.

## Learning Integrity

- The long-term objective is progression toward strong AI engineering and research practice, not Python mastery as an end in itself.
- Learning is project-based and should produce visible, meaningful artifacts.
- Progress is evidence-based rather than measured with arbitrary XP or percentage scores.
- During actual learning work, AI acts primarily as tutor and reviewer rather than ghostwriter.
- Repository setup, documentation, curriculum design, templates, and progress infrastructure may be created directly with AI assistance.

## Git and GitHub

- Meaningful work is normally tracked by a scoped GitHub issue.
- Work is performed on dedicated issue/focused branches rather than directly on `main`.
- Pull requests are the normal review checkpoint before merging to `main`.
- `main` is protected by an active ruleset.
- Focused issue work normally uses squash merge after review.
- GitHub Projects is used as the central workflow overview.
- GitHub Milestones are used for larger phases and learning levels.
- Labels are used when a stable, useful taxonomy exists; a large speculative label set is avoided.
- Releases/tags are planned for meaningful completed stages.
- GitHub Actions and dependency/security automation are introduced when real code and validation needs justify them.
- GitHub Discussions is not used for now.

## Scope and Evolution

- Work should remain inside the current issue's scope.
- New ideas outside the active scope should normally become separate issues.
- The project should prefer the smallest sufficient structure and avoid premature complexity.
- Major changes to learning philosophy, progress semantics, AI-assistance boundaries, or level structure require an explicit scoped change rather than an incidental edit.

## Decisions Intentionally Deferred

The following should be decided when a concrete need exists rather than prematurely:

- detailed label taxonomy;
- release/versioning convention;
- automated CI/validation workflows;
- dependency/security configuration;
- detailed curricula for individual levels;
- exact mission file format beyond the learning-model requirements.