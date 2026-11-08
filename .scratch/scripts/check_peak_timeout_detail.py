#!/usr/bin/env python3
"""Guard the peak_timeout contract between core and the per-mod catalog.

`macro sandbox_check_peak_timeout()` lives in the shared core and cannot scope
into the aggressor: the arc -> tag mapping is per-mod. So the macro delegates the
logging to `sandbox_log_peak_timeout_detail()`, which each mod defines.

Trap this exists to catch: core re-adding its own generic
`$sandbox_log_sc(sc_derail, peak_timeout)` pair alongside the hook. That compiles
fine, passes every other guard, and quietly prints TWO peak_timeout lines per
timeout - one blind, one informative - which breaks "one line per event" and
makes an extract look like the arc derailed twice.

Also catches the opposite failure: the hook disappearing from the mod catalog,
in which case core would call an undefined effect and the line would vanish
entirely.

Covers both mods.
"""
from __future__ import annotations

import pathlib
import re

MODS = [
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox"),
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56"),
]
CORE_MACROS = pathlib.Path(r"C:\Users\evgeny\Repos\HoI4\sandbox-mod-core\common\macros.hml")
CATALOG = pathlib.Path("common") / "scripted_effects" / "99_sandbox_scenarios.hsl"
COMPILED = pathlib.Path("common") / "scripted_effects" / "99_sandbox_scenarios.txt"

HOOK = "sandbox_log_peak_timeout_detail"


def core_problems() -> list[str]:
    if not CORE_MACROS.is_file():
        return [f"no core macros at {CORE_MACROS}"]
    src = CORE_MACROS.read_text(encoding="utf-8", errors="replace")
    start = src.find("macro sandbox_check_peak_timeout():")
    if start < 0:
        return ["core has no sandbox_check_peak_timeout macro"]
    end = src.find("\nmacro ", start + 1)
    body = src[start : end if end > 0 else len(src)]
    problems: list[str] = []
    # Strip comments so the explanatory text cannot satisfy the checks.
    live = "\n".join(l.split("#", 1)[0] for l in body.splitlines())
    if HOOK not in live:
        problems.append(f"core peak_timeout macro never calls {HOOK}()")
    if re.search(r"\$sandbox_log_sc\(\s*sc_derail\s*,\s*peak_timeout\s*\)", live):
        problems.append("core peak_timeout macro still logs its own blind sc_derail (duplicate line)")
    if re.search(r"\$sandbox_log_sc\(\s*sc_end\s*,\s*peak_timeout\s*\)", live):
        problems.append("core peak_timeout macro still logs its own blind sc_end (duplicate line)")
    return problems


def check(mod: pathlib.Path) -> list[str]:
    problems: list[str] = []

    hsl = mod / CATALOG
    if not hsl.is_file():
        return [f"{mod.name}: no {CATALOG}"]
    src = hsl.read_text(encoding="utf-8", errors="replace")
    if f"{HOOK}():" not in src:
        problems.append(f"{mod.name}: catalog does not define {HOOK}()")

    txt = mod / COMPILED
    if not txt.is_file():
        problems.append(f"{mod.name}: no compiled {COMPILED} (compile first)")
        return problems
    out = txt.read_text(encoding="utf-8", errors="replace")

    blind = len(re.findall(r"sc_derail peak_timeout sc=", out))
    if blind:
        problems.append(f"{mod.name}: compiled output still has {blind} blind `sc_derail peak_timeout sc=` line(s)")
    detailed = len(re.findall(r"sc_derail peak_timeout ai=", out))
    if detailed != 1:
        problems.append(f"{mod.name}: compiled output has {detailed} detailed sc_derail peak_timeout line(s), expected 1")
    detailed_end = len(re.findall(r"sc_end peak_timeout ai=", out))
    if detailed_end != 1:
        problems.append(f"{mod.name}: compiled output has {detailed_end} detailed sc_end peak_timeout line(s), expected 1")

    return problems


def main() -> int:
    problems = core_problems()
    print(f"core: problems {len(problems)}")
    for mod in MODS:
        found = check(mod)
        problems.extend(found)
        print(f"{mod.name}: problems {len(found)}")
    for p in problems:
        print(p)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
