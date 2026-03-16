---
title: "Tools Evolution"
type: pipeline
status: active
authority_weight: 10
schema_version: 3
created: "2026-03-16"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Wave 6 — Reflection]]"
  governs: []
  related:
    - "[[AM — Tool Conventions]]"
    - "[[AM — Integrity Layers]]"
    - "[[AM — Future Waves Register]]"
tags: [capture, tools, strategy]
---

# Tools Evolution

## Original Question

What are the minimum viable or maximum safe set of tool suites for Agent Maestro?

## Analysis (2026-03-17)

Discussed during Wave 7 proposal session. Three-tier answer:

**Minimum viable for Stage 1 (three suites):**

1. **vault-maintenance** (Wave 6 ✓) — "Is the vault structurally sound?" Files, links, YAML, orphans, naming.
2. **runtime** (Wave 7 — approved) — "Can AM operate autonomously?" Scheduling, orchestration, semantic summary, notification.
3. **pipeline-enforcement** — "Is the process being followed?" Verifies pipeline stages complete, proposals move through lifecycle, reflections exist, capture seeds close the loop. Proven need: Wave 6 reflection was skipped.

**Maximum safe for Stage 1 (adds two more):**

4. **git-ops** — "Is the repository well-managed?" Branch status, uncommitted changes, commit format, tag management. Proven friction: manual git operations in Cowork are irritating; Claude Code handles git but has no AM-aware enforcement.
5. **report-analytics** — "Are things getting better or worse?" Cross-run comparison, trend analysis, diff between health reports. Need not yet proven — requires accumulated daily reports from Wave 7.

**Decision:** Pipeline-enforcement and git-ops are scoped for Wave 8. Report-analytics deferred to the Future Waves Register.
