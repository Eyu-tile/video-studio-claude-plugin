# Deliver approved ads straight to Google Drive (no local copy, any size)

The Google Drive connector can only upload files up to 10 MB. Finished ads are 80-100 MB, so delivery uses a small
Apps Script ("Hume ad delivery", `Code.gs` + `appsscript.json` here). The producer installs it once in their Google
account. It creates one-time upload links and the session uploads the files to them from the cloud with curl.
Nothing passes through the producer's computer.

- Parent folder: **Hume_4Kiru** `1z_-7kEauhnZY9q_S8MYDpnxn5QiRcdvN`. Inbox: `Hume_4Kiru/_claude_uploads` `1lR3Oie_izwJYQIgpounLa67klwnUR3Fr`.
- The script runs every minute (setup() made the trigger). Files and folders it creates belong to the Google account that
  installed it and inherit Hume_4Kiru's sharing.

## Steps (only after the producer says the ad is approved)
1. Use the Drive connector `create_file` (text/plain, disableConversion) to write `req_<id>.json` into the inbox. `<id>` may contain letters, digits, `_` and `-`:
   `{"folder": "<ad name, i.e. the master file name without _H1_9x16_v1.mp4>", "files": [{"name": "<file>.mp4", "size": <bytes>, "mime": "video/mp4"}, ...]}`
   List every file to deliver (all hooks, all sizes). Sizes must be exact (`stat -c %s`).
   **Deliver only the latest approved version** (the newest `_vN` of each hook and size, the one on the review page the producer approved). Never take the files from another session's container, because its copies can be old.
2. Within about a minute the script creates the folder under Hume_4Kiru (or reuses one with that name), writes `res_<id>.json` and renames
   the request to `done_<id>.json`. Search `parentId = '<inbox>'` (new files can take a few seconds to show; follow
   `nextPageToken`). Download `res_<id>.json` and save it to a new empty folder in the scratchpad.
3. `python3 -I tools/drive_delivery/upload_sessions.py RES.json FILE [FILE ...]`. It prints a Drive file id per file.
   Links work once each and expire after about a week.
4. Check with `search_files parentId = '<folderId>'` that every file is there and `fileSize` equals the local size.
5. Log the folder link in `comments/<project>.md` and give it to the producer.

`res` with `"ok": false` carries the error, for example a bad name or a file over 5 GB. If no answer comes within 3 minutes,
ask the producer to open the script's Executions page.

First run: 2026-11-22, Band 2.0 Biological Age H1-H3 (279 MB). The answer came in 50 s and the upload took 16 s; all sizes matched. That test sent the **v1** files, which had already been replaced by v5. The method worked, but those were the wrong files: always check the version first.
