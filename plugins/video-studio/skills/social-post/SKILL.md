---
name: social-post
description: Post a finished video to TikTok, Instagram Reels, YouTube / Shorts, LinkedIn or X through Composio - prepare one upload per platform, write platform captions, check every limit, get the person's approval of the exact plan, post, and log the links. Offer it at the end of EVERY finished task, together with the review page. Use for "post this", "publish to TikTok/Instagram/YouTube", "share it on social", "schedule the posts", or when an approved video should go live.
---

# Social posting

Posting is public and hard to undo. **Nothing is posted without the person's explicit "yes" to the exact plan**:
platform, account, file, caption/title and privacy. "Yes, prepare posts" at the end of a task is not that approval.

## At the end of every finished task: one question set
After a finished task (final render, `vs task deliver`, export, ad batch), check both standing answers:
```bash
vs present pref    # review page: ask | always | never
vs social pref     # posting: ask | never
```
Ask everything still at `ask` in ONE AskUserQuestion call (up to two questions, so the person answers once):
- "Review page" (see `/video-review`).
- "Social": "Post <file name> to social media?" with options **Not now** ("Finish here.") ·
  **Yes, prepare posts** ("I'll prepare a file and caption per platform for you to approve; nothing posts without
  your OK.") · **Never ask** ("Don't offer posting." then `vs social pref never`).

Client work: posting to a client's accounts needs the client's approval of the final cut (`vs task` shows whether it
was approved); if it wasn't, say so instead of preparing posts.

## 1. Set up once (per machine)
`vs setup --social` installs Composio's `composio` skill for Claude Code
(`npx skills add ComposioHQ/composio --skill composio --agent claude-code --global`). Composio does the posting:
- Terminal Claude Code: the Composio CLI (`curl -fsSL https://composio.dev/install | bash`, then `composio login`;
  `composio login --no-wait` gives a login link when no browser opens here). Ask before installing it.
- claude.ai / Claude Desktop: Composio's MCP server (`https://connect.composio.dev/mcp`, browser sign-in).
Follow the `composio` skill for setup details; never put a Composio key in chat or in a file in the workspace.

## 2. Prepare
Ask which platforms (AskUserQuestion, multiSelect: TikTok, Instagram Reels, YouTube Shorts, YouTube, LinkedIn, X), then:
```bash
vs social prep $P/out/final.mp4 --project <P> --platforms tiktok,reels,shorts [--task <CODE>] --version <v> --title "<name>"
```
`out/social/<version>/` gets the upload file (H.264/AAC MP4, re-encoded only if needed), `cover.jpg`, `post.json`
and `post_plan.md`. File problems are listed per platform (too long, wrong aspect, too big). Fix those by cutting or
rendering a platform version (`vs render ... --preset tiktok|reels|shorts|x|linkedin`) and re-running prep, or by
dropping that platform; never stretch or crop silently. If the person accepts letterboxing (say a 16:9 film on
Reels), set `"accept_aspect": true` on that platform in post.json; length and size limits cannot be waived.

Write the captions into `post.json` yourself, one per platform, from the brief and transcript: the hook in the first
line, the platform's register (TikTok/Reels short and native, LinkedIn a few plain sentences, X under 280 with links
counted as 23, YouTube a title ≤ 100 plus a description). Hashtags: a few specific ones (Instagram allows 30, use far
fewer). Credit lines from `assets/CREDITS.md` go in the caption or description where a licence requires them.
Then `vs social check $P/out/social/<v>/post.json` until every platform says ready (exit 0).

## 3. Confirm the accounts, then the plan
- Connect each platform through Composio (it returns a Connect Link when the account isn't linked). Discover the tool
  slugs at runtime (`composio search "upload a video to tiktok"`); never invent them. Read the connected account's
  name with a read-only tool (e.g. the platform's user-info tool) and write it into `post.json` as `account`.
- Instagram takes only a **public direct URL** to the MP4 (MP4/MOV, ≤ 100 MB, ≥ 3 s; Business or Creator account):
  ask where to host it (their S3, R2, Cloudinary...). A Drive link or a private claude.ai page will not work. Put the
  URL in `post.json` as `public_url`.
- YouTube defaults to `private`; TikTok to `SELF_ONLY`. Change privacy only when the person says so.
- Show `post_plan.md` and ask one AskUserQuestion: "Post these N posts now?" listing platform → account → privacy.
  Only "yes" posts. Changes → edit post.json → check → ask again.

## 4. Post and log
Run the platform's upload/publish tools through Composio one platform at a time, in the order shown in the plan:
- TikTok: upload, then poll the publish status with backoff (5 s → 10 s → 20 s); never re-post the same publish id.
- Instagram: create the Reels container from `public_url`, poll its status until FINISHED, then publish.
- LinkedIn: upload, wait until the video is AVAILABLE, then create the video post with the commentary.
- X: chunked media upload (init, append, finalize, wait for processing), then the post.
- YouTube: upload with title, description, privacy.
After each success: `vs social log $P/out/social/<v>/post.json <platform> --url <post url> [--id <id>]` (also
recorded on the client task). A failure: get Composio's log or request id, read the `composio` skill's error guide,
fix that step, and retry only that platform. Report each link at the end.

TikTok alternative: when the Higgsfield MCP is connected, its `tiktok_accounts` / `tiktok_prepare_publish` /
`tiktok_publish_status` tools post to TikTok too; the same approval rule applies.
