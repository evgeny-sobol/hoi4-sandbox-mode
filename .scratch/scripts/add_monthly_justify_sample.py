#!/usr/bin/env python3
"""Sample sc_justify monthly in the s7 telemetry (issue 15).

The daily on_justifying_wargoal_pulse hook no longer logs (the pulse keeps
the Honor drip only). For every aggressor-direction sc_goal guard shaped as::

    if has_wargoal_against(T) or is_justifying_wargoal_against(T):
      $sandbox_log_sc(sc_goal, agg_on_t)

append, in the same aggressor scope::

    if is_justifying_wargoal_against(T):
      $sandbox_log_sc(sc_justify, agg_on_t)

so one line per month per actively-justified declared pair replaces the
per-day repeat. Aggressor and targets per arc come from the catalog's own
sandbox_seed_actors() / sandbox_set_targets() (same parse as the arc-hooks
generator). Idempotent.

Usage:
  python add_monthly_justify_sample.py <scenario-hsl> [--check]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

FUNC_RE = re.compile(r"^([A-Za-z_0-9]+)\(\):$")
ARC_RE = re.compile(r"global\.sandbox_scenario == (\d+)")
VAR_RE = re.compile(r"global\.sandbox_target_variant == (\w+)")
ELSE_RE = re.compile(r"^\s*else:\s*$")
SCOPE_RE = re.compile(r"^(\s*)([A-Z]{3}):\s*$")
ADD_RE = re.compile(r"^\s*global\.&sandbox_targets\[\]\.add\((\w+)\)\s*$")
TAG_HEAD_RE = re.compile(r"^\s*([A-Z]{3}):\s*$")
GOAL_GUARD_RE = re.compile(r"^(\s*)if has_wargoal_against\((\w+)\) or .*:\s*$")
GOAL_LOG_RE = re.compile(r"^\s*\$sandbox_log_sc\(sc_goal, (\w+)\)\s*$")


def split_functions(lines: list[str]) -> dict[str, list[str]]:
    funcs: dict[str, list[str]] = {}
    cur: str | None = None
    for line in lines:
        m = FUNC_RE.match(line)
        if m:
            cur = m.group(1)
            funcs[cur] = []
        elif cur is not None:
            funcs[cur].append(line)
    return funcs


def parse_aggressors(body: list[str]) -> dict[int, str]:
    out: dict[int, str] = {}
    arc: int | None = None
    for line in body:
        m = ARC_RE.search(line)
        if m and line.strip().startswith(("if", "elif")):
            arc = int(m.group(1))
            continue
        m = TAG_HEAD_RE.match(line)
        if m and arc is not None:
            out.setdefault(arc, m.group(1))
    return out


def transform(lines: list[str], aggressors: dict[int, str]) -> tuple[list[str], int, list[str]]:
    out: list[str] = []
    changed = 0
    log: list[str] = []
    arc: int | None = None
    scope = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        if FUNC_RE.match(line):
            arc, scope = None, ""
            out.append(line)
            i += 1
            continue
        m = ARC_RE.search(line)
        if m and line.strip().startswith(("if", "elif")):
            arc = int(m.group(1))
        if ELSE_RE.match(line):
            pass
        sm = SCOPE_RE.match(line)
        if sm and sm.group(2) != "else":
            scope = sm.group(2)
        gm = GOAL_GUARD_RE.match(line)
        if (
            gm
            and i + 1 < len(lines)
            and arc is not None
            and scope == aggressors.get(arc, "")
        ):
            indent, tgt = gm.group(1), gm.group(2)
            lm = GOAL_LOG_RE.match(lines[i + 1])
            want = f"{scope.lower()}_on_{tgt.lower()}"
            if lm and lm.group(1) == want:
                out.append(line)
                out.append(lines[i + 1])
                nxt = lines[i + 2] if i + 2 < len(lines) else ""
                if nxt.strip() == f"if is_justifying_wargoal_against({tgt}):":
                    log.append(f"SKIP (done): {i + 1} {want}")
                else:
                    out.append(f"{indent}if is_justifying_wargoal_against({tgt}):")
                    out.append(f"{indent}  $sandbox_log_sc(sc_justify, {want})")
                    changed += 1
                    log.append(f"ADD {i + 1}: {want}")
                i += 2
                continue
        out.append(line)
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
    funcs = split_functions(lines)
    aggressors: dict[int, str] = {}
    if "sandbox_seed_actors" in funcs:
        aggressors = parse_aggressors(funcs["sandbox_seed_actors"])
    new_lines, changed, log = transform(lines, aggressors)
    print(f"arcs with aggressors: {len(aggressors)}")
    for entry in log[:15]:
        print(entry)
    if len(log) > 15:
        print(f"... and {len(log) - 15} more")
    print(f"{changed} site(s) to update in {path}")
    if not check and changed:
        path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
