# Capability probe and evidence-route selection

Use a route **only after confirming it is available now**. A previous session's browser path, tool name or screenshot is not current evidence. The WebUI may have image tools and connectors but no direct access to the user's running app or desktop.

## Probe the task before the tool

| Artifact / claim | Required observation | Primary route if available | Inadequate substitute |
| --- | --- | --- | --- |
| Still image / edit | actually returned image pixels | supported image create/edit + viewing opened result | prose prompt, request accepted, filename |
| Exact reference replication | reference and candidate at comparable scales | inspect both rendered images, crop/overlay/measure if warranted | generic style description |
| HTML/web UI | rendered layout and live state | installed full browser + screenshot + pointer/keyboard actions on **actual candidate** | source scan, DOM-only engine, screenshot-only fake |
| Canvas/WebGL | rendered pixels over relevant states | verified full renderer with actual canvas output and checks | CSS canvas border, missing context, DOM screenshot guess |
| CSS/SVG animation | sampled frames across real time and loop boundary | full rendering engine / recording / representative timestamps | a single pleasing frame or CSS keyframe text |
| Video | visual frames + timing, optionally audio/captions | real decoded frames/clip and appropriate zoom-ins | transcript-only summary |
| PDF/slide/document | rasterized delivered pages | supported page render/export + open/inspect pages | parsed text, layout source only |
| Design-source only | structure and constraints | source review and static checks, explicitly scoped | claiming visual parity |

### Probe in this order

1. Identify the *actual* artifact bytes/URL and any user-provided original. Never invent sandbox paths or assume private files are locally mounted.
2. Inspect available tool capabilities (file viewer, image editor/generator, code container, browser, PDF/video pipeline, connected source). Distinguish tool advertised capability from an actual successful call.
3. For a browser: check executable presence and launch permissions, then attempt an isolated context/profile, actual candidate page, one screenshot and one real input. For animation also verify time advances while capturing. Capture network/CSP differences when relevant.
4. Prefer a faithful **full rendering engine** for visual fidelity. A lightweight engine may be faster for DOM or navigation but cannot substitute for unverified CSS filters, Canvas, WebGL, video or font pixels.
5. Inspect each produced image with an actual image-view mechanism. If no such mechanism is available, a generated PNG filename is **CAPTURED_NOT_VIEWED**, not inspected visual QA.

## Safe recovery ladder

- **Browser launch fails:** inspect the error; check executable location, installed full browsers, profiles/locks, available Playwright/browser dependencies and display flags. Retry with a fresh *isolated* profile or another permitted full browser where available. No permission bypass.
- **`file://` blocked:** do not declare Chromium broken. For *trusted self-contained synthetic HTML* a browser `set_content` route may be a legitimate render; for real apps use an authorized live/local origin. Label differences: no deployed-origin/CSP/network/asset fidelity demonstrated by `set_content`.
- **Browser exists but rendering unsupported:** prefer app-native capture/export or another approved full renderer. If only DOM semantics are available, label visual/temporal claims NOT_EVALUATED; do not silently treat them as PASS.
- **Image editing blocked:** use another actually supported edit route, preserve original, or mark the exact unsupported portion and provide a feasible handoff. Never imply that a one-shot image generator exposes its internal layers.
- **PDF pages unavailable:** use an allowed page rasterizer/preview after reading artifact-specific tool instructions; do not substitute text extraction for typography/layout checks.
- **No route succeeds:** preserve last-known best and issue `BLOCKED_ENV` (or `BLOCKED_PERMISSION` if action requires ungranted access). Name the failed commands/capability gaps without leaking private paths/secrets.

Allow genuinely free, project-isolated troubleshooting consistent with current permissions. Do not install global packages, change security settings, request credentials, open paid accounts or upload private material to third parties by default.

## Practical render rules

- Test **the actual candidate**. A simplified screenshot-only clone may be useful to isolate a bug but cannot prove the original is correct.
- Compare identical viewport/device scale, theme, font-load state and animation sample where meaningful. If normalized/cropped, retain original images and disclose the transformation.
- Check scroll containers and visual edges, not merely `document.scrollWidth > innerWidth`. An `overflow:hidden` ancestor can hide an essential button even when the document width equals the viewport.
- Make screenshot/interaction probes deterministic where possible: pause unrelated ambient animations for *static* layout comparisons only, and label that capture as modified; **never** use paused-animation captures to pass temporal motion.
- If screenshots were not opened/viewed, do not call them visually inspected, even if a pixel comparison script ran.
