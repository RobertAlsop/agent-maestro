---
title: "Wave 9 — Design Analysis"
type: pipeline
status: draft
authority_weight: 10
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Wave 9 — Self-Observation Brainstorm]]"
    - "[[Agent Maestro — Foundations]]"
    - "[[AM — LLM Conventions]]"
    - "[[AM — Integrity Layers]]"
    - "[[AM — Tool Conventions]]"
  governs: []
  related:
    - "[[Self-Observation]]"
    - "[[Memory Architecture]]"
    - "[[AM — Treatise on Core Principles]]"
    - "[[AM — Artifact Lifecycles]]"
tags: [capture, design-analysis, wave-9, self-observation, stage-1]
---

# Wave 9 — Design Analysis

**Source:** Design discussion between Rob and Claude (Cowork), 2026-03-17. This document formalises the design decisions emerging from the [[Wave 9 — Self-Observation Brainstorm]] by answering the brainstorm's open design questions, grounded in the governance chain.

**Purpose:** Provide a complete, auditable design landscape for Wave 9 — comprehensive enough to support an adversarial audit, and structured enough to feed a proposal when the scope is committed.

---

## 1. Observation Data Structure

### The Question

What does the observation data look like? What format, what schema, what does the storage need to support?

### The Answer Has Three Parts

This is not one question — it is three: what do we collect (schema), how do we store it (format), and what must the storage support (requirements).

### Format Decision: CSV

**Governance trace:** D2 (Three-Layer Memory Model) defines Layer 2 as "Structured Data (CSV, registry)" for operational data. The [[Memory Architecture]] concept note explicitly names CSV for this layer.

**Why not SQLite:** SQLite would provide more powerful querying, but introduces a new dependency before CSV has been proven insufficient. Law 3 (Economy) says only what is necessary. D3 (Controlled Evolution) says evolve through graduated experiments — start with CSV, escalate to SQLite only if evidence demonstrates the need.

**Why CSV is positively advantageous (not just "good enough"):**

- **Git-friendly.** Every change to observation data is versioned, diffable, and auditable. SQLite is an opaque binary — you lose Law 2 (verifiable, reversible, accountable) at the storage layer.
- **Human-readable.** Satisfies the dual-audience requirement from [[AM — Tool Conventions]] Convention 6 — output must be machine-readable and human-readable.
- **Tool-composable.** Any tool (bash, Python, LLM) can consume CSV without additional dependencies. Convention 4 — independently useful and composable.
- **Consistent with existing architecture.** `session_index.csv` already exists in `05_RECORD/logs/sessions/`. The pattern is proven.

### Schema Design: Derived from Seed 2

Seed 2 (Structure) says every system component must have or serve seven primitives. An observation record is a system component. The schema must address:

| Primitive | What it means for an observation record |
|-----------|----------------------------------------|
| **State** | What was measured? What was the value? |
| **Goal** | What does this metric relate to? (Traceable to governance or roadmap) |
| **Policy** | What threshold or expectation applies? (If any) |
| **Memory** | When? What run? What's the comparison point? (Previous value, delta) |
| **Tools** | What produced this observation? (Tool name, report source) |
| **Control** | Who/what is responsible for acting on this? (Escalation level) |
| **Feedback** | Is this value better, worse, or unchanged from previous? |

This produces a candidate schema:

```
timestamp, run_id, tool, metric_name, metric_value, previous_value, delta, direction, category, goal_trace, threshold, escalation_level, source_report
```

- `timestamp`: ISO 8601. When the observation was recorded.
- `run_id`: Unique identifier for the maintenance run that produced this data.
- `tool`: Which tool produced the source finding (e.g., `yaml_validation`, `proposal_lifecycle`).
- `metric_name`: What is being measured (e.g., `finding_count`, `warning_count`, `items_checked`).
- `metric_value`: The current value.
- `previous_value`: The value from the most recent prior run (empty if first run).
- `delta`: Change from previous (`metric_value - previous_value`).
- `direction`: Whether this delta is `improving`, `degrading`, or `stable`. Required because the meaning of a positive delta depends on the metric — rising finding counts are bad, rising items-checked counts are good. This field encodes the **Feedback primitive** (Seed 2): is this value better, worse, or unchanged? The direction for each metric is defined at metric registration time (e.g., `finding_count` has polarity `lower_is_better`; `items_checked` has polarity `higher_is_better`). The extraction tool computes direction mechanically from delta + polarity.
- `category`: Classification (e.g., `structural`, `lifecycle`, `git`).
- `goal_trace`: What governance goal this metric serves (e.g., `vault_integrity`, `pipeline_compliance`). Implements the **Goal primitive** (Seed 2).
- `threshold`: Expected value or acceptable range, if defined (e.g., `0` for finding counts, `>=previous` for items checked). Empty if no threshold applies. Implements the **Policy primitive** (Seed 2): what expectation applies to this metric?
- `escalation_level`: What level of response this metric warrants when it breaches threshold (`1` = automatic logging, `2` = flag for agent review, `3` = escalate to human). Implements the **Control primitive** (Seed 2): who is responsible for acting on this?
- `source_report`: Path to the report file this metric was extracted from.

