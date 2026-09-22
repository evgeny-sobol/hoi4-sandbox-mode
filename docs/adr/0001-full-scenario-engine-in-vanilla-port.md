# Port the full scenario engine to the vanilla mod

The vanilla mod (`_sandbox`) historically described the scenario port as
"content only, no mechanic changes". Deciding how to bring the scenario system
over, we chose to port the **entire engine** (director, `sandbox_targets[]`
with A/B variants, seed, ladder, derail arms, flip gates, join scorer,
ignite-by-war, civil-war derail, all `sc_*` telemetry) with the same file paths
and names as the Rt56 overlay, replacing only the focus/event ids and trimming
the arc pool to the content-portable arcs. "Content only" was read as "do not
change the mechanics while porting", not "do not carry the engine": the engine
is already mod-agnostic by design (targets live in an array, ids are data), so
a content-only port would have meant writing a second, divergent engine.

## Considered Options

- **Content-only port** (no engine): rejected - the vanilla mod has no scenario
  code at all, so this delivers nothing playable.
- **Reduced engine** (no A/B variants, no join levers): rejected - it forks the
  system and loses the features that make the pool replayable.
- **Full engine, same paths** (chosen): the two repos differ only in ids and
  pool composition, so a diff reads as data, not as architecture.
