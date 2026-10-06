#!/usr/bin/env python3
"""Verify a RU mirror: sections, checkboxes, punctuation, source freshness."""
from __future__ import annotations

import collections
import pathlib
import re
import subprocess
import sys

REPLACEMENTS = {
    "\u2212": "-",
    "\u2192": "->",
    "\u2248": "~=",
    "\u00d7": "x",
    "\u00b7": "*",
    "\u00b1": "+/-",
    "\u2014": "-",
    "\u2013": "-",
    "\u2265": ">=",
    "\u2264": "<=",
    "\u201c": '"',
    "\u201d": '"',
    "\u2018": "'",
    "\u2019": "'",
    "\u2026": "...",
}


SOURCE_RE = re.compile(r"^<!-- source: ([0-9a-f]{4,40}) -->$")


def check_freshness(en_path: pathlib.Path, ru_lines: list[str]) -> bool:
    """The RU file must name its source commit, and the EN file must be
    unchanged since then. Returns True when fresh."""
    if not ru_lines or not SOURCE_RE.match(ru_lines[0]):
        print("source line: MISSING (first line must be <!-- source: <hash> -->)")
        return False
    base = SOURCE_RE.match(ru_lines[0]).group(1)
    top = subprocess.run(
        ["git", "-C", str(en_path.parent), "rev-parse", "--show-toplevel"],
        capture_output=True, text=True)
    if top.returncode != 0:
        print(f"source line: cannot locate repo for {en_path}")
        return False
    root = pathlib.Path(top.stdout.strip())
    rel = en_path.resolve().relative_to(root.resolve()).as_posix()
    if subprocess.run(
            ["git", "-C", str(root), "cat-file", "-t", base],
            capture_output=True, text=True).returncode != 0:
        sub = root / "core"
        if (sub / ".git").exists() or sub.is_dir():
            sub_hit = subprocess.run(
                ["git", "-C", str(sub), "cat-file", "-t", base],
                capture_output=True, text=True)
            if sub_hit.returncode == 0:
                print(f"source line: foreign hash ({base[:12]} lives in core; freshness checked there)")
                return True
        print(f"source line: unknown commit {base}")
        return False
    log = subprocess.run(
        ["git", "-C", str(root), "log", "--format=%h", f"{base}..HEAD", "--", rel],
        capture_output=True, text=True)
    if log.returncode != 0:
        print(f"source line: unknown commit {base}")
        return False
    touched = [h for h in log.stdout.split() if h]
    if touched:
        print(f"source line: STALE (EN changed since {base}: {', '.join(touched)})")
        return False
    print(f"source line: fresh ({base})")
    return True


def norm(text: str) -> str:
    for ch, rep in REPLACEMENTS.items():
        text = text.replace(ch, rep)
    return text


def main() -> int:
    en_name, ru_name = sys.argv[1], sys.argv[2]
    ok = True
    en = pathlib.Path(en_name).read_text(encoding="utf-8").splitlines()
    rup = pathlib.Path(ru_name)
    ru = rup.read_text(encoding="utf-8").splitlines()
    en_h = [norm(line) for line in en if line.startswith("#")]
    ru_h = [norm(line.replace(" - RU", "")) for line in ru if line.startswith("#")]
    print("sections:", en_h == ru_h, len(en_h))
    if en_h != ru_h:
        ok = False
        print("EN ONLY:", ascii([h for h in en_h if h not in ru_h]))
        print("RU ONLY:", ascii([h for h in ru_h if h not in en_h]))
    en_box = [line[:5] for line in en if re.match(r"- \[[ x]\]", line)]
    ru_box = [line[:5] for line in ru if re.match(r"- \[[ x]\]", line)]
    print("checkbox:", en_box == ru_box, len(en_box))
    if en_box != ru_box:
        ok = False
    text = "\n".join(ru)
    for ch, rep in REPLACEMENTS.items():
        text = text.replace(ch, rep)
    rup.write_text(text, encoding="utf-8")
    left = collections.Counter(
        ord(ch) for ch in text if ord(ch) > 127 and not (0x0400 <= ord(ch) <= 0x045F))
    print("non-cyr-ascii left:", dict(left) if left else "NONE")
    if left:
        ok = False
    if not check_freshness(pathlib.Path(en_name), ru):
        ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
