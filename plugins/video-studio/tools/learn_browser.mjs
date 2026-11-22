// Reads a share page in headless Chromium and prints JSON on stdout. Used by `vs learn` for sources without an API.
//   node learn_browser.mjs frameio <share link>  -> [{id, name, path, dl, size}]  (walks into folders)
//   node learn_browser.mjs web <page link>       -> [{url, name}]  (videos/images linked or played on the page)
import { createRequire } from "module";
const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

const [mode, link] = process.argv.slice(2);
const MEDIA = /\.(mp4|mov|m4v|webm|mkv|avi|jpe?g|png|webp|gif|heic)(\?|$)/i;

async function scrollAll(p) {
  await p.evaluate(() => {
    let best = null, gap = 0;
    document.querySelectorAll("*").forEach((e) => {
      const d = e.scrollHeight - e.clientHeight;
      if (d > gap && e.clientHeight > 300) { gap = d; best = e; }
    });
    if (best) best.setAttribute("data-vs-scroll", "1");
  });
  let prev = -1, same = 0;
  for (let i = 0; i < 400 && same < 5; i++) {
    const top = await p.evaluate(() => {
      const e = document.querySelector('[data-vs-scroll="1"]') || document.scrollingElement;
      e.scrollTop += 700; return e.scrollTop;
    });
    await p.waitForTimeout(1300); // download links arrive as the list hydrates
    same = top === prev ? same + 1 : 0; prev = top;
  }
}

async function frameio(p) {
  const A = {};
  let cur = "";
  const ingest = (o) => {
    if (!o || typeof o !== "object") return;
    if (Array.isArray(o)) { o.forEach(ingest); return; }
    if (o.id && o.__typename && /Asset$/.test(o.__typename)) {
      const a = A[o.id] || { id: o.id, path: cur };  // folder = where it was first seen
      a.type = o.__typename;
      if (o.name) a.name = o.name;
      if (o.filesize || o.fileSize) a.size = o.filesize || o.fileSize;
      const dl = o.media && o.media.original && o.media.original.downloadUrl;
      if (dl) a.dl = dl.replace(/\\u0026/g, "&");
      A[o.id] = a;
    }
    for (const k in o) ingest(o[k]);
  };
  p.on("response", async (r) => {
    if (r.url().includes("/graphql") && r.request().method() === "POST") {
      try { ingest(JSON.parse(await r.text())); } catch (e) { /* not JSON */ }
    }
  });
  const done = new Set();
  const visit = async (path, depth) => {
    cur = path;
    await p.waitForTimeout(3000);
    await scrollAll(p);
    await p.waitForTimeout(2000);
    if (depth >= 4) return;
    const folders = Object.values(A).filter((a) => a.type === "FolderAsset" && a.name && a.path === path
                                            && !done.has(a.id));
    for (const f of folders) {
      done.add(f.id);
      try { await p.locator(`text="${f.name}"`).first().dblclick({ timeout: 8000 }); } catch (e) { continue; }
      await visit(path ? `${path}/${f.name}` : f.name, depth + 1);
      cur = path;
      await p.goBack().catch(() => {});
      await p.waitForTimeout(2500);
    }
  };
  await p.goto(link, { waitUntil: "networkidle", timeout: 90000 }).catch(() => {});
  await visit("", 0);
  return Object.values(A).filter((a) => a.dl && a.name)
    .map(({ id, name, path, dl, size }) => ({ id, name, path, dl, size }));
}

async function web(p) {
  const seen = new Map();
  p.on("response", (r) => {
    const ct = (r.headers()["content-type"] || "").toLowerCase();
    const len = parseInt(r.headers()["content-length"] || "0", 10);
    if ((ct.startsWith("video/") || (ct.startsWith("image/") && len > 200000)) && !seen.has(r.url()))
      seen.set(r.url(), { url: r.url(), size: len || undefined });
  });
  await p.goto(link, { waitUntil: "networkidle", timeout: 90000 }).catch(() => {});
  await scrollAll(p);
  const dom = await p.evaluate((re) => {
    const rx = new RegExp(re, "i"), o = [];
    document.querySelectorAll("video[src], video source[src], a[href], img[src]").forEach((e) => {
      const u = e.src || e.href;
      if (u && rx.test(u)) o.push({ url: u, name: (e.getAttribute("download") || e.textContent || "").trim().slice(0, 120) });
    });
    return o;
  }, MEDIA.source);
  for (const d of dom) if (!seen.has(d.url)) seen.set(d.url, d);
  return [...seen.values()].filter((x) => x.url.startsWith("http"));
}

const b = await chromium.launch({ args: ["--no-sandbox"] });
try {
  const p = await (await b.newContext({ viewport: { width: 1280, height: 1200 } })).newPage();
  const res = mode === "frameio" ? await frameio(p) : await web(p);
  process.stdout.write(JSON.stringify(res));
} finally {
  await b.close();
}
