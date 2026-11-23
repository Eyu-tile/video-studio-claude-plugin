"""`vs hyperscale`: a Hyperscale brief becomes a project; renders are prepared, uploaded and recorded."""
import http.server
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "plugins" / "video-studio"
TOOLS = ROOT / "tools"
BRIEF = Path(__file__).parent / "fixtures" / "hyperscale" / "brief_450.json"


class _Put(http.server.BaseHTTPRequestHandler):
    got = []

    def do_PUT(self):
        n = int(self.headers.get("Content-Length", 0))
        _Put.got.append((self.headers.get("Content-Type"), len(self.rfile.read(n))))
        self.send_response(200)
        self.end_headers()

    def log_message(self, *a):
        pass


class HyperscaleTest(unittest.TestCase):
    def setUp(self):
        self.ws = Path(tempfile.mkdtemp(prefix="vs-hs-"))
        self.env = {**os.environ, "VS_WORKSPACE": str(self.ws)}
        self.p = self.ws / "projects" / "hs-450-transformation"

    def tearDown(self):
        shutil.rmtree(self.ws, ignore_errors=True)

    def hs(self, *args, ok=True):
        r = subprocess.run([sys.executable, str(TOOLS / "hyperscale.py"), *args], capture_output=True, text=True,
                           env=self.env, cwd=self.ws)
        if ok and r.returncode:
            raise AssertionError(f"{args}\n{r.stdout}\n{r.stderr}")
        return r

    def clip(self, path, size="1080x1920"):
        path.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"color=c=blue:s={size}:d=4",
                        "-f", "lavfi", "-i", "sine=f=440:d=4", "-shortest", "-c:v", "libx264", "-pix_fmt", "yuv420p",
                        "-c:a", "aac", "-metadata", "title=secret-project", str(path)], check=True)

    def test_pull_builds_project(self):
        out = self.hs("pull", str(BRIEF), "--brand", "Haven & Spool").stdout
        self.assertIn("450_H1_9x16_v3.mp4", out)  # v1 and v2 already on the brief
        self.assertTrue((self.p / "BRIEF.md").exists())
        ab = json.loads((self.p / "work" / "brief.json").read_text())
        self.assertEqual(ab["format"], "ugc")
        self.assertEqual(ab["awareness"], "solution")
        self.assertEqual(ab["audience"]["age"], "55+")  # 45-65 -> midpoint 55
        self.assertEqual(ab["product"], "Roll-on")  # "rolling it on" in the brief, no product name given
        self.assertTrue(ab["policy"]["before_after"])
        self.assertIn("BUY 1 GET 1 FREE", ab["offer"])
        shots = json.loads((self.p / "work" / "hyperscale" / "shots.json").read_text())
        self.assertEqual(shots[0]["source"], "text")  # hook title rows are text, not footage
        self.assertIn("0:00", (self.p / "work" / "hyperscale" / "notes.txt").read_text())
        hist = json.loads((self.ws / "history" / "HS-450.json").read_text())
        self.assertEqual(len(hist["feedback"]), 1)
        self.hs("notes", str(BRIEF), "--project", self.p.name)  # same note again: not duplicated
        hist = json.loads((self.ws / "history" / "HS-450.json").read_text())
        self.assertEqual(len(hist["feedback"]), 1)

    def test_prep_put_done(self):
        self.hs("pull", str(BRIEF))
        self.clip(self.p / "out" / "final_h1.mp4")
        self.clip(self.p / "out" / "final_h2.mp4", size="1080x1080")
        r = self.hs("prep", "--project", self.p.name, ok=False)
        self.assertEqual(r.returncode, 1)  # the square H2 fails the 9x16 check
        self.assertIn("ok   450_H1_9x16_v3.mp4", r.stdout)
        self.assertIn("is not 9x16", r.stdout)
        f = self.p / "out" / "hyperscale" / "450_H1_9x16_v3.mp4"
        tags = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format_tags", "-of", "json", str(f)],
                              capture_output=True, text=True).stdout
        self.assertNotIn("secret-project", tags)
        srv = http.server.HTTPServer(("127.0.0.1", 0), _Put)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        try:
            url = f"http://127.0.0.1:{srv.server_port}/up"
            self.assertIn("failed its checks", self.hs("put", "H2", "--project", self.p.name, "--url", url,
                                                       ok=False).stderr)
            self.hs("put", "H1", "--project", self.p.name, "--url", url, "--upload-id", "u1")
        finally:
            srv.shutdown()
            srv.server_close()
        self.assertEqual(_Put.got[-1][0], "video/mp4")
        self.assertEqual(_Put.got[-1][1], f.stat().st_size)
        self.hs("done", "H1", "--project", self.p.name)
        st = json.loads((self.p / "work" / "hyperscale" / "state.json").read_text())
        h1 = next(u for u in st["uploads"] if u["hook"] == "H1")
        self.assertEqual((h1["status"], h1["upload_id"]), ("attached", "u1"))
        self.assertIn("attached", self.hs("status", "--project", self.p.name).stdout)


if __name__ == "__main__":
    unittest.main()
