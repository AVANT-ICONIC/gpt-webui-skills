# Contributing

Thanks for improving GPT WebUI Skills.

Keep contributions small, explicit, and WebUI-native.

## Rules

- Put each skill in its own top-level folder with a required `SKILL.md`.
- The frontmatter `name` must match the folder name.
- Keep task-specific behavior in task skills.
- Put shared cross-cutting behavior in a companion skill instead of copying it across task skills.
- Do not duplicate rules already owned by another canonical skill.
- Treat observed WebUI limits as dated empirical evidence, not permanent platform guarantees.
- Preserve durable checkpoints and recovery behavior when a skill can span multiple turns.
- Prefer existing project sources of truth over inventing shadow state.
- Keep examples and references only when they materially help execution.

## Pull requests

A contribution should explain:

1. when the skill activates;
2. what problem it solves;
3. what it deliberately does not do;
4. how it hands off or exits;
5. how the change was verified.

Run the repository validation workflow before merging.

## Scope

This repository is intentionally specific to ChatGPT WebUI. Portable, runtime-neutral Agent Skills belong in [AVANT-ICONIC/skills](https://github.com/AVANT-ICONIC/skills).
