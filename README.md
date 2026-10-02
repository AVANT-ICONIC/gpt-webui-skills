# GPT WebUI Skills

A growing set of WebUI-native skills for substantial and specialized work in **ChatGPT WebUI**.

These skills are intentionally WebUI-specific. They account for conversational planning, connector-based repository work, per-turn tool limits, durable checkpoints, `continue`, fresh-session recovery, and clean handoff to a local coding agent.

```text
idea / brain dump
  ↓
INTENT MODE, only when needed
  ↓
PLAN MODE, for project-level decisions
  ↓
concrete non-trivial code change
  ↓
OPENSPEC WORKFLOW
Explore → Propose → Apply → Verify/quality gates → Archive
  ↓
done

Projects without a native OpenSpec workflow may use SPEC MODE → DEV MODE.
LOCAL HANDOFF remains available when execution must continue elsewhere.
```

## Skills

| Skill | Purpose | Style |
| --- | --- | --- |
| [Intent Mode](./intent-mode/SKILL.md) | Reconstruct the real objective from messy or ambiguous input | Context-rich, gap-seeking, minimal interview |
| [Plan Mode](./plan-mode/SKILL.md) | Settle project-level or multi-change decisions without duplicating OpenSpec change exploration | Interactive, 2–3 independent decision threads per round |
| [OpenSpec Workflow](./openspec-workflow/SKILL.md) | Route non-trivial OpenSpec code changes through native Explore → Propose → Apply → verify/archive | OpenSpec-first, change-scoped |
| [Spec Mode](./spec-mode/SKILL.md) | Build standalone specs when no native change workflow owns the work; delegates OpenSpec projects | Autonomous, continuation-driven |
| [Dev Mode](./dev-mode/SKILL.md) | Implement, verify, and optionally hand off to a local agent | Autonomous, continuation-driven |
| [Video Watch](./video-watch/SKILL.md) | Actually inspect video frames + captions in WebUI | Automatic, frame-aware |
| [SEO + AI SEO](./seo-aiseo/SKILL.md) | Audit and optimize sites for classic search + AI citations/mentions | Research-led, evidence-tiered |
| [Visual Chat](./visual-chat/SKILL.md) | Shared presentation companion loaded alongside substantial task skills | Always apply |


## Skill composition

Skills can be **task skills** or **cross-cutting companion skills**.

```text
task skill       = what to do
companion skill  = shared behavior that applies across tasks
```

`visual-chat` is the first companion skill. It owns user-facing chat presentation for substantial work and is marked `always-apply: true`.

Shared behavior should live in one companion skill rather than being copied into every task skill. New skills should not duplicate visual presentation rules from `visual-chat`.

A task skill must remain semantically complete without relying on visual formatting. Companion skills may change presentation, workflow hygiene, or other cross-cutting behavior, but must not silently change the task's domain rules.


## Install

### ChatGPT Web / Desktop

Open:

```text
Settings → Personalization → Custom Instructions
```

Remove any older custom-instruction block that describes PLAN MODE, SPEC MODE, DEV AUTOPILOT, `/AI-Operating-System/`, tool-budget checkpoints, or fresh-session recovery.

Replace that whole workflow block with:

```text
Before substantial or specialized work, check https://github.com/AVANT-ICONIC/gpt-webui-skills for relevant skills. Load every applicable companion skill marked `always-apply: true`, then load the matching task skill(s). Treat that repository as canonical and discover skills from it rather than relying on a hard-coded list.

If I say "continue", resume the active skill set from its latest durable checkpoint without restarting discovery. In a fresh chat, recover the matching skills and durable project state first.

If work must continue on my local machine or with another coding agent, follow the active task skill's handoff instructions and preserve settled context.
```

Keep unrelated personal preferences and non-workflow Custom Instructions unchanged.

The repository is the canonical source. Custom Instructions should only route ChatGPT to the current skills instead of duplicating their behavior.

For repository work, connect GitHub or another source that lets ChatGPT inspect the actual project rather than asking you to manually relay facts it can retrieve.

### Verify installation

Start a new chat and try:

```text
intent reconstruct this brain dump
plan a new project
use OpenSpec for this feature
spec this project
dev this repo
watch https://youtu.be/VIDEO_ID
seo audit https://example.com
```

ChatGPT should load the matching `SKILL.md` before substantial work.

## Usage

### Intent

```text
intent <brain dump / fuzzy request / project idea>
```

Intent Mode reconstructs the underlying objective, separates outcome from proposed solution, surfaces assumptions and contradictions, defines observable success criteria, and routes concrete non-trivial code changes in OpenSpec projects into OpenSpec Workflow once the actual intent is clear.

### Plan

```text
plan <idea / project / feature>
```

Plan Mode is the human-in-the-loop stage for decisions above one concrete change: product direction, architecture programs, multi-change sequencing, and similar project-level choices. A concrete change in an OpenSpec project should move into OpenSpec Workflow instead of completing a second parallel planning interview.

### OpenSpec Workflow

