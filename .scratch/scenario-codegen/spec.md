# Scenario mechanics generated from arc specs

Status: ready-for-agent
Type: enhancement

## Problem Statement

A game designer can describe an arc's decisions in a TOML spec, but turning
those decisions into a running scenario still means hand-writing hundreds of
lines of HSL: target seeding, ladder dispatch, telemetry blocks, derail arms
and pick branches. Every hand-written line is a chance to disagree with the
spec (a wrong tag, a stale threshold, a missing label), and the same drift the
spec system was built to kill re-enters through the code. The designer wants
the mechanics derived from the spec the same way the catalog, the diagrams,
the boosts and the labels already are.

## Solution

The catalog builder CLI gains a second output: beside the generated catalog it
emits a generated HSL sibling file holding the arc's mechanics, derived from
the same spec. Hand-written code keeps the shared loops and all content
(`fire_*` functions, event texts, localisation); generated code holds exactly
what the spec already says (targets, ladder months, telemetry pairs, derail
conditions, pick data). Because only one arc has a spec in each mod so far,
generation is per-arc from day one: the hand dispatcher calls a generated
per-arc function, and the arc's old hand-written branches are deleted in the
same change, so no definition exists twice.

## User Stories

1. As a game designer, I want the target seeding derived from the spec's
   targets, so that a tag I change in TOML cannot linger in the code.
2. As a game designer, I want the ladder thresholds derived from the spec, so
   that the tick fires crises and peak on the months I wrote.
3. As a game designer, I want the telemetry blocks derived from the spec's
   pairs, so that every declared pair is sampled and no undeclared pair is.
4. As a game designer, I want the derail arms derived from the spec's targets
   and gate, so that the gone/capitulated arms and the flip gate match the
   design without hand-editing.
5. As a game designer, I want the pick branch and the pin data derived from
   the spec's number and aggressor, so that a new arc becomes selectable
   without touching the dispatcher by hand.
6. As a game designer, I want the crisis and ultimatum events to stay
   hand-written, so that event content and option design remain prose and
   logic, not data.
7. As a game designer, I want the generated file overwritten on every build
   and marked do-not-edit, so that I never wonder which copy is true.
8. As a game designer, I want a build failure when my spec's number matches no
   arc the code knows, so that a misnumbered arc surfaces before the game.
9. As a game designer, I want the generated output for the tracer arc compared
   against the hand-written code it replaces, so that I can see the generator
   reproduces proven behaviour.
10. As a maintainer, I want the shared tick loop to stay hand-written and call
    generated per-arc branches, so that phase and counter logic is fixed once
    instead of emitted per mod.
11. As a maintainer, I want one generated function per arc per aspect, so that
    migrating the next arc touches nothing already generated.
12. As a maintainer, I want the old hand-written branches of a migrated arc
    deleted in the same change, so that no definition exists twice.
13. As a maintainer, I want the label check to scan the generated file too, so
    that generated log lines obey the same label contract.
14. As a maintainer, I want the existing check mode to cover the new output, so
    that a stale generated file is a build error like every other artifact.
15. As a maintainer, I want the core tooling shared and the specs per-mod, so
    that the two-mod split from the earlier decision holds.
16. As an agent, I want a single CLI seam with golden-text tests, so that I can
    verify generation without launching the game.
17. As an agent, I want the generated per-arc function names to follow one
    contract, so that the hand dispatcher calls them without surprises.
18. As an agent, I want the compiler exit code and an observer session as the
    final gates, matching how every earlier change in this area was verified.

## Implementation Decisions

**Scope.** Only mechanics derivable from the spec are generated: target
seeding, ladder dispatch branches, telemetry blocks, derail arms, pick branch
and pin data. Crisis and ultimatum events, `fire_*` content, event texts and
localisation stay hand-written.

**Split.** The generated code lives in a generated sibling of the hand
catalog, overwritten on every build and marked do-not-edit. The hand catalog
keeps the shared loops, the content functions and the dispatcher branches of
arcs without specs.

**Calling direction.** The hand dispatcher calls generated per-arc functions;
never the reverse. The shared tick loop stays hand-written (phase counting and
counters are fixed once); it calls one generated branch function per migrated
arc. The contract for those functions:

```
gen_<arc>_<aspect>()
```

No arguments; they operate on the engine globals like all scenario code, where
`<arc>` is the spec id slug and `<aspect>` is one of the mechanical aspects
(targets, seed, tick branch, telemetry, derail, pick). The hand-written
branches of a migrated arc are deleted in the same change.

**Tracer.** The vanilla axis arc is migrated first: its spec already exists, so
the generated output is compared against the proven hand-written code it
replaces before the old branches are removed.

**Labels.** The expected-label inventory already covers spec pairs; the check
scans the generated file as well as the hand catalog, so generated log lines
obey the same lowercase pair contract.

**Numbers.** Spec numbers are already validated against the code dispatcher;
generation additionally fails when a spec's number matches nothing the
dispatcher knows.

**Supersession.** This direction reverses the earlier rejected option recorded
in ADR-0002; implementing it supersedes that ADR with a new one.

## Testing Decisions

A good test asserts external behaviour through the CLI seam: given fixture
specs, the build emits the expected generated text, and the check fails when
the generated file on disk differs. Tests must not assert on generator
internals.

Prior art in this codebase: the process-level harness around the catalog
builder CLI (exit codes plus output and file contents), the `--check` modes of
the sync and label tooling used as build gates, and the compiler exit code.

Modules to test:

- The catalog builder CLI: golden text of the generated mechanics for the
  tracer spec, green check after build, red check after a spec edit, red check
  when the generated file is hand-edited.
- The per-arc function contract: the hand dispatcher finds every generated
  function the build emits (no dangling calls, no duplicate definitions).
- The game gates stay as they are: clean recompile of both mods and an
  observer session reading the acceptance checklist.

## Out of Scope

- Crisis and ultimatum event content, `fire_*` functions, event texts and
  localisation; all hand-written.
- Migrating any arc beyond the vanilla tracer; each further arc is its own
  change following the same shape.
- The r56 mod; the tracer is vanilla only.
- Changing what any probe samples or what the ladder does; generation
  reproduces proven behaviour, nothing more.
- A cross-mod comparison of the two mods' specs; accepted drift stands.

## Further Notes

- The axis spec, the validator, the number-vs-dispatcher check and the label
  inventory already exist from the earlier work; this spec builds strictly on
  top of them.
- The migration-era splice modes are unaffected: generated telemetry lines
  carry the same labels the label check already scans.
- If the tracer shows the schema cannot express some mechanical need, fix the
  schema (and its validator, docs and tests) before migrating further, the same
  way the earlier tracer governed the catalog work.
