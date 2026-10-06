#!/usr/bin/env python3
"""Add reverse-direction sc_goal guards to the s7 telemetry (issue 06).

The s7 probe logs wargoals only aggressor-to-target, while the GDD documents
both directions. Driven from the arc specs: for every arc, variant and
declared target, the target's power block in `sandbox_scenario_s7_telemetry()`
gains, after its `$sandbox_log_sc_power()` line::

    if has_wargoal_against(AGG) or is_justifying_wargoal_against(AGG):
      $sandbox_log_sc(sc_goal, t_on_agg)

The justification alternative matches the forward guards (issue 16), and the
actor stays the target, so the label's first party is always the log actor.
Idempotent: blocks already carrying the label are skipped.

Usage:
  python add_reverse_goal_lines.py <scenario-hsl> <spec-dir> [--check]
"""
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

FUNC_RE = re.compile(r"^([A-Za-z_0-9]+)\(\):$")
ARC_RE = re.compile(r"global\.sandbox_scenario == (\d+)")
VAR_RE = re.compile(r"global\.sandbox_target_variant == (\w+)")
ELSE_RE = re.compile(r"^(\s*)else:\s*$")
GUARD_RE = re.compile(r"^(\s*)if country_exists\((\w+)\):\s*$")
SCOPE_RE = re.compile(r"^(\s*)(\w+):\s*$")


def load_specs(spec_dir: Path) -> dict[int, dict]:
    arcs: dict[int, dict] = {}
    for path in sorted(spec_dir.glob("*.toml")):
        with path.open("rb") as f:
            data = tomllib.load(f)
        number = data.get("number")
        if not isinstance(number, int):
            continue
        arcs[number] = {
            "aggressor": data["aggressor"],
            "targets": {v: list(data["targets"][v]) for v in ("a", "b")},
        }
    return arcs


def transform(lines: list[str], arcs: dict[int, dict]) -> tuple[list[str], int, list[str]]:
    out: list[str] = []
    changed = 0
    log: list[str] = []
    in_s7 = False
    arc: int | None = None
    variant: str | None = None
    i = 0
    while i < len(lines):
        line = lines[i]
        fm = FUNC_RE.match(line)
        if fm:
            in_s7 = fm.group(1) == "sandbox_scenario_s7_telemetry"
            arc, variant = None, None
            out.append(line)
            i += 1
            continue
        if not in_s7:
            out.append(line)
            i += 1
            continue
        am = ARC_RE.search(line)
        if am and line.strip().startswith(("if", "elif")):
            arc = int(am.group(1))
            variant = None
        vm = VAR_RE.search(line)
        if vm:
            variant = vm.group(1)
        elif ELSE_RE.match(line) and arc is not None:
            variant = "b"
        gm = GUARD_RE.match(line)
        spec = arcs.get(arc, {}) if arc is not None else {}
        if (
            gm
            and variant in ("a", "b")
            and spec
            and gm.group(2) in spec["targets"].get(variant, [])
        ):
            indent, tag = gm.group(1), gm.group(2)
            # find the target scope and its power line
            j = i + 1
            scope_indent = indent + "  "
            if j < len(lines) and lines[j] == f"{scope_indent}{tag}:":
                k = j + 1
                power_at = None
                while k < len(lines) and lines[k].startswith(scope_indent + "  "):
                    if lines[k].strip() == "$sandbox_log_sc_power()":
                        power_at = k
                    k += 1
                label = f"{tag.lower()}_on_{spec['aggressor'].lower()}"
                block = lines[i:k]
                if power_at is not None and not any(f"sc_goal, {label}" in b for b in block):
                    agg = spec["aggressor"]
                    out.extend(lines[i : power_at + 1])
                    out.append(f"{scope_indent}  if has_wargoal_against({agg}) or is_justifying_wargoal_against({agg}):")
                    out.append(f"{scope_indent}    $sandbox_log_sc(sc_goal, {label})")
                    out.extend(lines[power_at + 1 : k])
                    changed += 1
                    log.append(f"ADD arc {arc}{variant}: {label}")
                    i = k
                    continue
                if power_at is None:
                    log.append(f"SKIP arc {arc}{variant} {tag}: no power line")
                else:
                    log.append(f"SKIP (done) arc {arc}{variant}: {label}")
                out.extend(lines[i:k])
                i = k
                continue
        out.append(line)
        i += 1
    return out, changed, log


def main() -> None:
    check = "--check" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--check"]
    if len(args) != 2:
        print(__doc__)
        raise SystemExit(2)
    hsl_path, spec_dir = Path(args[0]), Path(args[1])
    arcs = load_specs(spec_dir)
    lines = hsl_path.read_text(encoding="utf-8").splitlines()
    new_lines, changed, log = transform(lines, arcs)
    for entry in log:
        print(entry)
    print(f"{changed} site(s) to update in {hsl_path}")
    if not check and changed:
        hsl_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
