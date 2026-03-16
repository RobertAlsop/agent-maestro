---
title: "Wave 6 — Reflection"
type: report
status: active
authority_weight: 30
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
    - "[[Proposal — Wave 6 Mechanical Integrity]]"
  governs: []
  related:
    - "[[Wave 5.2 — Final Reflection]]"
    - "[[AM — Integrity Layers]]"
    - "[[AM — Tool Conventions]]"
    - "[[AM — Roadmap]]"
    - "[[AM — Future Waves Register]]"
    - "[[Wave 7 — Brainstorm]]"
tags: [reflection, reflect, wave-6]
---

# Wave 6 — Reflection

## Purpose

Close the loop on Wave 6 (Mechanical Integrity). This reflection is written retrospectively — it was not produced at the end of the build session, which is itself a significant process finding addressed below.

## What Happened

### Starting State

Wave 5.2 (Pipeline Hardening) had delivered a lean, internally consistent vault with 72 codified rules, a universal workflow, a roadmap, and a future waves register. The governance was solid. The pipeline folders were operational. But nothing enforced any of it mechanically — every integrity check depended on a human and an LLM reading files and applying judgment. The vault's rules existed only as text that agents were expected to follow.

The roadmap's question for Wave 6: **Can AM detect its own structural problems?**

### Design Session (separate session, pre-build)

The Wave 6 proposal was drafted collaboratively. During that same session, two new governance documents were created to frame the work: [[AM — Integrity Layers]] (establishing the Mechanical/Semantic boundary) and [[AM — Tool Conventions]] (governing how tools must be built). These were approved before the proposal itself.

The design session also produced the [[Wave 7 — Brainstorm]] — a forward-looking conversation about what comes after Wave 6. This is relevant to the process analysis below.

### Build Session (separate session)

The build session delivered the full Wave 6 scope — not the minimum viable set, but the complete suite:

**Seven detection tools:**

| Tool | What it checks |
|------|---------------|
| `structure_check.sh` | Required folders, root files, pipeline CLAUDE.md files |
| `yaml_validation.sh` | YAML frontmatter parsing, required fields, controlled vocabulary, date formats |
| `broken_links.sh` | Wiki-link resolution in body text and frontmatter relationships |
| `orphan_detection.sh` | Every file reachable via at least one inbound link |
| `stub_detection.sh` | No empty files, no frontmatter-only or heading-only notes |
| `naming_validation.sh` | No duplicate filenames or titles, title-filename consistency |
| `inventory.sh` | Full vault manifest with type, status, authority weight, link counts |

**Supporting infrastructure:**

- `orchestrate.sh` — runs all tools in sequence, produces aggregate health report
- `config/defaults.conf` — generic Obsidian vault defaults
- `config/am.conf` — Agent Maestro-specific overrides
- `lib/config.sh` — shared bash library (config parsing, report helpers)
- `lib/yaml_validator.py` — Python YAML validation core
- `README.md` — complete documentation with config schema, invocation examples, architecture diagram

**Language strategy held:** Shell scripts for filesystem operations, Python for YAML parsing, uniform interface contract across both. The `yaml_validation.sh` wrapper maintains exit code consistency while delegating parsing to Python.

### First Health Report

The orchestrator ran against the AM vault and produced findings — exactly as intended. The whole point of Wave 6 is to find what humans can't see.

**Results:**

| Tool | Result |
|------|--------|
| Structure Check | CLEAN |
| YAML Validation | FINDINGS |
| Broken Links | FINDINGS |
| Orphan Detection | FINDINGS |
| Stub Detection | FINDINGS |
| Naming Validation | FINDINGS |
| Inventory | CLEAN |

**Nature of the findings:**

- **YAML validation:** 15 templates with empty date fields (expected — templates use placeholder values). 30+ archived files with schema v2 format (expected — pre-Wave-5 artifacts were archived without migration). These findings confirm the tools work correctly; they detect real non-compliance, even when the non-compliance is known and accepted.
- **Broken links, orphans, stubs, naming:** Findings concentrated in the archive. The active vault (governance, concepts, skills, pipeline folders) is substantially clean. The archive carries the historical debt of earlier waves.
- **Structure and inventory:** Clean. The vault skeleton and file manifest are intact.

The health report was filed in `05_RECORD/reports/`. Findings have not yet been categorised by Rob (critical/important/acceptable) per the proposal's Phase 2 specification. Remediation was explicitly out of scope for Wave 6.

### What Was Not Delivered

Two items from the proposal's completion criteria remain unchecked:

- **Wave 6 reflection written and filed in `06_REFLECT/`.** This document addresses that gap.
- **Capture seed for Wave 7 created in `01_CAPTURE/`.** The Wave 7 brainstorm exists but explicitly states it is not a capture seed. A proper capture seed — derived from this reflection — is needed.

## What We Learned

### About Agent Maestro

