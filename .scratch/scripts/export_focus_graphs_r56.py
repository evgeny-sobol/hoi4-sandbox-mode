#!/usr/bin/env python3
"""Export HoI4 national focus trees into Mermaid flowchart Markdown files.

For the _sandbox-r56 overlay this reads both the overlay sources and the
subscribed Road to 56 workshop tree, then writes diagram files under
gdd/National Focuses/ of the overlay.
"""
import os
import re
from pathlib import Path

FOCUS_PATTERN = re.compile(r"^\s*id\s*=\s*(\S+)", re.IGNORECASE)
PREREQ_PATTERN = re.compile(r"prerequisite\s*=\s*\{\s*focus\s*=\s*(\S+)", re.IGNORECASE)
MUTEX_PATTERN = re.compile(r"mutually_exclusive\s*=\s*\{\s*focus\s*=\s*(\S+)", re.IGNORECASE)


def split_braces(text: str) -> list[str]:
    """Split text by top-level braces, keeping empty items between them."""
    tokens: list[str] = []
    depth = 0
    start = 0
    for i, ch in enumerate(text):
        if ch == '{':
            if depth == 0:
                tokens.append(text[start:i])
                start = i + 1
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                tokens.append(text[start:i])
                start = i + 1
    if start < len(text):
        tokens.append(text[start:])
    return tokens


def parse_focus_blocks(text: str) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Return mappings from focus id to prerequisite/mutex ids."""
    prerequisites: dict[str, list[str]] = {}
    mutexes: dict[str, list[str]] = {}
    focus_tree_match = re.search(r"focus_tree\s*=\s*\{", text, re.IGNORECASE)
    if not focus_tree_match:
        return prerequisites, mutexes
    tree_start = text.find('{', focus_tree_match.end() - 1)
    if tree_start < 0:
        return prerequisites, mutexes
    depth = 0
    tree_body = ""
    for i in range(tree_start, len(text)):
        ch = text[i]
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                tree_body = text[tree_start + 1:i]
                break
    if not tree_body:
        return prerequisites, mutexes
    focus_blocks = re.findall(r"focus\s*=\s*\{", tree_body, re.IGNORECASE)
    if not focus_blocks:
        return prerequisites, mutexes
    cursor = 0
    for _ in focus_blocks:
        start = tree_body.find('{', cursor)
        if start < 0:
            break
        depth_local = 0
        end = start
        for i in range(start, len(tree_body)):
            ch = tree_body[i]
            if ch == '{':
                depth_local += 1
            elif ch == '}':
                depth_local -= 1
                if depth_local == 0:
                    end = i
                    break
        block = tree_body[start + 1:end]
        focus_id = None
        prereqs: list[str] = []
        mutex_list: list[str] = []
        for line in block.splitlines():
            stripped = line.strip()
            if focus_id is None:
                m = FOCUS_PATTERN.match(stripped)
                if m:
                    focus_id = m.group(1)
                    continue
            m = PREREQ_PATTERN.search(stripped)
            if m:
                prereqs.append(m.group(1))
            m = MUTEX_PATTERN.search(stripped)
            if m:
                mutex_list.append(m.group(1))
        if focus_id:
            prerequisites[focus_id] = prereqs
            mutexes[focus_id] = mutex_list
        cursor = end + 1
    return prerequisites, mutexes


def read_workshop_focus_trees() -> dict[str, tuple[dict[str, list[str]], dict[str, list[str]]]]:
    workshop = Path(r"C:\Games\Steam\steamapps\workshop\content\394360\820260968")
    if not workshop.is_dir():
        return {}
    output: dict[str, tuple[dict[str, list[str]], dict[str, list[str]]]] = {}
    for txt in (workshop / "common" / "national_focus").glob("*.txt"):
        try:
            text = txt.read_text(encoding="utf-8", errors="replace")
            prerequisites, mutexes = parse_focus_blocks(text)
            output[txt.stem] = (prerequisites, mutexes)
        except OSError:
            continue
    return output


def sanitize_focus_id(focus_id: str) -> str:
    return focus_id.strip().strip("}").strip()


def build_mermaid(title: str, prerequisites: dict[str, list[str]], mutexes: dict[str, list[str]]) -> str:
    lines = [f"# {title}\n", "```mermaid", "flowchart TD"]
    if not prerequisites:
        lines.append('    empty["(no focuses parsed)"]')
    else:
        all_ids = set(prerequisites.keys())
        for prereqs in prerequisites.values():
            all_ids.update(prereqs)
        for mutex_list in mutexes.values():
            all_ids.update(mutex_list)
        sanitized = {sanitize_focus_id(f): f for f in all_ids}
        alias_map = {f: sanitize_focus_id(f) for f in all_ids}
        used = set()
        for focus_id in sorted(all_ids):
            node_id = sanitize_focus_id(focus_id)
            if not node_id or node_id in used:
                continue
            used.add(node_id)
            lines.append(f"    {node_id}[\"{node_id}\"]")
        for raw_focus_id in sorted(all_ids):
            focus_id = sanitize_focus_id(raw_focus_id)
            if not focus_id:
                continue
            for prereq in prerequisites.get(raw_focus_id, []):
                target = sanitize_focus_id(prereq)
                if target and target in used:
                    lines.append(f"    {target} --> {focus_id}")
            for mutex in mutexes.get(raw_focus_id, []):
                target = sanitize_focus_id(mutex)
                if target and target in used:
                    lines.append(f"    {focus_id} -.-> {target}")
    lines.append("```\n")
    return "\n".join(lines)


def process_source(project_root: Path) -> None:
    overlay = project_root / "common" / "national_focus"
    if overlay.is_dir():
        output = project_root / "gdd" / "National Focuses"
        output.mkdir(parents=True, exist_ok=True)
        written: list[Path] = []
        for txt in overlay.glob("*.txt"):
            try:
                text = txt.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            prerequisites, mutexes = parse_focus_blocks(text)
            diagram = build_mermaid(txt.stem, prerequisites, mutexes)
            out_path = output / f"{txt.stem}.md"
            out_path.write_text(diagram, encoding="utf-8")
            written.append(out_path)
        print(f"wrote {len(written)} overlay focus graphs under {output}")
        for path in written:
            print(f"  - {path.relative_to(project_root)}")
    workshop_focus_trees = read_workshop_focus_trees()
    if not workshop_focus_trees:
        return
    r56_output = project_root / "gdd" / "National Focuses" / "r56"
    r56_output.mkdir(parents=True, exist_ok=True)
    written = []
    for name, (prerequisites, mutexes) in sorted(workshop_focus_trees.items()):
        diagram = build_mermaid(f"r56 - {name}", prerequisites, mutexes)
        out_path = r56_output / f"{name}.md"
        out_path.write_text(diagram, encoding="utf-8")
        written.append(out_path)
    print(f"wrote {len(written)} workshop focus graphs under {r56_output}")
    for path in written:
        print(f"  - {path.relative_to(project_root)}")


def main(argv: list[str]) -> int:
    base = Path(os.path.expandvars(
        r"%USERPROFILE%\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56"
    ))
    process_source(base)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
