# WilloMD Drive delivery (all RootOut / WilloMD ads)

Every approved WilloMD ad is delivered into the **WilloMD** Google Drive folder, one subfolder per ad, with the latest
version of every hook and size. Plugin: `vs deliver` + the `video-delivery` skill.

- Parent folder: **WilloMD** `1m2sQXAQhtQNiO8CGfr6fy2akLstLjUv7`
  (https://drive.google.com/drive/folders/1m2sQXAQhtQNiO8CGfr6fy2akLstLjUv7)
- Inbox: `WilloMD/_claude_uploads` `1lu-C8LikH2zp4jDXRKbC0Ot2DI5CBZod` (also `inbox_id` in `video-studio/style/delivery.json`).
- Apps Script: `Code.gs` + `appsscript.json` here (same as `video-studio/delivery/willomd/`), installed once by the
  folder owner; it answers requests every minute.
- Subfolder name = the ad's master name without the hook/size/version suffix, e.g. `WilloMD_RootOut_Set4`
  (files `WilloMD_RootOut_Set4_H1_9x16_v3.mp4` ...).

## In any WilloMD session (Sets 4, 5, 13, 17, 18, 19, 20 and every future WilloMD ad)
The target is already saved in `video-studio/style/delivery.json` (default `willomd`), so no setup is needed:
```bash
vs deliver targets                      # shows willomd
vs deliver plan <project> --to willomd  # latest _vN of each file -> req_<id>.json
```
then follow the `video-delivery` skill (create_file the request in the inbox, wait for res_<id>.json,
`vs deliver upload`, `vs deliver verify`, `vs task deliver <CODE> --link <folder url>`).

Rules: deliver **only after the person says the ad is approved**; only the newest `_vN` of every hook/size, from the
session that made it (never copies from another container); check every file's size in Drive; never put an email
address in a request, folder name or log.
