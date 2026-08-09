# L01-M001 — Fuel Cost Estimator

## Metadata

| Field | Value |
| --- | --- |
| Mission ID | `L01-M001` |
| Level | `1 — Python Foundations` |
| Type | `mission` |
| Status | `review` |
| Curriculum | `levels/level-01-python-foundations.md` — Segment 1 / M001 |
| GitHub Issue | `#13` |
| Artifact Role | `standalone` |
| Artifact Path | `projects/level-01/fuel-cost-estimator/` |
| Extends / Depends On | `none` |

## Learning Objective

Establish the minimum local Python workflow and independently build a small command-line program that accepts numeric trip and fuel data, performs the required calculation, and presents a clear result.

By the end of the mission, the learner should be able to create and run a Python source file locally, move simple user input through variables and numeric conversion into arithmetic, and explain the essential data flow without relying on a tutor-written solution.

## Target Skills

- install or verify a usable Python 3 interpreter;
- identify and use the platform-appropriate Python command;
- create and run a `.py` source file from a terminal;
- distinguish source code, user input, and program output;
- use `print()` and `input()` in a small CLI program;
- store values in variables;
- convert textual numeric input with `float()`;
- use basic arithmetic to derive a result from several inputs;
- produce readable formatted output with an f-string;
- perform a simple edit-run-observe development cycle;
- check behavior with concrete manual examples;
- explain the learner-written program's basic data flow.

## Prerequisites

- None. This is the first learning mission.
- General computer use is assumed, but practical Python setup knowledge is not.

## Mission Brief

Build a command-line **Fuel Cost Estimator** for a car trip.

The program should ask the user for:

- trip distance in kilometers;
- vehicle fuel consumption in liters per 100 kilometers;
- fuel price in euros per liter.

Using those values, the program should determine:

- how many liters of fuel the trip requires; and
- how much that fuel will cost.

Present both results clearly to the user.

Before implementing the estimator, establish the minimum working Python environment: verify or install Python 3, identify the correct interpreter command on the current platform, create the project/source file, run it from the terminal, change a simple output once, and run it again successfully.

The learner chooses the exact variable names, program order, prompts, and wording of the output.

## Constraints

- Use Python 3.
- Use only Python itself and its standard library; no third-party packages.
- No virtual environment is required.
- Assume the user enters valid numeric values; systematic error handling is deliberately deferred.
- Keep the solution within concepts introduced by this mission. Functions, lists, dictionaries, classes, automated tests, and other later abstractions are not required.
- The learner writes the core implementation. The tutor may explain concepts, answer questions, and provide progressively stronger hints, but should not provide the complete solution before a genuine learner attempt.
- Do not replace the task with a fill-in-the-blanks code skeleton.

## Acceptance Criteria

- [x] A usable Python 3 interpreter has been installed or verified locally.
- [x] The learner can identify the interpreter command used on the current machine and show its version.
- [x] The artifact contains a learner-created Python source file at `projects/level-01/fuel-cost-estimator/fuel_cost_estimator.py`.
- [x] The learner can run the source file from the terminal without the tutor controlling every command.
- [x] The program asks for trip distance in kilometers.
- [x] The program asks for fuel consumption in liters per 100 kilometers.
- [x] The program asks for fuel price in euros per liter.
- [x] The entered numeric text is converted into values suitable for calculation.
- [x] The program calculates and displays the fuel quantity required for the trip.
- [x] The program calculates and displays the total fuel cost.
- [x] The final quantities are presented readably, with sensible decimal formatting.
- [x] Example `100 km`, `5 L/100 km`, `2 €/L` produces `5.00 L` and `10.00 €` (wording may differ).
- [x] Example `250 km`, `6.4 L/100 km`, `1.75 €/L` produces `16.00 L` and `28.00 €` (wording may differ).
- [x] The learner has manually checked both examples and at least one additional self-chosen example.
- [x] Before final review, the learner can explain where input values come from, why numeric conversion is needed, how the calculation flows through the program, and how the result reaches the output.

Acceptance criteria establish readiness for review; they do not by themselves prove skill mastery.

## Artifact Relationship

**Role:** `standalone`

**Relationship:** This mission creates the first learner-built programming artifact in the roadmap. It begins as a standalone artifact so the initial evidence comes from fresh implementation rather than reused code. A later mission may reuse it only if the artifact-lifecycle rules make that pedagogically useful.

## Evidence

Fill this section as repository evidence exists.

