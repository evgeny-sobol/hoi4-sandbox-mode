#!/usr/bin/env python3
"""Add the scenario opinion-modifier localisation key to the vanilla mod.

The join lever tags joiners with the scenario_ally opinion modifier. No faction
is created any more (a faction leader is locked out of its own war focuses, some
of which require is_in_faction = no), so the sandbox_<ns>_faction keys were
removed. Writes with a UTF-8 BOM: HOI4 drops a localisation file without one.
"""
from __future__ import annotations

from pathlib import Path

LOC = (
    Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox")
    / "localisation" / "english" / "99_sandbox_l_english.yml"
)

MARKER = " # Scenario join lever (docs/gdd/Scenarios.md)"
KEYS = [("scenario_ally", "Scenario ally")]


def main() -> None:
    text = LOC.read_text(encoding="utf-8-sig").rstrip("\n")
    missing = [k for k, _ in KEYS if f"\n {k}:" not in text and f"\n  {k}:" not in text]
    if not missing:
        print("all keys present")
        return
    block = [MARKER] + [f' {k}: "{v}"' for k, v in KEYS if k in missing]
    LOC.write_text(text + "\n\n" + "\n".join(block) + "\n", encoding="utf-8-sig")
    print(f"added {len(block) - 1} keys")


if __name__ == "__main__":
    main()
