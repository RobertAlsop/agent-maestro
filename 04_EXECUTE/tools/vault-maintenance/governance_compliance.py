#!/usr/bin/env python3
"""governance_compliance.py — Governance document structural compliance enforcement.

Checks:
14. Authority floor: all documents in 02_KNOWLEDGE/governance/ with type: governance
    have authority_weight >= governance_min_authority_weight (default 70).
15. Location enforcement: all documents anywhere in the vault with type: governance
    are located in 02_KNOWLEDGE/governance/ (or a subfolder thereof).
17. Type/folder consistency: the type field in frontmatter matches the expected
    type for the folder the artifact lives in (per type_folder_map in config).
    Note: Check 16 (schema compliance) is intentionally omitted — it is already
    covered by yaml_validation.sh (yaml_validator.py). Per audit finding VI-1,
    duplicating it here would muddier concern boundaries.
    Check 17 is not in AM — Artifact Lifecycles; it was added per AL-1 finding
    as an implied structural rule. See proposal audit section.

Exemptions:
- CLAUDE.md, README.md, SYSTEM_MAP.md are never checked (structural files).
- Archive is excluded via exclude_patterns.
- Files in frontmatter_optional_folders are excluded from type/folder consistency.

Exit codes: 0 = clean, 1 = findings, 2 = error
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.vault_model import (
    build_vault_model, standard_arg_parser, resolve_tool_paths,
    write_report, is_frontmatter_optional,
)

TOOL_NAME = "Governance Compliance"
REPORT_FILENAME = "Governance_Compliance_report.md"
GOVERNANCE_FOLDER = "02_KNOWLEDGE/governance"

# Default type → folder prefix mapping (can be overridden in config)
DEFAULT_TYPE_FOLDER_MAP = {
    'governance': '02_KNOWLEDGE/governance',
    'concept': '02_KNOWLEDGE/concepts',
    'skill': '02_KNOWLEDGE/skills',
    'role': '02_KNOWLEDGE/governance/roles',
    'proposal': '03_DECIDE',
    'log': '05_RECORD/logs',
    'report': '05_RECORD/reports',
}


def main():
    parser = standard_arg_parser(
        "Enforce governance document structural compliance from AM — Artifact Lifecycles."
    )
    args = parser.parse_args()
    vault_root, config, output_dir, _ = resolve_tool_paths(args, __file__)

    governance_folder = config.get('governance_folder', GOVERNANCE_FOLDER)
    min_authority = int(config.get('governance_min_authority_weight', 70))
    type_folder_map = config.get('type_folder_map', DEFAULT_TYPE_FOLDER_MAP)
    optional_folders = config.get('frontmatter_optional_folders', [])

    artifacts = build_vault_model(vault_root, config)
    findings = []
    warnings = []
    checked = 0
    passed = 0

    for rel_path, artifact in artifacts.items():
        if not artifact.has_frontmatter:
            # Only check artifacts with frontmatter
            continue

        item_ok = True
        item_checked = False

        # ----------------------------------------------------------------
        # Check 14: Authority floor for documents IN governance folder
        # ----------------------------------------------------------------
        in_governance_folder = rel_path.startswith(governance_folder + '/')
        if in_governance_folder and artifact.artifact_type == 'governance':
            item_checked = True
            aw = artifact.authority_weight
            if aw is None or not isinstance(aw, (int, float)):
                findings.append(
                    f"{rel_path}: governance document has no numeric authority_weight "
                    f"(minimum required: {min_authority})"
                )
                item_ok = False
            elif aw < min_authority:
                findings.append(
                    f"{rel_path}: governance document has authority_weight {aw} "
                    f"< minimum {min_authority}"
                )
                item_ok = False

        # ----------------------------------------------------------------
        # Check 15: Location enforcement — type: governance must be in governance folder
        # ----------------------------------------------------------------
        if artifact.artifact_type == 'governance' and not in_governance_folder:
            item_checked = True
            findings.append(
                f"{rel_path}: type: governance but located outside {governance_folder}/ "
                f"— governance documents must live in the governance folder"
            )
            item_ok = False

        # ----------------------------------------------------------------
        # Check 17: Type/folder consistency
        # Skip frontmatter-optional folders (captures, session logs).
        # ----------------------------------------------------------------
        if (artifact.artifact_type
                and not is_frontmatter_optional(rel_path, optional_folders)):
            expected_folder = type_folder_map.get(artifact.artifact_type)
            if expected_folder is not None:
                item_checked = True
                if not rel_path.startswith(expected_folder + '/') and rel_path != expected_folder:
                    findings.append(
                        f"{rel_path}: type: {artifact.artifact_type!r} but located in "
                        f"'{os.path.dirname(rel_path)}' — expected location: {expected_folder}/"
                    )
                    item_ok = False

        if item_checked:
            checked += 1
            if item_ok:
                passed += 1

    result = "CLEAN" if not findings else "FINDINGS"
    report_path = write_report(
        output_dir, REPORT_FILENAME, TOOL_NAME, vault_root,
        result, checked, passed, findings, warnings
    )

    if not args.quiet:
        print(f"{TOOL_NAME}: {result} ({checked} checked, {len(findings)} findings, {len(warnings)} warnings)")
        print(f"Report: {report_path}")

    sys.exit(0 if not findings else 1)


if __name__ == '__main__':
    main()
