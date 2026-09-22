#!/usr/bin/env python3
"""Add the scenario faction-name and opinion-modifier l10n keys to the vanilla mod.

The engine creates sandbox_<ns>_faction for every arc and tags joiners with the
scenario_ally opinion modifier, but none of those keys were defined, so the UI
showed raw keys. Names reuse the Rt56 overlay where an equivalent arc exists;
British anti-Soviet drive and American war plan have no Rt56 counterpart and get
new names. Writes with a UTF-8 BOM: HOI4 drops a localisation file without one.
"""
from __future__ import annotations

from pathlib import Path

LOC = (
    Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox")
    / "localisation" / "english" / "99_sandbox_l_english.yml"
)

MARKER = " # Scenario factions (docs/gdd/Scenarios.md)"
KEYS = [
    ("sandbox_axis_faction", "Axis"),
    ("sandbox_sov_south_faction", "Comintern"),
    ("sandbox_japanese_faction", "Co-Prosperity"),
    ("sandbox_italian_faction", "Mare Nostrum"),
    ("sandbox_eng_soviet_faction", "New Empire"),
    ("sandbox_usa_warplan_faction", "Pacific Pact"),
    ("scenario_ally", "Scenario ally"),
]


def main() -> None:
    text = LOC.read_text(encoding="utf-8-sig").rstrip("\n")
    if any(f"\n {k}:" in text or f"  {k}:" in text for k, _ in KEYS):
        print("some keys already present, aborting to avoid duplicates")
        for k, _ in KEYS:
            present = f" {k}:" in text or f"  {k}:" in text
            print(f"  {k}: {'present' if present else 'absent'}")
        return
    block = [MARKER]
    block += [f' {k}: "{v}"' for k, v in KEYS]
    out = text + "\n\n" + "\n".join(block) + "\n"
    LOC.write_text(out, encoding="utf-8-sig")
    print(f"added {len(KEYS)} keys")


if __name__ == "__main__":
    main()