- **Mechanical integrity is a distinct and valuable layer.** The Integrity Layers distinction (mechanical vs. semantic) proved correct in practice. The tools found real issues that no amount of careful reading would reliably catch — particularly in the archive, where files accumulate silently. Scripts don't get bored, don't skip files, and don't assume things are fine because they were fine last time.
- **The archive is the biggest source of mechanical debt.** Pre-Wave-5 artifacts were archived without schema v3 migration. This was a deliberate choice (Law 3 — don't spend effort modernising artifacts that aren't active), but it means the health report will always show findings until a decision is made about archive compliance. This needs a policy decision: should archived files be exempt from schema validation, or should they be migrated? The answer probably belongs in the YAML validation config (exclude archived folders) or in a remediation wave.
- **Templates are a special case for validation.** Templates intentionally use empty placeholder values. The YAML validator correctly flags these as non-compliant. This is a known false positive that should be handled in config (exempting the templates folder) rather than weakening the validation rules.
- **The config model works.** The two-tier configuration (defaults + vault-specific overrides + CLI arguments) handled every case encountered during the build without becoming over-engineered. The config is readable, the schema is documented, and adding a new vault would mean writing one new `.conf` file.
- **04_EXECUTE is no longer empty.** This is symbolically significant. For the first time, AM has executable artifacts — code that does something. The vault is no longer purely a knowledge architecture; it has operational capability. This is the foundation that Wave 7 builds on.

### About the Process

- **The reflect stage is the most vulnerable step in the pipeline.** The build session delivered all technical artifacts but ended without reflecting. The proposal's own completion criteria listed the reflection as a gate requirement — and the gate wasn't passed. This is the most important process finding of Wave 6.
- **Why it happened: session boundaries don't respect pipeline stages.** Sessions end for practical reasons — context limits, fatigue, natural stopping points. The reflect stage sits at the end of the pipeline, which means it's the stage most likely to be cut when a session runs out of runway. There is no mechanical enforcement of the reflection gate. The tools we just built enforce structural rules; nothing enforces process rules.
- **The brainstorm created a false sense of completion.** The Wave 7 brainstorm was written during the design session, before Wave 6 was built. It looks and feels like forward-planning output from a reflection. But it isn't — it was speculative thinking that explicitly flagged itself as pending validation by the Wave 6 reflection. Its existence may have made the missing reflection feel less urgent. The brainstorm is a capture note, not a pipeline output.
- **Full scope was delivered without needing the degradation path.** The proposal defined a minimum viable set (four tools + config) and a full set (seven tools + orchestrator). The build session delivered everything. The scope degradation plan was good insurance that wasn't needed — which is the right outcome.
- **The Tool Conventions governance paid off immediately.** Every design decision during the build (exit codes, report format, read-only behaviour, config model) was already answered by the conventions document. The build session could focus on implementation rather than design decisions. Governance created before execution reduces friction during execution.

## What Comes Next

These items feed into the capture seed for Wave 7. They are consulted alongside the [[AM — Roadmap]] and [[AM — Future Waves Register]].

1. **Wave 7 — Scheduled Execution.** The roadmap's next committed wave. The question: "Can AM actually run things?" The [[Wave 7 — Brainstorm]] outlines a deliberately minimal scope: launchd schedules `orchestrate.sh`, reports land automatically, and optionally a thin Python script invokes an LLM to summarise findings. This brainstorm should now be validated against this reflection's findings and triaged into a formal proposal.

2. **Process gap: enforce the reflect stage.** The missing reflection is a pipeline integrity problem. Possible mitigations: a checklist in the session CLAUDE.md or pipeline CLAUDE.md that agents must confirm before closing; a mechanical check (does a reflection file exist for the current wave?); or a norm established in governance that the reflect stage is non-negotiable. This should be addressed before Wave 7 begins, not after.

3. **Health report triage.** The first health report findings need to be categorised by Rob (critical/important/acceptable). Key decisions: archive compliance policy (exempt or migrate?), template exemption in config, remediation scope and timing.

4. **Roadmap update.** The roadmap still describes Wave 7 as "build the runtime provider layer, implement scheduled execution (Python daemon or equivalent), establish the memory/persistence approach." The brainstorm and Future Waves Register both reflect the simplified scope. The roadmap should be updated to match once the Wave 7 proposal is finalised.

5. **Capture seed: "Tools Evolution."** A one-line capture note appeared in `01_CAPTURE/`: "What are the minimum viable or maximum safe set of tool suites for agent maestro?" This is a valid strategic question that should be triaged to the register.

## Process Reflection

Wave 6 followed the pipeline through five of six stages. Input (capture seed from Wave 5.2 reflection), Interpret (design session — proposal, governance documents), Decide (proposal approved), Act (build session — tools, orchestrator, health report), Record (health report filed, SYSTEM_MAP updated). The sixth stage — Reflect — was skipped.

This is the first time a wave has ended without completing the full pipeline. The irony is pointed: Wave 6 built tools to detect mechanical integrity failures, and the wave itself suffered a process integrity failure. The tools enforce vault rules; nothing enforces pipeline rules. That asymmetry is now visible.

The Wave 7 brainstorm, written in the design session before the build, muddied the pipeline sequence. Forward-looking design thinking is valuable, but it happened outside the pipeline's intended flow (reflect → seed → propose). The brainstorm correctly flagged itself as speculative and pending validation. This reflection now provides that validation: the brainstorm's conclusions hold. The simplified Wave 7 scope (launchd + optional LLM summary) is confirmed as the right approach. Nothing in the Wave 6 findings changes the direction.

**Recommendation:** Before beginning Wave 7, address the process gap. The reflect stage needs either mechanical enforcement or a governance-level norm that makes it non-negotiable. The cost of this reflection being late is manageable — we're writing it now, one session later. But the cost could compound if the pattern repeats for future waves, especially as AM moves toward autonomous operation where there is no human to catch the omission.

**Wave 6 is complete.**

---

*Filed in `06_REFLECT/`. A capture seed derived from this reflection should be placed in `01_CAPTURE/` to close the loop.*