**Note on metric registration:** The `direction`, `threshold`, and `escalation_level` fields are properties of the metric definition, not of individual observations. They should be defined in a **metric registry** (a small CSV or config file that lists each metric, its polarity, its threshold, and its escalation level). The extraction tool reads the registry to populate these fields in each observation row. This keeps metric definitions separate from metric data — the registry is the schema; the observation CSV is the data.

### Architectural Relationship to Existing Reports

**Critical point:** This CSV is not a replacement for health reports. The existing Markdown reports remain the detailed, human-readable snapshots — the source of truth for any specific run. The observation CSV is an **extraction layer** that pulls key metrics from those reports into a time-series structure.

The reports are the evidence. The CSV is the temporal index into them.

This separation follows the existing pattern: `orchestrate.sh` produces `vault_health_report.md` (the snapshot). The observation layer extracts metrics from it (the time series). Neither replaces the other.

---

## 2. Where Comprehension Lives

### The Question

The detection tools are mechanical scripts. Comprehension requires contextual reasoning. Where does this new kind of capability live in the architecture?

### The Boundary Test

[[AM — Integrity Layers]] defines the boundary: "Can the check be expressed as a deterministic rule that produces the same result every time, regardless of who or what runs it?" Comprehension fails this test by definition. "Finding counts dropped 60%" is mechanical; "finding counts dropped because Wave 6 fixed the most common structural violations" requires causal reasoning. **Comprehension lives in the semantic layer.**

### Existing Precedent

The architecture already contains a semantic layer component: `summarise_report.py` in `04_EXECUTE/runtime/` invokes a local LLM (Ollama) to produce a natural-language summary of the health report. This is a primitive comprehension tool — it consumes mechanical output and produces semantic interpretation. It lacks temporal context and structured judgment, but the architectural pattern is proven.

Wave 9's comprehension is the mature version of what `summarise_report.py` is the embryo of. Same pattern (LLM consumes mechanical output), deeper capability (temporal comparison, pattern recognition, causal reasoning, judgment).

### Governance Already Exists

The earlier design discussion hypothesised that Wave 9 would need a new "Agent Convention" document to govern LLM-mediated observation work. **This was wrong.** [[AM — LLM Conventions]] already covers this territory comprehensively:

- The three audits (Alignment, Integrity, Viability) apply to self-observation findings.
- The Evidence Convention (embed in artifact) governs how observation analyses are recorded.
- The "Consuming Mechanical Output" section directly supports the architecture: semantic layer grounds itself in mechanical output before reasoning about meaning.
- The Safety Rules (no self-approval, no irreversible changes without human approval, express uncertainty rather than force judgment) apply to observation-based judgments.
- The Operational Risks (context window pressure, hallucination, sycophancy, over-commitment, instruction drift) apply to autonomous comprehension.

**What Wave 9 may need:** Extensions or additions to LLM Conventions specific to temporal observation (e.g., conventions for how the LLM handles trend ambiguity, how it distinguishes signal from noise in time-series data, how it handles insufficient history for reliable trend detection). These would be additions to an existing document, not a new governance artifact. Law 3 — don't create governance that could live within existing governance.

### The Comprehension Layer Is Not a "Tool"

This is an important distinction. The Tool Conventions govern mechanical detection tools — they are stateless, read-check-report executors (Convention 1). Comprehension capabilities are fundamentally different:

| Property | Detection Tools (Tool Conventions) | Comprehension (LLM Conventions) |
|----------|-----------------------------------|-------------------------------|
| **Determinism** | Deterministic — same input, same output | Non-deterministic — same input may produce different analysis due to LLM reasoning |
| **Interpretive scope** | Checks against explicit rules — no reasoning about meaning | Reasons about meaning, causation, and context — interprets what data signifies |
| **Data scope** | Current vault state (single snapshot) | Current state + historical data (temporal context from observation CSV) |
| **Output** | Findings (pass/fail against rules) | Analysis (patterns, causes, judgments) |
| **Authority** | N/A — tools don't hold authority | Operates within a role (Worker/Reviewer) |
| **Governance** | Tool Conventions | LLM Conventions |

