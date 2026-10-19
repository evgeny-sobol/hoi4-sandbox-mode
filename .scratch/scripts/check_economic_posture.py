#!/usr/bin/env python3
"""Guard: the generated rival plans keep the economic-posture invariants.

Reads common/ai_strategy/99_sandbox_rivals_system.txt of each mod - generated
from sandbox-mod-core/common/macros.hml - and asserts what the design promises
(.scratch/economic-posture, issues 02 and 06), so a generator regression is
visible without launching the game. No game install, standard library only.

Usage:
  check_economic_posture.py [mod_dir ...] [--update]

Without a mod_dir the two default mod folders are checked. --update rewrites
the baseline beside this script (the per-mod plan counts). Exit 1 on any
violation, naming the file and line; exit 2 on a usage error.
"""
from __future__ import annotations

import pathlib
import re
import sys

MODS = [
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox"),
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56"),
]
PLANS = pathlib.Path("common/ai_strategy/99_sandbox_rivals_system.txt")
SCALE = pathlib.Path("common/_sandbox_scale.hml")
EFFECTS = pathlib.Path("common/scripted_effects/99_sandbox_scripted_effects.txt")
BASELINE = pathlib.Path(__file__).with_name("check_economic_posture_baseline")
SCALE_MACRO = re.compile(r"macro sandbox_opinion_scale\(\):\s*\n\s*(\d+)")
GOOD_MACRO = re.compile(r"macro sandbox_opinion_good\(\):\s*\n\s*(\d+)")

PLAN_START = re.compile(r"^([A-Za-z0-9_]+) = \{$")
PLAN_END = re.compile(r"^\}$")
TIER = ("", "_contain", "_feud")
ENTRY = re.compile(r"^\s*type = ([a-z_]+)$")
FIELD = re.compile(r"^\s*(id|seller|target|value) = (.+)$")
# Acts that are script-side: ai_strategy files must never carry them.
SCRIPT_ACTS = ("send_embargo", "break_embargo", "create_production_license")
# The per-tier economic contract: entry type -> (field, value) that must hold.
CONTRACT = {
    "_contain": {
        "equipment_market_trade_desire": ("value", "-50"),
        "equipment_market_buy": ("value", "-200"),
    },
    "_feud": {
        "equipment_market_trade_desire": ("value", "-200"),
        "equipment_market_buy": ("value", "-200"),
        "diplo_action_desire": ("value", "-200"),
    },
}
# The addressed field every economic entry must carry.
ADDRESSED = {
    "equipment_market_buy": "seller",
    "equipment_market_trade_desire": "id",
    "diplo_action_desire": "id",
}


