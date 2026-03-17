---
title: "Self-Observation"
type: concept
status: active
authority_weight: 50
schema_version: 3
created: "2026-03-16"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
  governs: []
  related:
    - "[[Skill — Audit]]"
    - "[[Agent Maestro — Strategy]]"
    - "[[Proposal — Wave 9 Self-Observation]]"
    - "[[AM — Artifact Lifecycles]]"
    - "[[AM — LLM Conventions]]"
tags: [concept, self-observation, foundational]
---

# Self-Observation

## Purpose

Define how Agent Maestro monitors its own health and identifies opportunities for improvement. This concept is the foundation for the system's eventual self-improvement capability.

## Definition

Self-observation is the Irreducible Loop executed with the system itself as subject. It is not a separate architecture — it is the same perceive → interpret → decide → act → record → reflect pattern used everywhere in AM, applied reflexively to the system's own operational behaviour.

```
perceive → interpret → decide → act → record → reflect
    ↑                                              |
    └──────────────── next cycle ◀─────────────────┘
```

The intensity at which each stage executes maps to the existing escalation levels:

| Escalation Level | When | What the Loop produces |
|-----------------|------|----------------------|
| **Level 1 — Automatic** | Routine maintenance. No anomalies. | Extract metrics, compare to previous, log to CSV. |
| **Level 2 — Agent Judgment** | Anomalies or trends detected. | Causal analysis, formulate recommendation. |
| **Level 3 — Human Approval** | Observations touch governance or architecture. | Draft proposal, escalate with full context. |

## What Self-Observation Checks

Self-observation applies the three audit lenses (from [[Skill — Audit]]) to the system as a whole:

### Alignment (top-down)
Is the vault serving its stated purpose? Do the governance documents still reflect the human's intent? Has the system drifted from the North Star?

### Integrity (horizontal)
Are all parts consistent with each other? Do wiki-links resolve? Does frontmatter conform to schema? Are there contradictions between governance documents?

### Viability (bottom-up)
Is everything earning its place? Are there documents nobody references? Skills that never get used? Folders that accumulate without being processed? Law 3 applied to the whole vault.

## Current Implementation

Self-observation is **automated and escalation-governed** (Wave 9):

- **Perceive + Record (Phase 1):** `extract_metrics.py` reads the 13 per-tool reports produced by `orchestrate.sh` and transforms their summary tables into append-only CSV rows in `05_RECORD/logs/observation_metrics.csv`. Each run computes deltas from the previous run. This is the temporal memory layer — it records what happened and how it compares to what happened before.

- **Interpret + Decide (Phase 2):** `observation_analysis.py` reads the CSV history, identifies trends (improving, degrading, stable, anomalous), and invokes the LLM to interpret them at the appropriate escalation level. Level 1 produces a brief mechanical summary. Level 2 produces causal analysis and recommendations. Level 3 escalates governance concerns to the human.

- **Reflect-to-Perceive feedback (Phase 3):** The observation analysis from one cycle feeds the next cycle's attention — the system checks whether previously flagged metrics improved, degraded, or remained stable.

The full maintenance sequence runs daily via launchd:
```
orchestrate.sh → extract_metrics.py → observation_analysis.py → summarise_report.py → notify.sh
```

## Capability Progression

Per [[Agent Maestro — Strategy]], the path from Stage 1 (Self-Governance) toward Stage 2 (First External Application) requires self-observation to become more systematic and eventually more autonomous. The progression, now grounded in the Loop model:

1. **Manual** — Human + AI walk the vault together (Wave 5.2)
2. **Scheduled detection** — Automated integrity checks run on a cycle (Wave 6 + 7)
3. **Scheduled observation** — Metrics accumulated and trends analysed automatically (Wave 9) ← current
4. **Proposing** — The system identifies issues and drafts proposals, subject to human approval
5. **Self-improving** — The full Reflect → Capture → Decide → Execute loop runs with human gate at Level 3 only

Each step increases autonomy while maintaining governance. D5 (Governance Before Autonomy) applies — the governance for each step must exist before the capability is deployed.

## Traceability

Self-observation is the operational expression of Seed 1 (Process) — specifically the Irreducible Loop applied to itself (fractal recursion). It also implements Seed 2 (Structure) — the Feedback primitive ("how do we know if the action worked?"). The three audit lenses come directly from the Audit Taxonomy in [[Agent Maestro — Foundations]]. The escalation levels come from Seed 3 (Constraint) — the same model used everywhere in AM.

The key design finding from Wave 9: self-observation is not a new architecture. It is the existing architecture applied reflexively. No new frameworks, depth levels, or observation models are needed. The existing architecture is sufficient.

## Related

- [[Agent Maestro — Foundations]]
- [[Skill — Audit]]
- [[Agent Maestro — Strategy]]
- [[Proposal — Wave 9 Self-Observation]]
- [[AM — Artifact Lifecycles]]
- [[AM — LLM Conventions]]
