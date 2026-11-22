#!/usr/bin/env python3
"""Deliver approved videos straight into a Google Drive folder, at any size, with no copy on anyone's computer.

The Google Drive connector uploads at most 10 MB, and finished videos are far bigger. A small Apps Script that the
folder's owner installs once ("video-studio delivery", made by `vs deliver setup`) answers request files in an inbox
folder with one-time upload links (Drive resumable-upload sessions). Claude writes the request and reads the answer
with the Drive connector; this tool picks the files, writes the request, uploads to the links and checks the result.

  vs deliver setup <folder link or id> --name acme [--root-name "Acme ads"]   save a delivery target + write its Apps Script
  vs deliver targets                                list saved targets
  vs deliver plan <project> [--to acme] [--dir out/ads] [--files a.mp4 ...] [--folder "Ad name"] [--allow-old]
                                                    pick the LATEST version of every file and write req_<id>.json
  vs deliver upload <project> <res.json> [--id <id>]   upload each file to its link (curl), record the Drive ids
  vs deliver verify <project> <listing.json> [--id <id>]   compare a Drive listing (search_files output) with what was sent

Files are versioned by a `_v<N>` suffix (…_H1_9x16_v5.mp4). `plan` keeps only the highest N of each file and refuses
an older version named with --files unless --allow-old is given. Everything is written under
<project>/out/delivery/<id>/ (plan.json, req_<id>.json, delivered.json) and summarised in out/delivery/log.md.
"""
import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import die, load_json, save_json  # noqa: E402

TEMPLATES = Path(__file__).parent / "templates" / "drive_delivery"
INBOX = "_claude_uploads"
MEDIA_EXT = {".mp4", ".mov", ".m4v", ".webm", ".mxf", ".wav", ".mp3", ".m4a", ".png", ".jpg", ".jpeg", ".gif",
             ".pdf", ".zip", ".srt", ".vtt"}
MIME = {".mp4": "video/mp4", ".m4v": "video/mp4", ".mov": "video/quicktime", ".webm": "video/webm",
        ".mxf": "application/mxf", ".wav": "audio/wav", ".mp3": "audio/mpeg", ".m4a": "audio/mp4",
        ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".gif": "image/gif",
        ".pdf": "application/pdf", ".zip": "application/zip", ".srt": "text/plain", ".vtt": "text/vtt"}
VERSION = re.compile(r"^(?P<base>.+?)[_-]v(?P<n>\d+)$", re.I)
NAME_OK = re.compile(r"^[^/\\]{1,200}$")


def workspace():
    ws = os.environ.get("VS_WORKSPACE")
    if ws:
        return Path(ws)
    top = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    return Path(top.stdout.strip() if top.returncode == 0 else os.getcwd()) / "video-studio"


def config_path():
    return workspace() / "style" / "delivery.json"


def load_config():
    p = config_path()
    return load_json(p) if p.exists() else {"targets": {}, "default": None}


def project_dir(name):
    p = Path(name)
    if p.is_dir() and (p / "out").is_dir():
        return p.resolve()
    d = workspace() / "projects" / name
    if not d.is_dir():
        die(f"no project {name} (looked in {d})")
    return d


def folder_id(s):
    m = re.search(r"/folders/([A-Za-z0-9_-]{10,})", s) or re.search(r"[?&]id=([A-Za-z0-9_-]{10,})", s)
    if m:
        return m.group(1)
    if re.fullmatch(r"[A-Za-z0-9_-]{10,}", s):
        return s
    die(f"not a Drive folder link or id: {s}")


def js_str(s):
    return json.dumps(str(s))[1:-1].replace("'", "\\'")


