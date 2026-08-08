# Contributing to AI Mastery Roadmap

AI Mastery Roadmap is both a personal learning journey and a repository that may become useful to others. Contributions should preserve its primary purpose: building real understanding through practical, progressively harder work.

## Core Rule

Repository infrastructure and learning content are treated differently.

### Repository and roadmap maintenance

AI tools and contributors may directly create or improve:

- repository documentation;
- GitHub templates;
- roadmap structure;
- mission specifications;
- progress/state schemas;
- resource lists;
- automation and repository tooling.

### Learning work

Once a mission is part of the actual learning phase, the learner is expected to write the core solution unless the mission explicitly states otherwise.

AI may:

- explain concepts;
- ask guiding questions;
- review code;
- identify bugs;
- explain error messages;
- suggest tests;
- challenge assumptions;
- review architecture;
- provide hints of increasing specificity when needed.

AI should not silently replace the learner by generating the complete core solution to a learning task.

## Working with Issues

Meaningful repository changes should normally correspond to a GitHub issue.

An issue should define:

- the goal;
- the intended scope;
- relevant constraints;
- a clear definition of done.

Keep changes inside the issue scope. If useful work is discovered that does not belong to the current issue, create or propose a separate issue instead of expanding the current one without limit.

## Branches

Use a dedicated branch for each issue or focused change.

Recommended naming:

```text
issue-<number>-<short-description>
```

Example:

```text
issue-12-python-functions-mission
```

`main` should represent the accepted state of the learning journey and repository.

## Commits

Commits should describe meaningful progress and remain understandable later.

Prefer messages such as:

```text
docs: define mission template
feat: add password generator mission
refactor: separate parsing from CLI handling
test: cover invalid user input
```

Avoid meaningless commit messages such as `fix`, `test`, `stuff`, or `asdf` when a more descriptive message is possible.

Learning mistakes do not need to be hidden, but the history should remain interpretable.

## Pull Requests

Pull requests are checkpoints for review and reflection.

A pull request should explain:

- what changed;
- why it changed;
- how it was verified;
- which issue it addresses;
- whether anything remains unresolved.

For learning projects, the review should evaluate understanding as well as whether the code runs.

## Learning Integrity

The purpose of the repository is mastery, not merely completion.

A task should not be marked complete solely because generated code produces the expected output. Where relevant, completion should require the learner to explain important concepts, design decisions, failure modes, or trade-offs.

Boss challenges and assessments may intentionally restrict AI assistance. Those restrictions should be stated in the corresponding mission or challenge definition.

## Scope Discipline

Prefer the smallest structure that solves the current problem.

Do not introduce frameworks, abstractions, directories, tracking systems, or automation only because they might become useful later. Expand the repository when the roadmap actually requires it.

## Documentation

Documentation should be concise enough to stay maintainable but explicit enough that a future human or AI tutor can understand the current system without relying on previous chat history.

When a decision materially affects how future missions are taught, evaluated, or recorded, document it in the repository.

## Public Repository Quality

Because the repository documents a public learning journey:

- do not commit secrets or personal credentials;
- do not publish third-party material without appropriate permission;
- keep `main` usable and understandable;
- clearly distinguish original work from copied or adapted material;
- prefer honest reflection over artificial perfection.

## Changing the Learning System

The roadmap is expected to evolve. Improvements are welcome when evidence from actual learning shows that the current structure is insufficient.

Major changes to levels, progress tracking, assessment rules, or AI-assistance rules should be proposed explicitly rather than introduced accidentally inside unrelated work.
