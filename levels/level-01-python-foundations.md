# Level 1 — Python Foundations

## Status

Initial curriculum baseline for Issue #7.

This document defines the current curriculum for the complete **Level 1 — Python Foundations** roadmap level. It is intentionally more detailed than the high-level roadmap, but it is not a frozen list of exercises. Mission sequencing may be refined when real learning evidence shows that a topic needs to be split, repeated, moved, or combined.

The level outcome is stable unless the roadmap itself is deliberately changed.

## Level Outcome

By the end of Level 1, the learner can independently design, implement, debug, and explain small, useful Python programs without having the core solution written for them.

The learner should be able to take a small problem, break it into manageable parts, choose suitable basic Python constructs, implement the program, test it with meaningful examples, identify obvious defects, and explain the important decisions in their own words.

Mission count is **not** a completion criterion. The planned sequence below is a baseline curriculum, not an XP track. Review missions may be inserted and planned missions may be split or combined when repository evidence justifies it.

## Beginner Entry Assumption

Level 1 assumes **no practical Python setup knowledge** and only minimal prior programming experience.

A learner should be able to enter this level without already knowing how to install Python, create a Python source file, select a working folder, use a terminal to run a script, or distinguish source code from program output.

Mission 001 therefore begins with a small environment bootstrap before the first programming artifact is implemented. The learner should understand enough of the local runtime workflow to work independently during later missions.

This bootstrap is intentionally limited to what Level 1 needs:

- install or verify a supported Python 3 interpreter;
- identify the platform-appropriate interpreter command such as `python`, `py`, or `python3`;
- verify the interpreter version;
- use a code editor to create and save a `.py` file;
- understand the role of the working directory at a basic level;
- run a script from the terminal and recognize its output;
- make a change, run the script again, and observe the changed behavior;
- recognize common setup failures such as an unavailable interpreter command and seek the correct platform-specific fix.

Virtual environments and dependency management are deliberately not required here. Level 1 work should use Python itself and the standard library only. Those environment-management skills belong to Level 2, where external dependencies become a meaningful engineering concern.

## Level Boundaries

Level 1 develops programming foundations. It should not quietly absorb later roadmap levels.

### In scope

- installing or verifying a usable Python 3 runtime for learning;
- creating and running `.py` source files;
- basic terminal/editor workflow needed to execute Python scripts;
- running and modifying Python scripts;
- basic values and data types;
- variables and assignment;
- expressions and arithmetic;
- text input and formatted output;
- explicit type conversion;
- comparisons and Boolean logic;
- conditional control flow;
- `while` and `for` loops;
- `range`, loop state, accumulators, and termination conditions;
- strings as data, including common transformations, indexing, slicing, `split`, and `join` where useful;
- lists and dictionaries;
- basic nested data such as lists of dictionaries when the problem benefits from them;
- membership checks and common collection operations;
- functions, parameters, return values, and local scope;
- decomposing a program into understandable functions;
- basic text-file reading and writing;
- load-modify-save program flow;
- simple line-based or delimiter-based data formats;
- basic traceback and debugging literacy;
- manual test cases and checking expected behavior;
- fundamental problem decomposition;
- reading, modifying, refactoring, and deliberately extending suitable learner-written artifacts from earlier missions.

### Deliberately deferred

These topics belong primarily to later roadmap levels and are not Level 1 exit requirements:

- package and module design;
- dependency and virtual-environment management;
- structured exception-handling practice;
- logging;
- JSON as an application data format;
- automated testing frameworks;
- type hints as a development discipline;
- object-oriented design;
- APIs, databases, concurrency, async, multiprocessing, and packaging;
- machine learning or numerical-computing frameworks.

A mission may expose a later concept when necessary, but exposure must not silently turn that concept into a Level 1 mastery requirement.

## Curriculum Design Principles

The sequence follows six rules.

1. **Start from an executable environment.** The first mission establishes the minimum runtime and editor workflow required to learn by building rather than assuming that setup knowledge already exists.
2. **Use before abstraction.** The learner first writes small working programs, then learns abstractions such as functions when repetition and complexity create a reason for them.
3. **One new difficulty at a time where practical.** Missions combine existing skills with a small number of new ideas rather than introducing many unrelated concepts simultaneously.
4. **Projects over isolated syntax drills.** Syntax practice may appear inside a mission, but each normal mission should produce a concrete program or meaningful program increment.
5. **Boss challenges test transfer.** A boss does not provide a recipe that merely repeats earlier missions. It requires the learner to plan and combine known skills in a less guided context.
6. **Evidence controls progression.** If later work reveals a gap, review work is inserted instead of pretending that completion of an earlier mission permanently proved mastery.

