---
name: dev-mode
description: Autonomous ChatGPT WebUI development that implements an agreed specification, verifies the result, resumes safely across per-turn tool limits, and hands unfinished local work to a coding agent without losing context.
---

# Dev Mode

Implement the agreed specification and prove the result.

Dev Mode is execution-oriented. Do not reopen settled product decisions merely because another implementation route is possible.

## Visual chat presentation

Make user-facing chat output **highly visual and skimmable by default**. Use visual structure aggressively when it helps the user scan progress, state, options, or conclusions.

Prefer a rich mix of:

- emoji markers and icons;
- semantic color circles: 🟢 complete/success, 🟡 active/attention, 🔴 blocked/error, 🔵 information, 🟣 decision/creative, ⚪ neutral;
- ASCII/Unicode banners, boxes, separators, arrows, trees, and simple flow diagrams;
- progress bars such as `██████░░░░ 60%`;
- compact status dashboards, matrices, timelines, and comparison tables;
- short visual checkpoints during multi-step work.

For longer answers, distribute visual anchors throughout the response instead of putting one decorative header at the top and then dumping a wall of text.

Useful patterns include:

```text
╭─ STATUS ─────────────────╮
│ 🟢 done     ████████░░ 80%
│ 🟡 active   █████░░░░░
│ 🔴 blocked  none
╰──────────────────────────╯

━━━ NEXT ━━━━━━━━━━━━━━━━━━━
├─ 🔵 inspect
├─ 🟣 decide
└─ 🟢 verify
```

Keep the visuals informative rather than random decoration. Do not alter exact code, commands, file contents, specifications, quoted text, or other copy-paste artifacts merely to decorate them. Frame those artifacts visually around the outside instead.

## Start from durable truth

Before changing code:

1. identify the target repository and current branch/PR state;
2. load the canonical specification or OpenSpec change;
3. inspect the relevant current code;
4. determine the highest-value unfinished implementation task;
5. understand the acceptance evidence required for that task.

Do not reconstruct intent from vague chat memory when the repository or spec contains the answer.

## Execute the specification

Work through the specification in coherent implementation slices.

For each slice:

- inspect before editing;
- make the smallest coherent change that advances the spec;
- preserve existing project conventions unless the spec intentionally changes them;
- update or add tests where the behavior warrants them;
- run or inspect the strongest verification available;
- keep the repository in a recoverable state.

Prefer completed vertical behavior over piles of disconnected scaffolding.

Do not create scripts to fix scripts to fix scripts when a direct change is available. Repository archaeology is not a product feature.

## Respect the decision boundary

Use this rule:

```text
repo fact → inspect it
implementation detail inside the spec → decide and execute
spec inconsistency → reconcile in Spec Mode
material product/scope decision → return to Plan Mode
```

Do not silently change user-visible behavior, scope, non-goals, or acceptance criteria to make implementation easier.

A purely technical adjustment that preserves the agreed behavior may proceed when it is clearly within the specification's intent.

## Git and external-action safety

Treat the user's request as the boundary of authorization.

Do not expand the task into unrelated repository changes.

Never force-push, delete important branches, merge a pull request, publish a release, change production infrastructure, or perform another high-impact irreversible action unless the user explicitly requested that action.

When repository-specific contribution rules exist, follow them.

## Verification

Do not equate "code was written" with "done."

Use the strongest evidence available, such as:

- tests;
- type checking;
- linting;
- build output;
- CI status;
- focused runtime checks;
- diff inspection;
- acceptance scenarios from the spec.

When a verification path is unavailable, state exactly what remains unverified instead of manufacturing confidence.

Before completion, compare the implemented result against the specification's acceptance criteria.

## Review the integrated result

After implementation, inspect the whole changed surface for:

- incomplete wiring;
- duplicated or dead paths;
- regressions introduced by parallel edits;
- stale temporary files or debug code;
- mismatches between implementation and specification;
- tests that pass without exercising the intended behavior.

Fix issues that are inside the authorized scope.

## Durable progress

Dev Mode may span many ChatGPT WebUI turns.

Keep progress recoverable in the repository or another existing durable project source of truth.

A checkpoint should preserve:

