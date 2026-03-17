---
title: "Wave 9 — Self-Observation Brainstorm"
type: pipeline
status: draft
authority_weight: 10
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[AM — Roadmap]]"
    - "[[AM — Future Waves Register]]"
    - "[[Self-Observation]]"
  governs: []
  related:
    - "[[Agent Maestro — Foundations]]"
    - "[[Agent Maestro — Strategy]]"
    - "[[Wave 8.3 — Reflection]]"
    - "[[Wave 8.4 — Capture Seed]]"
    - "[[AM — Artifact Lifecycles]]"
    - "[[AM — LLM Conventions]]"
    - "[[AM — Universal Workflow]]"
tags: [capture, brainstorm, wave-9, self-observation, stage-1]
---

# Wave 9 — Self-Observation Brainstorm

**Source:** Design conversation between Rob and Claude (Cowork), 2026-03-17. This is the first design session for Wave 9, following the completion of Wave 8.3 (Git Hygiene Detection) on the same day.

## Context

Wave 9 has been identified since the Wave 8 design sessions as the final Stage 1 wave. It was descoped from Wave 8 to keep that wave focused on pipeline enforcement and git-ops.

The mechanical integrity stack is now complete:

- **Structural** (Wave 6): vault shape, YAML validity, link integrity, naming conventions
- **Process** (Wave 8.2): lifecycle rules, pipeline gate compliance
- **Git** (Wave 8.3): version control convention compliance

All existing tools are **detection tools** — they check the current state of the vault against defined rules and report findings. They answer: *"Are the rules being followed right now?"*

Wave 9 asks a qualitatively different question.

## The Wave 9 Question

**Can AM observe its own operation across time, comprehend the patterns in what it sees, and form judgments about what should change — using the same pipeline, roles, and escalation framework it uses for everything else?**

This is the first time the system is invited to look at itself not as a set of rules to be checked, but as a living operation to be understood.

## Why This Wave Is Different

Waves 6 through 8 built **compliance checking** — mechanical verification against defined rules. Wave 9 introduces **operational self-awareness** — the ability to understand how the system is performing, why it performs the way it does, and what that implies for its evolution.

The shift is from *"is this correct?"* to *"what is happening, what does it mean, and what should change?"*

This is a significant inflection point. It's the first time an LLM is invited to reason about AM as a subject, not just process AM's artifacts as objects. It requires the most careful alignment with Foundations because the capability — once established — propagates fractally to every level of abstraction AM will eventually operate at.

## Three Core Capabilities

The design conversation identified three distinct capabilities hiding inside "self-observation." They are not a linear sequence — they form a **feedback triangle**, each informing the others.

### 1. Perception

**What:** Collecting data about what is happening in the system's operation.

Timing, metrics, frequencies, counts, trends. How long do waves take? How many findings accumulate per maintenance run? What's the ratio of warnings to errors over time? How frequently are sessions occurring? What's the distribution of work across pipeline stages?

**Character:** Largely mechanical. The detection tools already do a version of this at the structural level. Extending to operational telemetry is relatively straightforward — it's data collection.

**Relationship to existing tools:** The Wave 6 and 8 tools generate findings. Those findings are already data. Perception means collecting and structuring that data over time rather than treating each run as an isolated snapshot.

### 2. Comprehension

**What:** Looking at the data and understanding what it means in context.

A number by itself means nothing. "Wave 8.3 took 1 day" only means something if you know Wave 6 took 3 weeks and Wave 8.2 took 5 days. Comprehension is pattern recognition across time, and it requires memory — the ability to compare now to before.

**Character:** Requires context, history, and the ability to relate observations to each other. This is where the LLM's reasoning capability becomes essential — mechanical scripts can collect data, but comprehension requires the kind of contextual reasoning that detection tools cannot perform.

**Key insight:** Comprehension requires a model of what "normal" looks like. That model emerges from accumulated observation, not from a predefined rule.

### 3. Judgment

**What:** Deciding whether what you're observing is good, bad, improving, stagnating, or in need of change — and formulating what should be done about it.

**Character:** This is the strategic self-assessment piece. Not just "wave velocity is increasing" but "wave velocity is increasing because the mechanical integrity stack is mature enough that new capabilities build on solid ground — the architecture is compounding." Judgment connects observations to causes and causes to actions.

**Why it must be included now:** In a fractal system, a gap at the foundation propagates to every level built on top of it. If Wave 9 only builds perception, then the judgment pattern would need to be retrofitted later — shaped by the absence of judgment in the original design. Law 3 (Economy) says build only what's necessary, but this capability is demonstrably necessary for Stage 2 (applying AM to external systems). Better to design the complete pattern now and implement incrementally.

### The Feedback Triangle

The three capabilities are not sequential stages. They form a loop:

- **Comprehension informs perception:** Understanding what matters tells you where to look next.
- **Judgment informs comprehension:** Knowing what needs to change tells you what patterns to investigate.
- **Perception feeds comprehension:** Raw data provides the material for understanding.

This feedback structure mirrors the pipeline's own loop (Reflect feeds back to Capture). The observation apparatus itself is fractal — a small loop inside the larger loop.

### Completeness Test

Are these three comprehensive? The test is: can you think of an act of observation that doesn't decompose into some combination of perception, comprehension, and judgment? If you can, the model is incomplete. If you can't, it's sufficient.

One candidate for a fourth capability is **attention** — the selection of what to observe before perceiving it. But attention is a function of comprehension feeding backward (you need understanding to know where to look). It's not a separate capability; it's the feedback arrow from comprehension to perception.

## The Full Self-Improvement Loop

The observation capabilities serve a larger purpose: enabling AM to improve itself. The complete theoretical loop maps to the six pipeline stages:

| Moment | Pipeline Stage | What Happens |
|--------|---------------|-------------|
| **Perceive** | Capture | Collect operational data — timing, metrics, finding trends, session patterns |
| **Contextualise** | Knowledge | Place observations in context — compare to history, relate to goals, identify patterns |
| **Judge** | Decide | Evaluate whether something needs to change — formulate a proposal with evidence |
| **Execute** | Execute | Implement the change (or escalate to human) |
| **Record** | Record | Log what happened — the observation, the judgment, the action taken |
| **Reflect** | Reflect | Evaluate whether the change achieved its purpose — feed back into the next observation cycle |

This isn't a new pattern. It's the same universal pipeline the vault already uses for every wave. Wave 9 makes **the system itself the subject** of a pipeline cycle rather than a vault artifact.

The loop closes: reflection becomes the next observation. The system that observes itself learns from what it observes.

## Self-Knowledge vs Self-Understanding

The design conversation drew a distinction between two levels of operational self-awareness:

**Self-knowledge** is data with context: "Finding counts dropped 60% since Wave 6. The three remaining persistent findings are all in archived documents."

**Self-understanding** is data with causation: "Finding counts dropped because the Wave 6 tools identified the most common structural violations, which were then fixed. The remaining findings persist because archived documents are intentionally not updated — this is a policy decision, not a deficiency."

The difference matters because self-knowledge can only detect anomalies (things that deviate from pattern), while self-understanding can predict ("if we add this capability, it will integrate smoothly because the dependency structure supports it") and explain ("this principle exists because...").

**Design decision:** Wave 9 addresses the full landscape — both self-knowledge and self-understanding. Self-understanding is necessary for Stage 2 (governing external systems requires understanding *why* your governance works, not just *that* it works). In a fractal system, designing without it now means retrofitting later. The implementation can be incremental, but the design must be complete.

## AM's Self-Model

A critical insight from the design conversation: AM doesn't need to *create* a model of itself because **AM already is its own model**. The vault is simultaneously the system and the documentation of the system. The pipeline processes work and describes how work is processed. The governance documents govern the system and are themselves governed by the system.

The [[SYSTEM_MAP]] is the easiest access point — an index for an LLM to orient itself. But the complete self-model is the entire vault, including its git history, its operational reports, and its governance chain.

**What Wave 9 adds** is the dimension of **time**. Currently, AM knows its current state (what exists now). After Wave 9, AM knows its **trajectory** — where it's been, how fast it's moving, what's changing, what's stagnant. The extension is from snapshot to narrative, from inventory to history.

Temporal awareness enables trend detection, which enables prediction, which enables proactive self-improvement rather than reactive self-correction.

## The Self-Description Test

A related insight: if AM is truly self-describing and fractal, then an LLM reading CLAUDE.md and the governance chain should be able to explain what AM is, how it works, and how to operate within it — without a separate operating manual.

"Ask the system what it is and what it does" is both an onboarding mechanism and an integrity check. If the system can't explain itself coherently, that's a signal the documentation has drifted from reality. This should be one of Wave 9's observation capabilities.

## The Action Question

All current tools are detection tools — they read state and report. But AM has already taken **inward-facing actions** since Wave 7: writing reports, creating files, organising folders. The maintenance pipeline writes date-stamped reports to `05_RECORD/reports/`. These are actions — they create artifacts and change the vault's state.

So the action boundary isn't "Wave 9 introduces action." The distinction is:

- **Existing actions** are **routine and rule-driven** — run checks, write report, put it in the folder.
- **Wave 9 actions** would be **judgment-driven** — observe a pattern, form an understanding, propose a change.

The escalation levels already govern this:

| Level | What Wave 9 can do automatically |
|-------|--------------------------------|
| 1 — Automatic | Collect metrics, generate observation logs, produce trend reports |
| 2 — Agent judgment | Identify patterns, formulate improvement recommendations, draft proposals |
| 3 — Human approval | Any change to governance (authority_weight ≥ 80), structural changes, irreversible actions |