## Cross-Cutting Practices

These practices begin early and continue throughout the level rather than being isolated into one mission:

- read Python error messages and basic tracebacks instead of treating them as opaque failures;
- predict simple program behavior before running it when useful;
- use clear variable and function names;
- separate input, processing, and output conceptually even before formal architecture is introduced;
- test normal cases and obvious boundary cases manually;
- explain why a chosen condition, loop, collection, or function is appropriate;
- read existing learner-written code before modifying it;
- reuse earlier code deliberately when reuse supports the current learning goal;
- refactor or replace earlier code when the new requirement exposes a weakness rather than blindly preserving it;
- keep learner-written core logic separate from tutor-provided explanations and hints;
- record reflection and review evidence according to the learning model.

Git and GitHub continue to be used as the project workflow, but Git proficiency is not a Level 1 exit criterion because formal software-engineering workflow belongs to Level 2.

## Level 1 Artifact Strategy

Level 1 applies the repository-wide artifact lifecycle principle being formalized in Issue #9.

The curriculum should produce a **mixture** of artifact types rather than treating every mission as disposable or forcing every mission into one long-lived project.

### Standalone artifacts

Many missions intentionally create a fresh small program. These expose the learner to new problem contexts and provide independent evidence that a skill can be applied without relying on an existing codebase.

### Evolving artifacts

Selected artifacts are intentionally revisited later. The learner should experience what it means to open older code, understand it again, change requirements, refactor weak structure, preserve useful parts, and extend the program with new capabilities.

### Project seeds and milestones

Some early artifacts may become seeds for a larger Level 1 project. A later mission can turn a simple prototype into a more capable application when doing so creates a natural reason to use newly learned skills.

### Reuse rule

Reuse is encouraged when it creates useful learning evidence. It must not be used to bypass a skill that should be demonstrated independently.

A mission that extends an earlier artifact should make the relationship explicit. Repository history should preserve the evolution rather than replacing the earlier learning evidence with an unexplained final state.

The exact artifact metadata and mission-file representation are defined by the global artifact-lifecycle and mission-system work rather than by this curriculum.

## Skill Map

The following capabilities form the Level 1 skill scope. Stable skill identifiers should be finalized when the mission/progress implementation begins.

### A. Environment, program execution, and data

The learner can:

- install or verify a usable Python 3 interpreter for the learning environment;
- identify how to invoke the interpreter on the current platform;
- create and save a Python source file;
- run a Python script from the terminal and distinguish source code from program output;
- make a simple edit-run-observe cycle without tutor control of every command;
- create, read, and update variables;
- work with `str`, `int`, `float`, `bool`, and `None` at a foundational level;
- recognize that values have types and that operations depend on those types;
- convert between basic types deliberately;
- use arithmetic operators and understand basic operator precedence;
- use `print()` and `input()` appropriately for small CLI programs;
- produce readable output with f-strings.

### B. Decisions

The learner can:

- compare values;
- construct Boolean expressions;
- use `and`, `or`, and `not` deliberately;
- use `if`, `elif`, and `else` to model mutually exclusive and conditional behavior;
- reason about branch order and unreachable or overlapping conditions;
- distinguish a Boolean condition from the action performed when it is true.

### C. Repetition

The learner can:

- use `while` when repetition depends on a changing condition;
- use `for` when iterating over a sequence or known range;
- use `range()` appropriately;
- maintain loop state and accumulators;
- avoid common accidental infinite loops;
- use `break` or `continue` when they make the control flow clearer rather than as a substitute for reasoning;
- recognize when nested loops are appropriate for small problems.

### D. Strings and collections

The learner can:

- treat strings as data that can be inspected and transformed;
- use common string methods deliberately;
- index and slice simple sequences;
- use `split()` and `join()` for simple text transformation;
- create and modify lists;
- iterate over lists;
- use membership checks and common list operations;
- create, read, update, and iterate over dictionaries;
- choose between a list and dictionary for common small-program problems;
- build simple nested records when the data naturally requires them;
- accumulate counts, totals, filtered values, and lookup data using collections.

### E. Functions and decomposition

The learner can:

- define and call functions;
- pass values through parameters;
- return values instead of relying unnecessarily on global state or printing from every function;
- distinguish local variables from data outside a function at a foundational level;
- extract repeated or conceptually separate behavior into functions;
- combine small functions into a larger program flow;
- explain a program as a set of smaller responsibilities.