# ---------- setup ----------
def cmd_setup(a):
    fid = folder_id(a.folder)
    name = re.sub(r"[^a-z0-9-]+", "-", a.name.lower()).strip("-")
    if not name:
        die("--name needs letters or digits")
    root_name = a.root_name or name
    out = workspace() / "delivery" / name
    out.mkdir(parents=True, exist_ok=True)
    code = (TEMPLATES / "Code.gs").read_text(encoding="utf-8")
    code = code.replace("__ROOT_FOLDER_ID__", js_str(fid)).replace("__ROOT_NAME__", js_str(root_name))
    (out / "Code.gs").write_text(code, encoding="utf-8")
    shutil.copy(TEMPLATES / "appsscript.json", out / "appsscript.json")
    cfg = load_config()
    cfg["targets"][name] = {"root_id": fid, "root_name": root_name, "inbox": INBOX,
                            "inbox_id": cfg["targets"].get(name, {}).get("inbox_id"),
                            "folder_url": f"https://drive.google.com/drive/folders/{fid}"}
    if not cfg.get("default") or a.default:
        cfg["default"] = name
    save_json(config_path(), cfg)
    print(f"delivery target '{name}' saved in {config_path()}")
    print(f"Apps Script written to {out}/Code.gs and appsscript.json")
    print("One-time install, by the Google account that owns (or can edit) the folder:")
    print("  1. script.google.com > New project. Paste Code.gs. Project Settings > show appsscript.json, paste it.")
    print("  2. Choose setup in the function menu > Run > allow access (Advanced > Go to project, for your own script).")
    print(f"  3. It creates {root_name}/{INBOX} and answers requests there every minute.")


def cmd_targets(a):
    cfg = load_config()
    if not cfg["targets"]:
        print("no delivery targets: vs deliver setup <folder link> --name <name>")
        return
    for k, t in cfg["targets"].items():
        mark = "*" if k == cfg.get("default") else " "
        print(f"{mark} {k}: {t['root_name']}  {t['folder_url']}  inbox {t['inbox']}" + (f" ({t['inbox_id']})" if t.get("inbox_id") else ""))


def cmd_inbox(a):
    cfg = load_config()
    if a.target not in cfg["targets"]:
        die(f"no target {a.target}: vs deliver targets")
    cfg["targets"][a.target]["inbox_id"] = a.inbox_id
    save_json(config_path(), cfg)
    print(f"inbox id saved for {a.target}")


def target(cfg, name):
    name = name or cfg.get("default")
    if not name or name not in cfg["targets"]:
        die("no delivery target: vs deliver setup <folder link> --name <name> (or pass --to)")
    return name, cfg["targets"][name]


# ---------- choose files ----------
def split_version(path):
    m = VERSION.match(path.stem)
    return (m.group("base"), int(m.group("n"))) if m else (path.stem, None)


def latest(files):
    """Highest _vN of each file (same name without the version, same extension)."""
    best = {}
    for f in files:
        base, n = split_version(f)
        key = (base, f.suffix.lower())
        if key not in best or (n or 0) > (split_version(best[key])[1] or 0):
            best[key] = f
    return sorted(best.values())


def ad_name(files, fallback):
    stems = [split_version(f)[0] for f in files]
    common = os.path.commonprefix(stems)
    if len(stems) > 1 and common not in stems:
        common = re.split(r"[_\- ]", common[::-1], maxsplit=1)[-1][::-1] if re.search(r"[_\- ]", common) else ""
    common = re.sub(r"([_\- ](H|hook)\d+)?([_\- ]\d+x\d+)?$", "", common, flags=re.I).strip("_- ")
    return common or fallback


