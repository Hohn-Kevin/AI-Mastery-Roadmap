# Level 1 — Python Foundations

## Status

Initial curriculum baseline for Issue #7.

This document defines the current curriculum for the complete **Level 1 — Python Foundations** roadmap level. It is intentionally more detailed than the high-level roadmap, but it is not a frozen list of exercises. Mission sequencing may be refined when real learning evidence shows that a topic needs to be split, repeated, moved, or combined.

The level outcome is stable unless the roadmap itself is deliberately changed.

## Level Outcome

By the end of Level 1, the learner can independently design, implement, debug, and explain small, useful Python programs without having the core solution written for them.

The learner should be able to take a small problem, break it into manageable parts, choose suitable basic Python constructs, implement the program, test it with meaningful examples, identify obvious defects, and explain the important decisions in their own words.

Mission count is **not** a completion criterion. The planned sequence below is a baseline curriculum, not an XP track. Review missions may be inserted and planned missions may be split or combined when repository evidence justifies it.

## Level Boundaries

Level 1 develops programming foundations. It should not quietly absorb later roadmap levels.

### In scope

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
- fundamental problem decomposition.

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

The sequence follows five rules.

1. **Use before abstraction.** The learner first writes small working programs, then learns abstractions such as functions when repetition and complexity create a reason for them.
2. **One new difficulty at a time where practical.** Missions combine existing skills with a small number of new ideas rather than introducing many unrelated concepts simultaneously.
3. **Projects over isolated syntax drills.** Syntax practice may appear inside a mission, but each normal mission should produce a concrete program or meaningful program increment.
4. **Boss challenges test transfer.** A boss does not provide a recipe that merely repeats earlier missions. It requires the learner to plan and combine known skills in a less guided context.
5. **Evidence controls progression.** If later work reveals a gap, review work is inserted instead of pretending that completion of an earlier mission permanently proved mastery.

## Cross-Cutting Practices

These practices begin early and continue throughout the level rather than being isolated into one mission:

- read Python error messages and basic tracebacks instead of treating them as opaque failures;
- predict simple program behavior before running it when useful;
- use clear variable and function names;
- separate input, processing, and output conceptually even before formal architecture is introduced;
- test normal cases and obvious boundary cases manually;
- explain why a chosen condition, loop, collection, or function is appropriate;
- keep learner-written core logic separate from tutor-provided explanations and hints;
- record reflection and review evidence according to the learning model.

Git and GitHub continue to be used as the project workflow, but Git proficiency is not a Level 1 exit criterion because formal software-engineering workflow belongs to Level 2.

## Skill Map

The following capabilities form the Level 1 skill scope. Stable skill identifiers should be finalized when the mission/progress implementation begins.

### A. Program execution and data

The learner can:

- run a Python script and distinguish source code from program output;
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

### G. Problem solving, debugging, and explanation

The learner can:

- break a small requirement into inputs, processing, state, and outputs;
- turn a written rule into conditions and program flow;
- trace the value of variables through simple code;
- use error messages, small experiments, and temporary output to investigate defects;
- create manual test cases before declaring a program complete;
- identify obvious duplication or overly large blocks and improve them with already learned tools;
- explain the important behavior of learner-written code without reading a tutor-generated explanation.

## Planned Curriculum Sequence

The sequence below is the current baseline. Mission names are working curriculum names; exact mission file identifiers and final briefs are defined by the mission system.

### Segment 1 — Values, Input, and Decisions

This segment gets to useful programs immediately. It establishes the data-flow model that later control flow builds on.

| Mission | Working artifact | Primary new skills | Why here |
| --- | --- | --- | --- |
| M001 — Fuel Cost Estimator | CLI estimator for trip fuel cost | script execution, `input`, `print`, variables, `float`, conversion, arithmetic, f-strings | Produces a useful result with the smallest meaningful set of Python concepts. |
| M002 — Time Budget Planner | Convert and summarize a time budget | arithmetic operators, precedence, integer division/remainder where useful, numeric reasoning | Strengthens expressions before control flow adds another dimension. |
| M003 — Text Normalizer | Normalize and format user-entered text | strings, common methods, indexing/slicing, readable output | Establishes strings as manipulable data rather than only terminal text. |
| M004 — Decision Assistant | Rule-based recommendation from user inputs | comparisons, `bool`, `if`/`elif`/`else` | Introduces branching after the learner can already move data through a program. |
| M005 — Tiered Price Calculator | Calculate a price from several rules | compound Boolean logic, `and`/`or`/`not`, branch ordering | Deepens decision logic and exposes overlapping-rule mistakes. |

#### Ready-to-author requirements for the first segment

The first mission briefs should preserve these constraints:

- M001 assumes valid numeric input; systematic exception handling is deliberately deferred.
- The learner must write the core program rather than fill blanks in tutor-generated code.
- Each mission should include a small set of acceptance examples but not implementation pseudocode that reveals the whole solution.
- Explanations should be requested after implementation so working code alone is not treated as evidence of understanding.
- M001–M005 should remain small enough to finish individually, but each should produce a complete runnable program rather than an isolated syntax worksheet.

### Segment 2 — Repetition and Program State

This segment teaches the learner to model processes that evolve over time or across repeated inputs.

| Mission | Working artifact | Primary new skills | Why here |
| --- | --- | --- | --- |
| M006 — Savings Target Simulator | Simulate repeated contributions until a target is reached | `while`, changing state, termination conditions | A natural reason for condition-controlled repetition. |
| M007 — Batch Score Analyzer | Analyze a known sequence of scores | `for`, `range`, counters, totals, accumulators | Contrasts sequence iteration with `while`. |
| M008 — Interactive Menu Loop | Small repeated command menu | sentinel-controlled loops, `break`, `continue` where justified | Introduces long-running CLI flow without yet adding collections. |
| M009 — Schedule/Table Generator | Generate repeated structured output | nested loops, loop-variable reasoning | Adds one controlled layer of repetition before data structures increase complexity. |

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

