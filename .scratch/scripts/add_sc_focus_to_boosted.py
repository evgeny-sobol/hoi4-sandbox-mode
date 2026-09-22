#!/usr/bin/env python3
"""Add sc_focus completion logging to every focus that carries the arc boost.

Keeps telemetry in step with the widened boost set: if a focus is boosted, its
completion should show up in the log, otherwise a dead gate is invisible.
Idempotent.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NF = ROOT / "common" / "national_focus"

FOCUS_START = re.compile(r"(?m)^  focus\[id = (\w+)\]:")
BOOST = "$ai_scenario_focus_boost()"


def main() -> None:
    for p in sorted(NF.glob("*.include")):
        text = p.read_text(encoding="utf-8")
        if BOOST not in text:
            continue
        starts = [(m.start(), m.group(1)) for m in FOCUS_START.finditer(text)]
        added = 0
        # insert back-to-front so earlier offsets stay valid
        inserts: list[tuple[int, str]] = []
        for k, (s, fid) in enumerate(starts):
            e = starts[k + 1][0] if k + 1 < len(starts) else len(text)
            blk = text[s:e]
            if BOOST not in blk:
                continue
            if f"sc_focus, {fid}" in blk:
                continue
            inserts.append((e, fid))
        for at, fid in sorted(inserts, reverse=True):
            # append inside the block: back off trailing blank lines
            ins = at
            while ins > 0 and text[ins - 1] == "\n":
                ins -= 1
            text = text[:ins] + \
                f"\n    +completion_reward:\n      $sandbox_log_sc(sc_focus, {fid})\n" + \
                text[ins:]
            added += 1
        if added:
            p.write_text(text, encoding="utf-8")
        print(f"{p.name}: sc_focus added={added}")


if __name__ == "__main__":
    main()
