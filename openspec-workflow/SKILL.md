---
name: openspec-workflow
description: ChatGPT WebUI router for OpenSpec-first development. Use for non-trivial features, behavioral bug fixes, refactors, migrations, architecture changes, or implementation work in projects that use OpenSpec, and when the user says spec it, use OpenSpec, propose this change, or continue an OpenSpec change.
---

# OpenSpec Workflow

Treat OpenSpec as the live change workflow, not as a documentation export after ChatGPT has already finished planning somewhere else.

This skill routes work through the project's native OpenSpec lifecycle. It does not replace OpenSpec's generated skills, commands, schema, or project-specific rules.

## Core routing

For a project that already uses OpenSpec:

```text
request
  │
  ├─ messy underlying intent ─► Intent Mode, only if actually needed
  │
  └─ concrete code change
           │
           ├─ material uncertainty ─► OpenSpec Explore
           │
           └─ sufficiently clear ───► OpenSpec Propose
                                      ↓
                              agreed change contract
                                      ↓
                              OpenSpec Apply
                                      ↓
                           verification / project gates
                                      ↓
                                  Archive
```

OpenSpec is iterative rather than a rigid waterfall. Artifacts can be revised as evidence changes. The invariant is that implementation must not silently outrun or replace the agreed change contract.

## Activation boundary

Use this workflow for non-trivial coding work in an OpenSpec project, including:

- new features and capabilities;
- behavioral bugs where correct behavior needs definition;
- meaningful refactors;
- migrations or breaking changes;
- architecture, interface, or cross-module changes;
- work delegated to fresh-context agents;
- changes with meaningful scope, compatibility, acceptance, or failure-state ambiguity.

Do not force OpenSpec onto a truly mechanical edit with no meaningful product or architecture choice.

A useful test is:

```text
Can this change alter observable behavior, interfaces, architecture,
compatibility, migration state, or acceptance expectations?
  yes → OpenSpec
  no, purely mechanical → direct work may be appropriate
```

Explicit user requests to use OpenSpec always activate this skill.

## Inspect before routing

Before creating anything:

1. inspect the repository for an OpenSpec root, config, store declaration, existing changes/specs, and generated OpenSpec skills or commands;
2. inspect repository-specific contribution and quality rules;
3. identify whether a relevant existing change already covers the request;
4. prefer the project's native OpenSpec instructions over assumptions in this skill.

Current OpenSpec is schema-driven. Never assume every repository uses the same literal artifact graph.

If an existing change already covers the request, continue or update it. Do not create a replacement change because a new chat started.

## Do not initialize silently

If the repository does not already use OpenSpec and this skill was auto-selected, do not create `openspec/` or initialize OpenSpec as a side effect.

Adoption or initialization requires explicit user intent or an already-authorized project workflow.

When OpenSpec setup is explicitly requested, follow current official OpenSpec instructions rather than freezing installation folklore into this skill.

## Choose Explore vs Propose correctly

### Explore

Use the project's native OpenSpec Explore workflow when material uncertainty remains about:

- intended behavior;
- scope or non-goals;
- architecture with user-significant consequences;
- compatibility or migration;
- acceptance criteria;
- competing approaches that change the contract.

Explore may inspect code, tests, docs, and current specs. It is thinking and clarification, not implementation.

Do not duplicate change-specific OpenSpec exploration in Plan Mode merely because Plan Mode exists.

### Propose

Use the native OpenSpec Propose workflow when the change is clear enough to define.

Propose may still ask focused questions if ambiguity would materially change scope, behavior, compatibility, or acceptance.

Proposal/spec/design/task authoring is planning work. Do not edit product code during the same operation that is still establishing the contract.

## Relationship to the WebUI modes

### Intent Mode

Intent Mode is optional upstream help for genuinely messy brain dumps or hidden objectives.

Once the real objective is clear and the request is a concrete non-trivial code change in an OpenSpec project, route here. Do not force a separate Plan Mode pass unless broader project-level decisions remain.

### Plan Mode

Plan Mode is for higher-order decisions that span multiple OpenSpec changes, projects, product strategy, architecture programs, or workflows where the concrete change boundary is not yet known.

For one concrete OpenSpec change, prefer OpenSpec Explore over duplicating a separate planning interview.

### Spec Mode

Spec Mode is a compatibility entry point.

When the target project uses OpenSpec, Spec Mode must delegate the change lifecycle to this skill instead of waiting until all planning is finished and then exporting the result to OpenSpec.

For projects without a native specification system, Spec Mode may still build a coherent standalone specification.

### Dev Mode

When an OpenSpec project is implementing a non-trivial change, Dev Mode must implement from the identified OpenSpec change and respect the project's native Apply workflow.

If no suitable change exists yet, do not start ad-hoc implementation. Route back through Explore or Propose first.

## WebUI without the OpenSpec CLI

ChatGPT WebUI may have repository access without a local shell or OpenSpec CLI.

In that case:

- inspect the repository's existing `openspec/` configuration and generated OpenSpec skill/command instructions;
- preserve the project's schema and naming;
- use repository writes only when authorized;
- never invent generated metadata or a schema that cannot be verified;
- prefer updating canonical existing artifacts over creating parallel planning files.

If a safe next step genuinely requires the local OpenSpec CLI, terminal, or another unavailable local tool, hand off to a local coding agent with the exact repository, change identifier, completed work, and next native OpenSpec operation.

## Implement from the change

During Apply / Dev work:

- load the exact current change rather than reconstructing intent from chat history;
- implement coherent vertical behavior;
- keep task completion honest and evidence-backed;
- avoid helper-script chains when a direct code change is available;
- do not widen scope opportunistically;
- preserve repository-specific gates and authority boundaries.

If a new technical fact changes only the implementation route while preserving agreed behavior, update the design coherently.

If evidence changes intended behavior, scope, compatibility, or acceptance criteria, revise the OpenSpec change before continuing implementation.

## Incremental changes, not mega-specs

Do not turn a greenfield project into one giant frozen OpenSpec change covering the entire imagined future.

Prefer coherent increments:

```text
change A → implement → verify → archive
change B → implement → verify → archive
...
```

For brownfield repositories, specify the capabilities touched by the current change. Do not document the entire application before useful work can proceed.

## Avoid competing truth stores

Do not create `PLAN.md`, `SPEC.md`, handoff files, issue-body duplicates, or other shadow requirement stores merely to preserve the same information already held by the OpenSpec change.

Other systems may remain authoritative for issue identity, approvals, release gates, evidence, deployment, or organization-level policy. Respect those boundaries and link to them instead of copying them into a second truth store.

## Verification and archive

Before claiming implementation complete:

- compare implementation against observable requirements and scenarios;
- run or inspect the strongest available project verification;
- use the native OpenSpec Verify workflow when the installed profile provides it;
- obey repository-specific quality gates;
- state unavailable verification honestly.

Archive only when the change is actually complete. Do not use archive as a way to make unfinished work disappear into a nicer folder.

## Durable continuation

For multi-turn WebUI work, preserve:

- repository;
- OpenSpec root/store when relevant;
- exact change identifier;
- current artifact state;
- implementation tasks completed and remaining;
- verification already performed;
- blockers;
- exact next native workflow operation.

When the user sends `continue`, resume that operation. Do not restart discovery or create a fresh change.

## Completion

A completed OpenSpec workflow should leave:

- one coherent change, not several competing versions;
- implementation aligned to that change;
- verification evidence;
- repository-specific gates satisfied or explicit blockers recorded;
- archive completed when appropriate;
- no shadow spec created by WebUI.
