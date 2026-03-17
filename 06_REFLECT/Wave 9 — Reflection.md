---
title: "Wave 9 — Reflection"
type: report
status: active
authority_weight: 30
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
    - "[[Proposal — Wave 9 Self-Observation]]"
  governs: []
  related:
    - "[[Wave 7 — Reflection]]"
    - "[[AM — Roadmap]]"
    - "[[AM — LLM Conventions]]"
    - "[[AM — Artifact Lifecycles]]"
    - "[[Self-Observation]]"
tags: [reflection, reflect, wave-9, self-observation]
---

# Wave 9 — Reflection

## Purpose

Close the loop on Wave 9 (Self-Observation). This wave asked one question: "Can AM observe and measure its own operational behaviour?" The answer is yes.

## What Happened

### Starting State

Waves 6 through 8.3 delivered a comprehensive detection suite — 13 tools that check structural integrity, pipeline compliance, and git hygiene. Wave 7 made them run autonomously via launchd. But each health report was a snapshot. When the next run happened, the previous report was overwritten. AM had no temporal memory of its own operation — it could not answer whether findings were increasing or decreasing, whether changes actually helped, or how long patterns persisted.

The [[Wave 9 — Self-Observation Brainstorm]] and [[Wave 9 — Design Analysis v2]] established the key design finding: self-observation is not a new architecture. It is the Irreducible Loop applied reflexively — the same pattern used everywhere in AM, applied to the system's own operational behaviour with time as the new dimension.

### Key Decisions

1. **Full scope executed — all three phases.** Phase 1 (metric extraction), Phase 2 (semantic trend analysis), and Phase 3 (governance extensions + Reflect-to-Perceive feedback) were all built in a single session. The proposal's degradation plan allowed Phase 1 only (minimum viable) or Phases 1+2 (standard), but each phase was compact and the dependencies were linear.

2. **`extract_metrics.py` as a data transformation tool, not a detection tool.** The proposal audit (AL-1) identified that this tool doesn't fit the standard Tool Conventions model — it's stateful across runs (reads previous CSV) and writes to the vault content tree (`05_RECORD/logs/`). Rather than forcing compliance, the tool was honestly characterised as a new tool type that borrows applicable conventions (config-driven, exit codes, conservative) while acknowledging the differences. This honest characterisation is better than a misleading claim of full compliance.

3. **`observation_analysis.py` in `runtime/`, not `tools/`.** Following the Wave 7 precedent — LLM-invoking scripts live in `04_EXECUTE/runtime/` to keep the tools directory pure-mechanical. This keeps the [[AM — Integrity Layers]] boundary clean.

4. **Escalation level computed from threshold only, not direction.** The proposal audit (IN-3) identified gaps in the original escalation computation. The resolution simplified it: threshold breach = registry's default escalation; no breach = Level 1. Direction (improving/degrading/stable) is recorded as metadata for the LLM to reason about but does not affect the mechanical escalation. This keeps the mechanical/semantic boundary clean.

5. **Graceful degradation throughout.** Inventory's non-standard report format is skipped with a warning. Missing Ollama produces a mechanical-only report. Insufficient history exits cleanly. Every failure mode was encountered during testing and handled.

### Artifacts Produced

| Artifact | Location | Phase |
|----------|----------|-------|
| `extract_metrics.py` | `04_EXECUTE/tools/vault-maintenance/` | 1 |
| `metric_registry.csv` | `04_EXECUTE/tools/vault-maintenance/config/` | 1 |
| `observation_metrics.csv` | `05_RECORD/logs/` | 1 |
| `observation_analysis.py` | `04_EXECUTE/runtime/` | 2 |
| Temporal Reasoning Conventions section | `AM — LLM Conventions` | 2 |
| Observation analysis lifecycle + retention policy | `AM — Artifact Lifecycles` | 3 |
| Self-Observation concept update | `02_KNOWLEDGE/concepts/Self-Observation.md` | 3 |
| Reflect-to-Perceive feedback | `extract_metrics.py` extension | 3 |

### Modifications to Existing Artifacts

| Artifact | Change |
|----------|--------|
| `run_maintenance.sh` | Added Phase 2 (extract_metrics.py) and Phase 3 (observation_analysis.py) to sequence |
| `AM — LLM Conventions` | Added "Temporal Reasoning Conventions" section |
| `AM — Artifact Lifecycles` | Added observation analysis lifecycle (Section 8) and health report retention policy |
| `Self-Observation` concept | Rewritten to Loop-based model, updated relationships |
| `SYSTEM_MAP` | Updated with all Wave 9 artifacts |
| `AM — Roadmap` | Wave 9 marked complete with ✓ and outcome |

## What Was Learned

