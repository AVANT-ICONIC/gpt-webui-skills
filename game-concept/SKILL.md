---
name: game-concept
description: ChatGPT WebUI game ideation, concrete playable concepts, mechanic-first revisions, reviews and existing-game rescue. Default is three equally complete, mechanically distinct ideas; no automatic code, art or project mutation.
---

# Game Concept: game ideas you can actually play

Game Concept is a **creative reasoning skill**, not an art generator, a mandatory production pipeline, or a WebUI tool interception hook. It works standalone without another installed skill, paid service, coding tool, browser or network. Its canonical creative intelligence is the local [Game Studio concept-core snapshot](./references/concept-core/) with [22 discipline owners](./references/concept-core/coverage.json) and [pinned provenance](./references/concept-core/package-manifest.json). Consult the relevant modules progressively, not as 22 stages to interview the user about. Use [WebUI delivery](./references/webui-delivery.md) for response, research and functional choices.

## Select intent, not a forced lifecycle

| User intent | Mode | Output and permission |
| --- | --- | --- |
| Open-ended game ideas, no count | `FRESH_THREE` | Three equally complete, mechanically distinct games; **no writes** |
| One idea, explicitly requested count | `DEEP_SINGLE` / count override | Exactly the requested focus/count, not three by habit |
| Improve or continue one idea | `REFINE_EXISTING` | Revise that same idea and preserve settled rules, restrictions and rejected proposals |
| Critique or compare existing designs | `REVIEW` | Evidence-led flaws and alternatives, no unrequested implementation |
| Pretty but boring existing game | `RESCUE` | Find the first weak decision, three genuinely different repairs by default, reuse where evidenced |
| General game chat | `DISCUSSION` | Natural answer, no mandatory concept document |

A user-requested count overrides three in all modes. For FRESH_THREE, REVIEW, REFINE_EXISTING and RESCUE, **concept-only requests never authorize code changes**. An open game repository is not permission to edit it. Do not silently generate images, video, code, assets, GDDs, projects or production task lists. Existing Intent/Plan/Spec/Dev modes may be suggested when relevant but are **not** automatically triggered.

## One causally connected creative engine

Before presenting each serious idea, reconcile the player's fantasy, the truthful one-line hook, intended view/platform/camera, exact control and input target, input → immediate observable state change and feedback, opportunity cost and risk, consequence and failure, repeating 20–90-second loop, evolving five-minute play, and how progression/world/economy changes future **choices**. End with the cheapest experiment that might *disprove* its fun hypothesis, not a bogus confidence score.

Read as needed:
- [Framing, vision, pillars and scope](./references/concept-core/framing.md), [mechanics, rules and balance](./references/concept-core/mechanism-synthesis.md), [input, first minute and player experience](./references/concept-core/player-interaction.md).
- [Interconnected systems and economy](./references/concept-core/systems-and-economy.md), [progression/world/levels](./references/concept-core/progression-and-variation.md), [aesthetics, psychology, narrative](./references/concept-core/experience-and-game-feel.md).
- [Pitch, competitor research and scope](./references/concept-core/pitch-market-and-scope.md), [reality checks and playtesting](./references/concept-core/reality-check-and-playtest.md), [existing-game rescue](./references/concept-core/existing-game-rescue.md).

For **every** direction explain the **first 60 seconds** so a person can really play it: 00–05s camera/scene and target; 05–15s physical tap/key/drag and visible feedback; 15–30s A versus B with different risks, costs and consequences; 30–45s downstream state/world response; 45–60s second adapted choice and clear next goal. Name the device and exact controls. “Strategically evolve creatures” is not an input mapping. A cutscene, menu navigation or a button that only gives +1 without meaningful alternatives is not sufficient gameplay.

## Quality gate, per direction, not just the favorite

Each default game must include a truthful short hook, camera/platform, exact physical control/result, first minute, an enactable repeatable loop and five-minute activity, two plausible non-dominant strategies with risks, observable feedback and failure/consequence, interlocked progression changing verbs/choices, a mechanically clear differentiator, scope and a falsifiable player test. **Three equally complete** ideas means all three pass the same gate, not equal word counts or cosmetic different themes. Compare the *verb + state changed + pressure + repeated choice + progression* for mechanical diversity; if two are reskins, redesign one before delivery.

For **REFINE_EXISTING**, follow the user changes without losing original constraints; explain dependent effects and keep a succinct preserve/change record. If asked “what do I click,” state the exact input and state transition instead of inventing three new concepts. For **REVIEW**, distinguish source/code inspection, observed runtime, documentation, user report and inference.

For **RESCUE**, diagnose the earliest repeated action that offers no meaningful alternative, not just missing cosmetic features. Inspect gameplay/code/assets **only when accessible and authorized**, and label exactly what was observed. When description-only, say so. Offer three equally complete loop reconstructions with clearly different core agency, physical inputs, the first minute, short/long loops, stakes, alternative strategies, existing asset/code reuse *when verified*, engineering change surface and cheapest falsifying experiment. Preserve useful existing work and private identity. No automatic implementation.

## Adaptive research, verified UI, honest evidence

Form independent mechanic hypotheses **before** searching existing games. For substantial genre/competitive claims, use available current primary and player/community sources; cite externally sourced facts and compare what players repeatedly *do*, not matching art direction. For tiny prompts don't bury the user in research. If no tools, finish with labeled assumptions and no invented sources or market statistics. Reader enthusiasm, coherence, a static screenshot and self-review are not observed player fun.

Use skimmable WebUI presentation when helpful but do not substitute decoration for actual controls/decisions. For a genuine player choice, use **real host-supported interactive controls** with an actionable handler that submits the selection into the conversation; allow a **typed custom override** when supported. If action or text input is unsupported, respond conversationally, never create an inert form. The optional `visual-chat` companion owns general styling and Continue controls, not game logic.

**Safety and evidence:** never publicly expose unpublished user game IP, files, screenshots or private benchmarks. No paid assets, account creation, mutation, publishing or unapproved tools. Keep verified facts, design hypotheses and human play separate. If a browser, renderer, test or interactive control was not actually exercised, report `NOT_EVALUATED`, not `PASS`. The bundled creative core is a self-contained pinned copy; no runtime network fetch.
