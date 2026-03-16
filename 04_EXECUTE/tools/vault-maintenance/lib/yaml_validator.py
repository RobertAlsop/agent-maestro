#!/usr/bin/env python3
"""yaml_validator.py — Core YAML frontmatter validation logic.

Called by yaml_validation.sh. Validates frontmatter against schema v3 rules.

Arguments:
    --vault-root DIR    Vault root directory
    --config FILE       YAML config file path
    --output-dir DIR    Report output directory
    --quiet             Suppress stdout

Exit codes: 0 = clean, 1 = findings, 2 = error
"""

import sys
import os
import re
import json
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    # Try to handle missing PyYAML gracefully
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


def parse_config(config_path):
    """Parse a YAML config file."""
    if not config_path or not os.path.exists(config_path):
        return {}
    with open(config_path, 'r') as f:
        return yaml.safe_load(f) or {}


def load_merged_config(config_path, defaults_path):
    """Load defaults then override with vault-specific config."""
    config = {}
    if defaults_path and os.path.exists(defaults_path):
        config = parse_config(defaults_path)
    if config_path and os.path.exists(config_path):
        override = parse_config(config_path)
        config.update(override)
    return config


def is_excluded(filepath, vault_root, exclude_patterns):
    """Check if a file matches any exclude pattern."""
    rel = os.path.relpath(filepath, vault_root)
    for pattern in exclude_patterns:
        if rel.startswith(pattern) or f"/{pattern}/" in f"/{rel}/":
            return True
        if os.path.basename(filepath) == pattern:
            return True
    return False


def is_frontmatter_optional(filepath, vault_root, optional_folders):
    """Check if file is in a folder where frontmatter is optional."""
    rel = os.path.relpath(filepath, vault_root)
    for folder in optional_folders:
        if rel.startswith(folder + "/"):
            return True
    return False


def is_structural_file(filepath, exemptions):
    """Check if file is a structural exemption (no frontmatter expected)."""
    basename = os.path.basename(filepath)
    return basename in exemptions


def extract_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file. Returns (dict, error_string)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return None, f"cannot read file: {e}"

    if not content.startswith('---'):
        return None, None  # No frontmatter present (not an error per se)

    # Find closing ---
    lines = content.split('\n')
    end_idx = None
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            end_idx = i
            break

    if end_idx is None:
        return None, "frontmatter not closed (missing closing ---)"

    fm_text = '\n'.join(lines[1:end_idx])
    try:
        fm = yaml.safe_load(fm_text)
        if fm is None:
            return None, "frontmatter is empty between --- delimiters"
        if not isinstance(fm, dict):
            return None, "frontmatter is not a YAML mapping"
        return fm, None
    except yaml.YAMLError as e:
        return None, f"YAML parse error: {e}"