```text
use OpenSpec for <feature / bug / refactor / migration>
spec it with OpenSpec
continue the existing OpenSpec change
```

For a project that already uses OpenSpec, this is the default workflow for non-trivial code changes. It inspects the project's existing OpenSpec root and native skills, routes uncertainty to Explore, clear work to Propose, implementation to Apply, and completion through verification/project gates before archive. It does not duplicate OpenSpec's official skill bodies or silently initialize OpenSpec in projects that do not use it.

### Spec

```text
spec <project / repo / settled plan>
```

Spec Mode is now primarily for standalone specification work when no native change workflow owns the task. If the target repository already uses OpenSpec, Spec Mode delegates to OpenSpec Workflow early instead of waiting until all planning is finished and exporting it afterward.

### Dev

```text
dev <repo / specification>
```

Dev Mode implements the agreed specification and verifies the result. In an OpenSpec project it must identify the exact current change and execute through OpenSpec Workflow / native Apply semantics rather than starting ad-hoc code from chat memory.

### Video Watch

```text
watch <video URL / uploaded video> [question]
```

Video Watch resolves the actual video, extracts scene-change + timeline-coverage + dense opening frames, packs them into timestamped contact sheets, and has ChatGPT inspect those images alongside available captions.

It is intentionally WebUI-specific: contact sheets reduce dozens of visual frames to a small number of image-tool calls, while focused `--start` / `--end` passes allow closer inspection of important ranges.
### SEO + AI SEO

```text
seo audit https://example.com
ai seo audit https://example.com
optimize https://example.com/service for SEO + AI search
```

SEO + AI SEO performs a research-fresh audit across crawl/indexing, technical SEO, search intent, content quality, entity/local authority, AI crawler access, citation/mention opportunities, and measurement. It separates official platform guidance from observational studies and experiments instead of treating every GEO theory as fact.

### Local handoff

Use:

```text
handoff to codex
handoff to claude code
handoff to local agent
```

or let Dev Mode trigger the phase when work requires local-only access that WebUI cannot perform reliably.

The handoff is not a fourth skill. It is the final optional phase of Dev Mode.

It produces a continuation packet containing:

- repository and branch/PR state;
- canonical spec/OpenSpec change;
- completed work;
- exact unfinished work;
- relevant files and constraints;
- verification already performed;
- known blockers;
- exact next action;
- definition of done;
- an explicit instruction not to restart discovery or reinterpret settled product decisions.

Prefer existing durable project artifacts as the source of truth. Do not create a new handoff file merely for ceremony. If no durable project artifact can carry the state, output a self-contained copy/paste handoff prompt for the local agent.

## Continue

Long tool-heavy work may span multiple assistant turns.

When a mode reaches its safe per-turn checkpoint, it saves durable state and ends with:

```text
╭─ TOOL BUDGET ──────────────╮
│ 🟡 checkpoint saved        │
│ → send: continue           │
╰─────────────────────────────╯
```

Send:

```text
continue
```

The next turn resumes the exact unfinished operation. It must not restart discovery or re-ask settled questions.

For a fresh chat, use:

```text
continue plan on <project>
continue spec on <repo>
continue dev on <repo>
```

The skill recovers durable state first, then continues from the frontier.

## WebUI tool budget

The current tuning is empirical, not a platform guarantee.

A reconstructed ChatGPT WebUI turn on 2026-09-18 reached exactly **64 GitHub connector calls** and then hard-stopped before a normal assistant reply.

For GitHub-heavy turns these skills therefore treat roughly **56 connector calls** as the preferred voluntary checkpoint, leaving room to save state and finish an atomic operation.

Different tools or future WebUI versions may have different limits. The skills must prefer recoverability over deliberately testing the ceiling.

## OpenSpec

[OpenSpec](https://github.com/Fission-AI/OpenSpec) is treated as a live change workflow for repositories that use it, not merely as the output format of Spec Mode.

The WebUI router follows the project's native OpenSpec setup and official generated skills. Material uncertainty belongs in Explore; sufficiently clear changes go to Propose; implementation proceeds from the agreed change; verification and project-specific quality gates precede archive.

Current OpenSpec workflows are schema-driven and iterative. The familiar `proposal → specs → design → tasks` graph is common, not a format that should be blindly hard-coded over an existing project schema. OpenSpec should also stay change-scoped: do not create giant whole-application specs when focused incremental changes are the useful unit.

## Planning model

Plan Mode is inspired by the useful separation in [Matt Pocock's skills](https://github.com/mattpocock/skills) between:

- **grilling**: resolve the current decision frontier with the human;
- **wayfinding**: keep a map when the route is too large or uncertain to hold cleanly in one session.

This repository combines those ideas into one WebUI-native planning stage rather than requiring the user to choose between separate planning tools.

## Contributing

Contributions are welcome when they keep the repository focused and WebUI-native. See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT. See [LICENSE](./LICENSE).

---

Built for ChatGPT WebUI. Small on purpose.
