#!/usr/bin/env python3
"""concept_lifecycle.py — Concept artifact lifecycle enforcement.

Checks:
11. Draft stagnation: no concept in status: draft for more than
    concept_review_deadline_days (default 30) without review.
12. Authority chain: every active concept has a non-empty derives_from relationship.
13. Reflection reference: every active concept is referenced by at least one
    reflection in 06_REFLECT/ (simplified per audit finding IN-2 — reference
    existence check, not temporal mapping).

Exit codes: 0 = clean, 1 = findings, 2 = error
"""

import sys
import os
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.vault_model import (
    build_vault_model, standard_arg_parser, resolve_tool_paths,
    write_report, normalize_title, file_title,
)

TOOL_NAME = "Concept Lifecycle"
REPORT_FILENAME = "Concept_Lifecycle_report.md"
CONCEPTS_FOLDER = "02_KNOWLEDGE/concepts"
REFLECT_FOLDER = "06_REFLECT"


def main():
    parser = standard_arg_parser(
        "Enforce concept artifact lifecycle rules from AM — Artifact Lifecycles."
    )
    args = parser.parse_args()
    vault_root, config, output_dir, _ = resolve_tool_paths(args, __file__)

    review_deadline_days = int(config.get('concept_review_deadline_days', 30))
    today = date.today()

    artifacts = build_vault_model(vault_root, config)
    findings = []
    warnings = []
    checked = 0
    passed = 0

    concepts = [
        a for rel, a in artifacts.items()
        if rel.startswith(CONCEPTS_FOLDER + '/')
    ]
    reflections = [
        a for rel, a in artifacts.items()
        if rel.startswith(REFLECT_FOLDER + '/')
    ]

    for artifact in concepts:
        checked += 1
        item_ok = True
        concept_title = file_title(artifact.rel_path)
        fm_title_normalized = normalize_title(artifact.title) if artifact.title else None

        # ----------------------------------------------------------------
        # Check 11: Draft stagnation
        # ----------------------------------------------------------------
        if artifact.status == 'draft':
            if artifact.created_date is not None:
                age_days = (today - artifact.created_date).days
                if age_days > review_deadline_days:
                    findings.append(
                        f"{artifact.rel_path}: concept has been in status: draft for {age_days} days "
                        f"(deadline: {review_deadline_days} days) — review overdue"
                    )
                    item_ok = False

        # ----------------------------------------------------------------
        # Check 12: Authority chain (active concepts only)
        # ----------------------------------------------------------------
        if artifact.status == 'active':
            if not artifact.derives_from:
                findings.append(
                    f"{artifact.rel_path}: active concept has empty derives_from — "
                    f"authority chain missing"
                )
                item_ok = False

            # ----------------------------------------------------------------
            # Check 13: Reflection reference (active concepts only)
            # Simplified: verify concept is referenced by at least one reflection.
            # ----------------------------------------------------------------
            referenced_by_reflection = any(
                concept_title in ref.all_wiki_links
                or (fm_title_normalized and fm_title_normalized in ref.all_wiki_links)
                for ref in reflections
            )
            if not referenced_by_reflection:
                findings.append(
                    f"{artifact.rel_path}: active concept is not referenced by any reflection "
                    f"in {REFLECT_FOLDER}/ — concept origin not traced to a wave"
                )
                item_ok = False

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