| Mission | Working artifact | Primary new skills | Why here |
| --- | --- | --- | --- |
| M010 — Shopping Basket Manager | Maintain an in-memory basket | lists, append/remove, indexing, membership, `len` | First mutable collection with familiar real-world behavior. |
| M011 — Batch Data Filter | Filter and summarize a list of values | list iteration, conditions over collections, slicing | Connects existing loops and decisions to collection processing. |
| M012 — Inventory Lookup | Maintain item data keyed by identifier | dictionaries, lookup, update, deletion, membership | Introduces key/value representation after lists are understood. |
| M013 — Frequency Counter | Count repeated values | dictionary accumulation patterns | Builds an important general-purpose transformation pattern. |
| M014 — Structured Records | Manage several records with multiple fields | lists of dictionaries, nested access, record iteration | Prepares for realistic in-memory applications without introducing classes. |
| M015 — Collection Transformation | Produce a derived summary from structured records | combined list/dict processing, filtering, aggregation | Consolidates collection choice and transformation before functions. |

### Segment 4 — Functions and Problem Decomposition

Functions are introduced after the learner has experienced programs large enough to make repetition and tangled responsibilities visible. The abstraction then solves a problem the learner has actually encountered.

| Mission | Working artifact | Primary new skills | Why here |
| --- | --- | --- | --- |
| M016 — Refactor a Monolith | Improve one earlier learner-written program | function definition/call, parameters, return values | Makes functions a response to real complexity rather than abstract syntax. |
| M017 — Reusable Calculation Toolkit | Several related calculations behind functions | return-value flow, function contracts at a basic level | Strengthens data moving through functions. |
| M018 — Validation Helpers | Reusable checks for textual/user input rules | functions with decisions and loops | Demonstrates extracting recurring policy from program flow without requiring exception handling. |
| M019 — Data Processing Pipeline | Transform collection data through several functions | function composition, local scope, collection parameters/returns | Connects decomposition with realistic data processing. |
| M020 — Menu-Driven Application | In-memory CLI application split by responsibility | functions + loop + collections + control flow | First integrated application structure before persistence. |

### Boss 2 — Independent In-Memory Application

**Purpose:** Validate independent decomposition of a non-trivial small program.

The learner receives behavior requirements for an in-memory CLI manager or similarly sized application. The challenge should require lists or dictionaries, functions, decisions, loops, and clear program flow without prescribing function names or architecture.

Evidence sought:

- the learner identifies sensible responsibilities before or during implementation;
- functions have understandable purposes and data flow;
- collection choice fits the problem;
- the learner can modify one requirement without rewriting the entire program;
- substantial gaps trigger targeted review before file persistence is added.

### Segment 5 — Files and Persistence

Persistence arrives after the learner can manage in-memory state. This makes the new distinction clear: the program already knows how to work with data; files add durable storage rather than becoming entangled with every earlier concept at once.

| Mission | Working artifact | Primary new skills | Why here |
| --- | --- | --- | --- |
| M021 — Text File Analyzer | Read and summarize a text file | `open`, context managers, read/line iteration, whitespace handling | First controlled transition from terminal input to external data. |
| M022 — Persistent Log Writer | Write and append durable entries | file write/append modes, newline handling | Introduces output persistence separately from parsing. |
| M023 — Load-Modify-Save Tracker | Persist a simple list of records | load → in-memory change → save lifecycle | Connects file I/O to existing collections and functions. |
| M024 — Delimited Data Parser | Read/write a documented simple text record format | `split`, `join`, basic malformed-line checks | Provides simple structured persistence without pulling JSON/error-handling curriculum forward. |
| M025 — Persistent CLI Manager | Add persistence to an integrated CLI application | files + functions + collections + control flow | Consolidates the complete technical Level 1 skill set. |

### Boss 3 — Level 1 Capstone

**Purpose:** Determine whether the Level 1 outcome has actually been reached.

The capstone should be a small, useful CLI program whose exact domain may be chosen to remain motivating. The learner should receive goals and constraints, not a prescribed implementation plan.

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
8. the core learner implementation was learner-written under the AI-assistance rules.

If the evidence is mixed, the correct response is targeted review or another transfer task, not an arbitrary percentage threshold.

## Adaptation Rules

The curriculum is expected to evolve through evidence, but changes should remain deliberate.

The tutor may propose to:

- split a mission when it introduces too many new difficulties at once;
- combine missions when the learner demonstrates prerequisite skills more quickly than expected;
- insert a review mission after recurring errors or weak explanation;
- change an artifact domain to improve relevance without changing the target skill;
- move a topic when actual learning shows that its prerequisites were misjudged;
- add a mission when an important Level 1 skill lacks sufficient evidence.

The tutor should not:

- skip a weak prerequisite merely to preserve the planned sequence;
- add filler missions to increase mission count;
- treat speed as proof of understanding;
- move Level 2 material into Level 1 simply because it is convenient for one project;
- silently change the Level 1 outcome.

Significant curriculum changes should be visible in repository history and linked to the evidence that motivated them.

## Immediate Next Step

Once the first curriculum baseline is accepted, the next scoped work should establish the mission-file format and author **Mission 001** from the M001 curriculum entry.

That follow-up may begin while Issue #7 remains open for refinement of later Level 1 curriculum details.