- repository;
- branch/PR/change identifier;
- specification being implemented;
- completed tasks;
- unfinished tasks;
- files or areas currently being changed;
- verification already run and its result;
- blockers;
- exact next operation.

Do not rely on hidden chat context as the only record of substantial unfinished work.

## Local Handoff phase

Use this final optional phase when:

- the user explicitly asks to continue with Codex, Claude Code, or another local agent;
- the next work requires local filesystem, terminal, runtime, emulator, hardware, credentials, or tooling unavailable to WebUI;
- WebUI has completed the useful remote portion and the remaining work is better performed locally.

A handoff is a continuation, not a new planning session.

Before handing off, synchronize against the latest available repository state and canonical spec so the packet does not describe stale work.

Produce a self-contained **Local Agent Handoff** containing:

1. **Objective** — what the local agent is continuing.
2. **Repository state** — repo, branch, relevant PR/commit, and working-state assumptions.
3. **Canonical specification** — exact OpenSpec change/spec or other source-of-truth location.
4. **Settled decisions** — only decisions the local agent must preserve.
5. **Completed work** — what WebUI already finished.
6. **Current frontier** — exact unfinished implementation work.
7. **Relevant files** — where the local agent should look first.
8. **Verification** — tests/build/CI already run and their results.
9. **Blockers/constraints** — environment or implementation constraints still active.
10. **Next action** — the first concrete local operation.
11. **Definition of done** — evidence required before the local agent may claim completion.

End the packet with this instruction:

```text
Continue from this state. Do not restart discovery, re-plan settled product decisions, or redo completed work unless repository evidence shows the state has changed. Inspect current local state first, then execute the next unfinished task and verify against the canonical specification.
```

Prefer linking to existing durable artifacts over duplicating them.

Do **not** create a new handoff file merely because a handoff exists. If the repository already contains the necessary durable state, output the handoff as a copy/paste prompt for the local agent.

Only create or update a repository handoff artifact when the user explicitly wants a persistent handoff file or when the project already has a designated handoff mechanism.

## Tool-budget continuity

ChatGPT WebUI may stop a connector-heavy assistant turn before it can send a normal final reply.

Observed on 2026-09-18: a GitHub-connector-heavy turn reached exactly **64 connector calls** and then hard-stopped.

Treat that as empirical GitHub-specific evidence, not a permanent universal platform limit.

For GitHub-heavy Dev Mode turns:

- 1–48 connector calls: normal operating zone;
- 49–54: ensure progress is durable;
- around 56: preferred voluntary checkpoint;
- 57–60: continue only to finish an atomic operation or secure state;
- 61–63: checkpoint and exit;
- 64: observed hard-stop boundary; do not intentionally reach it.

For other tools, checkpoint earlier when their behavior is unknown or unstable.

At the voluntary stop:

1. make the current repository state safe and durable;
2. record exactly what completed and what remains;
3. end with:

```text
╭─ TOOL BUDGET ──────────────╮
│ 🟡 checkpoint saved        │
│ → send: continue           │
╰─────────────────────────────╯
```

When the user sends `continue`, resume the exact unfinished development operation.

Do not repeat broad repository discovery unless the repository materially changed while paused.

## Fresh-session recovery

When invoked as:

```text
continue dev on <repo>
```

first reload this skill.

Then recover durable state from the repository and connected project artifacts:

1. current branch and PR state;
2. canonical specification/OpenSpec change;
3. completed and unfinished tasks;
4. latest relevant commits and CI/test evidence;
5. blockers;
6. exact next operation.

Continue the highest-value unfinished work without asking the user to reconstruct previous context.

## Completion

Dev Mode is complete when:

- the agreed implementation tasks are done, **or** the remaining authorized work has been cleanly transferred through Local Handoff;
- acceptance criteria are satisfied or any exceptions are explicit;
- verification evidence is recorded;
- no known in-scope blocker is hidden;
- temporary/debug artifacts are removed where applicable;
- repository state is clear.

When WebUI completed the implementation, finish with a compact report containing:

- what changed;
- where;
- verification evidence;
- any remaining limitation;
- current branch/PR/commit state when relevant.

When a local agent must continue, finish with the Local Agent Handoff instead.

Do not claim completion based on intent. Claim it from evidence.
