#!/usr/bin/env python3
"""Export HoI4 national focus trees into Mermaid diagram Markdown files.

Usage:
    python export_focus_graphs.py [--mode swimlane|flowchart] [--src DIR] [--out DIR]

Reads common/national_focus/*.txt (default: in the current project tree) and writes
Markdown files into docs/gdd/National Focuses/, mirroring the source name.
Each Markdown file contains one diagram per root focus (a focus without
prerequisites) and all of its descendants; focuses not reachable from any
root are grouped into an "orphans" diagram.

Modes:
    swimlane (default)  swimlane-beta TD, one lane per depth tier
                        (distance from the root of the sub-diagram).
    flowchart           flowchart TD, plain node list plus edges.
"""
import argparse
import re
from pathlib import Path

FOCUS_PATTERN = re.compile(r"^\s*id\s*=\s*(\S+)", re.IGNORECASE)
FOCUS_OPEN_PATTERN = re.compile(
    r"(?<![A-Za-z_])(?:shared_focus|joint_focus|focus)\s*=\s*\{", re.IGNORECASE
)
PREREQ_BLOCK_PATTERN = re.compile(r"prerequisite\s*=\s*\{([^}]*)\}", re.IGNORECASE | re.DOTALL)
MUTEX_BLOCK_PATTERN = re.compile(r"mutually_exclusive\s*=\s*\{([^}]*)\}", re.IGNORECASE | re.DOTALL)
FOCUS_REF_PATTERN = re.compile(r"(?<![A-Za-z_])focus\s*=\s*(\S+)", re.IGNORECASE)


def strip_comments(text: str) -> str:
    """Blank out # line comments, keeping code inside quoted strings."""
    out: list[str] = []
    for line in text.splitlines(keepends=True):
        in_string = False
        cut = None
        i = 0
        while i < len(line):
            ch = line[i]
            if in_string:
                if ch == "\\":
                    i += 2
                    continue
                if ch == '"':
                    in_string = False
            else:
                if ch == '"':
                    in_string = True
                elif ch == "#":
                    cut = i
                    break
            i += 1
        out.append(line[:cut] + "\n" if cut is not None else line)
    return "".join(out)


def matching_brace(text: str, open_index: int) -> int:
    """Return the index of the brace closing the one at open_index, or -1."""
    depth = 0
    for i in range(open_index, len(text)):
        ch = text[i]
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return i
    return -1


