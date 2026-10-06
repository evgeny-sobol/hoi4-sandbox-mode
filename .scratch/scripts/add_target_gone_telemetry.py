#!/usr/bin/env python3
"""Add <tag>_gone telemetry for dead declared targets (issue 14).

For every peak-fire block shaped as::

    if country_exists(TAG):
      TAG:
        <status-call>

append::

    else:
      AGG:
        $sandbox_log_sc(sc_target, tag_gone)

where <status-call> is either the shared ``$sandbox_log_target_status(AGG)``
(vanilla) or a per-arc ``sandbox_log_<arc>_target_status()`` (r56, aggressor
resolved from the enclosing function name). Idempotent: sites already
followed by ``else:`` are skipped.

Usage:
  python add_target_gone_telemetry.py <scenario-hsl> [--check]
  --check only reports sites without modifying the file.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# r56 per-arc status function -> aggressor tag (mirrors the joiner scope and
# the per-arc comments in the r56 catalog).
R56_AGGRESSOR = {
    "axis": "GER",
    "soviet": "SOV",
    "japanese": "JAP",
    "italian": "ITA",
    "britain": "ENG",
    "red_america": "USA",
    "napoleonic_france": "FRA",
    "habsburg": "HUN",
}

GUARD_RE = re.compile(r"^(\s*)if country_exists\((\w+)\):\s*$")
SHARED_CALL_RE = re.compile(r"^\s*\$sandbox_log_target_status\((\w+)\)\s*$")
PER_ARC_CALL_RE = re.compile(r"^\s*sandbox_log_(\w+)_target_status\(\)\s*$")
FUNC_RE = re.compile(r"^(sandbox_\w+)\(\):$")


def transform(lines: list[str]) -> tuple[list[str], int, list[str]]:
    out: list[str] = []
    changed = 0
    log: list[str] = []
    cur_func = ""
    i = 0
    while i < len(lines):
        m = GUARD_RE.match(lines[i])
        if m and i + 2 < len(lines):
            indent, tag = m.group(1), m.group(2)
            scope = lines[i + 1].strip()
            call = lines[i + 2]
            agg = None
            m2 = SHARED_CALL_RE.match(call)
            if m2 and scope == f"{tag}:":
                agg = m2.group(1)
            else:
                m3 = PER_ARC_CALL_RE.match(call)
                if m3 and scope == f"{tag}:":
                    arc = m3.group(1)
                    # enclosing peak fn names look like sandbox_fire_<arc>_peak
                    if cur_func == f"sandbox_fire_{arc}_peak":
                        agg = R56_AGGRESSOR.get(arc)
            if agg is not None:
                out.extend(lines[i : i + 3])
                nxt = lines[i + 3] if i + 3 < len(lines) else ""
                if nxt.strip() == "else:":
                    log.append(f"SKIP (has else): {cur_func}:{i + 1} {tag}")
                else:
                    gone = tag.lower() + "_gone"
                    out.append(f"{indent}else:")
                    out.append(f"{indent}  {agg}:")
                    out.append(f"{indent}    $sandbox_log_sc(sc_target, {gone})")
                    changed += 1
                    log.append(f"ADD {cur_func}:{i + 1} {tag} -> {agg} sc_target {gone}")
                i += 3
                continue
        fm = FUNC_RE.match(lines[i])
        if fm:
            cur_func = fm.group(1)
        out.append(lines[i])
        i += 1
    return out, changed, log


def main() -> None:
    check = "--check" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--check"]
    if len(args) != 1:
        print(__doc__)
        raise SystemExit(2)
    path = Path(args[0])
    lines = path.read_text(encoding="utf-8").splitlines()
    new_lines, changed, log = transform(lines)
    for entry in log:
        print(entry)
    print(f"{changed} site(s) to update in {path}")
    if not check and changed:
        path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
