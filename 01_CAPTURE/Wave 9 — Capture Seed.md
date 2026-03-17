---
title: "Wave 9 — Capture Seed"
type: pipeline
status: draft
authority_weight: 10
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Wave 9 — Reflection]]"
  governs: []
  related:
    - "[[AM — Roadmap]]"
    - "[[AM — Future Waves Register]]"
    - "[[Self-Observation]]"
tags: [capture, seed, wave-9, stage-2]
---

# Wave 9 — Capture Seed

Seeds from [[Wave 9 — Reflection]] for future work.

## Stage 2 Readiness

Wave 9 completes Stage 1 (Self-Governance). The Roadmap points to Stage 2 (First External Application). Seeds:

- **Generalized Audit Protocol (Wave 10):** Extract AM's self-audit capability into a protocol that works on any folder structure or vault. The detection tools are AM-specific; the audit *pattern* is universal. What's the minimum extraction that lets AM assess a system it didn't build?

- **Proposal archival backlog:** Waves 7, 8.2, 8.3, and 9 all have proposals in `active/` that should be archived. This is a finishing ritual gap that the Proposal Lifecycle tool already flags.

## Observation Infrastructure

- **Inventory report format:** The one tool whose metrics can't be extracted by the standard parser. Either extend the report format or add a custom parser. Low priority — flag for future attention.

- **Observation data quality:** After 5+ runs, review the observation CSV and the first trend analyses. Are the metrics carrying useful signal? Which should be disabled? This is the empirical refinement the proposal anticipated.

- **Dashboard possibility:** `observation_metrics.csv` is a structured, append-only data source. A simple visualisation (even a spreadsheet chart) would make trends visible to the human without reading the LLM analysis. Deferred in Wave 9 scope but worth revisiting.

## Convention Gaps

- **Data transformation tool type:** `extract_metrics.py` exposed the first case where Tool Conventions don't fully apply. If future waves produce similar tools (stateful, writes to vault content tree), a convention extension may be warranted. For now, the honest characterisation in the tool's docstring is sufficient.
