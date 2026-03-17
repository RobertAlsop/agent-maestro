---
title: "Wave 9 — Design Analysis v2"
type: pipeline
status: draft
authority_weight: 10
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Wave 9 — Self-Observation Brainstorm]]"
    - "[[Wave 9 — Design Analysis]]"
    - "[[Agent Maestro — Foundations]]"
    - "[[AM — Artifact Lifecycles]]"
  governs: []
  related:
    - "[[AM — LLM Conventions]]"
    - "[[AM — Integrity Layers]]"
    - "[[AM — Tool Conventions]]"
    - "[[Self-Observation]]"
    - "[[Memory Architecture]]"
    - "[[AM — Treatise on Core Principles]]"
tags: [capture, design-analysis, wave-9, self-observation, stage-1]
---

# Wave 9 — Design Analysis v2

**Source:** Design discussion between Rob and Claude (Cowork), 2026-03-17. This document supersedes the v1 design analysis following an adversarial audit that revealed the original model was not fractal — it introduced a five-level knowledge hierarchy that did not map to the Irreducible Loop. This version reframes Wave 9 using a pattern that already exists in the system.

**Purpose:** Provide a complete, auditable design landscape for Wave 9, grounded in the fractal principle: the correct model already exists within the system.

---

## The Core Reframe

### What v1 Got Wrong

The v1 design analysis decomposed self-observation into three capabilities (perception, comprehension, judgment) arranged in a feedback triangle, with five depth levels (Raw Data → Self-Knowledge → Self-Understanding → Self-Prediction → Self-Direction). The adversarial audit found that the depth levels did not map to the Irreducible Loop — the fractal claim was forced. The v1 response was to withdraw the fractal claim and accept the depth levels as a separate "knowledge hierarchy."

That response was wrong. Not because the audit finding was wrong, but because accepting a non-fractal component into the architecture is accepting complexity. The fractal meta-principle exists to constrain complexity: if the same pattern applies at every level, you only need to understand one pattern. A non-fractal component breaks that property. In a system that will eventually have LLMs governing themselves, complexity is the primary threat. It is worth spending time here.

### What the Fractal Principle Tells Us

The fractal principle says: the correct model already exists within the system and has been used at every level below this one. Look for it.

The model that already exists is **the Irreducible Loop applied to different subjects at different intensities**. This is exactly how [[AM — Artifact Lifecycles]] works:

- A **capture item** follows the Loop at low intensity: created → triaged → routed. Gates are lightweight.
- A **governance document** follows the Loop at high intensity: drafted → full audit with adversarial lens → human approval → active. Gates are thorough.
- Same Loop. Same stages. Same gates. Different resolution. The subject determines the intensity.

Self-observation is the same pattern. It is the Irreducible Loop applied to **the system itself** as subject. The "three capabilities" from the brainstorm — perception, comprehension, judgment — are not a separate architecture. They are three of the six Loop stages, encountered again:

| Brainstorm capability | Irreducible Loop stage | Why they are the same |
|----------------------|----------------------|----------------------|
| Perception | **Perceive** (Capture) | Collect data about the system's operation |
| Comprehension | **Interpret** (Knowledge) | Understand what the data means in context |
| Judgment | **Decide** (Decide) | Evaluate what should change |
| *(not named in brainstorm)* | **Act** (Execute) | Propose or implement the change |
| *(not named in brainstorm)* | **Record** (Record) | Log what was observed and decided |
| *(not named in brainstorm)* | **Reflect** (Reflect) | Evaluate whether prior changes achieved their purpose; set attention for next cycle |

The brainstorm discovered the first three stages and recognised them as a loop. It didn't recognise them as the Irreducible Loop because it named them differently and treated them as a novel architecture. They are not novel. They are the same Loop the vault uses for everything else.

### What the "Depth Levels" Actually Were

The v1 depth levels (Raw Data, Self-Knowledge, Self-Understanding, Self-Prediction, Self-Direction) were not levels of a knowledge hierarchy. They were **examples of what the Loop stages produce at different intensities**:

| v1 "Depth Level" | Actually is | Loop stage | Intensity |
|-----------------|------------|------------|-----------|
| Raw Data | Perceive output at low intensity | Perceive | Low — extract numbers |
| Self-Knowledge | Interpret output at low intensity | Interpret | Low — compare to previous |
| Self-Understanding | Interpret output at high intensity | Interpret | High — reason about causation |
| Self-Prediction | Decide output at medium intensity | Decide | Medium — project from patterns |
| Self-Direction | Decide output at high intensity | Decide | High — recommend strategic action |

