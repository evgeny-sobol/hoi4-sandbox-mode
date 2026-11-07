#!/usr/bin/env python3
"""Guard the rival slot invariant (issue 08): one rival, one slot.

Two independent signals over a session extract, because each covers what the
other cannot:

* **Event stream** - replays `rivals_set` into a per-country three-slot model and
  flags a write whose tag already occupies a different slot. Covers all 131
  countries that ever touch a slot, but it only sees writes that happen inside the
  extract window, and a lost write makes later state wrong rather than obvious.
* **Monthly `census`** - flags a row whose two `rN=` fields name the same tag.
  Covers far fewer countries (the trigger is a fixed list of majors), but it is a
  direct observation of the state, not a reconstruction, so it cannot drift.

Neither is redundant: the census caught HUN holding FRA twice for seventeen
months, and the event stream caught four countries the census never prints.

Usage:
    python check_rival_slot_uniqueness.py [extract] [--verbose]

Defaults to the standard logs location. Exit code 1 when anything is found.

Trap this exists to catch: the invariant is enforced at two write paths and one
score gate, all of which can regress independently, and a duplicate is silent -
no error line, no failed log, just a country whose rivalry climbs twice as fast.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

DEFAULT_EXTRACT = Path(
    os.path.expandvars(
        "%USERPROFILE%/Documents/Paradox Interactive/Hearts of Iron IV/logs/sandbox_extract.txt"
    )
)

# `#sandbox  1:00, 1 February, 1936 GER rivals_set 0.00->50.00 d=50.00 age=0 other=USA slot=0 ...`
EVENT = re.compile(
    r"\b(?P<country>[A-Z]{3}) (?P<kind>rivals_set|rivals_clear_\w+)"
    r".*?other=(?P<other>[A-Z0-9]{3}) slot=(?P<slot>[0-2])\b"
)
# `#sandbox  1:00, 1 February, 1936 GER census ... r0=USA:54 r1=ENG:53 r2=LIT:52 ...`
CENSUS = re.compile(
    r"\b(?P<country>[A-Z]{3}) census\b.*?"
    r"r0=(?P<r0>\S+) r1=(?P<r1>\S+) r2=(?P<r2>\S+)"
)


def tag_of(field: str) -> str | None:
    """`USA:54` -> USA. An empty slot renders as `0`."""
    if field == "0" or ":" not in field:
        return None
    return field.split(":", 1)[0]


def scan_events(lines: list[str]) -> tuple[list[str], int]:
    """Replay the event stream; return duplicate writes and the event count."""
    state: dict[str, dict[int, str | None]] = {}
    problems: list[str] = []
    events = 0
    for line in lines:
        m = EVENT.search(line)
        if not m:
            continue
        events += 1
        country, kind, other, slot = (
            m.group("country"),
            m.group("kind"),
            m.group("other"),
            int(m.group("slot")),
        )
        slots = state.setdefault(country, {0: None, 1: None, 2: None})
        if kind == "rivals_set":
            already = [s for s, v in slots.items() if v == other and s != slot]
            if already:
                problems.append(
                    f"{country}: set {other} into slot {slot}, already held in slot {already[0]}"
                )
            slots[slot] = other
        else:
            # A clear frees the slot only when it names the tag that sits there;
            # a mismatch means our reconstruction is behind, not that the guard
            # should invent a failure.
            if slots.get(slot) == other:
                slots[slot] = None
    return problems, events


def scan_census(lines: list[str]) -> tuple[list[str], int]:
    """Return repeated tags inside one census row, and the row count."""
    problems: list[str] = []
    rows = 0
    parsed = 0
    for line in lines:
        m = CENSUS.search(line)
        if not m:
            continue
        rows += 1
        fields = [m.group(f"r{i}") for i in range(3)]
        tags = [t for t in (tag_of(f) for f in fields) if t]
        if tags:
            parsed += 1
        if len(tags) != len(set(tags)):
            country = m.group("country")
            dupes = sorted({t for t in tags if tags.count(t) > 1})
            problems.append(f"{country}: census shows {', '.join(dupes)} in more than one slot")
    # A census row whose slots carry no `TAG:strength` field at all means the
    # census line itself is broken, not that the slots are clean. This exact
    # shape shipped once: a cached-string cosmetics printed floats
    # (`r0=10780.22997`) on 524 of 526 rows, and a guard that only counted tags
    # reported "0 repeated tags" - vacuously true and useless.
    if rows and parsed == 0:
        problems.append(
            f"census carries no parseable TAG:strength field in any of {rows} rows - the census line itself is broken"
        )
    elif rows and parsed < rows:
        problems.append(f"census: only {parsed} of {rows} rows carry a parseable TAG:strength field")
    return problems, rows


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Guard rival slot uniqueness over a session extract.")
    parser.add_argument("extract", nargs="?", type=Path, default=DEFAULT_EXTRACT,
                        help="path to sandbox_extract.txt")
    parser.add_argument("--verbose", action="store_true", help="list every problem, not just the first few")
    args = parser.parse_args(argv)

    if not args.extract.is_file():
        print(f"error: no such extract: {args.extract}", file=sys.stderr)
        return 2
    lines = args.extract.read_text(encoding="utf-8", errors="replace").splitlines()

    event_problems, events = scan_events(lines)
    census_problems, rows = scan_census(lines)
    problems = event_problems + census_problems

    limit = None if args.verbose else 12
    print(f"event stream: {events} slot events, {len(event_problems)} duplicate write(s)")
    for p in (event_problems if limit is None else event_problems[:limit]):
        print(f"  {p}")
    print(f"census: {rows} row(s), {len(census_problems)} with a repeated tag")
    for p in (census_problems if limit is None else census_problems[:limit]):
        print(f"  {p}")

    if problems and limit is not None and len(problems) > limit:
        print(f"  ... {len(problems) - limit} more (use --verbose)")

    print(f"problems: {len(problems)}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
