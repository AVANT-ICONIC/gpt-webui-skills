---
name: intent-mode
description: ChatGPT WebUI intent reconstruction for messy brain dumps, fuzzy requests, ambiguous goals, and early-stage prompts before planning or specification.
---

# Intent Mode

Reconstruct what the human is actually trying to achieve before solving it.

Intent Mode exists for situations where the input is rich but messy, incomplete, contradictory, overly solution-shaped, or still hiding the real objective.

Do not reward messiness for its own sake. The value is richer context.

## Core principle

```text
brain dump
  ↓
reconstruct intent
  ↓
surface assumptions, contradictions, and gaps
  ↓
ask only material questions
  ↓
define outcome + success criteria
  ↓
stress-test the reconstructed intent
  ↓
handoff to Plan Mode, OpenSpec Workflow, or Spec Mode
```

Do not begin implementation in Intent Mode.

## Start from the whole signal

Use everything the user supplied, including:

- stated goal;
- frustrations and motivation;
- constraints;
- examples and references;
- previous attempts;
- rejected approaches;
- uncertainties;
- desired end state;
- accidental details that may reveal hidden requirements.

Separate:

```text
explicitly stated
inferred but likely
unknown / unresolved
contradictory
```

Do not silently convert an inference into a settled requirement.

## Reconstruct the intent

Produce a compact internal model of:

- **Underlying objective** — what outcome actually matters;
- **Why it matters** — the problem or friction being removed;
- **Target user or operator** — who experiences the result;
- **Constraints** — what must remain true;
- **Success criteria** — what observable evidence would mean this worked;
- **Non-goals** — what should not be optimized or built;
- **Assumptions** — beliefs currently filling missing information;
- **Contradictions** — supplied requirements that cannot all hold at once;
- **Open decisions** — choices that genuinely require the human.

Prefer reconstructing the user's goal over preserving the literal shape of their first proposed solution.

If the user says "build X" but the surrounding context strongly indicates that X is only one possible means to a broader outcome, preserve both:

```text
desired outcome
current proposed solution
```

Do not discard the proposed solution. Do not mistake it for the objective either.

## Ask only what changes the result

Do not interview for completeness theatre.

Ask a question only when the answer could materially change:

- scope;
- product behavior;
- architecture;
- risk;
- acceptance criteria;
- cost or effort;
- the choice between substantially different approaches.

Retrieve factual information yourself when tools can answer it.

Use:

```text
fact → retrieve
preference / intent → ask
```

When several questions are needed, ask a compact set of independent questions. Do not ask dependent questions in the same round.

If the user has already supplied enough information, ask nothing and continue.

## Challenge the reconstructed intent

Before handoff, run an adversarial pass.

Ask internally:

- What is the strongest alternative interpretation of the user's goal?
- Which assumption, if false, would change the project most?
- Are the success criteria measuring the real outcome or merely completion of the proposed solution?
- Is a stated constraint actually a preference?
- Is an apparent requirement inherited from a failed earlier approach?
- What would make the reconstructed brief produce the wrong thing despite sounding reasonable?

Surface only material findings.

Do not manufacture objections for symmetry.

## Durable Intent Brief

For substantial work, preserve a concise Intent Brief in the best available durable source of truth.

Prefer:

1. an existing project planning/spec artifact;
2. an explicitly designated issue or document;
3. the conversation when no writable durable store exists.

The brief should contain:

```text
Objective
Why
Users / actors
Constraints
Success criteria
Non-goals
Assumptions
Contradictions
Open decisions
Proposed solution, if one already exists
```

Do not create a new repository file merely for ceremony.

## Exit routing

Choose the next stage from the state of uncertainty.

### → Plan Mode

Use Plan Mode when material product, scope, architecture, workflow, or tradeoff decisions remain unresolved.

Intent Mode hands over:

- reconstructed objective;
- constraints;
- success criteria;
- assumptions;
- contradictions;
- open decisions.

Plan Mode must not restart intent discovery unless new evidence invalidates the brief.

### → OpenSpec Workflow

When the target is a concrete non-trivial code change in a project that already uses OpenSpec, hand the Intent Brief to `openspec-workflow`. Let that workflow choose native OpenSpec Explore vs Propose from the remaining change-specific uncertainty.

Do not force a separate Plan Mode and Spec Mode pass merely because those modes exist.

### → Spec Mode

Use Spec Mode directly when the intended behavior, scope, constraints, and important decisions are already settled **and** the target project does not have a native OpenSpec change workflow that should own the change.

Intent Mode hands the complete Intent Brief directly to Spec Mode.

### → Direct answer

For a small request that does not require planning or specification, answer it once the intent is clear.

Do not force every request through the full workflow.

## Boundary with Plan Mode

Intent Mode answers:

> What are we actually trying to accomplish?

Plan Mode answers:

> Which decisions must we make to accomplish it?

OpenSpec Workflow answers, for OpenSpec projects:

> Which native change step owns this now, and what must remain true through implementation?

Spec Mode answers, for standalone specification work:

> What exactly must remain true when we build it?

Dev Mode answers:

> How do we implement and verify it?

Do not duplicate Plan Mode's decision-tree work inside Intent Mode.

## Tool-budget continuity

ChatGPT WebUI may stop a connector-heavy turn before a normal reply.

Use the same conservative continuity rules as the other WebUI task skills:

- keep durable state current during tool-heavy work;
- prefer a voluntary checkpoint before the observed connector ceiling;
- save the Intent Brief before stopping;
- record the exact unanswered material question or next operation.

At a voluntary stop, end with:

```text
╭─ TOOL BUDGET ──────────────╮
│ 🟡 checkpoint saved        │
│ → send: continue           │
╰─────────────────────────────╯
```

When the user sends `continue`, resume from the saved Intent Brief. Do not reconstruct the entire conversation again.

## Fresh-session recovery

When invoked as:

```text
continue intent on <project>
```

reload this skill, recover the latest durable Intent Brief and project state, then continue from the exact unresolved frontier.

Do not ask the user to repeat information that can be recovered.

## Completion

Intent Mode is complete when:

- the underlying objective is explicit;
- the proposed solution is separated from the outcome when necessary;
- constraints and non-goals are visible;
- assumptions and contradictions are surfaced;
- success criteria are observable;
- only genuinely material decisions remain;
- the next stage can proceed without reinterpreting the user's original brain dump.
