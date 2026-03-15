#!/usr/bin/env python3
"""
Link Auditor Tool

Scans all markdown files in the Agent Maestro vault, extracts wiki-links,
and validates that each link resolves to an existing file.

Part of the Vault Curator constellation.

Usage:
    python link_auditor.py [vault_path]

Defaults:
    vault_path: Current directory
    output: 06_EXECUTION/reports/link_audit_report.csv
"""

import csv
import os
import re
import sys
from pathlib import Path
from datetime import datetime


def extract_wiki_links(content):
    """Extract all wiki-links from markdown content.

    Handles:
    - [[Simple Link]]
    - [[Link|Display Text]]
    - [[Path/To/Link]]
    - [[Path/To/Link|Display Text]]

    Returns list of (full_link_text, target) tuples where target is the
    part before any pipe character.
    """
    pattern = r'\[\[([^\[\]]+)\]\]'
    matches = re.findall(pattern, content)

    links = []
    for match in matches:
        # match is the content inside [[...]]
        # Split on pipe if present
        if '|' in match:
            target = match.split('|')[0].strip()
        else:
            target = match.strip()

        links.append((match, target))

    return links


def build_file_map(vault_path):
    """Build a map of file stems (case-insensitive) to their full paths.

    Returns:
        - file_map: dict mapping lowercase stem -> list of full paths
        - all_files: list of all .md file paths
    """
    vault = Path(vault_path)
    file_map = {}
    all_files = []

    for md_file in sorted(vault.rglob("*.md")):
        # Skip CLAUDE.md files
        if md_file.name == "CLAUDE.md":
            continue

        all_files.append(md_file)
        stem = md_file.stem.lower()

        if stem not in file_map:
            file_map[stem] = []
        file_map[stem].append(md_file)

    return file_map, all_files


def resolve_link(target, file_map):
    """Resolve a link target to a file or report status.

    Returns: (status, matching_file_path or None)
    - 'valid': exactly one match found
    - 'broken': no match found
    - 'ambiguous': multiple matches found
    """
    # Handle path targets: match on the last component
    if '/' in target:
        target = target.split('/')[-1]

    target_lower = target.lower()

    matches = file_map.get(target_lower, [])

    if len(matches) == 0:
        return 'broken', None
    elif len(matches) == 1:
        return 'valid', str(matches[0])
    else:
        return 'ambiguous', str(matches[0])  # Return first match for reference


def scan_vault(vault_path, file_map, all_files):
    """Scan all markdown files and extract and validate wiki-links.

    Returns list of link audit records.
    """
    audit_date = datetime.now().strftime('%Y-%m-%d')
    records = []

    vault = Path(vault_path)

    for md_file in all_files:
        # Get relative path for source_file
        rel_path = md_file.relative_to(vault)
        source_file = str(rel_path)

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except (UnicodeDecodeError, IOError):
            continue

        # Extract all wiki-links
        links = extract_wiki_links(content)

        for full_link, target in links:
            status, target_file = resolve_link(target, file_map)

            records.append({
                'source_file': source_file,
                'link_text': full_link,
                'target_file': target_file if target_file else target,
                'status': status,
                'audit_date': audit_date,
            })

    return records


def export_csv(records, output_path):
    """Write link audit records to CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'source_file', 'link_text', 'target_file', 'status', 'audit_date'
        ])
        writer.writeheader()
        writer.writerows(records)

    return len(records)


def print_stats(records):
    """Print link audit statistics."""
    total = len(records)
    valid = len([r for r in records if r['status'] == 'valid'])
    broken = len([r for r in records if r['status'] == 'broken'])
    ambiguous = len([r for r in records if r['status'] == 'ambiguous'])

    print(f"\n--- Link Audit Statistics ---")
    print(f"Total links:     {total}")
    print(f"Valid links:     {valid}")
    print(f"Broken links:    {broken}")
    print(f"Ambiguous links: {ambiguous}")

    if broken > 0:
        print(f"\nWarning: {broken} broken links found!")


def main():
    vault_path = sys.argv[1] if len(sys.argv) > 1 else "."
    output_path = os.path.join(vault_path, "06_EXECUTION", "reports", "link_audit_report.csv")

    print(f"Scanning vault: {vault_path}")

    file_map, all_files = build_file_map(vault_path)
    print(f"Found {len(all_files)} markdown files")

    records = scan_vault(vault_path, file_map, all_files)

    count = export_csv(records, output_path)
    print(f"Exported {count} link records to: {output_path}")

    print_stats(records)


if __name__ == "__main__":
    main()
