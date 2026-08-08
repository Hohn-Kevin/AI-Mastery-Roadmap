# AI Mastery Roadmap

AI Mastery Roadmap is a long-term, project-based learning repository for developing from foundational programming skills toward advanced AI engineering and research.

The repository is not intended to be a conventional course. It is the persistent, version-controlled state of the learning journey: roadmap, missions, projects, progress, reflections, and increasingly difficult technical challenges.

## Goal

Build the practical and theoretical foundation required to become a strong AI engineer and, over time, develop the depth needed to work with modern machine learning systems, deep learning, transformers, research papers, and original experiments.

The journey is deliberately long-term. Visible progress, completed projects, and demonstrated understanding matter more than rushing through topics.

## Learning Philosophy

The roadmap follows a few core principles:

- **Build to learn.** Theory should lead into something concrete as quickly as possible.
- **Understand before advancing.** Completing a task is not enough if the underlying idea cannot be explained.
- **Write the important code yourself.** AI may teach, explain, review, challenge, and help debug, but it should not replace the learner during the actual learning work.
- **Use real development workflows.** Git, branches, commits, pull requests, reviews, tests, documentation, and releases are part of the learning process.
- **Increase difficulty progressively.** Missions should grow from small programs into larger systems and eventually research-oriented work.
- **Reflect on mistakes.** Problems and misconceptions are useful state and should influence later review missions.
- **Make progress persistent.** The repository, not a single chat or AI assistant, is the source of truth for the current learning state.

## Role of AI

AI acts primarily as a tutor, reviewer, coach, and debugging partner.

During repository setup, documentation, curriculum design, templates, and progress infrastructure work, AI may directly create or update project files.

Once a mission is explicitly part of the learning phase, the default rule changes:

> The learner writes the core solution. AI supports understanding rather than replacing the work.

A mission may define different rules when the learning objective specifically concerns AI-assisted development or agentic workflows.

## Learning Model

The roadmap is organized around visible progression rather than isolated lessons.

Typical elements include:

- **Levels** — major stages of technical development.
- **Missions** — focused learning units that combine concepts with practical work.
- **Projects** — durable artifacts that demonstrate applied skills.
- **Boss challenges** — assessments that require combining previously learned skills with greater independence.
- **Review missions** — targeted work when later evidence exposes a skill gap.
- **Progress state** — a durable record of completed work, demonstrated skills, weak areas, and next steps.

The detailed learning rules live in [`docs/learning/`](docs/learning/).

## High-Level Roadmap

The current roadmap progresses through eight directional levels:

1. Python Foundations
2. Software Engineering Foundations
3. Professional Python
4. Machine Learning Foundations
5. Deep Learning
6. Transformers
7. LLM Engineering
8. AI Research Practice

See [`docs/learning/roadmap.md`](docs/learning/roadmap.md) for the maintained roadmap and level outcomes.

## Repository Structure

```text
AI-Mastery-Roadmap/
├── .github/       # GitHub issue and pull request templates
├── docs/
│   ├── project/   # Project scope, governance, decisions, and GitHub workflow
│   └── learning/  # Roadmap, learning model, and progress model
├── levels/        # Detailed curricula and completion criteria for learning levels
├── missions/      # Individual learning missions and challenges
├── projects/      # Durable learner-built artifacts
├── progress/      # Compact current learning state
├── resources/     # Curated references and learning resources
├── templates/     # Reusable learning/repository templates
├── README.md
├── CONTRIBUTING.md
└── CODE_OF_CONDUCT.md
```

See [`docs/README.md`](docs/README.md) for the documentation index and source-of-truth map.

## State and Agent Independence

A central purpose of this repository is to make the learning journey independent of any individual chat, model, or AI provider.

Important learning state is recorded in the repository. A future tutor should be able to inspect committed artifacts and determine, as far as practical:

- which missions are complete;
- which skills have been demonstrated;
- where difficulties occurred;
- which review topics remain useful;
- which projects exist;
- which level is currently active;
- what the next appropriate challenge is.

The compact state lives in `progress/progress.json`; the detailed evidence remains in missions, projects, reflections, reviews, and Git history.

## Public Learning Journey

This repository is intended to document genuine development over time. It should show finished work, meaningful iterations, reflections, and increasing technical depth rather than pretending that mistakes never happened.

The objective is not a perfectly polished history. The objective is a credible, understandable record of learning and engineering growth.

## Current Status

The repository is currently in **Phase 1 — Framework**.

Repository foundation, the high-level learning model, and persistent progress model are established. Project governance and documentation architecture are being consolidated before the detailed Level 1 curriculum and the first actual learning mission are introduced.