### The Architecture Is Reflexive

The most important validation from Wave 9: the Irreducible Loop genuinely works on itself. The design analysis sessions initially proposed novel architecture (five depth levels, a feedback triangle). The adversarial audit dissolved all of it back into existing patterns — Loop + escalation levels + Artifact Lifecycles. This is Seed 1 (fractal recursion) proven in practice: the same pattern at every level of abstraction, including when the subject is the pattern itself.

### Tool Conventions Have a Boundary

`extract_metrics.py` exposed the first case where the Tool Conventions don't fully apply. The tool is stateful (reads previous CSV) and writes to the vault content tree — both violations of the existing conventions. Rather than creating a new convention document for one tool (Law 3), the differences were acknowledged honestly. If this pattern recurs in future waves, it may warrant a convention extension.

### The CSV-as-Interface Pattern Works

The observation metrics CSV serves as a clean interface between Phase 1 (mechanical extraction) and Phase 2 (semantic analysis). Each side can evolve independently. Phase 1 can run for weeks before Phase 2 is built. Phase 2 can be replaced or upgraded without touching Phase 1. This is the same pattern as `orchestrate.sh` producing reports that `summarise_report.py` consumes — proven in Wave 7, reused here.

### Inventory Needs Attention

The Inventory tool's report format doesn't include the standard `| Checked | Passed | Failed | Warnings |` summary table — it produces a manifest instead. This means it's the one tool whose metrics can't be extracted by the standard parser. Not a problem now (the `enabled: false` flag handles it), but if Inventory's data becomes useful for trend analysis, either the tool's report format should be extended or `extract_metrics.py` should get a custom parser for it.

## Was the Wave's Question Answered?

**Question:** Can AM observe and measure its own operational behaviour?

**Answer:** Yes. At three levels:

- **Level 1 (mechanical):** `extract_metrics.py` silently accumulates temporal data with every maintenance run. No LLM required. The CSV grows, building the temporal memory.
- **Level 2 (semantic):** `observation_analysis.py` reads the history, identifies trends, and invokes the LLM for causal analysis when anomalies are detected.
- **Level 3 (governance):** Persistent process-category breaches are escalated as governance concerns for human review.

The Reflect-to-Perceive feedback closes the loop: each run checks whether previously flagged metrics have changed. The system doesn't just observe — it observes whether its observations led to improvement.

## Stage 1 Exit Proof

Wave 9 was positioned as the final Stage 1 wave. The Stage 1 exit criteria from the Roadmap:

- **The vault detects its own structural problems automatically** — Wave 6 (7 tools) + Wave 8.2 (5 tools) + Wave 8.3 (1 tool) = 13 detection tools.
- **A task can flow through all 6 pipeline stages with appropriate automation and gates** — Waves 5.2, 8.1, 8.2 established the pipeline with gates at every transition.
- **AM runs scheduled maintenance between human sessions** — Wave 7 delivered launchd scheduling.
- **Someone new (human or LLM) can pick up CLAUDE.md and operate effectively** — The Agent Bootloader sequence in CLAUDE.md, plus governance hierarchy, makes this possible.
- **SOPs document how the system works** — Tool Conventions, LLM Conventions, Artifact Lifecycles, Git Conventions, Universal Workflow.

Wave 9 adds: **AM observes its own operational trends and can identify improvement opportunities.** This is the reflexive capability that distinguishes self-governance from mere rule-following.

## Concept Promotion Check

**Did this wave surface any concepts strong enough for `02_KNOWLEDGE/concepts/`?**

No new concepts. The existing [[Self-Observation]] concept was updated to the Loop-based model — it was already in the vault but described an earlier, less precise understanding. The update reflects the design finding that self-observation is not a separate architecture but the existing architecture applied reflexively.

## What Comes Next

Wave 9 completes Stage 1. The Roadmap's Stage 2 (First External Application) is next — applying AM's methodology to a real external system. The immediate next steps:

1. **Let the observation data accumulate.** Phase 1 runs silently with every maintenance cycle. After 5+ runs, Phase 2 will start producing trend analyses. The longer the history, the more valuable the analysis.

2. **Wave 10 — Generalized Audit Protocol.** Per the Roadmap, the first Stage 2 wave extracts the self-audit capability into a protocol that works on any folder structure or vault. This is AM's first outward-facing capability.

3. **Archive completed proposals.** Waves 7, 8.2, 8.3, and 9 all have proposals in `active/` that should be archived as part of the finishing ritual.

## Related

- [[Proposal — Wave 9 Self-Observation]]
- [[Wave 9 — Self-Observation Brainstorm]]
- [[Wave 9 — Design Analysis v2]]
- [[AM — Roadmap]]
- [[Self-Observation]]
