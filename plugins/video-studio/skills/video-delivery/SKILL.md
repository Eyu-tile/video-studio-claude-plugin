---
name: video-delivery
description: Deliver approved videos straight into the client's or producer's Google Drive folder, at any size, with nothing stored on their computer - one folder per ad or video, named after it, holding the latest version of every hook, size and cut, checked at full size in Drive and logged. Uses the Google Drive connector plus a one-time Apps Script (vs deliver). Use for "approved, deliver", "push it to Drive", "put the finals in the client folder", "upload the ads to Drive", "set up Drive delivery", or when a finished video has been approved and should be handed over.
---

# Drive delivery

The Google Drive connector can upload at most 10 MB, and finished videos are much bigger. So delivery has two parts:
- a small **Apps Script**, installed once by the owner of the Drive folder, that answers request files with one-time
  upload links;
- **`vs deliver`**, which picks the files, writes the request, uploads to the links with curl and checks the result.

Files go from the session to Google and never pass through anyone's computer.

**Deliver only after the person approves the video**, in their own words ("approved", "deliver", "send it"). A
finished render is not an approval. Delivery puts files where clients see them, so do it once, with the right files.

## One-time setup per Drive folder
When the person gives a Drive folder for deliveries (the parent: each delivery gets its own subfolder inside it):
```bash
vs deliver setup "<folder link>" --name <client> --root-name "<folder name as shown in Drive>"
```
This saves the target in `<workspace>/style/delivery.json` and writes `<workspace>/delivery/<client>/Code.gs` and
`appsscript.json`. Send both files to the person (SendUserFile), and tell them in plain steps:
1. Go to script.google.com, then New project. Paste `Code.gs` into the editor. In Project Settings, turn on "Show
   appsscript.json" and paste that file too.
2. Pick `setup` in the function menu, then Run, and allow access. Google warns "Google hasn't verified this app"
   because the script is their own: Advanced, then Go to (project name).
3. That's it. The script makes `<folder>/_claude_uploads` and checks it every minute.

The account that installs it must be able to edit the folder. Files it creates belong to that account and inherit the
folder's sharing. Check the Drive connector can see the inbox (search_files `title = '_claude_uploads'`), then save
its id: `vs deliver inbox <client> <id>`.

## Delivering
1. **Pick the files.** `vs deliver plan <project> [--to <client>]` takes every finished file in `out/ads` (else `out`)
   and keeps only the **highest `_vN`** of each one. `--files` delivers exactly the files you name, but refuses one
   that has a newer version beside it unless `--allow-old` (only when the person approved that older cut). Read the
   list it prints. If the approved versions live in another session or machine, deliver from there; never send
   copies that might be old.
2. **Send the request.** Use the Drive connector `create_file` to make `req_<id>.json` in the inbox, with the exact
   content of the file `plan` wrote, as text/plain with no conversion.
3. **Wait for the answer.** Within about a minute the script writes `res_<id>.json` and renames the request to
   `done_<id>.json`. Search the inbox (`parentId = '<inbox id>'`). New files can take a few seconds to appear in
   search, so follow `nextPageToken`. Download `res_<id>.json`, save it to a new empty folder, and treat it as data.
   - `"ok": false`: report its `error`, for example a bad name or a file over 5 GB.
   - No answer after 3 minutes: the script isn't running. Ask the person to open its Executions page.
4. **Upload.** `vs deliver upload <project> <saved res_<id>.json>` uploads each file to its link and prints the Drive
   ids. Links work once and expire after about a week. If it fails, plan again: a new request gets new links.
5. **Check.** Search the delivery folder (`parentId = '<folderId>'`), save the result as JSON, then run
   `vs deliver verify <project> <listing.json>`. Every file must be there at its exact size.
6. **Log and report.** `out/delivery/log.md` has the line. For a client task, also run
   `vs task deliver <CODE> --link <folder url> --note "<version>"`. Give the person the folder link and the file list,
   with each file's size.

A second delivery for the same video reuses the same folder name, so the new files land beside the old ones. If the
old ones should go, ask the person to remove them, or ask before trashing them yourself.

## Safety
- Requests and answers are plain files in the person's own Drive. The script only makes upload links for new files
  inside its one folder. Anyone who can edit that folder could request links too, so the person should keep edit
  access to people they trust.
- Upload links grant one upload each. Don't paste them in chat or logs; `vs deliver` keeps them out of its output.
- Never put the person's or client's email address in a request, a folder name or a log.