def plans(text: str):
    """Yield (name, first_line, body) for every top-level plan."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = PLAN_START.match(lines[i])
        if not m:
            i += 1
            continue
        j = i + 1
        while j < len(lines) and not PLAN_END.match(lines[j]):
            j += 1
        yield m.group(1), i + 1, lines[i + 1:j]
        i = j + 1


def enable_of(body: list[str]) -> str:
    out: list[str] = []
    inside = False
    for line in body:
        if not inside:
            if line.strip() == "enable = {":
                inside = True
            continue
        if line.strip() == "}":
            break
        out.append(line)
    return "\n".join(out)


def entries_of(body: list[str]):
    """Yield one {field: value} per ai_strategy block, `type` included."""
    cur: dict[str, str] | None = None
    for line in body:
        m = ENTRY.match(line)
        if m:
            if cur is not None:
                yield cur
            cur = {"type": m.group(1)}
            continue
        if cur is not None:
            f = FIELD.match(line)
            if f:
                cur[f.group(1)] = f.group(2).strip()
    if cur is not None:
        yield cur


def check_mod(mod: pathlib.Path, problems: list[str]) -> tuple[int, int, int, int]:
    """Returns (base, contain, feud, tags) plan counts."""
    path = mod / PLANS
    if not path.is_file():
        problems.append(f"{path}: missing; compile the mod first")
        return 0, 0, 0, 0

    text = path.read_text(encoding="utf-8", errors="replace")
    seen: dict[str, list[str]] = {t: [] for t in TIER}

    for name, lineno, body in plans(text):
        suffix = next((s for s in ("_is_rival_contain", "_is_rival_feud", "_is_rival")
                       if name.endswith(s)), None)
        if suffix is None or not name[: -len(suffix)]:
            problems.append(f"{path}:{lineno}: unexpected plan {name}")
            continue
        tag = name[: -len(suffix)]
        tier = {"_is_rival": "", "_is_rival_contain": "_contain",
                "_is_rival_feud": "_feud"}[suffix]
        seen[tier].append(tag)
        enable = enable_of(body)

        if tier == "":
            if f"is_in_array = {{ rivals = {tag} }}" not in enable:
                problems.append(
                    f"{path}:{lineno}: {name} enable does not test {tag} in rivals[]")
        elif tier == "_contain":
            if not re.search(r"var=rivalry\^\d+ value=25 compare=greater_than_or_equals", enable):
                problems.append(f"{path}:{lineno}: {name} enable has no Rival band (>= 25)")
            # Feud must never carry both -50 and -200: the -50 tier stops at 75.
            if "< 75" not in enable:
                problems.append(
                    f"{path}:{lineno}: {name} enable has no Feud cut-off (< 75), so its "
                    "-50 would stack with the feud -200")
        elif not re.search(r"var=rivalry\^\d+ value=75 compare=greater_than_or_equals", enable):
            problems.append(f"{path}:{lineno}: {name} enable has no Feud band (>= 75)")

        for entry in entries_of(body):
            kind = entry.get("type", "")
            if kind in SCRIPT_ACTS:
                problems.append(f"{path}:{lineno}: {name} carries the script act {kind}")
                continue
            if kind not in ADDRESSED:
                continue
            field = ADDRESSED[kind]
            if entry.get(field) != tag:
                problems.append(
                    f"{path}:{lineno}: {name} {kind} is not addressed at {tag} "
                    f"({field} = {entry.get(field)!r})")
            if kind not in CONTRACT.get(tier, {}):
                problems.append(
                    f"{path}:{lineno}: {name} carries {kind}, which the "
                    f"'{tier or 'base'}' tier does not allow")
                continue
            want_field, want_value = CONTRACT[tier][kind]
            if entry.get(want_field) != want_value:
                problems.append(
                    f"{path}:{lineno}: {name} {kind} {want_field} is "
                    f"{entry.get(want_field)!r}, expected {want_value}")

    for act in SCRIPT_ACTS:
        for n, line in enumerate(text.splitlines(), 1):
            if act in line.split("#", 1)[0]:
                problems.append(f"{path}:{n}: {act} belongs in a scripted effect, not here")

    counts = {t: len(seen[t]) for t in TIER}
    for t in TIER:
        if counts[t] != counts[""]:
            problems.append(
                f"{path}: {counts[t]} *_is_rival{t} plans against {counts['']} *_is_rival plans")
    if len(set(seen[""])) != len(seen[""]):
        problems.append(f"{path}: a tag carries more than one *_is_rival plan")
    for t in TIER:
        if sorted(seen[t]) != sorted(seen[""]):
            problems.append(f"{path}: the *_is_rival{t} tag list differs from *_is_rival")
    return counts[""], counts["_contain"], counts["_feud"], len(set(seen[""]))


def opinion_literals(mod: pathlib.Path, problems: list[str]) -> None:
    """Where a block has_opinion appears, the threshold must come from a macro."""
    for path in sorted((mod / "common").rglob("*")):
        if path.suffix not in (".hml", ".hsl") or not path.is_file():
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        for n, line in enumerate(lines, 1):
            if not line.strip().startswith("has_opinion"):
                continue
            for follow in lines[n: min(n + 4, len(lines))]:
                m = re.match(r"\s*value\((.+)\)\s*$", follow)
                if m and "$sandbox_opinion_" not in m.group(1):
                    problems.append(
                        f"{path}:{n}: opinion threshold {m.group(1)} is not a "
                        "sandbox_opinion_* macro")


def opinion_threshold(mod: pathlib.Path, problems: list[str]) -> None:
    """Sympathy is half the mod's clamp: the per-mod threshold must say so, and
    the compiled effects must carry that number beside has_opinion."""
    path = mod / SCALE
    if not path.is_file():
        problems.append(f"{path}: missing; cannot check the opinion threshold")
        return
    text = path.read_text(encoding="utf-8", errors="replace")
    scale = SCALE_MACRO.search(text)
    good = GOOD_MACRO.search(text)
    if not scale or not good:
        problems.append(
            f"{path}: both sandbox_opinion_scale() and sandbox_opinion_good() must "
            "be defined")
        return
    want = int(scale.group(1)) // 2
    got = int(good.group(1))
    if got != want:
        problems.append(
            f"{path}: sandbox_opinion_good() is {got}, but half of "
            f"sandbox_opinion_scale() {scale.group(1)} is {want}")

    effects = mod / EFFECTS
    if not effects.is_file():
        return
    lines = effects.read_text(encoding="utf-8", errors="replace").splitlines()
    for n, line in enumerate(lines, 1):
        if "has_opinion = {" not in line:
            continue
        for follow in lines[n: min(n + 4, len(lines))]:
            m = re.match(r"\s*value = (-?\d+)", follow)
            if m:
                if int(m.group(1)) != got:
                    problems.append(
                        f"{effects}:{n}: has_opinion value {m.group(1)} is not the "
                        f"per-mod good threshold {got}")
                break


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--update"]
    mods = [pathlib.Path(a) for a in args] or MODS

    problems: list[str] = []
    table: list[str] = []
    for mod in mods:
        if not mod.is_dir():
            print("usage: check_economic_posture.py [mod_dir ...] [--update]", file=sys.stderr)
            return 2
        base, contain, feud, tags = check_mod(mod, problems)
        opinion_literals(mod, problems)
        opinion_threshold(mod, problems)
        table.append(f"{mod.name} {base + contain + feud} {base} {contain} {feud} {tags}")

    if "--update" in sys.argv:
        BASELINE.write_text("# mod total base contain feud tags\n" + "\n".join(table) + "\n",
                            encoding="utf-8")
        print(f"baseline written: {len(table)} mod(s)")
        return 0

    if not BASELINE.is_file():
        print("no baseline; run with --update", file=sys.stderr)
        return 2
    recorded: dict[str, int] = {}
    for line in BASELINE.read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or not line.split():
            continue
        parts = line.split()
        recorded[parts[0]] = int(parts[1])
    for row in table:
        name, total = row.split()[0], int(row.split()[1])
        if name not in recorded:
            problems.append(f"{name}: no baseline row; run with --update")
        elif recorded[name] != total:
            problems.append(f"{name}: {total} plans against a baseline of {recorded[name]}")

    for msg in problems:
        print(f"FAIL {msg}")
    print(f"problems: {len(problems)}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
