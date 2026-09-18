# GPT WebUI Skills

A tiny set of workflow skills for doing substantial project work in **ChatGPT WebUI**.

These skills are intentionally WebUI-specific. They account for conversational planning, connector-based repository work, per-turn tool limits, checkpoints, `continue`, and fresh-session recovery.

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
```

## Skills

| Skill | Purpose | Style |
| --- | --- | --- |
| [Plan Mode](./plan-mode/SKILL.md) | Turn a fuzzy idea into settled decisions | Interactive, 2–3 independent decision threads per round |
| [Spec Mode](./spec-mode/SKILL.md) | Turn settled decisions into an implementation-ready specification | Autonomous, continuation-driven |
| [Dev Mode](./dev-mode/SKILL.md) | Implement and verify the specification | Autonomous, continuation-driven |

## Install

### ChatGPT Web / Desktop

1. Open **Settings → Personalization → Custom Instructions**.
2. Make sure customization is enabled.
3. Add this instruction:

```text
For substantial project work in ChatGPT WebUI, load and follow the appropriate skill from https://github.com/AVANT-ICONIC/gpt-webui-skills before proceeding. Use plan-mode for planning and uncertain changes, spec-mode for turning settled decisions into an implementation-ready specification, and dev-mode for implementation. If I say "continue", resume the active skill from its latest durable checkpoint without restarting discovery. If I say "continue plan/spec/dev on <project or repo>" in a fresh chat, reload that skill and recover durable state first.
```

If you previously used longer WebUI workflow instructions in Custom Instructions, replace them with the block above. The repository is the canonical source; Custom Instructions only need to route ChatGPT to the correct skill.

For repository work, connect GitHub or another source that lets ChatGPT inspect the actual project instead of asking you to manually relay facts it can retrieve.

### Verify installation

Start a new chat and try one of:

```text
plan a new project
spec this project
dev this repo
```

ChatGPT should load the matching `SKILL.md` before doing substantial work.

## Usage

### Plan

```text
plan <idea / project / feature>
```

Plan Mode is the human-in-the-loop stage. It asks small rounds of independent questions, recommends answers, retrieves facts itself, and keeps unresolved dependencies out of the current round.

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

For a fresh chat, use an explicit recovery command:

```text
continue plan on <project>
continue spec on <repo>
continue dev on <repo>
```

The skill should recover durable state first, then continue from the frontier.

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
