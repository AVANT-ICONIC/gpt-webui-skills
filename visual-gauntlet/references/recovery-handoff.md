# Recovery and durable continuation

One failing command does not establish the environment is unusable. Recover safely, record what actually happened and resume the **same artifact**.

## Recovery decision tree

```text
required inspection
  ├─ available → capture actual output → OPEN → compare → fix → recheck
  └─ fails
      ├─ misconfiguration → isolate/reconfigure without privilege → retry
      ├─ alternative FULL renderer/export exists → use it, label scope
      ├─ only structural/DOM output exists → visual/animation NOT_EVALUATED
      ├─ needs owner approval / paid / credentials → BLOCKED_PERMISSION
      └─ genuinely inaccessible after recovery → BLOCKED_ENV
```

Do not quietly replace the user's exact reference, original source revision or required interaction to make a check pass. An environment error does not authorize publishing confidential screenshots or disabling host policies.

### Useful recoveries

- Browser missing/locked profile: verify the executable, inspect actual error, clean **isolated** test profile, recover with a supported full renderer.
- Direct file navigation denied: trusted self-contained synthetic `set_content` can inspect *that* HTML; deployed CSP/assets/cookies are still untested.
- Media unavailable: request/inspect an authorized local export or existing uploaded original. A transcript alone does not validate pixels or movement.
- Image editor constraints: use supported editing flow only. Output can be handed off as non-PASS with the exact fidelity condition that could not be verified.
- Browser tool cannot expose the user's private running window: do not pretend to screen-share or inspect it. Ask only for the necessary approved capture/export or local-agent continuation.

## Durable checkpoint contract

Record to the already-authorized repository, private workspace or chat:

```text
SCOPE / CONTRACT:
BEST VERIFIED REVISION + ARTIFACT:
SOURCE REFERENCE / VIEWPORT / STATE:
WHAT WAS ACTUALLY VIEWED (image paths/times/tools):
TESTS RUN + RESULTS (separate static, interaction, motion):
KNOWN DEFECTS / SEVERITY:
RECOVERY TRIED + EXACT ERROR:
NOT_EVALUATED REQUIREMENTS:
VERDICT (non-PASS while critical checks missing):
NEXT EXECUTABLE STEP:
```

On `continue`, recover this checkpoint and resume the next unresolved operation. Do not restart broad research or repeat completed inspected passes. Keep temporary local binary assets outside public skill repositories; protect privacy in public PR titles, branch names, diffs and CI logs.

## Local coding-agent handoff when runtime genuinely missing

Provide repo/branch/PR/current commit, exact candidate file or URL, specification/constraints, safe synthetic fixture if relevant, last passing tests, failed render/capture command, required viewport/states/timestamp checks, expected observable effects, restrictions and exact next command. Never claim the WebUI completed a browser verification that only the local agent *might* perform.

Keep implementation authorization separate: inspecting a visual does not authorize rewriting unrelated code, merging PRs, launching S3/S4, buying services, or touching private holdouts.

## Stop conditions

- `PASS`: actual critical visual/temporal/interaction observations support acceptance.
- `NEEDS_WORK`: real difference can be fixed in authorized scope.
- `PAUSED_RECOVERABLE`: good next step remains, but this turn is ending.
- `BLOCKED_ENV`: supported safe routes exhausted for a required observation.
- `BLOCKED_PERMISSION`: further work requires permission not already granted.
- `NEEDS_WORK` (plateau noted in the evidence): repeated changes did not improve a major issue; revise the approach and hand off with a **non-PASS** verdict. Keep the five S2 verdict codes consistent with the main skill and VG-08.

Do not turn "three passes" into an arbitrary exit rule; stopping before completion must be transparent.
