#!/usr/bin/env python3
"""List every focus that carries ai_scenario_focus_boost / sc_focus in a file."""
from __future__ import annotations

import re
import sys
from pathlib import Path

FOCUS_RE = re.compile(r"focus\[id\s*=\s*([A-Za-z0-9_]+)")
BOOST_RE = re.compile(r"ai_scenario_focus_boost")
SCFOCUS_RE = re.compile(r"sc_focus,\s*([A-Za-z0-9_]+)")


def main() -> None:
    root = Path(sys.argv[1])
    for f in sorted(root.glob("common/national_focus/*.include")):
        cur = None
        boost: list[tuple[str, int]] = []
        scf: list[tuple[str, int]] = []
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            m = FOCUS_RE.search(line)
            if m:
                cur = m.group(1)
            if BOOST_RE.search(line):
                boost.append((cur or "?", i))
            ms = SCFOCUS_RE.search(line)
            if ms:
                scf.append((ms.group(1), i))
        if boost or scf:
            print(f"== {f.name}: boost={len(boost)} sc_focus={len(scf)}")
            for sid, ln in boost:
                print(f"   boost {sid} @L{ln}")
            for sid, ln in scf:
                print(f"   sc_focus {sid} @L{ln}")


if __name__ == "__main__":
    main()
