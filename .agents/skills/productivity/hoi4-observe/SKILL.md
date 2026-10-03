---
name: hoi4-observe
description: Run an unattended Hearts of Iron 4 observer session to a target in-game year, then analyze the logs.
disable-model-invocation: true
---

Run one random observer session of the sandbox mod without touching the
keyboard: launch the game headless-ish, poll `game.log` until the in-game
year reaches the target, kill the process, then report what the session
did. Pinned sessions stay manual (game rules have no CLI).

```
python3 .agents/skills/productivity/hoi4-observe/scripts/hoi4_observe.py --mod sandbox --until-year 1940
```

Flags: `--mod sandbox|rt56` (which mod the launcher preset must hold;
default `sandbox`), `--until-year N` (default 1940), `--poll-seconds N`
(default 60), `--max-minutes N` (default 90), `--watchdog-minutes N`
(default 15, abort when the log stops growing), `--analyze-only` (skip
everything, just analyze the current logs).

Exit codes: 0 session reached the year and analysis printed; 1 crashed /
silent log / timeout; 2 bad preconditions.

Procedure:

1. Preconditions (abort before launching on any failure): `hoi4.exe`
   present, no `hoi4.exe` running, `dlc_load.json` enables the expected
   mod descriptor (`mod/_sandbox.mod` or `mod/_sandbox-r56.mod`), logs
   directory present.
2. Empty the `logs` and `save games` folders (counts printed; the game
   recreates what it needs). Saves go too: a stale save next to
   `-nolauncher` risks a resume instead of a fresh 1936 start.
3. Launch detached: `hoi4.exe -nolauncher -debug -historical=no
   -hands_off`. Verified 2026-10-04: this starts a fresh 1936 game as
   Haiti (the observer), unpaused at max speed - it does not resume.
4. Poll the log tail for the newest `[YYYY.MM.DD.HH]` rim date. At
   `YYYY >= --until-year`, `taskkill /F /IM hoi4.exe` (no save; observer
   sessions need none). Crash (process gone early) or a silent log past
   `--watchdog-minutes` aborts with a failure report.
5. Analyze: run `extract_sandbox.py`, print per-line-type counts, the
   decision lines (seed/pick/variant/phase/derail/repick/ignite/crisis/
   target/join), and the `error.log` scenario scan (sandbox/scenario/
   completion_reward hits plus parser errors). The agent reads the verdict
   off that report against the verification checklist.

Safety rules:

- Never launch while another `hoi4.exe` runs; never kill anything but
  `hoi4.exe`.
- Never touch `dlc_load.json`: the launcher owns playsets, the skill only
  verifies them.
- Never commit session logs; they live outside repos.
- Random sessions only. A pinned arc needs the lobby and stays manual.