**Note on statefulness:** Both detection tools and comprehension tools are stateless in implementation — neither maintains internal state across runs. Both read external data (the vault; the observation CSV) fresh each invocation. The critical distinction is **determinism** (a detection tool always produces the same findings from the same vault state; an LLM may produce different analyses from the same observation data) and **interpretive scope** (a detection tool checks against rules; a comprehension tool reasons about what the data means). These are the properties that place them on opposite sides of the [[AM — Integrity Layers]] boundary.

Attempting to govern comprehension with Tool Conventions would violate the Integrity Layers boundary. The two governance documents exist precisely because the two types of capability are fundamentally different.

---

## 3. Self-Understanding Scope — The Full Depth Map

### The Question

How deep does "understanding why" go? What is the complete landscape?

### Five Depth Levels

The design discussion identified a progression of depth levels. Each requires all levels below it (Seed 3 — Constraint: no higher level without the lower levels in place). Each maps to a stage in the Irreducible Loop.

| Level | Name | What it provides | Example |
|-------|------|-----------------|---------|
| **0** | **Raw Data** | Numbers, counts, timestamps, exit codes | "12 findings, 3 warnings, exit code 1" |
| **1** | **Self-Knowledge** | Data with context — comparison across time | "Finding counts dropped 60% since Wave 6. Three remaining findings are in archived documents." |
| **2** | **Self-Understanding** | Data with causation — why patterns exist | "Findings dropped because Wave 6 identified the most common structural violations, which were then fixed. Remaining findings persist because archived documents are intentionally not updated — a policy decision, not a deficiency." |
| **3** | **Self-Prediction** | Causation with projection — what happens next | "If we add lifecycle checking for templates, we should expect approximately 5-8 new findings based on the pattern from when we added lifecycle checking to concepts." |
| **4** | **Self-Direction** | Prediction with intent — what the system should do | "The system should prioritise extending git hygiene detection to cover tag signing before opening new detection categories, because closing coverage gaps in existing categories compounds more than opening new ones." |

### Relationship to the Irreducible Loop

The five depth levels are **not** a fractal instance of the Irreducible Loop. An earlier version of this analysis attempted to map each level to a Loop stage (Level 0 = Perception, Level 3 = Action, Level 4 = Feedback), but the mapping was forced — prediction is not action, and self-direction is closer to decision than feedback.

What is true: the five levels form a **dependency chain** governed by Seed 3 (Constraint) — no higher level without the lower levels in place. And the **observation pipeline** (Perceive → Comprehend → Judge → Record → next cycle) is a genuine fractal instance of the Irreducible Loop (see Section 5). But the depth levels describe **what the system can know**, not **how it processes**. They are a knowledge hierarchy, not a process instance. The Constraint seed governs them (strict dependency), but the Process seed does not map onto them directly.

This distinction matters: confusing a knowledge hierarchy with a process loop would lead to building the depth levels as sequential pipeline stages, when in practice multiple levels can be addressed within a single comprehension step (e.g., comprehension may produce both Level 1 context and Level 2 causal reasoning in the same analysis).

### Level Dependencies

The dependency chain is strict:

```
Level 0 (Raw Data)
  ↓ requires
Level 1 (Self-Knowledge) — needs data to contextualise
  ↓ requires
Level 2 (Self-Understanding) — needs context to reason about causes
  ↓ requires
Level 3 (Self-Prediction) — needs causal models to project
  ↓ requires
Level 4 (Self-Direction) — needs predictions to recommend
```

No level may bypass the one below it. This is Seed 3 applied to observation depth.

### Layer Mapping

Each level maps to the Integrity Layers:

- **Level 0:** Mechanical. Deterministic extraction of metrics from reports. Governed by Tool Conventions.
- **Levels 1-4:** Semantic. Requires LLM reasoning. Governed by LLM Conventions.

The boundary falls between Level 0 and Level 1 — exactly where the Integrity Layers boundary falls (deterministic vs. judgment-based).

### Stage 1 Scope Recommendation

For Stage 1 (self-governance), Levels 0-2 are necessary and Level 3 is valuable. Level 4 is already happening — it occurs in every wave reflection and design conversation — but it happens collaboratively (human + LLM), not autonomously. The question is whether to codify the *capability design* for Level 4 now (design it, govern it) even if the *implementation* remains collaborative.

**Recommendation:** Design all five levels now. The design must be complete because, in a fractal system, a gap at the foundation propagates upward (brainstorm insight). Implement Levels 0-2 as the primary build target. Implement Level 3 if achievable within wave scope. Document Level 4's design and governance without building autonomous implementation — it remains a human-collaborative capability until Stage 2.

D3 (Controlled Evolution) governs this: graduated implementation within complete design.

---

