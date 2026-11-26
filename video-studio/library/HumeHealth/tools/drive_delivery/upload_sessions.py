# upload_sessions.py RES.json FILE [FILE ...]
# Upload finished ads straight into Google Drive with the one-time upload links that the "Hume ad delivery" Apps Script
# wrote into RES.json (Hume_4Kiru/_claude_uploads/res_<id>.json, read with the Google Drive connector and saved locally).
# Each link accepts exactly one new file of the declared size. Files are matched to links by file name.
# Prints one line per file: name, bytes, Drive file id (or the error). Exit 1 if any upload failed.
import json, os, subprocess, sys

res = json.load(open(sys.argv[1]))
if not res.get("ok"):
    sys.exit("request failed: " + str(res.get("error")))
links = {u["name"]: u for u in res["uploads"]}
bad = 0
for path in sys.argv[2:]:
    name = os.path.basename(path)
    u = links.get(name)
    if not u:
        print(f"{name}: no upload link in the response"); bad += 1; continue
    size = os.path.getsize(path)
    if size != int(u["size"]):
        print(f"{name}: size {size} differs from the requested {u['size']}"); bad += 1; continue
    r = subprocess.run(["curl", "-sS", "--fail-with-body", "-X", "PUT", "--upload-file", path,
                        "-H", "Content-Type: video/mp4", "--retry", "3", "--retry-delay", "5", u["uploadUrl"]],
                       capture_output=True, text=True)
    try:
        j = json.loads(r.stdout)
        print(f"{name}: {size} bytes -> Drive file {j['id']}")
    except Exception:
        print(f"{name}: upload failed ({r.returncode}) {r.stdout[-300:]} {r.stderr[-300:]}"); bad += 1
print("folder:", res.get("folderUrl"))
sys.exit(1 if bad else 0)
