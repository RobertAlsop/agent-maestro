#!/usr/bin/env python3
"""proposal_lifecycle.py — Proposal artifact lifecycle enforcement.

Checks:
3. Status/location consistency: no proposal in active/ with status: draft;
   no proposal in proposals/ with status: active.
4. Audit gate: no proposal in active/ without a non-empty ## Audit section.
5. Completion gate: every active proposal whose wave is marked complete in the
   Roadmap has a corresponding reflection in 06_REFLECT/.
6. Archive gate: no proposal remains in active/ after its wave is complete.

Reads the Roadmap conservatively — unparseable entries are skipped and reported
as warnings, not findings.

Exit codes: 0 = clean, 1 = findings, 2 = error
"""

import sys
import os
import re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.vault_model import (
    build_vault_model, standard_arg_parser, resolve_tool_paths,
    write_report, parse_completed_waves, normalize_title, file_title,
)

TOOL_NAME = "Proposal Lifecycle"
REPORT_FILENAME = "Proposal_Lifecycle_report.md"
ACTIVE_FOLDER = "03_DECIDE/active"
PROPOSALS_FOLDER = "03_DECIDE/proposals"
REFLECT_FOLDER = "06_REFLECT"


def wave_id_from_artifact(artifact) -> str:
    """Extract wave identifier from a proposal artifact's filename or title.

    Returns e.g. 'Wave 6', 'Wave 8.1', or '' if not determinable.
    """
    # Check filename first
    for text in (artifact.rel_path, artifact.title or ''):
        m = re.search(r'\bWave\s+([\d.]+)', text, re.IGNORECASE)
        if m:
            return f"Wave {m.group(1)}"
    return ''


def has_reflection_for_wave(wave_id: str, reflections: list) -> bool:
    """Check if any reflection exists for the given wave identifier.

    Matches on filename only (conservative — content matching produces false
    positives from "what comes next" mentions of adjacent wave IDs).
    """
    wave_pattern = re.compile(re.escape(wave_id) + r'(?![\d.])', re.IGNORECASE)
    for ref in reflections:
        basename = os.path.basename(ref.rel_path)
        if wave_pattern.search(basename):
            return True
    return False


def main():
    parser = standard_arg_parser(
        "Enforce proposal artifact lifecycle rules from AM — Artifact Lifecycles."
    )
    args = parser.parse_args()
    vault_root, config, output_dir, _ = resolve_tool_paths(args, __file__)

    proposal_active_folder = config.get('proposal_active_folder', ACTIVE_FOLDER)
    proposal_draft_folder = config.get('proposal_draft_folder', PROPOSALS_FOLDER)
    roadmap_file = config.get('roadmap_file', '02_KNOWLEDGE/governance/AM — Roadmap.md')

    artifacts = build_vault_model(vault_root, config)
    findings = []
    warnings = []

    # Load Roadmap
    roadmap_path = os.path.join(vault_root, roadmap_file)
    completed_waves = []
    if os.path.exists(roadmap_path):
        with open(roadmap_path, 'r', encoding='utf-8') as f:
            roadmap_content = f.read()
        completed_waves = parse_completed_waves(roadmap_content)
        if not completed_waves:
            warnings.append(
                f"Roadmap at '{roadmap_file}' parsed but no completed waves (✓) found — "
                f"Checks 5 and 6 cannot run"
            )
    else:
        warnings.append(
            f"Roadmap not found at '{roadmap_file}' — Checks 5 and 6 skipped"
        )

    completed_wave_ids = {w['identifier'].lower() for w in completed_waves}

    # Collect active proposals, draft proposals, reflections
    active_proposals = [
        a for rel, a in artifacts.items()
        if rel.startswith(proposal_active_folder + '/')
        and a.artifact_type == 'proposal'
    ]
    draft_proposals = [
        a for rel, a in artifacts.items()
        if rel.startswith(proposal_draft_folder + '/')
        and a.artifact_type == 'proposal'
    ]
    reflections = [
        a for rel, a in artifacts.items()
        if rel.startswith(REFLECT_FOLDER + '/')
    ]

    checked = 0
    passed = 0
    checked_items = []

    # ----------------------------------------------------------------
    # Check 3a: No proposal in active/ with status: draft
    # ----------------------------------------------------------------
    for artifact in active_proposals:
        checked += 1
        checked_items.append(artifact)
        item_ok = True

        if artifact.status == 'draft':
            findings.append(
                f"{artifact.rel_path}: proposal in active/ has status: draft "
                f"— must be status: active or moved back to proposals/"
            )
            item_ok = False

        # ----------------------------------------------------------------
        # Check 4: No proposal in active/ without a non-empty ## Audit section
        # ----------------------------------------------------------------
        if not artifact.has_section_with_content('Audit'):
            findings.append(
                f"{artifact.rel_path}: proposal in active/ has no non-empty ## Audit section "
                f"— audit gate not passed"
            )
            item_ok = False

        # ----------------------------------------------------------------
        # Checks 5 & 6: Only apply to proposals for completed waves
        # ----------------------------------------------------------------
        wave_id = wave_id_from_artifact(artifact)
        if wave_id and wave_id.lower() in completed_wave_ids:
            # Check 5: Completed wave must have a reflection
            if not has_reflection_for_wave(wave_id, reflections):
                findings.append(
                    f"{artifact.rel_path}: {wave_id} is marked complete in Roadmap "
                    f"but no corresponding reflection found in {REFLECT_FOLDER}/"
                )
                item_ok = False

            # Check 6: Completed wave's proposal must not remain in active/
            findings.append(
                f"{artifact.rel_path}: {wave_id} is marked complete in Roadmap "
                f"but proposal still in active/ — should be archived to 05_RECORD/archive/"
            )
            item_ok = False

        if item_ok:
            passed += 1

    # ----------------------------------------------------------------
    # Check 3b: No proposal in proposals/ with status: active
    # ----------------------------------------------------------------
    for artifact in draft_proposals:
        checked += 1
        checked_items.append(artifact)
        if artifact.status == 'active':
            findings.append(
                f"{artifact.rel_path}: proposal in proposals/ has status: active "
                f"— must be moved to active/ or status corrected to draft"
            )
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