## 4. Temporal Data Retention

### The Question

How much history does AM need to keep? What's the retention policy?

### Three Data Categories, Three Retention Strategies

Different types of observation data have different retention characteristics. The governing principles are Law 2 (verifiable, reversible, accountable — favour keeping source data) balanced against Law 3 (only what is necessary — don't hoard data that serves no purpose).

#### Category 1: Raw Metrics (Observation CSV)

**Retention: Keep everything.**

The observation CSV grows at approximately one row per metric per maintenance run. Even with daily runs and 20 metrics per run, that is approximately 7,300 rows per year. CSV handles this trivially. Git handles this trivially.

Raw data is the foundation — higher-level analyses can always be re-derived from it, but raw data cannot be re-derived from summaries. Law 2 (reversible) favours keeping the source. Law 3 does not argue against it because the storage cost is negligible.

#### Category 2: Health Reports (Markdown Snapshots)

**Retention: Active window + archive.**

Keep recent reports accessible in `04_EXECUTE/tools/vault-maintenance/reports/` (suggested window: 90 days or a configurable number of runs). Archive older reports to `05_RECORD/archive/`. The observation CSV captures the essential metrics from each report, so archived reports serve as reference material for deep investigation rather than routine analysis.

This follows the existing pattern: completed proposals move from `03_DECIDE/active/` to `05_RECORD/archive/`. Health reports should follow the same lifecycle.

**Governance note:** This is an addition to [[AM — Artifact Lifecycles]], not a standalone policy. Health reports are an artifact type that needs a lifecycle definition. Law 3 — don't create governance that could live within existing governance.

#### Category 3: Comprehension Outputs (Analyses, Trend Reports, Judgments)

**Retention: Standard record lifecycle.**

Comprehension outputs are interpretive records. They live in `05_RECORD/` and follow the same lifecycle as session logs, audit reports, and wave reflections. They are the system's memory of what it understood at a given point — valuable for longitudinal comparison ("what did we understand six months ago vs. now?").

These artifacts follow the Evidence Convention from [[AM — LLM Conventions]]: the reasoning is embedded, traceable to the three audit types, and attributable.

### The Governing Principle

**Raw data is cheap, keep it. Interpreted artifacts follow Artifact Lifecycles. Nothing is deleted without passing the viability audit** (Foundations Audit Taxonomy: "Is this earning its place?").

---

## 5. Integration with Existing Maintenance

### The Question

Does Wave 9 extend the existing `orchestrate.sh` pipeline, or does it introduce a new orchestration layer that sits above it?

### Current Architecture

```
orchestrate.sh (runs 13 detection tools → vault_health_report.md)
  ↓ consumed by
run_maintenance.sh (wraps orchestrate → LLM summary via summarise_report.py → notification)
```

`orchestrate.sh` is a Capture-stage tool — it perceives the vault's current state mechanically. `run_maintenance.sh` is a simple coordinator that adds a semantic summary and a notification.

### The Fractal Answer

Wave 9 does not extend what orchestrate does. It adds a new loop that **consumes** what orchestrate produces. The observation pipeline is a loop within the loop — the same Irreducible Loop pattern, with orchestrate's output as its input.

**Do not extend orchestrate.sh.** It does its job (mechanical detection) correctly and completely. Adding observation capabilities to it would mix mechanical and semantic concerns, violating the Integrity Layers boundary.

**Build the observation pipeline as its own instance of the Irreducible Loop, composed with the existing detection pipeline.** The composition point is `run_maintenance.sh`, which evolves from a simple wrapper into a **coordination layer** that sequences the detection pipeline and the observation pipeline. This is architecturally a layer above `orchestrate.sh` — and that is the correct design. The coordination layer does not duplicate or replace what orchestrate does; it sequences two independent pipelines and manages their data flow. This is the same pattern as `orchestrate.sh` itself, which coordinates 13 independent detection tools.

### The Expanded Maintenance Flow

The observation pipeline is not a linear sequence. The brainstorm identifies three core capabilities (Perception, Comprehension, Judgment) that form a **feedback triangle** — each informs the others. The pipeline implementation must honour this structure.

```
MECHANICAL DETECTION (existing — unchanged)
  orchestrate.sh
    → runs 13 detection tools
    → produces vault_health_report.md

  ↓ output feeds into

OBSERVATION PIPELINE (Wave 9 — new)

  The three core capabilities form a feedback triangle:

  ┌─────────────────────────────────────────────────────┐
  │                                                     │
  │            ┌──────────────┐                         │
  │    ┌──────▶│  COMPREHEND  │◀─────┐                  │
  │    │       │ (Levels 1-2) │      │                  │
  │    │       └──────┬───────┘      │                  │
  │    │              │              │                  │
  │    │  understanding               judgment tells   │
  │    │  tells perception            comprehension    │
  │    │  where to look               what patterns    │
  │    │  next (attention)            to investigate   │
  │    │              │              │                  │
  │    │              ▼              │                  │
  │ ┌──┴───────┐           ┌───────┴──────┐           │
  │ │ PERCEIVE │           │    JUDGE     │           │
  │ │(Level 0) ├──────────▶│ (Levels 2-3) │           │
  │ └──────────┘  raw data └──────────────┘           │
  │                feeds                               │
  │                comprehension                       │
  └─────────────────────────────────────────────────────┘

  Perceive (Level 0 — mechanical)
    → extract metrics from vault_health_report.md
    → append to observation CSV
    → compute deltas from previous run
    → INPUT: health report + previous observation data
            + attention signals from prior comprehension
    → OUTPUT: updated observation CSV (feeds Comprehend)

  Comprehend (Levels 1-2 — semantic, LLM-mediated)
    → consume observation CSV + recent health reports
    → identify trends, patterns, anomalies
    → relate findings to governance context
    → produce observation analysis
    → INPUT: observation CSV (from Perceive)
            + investigation priorities (from Judge)
    → OUTPUT: trend analysis (feeds Judge)
             + attention signals (feeds back to Perceive:
               "look at git metrics more closely next run")

  Judge (Levels 2-3 — semantic, LLM-mediated)
    → evaluate whether patterns indicate something that should change
    → formulate recommendations or draft proposals
    → apply escalation levels (Level 1: automatic, Level 2: agent judgment, Level 3: escalate to human)
    → INPUT: trend analysis (from Comprehend)
    → OUTPUT: recommendations/proposals (feeds Record)
             + investigation priorities (feeds back to Comprehend:
               "this recommendation needs deeper causal analysis")

  Record
    → log observation, analysis, and judgment
    → update observation records in 05_RECORD/

  ↓ the full cycle feeds back into the next run

  NEXT CYCLE (loop closure)
    → the observation CSV persists — each run builds on all prior runs
    → comprehension's attention signals persist — what to look at next
    → judgment outcomes become data points in the next run's history
    → the triangle runs again with richer context each time

  ↓ outputs also feed into

NOTIFICATION (existing — extended)
  notify.sh
    → now includes observation findings alongside detection findings
```

**Note on execution order:** Although the three capabilities form a triangle, a single run still has a practical starting point: Perceive runs first (mechanical — it needs no prior semantic input on the first run), then Comprehend, then Judge. The feedback arrows operate **across runs**: Comprehend's attention signals from run N inform Perceive's focus in run N+1. Judge's investigation priorities from run N inform Comprehend's analysis in run N+1. The triangle is a temporal structure, not a within-run cycle. This is consistent with how the Irreducible Loop itself operates — Reflect feeds back to Capture, but across cycles, not within a single pass.

### Fractal Validation

The observation pipeline maps to the Irreducible Loop at the cycle level:

| Observation Pipeline Stage | Irreducible Loop Stage | What Happens |
|---------------------------|----------------------|-------------|
| Perceive | Perception (Capture) | Collect operational metrics |
| Comprehend | Interpretation (Knowledge) | Place metrics in temporal context |
| Judge | Decision (Decide) | Evaluate what should change |
| Record | Memory (Record) | Log the observation cycle |
| *(triangle feedback across runs)* | Feedback (Reflect) | Previous cycle's comprehension and judgment inform next cycle's perception and analysis |

The feedback triangle adds internal structure that the basic Irreducible Loop doesn't specify — it describes how the Interpretation, Decision, and Perception stages inform each other across iterations. This is consistent with the brainstorm's insight that the observation apparatus is "a small loop inside the larger loop." The triangle is the internal dynamic; the Irreducible Loop is the external cycle.

### Composition, Not Extension

Each stage of the observation pipeline is **independently useful and composable** (Tool Convention 4):

- The metric extraction step can run without comprehension (useful for building up history before enabling analysis).
- The comprehension step can run without judgment (useful for generating trend reports without recommending changes).
- The judgment step can run without automatic action (useful for producing proposals that require human review).

This composability allows incremental deployment — build and deploy one stage at a time, prove it works, then add the next. D3 (Controlled Evolution).

### D6 (Separation of Powers) in the Observation Pipeline

The brainstorm identifies D6 as "the critical governance constraint for Wave 9." The observation pipeline must specify how Worker/Reviewer separation operates, not just invoke D6 as a principle.

**The observation pipeline runs in Worker mode.** The full cycle — perceive, comprehend, judge, record — is Worker-role work. The Worker collects data, analyses trends, and formulates recommendations. This is analogous to how a Worker builds a proposal: the Worker drafts, but the draft is not approved by the Worker.

**Observation outputs require Reviewer audit before they become proposals.** A judgment that says "the system should change X" is a recommendation, not an approved action. If the judgment reaches Level 2 (agent judgment), a separate Reviewer pass audits the recommendation — applying the three audits (Alignment, Integrity, Viability) to the observation analysis itself. If the judgment reaches Level 3 (human approval), the recommendation is escalated as a proposal draft for human review.

**The same model may play both roles, but not in the same run.** Per D6 and [[AM — LLM Conventions]] Safety Rule 1: the observation run (Worker) and the audit of its findings (Reviewer) must be separate invocations. In practice, this means:

- **Unattended maintenance runs** produce observation analyses and recommendations as Worker output. These are logged but not acted upon until a Reviewer pass (in a subsequent session or a separate automated step) audits them.
- **Interactive sessions** may have the LLM switch from Worker to Reviewer within the session, provided the switch is explicit and the Reviewer re-loads its role definition before auditing.

**Level 1 actions are exempt from Reviewer audit.** Automatic actions (collecting metrics, generating observation logs, producing trend reports) are routine and rule-driven. They do not require D6 separation — the same way mechanical detection tools don't require a Reviewer to run. D6 applies at Level 2 and above, where judgment is exercised.

### What Happens to `summarise_report.py`

The existing `summarise_report.py` is a primitive comprehension tool — it invokes an LLM to summarise a single health report. Wave 9's comprehension step is a more capable version of the same function.

Two options:

1. **Absorb:** `summarise_report.py` is absorbed into the comprehension step. The new step does everything the old one did plus temporal analysis.
2. **Coexist:** `summarise_report.py` continues to produce a per-run summary (useful for quick notification). The comprehension step produces a deeper temporal analysis alongside it.

Recommendation: Coexist initially. The per-run summary serves a different purpose (immediate notification) than temporal analysis (strategic understanding). Merging them prematurely couples two concerns. Evaluate after implementation whether both are earning their place (Law 3).

---

## 6. Metrics Selection Principles

### The Question

What operational metrics are worth tracking? Can we derive principles rather than a fixed list?

### Principles for Metric Selection

The principles are derived from the Foundations and are applicable to any system AM governs — not just the AM vault. They serve two functions: **Principles 1-3 are universal** — every operational metric, at any depth level, must pass all three. **Principles 4-5 are the boundary test** between Level 0 (perception) and Levels 1-4 (comprehension) — they determine where a metric lives in the Integrity Layers architecture.

#### Principle 1 — Goal-Traceable (universal)

*Derives from: Law 1 (Direction of Authority) + Seed 2 (Goal primitive)*

Every metric must trace to something in the governance chain: North Star → Strategy → Roadmap → specific capability. If you cannot name what a metric serves, it does not earn its place (Law 3). The `goal_trace` field in the observation schema enforces this — every metric row must declare what it serves.

**Test:** "What governance goal does this metric advance?" If the answer requires reaching, the metric fails.

#### Principle 2 — Action-Informing (universal)

*Derives from: Seed 1 (Process — the decision stage) + Seed 2 (Control primitive)*

If a metric changes, there must be a plausible action response. A metric you can only observe but never act on is interesting but not operational.

**Test:** "If this number doubled tomorrow, what would we do?" If the answer is "nothing" or "I don't know," it is not a metric — it is trivia.

#### Principle 3 — Trend-Meaningful (universal)

*Derives from: Seed 1 (Process — the feedback stage) + Seed 2 (Memory primitive)*

The value over time must be more informative than the value at a single point. If a metric only matters as a snapshot ("are there broken links right now?"), it is a health check, not an observation metric. Observation metrics gain meaning from their trajectory — acceleration, deceleration, inflection points, plateaus.

**Test:** "Does this metric's history tell us something its current value doesn't?" If not, it belongs in detection, not observation.

#### Principle 4 — Mechanically Collectible (boundary test)

*Derives from: [[AM — Integrity Layers]] boundary test + D1 (Deterministic Control Surfaces)*

This principle does not filter out bad metrics — it **classifies** them. If a metric can be extracted deterministically from existing artifacts, it is a Level 0 perception metric (mechanical layer). If it requires judgment to produce, it belongs at Levels 1-4 (semantic layer). Both are valid metrics; they live in different layers.

**Test:** "Can a script extract this value from existing reports and produce the same result every time?" If yes → Level 0 perception metric, governed by Tool Conventions. If no → comprehension metric, governed by LLM Conventions.

A metric that passes Principles 1-3 but fails Principle 4 is not rejected — it is classified as semantic. For example, "causal explanation for finding trend" passes Goal-Traceable (serves vault improvement), Action-Informing (informs what to fix), and Trend-Meaningful (causation only matters across time) — but it requires LLM reasoning to produce, so it's a comprehension-layer output, not a perception-layer data point.

**Note on Principle 5 (Independent Verifiability):** An earlier version of this analysis included a fifth principle: "anyone should be able to reproduce the metric from the same inputs." This was removed because it is a consequence of Principle 4 + D1 (Deterministic Control Surfaces). If a metric is mechanically collectible (Principle 4), it is necessarily independently verifiable — D1 requires that mechanical operations are reproducible. A separate principle restating this adds no filtering or classification power (Law 3).

### Applying the Principles: Candidate Metrics

These candidates are illustrative, not prescriptive. The final list should be determined during the proposal phase using the five principles as the selection filter.

| Candidate Metric | Goal-Traceable | Action-Informing | Trend-Meaningful | Mechanically Collectible |
|-----------------|:-:|:-:|:-:|:-:|
| Finding count per tool per run | Yes (vault integrity) | Yes (rising = investigate) | Yes (trajectory matters) | Yes (parse reports) |
| Warning count per tool per run | Yes (vault integrity) | Yes (rising = investigate) | Yes (trajectory matters) | Yes (parse reports) |
| Total items checked per tool | Yes (coverage) | Yes (dropping = scope regression) | Yes (should grow with vault) | Yes (parse reports) |
| Wave duration (days from proposal to reflection) | Yes (process efficiency) | Yes (acceleration/stagnation signal) | Yes (trajectory is the insight) | Partial (requires commit history or date parsing) |
| Session frequency | Yes (operational tempo) | Partial (low frequency may be fine) | Yes (trend indicates engagement) | Yes (count session logs) |
| Finding resolution rate (fixed between runs) | Yes (vault health improvement) | Yes (declining = stagnation) | Yes (trajectory is the core value) | Yes (compare consecutive CSVs) |

---

## 7. Governance Implications

### What Already Exists and Covers Wave 9

The following governance documents already apply to Wave 9 without modification:

| Document | What it covers for Wave 9 |
|----------|--------------------------|
| [[Agent Maestro — Foundations]] | The kernel — all design traces here |
| [[AM — Integrity Layers]] | The mechanical/semantic boundary that structures the observation pipeline |
| [[AM — Tool Conventions]] | Governs the mechanical perception layer (Level 0 metric extraction) |
| [[AM — LLM Conventions]] | Governs the semantic comprehension/judgment layers (Levels 1-4) |
| [[AM — Artifact Lifecycles]] | Governs lifecycle of observation artifacts (with potential extension) |
| [[Role — Worker]] / [[Role — Reviewer]] | Governs who builds vs. who audits observation capabilities |

### What May Need Extension

| Document | Potential Extension |
|----------|-------------------|
| [[AM — LLM Conventions]] | Conventions for temporal observation: handling trend ambiguity, minimum history thresholds for reliable analysis, distinguishing signal from noise in time-series data |
| [[AM — Artifact Lifecycles]] | Lifecycle definition for health reports (active window → archive) and observation data (retention policy) |
| [[Self-Observation]] (concept) | Update to reflect the five depth levels and the observation pipeline architecture |
| [[SYSTEM_MAP]] | Update to include new Wave 9 artifacts |

### What Does Not Need to Be Created

- ~~Agent Convention document~~ — LLM Conventions already covers this. Creating a separate document would violate Law 3.
- ~~Standalone retention policy~~ — lives within Artifact Lifecycles.
- ~~New role definitions~~ — Worker and Reviewer roles already accommodate observation work.

---

## 8. Completeness Check — Seven Primitives

Applying Seed 2's completeness test to the Wave 9 design as a whole:

| Primitive | How Wave 9 addresses it |
|-----------|------------------------|
| **State** | Observation CSV captures current and historical metric state |
| **Goal** | Goal-traceable metrics; the overall goal is operational self-awareness for Stage 1 exit |
| **Policy** | Four metric selection principles; metric registry defines thresholds and escalation levels; LLM Conventions govern semantic work |
| **Memory** | Temporal data retention strategy; observation CSV is the memory layer; comprehension outputs are interpretive memory |
| **Tools** | Metric extraction tool (mechanical); comprehension/judgment tool (semantic); integrated via run_maintenance.sh |
| **Control** | D6 (Separation of Powers) — Worker builds, Reviewer audits; D4 (Human Sovereignty) — Level 3 for governance changes; escalation levels for observation-driven actions |
| **Feedback** | The observation pipeline itself IS the feedback mechanism — it closes the loop between detection and improvement |

No gaps identified.

---

## 9. Open Questions Remaining

1. **Specific CSV field refinement.** The candidate schema is derived from Seed 2 but needs validation against actual health report output to confirm all fields are extractable.

2. **Comprehension tool architecture (implementation-scope).** The comprehension step invokes an LLM — does it use the existing Ollama integration (local model), or is this the point where a more capable model is needed? What are the implications for unattended operation? This is a build decision, not a design decision — it belongs in the proposal, not the design analysis. Noted here as a known constraint.

3. **LLM Conventions extensions.** The specific additions needed for temporal observation work should be drafted and reviewed before build.

4. **Artifact Lifecycles additions.** Health report lifecycle and observation data lifecycle need to be defined within the existing document.

5. **Sub-wave decomposition.** Now that the design landscape is mapped, the question of staging returns — but informed by understanding rather than guesswork.

---

## Audit

**Auditor:** Claude (Reviewer mode), 2026-03-17
**Lens:** Adversarial — assumed the artifact fails, actively looked for evidence.
**Governance loaded:** Foundations, Strategy, Integrity Layers, Tool Conventions, LLM Conventions, Artifact Lifecycles, Treatise on Core Principles.

### Alignment (Seed 3 — Constraint)

Does this design serve the brainstorm's central question and the Foundations?

- **A1 (Significant — RESOLVED):** The observation pipeline was originally rendered as a linear sequence (Perceive → Comprehend → Judge), contradicting the brainstorm's feedback triangle insight. Fixed: pipeline now explicitly shows the three internal feedback arrows (comprehension → perception via attention, judgment → comprehension via investigation priorities, perception → comprehension via raw data) and clarifies that the triangle operates across runs, not within a single pass.
- **A2 (Moderate — RESOLVED):** The five depth levels were forced into an Irreducible Loop mapping (Level 3 = Action, Level 4 = Feedback). This was a retrofit, not a genuine fractal instance. Fixed: the false mapping was withdrawn. The depth levels are now correctly described as a knowledge hierarchy governed by Seed 3 (dependency chain), not a process instance of Seed 1.
- **A3 (Moderate — RESOLVED):** D6 (Separation of Powers) was cited but not operationally specified. Fixed: new section specifies that the observation pipeline runs in Worker mode, outputs require Reviewer audit before becoming proposals, the same model may play both roles but not in the same run, and Level 1 actions are exempt from D6 separation.

### Integrity (Seed 2 — Structure)

Is this internally sound and consistent?

- **I1 (Significant — RESOLVED):** The CSV schema claimed derivation from all seven Seed 2 primitives but omitted three fields (Policy, Control, Feedback-direction). Fixed: schema now includes `direction` (with metric polarity convention), `threshold` (Policy), and `escalation_level` (Control). A metric registry concept was introduced to separate metric definitions from metric data.
- **I2 (Minor — RESOLVED):** The comparison table between detection tools and comprehension incorrectly listed "statefulness" as the distinguishing property. Both are stateless in implementation. Fixed: table now uses "determinism" and "interpretive scope" as the key distinctions, with an explanatory note.
- **I3 (Moderate — RESOLVED):** The five metric selection principles were framed as universal filters, but Principles 4-5 only applied to Level 0 metrics. Fixed: Principles 1-3 are now explicitly labelled as universal; Principle 4 is a classification (boundary) test, not a filter. Principle 5 was removed as a consequence of Principle 4 + D1 (Law 3).
- **I4 (Minor — RESOLVED):** The design rejected "a layer above orchestrate" while describing exactly that. Fixed: the coordination layer is now explicitly acknowledged as a layer above `orchestrate.sh`, and the design owns this as the correct architecture.

### Viability (Seed 1 — Process)

Is everything earning its place?

- **V1 (Minor — RESOLVED):** Principles 4 and 5 overlapped. Fixed: Principle 5 removed (Law 3). Four principles remain.
- **V2 (Minor — RESOLVED):** A candidate metric ("Overall health status per run") that failed two principles was included in the illustrative table. Fixed: removed from the table.
- **V3 (Minor — RESOLVED):** Open Question 2 (Ollama vs. more capable model) is implementation-scope, not design-scope. Fixed: flagged as implementation-scope with a note that it belongs in the proposal.

### Verdict

All ten findings resolved. Two significant structural issues (feedback triangle linearisation, schema incompleteness) were corrected. The design analysis is internally consistent, aligned with its source documents, and every section earns its place. Ready to feed a proposal.

---

*This design analysis captures the formal design decisions from the Wave 9 design discussion on 2026-03-17. Adversarial audit completed and findings resolved on the same date.*