def parse_focus_blocks(text: str) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Return mappings from focus id to prerequisite/mutex ids.

    Handles plain focus, shared_focus and joint_focus blocks, ignores
    commented-out code, and matches braces from the block opening brace
    so nested blocks cannot desynchronize the scan.
    """
    prerequisites: dict[str, list[str]] = {}
    mutexes: dict[str, list[str]] = {}
    clean = strip_comments(text)
    for match in FOCUS_OPEN_PATTERN.finditer(clean):
        open_index = match.end() - 1
        close_index = matching_brace(clean, open_index)
        if close_index < 0:
            continue
        block = clean[open_index + 1:close_index]
        focus_id = None
        for line in block.splitlines():
            m = FOCUS_PATTERN.match(line.strip())
            if m:
                focus_id = m.group(1)
                break
        if not focus_id:
            continue
        prereqs: list[str] = []
        mutex_list: list[str] = []
        for m in PREREQ_BLOCK_PATTERN.finditer(block):
            prereqs.extend(FOCUS_REF_PATTERN.findall(m.group(1)))
        for m in MUTEX_BLOCK_PATTERN.finditer(block):
            mutex_list.extend(FOCUS_REF_PATTERN.findall(m.group(1)))
        prerequisites[focus_id] = prereqs
        mutexes[focus_id] = mutex_list
    return prerequisites, mutexes


def sanitize_focus_id(focus_id: str) -> str:
    cleaned = focus_id.strip()
    if cleaned.endswith("}"):
        cleaned = cleaned[:-1].strip()
    return cleaned.strip()


def split_into_diagrams(
    prerequisites: dict[str, list[str]],
    mutexes: dict[str, list[str]],
) -> list[tuple[str, dict[str, list[str]], dict[str, list[str]]]]:
    """Split a focus tree into per-root (root + descendants) subtrees.

    Returns a list of (diagram_title, prerequisites, mutexes) tuples, one
    per root focus, where the title is the root focus id. Orphan focuses
    without any root ancestor form their own single diagram.
    """
    sanitized_prereqs: dict[str, list[str]] = {}
    sanitized_mutexes: dict[str, list[str]] = {}
    children: dict[str, set[str]] = {}
    for focus_id, prereqs in prerequisites.items():
        node = sanitize_focus_id(focus_id)
        if not node:
            continue
        sanitized_prereqs[node] = []
        for prereq in prereqs:
            target = sanitize_focus_id(prereq)
            if target:
                sanitized_prereqs[node].append(target)
                children.setdefault(target, set()).add(node)
    for focus_id, mutex_list in mutexes.items():
        node = sanitize_focus_id(focus_id)
        if not node:
            continue
        sanitized_mutexes[node] = []
        for mutex in mutex_list:
            target = sanitize_focus_id(mutex)
            if target:
                sanitized_mutexes[node].append(target)

    diagrams: list[tuple[str, dict[str, list[str]], dict[str, list[str]]]] = []
    claimed: set[str] = set()
    roots = sorted(node for node, prereqs in sanitized_prereqs.items() if not prereqs)
    for root in roots:
        members: set[str] = {root}
        queue = [root]
        while queue:
            current = queue.pop()
            for child in sorted(children.get(current, ())):
                if child not in members:
                    members.add(child)
                    queue.append(child)
        claimed.update(members)
        sub_prereqs = {node: sanitized_prereqs[node] for node in sorted(members)}
        sub_mutexes = {node: sanitized_mutexes.get(node, []) for node in sorted(members)}
        diagrams.append((root, sub_prereqs, sub_mutexes))
    orphans = sorted(set(sanitized_prereqs) - claimed)
    if orphans:
        sub_prereqs = {node: sanitized_prereqs[node] for node in orphans}
        sub_mutexes = {node: sanitized_mutexes.get(node, []) for node in orphans}
        diagrams.append(("orphans", sub_prereqs, sub_mutexes))
    if not diagrams:
        diagrams.append(("(no focuses parsed)", {}, {}))
    return diagrams


def _resolve_nodes(
    prerequisites: dict[str, list[str]],
    mutexes: dict[str, list[str]],
) -> tuple[set[str], dict[str, list[str]], dict[str, list[str]], set[str], set[str]]:
    """Resolve sanitized node ids, shapes and effective edges.

    Returns (all_nodes, effective_prereqs, effective_mutexes,
    decision_nodes, root_nodes).
    """
    all_ids = set(prerequisites.keys())
    for prereqs in prerequisites.values():
        all_ids.update(prereqs)
    for mutex_list in mutexes.values():
        all_ids.update(mutex_list)
    nodes: set[str] = set()
    for raw_id in all_ids:
        node_id = sanitize_focus_id(raw_id)
        if node_id:
            nodes.add(node_id)

    effective_prereqs: dict[str, list[str]] = {}
    effective_mutexes: dict[str, list[str]] = {}
    for raw_id, prereqs in prerequisites.items():
        node = sanitize_focus_id(raw_id)
        if node not in nodes:
            continue
        effective_prereqs[node] = []
        for prereq in prereqs:
            target = sanitize_focus_id(prereq)
            if target in nodes:
                effective_prereqs[node].append(target)
    for raw_id, mutex_list in mutexes.items():
        node = sanitize_focus_id(raw_id)
        if node not in nodes:
            continue
        effective_mutexes[node] = []
        for mutex in mutex_list:
            target = sanitize_focus_id(mutex)
            if target in nodes:
                effective_mutexes[node].append(target)

    # Focuses that participate in any mutually exclusive pair.
    mutex_members: set[str] = set()
    for node, targets in effective_mutexes.items():
        for target in targets:
            mutex_members.add(node)
            mutex_members.add(target)

    # Prerequisites of mutually exclusive focuses are decision points and
    # render with the diamond shape.
    decision_nodes: set[str] = set()
    for node, prereqs in effective_prereqs.items():
        if node not in mutex_members:
            continue
        for prereq in prereqs:
            decision_nodes.add(prereq)

    # Root focuses (no prerequisites at all) render as circles; the diamond
    # decision shape takes priority over the circle.
    root_nodes = {node for node, prereqs in effective_prereqs.items() if not prereqs}
    return nodes, effective_prereqs, effective_mutexes, decision_nodes, root_nodes


class Aliaser:
    """Map focus ids to document-unique short node ids (n1, n2, ...)."""

    def __init__(self) -> None:
        self._aliases: dict[str, str] = {}

    def __call__(self, focus_id: str) -> str:
        alias = self._aliases.get(focus_id)
        if alias is None:
            alias = f"n{len(self._aliases) + 1}"
            self._aliases[focus_id] = alias
        return alias


def _node_declaration(
    node: str,
    decision_nodes: set[str],
    root_nodes: set[str],
    aliaser: Aliaser,
) -> str:
    alias = aliaser(node)
    if node in decision_nodes:
        return f'{alias}{{"{node}"}}'
    if node in root_nodes:
        return f'{alias}(("{node}"))'
    return f'{alias}["{node}"]'


def _edge_lines(
    nodes: set[str],
    effective_prereqs: dict[str, list[str]],
    effective_mutexes: dict[str, list[str]],
    aliaser: Aliaser,
) -> list[str]:
    lines: list[str] = []
    for node in sorted(nodes):
        for prereq in effective_prereqs.get(node, []):
            lines.append(f"{aliaser(prereq)} --> {aliaser(node)}")
    mutex_pairs: set[tuple[str, str]] = set()
    for node in sorted(nodes):
        for target in effective_mutexes.get(node, []):
            mutex_pairs.add(tuple(sorted((node, target))))
    for a, b in sorted(mutex_pairs):
        lines.append(f"{aliaser(a)} x--x {aliaser(b)}")
    return lines


def _depths(
    nodes: set[str],
    effective_prereqs: dict[str, list[str]],
) -> dict[str, int]:
    """Longest-path depth from the roots via topological order.

    Nodes inside a prerequisite cycle are left out of the result.
    """
    children: dict[str, set[str]] = {}
    indegree: dict[str, int] = {}
    for node in nodes:
        prereqs = [prereq for prereq in effective_prereqs.get(node, []) if prereq in nodes]
        indegree[node] = len(prereqs)
        for prereq in prereqs:
            children.setdefault(prereq, set()).add(node)
    depth: dict[str, int] = {}
    queue = sorted(node for node, degree in indegree.items() if degree == 0)
    for node in queue:
        depth[node] = 0
    cursor = 0
    while cursor < len(queue):
        current = queue[cursor]
        cursor += 1
        for child in sorted(children.get(current, ())):
            depth[child] = max(depth.get(child, 0), depth[current] + 1)
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
    return depth


def build_mermaid(
    title: str,
    prerequisites: dict[str, list[str]],
    mutexes: dict[str, list[str]],
    aliaser: Aliaser,
) -> str:
    lines = [f"# {title}", "", "```mermaid", "flowchart TD"]
    if not prerequisites:
        lines.append('    empty["(no focuses parsed)"]')
    else:
        nodes, effective_prereqs, effective_mutexes, decision_nodes, root_nodes = _resolve_nodes(
            prerequisites, mutexes
        )
        for node in sorted(nodes):
            lines.append(f"    {_node_declaration(node, decision_nodes, root_nodes, aliaser)}")
        for edge in _edge_lines(nodes, effective_prereqs, effective_mutexes, aliaser):
            lines.append(f"    {edge}")
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def build_swimlane(
    title: str,
    prerequisites: dict[str, list[str]],
    mutexes: dict[str, list[str]],
    aliaser: Aliaser,
) -> str:
    lines = [f"# {title}", "", "```mermaid", "swimlane-beta TD"]
    if not prerequisites:
        lines.append('    subgraph tier_0["(no focuses parsed)"]')
        lines.append('        empty["(no focuses parsed)"]')
        lines.append("    end")
    else:
        nodes, effective_prereqs, effective_mutexes, decision_nodes, root_nodes = _resolve_nodes(
            prerequisites, mutexes
        )
        depth = _depths(nodes, effective_prereqs)
        unplaced = sorted(node for node in nodes if node not in depth)
        tiers: dict[int, list[str]] = {}
        for node, tier in depth.items():
            tiers.setdefault(tier, []).append(node)
        for tier in sorted(tiers):
            lines.append(f'    subgraph tier_{tier}["Tier {tier}"]')
            for node in sorted(tiers[tier]):
                lines.append(f"        {_node_declaration(node, decision_nodes, root_nodes, aliaser)}")
            lines.append("    end")
        if unplaced:
            lines.append('    subgraph tier_unplaced["Unplaced (cycle)"]')
            for node in unplaced:
                lines.append(f"        {_node_declaration(node, decision_nodes, root_nodes, aliaser)}")
            lines.append("    end")
        for edge in _edge_lines(nodes, effective_prereqs, effective_mutexes, aliaser):
            lines.append(f"    {edge}")
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def render_diagram(
    mode: str,
    title: str,
    prerequisites: dict[str, list[str]],
    mutexes: dict[str, list[str]],
    aliaser: Aliaser,
) -> str:
    if mode == "flowchart":
        return build_mermaid(title, prerequisites, mutexes, aliaser)
    return build_swimlane(title, prerequisites, mutexes, aliaser)


def process_source(src_dir: Path, out_dir: Path, mode: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    patterns = list(src_dir.glob("*.txt"))
    if not patterns:
        raise SystemExit(f"no .txt sources under {src_dir}")
    written: list[Path] = []
    for txt in patterns:
        text = txt.read_text(encoding="utf-8", errors="replace")
        prerequisites, mutexes = parse_focus_blocks(text)
        diagrams = split_into_diagrams(prerequisites, mutexes)
        aliaser = Aliaser()
        parts: list[str] = []
        for diag_title, sub_prereqs, sub_mutexes in diagrams:
            parts.append(render_diagram(mode, diag_title, sub_prereqs, sub_mutexes, aliaser))
        out_path = out_dir / f"{txt.stem}.md"
        out_path.write_text("\n".join(parts), encoding="utf-8")
        written.append(out_path)
    print(f"wrote {len(written)} focus graph files (mode={mode}) from {src_dir} under {out_dir}")
    for path in written:
        print(f"  - {path}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Export HoI4 focus trees as Mermaid diagrams.")
    parser.add_argument(
        "--mode",
        choices=("swimlane", "flowchart"),
        default="swimlane",
        help="diagram type to emit (default: swimlane)",
    )
    parser.add_argument(
        "--src",
        type=Path,
        default=None,
        help="directory with *.txt focus sources (default: <mod>/common/national_focus)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="output directory for *.md diagrams (default: <mod>/docs/gdd/National Focuses)",
    )
    args = parser.parse_args(argv[1:])
    base = Path(__file__).resolve().parents[2]
    src_dir = args.src if args.src is not None else base / "common" / "national_focus"
    out_dir = args.out if args.out is not None else base / "docs" / "gdd" / "National Focuses"
    process_source(src_dir, out_dir, args.mode)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))