// Hume ad delivery helper. Lets Claude upload finished ads of any size into the Hume_4Kiru folder.
//
// How it works: Claude drops a small request file into Hume_4Kiru/_claude_uploads (through the Google Drive
// connection you already gave it). Every minute this script reads new requests and answers each one with a one-time
// upload link per file: a Google Drive "resumable upload session" for exactly one new file in the named ad folder.
// Your Drive login never leaves Google. An upload link can only upload that one file, and it expires after a week.
// Anyone who can edit Hume_4Kiru could ask for upload links too, so keep edit access to people you trust.
//
// Setup: paste this file and appsscript.json into a new Apps Script project, then run setup() once and allow access.

const ROOT_FOLDER_ID = '1z_-7kEauhnZY9q_S8MYDpnxn5QiRcdvN';   // Hume_4Kiru
const INBOX_NAME = '_claude_uploads';
const MAX_BYTES = 5 * 1024 * 1024 * 1024;                     // 5 GB per file

function setup() {
  inbox_();
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'processRequests') ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('processRequests').timeBased().everyMinutes(1).create();
  processRequests();
  Logger.log('Ready: requests in Hume_4Kiru/' + INBOX_NAME + ' are answered every minute.');
}

function inbox_() {
  var root = DriveApp.getFolderById(ROOT_FOLDER_ID);
  var it = root.getFoldersByName(INBOX_NAME);
  return it.hasNext() ? it.next() : root.createFolder(INBOX_NAME);
}

function cleanName_(s, what) {
  s = String(s || '').trim();
  if (!s || s.length > 200 || /[\/\\]/.test(s) || s.charAt(0) === '.') throw new Error('bad ' + what + ': ' + s);
  return s;
}

function processRequests() {
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(5000)) return;
  try {
    var inbox = inbox_();
    var root = DriveApp.getFolderById(ROOT_FOLDER_ID);
    var files = inbox.getFiles();
    while (files.hasNext()) {
      var f = files.next();
      var m = f.getName().match(/^req_([A-Za-z0-9_-]{1,64})\.json$/);
      if (!m) continue;
      var id = m[1], res;
      try {
        var req = JSON.parse(f.getBlob().getDataAsString());
        var folderName = cleanName_(req.folder, 'folder');
        var it = root.getFoldersByName(folderName);
        var target = it.hasNext() ? it.next() : root.createFolder(folderName);
        var uploads = (req.files || []).slice(0, 50).map(function (x) {
          var name = cleanName_(x.name, 'file name');
          var size = Number(x.size);
          if (!(size > 0 && size <= MAX_BYTES)) throw new Error('bad size for ' + name);
          var mime = /^[a-z]+\/[a-z0-9.+-]+$/i.test(x.mime || '') ? x.mime : 'application/octet-stream';
          return {name: name, size: size, uploadUrl: session_(name, mime, size, target.getId())};
        });
        res = {ok: true, folderId: target.getId(), folderUrl: target.getUrl(), uploads: uploads, at: new Date().toISOString()};
      } catch (e) {
        res = {ok: false, error: String((e && e.message) || e), at: new Date().toISOString()};
      }
      inbox.createFile('res_' + id + '.json', JSON.stringify(res, null, 1), MimeType.PLAIN_TEXT);
      f.setName('done_' + id + '.json');
    }
  } finally {
    lock.releaseLock();
  }
}

function session_(name, mime, size, parentId) {
  var r = UrlFetchApp.fetch('https://www.googleapis.com/upload/drive/v3/files?uploadType=resumable&supportsAllDrives=true', {
    method: 'post',
    contentType: 'application/json; charset=UTF-8',
    muteHttpExceptions: true,
    headers: {
      Authorization: 'Bearer ' + ScriptApp.getOAuthToken(),
      'X-Upload-Content-Type': mime,
      'X-Upload-Content-Length': String(size)
    },
    payload: JSON.stringify({name: name, parents: [parentId]})
  });
  if (r.getResponseCode() !== 200) {
    throw new Error('Drive refused the upload (' + r.getResponseCode() + '): ' + r.getContentText().slice(0, 200));
  }
  var h = r.getAllHeaders();
  return h.Location || h.location;
}