def validate_frontmatter(fm, filepath, config, vault_root):
    """Validate frontmatter dict against config rules. Returns (findings, warnings)."""
    findings = []
    warnings = []
    rel_path = os.path.relpath(filepath, vault_root)

    required_fields = config.get('required_fields', [])
    controlled_vocab = config.get('controlled_vocabulary', {})
    aw_range = config.get('authority_weight_range', {})
    aw_min = aw_range.get('min', 0)
    aw_max = aw_range.get('max', 100)

    # Check required fields
    for field in required_fields:
        if field not in fm:
            findings.append(f"{rel_path}: missing required field '{field}'")

    # Check controlled vocabulary
    for field, allowed_values in controlled_vocab.items():
        if field in fm:
            val = fm[field]
            if isinstance(allowed_values, list) and val not in allowed_values:
                findings.append(
                    f"{rel_path}: '{field}' value '{val}' not in allowed values {allowed_values}"
                )

    # Check authority_weight range
    if 'authority_weight' in fm:
        aw = fm['authority_weight']
        if isinstance(aw, (int, float)):
            if aw < aw_min or aw > aw_max:
                findings.append(
                    f"{rel_path}: authority_weight {aw} outside range [{aw_min}, {aw_max}]"
                )
        else:
            findings.append(f"{rel_path}: authority_weight is not a number: {aw}")

    # Check schema_version
    if 'schema_version' in fm:
        sv = fm['schema_version']
        if sv != 3:
            warnings.append(f"{rel_path}: schema_version is {sv}, expected 3")

    # Check dates are ISO 8601
    for date_field in ['created', 'updated']:
        if date_field in fm:
            val = str(fm[date_field])
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', val):
                findings.append(f"{rel_path}: '{date_field}' is not ISO 8601 format: '{val}'")

    # Check relationships structure
    if 'relationships' in fm:
        rels = fm['relationships']
        if not isinstance(rels, dict):
            findings.append(f"{rel_path}: 'relationships' must be a mapping")
        else:
            for sub in ['derives_from', 'governs', 'related']:
                if sub not in rels:
                    findings.append(f"{rel_path}: 'relationships' missing sub-field '{sub}'")
                elif rels[sub] is None:
                    findings.append(
                        f"{rel_path}: 'relationships.{sub}' is null, should be [] if empty"
                    )
                elif not isinstance(rels[sub], list):
                    findings.append(
                        f"{rel_path}: 'relationships.{sub}' must be a list"
                    )

    # Check tags
    if 'tags' in fm:
        tags = fm['tags']
        if tags is None:
            findings.append(f"{rel_path}: 'tags' is null, should be [] if empty")
        elif not isinstance(tags, list):
            findings.append(f"{rel_path}: 'tags' must be a list")

    return findings, warnings


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Validate YAML frontmatter')
    parser.add_argument('--vault-root', required=True)
    parser.add_argument('--config', default='')
    parser.add_argument('--output-dir', default='')
    parser.add_argument('--quiet', action='store_true')
    args = parser.parse_args()

    vault_root = os.path.abspath(args.vault_root)
    if not os.path.isdir(vault_root):
        print(f"ERROR: vault root does not exist: {vault_root}", file=sys.stderr)
        sys.exit(2)

    # Resolve config
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tool_dir = os.path.dirname(script_dir)  # vault-maintenance/
    defaults_path = os.path.join(tool_dir, 'config', 'defaults.conf')
    config = load_merged_config(args.config, defaults_path)
    config['vault_root'] = vault_root

    output_dir = args.output_dir or config.get('output_dir', 'reports')
    if not os.path.isabs(output_dir):
        output_dir = os.path.join(tool_dir, output_dir)
    os.makedirs(output_dir, exist_ok=True)

    exclude_patterns = config.get('exclude_patterns', [])
    optional_folders = config.get('frontmatter_optional_folders', [])
    structural_exemptions = config.get('structural_exemptions', ['CLAUDE.md', 'SYSTEM_MAP.md', 'README.md'])

    # Collect all .md files
    all_findings = []
    all_warnings = []
    checked = 0
    passed = 0

    for root, dirs, files in os.walk(vault_root):
        # Skip excluded dirs
        dirs[:] = [d for d in dirs if not is_excluded(os.path.join(root, d), vault_root, exclude_patterns)]
        for fname in sorted(files):
            if not fname.endswith('.md'):
                continue
            filepath = os.path.join(root, fname)
            if is_excluded(filepath, vault_root, exclude_patterns):
                continue

            # Skip structural files
            if is_structural_file(filepath, structural_exemptions):
                continue

            # Skip optional-frontmatter folders
            if is_frontmatter_optional(filepath, vault_root, optional_folders):
                continue

            checked += 1
            fm, error = extract_frontmatter(filepath)

            if error:
                rel = os.path.relpath(filepath, vault_root)
                all_findings.append(f"{rel}: {error}")
                continue

            if fm is None:
                rel = os.path.relpath(filepath, vault_root)
                all_findings.append(f"{rel}: no YAML frontmatter found")
                continue

            findings, warnings = validate_frontmatter(fm, filepath, config, vault_root)
            all_findings.extend(findings)
            all_warnings.extend(warnings)

            if not findings:
                passed += 1

    # Write report
    failed = len(set(f.split(':')[0] for f in all_findings)) if all_findings else 0
    warned = len(all_warnings)
    result = "CLEAN" if not all_findings else "FINDINGS"

    report_path = os.path.join(output_dir, 'YAML_Validation_report.md')
    with open(report_path, 'w') as f:
        f.write("# YAML Validation Report\n\n")
        f.write(f"**Vault:** {vault_root}\n")
        f.write(f"**Date:** {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')}\n")
        f.write(f"**Result:** {result}\n\n")
        f.write("## Summary\n\n")
        f.write("| Checked | Passed | Failed | Warnings |\n")
        f.write("|---------|--------|--------|----------|\n")
        f.write(f"| {checked} | {passed} | {checked - passed} | {warned} |\n\n")

        if all_findings:
            f.write("## Findings\n\n")
            for finding in all_findings:
                f.write(f"- {finding}\n")
            f.write("\n")

        if all_warnings:
            f.write("## Warnings (uncertain)\n\n")
            for warning in all_warnings:
                f.write(f"- {warning}\n")
            f.write("\n")

    if not args.quiet:
        print(f"YAML Validation: {result} ({checked} checked, {checked - passed} findings, {warned} warnings)")
        print(f"Report: {report_path}")

    sys.exit(0 if not all_findings else 1)


if __name__ == '__main__':
    main()
