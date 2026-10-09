---
name: geometric-design
description: Plan and inspect geometric logos, nested compositions, UI proportions, and source-backed audits in ChatGPT WebUI; probe actual runtime/renderer capabilities, distinguish exact from inferred φ, and produce verifiable handoffs rather than invented test passes.
---

# Geometric Design · WebUI

**EXPERIMENTAL ALPHA candidate; still draft/unmerged.** Supported technical workflow only. No independent blind recognition review or matched-agent creative-uplift proof (T3/T4 `NOT_EVALUATED`).

**Read [bundled canonical policy](references/geometry-policy.md) first.** This skill works with this folder alone. It never assumes the portable engine, a Node process, a browser or an image renderer is available in the ChatGPT session.

## Specialist routing

1. **Symbol construction / repair:** lock user geometry and reference; check connected foreground, counters and true source circle-vs-ellipse semantics. The current portable engine supports only a bounded inert SVG subset and white-painted, not transparent, counters.
2. **Composition:** preserve hierarchy and reading order, create genuinely different region-tree families unless exact reference fidelity is requested; name intentional φ/diagonal relationships rather than decorating with post-hoc golden overlays.
3. **Standalone source audit:** report actual source digest, field-linked metrics and declared constraints. A visual match to φ without source provenance is **inferred**, never established design intent. No automatic modification of approved artwork.
4. **Responsive UI tokens:** bounded ratio-based typography, spacing, modal sizes and touch targets; content at 320/390/768/1280/1920 and 200% text takes precedence over ratios; verify actual browser output if possible.
5. **Grammar and QA:** enforce split/align/focal/safe-zone/rhythm/vary rules and distinguish mathematical, pixel, accessibility and human-creative evidence. Owner-approved Spacing Option 0 preserves existing CSS. The composition contract now references the shipped rem-based `gap-card` token (~12.944px at root16; ~25.888px at root32); a declared model is not a measured browser layout.

## Capabilities and handoff

Probe tools and permissions **actually available**: source bytes/file hashes, Node.js 22+, optional installed free Inkscape/browser, screenshot inspection and repo access. Only report what really executed. Without a runnable engine, present scope/constraints and a concrete **local-agent handoff**, never a fabricated CLI log or visual PASS:

- Source file, revision/digest and relevant private-data boundaries.
- Frozen layout/logo reference, expected geometry, supported and unsupported features, exact proposed versus owner-approved changes.
- Portable skill install source: `AVANT-ICONIC/skills/geometric-design/` (a separate install, not implicitly available here).
- Command(s), input/output paths, renderer viewports/sizes and actual required verification evidence.
- Open blockers and exact next operation; no automatic source overwrite, release or merge.

A real imported PNG alone offers pixel-visible measurements but not exact original vector radii. Real screenshots and browser interaction are required for render/functional acceptance; independent human judgement is required for recognizability claims. Existing presentation and single-agent quality skills keep their own responsibilities. No paid API, autonomous background work or Universal Gauntlet integration.

The vendored shared policy is pinned by `sync-manifest.json`; run `node verify-sync.mjs` when Node 22+ exists. Actual canonical cross-repo comparison uses the manifest's immutable portable-source commit, never an unverified floating branch.
