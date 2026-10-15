"""Regression tests for video-watch's truthful, resilient evidence fallbacks."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "video_watch.py"


class VideoWatchFallbackTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.transcript = self.base / "user transcript.txt"
        self.original = "[00:01:02] First sale allegedly $116.\n[00:03:00] Totals uncertain.\n"
        self.transcript.write_text(self.original, encoding="utf-8")

    def run_watch(self, *args, path=None):
        env = os.environ.copy()
        if path is not None:
            env["PATH"] = path
        env.pop("YT_DLP_BIN", None)
        return subprocess.run(
            [sys.executable, str(SCRIPT), *map(str, args)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
            timeout=90,
        )

    def test_transcript_without_video_or_multimedia_tools(self):
        out = self.base / "output"
        completed = self.run_watch(
            "--transcript-file", self.transcript, "--out-dir", out, path=str(self.base / "no-tools")
        )
        self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
        result = json.loads(completed.stdout)
        self.assertEqual(result["status"], "transcript_only")
        self.assertFalse(result["visual_verified"])
        self.assertEqual(result["frame_count"], 0)
        self.assertEqual(result["contact_sheets"], [])
        self.assertEqual(Path(result["transcript"]).read_text(), self.original)
        manifest = json.loads(Path(result["manifest"]).read_text())
        self.assertEqual(manifest["analysis_mode"], "transcript_only")
        self.assertEqual(manifest["frames"], [])
        self.assertEqual(manifest["video_path"], None)
        self.assertIn("Visual evidence: NONE", Path(result["manifest_md"]).read_text())

    def test_missing_ffmpeg_does_not_erase_supplied_transcript(self):
        completed = self.run_watch(
            "https://youtu.be/xEKaDesfQK0", "--transcript-file", self.transcript,
            "--out-dir", self.base / "fallback",
            path=str(self.base / "missing-tools"),
        )
        self.assertEqual(completed.returncode, 0, completed.stdout)
        result = json.loads(completed.stdout)
        self.assertEqual(result["status"], "transcript_only")
        self.assertIn("ffmpeg", result["reason"])
        self.assertEqual(Path(result["transcript"]).read_text(), self.original)

    def test_video_download_failure_falls_back_instead_of_failing(self):
        if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
            self.skipTest("ffmpeg/ffprobe not present")
        tools_dir = self.base / "media-tools"
        tools_dir.mkdir()
        for name in ("ffmpeg", "ffprobe"):
            (tools_dir / name).symlink_to(shutil.which(name))
        completed = self.run_watch(
            "https://youtu.be/xEKaDesfQK0", "--transcript-file", self.transcript,
            "--out-dir", self.base / "download-failed",
            path=str(tools_dir),
        )
        self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
        result = json.loads(completed.stdout)
        self.assertEqual(result["status"], "transcript_only")
        self.assertIn("yt-dlp", result["reason"])
        self.assertEqual(Path(result["transcript"]).read_text(), self.original)

    def test_missing_transcript_is_a_real_error(self):
        completed = self.run_watch(
            "--transcript-file", self.base / "missing.txt",
            "--out-dir", self.base / "missing-output",
        )
        self.assertEqual(completed.returncode, 2)
        self.assertEqual(json.loads(completed.stdout)["status"], "error")

    def test_empty_transcript_is_a_real_error(self):
        self.transcript.write_text(" \n ", encoding="utf-8")
        completed = self.run_watch("--transcript-file", self.transcript)
        self.assertEqual(completed.returncode, 2)
        self.assertIn("empty", json.loads(completed.stdout)["message"])

    def test_missing_source_and_transcript_rejected(self):
        completed = self.run_watch()
        self.assertEqual(completed.returncode, 2)
        self.assertIn("provide a video source", completed.stderr)

    def test_missing_video_without_transcript_is_not_success(self):
        completed = self.run_watch(
            self.base / "no-video.mp4", "--out-dir", self.base / "failure"
        )
        self.assertNotEqual(completed.returncode, 0)
        result = json.loads(completed.stdout)
        self.assertEqual(result["status"], "error")

    def test_local_video_frames_ready_without_claiming_inspection(self):
        if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
            self.skipTest("ffmpeg/ffprobe not present")
        try:
            import PIL  # noqa: F401
        except ImportError:
            self.skipTest("Pillow is not present")
        video = self.base / "tiny.mp4"
        make = subprocess.run(
            ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
             "-f", "lavfi", "-i", "color=c=blue:s=96x54:r=5",
             "-t", "1", "-pix_fmt", "yuv420p", str(video)],
            capture_output=True, text=True, timeout=30,
        )
        self.assertEqual(make.returncode, 0, make.stderr)
        completed = self.run_watch(
            video, "--transcript-file", self.transcript,
            "--out-dir", self.base / "with-frames", "--max-frames", "12",
            "--frame-width", "96", "--sheet-thumb-width", "96",
        )
        self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
        result = json.loads(completed.stdout)
        self.assertEqual(result["status"], "ready")
        self.assertTrue(result["frames_extracted"])
        self.assertFalse(result["visual_verified"])  # Only a model inspecting them can verify.
        self.assertGreater(result["frame_count"], 0)
        self.assertTrue(all(Path(x).exists() for x in result["contact_sheets"]))
        self.assertEqual(Path(result["transcript"]).read_text(), self.original)


if __name__ == "__main__":
    unittest.main()