def cmd_plan(a):
    pdir = project_dir(a.project)
    cfg = load_config()
    tname, t = target(cfg, a.to)
    if a.files:
        chosen = [Path(f).resolve() for f in a.files]
        for f in chosen:
            if not f.is_file():
                die(f"no file {f}")
        newer = []
        for f in chosen:
            base, n = split_version(f)
            if n is None:
                continue
            for g in f.parent.iterdir():
                b2, n2 = split_version(g)
                if b2 == base and g.suffix.lower() == f.suffix.lower() and n2 is not None and n2 > n:
                    newer.append(f"{f.name} -> {g.name}")
        if newer and not a.allow_old:
            die("a newer version exists, so this would deliver an old cut:\n  " + "\n  ".join(newer)
                + "\npass the newest files, or --allow-old if the producer approved the older one")
    else:
        if a.dir:
            d = Path(a.dir)
            if not d.is_absolute():
                d = pdir / d if (pdir / d).is_dir() else d.resolve()
        else:
            d = pdir / "out" / "ads" if (pdir / "out" / "ads").is_dir() else pdir / "out"
        if not d.is_dir():
            die(f"no folder {d}")
        found = [f for f in d.iterdir() if f.is_file() and f.suffix.lower() in MEDIA_EXT and not f.name.startswith(".")]
        if not found:
            die(f"nothing to deliver in {d}")
        chosen = latest(found)
        skipped = sorted(set(found) - set(chosen))
        if skipped:
            print(f"left out {len(skipped)} older version(s): " + ", ".join(f.name for f in skipped[:6])
                  + (" …" if len(skipped) > 6 else ""))
    names = [f.name for f in chosen]
    if len(set(names)) != len(names):
        die("two files share a name; Drive would hold both under one name")
    for n in names:
        if not NAME_OK.match(n) or n.startswith("."):
            die(f"file name can't be delivered: {n}")
    versions = sorted({split_version(f)[1] for f in chosen if split_version(f)[1] is not None})
    folder = a.folder or ad_name(chosen, pdir.name)
    if not NAME_OK.match(folder) or folder.startswith("."):
        die(f"bad folder name: {folder}")
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d%H%M%S")
    rid = re.sub(r"[^A-Za-z0-9_-]+", "-", f"{pdir.name}"[:48]) + f"_{stamp}_{os.urandom(2).hex()}"
    out = pdir / "out" / "delivery" / rid
    out.mkdir(parents=True, exist_ok=True)
    files = [{"name": f.name, "size": f.stat().st_size, "mime": MIME.get(f.suffix.lower(), "application/octet-stream")}
             for f in chosen]
    req = {"folder": folder, "files": files}
    save_json(out / f"req_{rid}.json", req)
    save_json(out / "plan.json", {"id": rid, "target": tname, "folder": folder, "created": stamp,
                                  "files": [dict(x, path=str(f)) for x, f in zip(files, chosen)]})
    total = sum(x["size"] for x in files)
    print(f"delivery {rid}: {len(files)} file(s), {total / 1e6:.1f} MB, into {t['root_name']}/{folder}")
    for x in files:
        print(f"  {x['name']}  {x['size'] / 1e6:.1f} MB")
    if len(versions) > 1:
        print(f"note: the files are at different versions ({', '.join('v%d' % v for v in versions)}); "
              "check each is the approved one")
    print(f"request: {out / f'req_{rid}.json'}")
    inbox = f"'{t['inbox_id']}'" if t.get("inbox_id") else f"the '{t['inbox']}' folder inside {t['root_name']} ({t['root_id']})"
    print(f"next: with the Drive connector, create req_{rid}.json in {inbox} (text/plain, no conversion) with exactly "
          f"that content; within about a minute res_{rid}.json appears there. Save it locally, then:")
    print(f"  vs deliver upload {a.project} <saved res_{rid}.json>")


# ---------- upload / verify ----------
def plan_for(pdir, rid):
    base = pdir / "out" / "delivery"
    if rid:
        p = base / rid / "plan.json"
    else:
        plans = sorted(base.glob("*/plan.json"), key=lambda p: p.stat().st_mtime)
        if not plans:
            die(f"no delivery planned for {pdir.name}: vs deliver plan {pdir.name}")
        p = plans[-1]
    if not p.exists():
        die(f"no plan {p}")
    return p.parent, load_json(p)


def put(path, url, mime):
    r = subprocess.run(["curl", "-sS", "--fail-with-body", "-X", "PUT", "--upload-file", str(path),
                        "-H", f"Content-Type: {mime}", "--retry", "3", "--retry-delay", "5", url],
                       capture_output=True, text=True)
    try:
        return json.loads(r.stdout)["id"], None
    except Exception:
        return None, f"upload failed ({r.returncode}) {r.stdout[-300:]} {r.stderr[-300:]}".strip()


def log_line(pdir, text):
    p = pdir / "out" / "delivery" / "log.md"
    new = not p.exists()
    with p.open("a", encoding="utf-8") as fh:
        if new:
            fh.write("# Deliveries\n\n")
        fh.write(text + "\n")


