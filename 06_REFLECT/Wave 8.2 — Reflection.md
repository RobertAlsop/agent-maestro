---
title: "Wave 8.2 — Reflection"
type: report
status: active
authority_weight: 30
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Proposal — Wave 8.2 Pipeline Enforcement Tooling]]"
    - "[[AM — Artifact Lifecycles]]"
    - "[[AM — Tool Conventions]]"
  governs: []
  related:
    - "[[AM — Roadmap]]"
    - "[[AM — Integrity Layers]]"
    - "[[AM — LLM Conventions]]"
tags: [reflection, wave-8, pipeline-enforcement, tooling]
---

# Wave 8.2 — Reflection

## What Happened

Wave 8.2 built the pipeline enforcement tool suite: five Python tools that verify lifecycle rules from [[AM — Artifact Lifecycles]] are being followed, plus the shared `vault_model.py` library that all five tools depend on.

**Phase 1 — Vault Model Library:**
- `lib/vault_model.py` — parses all vault markdown, extracts frontmatter, builds in-memory artifact model. Provides `build_vault_model()`, `parse_completed_waves()`, wiki-link parsing, date resolution, reference checking helpers, and standardized report writing. Each tool imports this library independently; each invocation rebuilds the model from scratch (separate processes). Economy value is code reuse, not parse reduction.

**Phase 2 — Five Pipeline Enforcement Tools:**
- `capture_triage.py` — triage deadline and routing provenance (warning)
- `proposal_lifecycle.py` — status/location, audit gate, reflection existence, archive gate
- `reflection_completeness.py` — reflection existence per completed wave, capture seed existence, provenance chains
- `concept_lifecycle.py` — draft stagnation, authority chain, reflection reference
- `governance_compliance.py` — authority floor, location enforcement, type/folder consistency

All five tools follow [[AM — Tool Conventions]]: read-only, config-driven, exit codes 0/1/2, Markdown reports, conservative. All integrated into `orchestrate.sh` and producing reports in the aggregate vault health report.

**Supporting deliverables:**
- `config/am.conf` extended with pipeline-specific configuration
- `README.md` updated with Wave 8.2 tool documentation and library architecture
- `SYSTEM_MAP.md` updated to reflect new tool suite contents

## What Was Learned

**The pipeline worked.** The tools ran on the first test and found real problems — not false positives. This is validation that the [[AM — Artifact Lifecycles]] spec was mechanically precise enough to implement directly. When the governance is good, the tools almost write themselves.

**The tools found real vault gaps immediately:**
- Wave 7 proposal was never archived (finishing ritual incomplete)
- Wave 8.1 has no reflection
- Wave 5 has no reflection
- Old reflections (5.1, 5.2 phases, 5.2 final, 6) have no capture seeds
- `AM — Future Waves Register` has authority_weight 60 < governance minimum 70
- `Git Best Practices for AI-Assisted Builds.md` has type: concept but lives in protocols/

These are not tool errors. These are real debt that accumulated because there was nothing detecting them. The first health check run surfaced six findings of real process drift. This is exactly what Wave 8.2 was built to find.

**Content-matching is too permissive for wave identification.** The first implementation of `find_reflection_for_wave` used a content fallback: "if the reflection content mentions the wave ID, it counts." This caused Wave 6's reflection (which mentions "what comes next: Wave 7") to be returned as the Wave 7 reflection. Filename-only matching with word-boundary precision was the correct approach. This is a Law 3 lesson: the simpler, more conservative implementation was also the more correct one.

**`[^✓]*` spans lines.** The first roadmap parsing regex used `[^✓]*` to match text before the ✓ mark. In Python, `[^x]` matches any character including newlines unless explicitly excluded. Combined with `re.MULTILINE`, this allowed the regex to span multiple lines and produce incorrect wave matches. Fixed by using `.*?` (without `re.DOTALL`, `.` does not match newlines).

**Type/folder consistency has a multi-location edge case.** Reflections are type: `report` but live in `06_REFLECT/`, not `05_RECORD/reports/`. The type_folder_map approach correctly flagged this as a mismatch — but it was a false positive, not a real finding. Resolution: remove `report` from `type_folder_map` in `am.conf`. Reports legitimately live in two folders; single-folder mapping is too restrictive for this type. This is the only case in the vault where a type maps to multiple valid locations.

**Wave 8.1 has an open reflection gap.** The tools confirmed that Wave 8.1 (governance) has no reflection in `06_REFLECT/`. This is a real finding, not a test artifact. Wave 8.1 was completed in an earlier session and the reflection was not written. The tools correctly detect it.

## Was the Wave's Question Answered?

Wave 8.2 asked: **Can AM mechanically verify that its own process is being followed — not just that its files are well-formed?**

Yes. The five tools now check whether proposals have been audited before reaching `active/`, whether completed waves have reflections, whether reflections have capture seeds, whether concepts are tracked back to their origin waves, and whether governance documents meet their authority thresholds. These are process-level checks, not structural ones. The distinction from Wave 6 is real and proved out on the first run.

## Concept Promotion Check

No new concepts emerged from Wave 8.2 that are not already represented in the vault. The wave produced tooling, not new intellectual territory. The existing concepts (Operational Intelligence, Self-Observation, Authority Architecture) already frame what was built. No concept promotion needed.

## What Comes Next

**Immediate debt (surfaced by Wave 8.2 tools):**
1. Write the Wave 8.1 reflection (Wave 8.1 is ✓ in Roadmap but no reflection exists)
2. Archive the Wave 7 proposal (finishing ritual gap — tool finding confirmed)
3. Raise `AM — Future Waves Register` authority_weight from 60 to 70 (governance floor finding)
4. Investigate `Git Best Practices` type/location mismatch (type: concept in protocols/ folder)
5. Create capture seeds for the old reflections that lack them (Waves 5.1, 5.2, 6)

**Wave 8.3 — Git-Ops** is next in the roadmap. AM-aware git enforcement: branch naming, commit format validation, uncommitted change detection, tag management. Needs its own design conversation — see [[AM — Future Waves Register]].

**Wave 9 — Generalized Audit Protocol** is the Stage 2 transition. The self-audit capability extracted into a protocol that works on any folder structure.

The vault now has mechanical enforcement at both layers of the integrity stack:
- **Structural:** Does the vault have the right shape? (Wave 6)
- **Process:** Is the pipeline being followed? (Wave 8.2)

Stage 1 is nearly complete. The remaining item is Wave 8.3 (Git-Ops). After that, Stage 1 exit criteria can be assessed.
