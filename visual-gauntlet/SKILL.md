---
name: visual-gauntlet
description: Evidence-led visual QA for images, layouts, responsive UI, animation and interactions in ChatGPT WebUI. Activate for requested visual artifact creation, editing, faithful replication or visual inspection; never invent imagery for text-only work.
---

# Visual Gauntlet

**Inspect what actually exists.** A good-looking prompt, code diff, green test, screenshot filename or rendered-looking mock is not evidence that the delivered pixels, motion and controls are correct.

This WebUI companion specializes in *visible-output quality*. It does not replace a code/build workflow, document/PDF tools, the portable general-purpose Gauntlet, or presentation formatting. Use actual tools available **in this session**; never claim access to hidden tool internals or another person's desktop.

## Activate, but don't invent work

Use for user-requested new/edited images, interfaces, icons, reference replicas, diagrams with a rendered deliverable, slides, PDFs, illustrations, visible game scenes, motion or videos. Also use for **inspection-only** requests without forcing edits.

Do **not** generate a gratuitous illustration for a text-only concept, status report or research answer. If the user requested only source code and no renderer is accessible, inspect structure and label rendered fidelity **NOT_EVALUATED**, not PASS. Respect exact-file/JSON/code-only output requirements.

Skill discovery and invocation in ChatGPT are best-effort routing instructions, **not** automatic interception of image generation, platform screenshots, browser state or proprietary rendering tools.

## The single-agent operating loop

The same agent is responsible for BUILD/CODE → CHECK the **actual artifact** → FIX → CHECK again → POLISH → CHECK again. Repeat if a consequential defect remains, and rerun applicable checks after the last revision. A different critic is optional; self-review must be labeled as such.

1. **LOCK THE CONTRACT.** Record the user's exact reference, artifact revision, requested properties, hard requirements, forbidden changes and relevant states. For "exact" requests compare to **that** reference, not an invented moodboard. Unknown offscreen or unprovided states are unverified.
2. **PROBE CAPABILITIES.** Check which image inspection, image editing, full browser renderer, scripting, PDF export/page view, video/frames, file and connector tools really exist. Select an evidence route from [tool selection](./references/tool-selection.md). Attempt authorized recovery if a route fails.
3. **CAPTURE BASELINE.** Save or identify the current best-known artifact. Obtain real output at representative viewports/states, temporal positions and/or image references. **Open and look at captured images/frames**. Capturing a file is not inspection.
4. **DIAGNOSE THE LARGEST DEVIATIONS.** Compare geometry, text, color, gradients, layers, shadow/refraction, content and responsive framing against the locked contract. Verify temporal behavior and working interaction using [motion and interaction checks](./references/motion-interaction.md). Record specific observations, not "looks off".
5. **REPAIR, RECALIBRATE, REINSPECT.** Address critical/major defects first without rewriting unrelated content. Re-render the revised candidate in the same relevant conditions, inspect it, and regression-check earlier passed behavior. Keep or restore the best verified revision if a fix worsens it.
6. **POLISH AND GATE.** Audit finesse and coherence only after core behavior is correct. Aim for **three meaningful observed passes** on substantial visual builds unless already objectively exact or legitimately constrained; three blind prompts/screenshots are not passes. Continue beyond three while meaningful defects are fixable. Report the result using [evidence and reference comparison](./references/visual-evidence.md).

If testing cannot actually execute, use the precise status and [recovery / continuation](./references/recovery-handoff.md). Do not turn an environment blocker into a fabricated PASS.

## Reference and acceptance rules

- **Pixel-critical replication:** identify anchor positions, scale, spacing, typography, color/material and visible state. Compare side-by-side images at a common viewport and scale where possible; a subjective visual match is not a measured pixel-perfect equality. If a reference is only a still, animation fidelity remains **NOT_EVALUATED**.
- **Interactive layouts:** test representative wide and narrow viewports (include ~320px if applicable), clipping inside containers as well as document overflow, meaningful mouse/pointer action and keyboard/focus when relevant; a fake screenshot-only view does not count as functional UI.
- **Animation:** sample **across the full loop**, including near the loop boundary, plus transitions and user changes. A pleasing still cannot pass a broken cycle, discontinuity, timing, unexpected flashes or a motion reference mismatch.
- **Image edits:** use actual supported editing tools, inspect the returned image itself and preserve user-specified untouched regions; do not claim pixel-level backend control or an unseen iterative generation.
- **Slide/PDF/diagram:** inspect rendered pages at reading size, typography, layout and page breaks; source syntax alone is not visual proof.
- **Video:** where useful, compose with `video-watch` to inspect timestamped frames plus captions; sampling alone may not prove subtle motion or a seamless loop.
- **Security/privacy:** never upload sensitive private artifacts, screenshots, references or benchmark details to public repositories or third-party tools without authorization. Use synthetic public examples. No paid APIs, mandatory browser, system-level installs, elevated access or credential operations.

## Evidence in the answer or authorized private workspace

A concise report is enough for simple work. For significant work capture:

```text
Contract: reference/requirements and immutable inputs
Candidate: revision / artifact identifier
Tool route: real renderer/editor + any constraints or fallbacks
Passes: revision → actually inspected file/frame/state → defect → correction → recheck
Coverage: viewport sizes, interaction inputs/states, timestamps/loop boundaries
Verdict: PASS | NEEDS_WORK | PAUSED_RECOVERABLE | BLOCKED_ENV | BLOCKED_PERMISSION
Review: self-review (unless a genuinely independent reviewer ran)
Open limits: any NOT_EVALUATED critical requirement and exact next action
```

**PASS** requires every applicable *critical* requirement actually observed and met, and no known unresolved major/critical defect. Mark untested aspects **NOT_EVALUATED** within coverage; if such an aspect is critical, overall verdict cannot be PASS. Useful partial delivery may be marked NEEDS_WORK/BLOCKED, never misrepresented as verified. Details in [visual evidence](./references/visual-evidence.md).

## Compose with existing skills, do not duplicate them

- **`visual-chat`:** presentation and functional Continue button where available. It does **not** inspect images or drive quality gates.
- **`video-watch`:** supplies *actual viewed* timestamped frames/contact sheets for video; Visual Gauntlet judges reference fidelity, continuity and change results.
- **`dev-mode`:** owns repository implementation, tests, branch/PR checkpoints and agent handoff. Visual Gauntlet supplies rendered-output and interaction acceptance gates.
- **Portable `gauntlet-loop`:** optional general artifact QA foundation where installed/available. WebUI Visual Gauntlet is self-contained; it does not require that separate repository or any unmerged PR.

**Finish honestly:** verified result if evidenced; otherwise clearly bounded evidence, last best revision, blockers and the exact safe recovery step. Do not demand extra agents, fixed OS or a forced A/B test.