- Artifact: `projects/level-01/fuel-cost-estimator/`
- GitHub Issue: `#13`
- Pull request: `#14`
- Learner implementation commit: `e517899f7aa5d8c1d56ae01b2ba2f5220f442565`
- Merge commit: `pending`
- Prior artifact state: `n/a`
- Additional evidence:
  - Local Python runtime verified with `py --version` -> `Python 3.13.14`.
  - Learner-created implementation is present on the mission branch and in PR #14.
  - Learner ran the source file locally from the terminal and demonstrated the edit-run-observe cycle.
  - Learner implementation uses three numeric inputs, arithmetic for fuel usage and trip cost, and f-string output formatting.
  - Manual examples observed: `250 / 6.4 / 1.75` -> `16.00 L`, `28.00 €`; `100 / 5 / 2` -> `5.00 L`, `10.00 €`; self-chosen `1230 / 12.55 / 2.10` -> `154.37 L`, `324.17 €`.
  - Learner correctly explained that `input()` initially returns text, numeric conversion is required for the intended arithmetic, assignment stores the evaluated result in `fuel_usage`, and `:.2f` changes the printed representation rather than the stored numeric value. The tutor initially misread the learner's first `:.2f` explanation; the learner had already described it as an output-formatting effect.

## Tutor Assistance Record

Record only assistance that materially affects interpretation of the learning evidence.

- Tutor provided the initial local run/edit/run bootstrap and generic syntax examples for `input()`, `float()`, and f-string decimal formatting. The learner derived the fuel calculation, wrote the estimator implementation, selected names/output wording, and performed the mission test runs.

## Learner Reflection

### What I built or changed

Ich habe einen Fuel-Cost-Estimator gebaut. Dieser fragt mittels `input()` folgende Werte vom User ab: gefahrene Kilometer, durchschnittlicher Verbrauch auf 100 Kilometer und Kosten pro Liter Sprit. Danach rechnet er intern eine Verbrauchskostenrechnung: gefahrene Kilometer / 100, um auf dasselbe Format wie der Durchschnittsverbrauch zu kommen; Ergebnis davon * Durchschnittsverbrauch, um den tatsächlichen Verbrauch zu ermitteln; und den tatsächlichen Verbrauch in Litern * Spritpreis pro Liter, um die entstandenen Kosten zu errechnen. Das Ergebnis des tatsächlichen Verbrauchs und der Kosten wird dann mittels `print()` ausgegeben.

### What I can now explain or do

Ich verstehe, wie `input()` grundsätzlich funktioniert, dass es standardmäßig einen String liefert und für die Rechnung in einen gewünschten numerischen Typ geändert werden muss. Ich verstehe, dass Variablen Ergebnisse von Rechnungen speichern können und dass man mittels f-String die Ausgabe von `print()` direkt mit Variablen verbinden und formatieren kann — im Sinne einer veränderten Ausgabe, nicht eines veränderten Werts.

### Important mistakes or difficulties

Ich würde nicht sagen, dass es Missverständnisse oder Schwierigkeiten gab. Lediglich, dass `input()` standardmäßig ein String ist, hat einen zweiten Anlauf gebraucht, wurde danach aber verstanden.

### What I would approach differently

Nichts. Ich bin mit dem Lernergebnis zufrieden.

### Remaining uncertainty

Aus dieser Mission explizit nichts. Mal sehen, was die Zukunft bringt.

## Review Outcome

**Result:** `accepted`

### Findings

- The learner-written implementation satisfies the mission brief and all acceptance criteria.
- The arithmetic is correct and was validated with both required examples plus an additional learner-chosen example.
- The learner demonstrated and explained the essential data flow from textual input through numeric conversion and arithmetic to formatted output.
- The implementation stays within Level 1 scope and does not introduce unnecessary abstractions or dependencies.
- Non-blocking hygiene note: the current Python source does not end with a final newline. This does not affect mission correctness or acceptance.

### Skill Evidence Changes

- Evidence recorded for basic terminal execution of Python source files, `input()`/`print()`, variables, `float()` conversion, arithmetic, f-string formatting, manual example checking, and explanation of basic program data flow.
- This mission contributes evidence toward these skills; it does not by itself establish long-term mastery.

### Remaining Gaps / Review Needs

- No mission-specific blocking gaps remain.
- Invalid-input handling, functions, automated tests, and other later concepts remain intentionally outside this mission's scope.

### Completion Decision

Accepted for merge. The mission remains in `review` until PR #14 is explicitly approved for merge by the learner and the post-merge completion/progress state is recorded.
