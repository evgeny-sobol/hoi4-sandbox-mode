#!/usr/bin/env python3
"""Build Mermaid focus-path diagrams for every scenario arc.

Reads the pre-generated Mermaid focus graphs under docs/gdd/National Focuses/
(one .md per country: `# <branch_root>` sections, each a `flowchart TD`
with `nN["ID"]` / `nN(("ID"))` / `nN{"ID"}` nodes and `nA --> nB`
(prerequisite) / `nA x--x nB` (mutually exclusive) edges).

For each scenario arc it emits a compact Mermaid subgraph: the arc's key
focuses (the ones the director boosts / logs) plus the prerequisite and
mutual-exclusion edges among them. Output is grouped per aggressor country
with one `subgraph` per arc, ready to paste into docs/gdd/Scenarios.md.

Usage:
    python build_scenario_graphs.py
"""
from __future__ import annotations

import re
from pathlib import Path

GDD = Path(__file__).resolve().parents[2] / "docs" / "gdd" / "National Focuses"

NODE_RE = re.compile(r'^\s*(n\d+)(?:\(\(|\[\{?|\{)(.*?)(?:\)\)|\]|\})\s*$')
EDGE_RE = re.compile(r"^\s*(n\d+)\s*(-->|x--x)\s*(n\d+)")


def load_graph(path: Path):
    """Return (prereq, excl) as {focus_id: {parent_id}} / {(a,b)} sets."""
    text = path.read_text(encoding="utf-8")
    id_by_node: dict[str, str] = {}
    for raw in text.splitlines():
        m = NODE_RE.match(raw)
        if m:
            id_by_node[m.group(1)] = m.group(2).strip().strip('"')
    prereq: dict[str, set[str]] = {}
    excl: set[tuple[str, str]] = set()
    for raw in text.splitlines():
        e = EDGE_RE.match(raw)
        if not e:
            continue
        a, kind, b = e.groups()
        fa, fb = id_by_node.get(a), id_by_node.get(b)
        if not fa or not fb:
            continue
        if kind == "-->":
            prereq.setdefault(fb, set()).add(fa)
        else:
            excl.add((fa, fb))
    return prereq, excl


def ancestors(fid, prereq, max_depth):
    """All prerequisite ancestors of fid, up to max_depth hops."""
    seen: set[str] = set()
    frontier = {fid}
    for _ in range(max_depth):
        nxt: set[str] = set()
        for f in frontier:
            for p in prereq.get(f, ()):
                if p not in seen and p != fid:
                    seen.add(p)
                    nxt.add(p)
        frontier = nxt
        if not frontier:
            break
    return seen


def render_arc(name, keys, prereq, excl, roots=(), depth=3):
    """Mermaid flowchart for one arc: key focuses plus their prerequisite
    paths (bounded depth). Keys are double-bordered, path roots are rounded,
    intermediate path focuses are plain."""
    keyset = set(keys)
    keep = set(keyset)
    for k in keys:
        keep |= ancestors(k, prereq, depth)

    kept_edges = [(p, b) for b in keep for p in prereq.get(b, ()) if p in keep]
    has_parent = {b for _, b in kept_edges}
    rootset = set(roots) | {f for f in keep if f not in has_parent}

    out = ["```mermaid", "flowchart TD", f"    subgraph {name}"]
    for fid in sorted(keep):
        if fid in rootset:
            out.append(f'        {fid}(["{fid}"])')
        elif fid in keyset:
            out.append(f'        {fid}[["{fid}"]]')
        else:
            out.append(f'        {fid}["{fid}"]')
    for p, b in sorted(set(kept_edges)):
        out.append(f"        {p} --> {b}")
    for a, b in sorted(excl):
        if a in keep and b in keep:
            out.append(f"        {a} x--x {b}")
    out.append("    end")
    out.append("```")
    return "\n".join(out)


# arc id -> (title, aggressor file, key focuses, root focuses among keys)
ARCS = [
    (1, "Axis expansion", "germany",
     ["GER_danzig_or_war", "GER_demand_sudetenland", "GER_war_with_france", "GER_around_maginot",
      "GER_remilitarize_the_rhineland", "GER_anschluss"], ()),
    (2, "Soviet southern thrust", "soviet",
     ["SOV_preemptive_invasion_of_iran"], ()),
    (3, "Japanese expansion", "japan",
     ["JAP_reinforce_the_beijing_garrison", "JAP_strike_the_southern_road",
      "JAP_revisit_the_thirteen_demands", "JAP_occupy_siam"], ()),
    (4, "Italian expansion", "italy",
     ["ITA_italys_destiny", "ITA_war_with_greece",
      "ITA_foreign_affairs", "ITA_ratify_the_stresa_front"], ()),
    (5, "British anti-Soviet drive", "uk",
     ["ENG_war_with_ussr", "ENG_embargo_ussr", "ENG_steady_as_she_goes"], ()),
    (6, "American war plan", "usa",
     ["USA_war_plan_orange", "USA_war_plan_black", "USA_defense_of_the_pacific",
      "USA_intervention_in_europe"], ()),
]


def main():
    graphs: dict[str, tuple] = {}
    for _, _, country, _, _ in ARCS:
        if country not in graphs:
            path = GDD / f"{country}.md"
            if not path.is_file():
                raise SystemExit(f"missing focus graph: {path}")
            graphs[country] = load_graph(path)

    by_country: dict[str, list] = {}
    for arc, title, country, keys, roots in ARCS:
        by_country.setdefault(country, []).append((arc, title, keys, roots))

    for country, arcs in by_country.items():
        prereq, excl = graphs[country]
        print(f"\n<!-- {country} -->")
        for arc, title, keys, roots in arcs:
            print(f"\n#### Arc {arc}: {title}\n")
            print(render_arc(f"arc{arc}", keys, prereq, excl, roots))


if __name__ == "__main__":
    main()
