#!/usr/bin/env python3
"""Guard: every declared arc target must be covered by the arc's peak events,
and every scenario event must have its localisation keys.

Coverage: union of trigger tags over the events the arc's peak can fire.
L10n: each scenario event id needs <id>_t, <id>_d, <id>_a, <id>_b in the
mod's English localisation; a missing key falls back to a raw key in game.
"""
from __future__ import annotations

import pathlib
import re

MODS = [
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox"),
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56"),
]
CATALOG = pathlib.Path("common/scripted_effects/99_sandbox_scenarios.hsl")
EVENTS = pathlib.Path("events")
L10N = pathlib.Path("localisation/english/99_sandbox_l_english.yml")
FUNC = re.compile(r"^([A-Za-z_0-9]+)\(\):$")
SCEN = re.compile(r"sandbox_scenario == (\d+)")
ADD = re.compile(r"sandbox_targets\[\]\.add\((\w+)\)")
EID = re.compile(r"id\((sandbox_[\w.]+)\)")


def split_funcs(lines):
    out, cur = {}, None
    for line in lines:
        m = FUNC.match(line.strip())
        if m:
            cur = m.group(1)
            out[cur] = []
        elif cur:
            out[cur].append(line)
    return out


LETTERS = ("a", "b", "c", "d")


def declared(body):
    arcs, cur, slot = {}, None, 0
    for line in body:
        m = SCEN.search(line)
        if m and line.strip().startswith(("if", "elif")):
            cur = int(m.group(1))
            arcs[cur] = {}
            slot = 0
            continue
        v = re.search(r"if global\.sandbox_target_variant == (\w+):", line)
        if v:
            slot = len(arcs[cur])
            arcs[cur].setdefault(LETTERS[slot] if slot < len(LETTERS) else v.group(1), [])
            continue
        if line.strip() == "else:" and cur is not None:
            slot = len(arcs[cur])
            arcs[cur].setdefault(LETTERS[slot] if slot < len(LETTERS) else "else", [])
            continue
        a = ADD.search(line)
        if a and cur is not None:
            key = LETTERS[slot] if slot < len(LETTERS) else None
            if key is not None:
                arcs[cur].setdefault(key, []).append(a.group(1))
    return arcs


def event_tags(mod):
    out = {}
    for path in (mod / EVENTS).glob("*.hsl"):
        text = path.read_text(encoding="utf-8", errors="replace")
        for block in re.finditer(r"id\(([\w.]+)\)([\s\S]*?)(?=\ncountry_event:|\Z)", text):
            eid, body = block.group(1), block.group(2)
            m = re.search(r"trigger:\s*\n\s*tag\(([^)]+)\)", body)
            out[eid] = {t.strip() for t in m.group(1).split("|")} if m else set()
    return out


def arc_coverage(funcs_, ev):
    out: dict[int, set[str]] = {}
    for name, body in funcs_.items():
        if not name.endswith("_peak"):
            continue
        arc = None
        for line in body:
            m = SCEN.search(line)
            if m:
                arc = int(m.group(1))
            for eid in EID.findall(line):
                if arc is not None:
                    out.setdefault(arc, set()).update(ev.get(eid, set()))
    return out


TAG_SCOPE = re.compile(r"^(\s+)([A-Z]{3}):\s*$")
VAR = re.compile(r"sandbox_target_variant == (\w)")


def arc_callsites(funcs_, ev):
    """Pair every peak call's target scope with the event's own trigger tag.

    The union coverage above cannot see a swap where the union still equals the
    declared targets (issue 22: arc 1a sent the POL event to CZE and the CZE
    event to POL). This pairs each call site with the event's trigger and
    reports a call whose target the trigger does not admit.
    """
    problems: list[str] = []
    for name, body in funcs_.items():
        if not name.endswith("_peak"):
            continue
        arc, scope, variant = None, None, "?"
        for line in body:
            m = SCEN.search(line)
            if m and line.strip().startswith(("if", "elif")):
                arc = int(m.group(1))
            m = VAR.search(line)
            if m:
                variant = m.group(1)
            m = TAG_SCOPE.match(line)
            if m:
                scope = m.group(2)
                continue
            m = EID.search(line)
            if m and scope:
                eid = m.group(1)
                allowed = ev.get(eid, set())
                if allowed and scope not in allowed:
                    problems.append(
                        f"arc {arc}{variant} calls {eid} on {scope} "
                        f"but the event triggers on {sorted(allowed)}"
                    )
    return problems


def scenario_events(mod) -> set[str]:
    out: set[str] = set()
    for path in (mod / EVENTS).glob("*.hsl"):
        out |= set(re.findall(r"id\((sandbox_[\w.]+)\)", path.read_text(encoding="utf-8", errors="replace")))
    return out


def l10n_keys(mod) -> set[str]:
    path = mod / L10N
    if not path.is_file():
        return set()
    return set(re.findall(r"^\s+([A-Za-z0-9_.]+):", path.read_text(encoding="utf-8", errors="replace"), re.M))


def main() -> int:
    problems = 0
    for mod in MODS:
        f = split_funcs((mod / CATALOG).read_text(encoding="utf-8", errors="replace").splitlines())
        need = declared(f.get("sandbox_set_targets", []))
        cov = arc_coverage(f, event_tags(mod))
        for arc in sorted(need):
            covered = cov.get(arc, set())
            for variant in sorted(need[arc]):
                miss = [t for t in need[arc][variant] if t not in covered]
                if miss:
                    problems += 1
                    print(f"{mod.name}: arc {arc}{variant} declared={need[arc][variant]} "
                          f"covered={sorted(covered)} MISSING={miss}")

        keys = l10n_keys(mod)
        for eid in sorted(scenario_events(mod)):
            # localisation keys use underscores: sandbox_usa_warplan.2 -> sandbox_usa_warplan_2
            stem = eid.replace(".", "_")
            for suffix in ("_t", "_d", "_a", "_b"):
                if f"{stem}{suffix}" not in keys:
                    problems += 1
                    print(f"{mod.name}: {stem}{suffix} has no localisation key")

        for msg in arc_callsites(f, event_tags(mod)):
            problems += 1
            print(f"{mod.name}: {msg}")

    print(f"problems: {problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
