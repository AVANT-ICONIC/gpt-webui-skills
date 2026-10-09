# Temporal and interaction checks

A correct static frame does not prove a correct animation, and a styled control is not proof of functioning input. Judge each separately.

## Animation / video loop protocol

1. Identify user-expected motion: duration, easing, keyframe/deformation trajectory, phase relationship between colors/materials, continuity, start/end states, pause/resume and transitions. Lock an actual moving reference if available; a still cannot establish motion parity.
2. Observe the candidate **in motion** with a renderer/decoder capable of showing its pixels. Capture time-indexed frames from **at least early, quarter, midpoint, three-quarter and near-end** in the *same* cycle; add higher density around fast transitions, repeating motion or flash defects.
3. To check seamless looping, compare frames just before/after the repeat boundary and the apparent velocity/direction on both sides; for a repeat period `T`, inspect near `T - ε` and `T + ε` on a continuous-running timeline. A frame sampled at `T` alone is inadequate. A forced reset-to-frame-zero is not a genuine continuity check.
4. Measure/play through speed and state changes. For hover/focus/slider/modal controls, inspect visual response as well as the state mutation. Beware CSS transitions that restart, a flash crossfade hiding a pop, color regions stuck in discrete bands, and Canvas that has no drawn pixels.
5. Label any inference between sparse frames. If contact sheets cannot resolve smoothness or subtle jitter, require playback/video or mark smoothness **NOT_EVALUATED**. Never declare perfect seamless motion from a still.

### Reproducibility

Document browser/engine, device scale, FPS/sample schedule, animation rate, exact source revision and whether the animation was actually running. Prefer monotonic captures in one page lifetime, not separate page reloads that erase the boundary evidence. If deterministic seeking or Web Animations API playbackTime is used, disclose that it tests phase frames, **not** uninterrupted real-time playback; supplement with a real-time run for loop continuity.

## Responsive and interactive UI checks

For user-relevant viewports, at minimum a representative desktop and narrow mobile (including 320px if it exercises the design):

- Inspect actual screenshots at initial, changed and error/disabled states where relevant; check ancestor clipping and scroll containers, not document width alone.
- Use actual pointer/click and visible state/text feedback. For asynchronous changes, allow a bounded expectation of the **visible** result, not a stale hidden `textContent` match.
- Exercise keyboard Tab/Enter/Space where appropriate, visible focus and essential dialogs including Escape/focus restoration when relevant. A click PASS does not prove keyboard PASS.
- Test hover, focus, sliders, color pickers, navigation and scrolling only if the artifact uses them; don't manufacture controls solely for test coverage.
- For Canvas/WebGL verify pixels are actually painted by the target context and frames change when claimed. If context readback is unavailable, do not infer WebGL visual fidelity from a DOM shell.

Keep functional assertions separate from visual perception: a click test can prove state mutation but not polished glass/shadows; a screenshot can prove appearance but not keyboard navigation. Report each coverage category explicitly.

## Negative controls

A robust QA process notices deliberately broken cases:
- apparently responsive page with controls clipped by an `overflow:hidden` ancestor at 320px;
- a plausible UI button that never changes visible state;
- animation with correct first frame but different period/deformation or discontinuity at loop seam;
- keyboard-focused custom button that ignores Enter;
- reference match scored from CSS source without viewing candidate pixels.

If the tools cannot exercise a case, return the correct **non-PASS** handoff rather than writing imaginary validation.
