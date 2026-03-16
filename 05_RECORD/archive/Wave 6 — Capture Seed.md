---
title: "Wave 6 — Capture Seed"
type: pipeline
status: active
authority_weight: 10
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from:
    - "[[Wave 5.2 — Final Reflection]]"
  governs: []
  related:
    - "[[AM — Roadmap]]"
    - "[[AM — Future Waves Register]]"
tags: [seed, capture, wave-6]
---

# Wave 6 — Capture Seed

## Source

Derived from [[Wave 5.2 — Final Reflection]]. Wave 5.2 (Pipeline Hardening) is complete — all six phases delivered, all completion criteria met.

## What Feeds Forward

### Primary: Wave 6 — Mechanical Integrity

The [[AM — Roadmap|Roadmap]] identifies this as the next committed wave. The question it answers: **Can AM detect its own structural problems?**

Build the shell script layer for deterministic vault validation. Core capabilities from the [[AM — Future Waves Register|Register]]: broken link detection, YAML validation, orphan detection, inventory generation, duplicate ID detection, stub detection. Config-driven and portable.

Key design principle established in Wave 5.2: scripts enforce mechanical integrity, LLMs enforce semantic integrity. Scripts detect and report; they never interpret meaning.

See the Register's "Mechanical Integrity Layer" entry for the full idea set, including the agent responsibility collision architecture (Layers 0–5).

### Secondary Items

- **Universal Workflow status:** Currently `draft`. Review after one wave of use and promote to `active` if it holds.
- **Wiki-links in skill files:** 6 of 7 lack body wiki-links. Minor cleanup.
- **Git housekeeping:** Commit all Wave 5.2 changes, manage branches.

## Entry Point

Consult the [[AM — Roadmap]] and [[AM — Future Waves Register]] per Vault Rule 52. Draft a proposal for Wave 6 in `03_DECIDE/proposals/`.
