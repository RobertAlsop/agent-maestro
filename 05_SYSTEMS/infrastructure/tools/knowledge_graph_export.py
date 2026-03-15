#!/usr/bin/env python3
"""
Knowledge Graph Export Tool

Scans all markdown files in the Agent Maestro vault, extracts relationships
from YAML frontmatter, and exports the knowledge graph as a CSV file.

Part of the Vault Curator constellation — Improvement 4A.

Usage:
    python knowledge_graph_export.py [vault_path] [output_path]

Defaults:
    vault_path:  Current directory
    output_path: 02_KNOWLEDGE/indexes/knowledge_graph_index.csv
"""

import csv
import os
import re
import sys
from pathlib import Path


def extract_frontmatter(file_path):
    """Extract YAML frontmatter from a markdown file as raw text."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except (UnicodeDecodeError, IOError):
        return None

    if not content.startswith("---"):
        return None

    end = content.find("---", 3)
    if end == -1:
        return None

    return content[3:end].strip()


def parse_frontmatter_simple(fm_text):
    """Parse YAML frontmatter without pyyaml dependency.

    Handles the specific structure used in Agent Maestro vault notes.
    Returns a dict with id, relationships, and other key fields.
    """
    result = {"id": "", "relationships": {}}
    current_key = None
    current_subkey = None

    for line in fm_text.split("\n"):
        stripped = line.strip()

        # Skip empty lines and comments
        if not stripped or stripped.startswith("#"):
            continue

        # Top-level key: value
        if not line.startswith(" ") and not line.startswith("\t"):
            if ":" in stripped:
                key, _, value = stripped.partition(":")
                key = key.strip()
                value = value.strip()
                if key == "id":
                    result["id"] = value.strip('"').strip("'")
                elif key == "relationships":
                    current_key = "relationships"
                    current_subkey = None
                else:
                    current_key = key
                    current_subkey = None
            continue

        # Inside relationships block
        if current_key == "relationships":
            # Subkey like "  defines: []" or "  defines:"
            if re.match(r"^  \w", line) and ":" in stripped:
                subkey, _, value = stripped.partition(":")
                subkey = subkey.strip()
                value = value.strip()
                current_subkey = subkey
                if value == "[]":
                    result["relationships"][subkey] = []
                elif value:
                    result["relationships"][subkey] = [value]
                else:
                    result["relationships"][subkey] = []
            # List item like "    - \"[[Something]]\""
            elif stripped.startswith("- ") and current_subkey:
                item = stripped[2:].strip().strip('"').strip("'")
                if current_subkey not in result["relationships"]:
                    result["relationships"][current_subkey] = []
                result["relationships"][current_subkey].append(item)

    return result


def extract_wiki_link_target(link_text):
    """Extract the target note name from a wiki-link string.

    Handles:
    - [[Simple Link]]
    - [[Path/To/Note]]
    - [[Note|Display Text]]
    - Plain text references
    """
    # Remove wiki-link brackets
    link_text = link_text.strip()
    if link_text.startswith("[[") and link_text.endswith("]]"):
        link_text = link_text[2:-2]

    # Handle aliased links: [[target|display]]
    if "|" in link_text:
        link_text = link_text.split("|")[0]

    # Handle paths: take the last component
    if "/" in link_text:
        link_text = link_text.split("/")[-1]

    return link_text.strip()


def scan_vault(vault_path):
    """Scan all markdown files and extract knowledge graph edges."""
    edges = []
    vault = Path(vault_path)

    for md_file in sorted(vault.rglob("*.md")):
        # Skip CLAUDE.md files and archive
        rel_path = md_file.relative_to(vault)
        if md_file.name == "CLAUDE.md":
            continue

        fm_text = extract_frontmatter(md_file)
        if not fm_text:
            continue

        parsed = parse_frontmatter_simple(fm_text)
        source_id = parsed.get("id", "")
        source_name = md_file.stem  # Filename without extension

        if not source_id:
            continue

        relationships = parsed.get("relationships", {})
        for rel_type, targets in relationships.items():
            if not targets:
                continue
            for target in targets:
                target_name = extract_wiki_link_target(target)
                if target_name:
                    edges.append({
                        "source_id": source_id,
                        "source_name": source_name,
                        "relationship_type": rel_type,
                        "target_id": "",  # Resolved in a second pass
                        "target_name": target_name,
                    })

    # Second pass: resolve target IDs
    id_map = {}
    for md_file in vault.rglob("*.md"):
        if md_file.name == "CLAUDE.md":
            continue
        fm_text = extract_frontmatter(md_file)
        if fm_text:
            parsed = parse_frontmatter_simple(fm_text)
            if parsed.get("id"):
                id_map[md_file.stem] = parsed["id"]

    for edge in edges:
        target_name = edge["target_name"]
        edge["target_id"] = id_map.get(target_name, "")

    return edges


def export_csv(edges, output_path):
    """Write edges to CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "source_id", "source_name", "relationship_type",
            "target_id", "target_name"
        ])
        writer.writeheader()
        writer.writerows(edges)

    return len(edges)


def print_stats(edges):
    """Print graph statistics."""
    sources = set(e["source_id"] for e in edges)
    targets = set(e["target_name"] for e in edges)
    all_nodes = sources | set(e["source_name"] for e in edges) | targets
    rel_types = {}
    for e in edges:
        rt = e["relationship_type"]
        rel_types[rt] = rel_types.get(rt, 0) + 1

    print(f"\n--- Knowledge Graph Statistics ---")
    print(f"Total edges:     {len(edges)}")
    print(f"Unique nodes:    {len(all_nodes)}")
    print(f"Source notes:    {len(sources)}")
    print(f"\nEdges by relationship type:")
    for rt, count in sorted(rel_types.items(), key=lambda x: -x[1]):
        print(f"  {rt}: {count}")


def main():
    vault_path = sys.argv[1] if len(sys.argv) > 1 else "."
    default_output = os.path.join(vault_path, "02_KNOWLEDGE", "indexes", "knowledge_graph_index.csv")
    output_path = sys.argv[2] if len(sys.argv) > 2 else default_output

    print(f"Scanning vault: {vault_path}")
    edges = scan_vault(vault_path)

    count = export_csv(edges, output_path)
    print(f"Exported {count} edges to: {output_path}")

    print_stats(edges)


if __name__ == "__main__":
    main()
