#!/usr/bin/env python3
"""Guard the scorer self-exclusion (issue 03): a country must never score itself.

Trap this exists to catch: `FROM == THIS` reads as an identity test but HSL
lowers a scope-keyword compare through `check_variable`, which tests a variable
against a value. The compiled modifier therefore never excluded the initiator,
so a country could take itself as a rival and then embargo itself.

Accepted shape is a tag compare, `tag(FROM)`, which compiles to `tag = FROM` -
the idiom vanilla uses inside a scorer (operative_mission_scorer.txt:97).

Both the HSL source and the compiled output are checked, because the source can
look right while the compiler emits something else (that is exactly how the
original bug survived).

Covers both mods. The opinion scale differs between them on purpose; only the
identity modifier is audited here.
"""
from __future__ import annotations

import pathlib
import re

MODS = [
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox"),
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56"),
]
SCORER_HSL = pathlib.Path("common") / "scorers" / "country" / "99_sandbox_scorer.hsl"
SCORER_TXT = pathlib.Path("common") / "scorers" / "country" / "99_sandbox_scorer.txt"

# The three scorers that must each carry exactly one identity modifier.
EXPECTED_IDENTITY_MODIFIERS = 3


def check(mod: pathlib.Path) -> list[str]:
    problems: list[str] = []

    hsl = mod / SCORER_HSL
    if not hsl.is_file():
        return [f"{mod.name}: no {SCORER_HSL}"]
    src = hsl.read_text(encoding="utf-8", errors="replace")
    # Strip comments before auditing, so the explanatory comment that quotes the
    # broken form cannot be mistaken for a live modifier.
    live = "\n".join(l.split("#", 1)[0] for l in src.splitlines())

    if re.search(r"^\s*FROM\s*==\s*THIS\s*$", live, re.M):
        problems.append(f"{mod.name}: live `FROM == THIS` survives; it compiles to a check_variable compare")
    if re.search(r"^\s*THIS\s*==\s*FROM\s*$", live, re.M):
        problems.append(f"{mod.name}: live `THIS == FROM` survives; same defect, reversed")

    tags = len(re.findall(r"^\s*tag\(FROM\)\s*$", live, re.M))
    if tags != EXPECTED_IDENTITY_MODIFIERS:
        problems.append(
            f"{mod.name}: {tags} tag(FROM) identity modifier(s) in the source, expected {EXPECTED_IDENTITY_MODIFIERS}"
        )

    txt = mod / SCORER_TXT
    if not txt.is_file():
        problems.append(f"{mod.name}: no {SCORER_TXT} (compile first)")
        return problems
    out = txt.read_text(encoding="utf-8", errors="replace")
    if "check_variable = { FROM = THIS }" in out:
        problems.append(f"{mod.name}: compiled scorer still emits check_variable = {{ FROM = THIS }}")
    if re.search(r"check_variable\s*=\s*\{\s*THIS\s*=\s*FROM\s*\}", out):
        problems.append(f"{mod.name}: compiled scorer emits a reversed scope compare")
    compiled = len(re.findall(r"^\s*tag\s*=\s*FROM\s*$", out, re.M))
    if compiled != EXPECTED_IDENTITY_MODIFIERS:
        problems.append(
            f"{mod.name}: {compiled} compiled `tag = FROM` modifier(s), expected {EXPECTED_IDENTITY_MODIFIERS}"
        )

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
