---
title: "Proposal — Wave 9 Self-Observation"
type: proposal
status: active
approved: "2026-03-17"
authority_weight: 30
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
    - "[[AM — Tool Conventions]]"
    - "[[AM — LLM Conventions]]"
    - "[[AM — Integrity Layers]]"
    - "[[AM — Artifact Lifecycles]]"
  governs: []
  related:
    - "[[AM — Roadmap]]"
    - "[[AM — Future Waves Register]]"
    - "[[Wave 9 — Self-Observation Brainstorm]]"
    - "[[Wave 9 — Design Analysis v2]]"
    - "[[Self-Observation]]"
    - "[[Memory Architecture]]"
tags: [proposal, wave-9, self-observation, stage-1]
---

# Proposal — Wave 9 Self-Observation

## Problem Statement

AM can detect structural problems in its vault (Wave 6), enforce its own process (Wave 8.2), and verify its git conventions (Wave 8.3). All 13 detection tools produce findings at a point in time. Each health report is a snapshot — when the next run happens, the previous report is overwritten.

AM has no temporal memory of its own operation. It cannot answer:

- Are findings increasing or decreasing over time?
- Did the changes from Wave 8 actually reduce the problems Wave 6 identified?
- How long do waves take? Is velocity changing?
- Which tool categories produce the most persistent findings?

These are not structural questions (Wave 6), not process questions (Wave 8), and not git questions (Wave 8.3). They are **operational self-awareness questions** — questions about the system's behaviour across time. Answering them requires two things AM does not yet have: a temporal metric store and the ability to reason about trends.

**Wave 9's question:** Can AM observe and measure its own operational behaviour?

**What successful Wave 9 proves:** AM's architecture is reflexive — the Irreducible Loop can take the system itself as subject, using existing escalation levels to govern intensity, existing roles to separate observation from audit, and existing conventions to govern both mechanical extraction and semantic reasoning. This is the Stage 1 exit proof: if the pipeline works on itself as a whole system (not just on individual artifacts), the fractal principle says it transfers to other systems.

