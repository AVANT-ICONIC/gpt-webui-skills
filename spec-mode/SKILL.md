---
name: spec-mode
description: ChatGPT WebUI specification work for projects without a native change workflow, plus a compatibility entry point that delegates OpenSpec projects to openspec-workflow.
---

# Spec Mode

Turn settled decisions into a buildable specification when no native change workflow already owns the job.

## OpenSpec projects delegate early

If the target project already uses OpenSpec and this is a non-trivial code change, load `openspec-workflow` and delegate immediately.

Do **not** require all product and architecture decisions to be settled before involving OpenSpec. Native OpenSpec Explore exists specifically to inspect the codebase, weigh options, and clarify change-specific uncertainty before Propose.

In an OpenSpec project, Spec Mode is therefore a compatibility entry point, not a parallel specification system.

Spec Mode is not another planning interview. The default behavior is autonomous: inspect the project, resolve factual gaps, write or refine the specification, verify coherence, and continue until the spec is ready for implementation.


## Entry condition

For standalone specification work, start when the important product and architecture decisions are already settled.

For OpenSpec projects, use the delegation rule above instead of this entry condition.

Recover the latest Plan Mode handoff and the target project's current state before doing new work.

If a material decision is genuinely unresolved, do not invent it. Record the exact decision needed and hand it back to Plan Mode.

Minor factual gaps are not planning questions. Retrieve the facts yourself.

## Prefer the project's real specification system

If the target project already uses OpenSpec, this mode delegates to `openspec-workflow`. That workflow inspects the project's real OpenSpec root, schema, existing changes, generated native skills, and available CLI behavior before deciding Explore, Propose, Update, or continuation.

Do not recreate OpenSpec semantics inside Spec Mode.

## Default when no schema exists

If the project does not already define a specification system, use the default OpenSpec-style shape:

```text
proposal
  ↓
specs
  ↓
design
  ↓
tasks
```

Conceptually:

- **Proposal** — why the change exists, scope, non-goals, impact;
- **Specs** — observable requirements and concrete scenarios;
- **Design** — architecture, interfaces, data flow, constraints, tradeoffs;
- **Tasks** — implementation slices derived from the settled design.

Keep acceptance evidence explicit.

For behavioral requirements, prefer concrete scenarios such as:

```text
WHEN <condition or action>
THEN <observable outcome>
```

Do not turn implementation guesses into requirements.

## Work autonomously

Once the input decisions are sufficient:

- inspect relevant repository files before specifying their replacement;
- research current APIs, libraries, constraints, and external facts when needed;
- reconcile the spec against the actual codebase;
- identify migrations, compatibility concerns, tests, rollout constraints, and failure states;
- eliminate contradictions between artifacts;
- keep scope aligned with the Plan Mode handoff.

Do not repeatedly ask the user to approve routine specification details that are derivable from settled decisions and project facts.

## Preserve the decision boundary

Use this rule:

```text
retrievable fact → retrieve it
implementation detail inside settled behavior → specify it
material product/scope decision → return to Plan Mode
```

If new evidence changes the implementation route without changing intent, update the design coherently.

If new evidence changes the intended behavior, scope, or user-visible contract, stop that branch and request a planning decision instead of silently rewriting intent.

## Definition of ready

The specification is implementation-ready when:

- scope and non-goals are explicit;
- requirements are observable and non-contradictory;
- important edge cases and failure behavior are covered;
- architecture and interfaces are clear enough to implement;
- tasks are derived from the design rather than invented independently;
- acceptance criteria are testable;
- repository facts used by the spec match the current project;
- unresolved product decisions are empty or explicitly deferred;
- Dev Mode can start without reconstructing intent from chat history.

Before declaring completion, perform a coherence pass across all artifacts.

## Durable state

Spec Mode may span multiple WebUI turns.

Keep the canonical spec in the target project's existing source of truth whenever writes are authorized.

A continuation checkpoint must preserve:

- target project/repository;
- specification/change identifier;
- artifacts completed;
- artifacts still incomplete;
- evidence/research already gathered;
- unresolved blockers;
- exact next operation.

Do not create a parallel shadow spec merely to checkpoint progress.

## Tool-budget continuity

ChatGPT WebUI may hard-stop a tool-heavy assistant turn.

Observed on 2026-09-18: a GitHub-connector-heavy turn stopped at exactly **64 connector calls** before a normal assistant final reply.

Treat 64 as an observed GitHub connector boundary, not a universal guarantee.

For GitHub-heavy Spec Mode turns:

- 1–48 connector calls: normal;
- 49–54: keep durable state current;
- around 56: preferred voluntary checkpoint;
- 57–60: finish only useful atomic work or secure state;
- 61–63: close out and checkpoint;
- 64: do not intentionally reach it.

For other tools or future WebUI behavior, adapt conservatively.

At the voluntary stop:

1. save the canonical work first;
2. record the exact unfinished operation;
3. end with:

```text
╭─ TOOL BUDGET ──────────────╮
│ 🟡 checkpoint saved        │
│ → send: continue           │
╰─────────────────────────────╯
```

When the user sends `continue`, resume the exact unfinished operation. Do not restart repository discovery, reread everything indiscriminately, or regenerate completed artifacts.

## Fresh-session recovery

When invoked as:

```text
continue spec on <repo>
```

first reload this skill.

Then recover:

1. the target repository and current branch/change state;
2. the existing spec/OpenSpec artifacts;
3. the latest durable checkpoint or Plan Mode handoff;
4. completed versus unfinished specification work;
5. the exact next operation.

Resume from there.

Do not ask the user to restate information that exists in the repository or durable artifacts.

## Completion

When ready, report compactly:

- specification/change identifier;
- canonical artifact locations;
- important deferred items, if any;
- evidence that the spec is coherent;
- the correct next stage: Dev Mode for standalone specs, or the OpenSpec workflow's native implementation step for OpenSpec changes.

Do not start implementation merely because the specification is complete.
