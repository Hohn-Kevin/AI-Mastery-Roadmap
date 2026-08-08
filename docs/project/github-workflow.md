# GitHub Workflow

## Purpose

GitHub is used as the operational layer of AI Mastery Roadmap: work planning, change isolation, review, accepted history, and major learning milestones are represented there.

## Standard Change Flow

Meaningful repository work should normally follow:

1. Create or select a scoped issue.
2. Move it to the appropriate Project status.
3. Create a dedicated branch from the accepted `main` state.
4. Implement only the issue scope.
5. Commit meaningful progress with descriptive messages.
6. Push the branch and open a pull request.
7. Move the work to `Review`.
8. Review the complete diff and resolve review threads.
9. Merge the accepted change, normally using squash merge for focused issue work.
10. Close the linked issue and move it to `Done`.
11. Delete obsolete working branches after merge.

Direct changes to `main` are not part of the normal workflow. The initial repository bootstrap was a one-time setup condition, not the ongoing model.

## Project Board

The public GitHub Project **AI Mastery Roadmap — Development Board** is the central work overview:

https://github.com/users/Hohn-Kevin/projects/1

Statuses:

- `Backlog` — planned work that is not yet prepared or prioritized for immediate execution.
- `Ready` — clearly defined work that can be started next.
- `In Progress` — work currently being actively implemented.
- `Review` — implementation is complete and awaiting review and/or merge.
- `Done` — fully completed and accepted work.

Closed historical framework issues are retained in the Project so the board reflects the development of the repository, not only current work.

## Milestones

Milestones group meaningful larger stages.

The initial milestone is `Phase 1 - Framework`, covering repository foundation, learning/progress architecture, documentation/governance, and the curriculum framework required before actual learning begins.

Future milestones should represent meaningful completed stages such as learning levels or major project phases. They should not be created merely to increase tracking detail.

## Feature Policy

| GitHub feature | Policy | Purpose |
| --- | --- | --- |
| Issues | Active | Scoped work, learning missions, changes, and technical tasks |
| Projects | Active | Central workflow and status overview |
| Milestones | Active | Group major phases and learning levels |
| Branches | Active | Isolate issue/focused work from `main` |
| Pull Requests | Active | Review checkpoint before accepted changes reach `main` |
| Rulesets / Branch Protection | Active | Protect `main` and enforce the PR workflow |
| Labels | Planned / not yet configured | Categorize issues and PRs once a stable taxonomy is defined |
| Releases / Tags | Planned | Mark meaningful completed levels or major versions |
| GitHub Actions | Planned | Add automated validation/testing when the repository benefits from it |
| Dependabot / Security | Planned | Enable when real dependency/code risk makes the features relevant |
| Wiki | Not used for now | Repository documentation remains version-controlled under `docs/` |
| Discussions | Not used for now | Reconsider only if an external community creates a real need |

## Labels

Labels are intended as a project-management tool, but no project-specific taxonomy has been configured yet.

The taxonomy should remain small and purposeful. Do not create a large label set in advance. Introduce labels when recurring issue/PR categories make filtering materially useful. Level-specific labels should not be created until level work actually exists.

## Ruleset

`main` is protected by an active repository ruleset. The intended protection includes:

- branch deletion protection;
- non-fast-forward protection;
- pull requests as the normal path into `main`;
- required resolution of review threads before merge.

Ruleset configuration lives in GitHub itself; this document records the intended project policy rather than duplicating GitHub's complete configuration export.

## Merge Strategy

Focused issue work should normally use squash merge so `main` retains a concise, understandable history while the working branch may contain multiple implementation commits.

A different merge method may be used when preserving individual commits has a clear reason.

## Automation

Project automation is already configured and active to reduce repetitive status maintenance.

Current automation handles routine Project state transitions such as adding relevant work to the Project and moving closed or completed work into the appropriate final state. The exact GitHub workflow configuration remains managed in the Project itself.

Automation supports the operational workflow but does not replace deliberate review, scope checks, or the evidence required before learning work is considered complete.