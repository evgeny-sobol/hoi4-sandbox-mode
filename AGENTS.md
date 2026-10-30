# Agent rules

Standing rules live as plain markdown in `.agents/rules/`, one file per rule. Read every rule that matches the task before acting; they are not optional. Shared rules are authored in `sandbox-mod-core` and synced into both mods. A mod may add its own rule files to the same directory (for example `r56-overlay.md` in `_sandbox-r56`); those are local and are never synced.

- `issue-tracker.md`: issues and specs are local markdown under `.scratch/`.
- `triage-labels.md`: five canonical triage roles, label strings equal to role names.
- `domain.md`: single-context domain docs, root `CONTEXT.md` plus `docs/adr/`.
- `external-dirs.md`: work spans six directories (vanilla, Rt56, both mods, shared core, HSL).
- `consult-gdd.md`: read `docs/gdd/` for the intended design before changing it.
- `sync-core-first.md`: sync `core/` before editing shared files, and commit core before the mod.
- `compile-after-hsl.md`: compile after any `.include`, `.hsl`, or `.hml` change.
- `analyze-sandbox-logs.md`: read `game.log` through `.scratch/scripts/extract_sandbox.py`.

Global rules in `~/.agents/rules/` (`language.md`, `characters.md`, `git-conventions.md`, `ignore-directories.md`, `python-venv.md`, `no-unauthorized-installations.md`) apply on top; this file does not restate them.
