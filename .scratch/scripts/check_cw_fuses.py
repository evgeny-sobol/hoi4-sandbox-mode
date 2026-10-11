"""Guard against new civil-war fuses.

A civil-war fuse is any `start_civil_war` outside `common/national_focus`.
The mod gates a fuse at its caller (an event trigger, a decision ai_will_do, a
mission delay), so a fuse cannot be proven "gated" from the site alone. This
guard instead fails when a NEW fuse appears - a game update adding one - so the
maintainer reviews it and either gates it or allowlists it.

Usage:
  check_cw_fuses.py <vanilla_root> [--update]

Without --update it compares the current sites with the baseline beside this
script and exits 1 if a site is new. With --update it rewrites the baseline.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SCAN_DIRS = ["common/decisions", "common/scripted_effects", "common/on_actions",
             "common/balance_of_power", "common/operations", "events"]
EVENT_ID = re.compile(r"^\s*id\s*=\s*([A-Za-z0-9_.]+)")
DEC_ID = re.compile(r"^\t{1,2}([A-Za-z0-9_]+)\s*=\s*\{")
SE_NAME = re.compile(r"^([A-Za-z0-9_]+)\s*[:=]\s*\{?\s*$")
OP_ID = re.compile(r"^([A-Za-z0-9_]+)\s*=\s*\{")
ON_ACTION_ID = re.compile(r"^\s*(on_[A-Za-z0-9_]+)\s*=\s*\{")
# Generic DSL keys are not decision ids; skip them so the baseline names the
# decision, not its inner block.
GENERIC_KEYS = {
    "timeout_effect", "remove_effect", "complete_effect", "cancel_effect",
    "ai_will_do", "available", "visible", "activation", "targeted_modifier",
    "modifier", "effect", "immediate", "option", "trigger", "select_effect",
    "custom_effect_tooltip", "cancel_trigger", "targets", "highlight_states",
    "on_complete", "completion_reward", "allowed", "icon", "cost",
    "target_root_trigger", "target_trigger", "target_array",
}
BASELINE = Path(__file__).with_name("check_cw_fuses_baseline")


def id_matcher(rel: str):
    if rel.startswith("events/"):
        return EVENT_ID
    if rel.startswith("common/decisions/"):
        return DEC_ID
    if rel.startswith("common/scripted_effects/"):
        return SE_NAME
    if rel.startswith("common/on_actions/"):
        return ON_ACTION_ID
    return OP_ID


def current(root: Path) -> set[str]:
    out: set[str] = set()
    for d in SCAN_DIRS:
        base = root / d
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*.txt")):
            rel = p.relative_to(root).as_posix()
            if "national_focus" in rel:
                continue
            rx = id_matcher(rel)
            cur = "?"
            for ln in p.read_text(encoding="utf-8-sig", errors="replace").splitlines():
                # A real fuse is a `start_civil_war = {` effect. Skip comments
                # and display-only tooltips, which contain the same substring.
                code = ln.split("#", 1)[0]
                if "custom_effect_tooltip" in code or "effect_tooltip" in code:
                    continue
                m = rx.match(ln)
                if m and "start_civil_war" not in ln and m.group(1) not in GENERIC_KEYS:
                    cur = m.group(1)
                if "start_civil_war" in code:
                    out.add(f"{rel}:{cur}")
    return out


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: check_cw_fuses.py <vanilla_root> [--update]", file=sys.stderr)
        return 2
    root = Path(sys.argv[1])
    now = current(root)
    if "--update" in sys.argv:
        BASELINE.write_text("\n".join(sorted(now)) + "\n", encoding="utf-8")
        print(f"baseline written: {len(now)} sites")
        return 0
    if not BASELINE.is_file():
        print("no baseline; run with --update", file=sys.stderr)
        return 2
    base = set(BASELINE.read_text(encoding="utf-8").split())
    new = sorted(now - base)
    gone = sorted(base - now)
    if new:
        print(f"new civil-war fuses (review and gate): {len(new)}")
        for s in new:
            print(f"  {s}")
        return 1
    if gone:
        print(f"note: {len(gone)} baseline fuses are gone (a game update?)")
    print(f"ok: no new civil-war fuses ({len(now)} sites)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