**Design lineage:** This proposal is grounded in the design analysis sessions documented in [[Wave 9 — Self-Observation Brainstorm]] and [[Wave 9 — Design Analysis v2]]. The key design finding: self-observation is not a new architecture. It is the Irreducible Loop applied reflexively — the same pattern used by [[AM — Artifact Lifecycles]], applied to a new subject (the system's own operation) with a new dimension (time). No new frameworks, depth levels, or observation models are needed. The existing architecture is sufficient.

## Proposed Change

### The Model

Self-observation is the Irreducible Loop executed with the system itself as subject:

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

This is the same escalation model used everywhere in AM. No new intensity framework is needed.

### Three Phases

The build is decomposed into three phases, each deployable independently (D3 — Controlled Evolution). Each phase adds one layer of the observation loop.

---

#### Phase 1: Perceive + Record (Mechanical Metric Extraction)

**Deliverables:**

**1. `extract_metrics.py`** — A data transformation tool in `04_EXECUTE/tools/vault-maintenance/`.

Reads each per-tool report produced by `orchestrate.sh` and extracts the standard metrics into CSV rows. This is not a detection tool — it does not check rules or produce findings. It transforms report data into a temporal format. It borrows several [[AM — Tool Conventions]] (config-driven, composable, meaningful exit codes, conservative, dual-audience output) but differs from detection tools in two ways: it is **stateful across runs** (reads the existing CSV to compute deltas — degrades gracefully on first run when no history exists) and it **writes to the vault content tree** (`05_RECORD/logs/`, not the tool's own output directory). These differences are inherent to its purpose — temporal data requires history, and temporal data belongs in the record layer. If this tool type recurs in future waves, it may warrant a convention extension. For now, this note acknowledges the boundary honestly.

**Input:** The 13 per-tool reports in `reports/` (read after `orchestrate.sh` completes).

**Output:** Rows appended to `observation_metrics.csv`.

**Extraction logic:** Each tool report contains a `| Checked | Passed | Failed | Warnings |` summary table. The tool parses this table and produces one row per metric per tool. For the aggregate health report, it additionally extracts the per-tool exit codes and overall result.

**CSV schema (13 fields, derived from Seed 2):**

```
timestamp,run_id,tool,metric_name,metric_value,previous_value,delta,direction,category,goal_trace,threshold,escalation_level,source_report
```

| Field(s) | Seed 2 Primitive | Source |
|----------|-----------------|--------|
| `timestamp` | Memory — when did this happen? | ISO 8601 UTC, generated at extraction time |
| `run_id` | Memory — which run does this belong to? | ISO 8601 date stamp (e.g., `2026-03-17`), matching the health report's date. Groups all rows from a single maintenance run. |
| `metric_name`, `metric_value` | State — what is true right now? | Parsed from tool report |
| `goal_trace` | Goal — what does this serve? | From metric registry |
| `threshold` | Policy — what expectation applies? | From metric registry |
| `previous_value`, `delta`, `direction` | Memory + Feedback — comparison to past | Computed from previous CSV row for same tool+metric |
| `tool`, `source_report` | Tools — what produced this? | From report header |
| `escalation_level` | Control — who acts on this? | Computed from threshold breach (see below) |
| `category` | *(Convenience — not a Seed 2 primitive)* | From metric registry. Grouping label for analysis (e.g., `structural`, `process`, `git`). Useful for filtering; not architecturally required. |

**How `previous_value`, `delta`, and `direction` are computed:** The tool reads the existing CSV, finds the most recent row matching the same `tool` + `metric_name`, and computes the delta. `direction` is determined by the metric registry's polarity: if a metric is `lower_is_better` (e.g., `failed` count) and the delta is negative, `direction` = `improving`. If the CSV has no previous row for this metric (first run), `previous_value`, `delta`, and `direction` are empty.

**How `escalation_level` is computed:** Threshold-only, two cases: if the metric value breaches the threshold (respecting polarity — above threshold for `lower_is_better`, below for `higher_is_better`), the escalation level is the registry's `default_escalation`. Otherwise, Level 1. Direction (`improving`, `degrading`, `stable`) is recorded as metadata for Phase 2's LLM to reason about — it does not affect the mechanical escalation. This keeps the mechanical/semantic boundary clean: Phase 1 decides "threshold crossed or not" (deterministic); Phase 2 decides "what does the trend mean?" (judgment).

**2. `metric_registry.csv`** — Configuration file defining each metric.

**Location:** `04_EXECUTE/tools/vault-maintenance/config/`

**Schema:**

```
tool,metric_name,enabled,polarity,threshold,default_escalation,category,goal_trace
```

| Field | Purpose | Example |
|-------|---------|---------|
| `tool` | Which detection tool | `Broken Links` |
| `metric_name` | Which metric | `failed` |
| `enabled` | Whether to extract this metric | `true` |
| `polarity` | Direction of health | `lower_is_better` |
| `threshold` | Value above/below which this metric is concerning | `0` |
| `default_escalation` | Escalation level when threshold is breached | `2` |
| `category` | Grouping for analysis | `structural` |
| `goal_trace` | Which governance concern this serves | `Seed 2 — Integrity` |

**Initial metrics (extracted from actual health report output):**

For each of the 13 detection tools, four standard metrics: `checked`, `passed`, `failed`, `warnings`. That's 52 metric definitions. Plus aggregate metrics from the health report: `tools_clean`, `tools_findings`, `tools_error`, `overall_result`. Total: ~56 initial metric definitions. Not all will carry useful signal — some (`Inventory.checked`, `Inventory.failed`) are vault-size proxies or constants, not operational health indicators. The initial set is deliberately broad; metrics that prove uninformative after Phase 1 data accumulates can be disabled via the registry's `enabled` flag without removing their definitions.

The registry is a CSV file, not hardcoded. New metrics are added by adding rows, not by modifying code. Convention 2 (Config-Driven).

**3. `observation_metrics.csv`** — The temporal metric store.

**Location:** `05_RECORD/logs/` (operational data, not a report).

**Retention:** Keep everything. At ~56 rows per run, daily runs produce ~20,000 rows/year. Negligible storage cost, irreplaceable source data. Law 2 (reversible) favours retention. Governed by D2 (Three-Layer Memory Model, Layer 2 — Structured Data).

**4. Integration with `run_maintenance.sh`** — Coordination layer.

`run_maintenance.sh` (Wave 7) evolves to sequence:

```
1. orchestrate.sh          → tool reports + health report    (detection)
2. extract_metrics.py      → observation_metrics.csv          (observation)
3. summarise_report.py     → LLM summary + notification       (existing)
```

`extract_metrics.py` runs after `orchestrate.sh` and before `summarise_report.py`. It consumes the tool reports that `orchestrate.sh` produces. This is a coordination change, not an architectural change — `run_maintenance.sh` already sequences `orchestrate.sh` and `summarise_report.py`.

**Phase 1 is self-contained.** After Phase 1, AM accumulates metric history with every maintenance run. No LLM reasoning is required. The CSV grows silently, building the temporal memory that Phase 2 will consume. Phase 1 can run indefinitely before Phase 2 is built — and the longer it runs, the more history Phase 2 has to work with.

---

#### Phase 2: Interpret + Decide (Semantic Trend Analysis)

**Deliverables:**

**1. `observation_analysis.py`** — A semantic analysis script in `04_EXECUTE/runtime/` (alongside `summarise_report.py`, following the Wave 7 precedent: LLM-invoking scripts live in `runtime/`, not in the `tools/` directory, keeping the tool directory pure-mechanical).

**Input:** `observation_metrics.csv` (the full history or a configured window).

**Output:** An observation analysis report in `05_RECORD/reports/`.

**What it does:** Reads the metric CSV, identifies trends (improving, degrading, stable, anomalous), and invokes the LLM to interpret them. The LLM operates at the escalation level determined by the data:

- **Level 1 (no anomalies):** Brief summary — "all metrics stable, no action needed." Mechanical template, no deep reasoning.
- **Level 2 (anomalies or trends detected):** Causal analysis — why is this happening? What does it mean? Formulate a recommendation (not a proposal — a recommendation is a draft that requires Reviewer audit before it becomes a proposal). The LLM follows [[AM — LLM Conventions]]: ground in mechanical output, express uncertainty, trace to Foundations.
- **Level 3 (governance-level concern):** Full analysis with proposal draft for human review. Escalate explicitly.

**Minimum history threshold:** The tool requires a configurable minimum number of data points (e.g., 5 runs) before attempting trend analysis. Below that threshold, it reports "insufficient history" and exits cleanly. This prevents false pattern detection on sparse data.

**D6 application:** The observation analysis runs in Worker mode. If it produces a Level 2 recommendation, a separate Reviewer pass audits the recommendation before it can become a proposal. Same model may play both roles, but not in the same invocation (Safety Rule 1).

**2. LLM Conventions extension** — Small additions to [[AM — LLM Conventions]].

Three paragraphs added to a new section "Temporal Reasoning Conventions":

- **Minimum history:** Do not draw conclusions from fewer than N data points (configurable). State the sample size when reporting trends.
- **Trend ambiguity:** When a trend could be explained by multiple causes, present all plausible explanations rather than committing to one. Express confidence qualitatively (e.g., "likely," "possibly," "insufficient evidence").
- **Signal vs noise:** Short-term fluctuations in small-count metrics (e.g., `failed` going from 0 to 1 back to 0) are noise, not trends. Require sustained directional change across multiple runs before calling it a trend.

These are conventions, not new architecture. They extend the existing document within its current scope.

**3. Integration with `run_maintenance.sh`:**

```
1. orchestrate.sh          → tool reports + health report    (detection)
2. extract_metrics.py      → observation_metrics.csv          (observation)
3. observation_analysis.py → observation report                (interpretation)
4. summarise_report.py     → LLM summary + notification       (existing, now also summarises observation report)
```

**Phase 2 depends on Phase 1.** It consumes the CSV that Phase 1 produces. It also depends on sufficient history — the earliest useful run of Phase 2 happens after Phase 1 has accumulated enough data points.

---

#### Phase 3: Close-Out + Reflect Integration

**Deliverables:**

**1. Observation analysis report lifecycle** — Addition to [[AM — Artifact Lifecycles]].

Observation analyses are a new report type. They follow the Report lifecycle (Generated → Current → Superseded → Archived) but with an additional property: Level 2+ analyses that contain recommendations are **archivable** (they contain unique analysis), not ephemeral. This ensures that the system's self-assessment history is preserved, enabling future cycles to check whether past recommendations achieved their purpose.

**2. Health report retention policy** — Addition to [[AM — Artifact Lifecycles]].

- **Raw metrics (observation CSV):** Keep everything. Append-only. Never delete.
- **Per-tool reports:** Ephemeral — overwritten each run (already the case).
- **Health reports (aggregate):** Active window of configurable duration (default 90 days) in `05_RECORD/reports/`, then archived to `05_RECORD/archive/`. Date-stamped filenames (already the case in `05_RECORD/reports/`).
- **Observation analyses:** Standard Record lifecycle. Archivable when superseded.

**3. Self-Observation concept update** — Update [[Self-Observation]] in `02_KNOWLEDGE/concepts/` to reflect the Loop-based model. Self-observation is the Irreducible Loop applied reflexively, not a separate architecture. The concept note currently describes a progression (Manual → Scheduled → Proposing → Self-improving) which is valid as a capability maturity description but should be grounded in the Loop model.

**4. Reflect-to-Perceive feedback.** The observation analysis from one cycle feeds the next cycle's attention. Concretely: the analysis report records which metrics were flagged and what was recommended. The next run's `extract_metrics.py` reads the previous analysis (if one exists) and logs whether flagged metrics improved, degraded, or remained stable. This closes the loop — Reflect feeds Perceive.

**Note:** This deliverable extends `extract_metrics.py`'s scope — in Phase 1, it reads only tool reports; in Phase 3, it also reads observation analysis reports. This creates a coupling between the Phase 1 tool and Phase 2's output format. The coupling is narrow (one additional input, optional — degrades gracefully if no analysis exists), but it means Phase 3 modifies a Phase 1 artifact.

**Phase 3 depends on Phase 2.** The Reflect stage evaluates whether Phase 2's interpretations and recommendations achieved their purpose.

---

### Modifications to Existing Artifacts

| Artifact | Change | Phase |
|----------|--------|-------|
| `run_maintenance.sh` | Add `extract_metrics.py` to sequence | 1 |
| `run_maintenance.sh` | Add `observation_analysis.py` to sequence | 2 |
| [[AM — LLM Conventions]] | Add "Temporal Reasoning Conventions" section | 2 |
| [[AM — Artifact Lifecycles]] | Add observation analysis lifecycle + health report retention policy | 3 |
| [[Self-Observation]] (concept) | Update to Loop-based model | 3 |
| [[SYSTEM_MAP]] | New Wave 9 artifacts | 3 |
| [[AM — Roadmap]] | Mark Wave 9 complete with outcome | 3 |

### New Artifacts

| Artifact | Location | Phase |
|----------|----------|-------|
| `extract_metrics.py` | `04_EXECUTE/tools/vault-maintenance/` | 1 |
| `metric_registry.csv` | `04_EXECUTE/tools/vault-maintenance/config/` | 1 |
| `observation_metrics.csv` | `05_RECORD/logs/` | 1 (created on first run) |
| `observation_analysis.py` | `04_EXECUTE/runtime/` | 2 |

### What Is NOT in Scope

| Item | Why deferred | Revisit when |
|------|-------------|--------------|
| Self-description test ("ask the system what it is") | Specific use case of observation loop, not foundational infrastructure. Can be built as a standalone tool using the same pattern once the observation infrastructure exists. | After Wave 9, as a Wave 10 candidate or register entry |
| Automated proposal creation | The observation loop produces recommendations and escalations, not approved proposals. Automated proposal creation crosses the D4 boundary (human sovereignty). | Stage 2+, when autonomous proposal is governed |
| Vector memory / embeddings | D2 lists Vector Memory as a layer, but it's not required for trend analysis on structured CSV data. Premature optimisation. | When semantic search across observations becomes necessary |
| Dashboard / visualisation | A human-facing dashboard would consume `observation_metrics.csv`. Useful but not foundational. The CSV is the interface. | After the loop proves value |
| Predictive modelling | The brainstorm identified "self-prediction" as a depth level. This dissolves into Level 2 Interpret at high intensity — the LLM can project from trends. No special predictive tooling is needed at this stage. | If pattern complexity exceeds LLM reasoning capability |

## Scope Degradation Plan

**Minimum viable Wave 9** (Phase 1 only — mechanical metric extraction):
- `extract_metrics.py`, `metric_registry.csv`, `observation_metrics.csv`, `run_maintenance.sh` integration. AM accumulates temporal data. No LLM reasoning yet. This alone answers the wave's question at Level 1: "Can AM observe its own operational behaviour?" Yes — it can record it. Interpretation is manual (human reads the CSV).

**Standard Wave 9** (Phases 1 + 2 — extraction + trend analysis):
- Adds `observation_analysis.py` and LLM Conventions extension. AM can now observe AND interpret. The full observation loop runs at Level 1 and Level 2. This is the target scope.

**Full Wave 9** (all three phases):
- Adds governance extensions, concept updates, Reflect-to-Perceive feedback, and the full lifecycle integration. The loop closes completely. This is the stretch goal.

## Traceability

| Decision | Foundation |
|----------|-----------|
| Self-observation as reflexive Loop | Seed 1 (Process) + Fractal Design — same pattern, new subject |
| Intensity governed by escalation levels | Seed 3 (Constraint) — existing escalation model applies unchanged |
| CSV schema derived from Seed 2 | Each field traces to a Seed 2 primitive (see Phase 1 schema table) |
| Metric registry as separate config | Convention 2 (Config-Driven) + Law 3 (Economy) — metric definitions separate from metric data |
| Observation CSV as append-only temporal store | D2 (Three-Layer Memory Model, Layer 2 — Structured Data) + Law 2 (reversible — keep source data) |
| `extract_metrics.py` borrows from Tool Conventions | [[AM — Tool Conventions]] — config-driven, composable, meaningful exit codes, conservative. Differs: stateful across runs (reads previous CSV), writes to vault content tree. See Phase 1 description. |
| `observation_analysis.py` follows LLM Conventions | [[AM — LLM Conventions]] — ground in mechanical output, express uncertainty, trace to Foundations. Lives in `runtime/` (Wave 7 precedent). |
| Worker observes, Reviewer audits | D6 (Separation of Powers) — Level 2+ recommendations audited before becoming proposals |
| Phase decomposition | D3 (Controlled Evolution) — each phase is independently deployable and valuable |
| No new observation framework | Law 3 (Economy) + Fractal Design — existing architecture handles the reflexive case |

## Impact Assessment

**What this affects:**
- `04_EXECUTE/tools/vault-maintenance/` — receives `extract_metrics.py`
- `04_EXECUTE/runtime/` — receives `observation_analysis.py` (LLM-invoking, alongside `summarise_report.py`)
- `04_EXECUTE/tools/vault-maintenance/config/` — receives `metric_registry.csv`
- `05_RECORD/logs/` — receives `observation_metrics.csv`
- `05_RECORD/reports/` — receives observation analysis reports
- `run_maintenance.sh` — extended with two new sequence entries
- [[AM — LLM Conventions]] — receives "Temporal Reasoning Conventions" section (Phase 2)
- [[AM — Artifact Lifecycles]] — receives observation analysis lifecycle + retention policy (Phase 3)
- [[Self-Observation]] (concept) — updated to Loop-based model (Phase 3)
- [[SYSTEM_MAP]] — updated with new artifacts (Phase 3)

**What this does NOT affect:**
- `orchestrate.sh` — unchanged. Observation consumes its output, does not modify it.
- Existing Wave 6 tools — unchanged.
- Existing Wave 8.2/8.3 tools — unchanged.
- `vault_model.py` — unchanged. `extract_metrics.py` parses reports directly, does not need the model library.
- Governance documents (Foundations, Vault Rules, Strategy, North Star) — unchanged.
- Wave 7 runtime (launchd scheduling, `notify.sh`) — unchanged; the coordination layer picks up new tools automatically.
- Vault structure — no new folders.

**What could go wrong:**

- **Report format changes.** `extract_metrics.py` parses the markdown reports produced by detection tools. If a tool changes its report format, extraction breaks. Mitigation: the report format (header + summary table + findings) is consistent across all 13 tools and established since Wave 6. The parser should handle minor variations gracefully and report extraction failures per-tool rather than failing entirely (same best-effort pattern as `git_hygiene.py`).

- **CSV corruption or encoding issues.** An interrupted write to `observation_metrics.csv` could produce a malformed row. Mitigation: write to a temp file and rename atomically. Validate CSV structure on read.

- **LLM trend analysis quality.** The Phase 2 LLM analysis may produce low-quality or hallucinated interpretations, especially early when history is sparse. Mitigation: minimum history threshold, temporal reasoning conventions in LLM Conventions, and D6 (Reviewer audits Worker output).

- **Metric registry maintenance burden.** 56 initial metrics is manageable but non-trivial. If new detection tools are added in future waves, the registry must be extended. Mitigation: the registry is a simple CSV — adding a row is trivial. The metric selection principles (goal-traceable, action-informing, trend-meaningful, mechanically-collectible) provide criteria for what to include.

- **First-run findings volume.** The first observation analysis (Phase 2) will reason about whatever trends exist in the CSV at that point. If Phase 1 has only run a few times, the analysis will be thin. This is expected — the minimum history threshold prevents false conclusions, and the analysis quality improves as history accumulates.

## Alternatives Considered

**Alternative 1: Extend `orchestrate.sh` to include metric extraction.**
Rejected. `orchestrate.sh` coordinates detection tools — it runs them and aggregates their reports. Metric extraction is a different concern: it reads the reports and transforms them into temporal data. Mixing the two violates the concern boundary. The coordination layer (`run_maintenance.sh`) is the right place to sequence them — same pattern as `orchestrate.sh` coordinating independent tools.

**Alternative 2: Store observations in a database (SQLite) instead of CSV.**
Rejected for Phase 1. CSV is simpler, git-friendly, human-readable, and consistent with the existing `session_index.csv` pattern. At ~20,000 rows/year, CSV performance is not a concern. If query complexity eventually requires a database, the CSV can be migrated — it's structured data. Law 3 (Economy): start simple, upgrade only if needed.

**Alternative 3: Build all three phases as a single wave.**
Rejected. Phase decomposition enables incremental deployment (D3). Phase 1 provides immediate value (temporal data accumulation) and can run for weeks before Phase 2 is built. This also reduces the risk of building LLM analysis tooling (Phase 2) before understanding what the data looks like in practice.

**Alternative 4: Introduce a new "observation framework" with depth levels and feedback triangles.**
Rejected through the design analysis process (see [[Wave 9 — Design Analysis v2]]). The v1 design analysis proposed five depth levels and a feedback triangle. Adversarial audit found the depth levels were not fractal — they did not map to the Irreducible Loop. The v2 reframe dissolved all novel architecture back into existing patterns (Loop + escalation levels + Artifact Lifecycles parallel). Law 3 + Fractal Design: don't create what already exists.

## Gate Criteria

**This proposal is ready to execute when:**

- [ ] Proposal drafted with all required elements
- [ ] Adversarial audit completed (alignment, integrity, viability)
- [ ] Human (Rob) approves the proposal

**Phase 1 is complete when:**

- [ ] `extract_metrics.py` parses all 13 tool reports and produces correct CSV output
- [ ] The tool follows applicable [[AM — Tool Conventions]]: config-driven, composable, exit codes 0/1/2, conservative, dual-audience output
- [ ] `metric_registry.csv` defines all initial metrics with polarity, threshold, escalation, category, and goal trace
- [ ] `observation_metrics.csv` is created on first run and appended on subsequent runs
- [ ] `previous_value`, `delta`, and `direction` are correctly computed from CSV history + registry polarity
- [ ] `run_maintenance.sh` sequences `extract_metrics.py` after `orchestrate.sh`
- [ ] Tool tested against the actual repository — metrics match what the health reports show
- [ ] CSV handles edge cases: first run (no previous data), missing reports, malformed report tables

**Phase 2 is complete when:**

- [ ] `observation_analysis.py` reads `observation_metrics.csv` and produces an observation analysis report
- [ ] The tool respects the minimum history threshold — does not analyse sparse data
- [ ] Level 1 analysis produces a brief mechanical summary
- [ ] Level 2 analysis produces causal reasoning grounded in data, following LLM Conventions
- [ ] [[AM — LLM Conventions]] extended with Temporal Reasoning Conventions section
- [ ] `run_maintenance.sh` sequences `observation_analysis.py` after `extract_metrics.py`
- [ ] D6 verified: observation run (Worker) and recommendation audit (Reviewer) are separate invocations

**Phase 3 is complete when:**

- [ ] [[AM — Artifact Lifecycles]] extended with observation analysis lifecycle and health report retention policy
- [ ] [[Self-Observation]] concept updated to Loop-based model
- [ ] Reflect-to-Perceive feedback implemented: next run checks whether previous recommendations were addressed
- [ ] [[SYSTEM_MAP]] updated
- [ ] [[AM — Roadmap]] updated — Wave 9 marked complete with outcome
- [ ] Wave 9 reflection written and filed in `06_REFLECT/`
- [ ] Capture seed for next work created in `01_CAPTURE/`

**Wave 9 is complete when:**

- [ ] At minimum, Phase 1 is complete (minimum viable Wave 9)
- [ ] Target: Phases 1 + 2 complete (standard Wave 9)
- [ ] Stretch: All three phases complete (full Wave 9)

## Proposal Type

[x] Structural — Level 2 (Reviewer gate required)

This proposal creates new executable artifacts in `04_EXECUTE/tools/vault-maintenance/` and makes small extensions to two governance documents ([[AM — LLM Conventions]] and [[AM — Artifact Lifecycles]]). The governance extensions are additions to existing documents within their current scope, not new governance architecture. The Foundations, Vault Rules, Strategy, and North Star are unchanged.

## Audit

**Auditor context:** This audit is performed by the same agent that drafted the proposal, in the same session. This violates the spirit of D6 (Separation of Powers). The adversarial lens is applied with extra rigour to compensate, but the finding should be noted: a second-session review by a fresh agent would provide stronger separation. The human's review at approval time is the definitive gate.

### Alignment

**Question:** Does this proposal serve what's above it?

**Finding AL-1: `extract_metrics.py` does not fit the Tool Conventions model.** The proposal claims the tool "follows [[AM — Tool Conventions]]: stateless, config-driven, read-check-report, meaningful exit codes." But Tool Convention 1 states: "Each invocation is self-contained — a tool does not remember previous runs, does not maintain internal state between executions, and does not depend on having been run before."

`extract_metrics.py` reads the existing `observation_metrics.csv` to compute `previous_value`, `delta`, and `direction`. It depends on its own previous output. It degrades gracefully on first run (fields are empty), so it does not *require* previous state — but it *consumes* it when available, which makes it stateful across runs in a way no existing detection tool is.

Additionally, Tool Convention 3 says tools may only write "report files" and "log files." Safety Rule 2 says "Reports and logs are the only write outputs, and they are written to the tool's own output directory, not into the vault content tree." The observation CSV lives in `05_RECORD/logs/` — inside the vault content tree, not in the tool's output directory. And the CSV is not a report or a log in the Convention sense — it's a persistent temporal data store that grows across runs.

This is not an argument that `extract_metrics.py` is wrong. It's an argument that the proposal mischaracterises its relationship to Tool Conventions. The tool is a **data transformation tool** that reads reports and produces structured temporal data. This is a new category that the existing Tool Conventions don't cover. The proposal should either: (a) acknowledge that `extract_metrics.py` is a new tool type that borrows *some* conventions (config-driven, meaningful exit codes, conservative) but not others (stateless, report-only output), or (b) propose an extension to Tool Conventions that accommodates data transformation tools.

**Severity: Medium.** The tool design is sound. The problem is that claiming full Tool Conventions compliance when the tool doesn't fully comply erodes trust in the traceability claims. Better to be honest about the boundary being stretched.

**Finding AL-2: `observation_analysis.py` performs semantic interpretation inside the tools directory.** Tool Conventions Safety Rule 1 states: "No semantic interpretation. Tools must never reason about meaning." Yet `observation_analysis.py` invokes an LLM to perform causal analysis and formulate recommendations. The proposal places it in `04_EXECUTE/tools/vault-maintenance/` alongside the detection tools.

There is precedent: `summarise_report.py` (Wave 7) also invokes an LLM and lives in `04_EXECUTE/runtime/` — not in the tools directory. The Wave 7 architecture placed the LLM summariser in `runtime/` specifically because it is *not* a detection tool. The proposal should follow this precedent: `observation_analysis.py` belongs in `04_EXECUTE/runtime/`, not in `04_EXECUTE/tools/vault-maintenance/`.

**Severity: Low.** File location choice, not architectural. But the precedent exists for a reason — keeping the tool directory pure-mechanical makes the trust boundary clean.

**Overall alignment: CONDITIONAL PASS.** The proposal faithfully serves its stated purpose and traces to the Foundations correctly. The core model (reflexive Loop, escalation-governed intensity) is genuinely derived from existing architecture. The two findings are about accuracy of claims rather than alignment failures. AL-1 requires resolution — the Tool Conventions relationship must be honestly characterised.

---

### Integrity

**Question:** Is this internally sound?

**Finding IN-1: `run_id` is in the CSV schema but never defined.** The 13-field schema includes `run_id` as the second field. The field description table maps it to no Seed 2 primitive. The computation explanations don't mention what generates it. Is it a timestamp? A UUID? An incrementing counter? A hash? This is the only schema field with no specification.

**Severity: Low.** Implementation detail, but the schema is presented as a design artifact — all other fields are fully specified.

**Finding IN-2: The `category` field breaks the Seed 2 derivation pattern.** The schema is presented as "derived from Seed 2" with a table mapping every field to a primitive. The `category` field is mapped to "(Classification)" — not a Seed 2 primitive. If the schema's claimed design basis is that every field traces to Seed 2, `category` is the exception. Either it traces (to which primitive?) or it's a convenience field that should be acknowledged as such.

**Severity: Low.** The schema is sound regardless. The claim is slightly overstated.

**Finding IN-3: The escalation level computation has gaps.** The proposal says: "If the metric value exceeds the threshold, the escalation level from the registry applies. If within threshold and direction is stable or improving, Level 1." This covers two cases but not all four:

| Value vs threshold | Direction | Proposed level | Specified? |
|---|---|---|---|
| Within threshold | Stable/improving | Level 1 | ✓ |
| Exceeds threshold | Any | Registry default | ✓ |
| Within threshold | Degrading | ? | ✗ |
| Exceeds threshold but improving | ? | ✗ |

The third case is important: a metric that's within threshold but trending in the wrong direction is a leading indicator. The fourth case matters too: a metric that still exceeds threshold but is improving may not need the same urgency as one that's worsening. The proposal should specify all four cases or note that the logic will be refined during implementation.

**Severity: Medium.** The escalation computation is a core mechanical decision that determines what triggers LLM reasoning in Phase 2. Under-specification here propagates to ambiguity in Phase 2's behaviour.

**Finding IN-4: Phase 3 creates an unacknowledged coupling between phases.** Phase 3 Deliverable 4 (Reflect-to-Perceive feedback) says: "The next run's `extract_metrics.py` reads the previous analysis (if one exists) and logs whether flagged metrics improved." This means the Phase 1 tool must understand the output format of the Phase 2 tool. In Phase 1, `extract_metrics.py` reads tool reports only. In Phase 3, it also reads observation analysis reports. This expands the tool's scope and creates a dependency from Phase 1's tool on Phase 2's output format — a coupling that cuts across the phase decomposition.

**Severity: Low.** The coupling is narrow (reading one additional input) and Phase 3 is a stretch goal. But it should be acknowledged as a scope extension to `extract_metrics.py`, not presented as a simple addition.

**Finding IN-5: Not all 56 initial metrics pass the metric selection principles.** The proposal defines four metric selection principles: goal-traceable, action-informing, trend-meaningful, mechanically-collectible. It then proposes 52 metrics (4 per tool × 13 tools) plus 4 aggregate metrics. But some of these don't pass Principle 3 (trend-meaningful):

- `Inventory.checked` = total files in vault. This increases monotonically as the vault grows. The trajectory tells you the vault is growing, which is not an operational health signal.
- `Inventory.failed` = always 0 (the Inventory tool doesn't fail files, it counts them). A metric that never changes has no meaningful trend.
- Several tools' `checked` counts are functions of vault size, not operational health.

The proposal should acknowledge that the initial 56 is a starting set that may be pruned after Phase 1 reveals which metrics carry useful signal. Alternatively, the metric registry could include an `enabled` flag so metrics can be silenced without removing their definitions.

**Severity: Low.** The proposal already describes the registry as the configuration layer, so pruning is mechanically easy. But the claim of "56 initial metrics" should be qualified: "56 initial metric definitions, to be refined based on observed signal."

**Overall integrity: CONDITIONAL PASS.** The proposal is internally coherent in its major architecture. The findings are about specification gaps (IN-1, IN-3), slightly overstated claims (IN-2, IN-5), and a minor coupling issue (IN-4). IN-3 is the most substantive — the escalation computation needs all cases specified before implementation.

---

### Viability

**Question:** Is every component earning its place?

**Finding VI-1: Phase 3 is more of a finishing ritual than a capability phase.** Phases 1 and 2 deliver new tools and capabilities. Phase 3 delivers: governance doc extensions, concept update, Reflect-to-Perceive feedback, SYSTEM_MAP update, roadmap update, reflection, capture seed. Of these, only the Reflect-to-Perceive feedback is genuinely new functionality. The rest are standard finishing ritual items from [[AM — Artifact Lifecycles]] that would be done at the end of any wave.

Calling it a "phase" alongside the other two overweights its substance and may create the impression that Wave 9 requires three substantial builds. The scope degradation plan correctly positions it as a "stretch goal," but the framing within the proposal's body is misleading.

**Severity: Low.** Consider renaming to "Phase 3: Close-Out + Reflect Integration" to distinguish it from the capability-building phases, or folding the finishing ritual items into "Wave 9 is complete when" and making Phase 3 solely about the Reflect-to-Perceive feedback.

**Finding VI-2: D6 process note.** As stated above, this audit was performed by the drafting agent in the same session. The human's review at approval time provides the definitive gate.

**Overall viability: PASS.** Every major component earns its place. The phase decomposition is sound. The scope degradation plan is well-ordered. The "not in scope" decisions are all justified and correctly deferred.

---

### Summary of Findings

| ID | Finding | Severity | Resolution |
|----|---------|----------|------------|
| AL-1 | `extract_metrics.py` doesn't fit Tool Conventions model (stateful, writes to vault content tree) | Medium | **RESOLVED.** Tool recharacterised as "data transformation tool" that borrows applicable conventions. Differences acknowledged honestly in Phase 1 description and Traceability table. No new convention document — Law 3 applies; if the pattern recurs, then formalise. |
| AL-2 | `observation_analysis.py` performs semantic work — belongs in `runtime/` not `tools/` | Low | **RESOLVED.** Moved to `04_EXECUTE/runtime/` following Wave 7 precedent. New Artifacts table and Impact Assessment updated. |
| IN-1 | `run_id` field in CSV schema is never defined | Low | **RESOLVED.** Defined as ISO 8601 date stamp matching the health report's date, grouping all rows from a single maintenance run. Added to schema table. |
| IN-2 | `category` field breaks the Seed 2 derivation claim | Low | **RESOLVED.** Acknowledged as convenience field, not a Seed 2 primitive. Schema table updated. |
| IN-3 | Escalation level computation has unspecified cases | Medium | **RESOLVED.** Simplified to threshold-only: breach → registry default; no breach → Level 1. Direction is recorded as metadata for Phase 2's LLM, not an escalation trigger. Keeps the mechanical/semantic boundary clean. |
| IN-4 | Phase 3 creates coupling between `extract_metrics.py` and Phase 2 output | Low | **RESOLVED.** Coupling acknowledged in Phase 3 Deliverable 4 with explicit note about scope extension. |
| IN-5 | Not all 56 initial metrics pass metric selection principles | Low | **RESOLVED.** Metric count qualified as "initial definitions, to be refined." `enabled` flag added to registry schema for silencing uninformative metrics. |
| VI-1 | Phase 3 is a finishing ritual, not a capability phase — framing is misleading | Low | **RESOLVED.** Renamed to "Phase 3: Close-Out + Reflect Integration." |
| VI-2 | D6 process — same-session audit | Noted | Human review is the definitive gate. |

### Audit Verdict

**Post-resolution verdict: PASS.** All nine findings have been addressed. The two medium-severity findings (AL-1 and IN-3) are resolved: the Tool Conventions relationship is now honestly characterised, and the escalation computation is simplified to a clean threshold-only rule with direction as metadata.

The proposal is ready for human approval.
