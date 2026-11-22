#!/usr/bin/env python3
"""API keys for video-studio, per machine or per project.

Different projects often bill different accounts (one client's ElevenLabs, another's), so a
key can be saved for one project and it overrides the machine-wide key there.

  vs keys ask elevenlabs --project acme      pop-up window with a hidden field (key never shown)
  vs keys set elevenlabs --project acme      same, typed in the terminal (hidden prompt)
  vs keys check elevenlabs --project acme    exit 0 if a key is available; says where it comes from
  vs keys exec --project acme -- <command>   run a command with that project's keys in its environment
  vs keys list [--project acme]              what's set (last 4 characters only)
  vs keys unset elevenlabs --project acme

Without --project the key is machine-wide. Inside <workspace>/projects/<name>/ the project is
picked up automatically. Lookup order: project key, then the environment variable, then the
machine-wide key. Keys are never printed, only "…" plus the last 4 characters.

Files: machine-wide ~/.config/video-studio/keys.env, per project
~/.config/video-studio/projects/<name>.env (both 0600, outside the workspace so they are never
committed). $VS_KEYS_DIR moves both.
"""
import argparse
import getpass
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path

# provider -> (env var, what it is for, where to get it)
PROVIDERS = {
    # audio and voice (paid; often a different account per project)
    "elevenlabs": ("ELEVENLABS_API_KEY", "voiceover, voice cloning, dubbing", "elevenlabs.io → Profile → API keys"),
    "heygen": ("HEYGEN_API_KEY", "voiceover with word timestamps, avatars", "app.heygen.com → Settings → API"),
    "openai": ("OPENAI_API_KEY", "voiceover (TTS), transcription", "platform.openai.com → API keys"),
    "gemini": ("GEMINI_API_KEY", "music beds (Lyria), TTS", "aistudio.google.com → Get API key"),
    # client footage libraries (vs learn)
    "gdrive": ("GOOGLE_DRIVE_API_KEY", "list and read Google Drive folders fast (vs learn)",
               "console.cloud.google.com → APIs & Services → Credentials → API key (enable Drive API)"),
    "dropbox": ("DROPBOX_TOKEN", "list Dropbox shared folders without downloading the zip (vs learn)",
                "dropbox.com/developers/apps → your app → Generate access token"),
    # stock media (free)
    "pexels": ("PEXELS_API_KEY", "stock video and photos", "pexels.com/api"),
    "pixabay": ("PIXABAY_API_KEY", "stock video, photos, music", "pixabay.com/api/docs"),
    "unsplash": ("UNSPLASH_ACCESS_KEY", "stock photos", "unsplash.com/developers"),
    "freesound": ("FREESOUND_API_KEY", "sound effects", "freesound.org/apiv2/apply"),
    "jamendo": ("JAMENDO_CLIENT_ID", "music", "devportal.jamendo.com"),
}
AUDIO = ("elevenlabs", "heygen", "openai", "gemini")


def die(msg, code=1):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def keys_dir():
    d = os.environ.get("VS_KEYS_DIR")
    if d:
        return Path(d)
    f = os.environ.get("VS_KEYS_FILE")  # older override, kept working
    return Path(f).parent if f else Path.home() / ".config" / "video-studio"


def global_file():
    f = os.environ.get("VS_KEYS_FILE")
    return Path(f) if f and not os.environ.get("VS_KEYS_DIR") else keys_dir() / "keys.env"


def project_file(project):
    return keys_dir() / "projects" / f"{project}.env"


def read_env(path):
    out = {}
    if path.exists():
        for line in path.read_text().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                out[k.strip()] = v.strip().strip('"')
    return out


