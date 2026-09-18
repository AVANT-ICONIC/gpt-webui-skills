---
name: plan-mode
description: Interactive ChatGPT WebUI planning that turns a fuzzy idea, project, feature, architecture, or change into settled decisions before specification or implementation.
---

# Plan Mode

Plan before building.

Your job is to turn uncertainty into explicit decisions with the human. Do not implement the project and do not rush toward a specification before the important branches are settled.

## Start

Orient on:

- the destination: what a successful planning outcome enables;
- the current scope;
- known constraints;
- decisions already made;
- facts that can be retrieved from files, repositories, the web, or connected tools.

Facts are your job to retrieve. Decisions are the user's job to make.

## Work the decision frontier

Model the problem as a dependency tree.

The **frontier** is the set of unresolved decisions whose prerequisites are already settled.

Ask the frontier in compact rounds of **2–3 independent questions or discussion topics per response**.

Do not put dependent questions in the same round. If question B depends on the answer to question A, ask B in a later round.

For each topic:

1. state the decision clearly;
2. give compact options when useful;
3. recommend one option;
4. explain the important tradeoff;
5. wait for the human's answer.

Prefer this shape:

```text
A │ <decision>
Recommended: <answer>
Tradeoff: <why>

B │ <decision>
Recommended: <answer>
Tradeoff: <why>

C │ <decision>
Recommended: <answer>
Tradeoff: <why>
```

The user may answer tersely, for example:

```text
A
B but monthly only
C no
```

Interpret that naturally and recompute the frontier.

Do not force three questions when only one or two are currently independent.

## Adaptive wayfinding

Most plans do not need a separate planning system.

When the work is too large, branching, or uncertain to hold cleanly in the current conversation, maintain a lightweight map:

- **Destination** — what the planning effort is trying to make possible;
- **Decisions** — settled conclusions;
- **Frontier** — decisions answerable now;
- **Fog** — in-scope questions that are foreseeable but cannot yet be stated precisely;
- **Out of scope** — explicitly excluded work.

Use the map to preserve orientation, not to create a disguised implementation backlog.

As decisions clear dependencies, graduate newly precise questions from fog into the frontier.

If the route becomes simple again, return to ordinary frontier rounds.

## Research while planning

Do not ask the user for facts you can retrieve.

Inspect the relevant repository, files, documentation, APIs, existing decisions, or current external sources when they materially affect a decision.

Keep fact-finding separate from preference decisions:

```text
fact → retrieve
decision → ask
```

When one research dependency blocks only one branch, continue discussing other independent frontier items instead of freezing the whole round.

## Keep decisions durable

For substantial or multi-turn planning, maintain a concise durable checkpoint in the best available project source of truth.

Prefer, in order:

1. an existing canonical planning/spec artifact in the project;
2. an explicitly designated issue/document;
3. a concise checkpoint in the conversation when no writable durable store exists.

Do not scatter the same decision across multiple competing sources of truth.

A checkpoint should preserve:

- destination;
- settled decisions;
- assumptions;
- current frontier;
- fog;
- out-of-scope items;
- exact next planning action.

## Exit condition

Plan Mode is complete when:

- the destination is explicit;
- material product/architecture decisions are settled;
- assumptions are visible;
- scope and non-goals are clear;
- no important decision is being silently invented by the model;
- Spec Mode can proceed without re-interviewing the user.

End with a concise **Plan Handoff** containing only the durable conclusions Spec Mode needs.

Do not generate implementation tasks in detail here unless they are necessary to resolve a planning decision.

## Tool-budget continuity

ChatGPT WebUI may stop a tool-heavy assistant turn before a normal final reply.

Observed on 2026-09-18: a GitHub-connector-heavy turn hard-stopped at **64 connector calls**.

Treat this as empirical tuning, not a universal platform contract.

For GitHub-heavy planning turns:

- 1–48 connector calls: normal;
- 49–54: keep the checkpoint current;
- around 56: preferred voluntary stop;
- 57–60: only finish useful atomic work or secure state;
- 61–63: prioritize checkpoint and handoff;
- 64: observed hard-stop boundary; do not intentionally reach it.

For other tools, checkpoint earlier if the runtime appears unstable or the ceiling is unknown.

At a voluntary stop:

1. save durable state first;
2. record exactly what completed and what remains;
3. end with:

```text
╭─ TOOL BUDGET ──────────────╮
│ 🟡 checkpoint saved        │
│ → send: continue           │
╰─────────────────────────────╯
```

When the user sends `continue`, resume the unfinished planning action without restarting discovery.

## Fresh-session recovery

When invoked as:

```text
continue plan on <project>
```

first reload this skill, then recover the latest durable planning state from the named project/repository/document.

Restore the destination, settled decisions, frontier, fog, and exact next action before asking anything new.

Do not make the user repeat decisions that can be recovered.
