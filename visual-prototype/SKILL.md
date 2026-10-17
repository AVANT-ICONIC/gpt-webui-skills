---
name: visual-prototype
description: Visual design-anchor gate for visually led games, consumer apps, websites and interfaces around specification authoring. Generate or select one cohesive reference, approve it, and bind specs and visual QA to it; avoid variant spam.
---

# Visual Prototype: approve the picture before building the product

This is a **conditional design companion**, not a universal image-generation requirement. Use it for a visually led game, consumer application, interface, marketing-led interactive product or redesign when visual direction materially changes implementation. Pair with Plan Mode, Spec Mode or native OpenSpec Explore/Propose as appropriate, and Visual Gauntlet during implementation verification.

Do **not** trigger for nonvisual/backend tasks, ordinary bug fixes, already locked references, or when the user explicitly requests text/code only. Never invent an image task where no image output is authorized. If a relevant visual reference already exists, inspect and reuse it instead of generating another.

## Placement in the workflow

```text
intent / project planning / gameplay or UX decisions
        ↓
VISUAL PROTOTYPE GATE, only for visually led projects
  one integrated concept board → inspect → owner selects / approves
        ↓
specification / native OpenSpec change design
  reference locked image, visual contract and behavioral constraints
        ↓
implementation → actual rendered inspection via visual-gauntlet
```

If a draft spec is necessary to make the visual honest, draft only the needed mechanics and screen inventory first, then complete the visual gate **immediately after that exploratory draft and before implementation**. In an OpenSpec project, keep the result in the project's native Explore/Propose artifacts, not a parallel shadow GDD.

## One-shot-first method

1. **Ground the brief.** Recover locked player actions, core loop, camera/orientation, key screens, design constraints, known brand system, and prohibited or deferred features. Distinguish a game mechanic from a thematic illustration.
2. **Choose one anchor artifact.** By default create **one cohesive, integrated game/app prototype board** showing a hero gameplay/product screen, core interaction, major UI states, 1–3 supporting screens or variants, and consistent color/material/lighting/type rules. A well-organized multi-panel board is explicitly encouraged when it gives the builder useful context. Prioritize the first result instead of preplanning a pile of variants.
3. **Inspect the returned image itself.** Check that it represents the agreed game/app rather than merely looking pretty: camera, screen ratio, inputs, HUD, primary mechanic, interaction states, UI legibility, coherent motifs, and absent invented economy/content. Rendered text and icon details are illustrative until specified precisely.
4. **Approval is the stop signal.** If the owner likes a reference, mark it **APPROVED / IMMUTABLE BASELINE** and stop generating. Do not continue on autopilot to images 2–6. Produce a targeted edit or alternative only for a *specific* defect, meaningful divergent direction, or explicit owner request. Never overwrite the approved baseline.
5. **Bind image to specification.** Preserve the exact approved asset/reference in the project's accessible design source of truth when authorized; record its revision/path, a succinct visual contract (palette, materials, layout, typography, lighting, interaction hierarchy, component/asset vocabulary), and the mechanics the reference is allowed to depict. A prompt, prose description or later unapproved image is not a substitute for the actual reference. If asset persistence is unavailable, report the gap instead of claiming a durable reference.
6. **Implement against reference.** Add visual fidelity acceptance criteria to the actual specification. Use Visual Gauntlet to compare running screens, responsive sizes and interaction states against the approved anchor. Concept art is not an executable UI or proof of feasibility; accurate gameplay rules always outrank an image hallucination.

## Guards against agent slop

- **Consistency over quantity.** Reuse one chosen identity across gameplay, menu, tournament, upgrades and content screens. Multiple independent image generations often drift into unrelated art directions.
- **Never inherit invented features.** An arcade-styled screenshot may depict ticket shops, cabinets, or currency. These are art motifs, **not scope authorization**. Features enter the GDD only through settled product decisions.
- **Visible behavior matters.** A beautiful hero art scene without a plausible control surface, level camera or screen state fails as a prototype reference.
- **One authoritative selection.** Explicitly record accepted versus rejected concepts; later generations cannot silently replace the chosen one.
- **No forced image production.** Respect user-selected medium and current tool/image authorization. Existing brand assets, user screenshots, sketches or reference decks may satisfy the gate; choose image generation only when a new rendered image is desired.
- **No infinite prompt treadmill.** Once the baseline is approved, specify and build; revisit visuals only for a diagnosed mismatch or material design change.

## Handoff contract

A visually led spec should carry:

- `anchor_status`: `APPROVED` | `PENDING` | `NOT_APPLICABLE` | `BLOCKED`;
- `anchor_ref`: verified path, asset, or source ID for the selected image, not a guessed URL;
- `approved_direction`: 2–5 sentences of the visual identity;
- `must_match`: actionable screen geometry, style, component/asset language, and readability priorities;
- `must_not_infer`: hallucinated UI/features seen only in the image;
- `acceptance`: the real rendered screens/states and device sizes to inspect later.

If a specific visual project has a selected anchor but the exact file cannot yet be persisted, keep that limitation explicit and do not claim the visual gate has a durable machine-accessible handoff.

## BANKSHOT lesson

BANKSHOT: ROGUE CUP established the useful pattern: the **first cohesive Toy Arcade concept sheet was approved**. Later sheets drifted toward ticket/prize shops and generic arcade machines, which were never approved mechanics. Keep the first image as the visual anchor for that project; do not merge later designs into the spec or create more variants unless requested. Its physics roguelite rules and undecided monetization still govern functionality.

The point of the gate is not to require a concept gallery. It is to stop visual-agent improvisation **before** agents turn random art direction into product requirements.
