#!/usr/bin/env python3
"""Cover the justification window in the sc_goal probe (issue 16).

For every line shaped as::

    if has_wargoal_against(TAG):

immediately followed by a ``$sandbox_log_sc(sc_goal, ...)`` line, rewrite
the condition to::

    if has_wargoal_against(TAG) or is_justifying_wargoal_against(TAG):

so the monthly s7 sample reports pressure while the claim is being built,
not only after the wargoal lands. Idempotent: lines already containing
``is_justifying_wargoal_against`` are skipped.

Usage:
  python add_justify_to_goal_probe.py <scenario-hsl> [--check]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

GUARD_RE = re.compile(r"^(\s*)if has_wargoal_against\((\w+)\):\s*$")


def transform(lines: list[str]) -> tuple[list[str], int, list[str]]:
    out: list[str] = []
    changed = 0
    log: list[str] = []
    for i, line in enumerate(lines):
        m = GUARD_RE.match(line)
        if m and i + 1 < len(lines) and "sandbox_log_sc(sc_goal" in lines[i + 1]:
            if "is_justifying_wargoal_against" in line:
                log.append(f"SKIP (done): {i + 1}")
            else:
                indent, tag = m.group(1), m.group(2)
                line = (
                    f"{indent}if has_wargoal_against({tag})"
                    f" or is_justifying_wargoal_against({tag}):"
                )
                changed += 1
                log.append(f"ADD {i + 1}: {tag}")
        out.append(line)
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
    for entry in log[:12]:
        print(entry)
    if len(log) > 12:
        print(f"... and {len(log) - 12} more")
    print(f"{changed} site(s) to update in {path}")
    if not check and changed:
        path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
