"""Revisions in two commands (`vs fix`): the note's moment with its words, pauses and exact cut commands; then
captions remade, a --since render of only the changed shots, a window-only QA and a before/after sheet (needs ffmpeg).

Run: python3 -m unittest discover -s tests -v
"""
import json
import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VS = ROOT / "plugins" / "video-studio" / "bin" / "vs"


def sh(*cmd, cwd=None, env=None, ok=True):
    p = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, cwd=cwd, env=env)
    if ok and p.returncode != 0:
        raise AssertionError(f"{' '.join(map(str, cmd))}\n{p.stdout}\n{p.stderr[-2500:]}")
    return p


class FixTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="vs-fix-"))
        cls.env = {**os.environ, "VS_WORKSPACE": str(cls.tmp / "video-studio")}
        cls.env.pop("VS_BRAND", None)
        pd = cls.tmp / "video-studio" / "projects" / "demo"
        for d in ("raw", "work", "out"):
            (pd / d).mkdir(parents=True)
        cls.pd = pd
        sh("ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "testsrc2=s=320x180:r=30:d=20", "-f", "lavfi",
           "-i", "sine=f=220:d=20", "-shortest", "-c:v", "libx264", "-g", "60", "-c:a", "aac", pd / "raw" / "talk.mp4")
        # a transcript with a long pause after word 6 (3.0 -> 3.9 s) and an "um" at 6.2 s
        words, t = [], 0.3
        for i, w in enumerate("so this is the main point here um and then the next part comes now okay".split()):
            if i == 7:
                t += 0.9
            words.append({"w": w, "s": round(t, 2), "e": round(t + 0.3, 2), "p": 0.99})
            t += 0.42
        (pd / "work" / "talk.transcript.json").write_text(json.dumps(
            {"source": str(pd / "raw" / "talk.mp4"), "words": words, "language": "en"}))
        edl = {"source": str(pd / "raw" / "talk.mp4"),
               "segments": [{"start": 0.0, "end": 4.6}, {"start": 5.0, "end": 9.5}, {"start": 10.0, "end": 14.0}],
               "meta": {"from": str(pd / "work" / "talk.transcript.json")}}
        (pd / "work" / "edl.json").write_text(json.dumps(edl))
        sh(VS, "captions", pd / "work" / "talk.transcript.json", pd / "work" / "edl.json", "-o",
           pd / "work" / "captions", "--style", "bold-pop", "--aspect", "16:9", cwd=cls.tmp, env=cls.env)
        sh(VS, "render", pd / "work" / "edl.json", "-o", pd / "out" / "cut.mp4", "--captions",
           pd / "work" / "captions.ass", cwd=cls.tmp, env=cls.env)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_two_command_revision(self):
        out = sh(VS, "fix", "demo", "0:03 shorten this pause", cwd=self.tmp, env=self.env).stdout
        self.assertIn("Reviewed version: cut.mp4", out)
        self.assertIn("| shot 1 | segments[0] |", out)
        self.assertIn("[1.98] main", out)                                   # words with their output times
        m = re.search(r"pause ([\d.]+)-([\d.]+) \(([\d.]+) s\).*`vs edl cut (\S+) ([\d.]+) ([\d.]+)`", out)
        self.assertIsNotNone(m, out)
        self.assertIn("filler 'um'", out)
        self.assertNotIn("segments[2]", out)                                # only what is at that moment
        sh(VS, "edl", "cut", m.group(4), m.group(5), m.group(6), cwd=self.tmp, env=self.env)
        r = sh(VS, "fix", "demo", "--render", "--how", "shortened the pause", cwd=self.tmp, env=self.env)
        self.assertIn("captions remade", r.stdout)
        self.assertIn("revision: re-encoded", r.stdout)                     # not a full render
        self.assertIn("note 1", r.stdout)
        v2 = self.pd / "out" / "cut_v2.mp4"
        self.assertTrue(v2.exists() and Path(str(v2) + ".render.json").exists())
        self.assertTrue((self.pd / "work" / "focus" / "note-1" / "frames.png").exists())
        book = json.loads((self.pd / "work" / "notes.json").read_text())
        self.assertEqual(book["notes"][0]["status"], "done")
        # the same result as rendering the edit in full
        sh(VS, "render", self.pd / "work" / "edl.json", "-o", self.pd / "out" / "full.mp4", "--captions",
           self.pd / "work" / "captions.ass", "--since", "none", cwd=self.tmp, env=self.env)
        p = sh("ffmpeg", "-hide_banner", "-i", v2, "-i", self.pd / "out" / "full.mp4", "-lavfi", "[0:v][1:v]psnr",
               "-f", "null", "-")
        mn = re.findall(r"min:([\d.]+|inf)", p.stderr)[-1]
        self.assertGreater(float("inf") if mn == "inf" else float(mn), 40)

    def test_whole_video_note_has_no_window(self):
        out = sh(VS, "fix", "demo", "the whole thing should be warmer", cwd=self.tmp, env=self.env).stdout
        self.assertIn("about the whole video", out)


if __name__ == "__main__":
    unittest.main()
