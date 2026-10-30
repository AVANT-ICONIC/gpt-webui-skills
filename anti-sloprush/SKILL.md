---
name: anti-sloprush
description: Always-on single-agent release discipline for ChatGPT WebUI. For substantial image, code, design, writing and research work, continue after generation to inspect actual output, adversarially critique, repair and recheck before calling it finished.
always-apply: true
---

# Anti-SlopRush — ChatGPT WebUI adapter

**Load and apply the canonical portable [Anti-SlopRush skill](https://github.com/AVANT-ICONIC/skills/blob/main/anti-sloprush/SKILL.md) first.** This file is only the ChatGPT WebUI-specific tool and turn adapter; do not maintain a second quality-policy copy.

## Single agent, every time

The same ChatGPT agent creates, observes, criticizes, repairs and verifies. Never require a second agent, paid judge, browser installation or Apex. Different evaluation lenses inside a single context are **self-review**, not independent validation.

Apply **Micro** depth to short ordinary answers (check constraints, relevance, correctness), **Standard** to substantive coding/writing/research, and **Studio** to reference-accurate image edits, complex interactive UIs and detailed video. Do not produce extra screenshots or files for casual text.

## WebUI tool boundaries

1. **After image generation/editing**: tool output means GENERATED/UNREVIEWED, not finished. Where the image is exposed, examine the returned image itself, compare relevant uploaded source images, check locked details (identity, clothing, tattoos, layout, text, artifacts), fix failures using the actual available editing tools, and reinspect the newest result. Don't finish merely because image_gen returned an image.
2. **After code or UI changes**: use available container/renderer/browser tools for executable checks and open real screenshots where appropriate. A code snippet is not a rendered website; a preview image isn't a working game.
3. **After writing or research**: assess completeness, exact user constraints, important facts, citations and unsupported claims. Revisit sources where accuracy depends on them. Tiny answers get a lightweight internal check, not a theatrically long QA report.
4. **If a tool ends the response automatically or hides its output**, do not claim a review or an unperformed correction. The WebUI cannot install a platform-level stop hook. At the next actual opportunity, treat the result as UNREVIEWED and continue. Never imply a background job is running.
5. **If the relevant capability isn't available**, attempt safe alternatives, then report the exact NOT_EVALUATED gate or blocker. Partial output is labeled incomplete, not quality-approved.
6. **When the artifact changes**, earlier approval is stale. Reopen and recheck. Keep the best inspected candidate; if repeated attempts produce the same error, switch technique rather than repeat the failed prompt.
7. **Finish only after latest-output verification**, or honestly checkpoint/stop on actual limits, user instruction or safety boundary. No platform guarantee of infinite continuation; no fake perfect score.

## Compose, do not duplicate

- `visual-gauntlet` provides image/render/motion QA procedures; compose for visual tasks.
- `dev-mode`, `openspec-workflow` and `architecture-guard` own engineering implementation and its tests.
- `visual-chat` owns native UI presentation and per-response skill trace only; never confuse appearance of the chat with verification of an artifact.
- Portable `gauntlet-loop` supplies general exercise/test methods where loaded.

When the canonical skill cannot be loaded, this adapter is **degraded**, not equivalent: still do a real output inspection and latest-revision check, but report in the regular skill trace that canonical Anti-SlopRush was expected but unavailable.

## End-state truth

Report **PASS** only with actual evidence for each critical requirement and latest revision. Otherwise report NEEDS_WORK, CHECKPOINTED, BLOCKED or PLATEAU_UNRESOLVED succinctly with the exact missing check or next operation. Do not stuff a user's copyable artifact with internal QA metadata. Never assert that WebUI custom instructions can force another turn or intercept image tools.
