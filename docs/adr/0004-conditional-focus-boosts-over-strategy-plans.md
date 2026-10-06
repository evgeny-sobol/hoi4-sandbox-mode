# Keep conditional focus boosts instead of vanilla strategy plans

Status: accepted

## Context

The focus-driving slice (boost splices, focus graphs, `paths` in arc specs)
looked replaceable by vanilla `ai_strategy_plans`: an ordered
`ai_national_focuses` list with day offsets guarantees what an aggressor
takes, and our own `GER_sandbox_strategy_plan` already uses that mechanism
for single-focus forcing. A grill session (2026-10-03) tested whether the
slice overengineers what vanilla gives for free, and fixed its semantics
first: the director provides priority, never a guarantee — the aggressor
must stay unpredictable.

## Decision

Keep the custom slice, with priority semantics:

- Boosts stay `ai_will_do`-style splices gated on the live aggressor
  (`is_live_scenario_aggressor()`), so a country is steered only while its
  arc runs. Static vanilla weights or plans cannot express that condition.
- The boost closure (key focuses plus prerequisite ancestors, computed from
  the focus graphs) stays: a boosted key the AI cannot reach is dead weight,
  and vanilla lists include whole chains for the same reason.
- `paths` keep their order for diagrams and design reading even though only
  membership reaches the game.
- `sc_focus` telemetry splices stay regardless: strategy plans cannot log.

## Considered Options

- **Per-arc ai_strategy_plans generated from spec paths (rejected).** Gives
  strict order, but strict order is a guarantee and the grill fixed priority
  as the wanted semantics. An unpredictable aggressor must not march a
  scripted list.
- **Static ai_will_do weights on scenario focuses (rejected).** Loses the
  live-aggressor condition: countries would be steered down scenario paths
  in sessions where they run no arc.
- **Boost keys only, drop the ancestor closure (rejected).** The AI cannot
  path to unreached keys; the graph already exists and is checked.
- **Keep conditional boosts with closure (chosen).** Every piece carries a
  load vanilla cannot: conditionality, reachability, design docs, logging.

## Consequences

- The focus graphs, the exporter and the boost guards stay load-bearing
  tooling, not legacy: removing any of them must re-argue Q4-Q6 above.
- If priority ever becomes guarantee (a future decision that aggressors
  must march scripted lists), this ADR inverts: generated strategy plans
  become the mechanism and the boost splices go.
