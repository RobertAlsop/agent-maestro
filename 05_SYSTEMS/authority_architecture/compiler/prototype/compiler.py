#!/usr/bin/env python3
"""
Agent Maestro Authority Pack Compiler — Prototype v0.1

Transforms design-time authority packs (YAML) into compiled governance
artifacts (JSON), implementing the 8-stage pipeline defined in
05_SYSTEMS/authority_architecture/compiler/Compiler Pipeline.md

Usage:
    python compiler.py <pack_file_or_dir> [--output-dir <dir>] [--vault-root <dir>]

Examples:
    # Compile a single pack
    python compiler.py ../../packs/constellation_packs/vault_curator/executive.yaml

    # Compile all packs in a directory
    python compiler.py ../../packs/constellation_packs/vault_curator/

    # Specify output directory
    python compiler.py ../../packs/constellation_packs/vault_curator/ --output-dir ./artifacts
"""

import csv
import copy
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml
from jsonschema import validate, ValidationError

COMPILER_VERSION = "0.1.0"


def load_schema(schema_name):
    """Load a JSON Schema file from the schema/ directory."""
    schema_dir = Path(__file__).parent / "schema"
    schema_path = schema_dir / schema_name
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_pack(pack_path):
    """Load an authority pack from a YAML file."""
    with open(pack_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def find_pack_by_id(pack_id, search_dirs):
    """Find a pack file by its pack_id across search directories."""
    for search_dir in search_dirs:
        for yaml_file in Path(search_dir).rglob("*.yaml"):
            try:
                pack = load_pack(yaml_file)
                if pack and pack.get("pack_id") == pack_id:
                    return pack, yaml_file
            except Exception:
                continue
    return None, None


# ── Stage 1: Input Validation ──────────────────────────────────────

def stage_1_input_validation(pack, schema):
    """Validate input pack against the authority pack schema."""
    try:
        validate(instance=pack, schema=schema)
        return True, []
    except ValidationError as e:
        return False, [f"Schema violation: {e.message} at {list(e.path)}"]


# ── Stage 2: Inheritance Resolution ────────────────────────────────

def stage_2_inheritance_resolution(pack, search_dirs):
    """Resolve inheritance chain and flatten into a single merged pack."""
    chain = [pack]
    current = pack
    visited = {pack["pack_id"]}

    while current.get("inherits_from"):
        parent_id = current["inherits_from"]
        if parent_id in visited:
            return None, chain, [f"Circular inheritance detected: {parent_id}"]
        visited.add(parent_id)

        parent, _ = find_pack_by_id(parent_id, search_dirs)
        if parent is None:
            return None, chain, [f"Parent pack not found: {parent_id}"]

        chain.append(parent)
        current = parent

    # Flatten: start from root (last in chain), apply each child's overrides
    chain.reverse()
    merged = {}
    for ancestor in chain:
        merged = merge_packs(merged, ancestor)

    return merged, chain, []


def merge_packs(base, override):
    """Deep merge two pack dicts. Override values take precedence."""
    result = copy.deepcopy(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_packs(result[key], value)
        elif key in result and isinstance(result[key], list) and isinstance(value, list):
            # For lists, override replaces entirely (explicit override)
            result[key] = copy.deepcopy(value)
        else:
            result[key] = copy.deepcopy(value)
    return result


# ── Stage 3: Override Application ──────────────────────────────────

def stage_3_override_application(merged, chain):
    """Track which fields were overridden from parent packs."""
    if len(chain) < 2:
        return merged, []

    overrides = []
    root = chain[0]
    child = chain[-1]

    for key in child:
        if key in root and child[key] != root.get(key):
            overrides.append(f"{child['pack_id']} overrides '{key}' from {root['pack_id']}")

    return merged, overrides


# ── Stage 4: Policy Resolution ─────────────────────────────────────

def stage_4_policy_resolution(merged):
    """Check for conflicting rules. Fail if unresolvable."""
    rules = merged.get("rules", [])
    rule_ids = [r["rule_id"] for r in rules]
    duplicates = [rid for rid in rule_ids if rule_ids.count(rid) > 1]

    if duplicates:
        return False, [f"Conflicting rule IDs: {set(duplicates)}"]
    return True, []


# ── Stage 5: Completeness Validation ──────────────────────────────

def stage_5_completeness_validation(merged):
    """Verify all required governance sections are present."""
    required_sections = [
        "pack_id", "pack_name", "version", "owner",
        "authority_type", "scope"
    ]
    recommended_sections = [
        "governed_entities", "governed_actions", "rules",
        "control_gates", "evidence_requirements",
        "escalation", "failure_semantics"
    ]

    errors = []
    warnings = []

    for section in required_sections:
        if section not in merged or merged[section] is None:
            errors.append(f"Required section missing: {section}")

    for section in recommended_sections:
        if section not in merged or merged[section] is None:
            warnings.append(f"Recommended section missing: {section}")

    return len(errors) == 0, errors, warnings


# ── Stage 6: Artifact Generation ──────────────────────────────────

def stage_6_artifact_generation(merged, chain, overrides, warnings):
    """Produce the compiled governance artifact."""
    now = datetime.now(timezone.utc).isoformat()

    artifact = {
        "artifact_id": f"compiled.{merged['pack_id']}.v{merged['version']}",
        "compiled_from": {
            "pack_id": merged["pack_id"],
            "pack_name": merged.get("pack_name", ""),
            "pack_version": merged["version"],
            "parent_pack_id": merged.get("inherits_from"),
            "constellation": merged.get("constellation", ""),
            "agent_role": merged.get("agent_role", ""),
        },
        "compiled_at": now,
        "compiler_version": COMPILER_VERSION,
        "compilation_report": {
            "stages_passed": [
                "input_validation",
                "inheritance_resolution",
                "override_application",
                "policy_resolution",
                "completeness_validation",
                "artifact_generation",
            ],
            "inheritance_chain": [p["pack_id"] for p in chain],
            "overrides_applied": overrides,
            "warnings": warnings,
        },
        "governance": {
            "authority_type": merged.get("authority_type", ""),
            "scope": merged.get("scope", {}),
            "governed_entities": merged.get("governed_entities", []),
            "governed_actions": merged.get("governed_actions", []),
            "rules": merged.get("rules", []),
            "control_gates": merged.get("control_gates", []),
            "evidence_requirements": merged.get("evidence_requirements", []),
            "escalation": merged.get("escalation", {}),
            "failure_semantics": merged.get("failure_semantics", {}),
        },
    }

    return artifact


# ── Stage 7: Host Binding ─────────────────────────────────────────

def stage_7_host_binding(artifact, output_dir):
    """Bind artifact to filesystem host."""
    now = datetime.now(timezone.utc).isoformat()
    pack_id = artifact["compiled_from"]["pack_id"]
    filename = f"{pack_id.replace('.', '_')}_compiled.json"
    host_path = os.path.join(output_dir, filename)

    artifact["host_binding"] = {
        "host_type": "filesystem",
        "host_path": host_path,
        "bound_at": now,
    }

    artifact["compilation_report"]["stages_passed"].append("host_binding")

    os.makedirs(output_dir, exist_ok=True)
    with open(host_path, "w", encoding="utf-8") as f:
        json.dump(artifact, f, indent=2, ensure_ascii=False)

    return host_path


# ── Stage 8: Output Registration ──────────────────────────────────

def stage_8_output_registration(artifact, host_path, vault_root):
    """Register compiled artifact in the compiler artifacts registry CSV.

    v0.3: Uses upsert — updates existing entry if pack_id matches,
    otherwise appends. No longer resets the registry on each run.
    """
    registry_path = os.path.join(
        vault_root,
        "05_SYSTEMS", "authority_architecture", "compiler",
        "compiler_artifacts_registry.csv"
    )

    artifact["compilation_report"]["stages_passed"].append("output_registration")

    fieldnames = [
        "artifact_id", "pack_id", "pack_version", "constellation",
        "agent_role", "compiled_date", "compiler_version",
        "host_type", "host_path", "status"
    ]

    new_row = {
        "artifact_id": artifact["artifact_id"],
        "pack_id": artifact["compiled_from"]["pack_id"],
        "pack_version": artifact["compiled_from"]["pack_version"],
        "constellation": artifact["compiled_from"].get("constellation", ""),
        "agent_role": artifact["compiled_from"].get("agent_role", ""),
        "compiled_date": datetime.now().strftime("%Y-%m-%d"),
        "compiler_version": artifact["compiler_version"],
        "host_type": artifact["host_binding"]["host_type"],
        "host_path": host_path,
        "status": "active",
    }

    # Read existing rows (if any)
    existing_rows = []
    if os.path.exists(registry_path) and os.path.getsize(registry_path) > 0:
        with open(registry_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            existing_rows = list(reader)

    # Upsert: replace if pack_id matches, otherwise append
    updated = False
    for i, row in enumerate(existing_rows):
        if row.get("pack_id") == new_row["pack_id"]:
            existing_rows[i] = new_row
            updated = True
            break

    if not updated:
        existing_rows.append(new_row)

    # Write back
    with open(registry_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing_rows)

    # Re-write the artifact with the final compilation report
    with open(host_path, "w", encoding="utf-8") as f:
        json.dump(artifact, f, indent=2, ensure_ascii=False)


# ── Main Compilation Pipeline ─────────────────────────────────────

def compile_pack(pack_path, output_dir, vault_root, search_dirs):
    """Run the full 8-stage compilation pipeline on a single pack."""
    pack_name = Path(pack_path).stem
    print(f"\n{'='*60}")
    print(f"  Compiling: {pack_name}")
    print(f"  Source:    {pack_path}")
    print(f"{'='*60}")

    # Load
    try:
        pack = load_pack(pack_path)
    except Exception as e:
        print(f"  FAIL: Could not load pack: {e}")
        return False

    if not pack:
        print(f"  FAIL: Pack file is empty")
        return False

    # Stage 1
    print(f"  Stage 1: Input Validation...", end=" ")
    schema = load_schema("authority_pack.schema.json")
    valid, errors = stage_1_input_validation(pack, schema)
    if not valid:
        print(f"FAIL")
        for e in errors:
            print(f"    {e}")
        return False
    print("PASS")

    # Stage 2
    print(f"  Stage 2: Inheritance Resolution...", end=" ")
    merged, chain, errors = stage_2_inheritance_resolution(pack, search_dirs)
    if merged is None:
        print(f"FAIL")
        for e in errors:
            print(f"    {e}")
        return False
    chain_display = " → ".join(p["pack_id"] for p in chain)
    print(f"PASS (chain: {chain_display})")

    # Stage 3
    print(f"  Stage 3: Override Application...", end=" ")
    merged, overrides = stage_3_override_application(merged, chain)
    print(f"PASS ({len(overrides)} overrides)")
    for o in overrides:
        print(f"    {o}")

    # Stage 4
    print(f"  Stage 4: Policy Resolution...", end=" ")
    valid, errors = stage_4_policy_resolution(merged)
    if not valid:
        print(f"FAIL")
        for e in errors:
            print(f"    {e}")
        return False
    print("PASS")

    # Stage 5
    print(f"  Stage 5: Completeness Validation...", end=" ")
    valid, errors, warnings = stage_5_completeness_validation(merged)
    if not valid:
        print(f"FAIL")
        for e in errors:
            print(f"    {e}")
        return False
    print(f"PASS ({len(warnings)} warnings)")
    for w in warnings:
        print(f"    {w}")

    # Stage 6
    print(f"  Stage 6: Artifact Generation...", end=" ")
    artifact = stage_6_artifact_generation(merged, chain, overrides, warnings)
    print("PASS")

    # Stage 7
    print(f"  Stage 7: Host Binding...", end=" ")
    host_path = stage_7_host_binding(artifact, output_dir)
    print(f"PASS → {host_path}")

    # Stage 8
    print(f"  Stage 8: Output Registration...", end=" ")
    stage_8_output_registration(artifact, host_path, vault_root)
    print("PASS")

    print(f"\n  ✓ Compilation successful: {artifact['artifact_id']}")
    return True


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Agent Maestro Authority Pack Compiler"
    )
    parser.add_argument(
        "input",
        help="Pack YAML file or directory containing pack YAML files"
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Output directory for compiled artifacts"
    )
    parser.add_argument(
        "--vault-root",
        default=None,
        help="Root directory of the Agent Maestro vault"
    )

    args = parser.parse_args()

    input_path = Path(args.input).resolve()

    # Determine vault root
    if args.vault_root:
        vault_root = Path(args.vault_root).resolve()
    else:
        # Walk up from input to find vault root (has 01_CAPTURE)
        vault_root = input_path
        while vault_root != vault_root.parent:
            if (vault_root / "01_CAPTURE").exists():
                break
            vault_root = vault_root.parent
        else:
            vault_root = Path.cwd()

    # Determine output directory
    if args.output_dir:
        output_dir = Path(args.output_dir).resolve()
    else:
        output_dir = Path(__file__).parent / "artifacts"

    # Search directories for inheritance resolution
    search_dirs = [
        vault_root / "05_SYSTEMS" / "authority_architecture" / "packs",
    ]

    # Collect pack files
    if input_path.is_file():
        pack_files = [input_path]
    elif input_path.is_dir():
        pack_files = sorted(input_path.glob("*.yaml"))
    else:
        print(f"Error: {input_path} is not a file or directory")
        sys.exit(1)

    if not pack_files:
        print(f"No .yaml files found in {input_path}")
        sys.exit(1)

    # Ensure registry CSV exists with headers (v0.3: append mode, no longer resets)
    registry_path = vault_root / "05_SYSTEMS" / "authority_architecture" / "compiler" / "compiler_artifacts_registry.csv"
    registry_headers = [
        "artifact_id", "pack_id", "pack_version", "constellation",
        "agent_role", "compiled_date", "compiler_version",
        "host_type", "host_path", "status"
    ]
    if not registry_path.exists() or registry_path.stat().st_size == 0:
        with open(registry_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(registry_headers)

    print(f"Agent Maestro Authority Pack Compiler v{COMPILER_VERSION}")
    print(f"Vault root: {vault_root}")
    print(f"Output dir: {output_dir}")
    print(f"Pack files: {len(pack_files)}")

    # Compile each pack
    results = {}
    for pack_file in pack_files:
        success = compile_pack(
            str(pack_file), str(output_dir), str(vault_root),
            [str(d) for d in search_dirs]
        )
        results[pack_file.name] = success

    # Summary
    print(f"\n{'='*60}")
    print(f"  Compilation Summary")
    print(f"{'='*60}")
    passed = sum(1 for v in results.values() if v)
    failed = sum(1 for v in results.values() if not v)
    for name, success in results.items():
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"  {status}  {name}")
    print(f"\n  Total: {len(results)} | Passed: {passed} | Failed: {failed}")


if __name__ == "__main__":
    main()