The existing Worker/Reviewer/Human architecture (D6 — Separation of Powers) applies to the self-improvement loop: the Worker observes and builds the analysis; the Reviewer audits the analysis before it becomes a proposal; the Human approves anything that touches governance.

## Separation of Powers in Self-Observation

D6 (Separation of Powers) is the critical governance constraint for Wave 9. The existing implementation — Worker and Reviewer roles as defined in `02_KNOWLEDGE/governance/roles/` — already provides the mechanism.

When the pipeline runs on itself as subject, D6 still applies: the entity that observes and proposes cannot also approve. The same model can play both Worker and Reviewer roles, but not for the same work in the same context. This is unchanged from any other AM operation — confirming that the existing architecture handles the self-observation case without modification.

## Fractal Validation

The pattern discovered in Wave 9 — a system observing its own operation across time, comprehending patterns, and forming judgments about what should change — must map at every level of abstraction:

| Scale | Subject | Observer |
|-------|---------|----------|
| **AM self-governance** | The vault, its processes, its history | AM's observation capabilities (Wave 9) |
| **AM governing an external system** | Another vault, codebase, or operational system | AM applying the same observe-comprehend-judge pattern outward |
| **A team governing its processes** | Team workflows, delivery patterns, communication | The team applying the same pattern to its own operation |
| **An organisation governing itself** | Departments, strategy execution, operational health | The organisation applying the same pattern at enterprise scale |

If the pattern works at the first level but breaks at any other, either the pattern is incomplete or the abstraction is wrong. This validation should be part of the Wave 9 design — not just building the capability, but confirming it's truly fractal.

## Relationship to Stage 1 Exit

Wave 9 is positioned as the final Stage 1 wave. The Stage 1 exit criteria from [[Agent Maestro — Strategy]]:

1. ✓ The vault detects its own structural problems automatically (Wave 6)
2. ✓ A task can flow through all 6 pipeline stages with appropriate automation and gates (Waves 5–8)
3. ✓ AM runs scheduled maintenance between human sessions (Wave 7)
4. ~ Someone new can pick up CLAUDE.md and operate effectively → **The self-description test (above) addresses this**
5. ✓ SOPs document how the system works → **[[AM — Universal Workflow]] and [[AM — Artifact Lifecycles]] cover this**

However, Stage 2 (applying AM to other systems) may still be further away than the criteria suggest. The design conversation identified potential additional waves within Stage 1 beyond Wave 9 — particularly around git workflow automation (Wave 8.4) and potentially other capabilities that emerge from Wave 9's self-observation findings. The exit assessment should happen after Wave 9 is complete, informed by what the self-observation capability actually reveals about AM's readiness.

## Open Design Questions for Proposal Phase

1. **Sub-wave structure:** Should Wave 9 be divided into sub-waves (9.1, 9.2, 9.3) corresponding to the three capabilities (perception, comprehension, judgment)? Or is a different decomposition more natural — perhaps by infrastructure layer (data collection, analysis engine, reporting/proposal mechanism)?

2. **Observation data structure:** What does `observation_log.csv` (or equivalent) look like? What fields capture operational telemetry in a way that supports trend analysis? How does it relate to the existing maintenance reports?

3. **Where does comprehension live?** The detection tools are Python scripts in `04_EXECUTE/tools/`. Comprehension and judgment require LLM reasoning. Does this mean the comprehension layer is a different kind of tool — one that invokes an LLM rather than running mechanical checks? How does this relate to the existing Ollama integration in Wave 7's maintenance pipeline?

4. **Self-understanding scope:** How deep does "understanding why" go in Stage 1? Can we define concrete tests for self-understanding (e.g., "the system can explain why finding counts decreased" or "the system can predict the impact of a proposed change")?

5. **Temporal data retention:** How much history does AM need to keep? Is there a governance rule for observation data lifecycle — how long metrics are retained, when they're archived, what's summarised vs. kept raw?

6. **Integration with existing maintenance:** Does Wave 9 extend the existing `orchestrate.sh` pipeline, or does it introduce a new orchestration layer that sits above it? The existing pipeline runs detection; the new layer would run observation-comprehension-judgment on top of detection outputs.

7. **The self-description test as a capability:** How do we implement "ask the system what it is"? Is it a tool that synthesises CLAUDE.md + governance chain + SYSTEM_MAP into a coherent self-description? What does a passing vs. failing self-description look like?

8. **Metrics that matter:** What are the specific operational metrics worth tracking? Candidates include: wave duration, finding counts per category over time, finding resolution rate, session frequency, governance document change frequency, proposal approval rate, time from capture to completion.

---

*This brainstorm captures the Wave 9 design conversation from 2026-03-17. It should be processed through a proposal when the design is ready to commit to scope and implementation approach.*
