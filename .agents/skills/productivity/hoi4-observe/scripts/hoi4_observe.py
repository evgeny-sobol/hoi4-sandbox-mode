#!/usr/bin/env python3
"""Unattended observer session: launch, monitor to a target year, kill, report.

See ../SKILL.md. Random sessions only; the launcher playset must already
hold the mod under test. Windows-only (taskkill, DETACHED_PROCESS).
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

GAME_DIR = Path(r"C:\Games\Steam\steamapps\common\Hearts of Iron IV")
DOCS = Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV")
LOG_DIR = DOCS / "logs"
MODS = {
    "sandbox": DOCS / "mod" / "_sandbox",
    "rt56": DOCS / "mod" / "_sandbox-r56",
}
DESCRIPTORS = {
    "sandbox": "mod/_sandbox.mod",
    "rt56": "mod/_sandbox-r56.mod",
}
SAVES_DIR = DOCS / "save games"
DATE_RE = re.compile(r"\[(\d{4})\.(\d{2})\.(\d{2})\.\d{2}\]")


def clear_dir(path: Path) -> int:
    """Delete everything inside path (files and subdirs); return entry count."""
    count = 0
    if not path.is_dir():
        return 0
    for entry in list(path.iterdir()):
        if entry.is_dir() and not entry.is_symlink():
            shutil.rmtree(entry, ignore_errors=True)
        else:
            try:
                entry.unlink()
            except OSError:
                continue
        count += 1
    return count
KEY_RE = re.compile(r"\b(sc_seed|sc_pick|sc_repick|sc_variant|sc_phase|sc_derail|sc_end|sc_ignite|sc_success|sc_crisis|sc_target|sc_offer|sc_join)\b")
ERR_RE = re.compile(r"sandbox|scenario|completion_reward|Else/else if", re.IGNORECASE)


class Fail(Exception):
    pass


def newest_year(log: Path, tail_lines: int = 60) -> int | None:
    try:
        with log.open("r", encoding="utf-8", errors="replace") as fh:
            tail = fh.readlines()[-tail_lines:]
    except OSError:
        return None
    years = [int(m.group(1)) for line in tail for m in [DATE_RE.search(line)] if m]
    return max(years) if years else None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--mod", choices=("sandbox", "rt56"), default="sandbox")
    ap.add_argument("--until-year", type=int, default=1940)
    ap.add_argument("--poll-seconds", type=int, default=60)
    ap.add_argument("--max-minutes", type=int, default=90)
    ap.add_argument("--watchdog-minutes", type=int, default=15)
    ap.add_argument("--analyze-only", action="store_true",
                    help="skip launch/monitor/kill; analyze the current logs")
    args = ap.parse_args()
    if args.until_year < 1936:
        ap.error("--until-year must be 1936 or later")
    if args.poll_seconds <= 0 or args.max_minutes <= 0 or args.watchdog_minutes <= 0:
        ap.error("poll/max/watchdog values must be positive")

    mod_dir = MODS[args.mod]
    game_log = LOG_DIR / "game.log"
    err_log = LOG_DIR / "error.log"
    exe = GAME_DIR / "hoi4.exe"
    try:
        if not exe.is_file():
            raise Fail(f"no game binary at {exe}")
        if not args.analyze_only:
            running = subprocess.run(["tasklist", "/FI", "IMAGENAME eq hoi4.exe"],
                                     capture_output=True, text=True).stdout
            if "hoi4.exe" in running.lower().split("info:")[0]:
                raise Fail("hoi4.exe already running; quit it first")
        dlc = json.loads((DOCS / "dlc_load.json").read_text(encoding="utf-8"))
        if DESCRIPTORS[args.mod] not in dlc.get("enabled_mods", []):
            raise Fail(f"playset does not enable {DESCRIPTORS[args.mod]}; set it in the launcher first")
        if not LOG_DIR.is_dir():
            raise Fail(f"no logs dir at {LOG_DIR}")

        if args.analyze_only:
            print("analyze-only: skipping launch/monitor/kill")
        else:
            n_logs = clear_dir(LOG_DIR)
            n_saves = clear_dir(SAVES_DIR)
            print(f"cleared {n_logs} log entries, {n_saves} save entries")

            proc = subprocess.Popen(
                [str(exe), "-nolauncher", "-debug", "-historical=no", "-hands_off"],
                cwd=str(GAME_DIR),
                creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL,
            )
            print(f"launched pid {proc.pid}; waiting for logs...")
            deadline = time.time() + args.max_minutes * 60
            silent_since = time.time()
            last_size = -1
            outcome = "target-year"
            while True:
                time.sleep(args.poll_seconds)
                if proc.poll() is not None:
                    outcome = "process-gone"
                    break
                size = game_log.stat().st_size if game_log.is_file() else 0
                if size != last_size:
                    last_size = size
                    silent_since = time.time()
                year = newest_year(game_log)
                print(f"  year={year} size={size}", flush=True)
                if year is not None and year >= args.until_year:
                    break
                if time.time() - silent_since > args.watchdog_minutes * 60:
                    outcome = "silent-log"
                    break
                if time.time() > deadline:
                    outcome = "timeout"
                    break
            subprocess.run(["taskkill", "/F", "/IM", "hoi4.exe"],
                           capture_output=True, text=True)
            time.sleep(5)
            print(f"stopped: {outcome}")
            if outcome != "target-year":
                return 1

        ext = mod_dir / ".scratch" / "scripts" / "extract_sandbox.py"
        print("--- analysis ---", flush=True)
        subprocess.run([sys.executable, str(ext), str(game_log)], check=False)
        extract_txt = LOG_DIR / "sandbox_extract.txt"
        if not extract_txt.is_file():
            raise Fail("extractor produced no output; game.log may hold no telemetry")
        lines = extract_txt.read_text(encoding="utf-8", errors="replace").splitlines()
        counts: Counter = Counter()
        for line in lines:
            m = re.search(r"\b(sc_\w+)", line)
            if m:
                counts[m.group(1)] += 1
        print(f"--- extract: {len(lines)} lines ---")
        print(dict(counts))
        print("--- decision lines ---")
        for line in lines:
            if "sc_power" not in line and ("sc_focus" not in line) and KEY_RE.search(line):
                print(" ", line[:165])
        print("--- error.log scenario scan ---")
        hits = [l for l in err_log.read_text(encoding="utf-8", errors="replace").splitlines()
                if ERR_RE.search(l)] if err_log.is_file() else []
        print(f"scenario hits: {len(hits)}")
        for line in hits[:15]:
            print(" ", line[:150])
        return 0
    except Fail as exc:
        print(f"aborted: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
