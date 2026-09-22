# GPT WebUI Skills

A growing set of WebUI-native skills for substantial and specialized work in **ChatGPT WebUI**.

These skills are intentionally WebUI-specific. They account for conversational planning, connector-based repository work, per-turn tool limits, durable checkpoints, `continue`, fresh-session recovery, and clean handoff to a local coding agent.

```text
idea
  ↓
PLAN MODE
  ↓
SPEC MODE
  ↓
DEV MODE
  ↓
done
  or
LOCAL HANDOFF → Codex / Claude Code / local agent
```

## Skills

| Skill | Purpose | Style |
| --- | --- | --- |
| [Plan Mode](./plan-mode/SKILL.md) | Turn a fuzzy idea into settled decisions | Interactive, 2–3 independent decision threads per round |
| [Spec Mode](./spec-mode/SKILL.md) | Turn settled decisions into an implementation-ready specification | Autonomous, continuation-driven |
| [Dev Mode](./dev-mode/SKILL.md) | Implement, verify, and optionally hand off to a local agent | Autonomous, continuation-driven |
| [Video Watch](./video-watch/SKILL.md) | Actually inspect video frames + captions in WebUI | Automatic, frame-aware |


## Visual-first skill convention

Every skill should make ChatGPT's **user-facing chat output visually dense and easy to scan**. New `SKILL.md` files should include the repository's visual chat guidance: semantic emoji/color circles, progress bars, ASCII/Unicode boxes and separators, trees/flows, compact dashboards, and other useful visual anchors.

```text
🟢 complete   ██████████ 100%
🟡 active     ██████░░░░  60%
🔴 blocked    ██░░░░░░░░  20%

╭─ CHECKPOINT ─────────────╮
│ 🔵 state                 │
│ 🟣 decision              │
│ 🟢 next action           │
╰──────────────────────────╯
```

Visuals should improve comprehension, not corrupt exact code, commands, specifications, file contents, or reusable artifacts.


## Install

### ChatGPT Web / Desktop

Open:

```text
Settings → Personalization → Custom Instructions
```

Remove any older custom-instruction block that describes PLAN MODE, SPEC MODE, DEV AUTOPILOT, `/AI-Operating-System/`, tool-budget checkpoints, or fresh-session recovery.

Replace that whole workflow block with:

```text
Before substantial or specialized work, check https://github.com/AVANT-ICONIC/gpt-webui-skills for a matching skill. If one exists, load its current SKILL.md and follow it. Treat that repository as canonical and discover available skills from it rather than relying on a hard-coded list.

If I say "continue", resume the active skill from its latest durable checkpoint without restarting discovery. In a fresh chat, recover the matching skill and durable project state first.

If work must continue on my local machine or with another coding agent, follow the active skill's handoff instructions and preserve settled context.
```

Keep unrelated personal preferences and non-workflow Custom Instructions unchanged.

The repository is the canonical source. Custom Instructions should only route ChatGPT to the current skills instead of duplicating their behavior.

For repository work, connect GitHub or another source that lets ChatGPT inspect the actual project rather than asking you to manually relay facts it can retrieve.

### Verify installation

Start a new chat and try:

```text
plan a new project
spec this project
dev this repo
watch https://youtu.be/VIDEO_ID
```

ChatGPT should load the matching `SKILL.md` before substantial work.

## Usage

### Plan

```text
plan <idea / project / feature>
```

Plan Mode is the human-in-the-loop stage. It asks compact rounds of independent questions, recommends answers, retrieves facts itself, and keeps dependent decisions out of the current round.

### Spec

```text
spec <project / repo / settled plan>
```

Spec Mode consumes settled planning decisions and builds the specification autonomously. It prefers an existing OpenSpec setup when one is present and follows that project's schema. Otherwise it can produce the default OpenSpec-style `proposal → specs → design → tasks` shape.

### Dev

```text
dev <repo / specification>
```

Dev Mode implements the agreed specification, verifies the result, and keeps product decisions separate from execution.

### Video Watch

```text
watch <video URL / uploaded video> [question]
```

Video Watch resolves the actual video, extracts scene-change + timeline-coverage + dense opening frames, packs them into timestamped contact sheets, and has ChatGPT inspect those images alongside available captions.

It is intentionally WebUI-specific: contact sheets reduce dozens of visual frames to a small number of image-tool calls, while focused `--start` / `--end` passes allow closer inspection of important ranges.
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

Spec Mode uses [OpenSpec](https://github.com/Fission-AI/OpenSpec) as the preferred specification system when the target project already uses it.

Current OpenSpec workflows are schema-driven. The familiar `proposal → specs → design → tasks` flow is the default, not a format that should be blindly hard-coded over an existing project schema.

## Planning model

Plan Mode is inspired by the useful separation in [Matt Pocock's skills](https://github.com/mattpocock/skills) between:

- **grilling**: resolve the current decision frontier with the human;
- **wayfinding**: keep a map when the route is too large or uncertain to hold cleanly in one session.

This repository combines those ideas into one WebUI-native planning stage rather than requiring the user to choose between separate planning tools.

---

Built for ChatGPT WebUI. Small on purpose.
