---
title: "Retrospective Exemptions"
type: report
status: active
authority_weight: 30
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[AM — Artifact Lifecycles]]"
  governs: []
  related:
    - "[[Wave 5.1 — Design Session Reflection]]"
    - "[[Wave 5.2 — Phases 1–3 Reflection]]"
    - "[[Wave 5.2 — Final Reflection]]"
    - "[[Wave 6 — Reflection]]"
    - "[[Wave 8.2 — Reflection]]"
tags: [reflection, exemption, governance, debt-resolution]
---

# Retrospective Exemptions

This document records legitimate exemptions from reflection and capture seed requirements for waves completed before those requirements were formalised. It exists so the pipeline enforcement tools have an honest target rather than flagging known, accepted gaps.

## Missing Reflections

### Wave 5 — No Reflection

Wave 5 was completed before [[AM — Artifact Lifecycles]] established the requirement that every completed wave must have a reflection. No reflection was written at the time. Writing one retroactively would produce a compliance artifact with no genuine learning value — the agent writing it did not do the work and the human's memory of the wave has faded. Exempted.

### Wave 8.1 — No Reflection

Wave 8.1 (governance) produced [[AM — Artifact Lifecycles]], [[AM — LLM Conventions]], and [[AM — Git Conventions]]. The reflection was not written at session close. The governance documents themselves are the lasting output — the learning is embedded in the specs. A retroactive reflection would restate what the documents already say. Exempted.

## Missing Capture Seeds

### Wave 5.1 — Design Session Reflection

Reflection exists. No capture seed was created. Wave 5.1 predates the capture seed convention. The work that would have been seeded was already absorbed into subsequent waves. Exempted.

### Wave 5.2 — Phases 1–3 Reflection

Reflection exists. No capture seed was created. Same rationale as Wave 5.1. Exempted.

### Wave 5.2 — Final Reflection

Reflection exists. No capture seed was created. Same rationale as Wave 5.1. Exempted.

### Wave 6 — Reflection

Reflection exists. No capture seed was created. Wave 6 predates the formal capture seed requirement. The reflection's "what comes next" content was absorbed into the Wave 7 and Wave 8 design conversations. Exempted.

## Missing Capture Seed (Post-Convention)

### Wave 8.2 — No Wave 8.3 Capture Seed

Wave 8.2 was completed after [[AM — Artifact Lifecycles]] formalised the capture seed requirement. The proposal's gate criteria explicitly included "Capture seed for Wave 8.3 created in `01_CAPTURE/`." The build session declared completion without creating this artifact — the closing ritual was skipped for the seed step.

This is not exempted in the same way as the pre-convention gaps above. The requirement existed and was not met. However, a separate brainstorm ([[Wave 8.3 — Git-Ops Brainstorm]]) was created independently and covers the same ground a capture seed would have. The input for Wave 8.3 exists; it just arrived through a different path.

**Process note:** The wave that built the tools to detect skipped closing rituals skipped part of its own closing ritual. This should inform how closing rituals are reinforced — detection alone is not prevention.

## Policy

Items listed here are acknowledged debt, not ignored debt. The pipeline enforcement tools may still flag them. When reviewing tool reports, findings that match an entry in this document can be treated as known and accepted.

If the vault introduces a mechanism for tool-level exemptions (e.g., an `exemptions` section in `am.conf`), the entries here should be migrated to that mechanism and this document archived.