Five "levels" reduce to two stages at varying intensities. The Constraint seed (dependency chain) still applies — you cannot interpret without data, you cannot decide without interpretation — but that is just the Loop's own stage ordering, which already enforces this. No additional model is needed.

---

## The Self-Observation Loop

### Definition

Self-observation is the Irreducible Loop executed with the system itself as subject.

```
perceive → interpret → decide → act → record → reflect
    ↑                                              |
    └──────────────── next cycle ◀─────────────────┘
```

This is not a new pipeline. It is the same pipeline the vault already uses for every wave, every artifact lifecycle, and every maintenance run. What is new is the **subject** (the system's own operation) and the **temporal dimension** (observations accumulate across runs, enabling trend detection).

### Intensity Is Governed by Escalation Levels

The intensity at which each stage executes is not arbitrary — it maps directly to the escalation levels already defined in the Foundations:

| Escalation Level | When it applies | What the Loop produces |
|-----------------|----------------|----------------------|
| **Level 1 — Automatic** | Routine maintenance runs. No anomalies detected. | Perceive: extract metrics. Interpret: compare to previous run. Decide: no action needed. Act: nothing. Record: append to CSV. Reflect: carry forward attention signals. |
| **Level 2 — Agent Judgment** | Anomalies, trends, or patterns detected that require reasoning. | Perceive: extract metrics + deeper data gathering. Interpret: causal analysis — why is this happening? Decide: formulate recommendation. Act: draft a recommendation (not a proposal). Record: produce observation analysis. Reflect: evaluate whether prior recommendations achieved their purpose. |
| **Level 3 — Human Approval** | Observations indicate something that touches governance, architecture, or irreversible change. | Perceive: comprehensive data gathering. Interpret: full causal analysis with evidence chain. Decide: draft a proposal for human review. Act: escalate to human with full context. Record: full observation report. Reflect: post-change assessment — did the approved change achieve its goal? |

This is the same escalation model used everywhere in AM. The observation loop does not need its own intensity framework — the system already has one.

### The Artifact Lifecycles Parallel

The parallel to [[AM — Artifact Lifecycles]] is direct and structural, not metaphorical:

| Property | Artifact Lifecycles | Self-Observation Loop |
|----------|-------------------|--------------------|
| **Pattern** | Irreducible Loop | Irreducible Loop |
| **Subject** | A vault artifact (capture item, proposal, concept, etc.) | The system's own operation |
| **Stages** | Created → Triaged → Routed → Referenced (capture item example) | Perceive → Interpret → Decide → Act → Record → Reflect |
| **Gates** | Between every stage. Intensity scales with authority_weight. | Between every stage. Intensity scales with escalation level. |
| **Intensity variable** | Authority weight of the artifact type | Escalation level triggered by observations |
| **Low intensity** | Capture item: lightweight triage gate | Level 1: routine metric extraction and comparison |
| **High intensity** | Governance document: full adversarial audit + human approval | Level 3: comprehensive analysis, proposal, human review |
| **Governance** | Mechanical checks (Tool Conventions) + semantic assessment (LLM Conventions) | Mechanical perception (Tool Conventions) + semantic interpretation/judgment (LLM Conventions) |

The self-observation loop is an artifact lifecycle where the "artifact" is the system's operational state across time.

---

## Practical Design Decisions

The reframe simplifies the conceptual model. The practical questions from v1 remain, but several answers become cleaner.

### 1. Observation Data Structure

**Unchanged from v1 (post-audit).** The CSV format decision, the Seed 2 derivation, and the 13-field schema remain valid. They were not affected by the depth-level model — they were derived from Seed 2 independently.

**Format:** CSV. Governed by D2 (Three-Layer Memory Model, Layer 2). Git-friendly, human-readable, tool-composable, consistent with existing `session_index.csv` pattern.

**Schema:**

```
timestamp, run_id, tool, metric_name, metric_value, previous_value, delta, direction, category, goal_trace, threshold, escalation_level, source_report
```

Each field traces to a Seed 2 primitive:

| Field(s) | Seed 2 Primitive |
|----------|-----------------|
| `metric_name`, `metric_value` | State — what is true right now? |
| `goal_trace` | Goal — what does this serve? |
| `threshold` | Policy — what expectation applies? |
| `previous_value`, `delta`, `direction` | Memory + Feedback — comparison to past, directional assessment |
| `tool`, `source_report` | Tools — what produced this? |
| `escalation_level` | Control — who acts on this? |

**Metric registry:** A separate small CSV or config file defines each metric's polarity (`lower_is_better` / `higher_is_better`), threshold, and default escalation level. The extraction tool reads the registry to compute `direction` mechanically from `delta` + polarity. This keeps metric definitions separate from metric data.

**Architectural relationship:** The observation CSV is an extraction layer. Health reports remain the source of truth for any specific run. The CSV is the temporal index into them.

### 2. Where Comprehension Lives

**Simplified by the reframe.** The question "where does comprehension live?" dissolves. There is no separate "comprehension layer." There are Loop stages, and they are either mechanical or semantic:

| Loop Stage | Integrity Layer | Governance |
|-----------|----------------|------------|
| **Perceive** | Mechanical | Tool Conventions — deterministic metric extraction |
| **Interpret** | Semantic | LLM Conventions — contextual reasoning about meaning |
| **Decide** | Semantic | LLM Conventions — judgment about what should change |
| **Act** | Depends on action | Level 1: mechanical (log). Level 2-3: semantic (propose) |
| **Record** | Mechanical | Tool Conventions — deterministic write to CSV/log |
| **Reflect** | Semantic | LLM Conventions — evaluative reasoning |

The [[AM — Integrity Layers]] boundary applies stage-by-stage, not capability-by-capability. Perceive and Record are mechanical. Interpret, Decide, and Reflect are semantic. Act straddles the boundary depending on escalation level. This is the same boundary that already operates in the maintenance pipeline — `orchestrate.sh` (mechanical) feeds `summarise_report.py` (semantic).

The existing `summarise_report.py` is a primitive instance of the Interpret stage at low intensity. Wave 9 extends it to operate at higher intensity and across time. Same stage, more capability.

### 3. Integration with Existing Maintenance

**The observation loop composes with the detection pipeline.** `orchestrate.sh` (mechanical detection) produces data. The observation loop consumes that data as its Perceive stage input.

`run_maintenance.sh` evolves into a coordination layer that sequences:

```
1. orchestrate.sh          → vault_health_report.md    (detection)
2. observation loop         → observation CSV + analysis  (self-observation)
3. notify.sh               → notification               (output)
```

This is architecturally a layer above `orchestrate.sh`. The coordination layer does not duplicate what orchestrate does — it sequences two independent pipelines. Same pattern as `orchestrate.sh` itself, which coordinates 13 independent detection tools.

**Composability (Tool Convention 4):** Each observation loop stage is independently useful:

- Perceive alone: builds up metric history before enabling semantic analysis. Useful for first N runs.
- Perceive + Interpret: produces trend reports without recommendations. Useful for human review.
- Full loop: produces recommendations. Useful at maturity.

This enables incremental deployment (D3 — Controlled Evolution): build and deploy one stage at a time.

**What happens to `summarise_report.py`:** Coexist initially. The per-run summary serves a different purpose (immediate notification) than temporal interpretation (strategic understanding). Evaluate after implementation whether both earn their place (Law 3).

### 4. D6 (Separation of Powers)

**The observation loop runs in Worker mode.** Perceive, Interpret, Decide, Act, Record, Reflect — all Worker-role work. The Worker collects data, analyses trends, and formulates recommendations.

**Observation outputs require Reviewer audit before they become proposals.** A recommendation is a draft, not an approved action. At Level 2: a separate Reviewer pass audits the recommendation. At Level 3: the recommendation is escalated as a proposal draft for human review.

**Same model, not same run.** Per D6 and [[AM — LLM Conventions]] Safety Rule 1: the observation run (Worker) and the audit of its findings (Reviewer) are separate invocations.

**Level 1 is exempt from D6.** Automatic actions (extracting metrics, logging observations) are routine and rule-driven. D6 applies at Level 2 and above, where judgment is exercised.

### 5. Metric Selection Principles

**Four principles, unchanged from v1 post-audit.**

Principles 1-3 are **universal** — every operational metric must pass all three:

1. **Goal-Traceable** (Law 1 + Seed 2 Goal): every metric must trace to the governance chain.
2. **Action-Informing** (Seed 1 Decision + Seed 2 Control): if it changes, there must be a plausible response.
3. **Trend-Meaningful** (Seed 1 Feedback + Seed 2 Memory): trajectory must be more informative than snapshot.

Principle 4 is a **boundary classifier**:

4. **Mechanically Collectible** (Integrity Layers boundary + D1): classifies the metric as mechanical (Level 0 Perceive, Tool Conventions) or semantic (Interpret/Decide, LLM Conventions).

### 6. Temporal Data Retention

**Unchanged from v1.** Three categories, three strategies:

- **Raw metrics (observation CSV):** Keep everything. ~7,300 rows/year. Negligible cost, irreplaceable source data. Law 2 (reversible) favours keeping it.
- **Health reports:** Active window (configurable, ~90 days) in `reports/`, then archive to `05_RECORD/archive/`. Addition to [[AM — Artifact Lifecycles]].
- **Observation analyses (Interpret/Decide outputs):** Standard record lifecycle in `05_RECORD/`. Evidence Convention from [[AM — LLM Conventions]] applies.

**Governing principle:** Raw data is cheap, keep it. Interpreted artifacts follow Artifact Lifecycles. Nothing is deleted without passing the viability audit.

---

## Governance Implications

### What Already Exists

| Document | What it covers |
|----------|---------------|
| [[Agent Maestro — Foundations]] | The kernel — the Loop IS the observation model |
| [[AM — Integrity Layers]] | Mechanical/semantic boundary applies stage-by-stage |
| [[AM — Tool Conventions]] | Governs Perceive and Record stages |
| [[AM — LLM Conventions]] | Governs Interpret, Decide, and Reflect stages |
| [[AM — Artifact Lifecycles]] | The parallel pattern — observation loop IS an artifact lifecycle |
| [[Role — Worker]] / [[Role — Reviewer]] | D6 application — Worker observes, Reviewer audits |

### What Needs Extension

| Document | Extension |
|----------|----------|
| [[AM — Artifact Lifecycles]] | Health report lifecycle (active window → archive). Observation data retention policy. |
| [[AM — LLM Conventions]] | Conventions for temporal reasoning: handling trend ambiguity, minimum history thresholds, signal vs. noise in time-series data. |
| [[Self-Observation]] (concept) | Update to reflect the Loop-based model — self-observation is the Irreducible Loop applied reflexively, not a separate architecture. |
| [[SYSTEM_MAP]] | New Wave 9 artifacts. |

### What Does Not Need to Be Created

- ~~Five depth levels~~ — dissolved into Loop stages at varying intensities.
- ~~Feedback triangle~~ — dissolved into the Loop's own cross-cycle feedback (Reflect feeds next Perceive).
- ~~Agent Convention document~~ — LLM Conventions already covers semantic work.
- ~~Standalone retention policy~~ — lives within Artifact Lifecycles.
- ~~New role definitions~~ — Worker and Reviewer already accommodate observation work.
- ~~New intensity/resolution framework~~ — escalation levels already provide this.

---

## Completeness Check — Seven Primitives

Applying Seed 2 to the Wave 9 design as a whole:

| Primitive | How Wave 9 addresses it |
|-----------|------------------------|
| **State** | Observation CSV captures current and historical metric state |
| **Goal** | Goal-traceable metrics; the overall goal is operational self-awareness for Stage 1 exit |
| **Policy** | Four metric selection principles; metric registry defines thresholds; escalation levels govern intensity; LLM Conventions govern semantic work |
| **Memory** | Observation CSV is temporal memory; health reports are snapshot memory; analyses are interpretive memory |
| **Tools** | Metric extraction (mechanical, Perceive/Record); LLM analysis (semantic, Interpret/Decide/Reflect); coordinated via run_maintenance.sh |
| **Control** | D6 — Worker observes, Reviewer audits; D4 — Level 3 for governance changes; escalation levels govern the full intensity range |
| **Feedback** | The observation loop IS the feedback mechanism. Reflect feeds next Perceive. The loop closes. |

No gaps.

---

## Stress Test — What Could Be Wrong With This Model?

These are the adversarial questions v2 should answer honestly before it goes to proposal.

### 1. Is the Artifact Lifecycles parallel genuine, or cosmetic?

The parallel holds structurally: same Loop, same gates, intensity scaled by a system variable (authority_weight for artifacts, escalation level for observations). The subject is different (a document vs. the system's operation), but the pattern is identical. The test: could you describe an artifact lifecycle and a self-observation cycle using the same template, parameterised only by subject and intensity variable? If yes, the parallel is structural. If no, it's cosmetic.

**Assessment:** Yes. Both are instances of: "receive input → interpret in context → decide on action → execute → record → reflect. Gates between stages. Intensity scales with stakes." The parallel is genuine.

### 2. Have we lost anything from v1 by dissolving the depth levels?

The depth levels described a real phenomenon: there is a difference between "findings dropped 60%" and "findings dropped because Wave 6 fixed the most common violations." The question is whether that difference needs its own model, or whether "low-intensity Interpret vs. high-intensity Interpret" captures the same phenomenon without additional architecture.

**Assessment:** The phenomenon is preserved. The model is simplified. What we lose is explicit names for the intermediate states (Self-Knowledge, Self-Understanding, Self-Prediction, Self-Direction). These names were useful for communication but architecturally they were just labels for "this stage at this intensity." If the labels prove useful during implementation, they can be reintroduced as vocabulary without reintroducing the five-level model. Law 3: remove now, add back only if needed.

### 3. Does the feedback triangle dissolve cleanly?

The brainstorm identified three feedback arrows: comprehension informs perception (attention), judgment informs comprehension (investigation priorities), perception feeds comprehension (raw data). In the Loop model: Reflect informs next Perceive (attention), Decide informs next Interpret (priorities), Perceive feeds Interpret (data). These are the Loop's standard cross-cycle feedback arrows. The triangle is not a separate structure — it is what the Loop's feedback looks like when you zoom in on three adjacent stages.

**Assessment:** Dissolves cleanly. The Loop's own Reflect → Perceive feedback, combined with the natural stage ordering (Perceive feeds Interpret, Interpret feeds Decide), produces the same three arrows without an additional "triangle" concept.

### 4. Is escalation level the right intensity variable?

Escalation levels (1, 2, 3) are coarse — three settings. The v1 depth levels had five settings. Is three sufficient?

**Assessment:** Three is sufficient because the escalation levels map to qualitative shifts in how work is done (automatic / agent judgment / human approval), not quantitative gradations. Within each level, the actual intensity varies naturally with the data — a Level 2 Interpret step that encounters a dramatic trend will produce deeper analysis than one that encounters a stable pattern. The escalation level sets the ceiling; the data determines the actual depth within that ceiling. Forcing finer gradations would be artificial.

### 5. Does this model handle the "self-understanding" insight from the brainstorm?

The brainstorm drew a distinction between self-knowledge (data + context) and self-understanding (data + causation). The latter requires knowing *why* — not just that findings dropped, but that they dropped because of a specific intervention. Does the Loop model capture this?

**Assessment:** Yes. The Interpret stage at Level 2+ is where causal reasoning happens. The LLM Conventions govern how the LLM performs this reasoning — grounded in mechanical output, traceable to Foundations, expressing uncertainty when appropriate. The distinction between "what happened" and "why it happened" is the distinction between Level 1 Interpret (routine comparison) and Level 2 Interpret (reasoned analysis). The Loop model captures it as an intensity difference within a single stage, which is simpler than a separate "level" in a knowledge hierarchy.

### 6. Does this model handle the "self-description test" from the brainstorm?

The brainstorm proposed: "ask the system what it is and what it does" as both an onboarding mechanism and an integrity check. Where does this live?

**Assessment:** This is a specific instance of the self-observation loop at Level 2 or 3. The subject is the system's documentation rather than its operational metrics. Perceive: read CLAUDE.md + governance chain + SYSTEM_MAP. Interpret: synthesise into a coherent self-description. Decide: evaluate whether the description is coherent — if not, that's a finding. Same Loop, different input data. It does not need its own model.

---

## Open Questions for Proposal Phase

1. **CSV schema validation.** The 13-field schema needs validation against actual health report output to confirm all fields are mechanically extractable.

2. **Metric registry design.** What format? How many initial metrics? What are the initial polarity, threshold, and escalation settings?

3. **LLM Conventions extensions.** Specific additions for temporal reasoning (trend ambiguity, minimum history, signal vs. noise) should be drafted before build.

4. **Artifact Lifecycles additions.** Health report lifecycle needs to be defined within the existing document.

5. **Comprehension tool architecture (implementation-scope).** Ollama vs. more capable model. Build decision, not design decision.

6. **Sub-wave decomposition.** Now that the model is simpler, staging may also be simpler — potentially: (a) build Perceive + Record (mechanical metric extraction), (b) build Interpret + Decide (semantic analysis), (c) build Reflect + full-loop integration.

---

*This design analysis (v2) supersedes v1 by reframing self-observation as the Irreducible Loop applied reflexively — the same pattern used by Artifact Lifecycles, applied to a new subject. The five depth levels and feedback triangle from v1 dissolve into the Loop's own stages, intensities, and cross-cycle feedback. v1 is preserved in capture for traceability.*
