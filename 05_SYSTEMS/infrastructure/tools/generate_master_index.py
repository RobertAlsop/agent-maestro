#!/usr/bin/env python3
"""
Master Index Generator Tool

Scans all markdown files in the Agent Maestro vault, extracts frontmatter,
and generates a comprehensive master index organized by note_class.

Part of the Vault Curator constellation.

Usage:
    python generate_master_index.py [vault_path]

Defaults:
    vault_path: Current directory
    output: 02_KNOWLEDGE/indexes/Master Index — Generated.md
"""

import os
import sys
from pathlib import Path
from datetime import datetime


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

    Returns a dict with key fields: id, note_class, status, filename
    """
    result = {}

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

                # Strip quotes
                value = value.strip('"').strip("'")

                # Only capture the fields we need
                if key in ('id', 'note_class', 'status'):
                    result[key] = value

    return result


def scan_vault(vault_path):
    """Scan all markdown files and extract metadata.

    Returns dict: {note_class: [list of (id, filename, status)]}
    """
    vault = Path(vault_path)
    notes_by_class = {}

    for md_file in sorted(vault.rglob("*.md")):
        # Skip CLAUDE.md files
        if md_file.name == "CLAUDE.md":
            continue

        fm_text = extract_frontmatter(md_file)
        if not fm_text:
            continue

        parsed = parse_frontmatter_simple(fm_text)

        note_id = parsed.get('id', '')
        note_class = parsed.get('note_class', 'uncategorized')
        status = parsed.get('status', 'unknown')

        if not note_id:
            continue

        # Group by note_class
        if note_class not in notes_by_class:
            notes_by_class[note_class] = []

        notes_by_class[note_class].append({
            'id': note_id,
            'filename': md_file.stem,
            'status': status,
        })

    return notes_by_class


def generate_frontmatter():
    """Generate the frontmatter for the Master Index."""
    today = datetime.now().strftime('%Y-%m-%d')

    frontmatter = f"""---
id: INDEX.master.generated
type: index
note_class: index
domain: agent_maestro
layer: indexes
scope: vault_root

canonical: false
authority_weight: 50
resolution_basis: generated
schema_version: 2

status: active
review_status: approved
version: 1

created: {today}
updated: {today}
last_reviewed: null
review_cycle: quarterly

owner: AgentMaestro

relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to: []
  uses: []
  produces: []

related: []
related_maps: []

source_type: generated
supersedes: []
superseded_by: []

tags:
  - index
  - generated
  - master_index
  - vault_root

hash: ""
---"""

    return frontmatter


def generate_markdown(notes_by_class):
    """Generate markdown content for the Master Index."""
    lines = []

    lines.append("# INDEX.master.generated\n")
    lines.append("> Auto-generated master index of all notes in the Agent Maestro vault, organized by note_class.\n")
    lines.append("> Last generated: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")

    # Sort classes alphabetically
    for note_class in sorted(notes_by_class.keys()):
        notes = notes_by_class[note_class]

        # Class header
        lines.append(f"\n## {note_class.replace('_', ' ').title()}\n")
        lines.append(f"*{len(notes)} notes*\n")

        # Sort notes by ID within each class
        for note in sorted(notes, key=lambda n: n['id']):
            note_id = note['id']
            filename = note['filename']
            status = note['status']

            # Create wiki-link using filename
            lines.append(f"- [[{filename}]] (`{note_id}`) — {status}\n")

    return "\n".join(lines)


def write_index(content, output_path):
    """Write the generated index to file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)


def print_stats(notes_by_class):
    """Print index generation statistics."""
    total_notes = sum(len(notes) for notes in notes_by_class.values())
    total_classes = len(notes_by_class)

    print(f"\n--- Master Index Statistics ---")
    print(f"Total notes:        {total_notes}")
    print(f"Note classes:       {total_classes}")
    print(f"\nNotes by class:")
    for note_class in sorted(notes_by_class.keys()):
        count = len(notes_by_class[note_class])
        print(f"  {note_class}: {count}")


def main():
    vault_path = sys.argv[1] if len(sys.argv) > 1 else "."
    output_path = os.path.join(vault_path, "02_KNOWLEDGE", "indexes", "Master Index — Generated.md")

    print(f"Scanning vault: {vault_path}")

    notes_by_class = scan_vault(vault_path)

    frontmatter = generate_frontmatter()
    markdown = generate_markdown(notes_by_class)
    full_content = frontmatter + "\n\n" + markdown

    write_index(full_content, output_path)
    print(f"Generated master index: {output_path}")

    print_stats(notes_by_class)


if __name__ == "__main__":
    main()