def write_env(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    os.chmod(path.parent, 0o700)
    path.write_text("".join(f"{k}={v}\n" for k, v in data.items()))
    os.chmod(path, 0o600)


def detect_project(explicit):
    """--project, else the folder name when the current directory is inside <...>/projects/<name>/."""
    if explicit:
        if not re.fullmatch(r"[A-Za-z0-9._-]+", explicit):
            die("project name may only use letters, digits, '.', '_' and '-'")
        return explicit
    parts = Path.cwd().resolve().parts
    for i in range(len(parts) - 2, -1, -1):
        if parts[i] == "projects" and i + 1 < len(parts):
            return parts[i + 1]
    return None


def mask(v):
    return "…" + v[-4:] if len(v) >= 8 else "…"


def resolve(provider, project):
    """(value, source) using project key > environment variable > machine-wide key."""
    env = PROVIDERS[provider][0]
    if project:
        v = read_env(project_file(project)).get(env)
        if v:
            return v, f"project {project}"
    if os.environ.get(env):
        return os.environ[env], f"environment ${env}"
    v = read_env(global_file()).get(env)
    if v:
        return v, "machine-wide"
    return None, None


def need_provider(p):
    if p not in PROVIDERS:
        die(f"unknown provider '{p}'. Known: {', '.join(PROVIDERS)}")


def dialog(provider, project):
    """Ask for the key in a native pop-up with a hidden field. Returns the key, '' if cancelled,
    None if no pop-up is possible here (no desktop session)."""
    env, use, where = PROVIDERS[provider]
    scope = f"project “{project}”" if project else "this computer (all projects)"
    msg = f"{provider.capitalize()} API key for {scope}.\n\nUsed for: {use}.\nGet it at: {where}."
    custom = os.environ.get("VS_KEYS_DIALOG_CMD")  # tests / custom prompt helpers: prints the key
    if custom:
        cmd = custom.split()
    elif platform.system() == "Darwin" and shutil.which("osascript"):
        esc = msg.replace("\\", "\\\\").replace('"', '\\"')
        cmd = ["osascript", "-e",
               f'text returned of (display dialog "{esc}" default answer "" with hidden answer '
               f'with title "video-studio" buttons {{"Cancel", "Save"}} default button "Save" with icon note)']
    elif (platform.system() == "Windows" or os.environ.get("WSL_DISTRO_NAME")) and shutil.which("powershell.exe"):
        ps_msg = msg.replace("'", "''")
        cmd = ["powershell.exe", "-NoProfile", "-Command",
               f"$c = Get-Credential -UserName '{provider}' -Message '{ps_msg}'; "
               "if ($c) { $c.GetNetworkCredential().Password }"]
    elif os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY"):
        if shutil.which("zenity"):
            cmd = ["zenity", "--password", "--title", f"video-studio: {provider} API key"]
        elif shutil.which("kdialog"):
            cmd = ["kdialog", "--title", "video-studio", "--password", msg]
        else:
            return None
    else:
        return None
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return p.stdout.strip() if p.returncode == 0 else ""


def save(provider, project, value):
    env = PROVIDERS[provider][0]
    path = project_file(project) if project else global_file()
    data = read_env(path)
    data[env] = value.strip()
    write_env(path, data)
    print(f"{provider}: saved for {'project ' + project if project else 'this computer'} ({mask(value.strip())})")


def cmd_ask(a, project):
    need_provider(a.provider)
    if not a.force:
        v, src = resolve(a.provider, project)
        if v and (src.startswith("project") or not project):
            print(f"{a.provider}: already set ({src}, {mask(v)}); use --force to replace it")
            return
    v = dialog(a.provider, project)
    if v is None:
        target = f" --project {project}" if project else ""
        die(f"no pop-up window is available here (no desktop session). Ask the person to run this in their "
             f"own terminal, where the key is typed hidden:\n  ! vs keys set {a.provider}{target}\n"
             f"In a Claude Code cloud session, use the secure credential form instead (the key is attached by "
             f"the network proxy and never enters the session).", 3)
    if not v:
        die("cancelled; no key saved", 2)
    save(a.provider, project, v)


def cmd_set(a, project):
    need_provider(a.provider)
    v = a.value or (sys.stdin.readline().strip() if not sys.stdin.isatty()
                    else getpass.getpass(f"{PROVIDERS[a.provider][0]} (hidden): "))
    if not v:
        die("empty key")
    save(a.provider, project, v)


def cmd_unset(a, project):
    need_provider(a.provider)
    path = project_file(project) if project else global_file()
    data = read_env(path)
    data.pop(PROVIDERS[a.provider][0], None)
    write_env(path, data)
    print(f"{a.provider}: removed from {'project ' + project if project else 'this computer'}")


def cmd_check(a, project):
    need_provider(a.provider)
    v, src = resolve(a.provider, project)
    if v:
        print(f"{a.provider}: available ({src}, {mask(v)})")
        return
    hint = f" --project {project}" if project else ""
    print(f"{a.provider}: missing. Ask for it with:  vs keys ask {a.provider}{hint}")
    sys.exit(1)


def cmd_list(a, project):
    print(f"keys for {'project ' + project if project else 'this computer'} "
          f"(project > environment > machine-wide):")
    for p, (env, use, _) in PROVIDERS.items():
        v, src = resolve(p, project)
        state = f"set   {mask(v)}  ({src})" if v else "not set"
        print(f"  {p:10} {state:42} {use}")
    print("no key needed: openverse, archive, wikipedia, wikimedia, youtube (CC), incompetech, ccmixter, nasa, kokoro")


def cmd_exec(a, project):
    if not a.command:
        die("usage: vs keys exec [--project P] -- <command> [args]")
    env = dict(os.environ)
    for p, (var, _, _) in PROVIDERS.items():
        v, _ = resolve(p, project)
        if v:
            env[var] = v
    os.execvpe(a.command[0], a.command, env)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("action", choices=["ask", "set", "unset", "check", "list", "exec"])
    ap.add_argument("provider", nargs="?")
    ap.add_argument("value", nargs="?", help="set: omit to be prompted (keeps it out of shell history)")
    ap.add_argument("--project", help="save/look up the key for this project only")
    ap.add_argument("--force", action="store_true", help="ask: replace an existing key")
    argv = sys.argv[1:]
    cmd = []
    if "--" in argv:
        i = argv.index("--")
        argv, cmd = argv[:i], argv[i + 1:]
    a = ap.parse_args(argv)
    a.command = cmd
    if a.action not in ("list", "exec") and not a.provider:
        die(f"usage: vs keys {a.action} <provider> [--project P]")
    if a.action == "exec" and a.provider:  # `vs keys exec cmd ...` without `--`
        a.command = [a.provider] + ([a.value] if a.value else []) + a.command
    project = detect_project(a.project)
    {"ask": cmd_ask, "set": cmd_set, "unset": cmd_unset, "check": cmd_check,
     "list": cmd_list, "exec": cmd_exec}[a.action](a, project)


if __name__ == "__main__":
    main()