### F. Files and persistence

The learner can:

- open and read a text file;
- write and append text deliberately;
- use a context manager for file access;
- process file content line by line when appropriate;
- normalize simple line endings and whitespace;
- represent small amounts of structured data with a simple documented text format;
- load data, modify it in memory, and save it again;
- reason about the difference between in-memory state and persisted state.

### G. Problem solving, debugging, reuse, and explanation

The learner can:

- break a small requirement into inputs, processing, state, and outputs;
- turn a written rule into conditions and program flow;
- trace the value of variables through simple code;
- use error messages, small experiments, and temporary output to investigate defects;
- create manual test cases before declaring a program complete;
- identify obvious duplication or overly large blocks and improve them with already learned tools;
- reopen and understand an earlier learner-written artifact well enough to change it intentionally;
- distinguish useful reuse from blindly copying code that is not understood;
- explain the important behavior of learner-written code without reading a tutor-generated explanation.

## Planned Curriculum Sequence

The sequence below is the current baseline. Mission names are working curriculum names; exact mission file identifiers and final briefs are defined by the mission system.

### Segment 1 — Environment, Values, Input, and Decisions

This segment starts from the real beginner entry point and gets to useful programs immediately. It establishes the runtime workflow and data-flow model that later control flow builds on.

| Mission | Working artifact | Artifact role | Primary new skills | Why here |
| --- | --- | --- | --- | --- |
| M001 — Fuel Cost Estimator | CLI estimator for trip fuel cost | New standalone artifact after environment bootstrap | install/verify Python, editor/terminal workflow, script execution, `input`, `print`, variables, `float`, conversion, arithmetic, f-strings | Proves the learner can get from a local machine to a useful running Python program without assuming an existing Python setup. |
| M002 — Time Budget Planner | Convert and summarize a time budget | New standalone artifact | arithmetic operators, precedence, integer division/remainder where useful, numeric reasoning | Strengthens expressions before control flow adds another dimension. |
| M003 — Text Normalizer | Normalize and format user-entered text | New standalone artifact | strings, common methods, indexing/slicing, readable output | Establishes strings as manipulable data rather than only terminal text. |
| M004 — Decision Assistant | Rule-based recommendation from user inputs | New standalone artifact | comparisons, `bool`, `if`/`elif`/`else` | Introduces branching after the learner can already move data through a program. |
| M005 — Tiered Price Calculator | Calculate a price from several rules | New standalone artifact | compound Boolean logic, `and`/`or`/`not`, branch ordering | Deepens decision logic and exposes overlapping-rule mistakes. |

#### Ready-to-author requirements for the first segment

The first mission briefs should preserve these constraints:

- M001 must not assume Python is already installed or correctly available from the terminal.
- M001 should guide the learner through installation or verification, version checking, creating a working directory and `.py` file, running it, changing it, and rerunning it before the Fuel Cost Estimator is implemented.
- Setup guidance should account for common platform differences such as `python`, `py`, and `python3` rather than hard-coding one operating system as the only valid route.
- M001 should use no third-party dependency and should not require a virtual environment.
- M001 assumes valid numeric input once programming begins; systematic exception handling is deliberately deferred.
- The learner must write the core program rather than fill blanks in tutor-generated code.
- Each mission should include a small set of acceptance examples but not implementation pseudocode that reveals the whole solution.
- Explanations should be requested after implementation so working code alone is not treated as evidence of understanding.
- M001–M005 should remain small enough to finish individually, but each should produce a complete runnable program rather than an isolated syntax worksheet.

### Segment 2 — Repetition and Program State

This segment teaches the learner to model processes that evolve over time or across repeated inputs.

| Mission | Working artifact | Artifact role | Primary new skills | Why here |
| --- | --- | --- | --- | --- |
| M006 — Savings Target Simulator | Simulate repeated contributions until a target is reached | New standalone artifact | `while`, changing state, termination conditions | A natural reason for condition-controlled repetition. |
| M007 — Batch Score Analyzer | Analyze a known sequence of scores | New standalone artifact | `for`, `range`, counters, totals, accumulators | Contrasts sequence iteration with `while`. |
| M008 — Interactive Menu Prototype | Small repeated command menu | **Project seed A** | sentinel-controlled loops, `break`, `continue` where justified | Introduces long-running CLI flow and creates a deliberately simple artifact that can later grow into a structured application. |
| M009 — Schedule/Table Generator | Generate repeated structured output | New standalone artifact | nested loops, loop-variable reasoning | Adds one controlled layer of repetition before data structures increase complexity. |

