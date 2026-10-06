# Join filters run through one flagged scorer, and joiners are generated

The join lever needs optional, composable candidate-pool filters (same
ideology, same continent) instead of a scorer per combination. We keep the
single shared `scenario_join_scorer` and let it read per-call filter flags
(`scenario_join_same_ideology`, `scenario_join_same_continent`), and we make
the builder generate every `sandbox_select_<key>_joiners()` from the arc spec
so `[joiners] select/n/require` stops being validated-but-unused. Rejected: N
duplicated scorer functions (combinatorial, and the six pre-existing per-arc
hand bodies had already drifted from the spec they describe).
