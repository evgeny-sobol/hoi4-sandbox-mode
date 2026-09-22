#!/usr/bin/env python3
"""Extract #sandbox telemetry lines from a HoI4 game.log into a text file.

Usage:
    python extract_sandbox.py [game_log] [out_file]

Defaults:
    game_log = %USERPROFILE%/Documents/Paradox Interactive/Hearts of Iron IV/logs/game.log
    out_file = <game_log_dir>/sandbox_extract.txt

Exits 0 with at least one match, 1 otherwise. Prints stats to stderr.

The rim prefix (e.g. `[22:20:15]...`) repeats on every effect line; the
extracted file keeps only the payload after the second timestamp bracket,
so a `#sandbox` line reads `1936.1.1.12 12:00 ... payload`.
"""

import os
import sys
from pathlib import Path

MARKER = "#sandbox"
DEFAULT_LOG = Path(
    os.path.expandvars("%USERPROFILE%/Documents/Paradox Interactive/Hearts of Iron IV/logs/game.log")
)


def payload(line: str) -> str:
    """Strip the effectbase prefix; keep one date/time and the payload.

    A line looks like:
    [22:20:15][1936.01.01.12][effectbase.cpp:1799]: [22:20:15][1936.01.01.12][effectbase.cpp:1783]: #sandbox ...
    We drop everything up to and including the second ']: '.
    """
    marker = line.find(MARKER)
    if marker < 0:
        return line
    # Cut back to the last ']: ' before the marker so we keep a readable
    # date + time in the output.
    sep = line.rfind("]: ", 0, marker)
    head = line[sep + 3:] if sep >= 0 else line
    return head.rstrip("\n")


def main(argv: list[str]) -> int:
    src = Path(argv[1]) if len(argv) > 1 else DEFAULT_LOG
    dest_text = argv[2] if len(argv) > 2 else str(src.with_name("sandbox_extract.txt"))
    dest = Path(dest_text)

    if not src.is_file():
        print(f"error: no such log: {src}", file=sys.stderr)
        return 1

    hits: list[str] = []
    with src.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if MARKER in line:
                hits.append(payload(line))

    with dest.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(hits))
        fh.write("\n")

    print(f"extracted {len(hits)} #sandbox lines", file=sys.stderr)
    print(f"wrote {dest}", file=sys.stderr)
    return 0 if hits else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))