### Boss 1 — Control Flow Transfer Challenge

**Purpose:** Validate that the learner can independently combine values, input/output, arithmetic, decisions, and repetition.

The challenge should provide a problem brief and behavioral requirements but avoid step-by-step implementation instructions. The learner should decide the control-flow structure.

Evidence sought:

- conditions correctly represent written rules;
- loops terminate for the intended reasons;
- variable state is understandable;
- the learner can explain the control flow and diagnose at least one defect found during development.

### Segment 3 — Collections and Data Processing

Collections are introduced only after the learner can already reason about control flow. This lets missions focus on representing and processing multiple values rather than learning loops and collections simultaneously.

| Mission | Working artifact | Artifact role | Primary new skills | Why here |
| --- | --- | --- | --- | --- |
| M010 — Shopping Basket Manager | Maintain an in-memory basket | New standalone artifact | lists, append/remove, indexing, membership, `len` | First mutable collection with familiar real-world behavior. |
| M011 — Batch Data Filter | Filter and summarize a list of values | New standalone artifact | list iteration, conditions over collections, slicing | Connects existing loops and decisions to collection processing. |
| M012 — Inventory Lookup | Maintain item data keyed by identifier | **Project seed B** | dictionaries, lookup, update, deletion, membership | Introduces key/value representation and creates a small data-oriented artifact suitable for later evolution. |
| M013 — Frequency Counter | Count repeated values | New standalone artifact | dictionary accumulation patterns | Builds an important general-purpose transformation pattern. |
| M014 — Structured Inventory Records | Extend M012 to records with multiple fields | **Extends project seed B** | lists of dictionaries, nested access, record iteration | Teaches nested data while forcing the learner to understand and evolve an earlier artifact. |
| M015 — Inventory Summary and Filtering | Add derived summaries and filtering to M014 | **Extends project seed B** | combined list/dict processing, filtering, aggregation | Consolidates collection transformation through purposeful extension rather than another unrelated dataset. |

### Segment 4 — Functions and Problem Decomposition

Functions are introduced after the learner has experienced programs large enough to make repetition and tangled responsibilities visible. The abstraction then solves a problem the learner has actually encountered.

| Mission | Working artifact | Artifact role | Primary new skills | Why here |
| --- | --- | --- | --- | --- |
| M016 — Refactor a Monolith | Improve one earlier learner-written program | **Learner-selected artifact evolution** | function definition/call, parameters, return values | Makes functions a response to real complexity and explicitly teaches reading and improving old code. |
| M017 — Reusable Calculation Toolkit | Several related calculations behind functions | New standalone artifact | return-value flow, function contracts at a basic level | Strengthens data moving through functions in a fresh context. |
| M018 — Validation Helpers | Reusable checks for textual/user input rules | New reusable artifact | functions with decisions and loops | Demonstrates extracting recurring policy from program flow without requiring exception handling. |
| M019 — Data Processing Pipeline | Transform collection data through several functions | New standalone artifact | function composition, local scope, collection parameters/returns | Connects decomposition with realistic data processing. |
| M020 — Menu-Driven Application | Evolve M008 into an in-memory CLI application split by responsibility | **Extends project seed A** | functions + loop + collections + control flow | Revisits an intentionally primitive prototype after the learner has the tools to structure it properly. |

### Boss 2 — Independent In-Memory Application

**Purpose:** Validate independent decomposition of a non-trivial small program.

The learner receives behavior requirements for an in-memory CLI manager or similarly sized application. The challenge should require lists or dictionaries, functions, decisions, loops, and clear program flow without prescribing function names or architecture.

The tutor should normally choose a fresh problem context for Boss 2 so that artifact reuse in surrounding missions does not replace transfer evidence. If repository evidence provides a stronger assessment reason for substantial extension instead, that decision should be explicit.

Evidence sought:

- the learner identifies sensible responsibilities before or during implementation;
- functions have understandable purposes and data flow;
- collection choice fits the problem;
- the learner can modify one requirement without rewriting the entire program;
- substantial gaps trigger targeted review before file persistence is added.

### Segment 5 — Files and Persistence

Persistence arrives after the learner can manage in-memory state. This makes the new distinction clear: the program already knows how to work with data; files add durable storage rather than becoming entangled with every earlier concept at once.