def cmd_upload(a):
    if not shutil.which("curl"):
        die("curl is needed for the upload")
    pdir = project_dir(a.project)
    d, plan = plan_for(pdir, a.id)
    res = load_json(Path(a.res))
    if not res.get("ok"):
        die("the delivery script refused the request: " + str(res.get("error")))
    links = {u["name"]: u for u in res.get("uploads", [])}
    done, bad = [], 0
    for f in plan["files"]:
        u, path = links.get(f["name"]), Path(f["path"])
        if not u:
            print(f"{f['name']}: no upload link in the answer"); bad += 1; continue
        size = path.stat().st_size if path.exists() else -1
        if size != f["size"] or int(u["size"]) != f["size"]:
            print(f"{f['name']}: size changed since the plan ({size} vs {f['size']}); plan again"); bad += 1; continue
        fid, err = put(path, u["uploadUrl"], f["mime"])
        if err:
            print(f"{f['name']}: {err}"); bad += 1; continue
        print(f"{f['name']}: {size} bytes -> Drive file {fid}")
        done.append({"name": f["name"], "size": size, "drive_id": fid})
    rec = {"id": plan["id"], "target": plan["target"], "folder": plan["folder"], "folder_id": res.get("folderId"),
           "folder_url": res.get("folderUrl"), "files": done, "failed": bad, "verified": False,
           "at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
    save_json(d / "delivered.json", rec)
    log_line(pdir, f"- {rec['at']} · {plan['id']} · {len(done)}/{len(plan['files'])} file(s) · {plan['folder']} · "
                   f"{rec['folder_url']}" + (" · FAILED: " + str(bad) if bad else ""))
    print("folder:", rec["folder_url"])
    print(f"next: list the folder with the Drive connector (search_files parentId = '{rec['folder_id']}'), save the "
          f"result, then: vs deliver verify {a.project} <saved listing>")
    sys.exit(1 if bad else 0)


def listing_files(data):
    if isinstance(data, dict):
        data = data.get("files", data.get("items", []))
    out = {}
    for x in data or []:
        name = x.get("title") or x.get("name")
        size = x.get("fileSize", x.get("size"))
        if name is not None and size is not None:
            out.setdefault(name, []).append(int(size))
    return out


def cmd_verify(a):
    pdir = project_dir(a.project)
    d, plan = plan_for(pdir, a.id)
    have = listing_files(load_json(Path(a.listing)))
    bad = 0
    for f in plan["files"]:
        sizes = have.get(f["name"], [])
        if f["size"] in sizes:
            print(f"ok    {f['name']}  {f['size']} bytes" + (f"  (and {len(sizes) - 1} other copy)" if len(sizes) > 1 else ""))
        else:
            print(f"WRONG {f['name']}: " + (f"Drive has {sizes}, sent {f['size']}" if sizes else "not in the folder")); bad += 1
    rec_p = d / "delivered.json"
    if rec_p.exists():
        rec = load_json(rec_p)
        rec["verified"] = not bad
        save_json(rec_p, rec)
    log_line(pdir, f"- verify {plan['id']}: " + ("all files in Drive at full size" if not bad else f"{bad} file(s) wrong"))
    print("verified: every file is in Drive at full size" if not bad else f"{bad} file(s) missing or wrong size")
    sys.exit(1 if bad else 0)


def main():
    ap = argparse.ArgumentParser(prog="vs deliver", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("setup", help="save a Drive delivery target and write its Apps Script")
    s.add_argument("folder", help="Drive folder link or id (the parent of every delivery folder)")
    s.add_argument("--name", required=True, help="short name for this target, e.g. the client")
    s.add_argument("--root-name", help="the folder's name as shown in Drive (for messages)")
    s.add_argument("--default", action="store_true", help="make it the default target")
    sub.add_parser("targets", help="list delivery targets")
    i = sub.add_parser("inbox", help="remember a target's inbox folder id")
    i.add_argument("target"); i.add_argument("inbox_id")
    p = sub.add_parser("plan", help="pick the latest version of each file and write the request")
    p.add_argument("project"); p.add_argument("--to", help="delivery target (default: the default target)")
    p.add_argument("--dir", help="folder holding the finished files (default out/ads, else out)")
    p.add_argument("--files", nargs="+", help="deliver exactly these files")
    p.add_argument("--folder", help="Drive folder name (default: the files' common name)")
    p.add_argument("--allow-old", action="store_true", help="allow a file that has a newer version beside it")
    u = sub.add_parser("upload", help="upload to the links in the script's answer")
    u.add_argument("project"); u.add_argument("res", help="res_<id>.json saved from the inbox"); u.add_argument("--id")
    v = sub.add_parser("verify", help="check a Drive listing against what was sent")
    v.add_argument("project"); v.add_argument("listing", help="search_files output for the delivery folder, saved as JSON")
    v.add_argument("--id")
    a = ap.parse_args()
    {"setup": cmd_setup, "targets": cmd_targets, "inbox": cmd_inbox, "plan": cmd_plan,
     "upload": cmd_upload, "verify": cmd_verify}[a.cmd](a)


if __name__ == "__main__":
    main()
