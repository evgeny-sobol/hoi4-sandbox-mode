#!/usr/bin/env python3
"""Guard the repick gate (issue 01): ending an arc must repick it.

An arc ends two ways: it derails, or it ignites by war. Both set the phase to
3, and the ignition path runs before the derail dispatcher, so a gate that
snapshots the phase inside the dispatcher never sees the ignition crossing and
the director parks for the rest of the session.

The accepted shape is: the tick snapshots the phase itself, before either check
can move it, and calls the repick after both have run; an ignition outside the
tick (on_declare_war) raises a pending flag that the next tick consumes.

Covers both mods.
"""
from __future__ import annotations

import pathlib
import re

MODS = [
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox"),
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56"),
]
CATALOG = pathlib.Path("common") / "scripted_effects" / "99_sandbox_scenarios.hsl"
GEN_HSL = pathlib.Path("common") / "scripted_effects" / "99_sandbox_scenarios_gen.hsl"
FUNC = re.compile(r"^([A-Za-z_0-9]+)\(\):$")


def bodies(lines: list[str]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    cur = None
    for line in lines:
        m = FUNC.match(line.strip())
        if m:
            cur = m.group(1)
            out[cur] = []
        elif cur is not None:
            out[cur].append(line)
    return out


def check(mod: pathlib.Path) -> list[str]:
    path = mod / CATALOG
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    funcs = bodies(lines)
    problems: list[str] = []

    tick = funcs.get("sandbox_scenario_tick")
    if tick is None:
        return [f"{mod.name}: no sandbox_scenario_tick()"]

    ignite_at = derail_at = snapshot_at = repick_at = -1
    for i, line in enumerate(tick):
        if "sandbox_scenario_check_ignite_by_war()" in line and ignite_at < 0:
            ignite_at = i
        if "sandbox_scenario_check_derail()" in line and derail_at < 0:
            derail_at = i
        if "sandbox_scenario_maybe_repick()" in line and repick_at < 0:
            repick_at = i
        if re.match(r"^\s+[a-z_0-9]+ = global\.sandbox_scenario_phase\s*$", line) and snapshot_at < 0:
            snapshot_at = i

    if snapshot_at < 0:
        problems.append(f"{mod.name}: tick takes no phase snapshot")
    elif ignite_at >= 0 and snapshot_at > ignite_at:
        problems.append(f"{mod.name}: tick snapshots the phase after ignition, so the gate cannot fire")
    if repick_at < 0:
        problems.append(f"{mod.name}: tick never calls sandbox_scenario_maybe_repick()")

    derail = funcs.get("sandbox_scenario_check_derail")
    if derail is not None and any("sandbox_scenario_maybe_repick()" in l for l in derail):
        problems.append(f"{mod.name}: derail dispatcher still repicks; the tick owns the gate")

    success = funcs.get("sandbox_log_scenario_success")
    if success is None:
        problems.append(f"{mod.name}: no sandbox_log_scenario_success()")
    elif not any("sandbox_scenario_repick_pending = 1" in l for l in success):
        problems.append(f"{mod.name}: ignite path does not raise sandbox_scenario_repick_pending")

    pick = funcs.get("sandbox_pick_scenario")
    repick = funcs.get("sandbox_scenario_maybe_repick")
    for name, body in (("sandbox_pick_scenario", pick), ("sandbox_scenario_maybe_repick", repick)):
        if body is None:
            problems.append(f"{mod.name}: no {name}()")
        elif not any("sandbox_scenario_repick_pending = 0" in l for l in body):
            problems.append(f"{mod.name}: {name} does not clear sandbox_scenario_repick_pending")

    problems.extend(check_human_aggressor_excluded(mod, repick))
    return problems


# ADR-0009: a human aggressor is never drawn. Both pick paths must gate every
# eligibility entry on the aggressor being AI-run, and the peak gate must not
# carry an arm for a human aggressor (unreachable once the pool excludes it).
ARCS = (("GER", 1), ("ITA", 2), ("JAP", 3), ("SOV", 4), ("FRA", 5), ("ENG", 6), ("USA", 7))


def check_human_aggressor_excluded(mod: pathlib.Path, repick: list[str] | None) -> list[str]:
    problems: list[str] = []

    # The repick pool is hand-written, so audit its arms directly. Issue 04
    # wants one strict `if` line per arm: the aggressor exists, is AI, is not
    # already derailed, and is not at war with ANY declared target. A war test
    # written as bare body lines compiles OUTSIDE `limit` and gates nothing, so
    # the check requires the whole gate on the `if` line itself.
    if repick is None:
        problems.append(f"{mod.name}: no sandbox_scenario_maybe_repick() to audit")
    else:
        for tag, number in ARCS:
            hits = [i for i, l in enumerate(repick) if f"eligible[].add({number})" in l]
            if not hits:
                continue
            head = next(
                (repick[i] for i in range(hits[0] - 1, -1, -1) if repick[i].strip().startswith(("if ", "elif "))),
                "",
            )
            if f"{tag}->is_ai(yes)" not in head:
                problems.append(f"{mod.name}: repick arc {number} ({tag}) is eligible without is_ai(yes)")
            if f"not {tag}->has_war_with(" not in head:
                problems.append(f"{mod.name}: repick arc {number} ({tag}) has no war test on the eligibility line")
            foreign = [w for w in re.findall(r"(\w+)->has_war_with\(", head) if w != tag]
            if foreign:
                problems.append(f"{mod.name}: repick arc {number} ({tag}) war test uses a foreign tag: {foreign[0]}")
            # Nothing between head and the add may carry a bare condition: it
            # would land outside `limit` when compiled.
            stray = [l.strip() for l in repick[repick.index(head) + 1 : hits[0]] if l.strip()]
            if stray:
                problems.append(
                    f"{mod.name}: repick arc {number} ({tag}) has body conditions that compile outside limit: {stray[0]}"
                )

    # The initial pick delegates to the generated eligible() functions.
    gen = mod / GEN_HSL
    if not gen.is_file():
        problems.append(f"{mod.name}: no {GEN_HSL}")
        return problems
    gen_funcs = bodies(gen.read_text(encoding="utf-8", errors="replace").splitlines())
    for tag, number in ARCS:
        name = next((n for n in gen_funcs if n.endswith("_scenario_eligible") and f"eligible[].add({number})" in "\n".join(gen_funcs[n])), None)
        if name is None:
            continue
        body = "\n".join(gen_funcs[name])
        if f"{tag}->is_ai(yes)" not in body:
            problems.append(f"{mod.name}: {name}() is eligible without {tag}->is_ai(yes)")
        gate_line = next((l for l in gen_funcs[name] if l.strip().startswith("if ")), "")
        if f"not {tag}->has_war_with(" not in gate_line:
            problems.append(f"{mod.name}: {name}() has no war test on the `if` line (body conditions compile outside limit)")
        foreign = [w for w in re.findall(r"(\w+)->has_war_with\(", gate_line) if w != tag]
        if foreign:
            problems.append(f"{mod.name}: {name}() war test uses a foreign tag: {foreign[0]}")

    # No peak arm may fire on a human aggressor.
    for name, body in gen_funcs.items():
        if name.endswith("_scenario_tick") and any("is_ai(no)" in l for l in body):
            problems.append(f"{mod.name}: {name}() still carries a human-aggressor arm")

    return problems


def main() -> int:
    problems: list[str] = []
    for mod in MODS:
        found = check(mod)
        problems.extend(found)
        print(f"{mod.name}: problems {len(found)}")
    for p in problems:
        print(p)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
