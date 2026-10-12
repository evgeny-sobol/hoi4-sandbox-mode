# External Directories

The agent's working directory is the `_sandbox` mod, but relevant files live in six directories. Consult all reachable ones before answering; do not assume everything is inside the working directory.

| Path                                                                               | Contents                                                                                                     | Access                                                                                        |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `C:\Games\Steam\steamapps\common\Hearts of Iron IV`                                | Vanilla game files; reference for base mechanics, vanilla focuses, triggers, effects                         | Read-only: never edit, create, or delete files here                                           |
| `C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox`     | This repo (working directory); sandbox-only overhaul of vanilla                                              | Editable: primary place for edits                                                             |
| `C:\Games\Steam\steamapps\workshop\content\394360\820260968`                       | The Road to 56 workshop mod; reference for Rt56-only content                                                 | Read-only: never edit, create, or delete files here                                           |
| `C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56` | Adaptation of the `_sandbox` mod for Rt56                                                                    | Editable via absolute path when the task touches the Rt56 adaptation                          |
| `C:\Users\evgeny\Repos\HoI4\sandbox-mod-core`                                      | Shared modules used by both `_sandbox` and `_sandbox-r56`; authoritative source of `core/` submodule content | Editable via absolute path when the task touches shared behavior                              |
| `C:\Users\evgeny\Repos\HoI4\hsl`                                                   | A Python-like language that compiles to Hearts of Iron IV (Clausewitz) script                                | Editable via absolute path when the optimal way to implement the task requires changes to HSL |

## Rules

- Always use absolute paths when reading or editing outside the working directory. Do not guess relative paths between these directories.
- Read-only means read-only: use `read`/`grep` there, never `edit`/`write`/`shell` redirection. To override shared or upstream behavior, change the editable mod or core repo instead.
- Shared behavior lives in `sandbox-mod-core`: never edit a synced copy under `core/` to change shared behavior. Edit the authoritative file in `C:\Users\evgeny\Repos\HoI4\sandbox-mod-core` (or under `core/` as its checkout), then sync outward per `.cursor/rules/sync-core-first.mdc`. Per-mod catalogs stay editable in each mod.
- Cross-mod portability is per-mod (see `CONTEXT.md`: `Content-portable arc`): an arc portable in `_sandbox` is not automatically portable in `_sandbox-r56`. Verify against the target mod's files, not from memory.
- If a requested change spans repos (e.g. core + both mods), state which files change in which directory; do not silently limit the change to the working directory.
