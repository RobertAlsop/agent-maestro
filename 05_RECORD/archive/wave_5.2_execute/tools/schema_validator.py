#!/usr/bin/env python3
"""
Schema Validator Tool

Scans all markdown files in the Agent Maestro vault, validates YAML frontmatter
against the governance schema, and reports validation issues.

Part of the Vault Curator constellation.

Usage:
    python schema_validator.py [vault_path]

Defaults:
    vault_path: Current directory
    output: 06_EXECUTION/reports/schema_validation_report.csv
"""

import csv
import os
import re
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

    Returns a dict with all top-level and nested keys found.
    """
    result = {}
    current_key = None
    current_dict = None

    for line in fm_text.split("\n"):
        stripped = line.strip()

        # Skip empty lines and comments
        if not stripped or stripped.startswith("#"):
            continue

        # Top-level key: value (no leading spaces)
        if not line.startswith(" ") and not line.startswith("\t"):
            if ":" in stripped:
                key, _, value = stripped.partition(":")
                key = key.strip()
                value = value.strip()

                # Handle nested structures
                if value in ('[]', '{}', ''):
                    if value == '[]':
                        result[key] = []
                    elif value == '{}':
                        result[key] = {}
                    else:
                        result[key] = None
                else:
                    # Strip quotes
                    value = value.strip('"').strip("'")
                    result[key] = value

                current_key = key
                if isinstance(result.get(key), dict):
                    current_dict = result[key]
                else:
                    current_dict = None
            continue

        # Nested key (indented)
        if line.startswith(" ") or line.startswith("\t"):
            # Subkey like "  defines: []"
            if ":" in stripped:
                subkey, _, value = stripped.partition(":")
                subkey = subkey.strip()
                value = value.strip()

                # Store in nested dict or list
                if current_key and isinstance(result.get(current_key), dict):
                    if value in ('[]', '{}'):
                        result[current_key][subkey] = [] if value == '[]' else {}
                    else:
                        value = value.strip('"').strip("'")
                        result[current_key][subkey] = value
            # List item like "    - item"
            elif stripped.startswith("- "):
                item = stripped[2:].strip().strip('"').strip("'")
                if current_key and isinstance(result.get(current_key), list):
                    result[current_key].append(item)

    return result


def validate_field(file_path, field_name, value, schema_def):
    """Validate a single field against schema definition.

    Returns list of (issue_type, expected_value, actual_value) tuples.
    Empty list means valid.
    """
    issues = []

    # Field missing
    if field_name not in schema_def:
        if value is None:
            issues.append(('missing_field', schema_def.get(field_name, 'N/A'), 'null'))
            return issues

    schema = schema_def.get(field_name, {})
    required = schema.get('required', True)
    field_type = schema.get('type', 'string')
    enum_values = schema.get('enum', None)
    min_val = schema.get('min', None)
    max_val = schema.get('max', None)

    # Check required
    if required and value is None:
        issues.append(('missing_field', field_type, 'null'))
        return issues

    if value is None:
        return issues

    # Type validation
    if field_type == 'string':
        if not isinstance(value, str) or not value:
            issues.append(('invalid_type', 'string', type(value).__name__))
    elif field_type == 'boolean':
        if isinstance(value, str):
            if value.lower() not in ('true', 'false'):
                issues.append(('invalid_value', 'true|false', value))
        elif not isinstance(value, bool):
            issues.append(('invalid_type', 'boolean', type(value).__name__))
    elif field_type == 'integer':
        try:
            int_val = int(value) if isinstance(value, str) else value
            if not isinstance(int_val, int):
                issues.append(('invalid_type', 'integer', type(value).__name__))
            elif min_val is not None and int_val < min_val:
                issues.append(('invalid_value', f'>={min_val}', str(int_val)))
            elif max_val is not None and int_val > max_val:
                issues.append(('invalid_value', f'<={max_val}', str(int_val)))
        except (ValueError, TypeError):
            issues.append(('invalid_type', 'integer', type(value).__name__))
    elif field_type == 'date':
        if isinstance(value, str):
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', value):
                issues.append(('invalid_value', 'YYYY-MM-DD', value))
    elif field_type == 'dict':
        if not isinstance(value, dict):
            issues.append(('invalid_type', 'dict', type(value).__name__))

    # Enum validation
    if enum_values and not isinstance(value, dict):
        if isinstance(value, str) and value not in enum_values:
            issues.append(('invalid_value', '|'.join(enum_values), value))

    return issues


def get_schema():
    """Return the Agent Maestro schema definition."""
    return {
        'id': {'type': 'string', 'required': True},
        'type': {'type': 'string', 'required': True},
        'note_class': {'type': 'string', 'required': True},
        'domain': {'type': 'string', 'required': True},
        'layer': {'type': 'string', 'required': True},
        'canonical': {'type': 'boolean', 'required': True},
        'authority_weight': {'type': 'integer', 'required': True, 'min': 0, 'max': 100},
        'schema_version': {'type': 'integer', 'required': True},
        'status': {'type': 'string', 'required': True, 'enum': ['active', 'draft', 'deprecated', 'archived']},
        'review_status': {'type': 'string', 'required': False, 'enum': ['draft', 'approved', 'needs_review']},
        'version': {'type': 'integer', 'required': True, 'min': 1},
        'created': {'type': 'date', 'required': True},
        'updated': {'type': 'date', 'required': True},
        'owner': {'type': 'string', 'required': True},
        'relationships': {'type': 'dict', 'required': True},
        'source_type': {'type': 'string', 'required': True},
    }


def scan_vault(vault_path):
    """Scan all markdown files and validate schemas.

    Returns list of validation issue records.
    """
    validation_date = datetime.now().strftime('%Y-%m-%d')
    records = []
    schema = get_schema()

    vault = Path(vault_path)

    for md_file in sorted(vault.rglob("*.md")):
        # Skip CLAUDE.md files
        if md_file.name == "CLAUDE.md":
            continue

        # Get relative path
        rel_path = md_file.relative_to(vault)
        file_path = str(rel_path)

        fm_text = extract_frontmatter(md_file)
        if not fm_text:
            # Missing frontmatter is an issue
            records.append({
                'file_path': file_path,
                'field_name': 'frontmatter',
                'issue_type': 'missing_field',
                'expected_value': 'YAML frontmatter',
                'actual_value': 'none',
                'validation_date': validation_date,
            })
            continue

        parsed = parse_frontmatter_simple(fm_text)

        # Check schema version
        schema_version = parsed.get('schema_version')
        if schema_version and schema_version != 2 and isinstance(schema_version, str):
            try:
                schema_version = int(schema_version)
            except ValueError:
                pass

        if schema_version and schema_version != 2:
            records.append({
                'file_path': file_path,
                'field_name': 'schema_version',
                'issue_type': 'schema_version_mismatch',
                'expected_value': '2',
                'actual_value': str(schema_version),
                'validation_date': validation_date,
            })

        # Validate all required fields
        for field_name, schema_def in schema.items():
            value = parsed.get(field_name)
            issues = validate_field(file_path, field_name, value, schema)

            for issue_type, expected, actual in issues:
                records.append({
                    'file_path': file_path,
                    'field_name': field_name,
                    'issue_type': issue_type,
                    'expected_value': expected,
                    'actual_value': actual,
                    'validation_date': validation_date,
                })

    return records


def export_csv(records, output_path):
    """Write validation records to CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'file_path', 'field_name', 'issue_type', 'expected_value',
            'actual_value', 'validation_date'
        ])
        writer.writeheader()
        writer.writerows(records)

    return len(records)


def print_stats(records):
    """Print validation statistics."""
    total = len(records)
    missing = len([r for r in records if r['issue_type'] == 'missing_field'])
    invalid_value = len([r for r in records if r['issue_type'] == 'invalid_value'])
    invalid_type = len([r for r in records if r['issue_type'] == 'invalid_type'])
    schema_mismatch = len([r for r in records if r['issue_type'] == 'schema_version_mismatch'])

    print(f"\n--- Schema Validation Statistics ---")
    print(f"Total issues:            {total}")
    print(f"Missing fields:          {missing}")
    print(f"Invalid values:          {invalid_value}")
    print(f"Invalid types:           {invalid_type}")
    print(f"Schema version mismatches: {schema_mismatch}")

    if total > 0:
        print(f"\nWarning: {total} validation issues found!")


def main():
    vault_path = sys.argv[1] if len(sys.argv) > 1 else "."
    output_path = os.path.join(vault_path, "06_EXECUTION", "reports", "schema_validation_report.csv")

    print(f"Scanning vault: {vault_path}")

    records = scan_vault(vault_path)

    count = export_csv(records, output_path)
    print(f"Exported {count} validation records to: {output_path}")

    print_stats(records)


if __name__ == "__main__":
    main()
