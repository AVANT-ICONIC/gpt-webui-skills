"""Static documentation regression checks, not a runtime/tool-call audit."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
SKILL = (ROOT / "visual-chat" / "SKILL.md").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")


class SkillTraceContract(unittest.TestCase):
    def test_always_apply_companion(self):
        self.assertIn("name: visual-chat", SKILL.split("---", 2)[1])
        self.assertIn("always-apply: true", SKILL.split("---", 2)[1])

    def test_distinct_evidence_based_states(self):
        for marker in ("✓ applied", "◐ inspected", "○ considered", "⚠ expected, not loaded"):
            with self.subTest(marker=marker):
                self.assertIn(f"| `{marker}` |", SKILL)

    def test_all_five_features_and_limitations(self):
        for snippet in (
            "every ordinary chat response",
            "Explicit missing-skill warning",
            "Phase attribution for complex work",
            "Optional evidence links and honesty boundary",
            "SKILL.md",
            "commit permalink",
            "host-generated tool/skill event ledger",
            "none applied",
            "exact-output-only",
        ):
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, SKILL)

    def test_documented_custom_instruction_routing(self):
        for snippet in (
            "### Skill Trace",
            "🧩 Skills:",
            "At the end of ordinary chat replies, follow visual-chat's Skill Trace",
            "self-report, not host-generated telemetry",
        ):
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, README)


if __name__ == "__main__":
    unittest.main()
