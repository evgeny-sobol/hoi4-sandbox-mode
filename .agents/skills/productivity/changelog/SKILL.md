---
name: changelog
description: Write a player-facing changelog entry for a mod release.
disable-model-invocation: true
---

Write one release entry covering everything since the previous release tag,
in the player's language: what changed in the game, not what changed in the code.

Procedure:

1. Find the previous release tag in the mod repo being released
   (`git tag --list --sort=-creatordate`, pattern `vX.Y/vX.Y.Z`) and read
   the new version from that repo's `descriptor.mod` (`version="..."`).
   The entry header is `v<version>:`.
2. List the range: `git log --oneline <tag>..HEAD`. Read every subject;
   open the diff of any commit whose player impact is unclear instead of
   guessing from the message.
3. Draft one bullet per player-visible gameplay change. A change is
   player-visible when a session shows it: wars start or end differently,
   the AI picks different focuses or allies, options appear or disappear,
   errors stop appearing. Telemetry labels, guards, splices, tracers,
   refactors, docs, diagrams, submodule syncs and version bumps are not
   entries.
4. Check every bullet against its commit: the range must contain the
   behavior the bullet claims. Drop anything unverifiable; fold duplicates
   into one bullet. Completion: every commit in the range is either mapped
   to a bullet or classified as internal, the header version matches
   `descriptor.mod`, and the entry reads without repo jargon.

Style:

- Format: header line `vX.Y.Z:` then `* <type>: <one sentence>` bullets.
- Types: `fix` (broken behavior now works), `feat` (new playable content
  or option).
- Lowercase throughout, plain words, one clause per bullet.
- Name game concepts the way the player sees them (ultimatum, wargoal,
  war, ally, scenario). Never internal ids: no `sc_*` lines, focus ids,
  file paths, issue numbers or commit SHAs.
- Carry the before and the after in one breath where it fits: "refusing
  a peak ultimatum now hands the aggressor a wargoal, so standoffs turn
  into wars".

Output:

- Deliver the entry as chat text. There is no changelog file in the repos;
  create one only if the user names a path, and commit nothing unless asked.
