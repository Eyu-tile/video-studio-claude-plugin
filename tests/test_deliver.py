"""Tests for `vs deliver`: the Apps Script made for a folder, picking only the latest version of every file, refusing
an old cut, the request file, the upload to one-time links (a local stand-in for Drive's resumable-upload sessions)
and the check against a Drive listing.

Run: python3 -m unittest discover -s tests -v
"""
import http.server
import json
import os
import shutil
import subprocess
import tempfile
import threading
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VS = ROOT / "plugins" / "video-studio" / "bin" / "vs"
FOLDER = "1AbCdEfGhIjKlMnOpQrStUvWxYz012345"


def sh(*cmd, env=None, ok=True, cwd=None):
    p = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, env=env, cwd=cwd)
    if ok and p.returncode != 0:
        raise AssertionError(f"{' '.join(map(str, cmd))}\n{p.stdout}\n{p.stderr[-2000:]}")
    return p


class FakeDrive(http.server.BaseHTTPRequestHandler):
    """Accepts one PUT per link, like a Drive resumable-upload session, and answers with the new file's id."""
    got = {}

    def do_PUT(self):
        n = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(n)
        name = self.path.strip("/")
        if name in FakeDrive.got:                       # a link uploads one file only
            self.send_response(404); self.end_headers(); return
        FakeDrive.got[name] = len(body)
        out = json.dumps({"id": "drive_" + name, "name": name}).encode()
        self.send_response(200); self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(out))); self.end_headers(); self.wfile.write(out)

    def log_message(self, *a):
        pass


class DeliverTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="vs-deliver-"))
        cls.ws = cls.tmp / "video-studio"
        cls.env = {**os.environ, "VS_WORKSPACE": str(cls.ws), "NO_PROXY": "127.0.0.1,localhost",
                   "no_proxy": "127.0.0.1,localhost"}
        sh(VS, "new", "demo", env=cls.env, cwd=cls.tmp)
        cls.ads = cls.ws / "projects" / "demo" / "out" / "ads"
        cls.ads.mkdir(parents=True, exist_ok=True)
        for name, size in [("AD_Batch1_Week2_H1_9x16_v1.mp4", 1000), ("AD_Batch1_Week2_H1_9x16_v5.mp4", 5000),
                           ("AD_Batch1_Week2_H2_9x16_v5.mp4", 5200), ("AD_Batch1_Week2_H1_4x5_v3.mp4", 3000)]:
            (cls.ads / name).write_bytes(os.urandom(size))
        cls.srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), FakeDrive)
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
        sh(VS, "deliver", "setup", f"https://drive.google.com/drive/folders/{FOLDER}?usp=sharing",
           "--name", "Acme", "--root-name", "Acme ads", env=cls.env, cwd=cls.tmp)

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def vs(self, *args, ok=True):
        return sh(VS, *args, env=self.env, ok=ok, cwd=self.tmp)

    def plan(self, *args):
        out = self.vs("deliver", "plan", "demo", *args).stdout
        d = sorted((self.ws / "projects" / "demo" / "out" / "delivery").glob("*/plan.json"),
                   key=lambda p: p.stat().st_mtime)[-1].parent
        return out, d, json.loads((d / "plan.json").read_text())

    def test_setup_writes_the_script_for_that_folder(self):
        code = (self.ws / "delivery" / "acme" / "Code.gs").read_text()
        self.assertIn(f"const ROOT_FOLDER_ID = '{FOLDER}';", code)
        self.assertNotIn("__ROOT", code)
        self.assertTrue((self.ws / "delivery" / "acme" / "appsscript.json").exists())
        cfg = json.loads((self.ws / "style" / "delivery.json").read_text())
        self.assertEqual(cfg["default"], "acme")
        self.assertEqual(cfg["targets"]["acme"]["root_id"], FOLDER)
        self.assertIn("acme", self.vs("deliver", "targets").stdout)

    def test_plan_keeps_only_the_latest_version(self):
        out, d, plan = self.plan()
        names = sorted(f["name"] for f in plan["files"])
        self.assertEqual(names, ["AD_Batch1_Week2_H1_4x5_v3.mp4", "AD_Batch1_Week2_H1_9x16_v5.mp4",
                                 "AD_Batch1_Week2_H2_9x16_v5.mp4"])
        self.assertEqual(plan["folder"], "AD_Batch1_Week2")
        self.assertIn("left out 1 older version", out)
        self.assertIn("different versions", out)
        req = json.loads((d / f"req_{plan['id']}.json").read_text())
        self.assertEqual(req["folder"], "AD_Batch1_Week2")
        self.assertEqual({f["name"]: f["size"] for f in req["files"]},
                         {"AD_Batch1_Week2_H1_4x5_v3.mp4": 3000, "AD_Batch1_Week2_H1_9x16_v5.mp4": 5000,
                          "AD_Batch1_Week2_H2_9x16_v5.mp4": 5200})
        self.assertTrue(all(f["mime"] == "video/mp4" for f in req["files"]))
        self.assertNotIn("path", json.dumps(req))           # the request carries no local paths

    def test_refuses_an_old_cut_unless_allowed(self):
        old = self.ads / "AD_Batch1_Week2_H1_9x16_v1.mp4"
        p = self.vs("deliver", "plan", "demo", "--files", old, ok=False)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("newer version exists", p.stderr + p.stdout)
        out, d, plan = self.plan("--files", old, "--allow-old", "--folder", "Approved v1")
        self.assertEqual([f["name"] for f in plan["files"]], [old.name])
        self.assertEqual(plan["folder"], "Approved v1")

    def test_upload_and_verify(self):
        FakeDrive.got.clear()
        _, d, plan = self.plan()
        port = self.srv.server_address[1]
        res = {"ok": True, "folderId": "fold123", "folderUrl": "https://drive.google.com/drive/folders/fold123",
               "uploads": [{"name": f["name"], "size": f["size"], "uploadUrl": f"http://127.0.0.1:{port}/{f['name']}"}
                           for f in plan["files"]]}
        rp = self.tmp / "res.json"
        rp.write_text(json.dumps(res))
        out = self.vs("deliver", "upload", "demo", rp).stdout
        self.assertEqual(FakeDrive.got, {f["name"]: f["size"] for f in plan["files"]})
        self.assertNotIn(f"127.0.0.1:{port}", out)            # upload links stay out of the output
        rec = json.loads((d / "delivered.json").read_text())
        self.assertEqual(len(rec["files"]), 3)
        self.assertEqual(rec["folder_url"], res["folderUrl"])
        self.assertEqual(rec["failed"], 0)
        # a Drive listing (search_files output) with every file at full size passes; a short one fails
        listing = {"files": [{"title": f["name"], "fileSize": str(f["size"])} for f in plan["files"]]}
        lp = self.tmp / "listing.json"
        lp.write_text(json.dumps(listing))
        self.assertIn("verified", self.vs("deliver", "verify", "demo", lp).stdout)
        self.assertTrue(json.loads((d / "delivered.json").read_text())["verified"])
        listing["files"][0]["fileSize"] = "12"
        lp.write_text(json.dumps(listing))
        self.assertNotEqual(self.vs("deliver", "verify", "demo", lp, ok=False).returncode, 0)
        log = (self.ws / "projects" / "demo" / "out" / "delivery" / "log.md").read_text()
        self.assertIn("3/3 file(s)", log)
        self.assertIn("1 file(s) wrong", log)
        # the same links can't be used twice: a second upload fails and says so
        p = self.vs("deliver", "upload", "demo", rp, ok=False)
        self.assertNotEqual(p.returncode, 0)

    def test_refused_request(self):
        self.plan()
        rp = self.tmp / "res_bad.json"
        rp.write_text(json.dumps({"ok": False, "error": "bad folder: x/y"}))
        p = self.vs("deliver", "upload", "demo", rp, ok=False)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("bad folder", p.stderr + p.stdout)


if __name__ == "__main__":
    unittest.main()
