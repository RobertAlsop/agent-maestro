#!/usr/bin/env python3
"""capture_triage.py — Capture item lifecycle enforcement.

Checks:
1. Triage deadline: capture items older than capture_triage_deadline_days (default 14)
   that are not referenced by any other vault artifact.
2. Routing provenance (warning): capture items referenced by another artifact
   but whose destination does not link back. Reported as warnings per audit
   finding IN-3 (risk of false positives on informally triaged items).
   Applied only to capture items created on or after 2026-03-17 (when
   bidirectional linking was formalised in AM — Artifact Lifecycles).

Exit codes: 0 = clean, 1 = findings, 2 = error
"""

import sys
import os
from datetime import date

# Allow running from vault-maintenance/ directly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.vault_model import (
    build_vault_model, standard_arg_parser, resolve_tool_paths,
    write_report, normalize_title, file_title, find_artifacts_in_folder,
)

TOOL_NAME = "Capture Triage"
REPORT_FILENAME = "Capture_Triage_report.md"
CAPTURE_FOLDER = "01_CAPTURE"
LIFECYCLE_FORMALISED_DATE = date(2026, 3, 17)


def main():
    parser = standard_arg_parser(
        "Enforce capture item lifecycle rules from AM — Artifact Lifecycles."
    )
    args = parser.parse_args()
    vault_root, config, output_dir, _ = resolve_tool_paths(args, __file__)

    deadline_days = int(config.get('capture_triage_deadline_days', 14))
    today = date.today()

    artifacts = build_vault_model(vault_root, config)

    # Separate capture items from everything else
    capture_items = [
        a for rel, a in artifacts.items()
        if rel.startswith(CAPTURE_FOLDER + '/')
    ]
    non_captures = {
        rel: a for rel, a in artifacts.items()
        if not rel.startswith(CAPTURE_FOLDER + '/')
    }

    findings = []
    warnings = []
    checked = 0
    passed = 0

    for artifact in capture_items:
        checked += 1
        item_title = file_title(artifact.rel_path)
        item_findings = []

        # ----------------------------------------------------------------
        # Check 1: Triage deadline
        # ----------------------------------------------------------------
        if artifact.created_date is not None:
            age_days = (today - artifact.created_date).days
            if age_days > deadline_days:
                # Check if referenced anywhere outside 01_CAPTURE
                is_referenced = any(
                    item_title in a.all_wiki_links
                    for a in non_captures.values()
                )
                # Also check by frontmatter title if present
                if not is_referenced and artifact.title:
                    title_normalized = normalize_title(artifact.title)
                    is_referenced = any(
                        title_normalized in a.all_wiki_links
                        for a in non_captures.values()
                    )
                if not is_referenced:
                    item_findings.append(
                        f"{artifact.rel_path}: untriaged for {age_days} days "
                        f"(deadline: {deadline_days} days) — not referenced by any vault artifact"
                    )

        # ----------------------------------------------------------------
        # Check 2: Routing provenance (warning — IN-3)
        # Only for captures created on/after lifecycle formalisation date.
        # ----------------------------------------------------------------
        if artifact.created_date is not None and artifact.created_date >= LIFECYCLE_FORMALISED_DATE:
            # Is this capture referenced by a non-capture artifact?
            referencing_artifacts = [
                a for a in non_captures.values()
                if item_title in a.all_wiki_links
                or (artifact.title and normalize_title(artifact.title) in a.all_wiki_links)
            ]
            if referencing_artifacts:
                # Check if any of those referencing artifacts link back from the capture's perspective:
                # i.e., does the capture itself reference any of those destinations?
                capture_links = set(artifact.all_wiki_links)
                destination_titles = {
                    file_title(a.rel_path) for a in referencing_artifacts
                }
                no_backlink = not capture_links.intersection(destination_titles)
                if no_backlink:
                    dest_list = ', '.join(
                        a.rel_path for a in referencing_artifacts[:3]
                    )
                    warnings.append(
                        f"{artifact.rel_path}: referenced by [{dest_list}] "
                        f"but does not link back — bidirectional provenance incomplete"
                    )

        if item_findings:
            findings.extend(item_findings)
        else:
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
