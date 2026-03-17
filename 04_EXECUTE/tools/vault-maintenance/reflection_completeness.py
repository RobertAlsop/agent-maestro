#!/usr/bin/env python3
"""reflection_completeness.py — Reflection and capture seed lifecycle enforcement.

Checks:
7. Reflection existence: every wave marked complete (✓) in the Roadmap has a
   corresponding reflection in 06_REFLECT/.
8. Capture seed existence: every reflection in 06_REFLECT/ has a corresponding
   capture seed in 01_CAPTURE/.
9. Reflection provenance: the reflection's derives_from includes the wave's proposal.
10. Capture seed provenance: the capture seed references the reflection.

Note: Check 7 intentionally overlaps with proposal_lifecycle.py Check 5.
Per Convention 4 (Independence) each tool must be independently complete.
Duplicate findings in the aggregate report are by design — same problem, two angles.

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

TOOL_NAME = "Reflection Completeness"
REPORT_FILENAME = "Reflection_Completeness_report.md"
REFLECT_FOLDER = "06_REFLECT"
CAPTURE_FOLDER = "01_CAPTURE"


def find_reflection_for_wave(wave_id: str, reflections: list):
    """Find a reflection artifact for the given wave identifier.

    Matches on filename only (not content). Content matching is too imprecise
    because reflections often mention adjacent wave IDs in "what comes next"
    sections, producing false matches. Filename matching is conservative:
    "Wave 7" matches "Wave 7 — Reflection.md" but not "Wave 7.1 — ...".

    Wave ID must be followed by whitespace, dash, end of string, or .md to
    prevent "Wave 8" from matching "Wave 8.1 — Reflection.md".
    """
    # Precise: wave_id followed by word boundary (not another digit or dot)
    wave_pattern = re.compile(
        re.escape(wave_id) + r'(?![\d.])',
        re.IGNORECASE
    )
    for ref in reflections:
        basename = os.path.basename(ref.rel_path)
        if wave_pattern.search(basename):
            return ref
    return None


def find_proposal_for_wave(wave_id: str, artifacts: dict):
    """Find the proposal artifact for the given wave identifier.

    Checks 03_DECIDE/ (active and proposals) and 05_RECORD/archive/.
    Returns first match or None.
    """
    wave_pattern = re.compile(re.escape(wave_id), re.IGNORECASE)
    for rel_path, artifact in artifacts.items():
        if artifact.artifact_type != 'proposal':
            continue
        if wave_pattern.search(rel_path) or (artifact.title and wave_pattern.search(artifact.title)):
            return artifact
    return None


def find_seed_for_reflection(reflection, capture_items: list):
    """Find a capture seed that references the reflection.

    Returns the first capture item that references the reflection by
    wiki-link or content mention. Returns None if not found.
    """
    ref_title = file_title(reflection.rel_path)
    # Also check frontmatter title
    ref_fm_title = normalize_title(reflection.title) if reflection.title else None

    for capture in capture_items:
        # Direct wiki-link reference
        if ref_title in capture.all_wiki_links:
            return capture
        if ref_fm_title and ref_fm_title in capture.all_wiki_links:
            return capture
        # Raw content mention (handles "Wave 8.1 — Reflection" style references)
        if reflection.title and reflection.title.lower() in capture.content.lower():
            return capture
        # Filename fragment match
        basename = os.path.splitext(os.path.basename(reflection.rel_path))[0]
        if basename.lower() in capture.content.lower():
            return capture
    return None


def main():
    parser = standard_arg_parser(
        "Enforce reflection and capture seed lifecycle rules from AM — Artifact Lifecycles."
    )
    args = parser.parse_args()
    vault_root, config, output_dir, _ = resolve_tool_paths(args, __file__)

    roadmap_file = config.get('roadmap_file', '02_KNOWLEDGE/governance/AM — Roadmap.md')

    artifacts = build_vault_model(vault_root, config)
    findings = []
    warnings = []
    checked = 0
    passed = 0

    # Load Roadmap
    roadmap_path = os.path.join(vault_root, roadmap_file)
    completed_waves = []
    if os.path.exists(roadmap_path):
        with open(roadmap_path, 'r', encoding='utf-8') as f:
            roadmap_content = f.read()
        completed_waves = parse_completed_waves(roadmap_content)
        if not completed_waves:
            warnings.append(
                f"Roadmap at '{roadmap_file}' parsed but no completed waves found — "
                f"Checks 7, 9 cannot run"
            )
    else:
        warnings.append(
            f"Roadmap not found at '{roadmap_file}' — Checks 7, 9 skipped"
        )

    reflections = [
        a for rel, a in artifacts.items()
        if rel.startswith(REFLECT_FOLDER + '/')
    ]
    capture_items = [
        a for rel, a in artifacts.items()
        if rel.startswith(CAPTURE_FOLDER + '/')
    ]

    # ----------------------------------------------------------------
    # Checks 7 & 9: Per completed wave — reflection existence + provenance
    # ----------------------------------------------------------------
    for wave in completed_waves:
        wave_id = wave['identifier']
        checked += 1
        item_ok = True

        reflection = find_reflection_for_wave(wave_id, reflections)

        # Check 7: Reflection must exist
        if reflection is None:
            findings.append(
                f"{wave_id}: marked complete in Roadmap but no reflection found in {REFLECT_FOLDER}/"
            )
            item_ok = False
        else:
            # Check 9: Reflection's derives_from must include the wave's proposal
            proposal = find_proposal_for_wave(wave_id, artifacts)
            if proposal:
                proposal_title = normalize_title(
                    proposal.title or os.path.splitext(os.path.basename(proposal.rel_path))[0]
                )
                derives_normalized = [normalize_title(d) for d in (reflection.derives_from or [])]
                if proposal_title not in derives_normalized:
                    # Also check raw content for proposal mention
                    if proposal_title not in reflection.content.lower():
                        findings.append(
                            f"{reflection.rel_path}: reflection for {wave_id} — "
                            f"derives_from does not include the wave's proposal "
                            f"({proposal.rel_path})"
                        )
                        item_ok = False
            else:
                warnings.append(
                    f"{wave_id}: no proposal artifact found — Check 9 (reflection provenance) skipped"
                )

        if item_ok:
            passed += 1

    # ----------------------------------------------------------------
    # Checks 8 & 10: Per reflection — capture seed existence + provenance
    # ----------------------------------------------------------------
    for reflection in reflections:
        checked += 1
        item_ok = True

        seed = find_seed_for_reflection(reflection, capture_items)

        # Check 8: Capture seed must exist
        if seed is None:
            findings.append(
                f"{reflection.rel_path}: no capture seed found in {CAPTURE_FOLDER}/ "
                f"referencing this reflection"
            )
            item_ok = False
        else:
            # Check 10: Seed must reference the reflection
            ref_title = file_title(reflection.rel_path)
            ref_fm_title = normalize_title(reflection.title) if reflection.title else None
            basename = os.path.splitext(os.path.basename(reflection.rel_path))[0]

            seed_references = (
                ref_title in seed.all_wiki_links
                or (ref_fm_title and ref_fm_title in seed.all_wiki_links)
                or (reflection.title and reflection.title.lower() in seed.content.lower())
                or basename.lower() in seed.content.lower()
            )
            if not seed_references:
                findings.append(
                    f"{seed.rel_path}: capture seed for {reflection.rel_path} "
                    f"does not reference the reflection — provenance link missing"
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
