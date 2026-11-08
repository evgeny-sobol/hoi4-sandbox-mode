#!/usr/bin/env python3
"""Check that the monthly rivalry delta equals the terms that produced it.

`update_rivalry_monthly()` in core
`common/scripted_effects/99_sandbox_scripted_effects.hsl` sums these terms:

    +2  we are at war with the rival          (w)
    +2  we own a state they have a core on    (cu)
    +2  they own a state we have a core on    (ct)
    +1  enemy ideology                        (id)
    -1  same government                       (same)
    -1  non-aggression pact                   (pact)
    +1  they fight a country we are friends with (fr)
    +1  slot 0 only: authoritarian ruler      (lead, or -1 for liberal)
    -1  when no plus term fired

With `sandbox_log_rival_terms` raised the game writes one `rivals_terms` line per
slot per month naming every term beside the delta it applied, so this check
recomputes the sum from those flags and compares. That is the strong form: it
tests the arithmetic the code actually performed.

Without the probe - an older extract, or a session with the flag off - the check
falls back to a weaker band: the `war=` field in the census is 0.00 exactly when
a country fights nobody, which zeroes the war term and bounds the declared growth
for a country at peace. The band allows the leader bonus on slot 0, because that
term is real and a band that ignores it reports failures that are not failures.

Usage:
    check_rivalry_delta.py <extract.txt> [--verbose]

Exit 0 when every judged pair-month matches, 1 when one does not, 2 when the
extract yields nothing to judge (a silent pass would claim coverage it does not
have).
"""

from __future__ import annotations

import argparse
import collections
import pathlib
import re
import sys

MONTHS = {
    m: i
    for i, m in enumerate(
        "January February March April May June July August September October "
        "November December".split(),
        1,
    )
}

CENSUS = re.compile(
    r"(\d+) (\w+), (\d{4}) ([A-Z0-9]{3}) census .*?"
    r"r0=(\S+) r1=(\S+) r2=(\S+)"
)
RIVAL = re.compile(r"^([A-Z0-9]{3}):([0-9.]+)$")
WAR = re.compile(r" war=([0-9.]+)")

# Terms as the game reports them.
TERMS = re.compile(
    r"([A-Z0-9]{3}) rivals_terms slot=(\d+) other=(\S+) "
    r"w=(-?\d+) cu=(-?\d+) ct=(-?\d+) id=(-?\d+) same=(-?\d+) pact=(-?\d+) "
    r"fr=(-?\d+) lead=(-?\d+) plus=(-?\d+) d=(-?\d+)"
)

# Fallback band for a country at peace, when the probe is not in the extract.
# +2 on slot 0: enemy ideology (+1) and the authoritarian ruler bonus (+1).
# -3 at the floor: same government, a pact, and the no-plus decay.
PEACE_SLOT0_MAX = 2.0
PEACE_MAX = 1.0
PEACE_MIN = -3.0


def recompute(m, offset):
    w, cu, ct, idv, same, pact, fr, lead, plus, d = (
        int(m.group(offset + i)) for i in range(10)
    )
    expected_plus = w + cu + ct + idv + fr + (1 if lead == 1 else 0)
    expected = 2 * w + 2 * cu + 2 * ct + idv - same - pact + fr + lead
    if expected_plus == 0:
        expected -= 1
    return expected_plus, expected, d


def check_probe(path: pathlib.Path, verbose: bool):
    """Recompute from the per-term flags. Returns (judged, problems, report)."""
    judged = 0
    problems = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = TERMS.search(line)
        if not m:
            continue
        judged += 1
        expected_plus, expected_delta, reported_delta = recompute(m, 4)
        if m.group(12) and int(m.group(12)) != expected_plus:
            problems.append(
                f"  {m.group(1)} slot{m.group(2)} {m.group(3)}: plus reported "
                f"{m.group(12)}, terms give {expected_plus}"
            )
        elif reported_delta != expected_delta:
            problems.append(
                f"  {m.group(1)} slot{m.group(2)} {m.group(3)}: delta reported "
                f"{reported_delta}, terms give {expected_delta}"
            )
    return judged, problems


def check_band(path: pathlib.Path):
    """Fallback: bound a peaceful country's growth from the census alone."""
    series = collections.defaultdict(list)
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = CENSUS.search(line)
        if not m:
            continue
        day, month, year, country = m.group(1), m.group(2), m.group(3), m.group(4)
        if month not in MONTHS:
            continue
        ordinal = int(year) * 1000 + MONTHS[month] * 40 + int(day)
        w = WAR.search(line)
        war = float(w.group(1)) if w else 0.0
        for slot in range(3):
            rm = RIVAL.match(m.group(5 + slot))
            if not rm or rm.group(1) == "0":
                continue
            series[(country, slot)].append(
                (ordinal, rm.group(1), float(rm.group(2)), war)
            )
    judged = 0
    problems = []
    for (country, slot), rows in sorted(series.items()):
        rows.sort()
        for (o1, r1, s1, w1), (o2, r2, s2, w2) in zip(rows, rows[1:]):
            if r1 != r2 or o2 <= o1 or w1 != 0.0 or w2 != 0.0:
                continue
            if s2 >= 100.0 or s1 <= 0.0:
                continue
            judged += 1
            delta = round(s2 - s1, 1)
            top = PEACE_SLOT0_MAX if slot == 0 else PEACE_MAX
            if delta > top or delta < PEACE_MIN:
                problems.append(
                    f"  {country} slot{slot} {r1} @{o2}: delta {delta:+.1f} "
                    f"({s1:.0f} -> {s2:.0f}) while war=0.00, band is "
                    f"{PEACE_MIN:+.0f}..{top:+.0f}"
                )
    return judged, problems


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("extract", type=pathlib.Path)
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args(argv)

    if not args.extract.is_file():
        print(f"no extract at {args.extract}", file=sys.stderr)
        return 2

    judged, problems = check_probe(args.extract, args.verbose)
    mode = "per-term probe"
    if judged == 0:
        judged, problems = check_band(args.extract)
        mode = "census band (no probe lines in this extract)"

    print(f"mode: {mode}")
    print(f"pair-months judged: {judged}")
    if problems and args.verbose:
        print("problems:")
        for p in problems[:40]:
            print(p)
        if len(problems) > 40:
            print(f"  ... {len(problems) - 40} more")

    if judged == 0:
        print("problems: 1 - nothing to judge; a pass here would claim coverage "
              "this run does not have")
        return 2
    if problems:
        print(f"problems: {len(problems)}")
        return 1
    print("problems: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