| Mission | Working artifact | Artifact role | Primary new skills | Why here |
| --- | --- | --- | --- | --- |
| M021 — Text File Analyzer | Read and summarize a text file | New standalone artifact | `open`, context managers, read/line iteration, whitespace handling | First controlled transition from terminal input to external data. |
| M022 — Persistent Log Writer | Write and append durable entries | New standalone artifact | file write/append modes, newline handling | Introduces output persistence separately from parsing. |
| M023 — Persistent Inventory | Add load-modify-save persistence to the M014/M015 inventory lineage | **Extends project seed B** | load → in-memory change → save lifecycle | Revisits a known data model so the new difficulty is persistence rather than rediscovering the application domain. |
| M024 — Delimited Data Parser | Read/write a documented simple text record format | New standalone artifact | `split`, `join`, basic malformed-line checks | Provides simple structured persistence without pulling JSON/error-handling curriculum forward. |
| M025 — Persistent CLI Manager | Add persistence to the M020 application | **Extends project seed A** | files + functions + collections + control flow | Completes a visible prototype → structured application → persistent application evolution chain. |

### Boss 3 — Level 1 Capstone

**Purpose:** Determine whether the Level 1 outcome has actually been reached.

The capstone should be a small, useful CLI program whose exact domain may be chosen to remain motivating. The learner should receive goals and constraints, not a prescribed implementation plan.

The tutor should choose between a fresh capstone and a substantial evolution of an existing artifact based on the evidence still needed. If reuse is allowed, the new requirements must be large enough to demand genuine planning and the learner must be able to explain both inherited and newly written behavior. Reuse must never turn the capstone into a mechanical feature addition that fails to test independent Level 1 capability.

The final artifact should require, where naturally appropriate:

- terminal input and readable output;
- variables and basic types;
- meaningful conditional logic;
- meaningful repetition;
- at least one suitable collection;
- several learner-designed functions;
- text-file persistence;
- decomposition of the problem into understandable responsibilities;
- learner-created manual test cases.

The capstone must not be made artificially complex merely to tick every syntax box. If a required skill is better demonstrated by earlier evidence, the tutor may rely on that evidence rather than forcing an unnatural construct into the final program.

## Level 1 Completion Evidence

Level 1 is complete only when repository evidence supports the roadmap outcome. Finishing every planned mission mechanically is neither necessary nor sufficient.

Before progression to Level 2, the tutor should verify that:

1. the core Level 1 skill areas have evidence at an appropriate demonstrated level;
2. no foundational skill that blocks progression remains `review_needed`;
3. Boss 3 / the Level 1 capstone has been completed and reviewed successfully;
4. weaknesses exposed by earlier bosses have been resolved or shown not to block progression;
5. the learner can explain the important control flow, data representation, function boundaries, and persistence behavior in their own capstone;
6. the learner can make a small requirement change to their program without needing the tutor to rewrite the solution;
7. the learner has demonstrated basic debugging behavior rather than depending on the tutor to identify every defect;
8. the learner has demonstrated both creation of fresh small programs and deliberate modification of existing learner-written code;
9. where earlier artifacts were reused, the learner can explain the reused code and why reuse was appropriate;
10. the core learner implementation was learner-written under the AI-assistance rules.

If the evidence is mixed, the correct response is targeted review or another transfer task, not an arbitrary percentage threshold.

## Adaptation Rules

The curriculum is expected to evolve through evidence, but changes should remain deliberate.

The tutor may propose to:

- split a mission when it introduces too many new difficulties at once;
- combine missions when the learner demonstrates prerequisite skills more quickly than expected;
- insert a review mission after recurring errors or weak explanation;
- change an artifact domain to improve relevance without changing the target skill;
- convert a planned standalone artifact into an extension of an earlier artifact when reuse creates stronger learning evidence;
- require a fresh artifact instead of reuse when independent transfer still needs evidence;
- move a topic when actual learning shows that its prerequisites were misjudged;
- add a mission when an important Level 1 skill lacks sufficient evidence.

The tutor should not:

- skip a weak prerequisite merely to preserve the planned sequence;
- add filler missions to increase mission count;
- treat speed as proof of understanding;
- reuse an artifact merely to save effort when doing so would avoid practicing the target skill;
- preserve poor earlier structure only because code already exists;
- move Level 2 material into Level 1 simply because it is convenient for one project;
- silently change the Level 1 outcome.

Significant curriculum changes should be visible in repository history and linked to the evidence that motivated them.

## Immediate Next Step

Once the first curriculum baseline is accepted, the next scoped work should establish the mission-file format and author **Mission 001** from the M001 curriculum entry.

That follow-up may begin while Issue #7 remains open for refinement of later Level 1 curriculum details.