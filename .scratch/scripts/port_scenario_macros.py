#!/usr/bin/env python3
"""Append the scenario macros to _sandbox/common/macros.hml, ported from the
Rt56 overlay with the same bodies. Flip-gate macros are omitted (every vanilla
arc is historical). The focus-boost macro and the sc_* log/gate/derail macros
are mod-agnostic and carried verbatim.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R56 = Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56")
SB_MACROS = ROOT / "common" / "macros.hml"
R56_MACROS = R56 / "common" / "macros.hml"

WANT = [
    "ai_scenario_focus_boost",
    "sandbox_log_sc",
    "sandbox_log_sc_power",
    "sandbox_log_sc_seed",
    "sandbox_log_target_status",
    "sandbox_add_rivalry_vs",
    "sandbox_seed_rival",
    "sandbox_check_targets_derail1",
    "sandbox_check_targets_derail2",
    "sandbox_check_targets_derail3",
    "sandbox_check_targets_derail4",
    "sandbox_check_aggressor_civil_war",
]


def extract_macros(text: str) -> dict[str, str]:
    """Return {macro_name: full_block_text} for each `macro NAME(...):` in text.

    A block runs until the next `macro ` at column 0 or a top-level comment that
    precedes one (we keep trailing blank lines under control).
    """
    lines = text.splitlines(keepends=True)
    starts: list[tuple[int, str]] = []
    for i, ln in enumerate(lines):
        m = re.match(r"macro ([A-Za-z_0-9]+)\(", ln)
        if m:
            starts.append((i, m.group(1)))
    out: dict[str, str] = {}
    for idx, (i, name) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(lines)
        # trim trailing blank lines
        block = "".join(lines[i:end]).rstrip("\n")
        out[name] = block
    return out


def main() -> None:
    r56 = extract_macros(R56_MACROS.read_text(encoding="utf-8"))
    missing = [w for w in WANT if w not in r56]
    if missing:
        raise SystemExit(f"missing in r56 macros: {missing}")

    sb = SB_MACROS.read_text(encoding="utf-8")
    already = set(re.findall(r"^macro ([A-Za-z_0-9]+)\(", sb, re.M))
    to_add = [w for w in WANT if w not in already]

    block = "\n\n".join(r56[w] for w in to_add)
    header = (
        "\n# Scenario engine macros (docs/gdd/Scenarios.md), shared with the Rt56\n"
        "# overlay. Flip gates are omitted: every vanilla arc is historical.\n\n"
    )
    SB_MACROS.write_text(sb.rstrip("\n") + "\n" + header + block + "\n", encoding="utf-8")
    print(f"added {len(to_add)} macros: {', '.join(to_add)}")


if __name__ == "__main__":
    main()
