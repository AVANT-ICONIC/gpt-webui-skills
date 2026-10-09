"""S4 standalone skill and pinned S3 snapshot regression checks.

These checks cover static instructions, integrity and malicious mutation controls,
NOT human enjoyment, real WebUI callbacks or independent agent effectiveness.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("package_verify", ROOT/"scripts"/"verify_package.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
SKILL = (ROOT/"SKILL.md").read_text(encoding="utf-8")
ADAPTER = (ROOT/"references"/"webui-delivery.md").read_text(encoding="utf-8")

class Contract(unittest.TestCase):
    def test_frontmatter_and_scope(self):
        self.assertTrue(SKILL.startswith("---\nname: game-concept\n"))
        self.assertIn("concept-only requests never authorize code changes", SKILL)
        self.assertIn("no runtime network fetch", SKILL)
    def test_modes_and_no_forced_trio(self):
        for mode in ("FRESH_THREE","DEEP_SINGLE","REFINE_EXISTING","REVIEW","RESCUE","DISCUSSION"):
            with self.subTest(mode=mode): self.assertIn(mode, SKILL)
        self.assertIn("user-requested count overrides three", SKILL)
    def test_equal_mechanics_and_controls(self):
        for phrase in ("Three equally complete","mechanical diversity","first 60 seconds",
                       "00–05s","05–15s","15–30s","30–45s","45–60s","failure/consequence"):
            self.assertIn(phrase.lower(), SKILL.lower())
    def test_research_available_small_unavailable(self):
        for phrase in ("Substantial", "Small creative", "Unavailable tools","cite","invented"):
            self.assertIn(phrase.lower(), ADAPTER.lower())
    def test_functional_selection_and_custom_override(self):
        for phrase in ("custom typed override","submits","NOT_EVALUATED","bound"):
            self.assertIn(phrase.lower(), ADAPTER.lower())
    def test_links_and_no_private_identifiers(self):
        for path in (ROOT/"SKILL.md", ROOT/"references"/"webui-delivery.md"):
            for target in re.findall(r"\]\((\./[^)#]+)", path.read_text(encoding="utf-8")):
                self.assertTrue((path.parent/target).exists(), f"{path}: {target}")
        for path in ROOT.rglob("*"):
            if path.is_file() and path.suffix in {".md",".py",".json"}:
                for term in ("cosmic"+"-office", "agent"+"-workbench"):
                    self.assertNotIn(term, path.read_text(encoding="utf-8").lower())

class Snapshot(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dst = Path(self.tmp.name)/"snapshot"
        shutil.copytree(v.CORE, self.dst)
    def test_exact_pinned_source_and_ten_files(self):
        self.assertEqual([], v.verify(self.dst))
        self.assertEqual(10, len(v.BLOBS))
    def test_22_discipline_coverage(self):
        rows = json.loads((self.dst/"coverage.json").read_text())["baseline_disciplines"]
        self.assertEqual([f"D{x:02}" for x in range(22)], [row["id"] for row in rows])
    def test_mutated_file_detected(self):
        (self.dst/"framing.md").write_text("tamper")
        self.assertTrue(any("pinned source blob drift" in e for e in v.verify(self.dst)))
    def test_forged_manifest_rehash_still_detected(self):
        target = self.dst/"framing.md"
        target.write_text("tamper")
        doc = json.loads((self.dst/v.MANIFEST).read_text())
        row = next(e for e in doc["files"] if e["generated_path"]=="framing.md")
        data = target.read_bytes()
        row["sha256"] = hashlib.sha256(data).hexdigest()
        row["bytes"] = len(data)
        (self.dst/v.MANIFEST).write_text(json.dumps(doc))
        self.assertTrue(any("pinned source blob drift" in e for e in v.verify(self.dst)))
    def test_missing_and_unlisted_file_detected(self):
        (self.dst/"player-interaction.md").unlink()
        (self.dst/"rogue.txt").write_text("unapproved")
        errs = v.verify(self.dst)
        self.assertTrue(any("missing:" in e for e in errs))
        self.assertTrue(any("unexpected:" in e for e in errs))
    def test_manifest_tamper_detected(self):
        (self.dst/v.MANIFEST).write_text("{}")
        self.assertTrue(v.verify(self.dst))
    def test_wrong_pin_and_revision_drift_detected(self):
        self.assertTrue(any("requested source revision" in e for e in v.verify(self.dst, required_revision="f"*40)))
        doc=json.loads((self.dst/v.MANIFEST).read_text())
        doc["source_revision"]="f"*40
        (self.dst/v.MANIFEST).write_text(json.dumps(doc))
        self.assertTrue(any("manifest source_revision" in e for e in v.verify(self.dst)))
    def test_paired_checkout_and_changed_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            src=Path(tmp)
            for name in v.BLOBS: (src/name).write_bytes((self.dst/name).read_bytes())
            self.assertEqual([],v.verify(self.dst,source=src))
            (src/"coverage.json").write_text("updated core without re-pinning")
            self.assertTrue(any("paired source" in e for e in v.verify(self.dst,source=src)))
    def test_symlink_file_rejected(self):
        x=self.dst/"framing.md"
        x.unlink()
        x.symlink_to(v.CORE/"framing.md")
        self.assertTrue(any("unsafe or missing file" in e for e in v.verify(self.dst)))

if __name__ == "__main__":
    unittest.main()
