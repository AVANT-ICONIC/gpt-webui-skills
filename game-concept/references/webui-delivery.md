# WebUI-specific delivery and interaction adapter

This file adapts the immutable canonical Game Studio concept core to conversational ChatGPT WebUI. It does **not** fork game-design knowledge or require a browser/API key. This skill remains independently installable. A presentation companion may format responses but cannot change creative constraints.

## Response modes and controls

- `FRESH_THREE`: three *equally complete* playable concepts, not one winning concept plus two slogans. Each has: truthful hook, view/platform, exact tap/key/drag and target, minute-one sequence, two strategic choices with risk, feedback/state, 20–90s loop, five-minute evolution, failure, world/progression feedback, minimal falsifying test. Distinguish mechanic and player agency rather than art.
- `DEEP_SINGLE` and explicit count: develop only that number. `REFINE_EXISTING`: preserve restrictions, prior decisions and rejected changes; revise the *same* idea. `REVIEW` and `RESCUE`: distinguish actually seen gameplay from descriptions and user reports. No implementation in these modes.
- No GDD, new art, code or new mode transitions for mere brainstorming. One short question is preferable to an unnecessary UI form.

## Research branches: source facts or hypotheses

1. **Substantial competitive or genre research and tools available:** generate independent hypotheses before searching. Verify actual competitor mechanics, player/community evidence where relevant, and any claimed release/popularity facts. Cite every external factual claim and contrast *player verbs, constraints and consequences*, not matching themes. Research should change a mechanic only for a concrete reason.
2. **Small creative prompt:** reason directly without unnecessary long searches.
3. **Unavailable tools:** complete the idea with explicitly labeled research gaps. No invented citations, market metrics, playtesting or originality guarantee.

## Functional interactive choices

Offer selection controls only when the user has a genuine decision and WebUI supports real event callbacks. Every visible choice must be bound to an actual supported user-activated action that submits a new turn preserving the concept, requested mode and constraints. A decorative unbound button is **not** a functioning interface.

When the host supports a text field, accept the user's **custom typed override** and submit the custom value, not a default numbered choice. A minimal conversational reply is the fallback if real host actions or the text field are unavailable. The optional `visual-chat` presentation companion handles its own Continue button; do not duplicate or invent unrelated component APIs.

Test both a selected option and the submitted free-text override in the actual host *before claiming live interaction PASS*. Source documentation or a scripted contract does not prove the host processed user clicks. Without exercised UI evidence, mark live interaction `NOT_EVALUATED`. Never suggest a control triggered side effects if no host acknowledgment exists.

## Boundaries

Keep all unpublished user ideas, project identifiers, benchmarks and uploads private. Distinguish a design's coherent theory, assistant self-review, real code inspected, real runtime play, externally cited gameplay descriptions, and *actual human player behavior*. Only the last supports a claim of observed human enjoyment. The standalone adapter never fetches the S3 repository at runtime.
