---
title: "AM — Future Waves Register"
type: governance
status: active
authority_weight: 60
schema_version: 3
created: "2026-03-16"
updated: "2026-03-17"
note: "Wave 8 restructured: 8.1 governance complete, 8.2 pipeline tooling ready for proposal, 8.3 git-ops registered, self-observation deferred"
relationships:
  derives_from:
    - "[[Agent Maestro — Strategy]]"
    - "[[AM — Roadmap]]"
  governs: []
  related:
    - "[[Agent Maestro — North Star]]"
tags: [register, strategy, backlog]
---

# AM — Future Waves Register

## Purpose

A living backlog of validated ideas that could become future waves. This register is the menu from which the [[AM — Roadmap|Roadmap]] selects. Ideas live here until they are promoted to the roadmap as a committed wave, or archived if they become irrelevant.

## Principle

The register is inclusive — every plausible idea gets a place. The roadmap is selective — only committed work appears there. The register feeds the roadmap; the roadmap does not feed the register. Ideas are grouped by the [[Agent Maestro — Strategy|Strategy]] stage they most naturally belong to, but may shift as understanding evolves.

---

## Stage 1 — Self-Governance

### Mechanical Integrity Layer (Wave 6 — promoted)

**Status:** Promoted to Roadmap. Proposal approved 2026-03-16. See [[Proposal — Wave 6 Mechanical Integrity]] in `03_DECIDE/active/`.

**Governance produced during design:** [[AM — Integrity Layers]] (establishes Mechanical/Semantic boundary), [[AM — Tool Conventions]] (governs how tools are built). Both in `02_KNOWLEDGE/governance/`.

**Related ideas resolved:**
- "Potential rule" → codified as [[AM — Integrity Layers]]
- "Agent responsibility collision" → simplified to two-layer model (Mechanical Integrity / Semantic Integrity) with future layers deferred until proven need

### Scheduled Execution (Wave 7 — promoted)

**Status:** Promoted to Roadmap. Proposal drafted 2026-03-16, adversarial audit complete. See [[Proposal — Wave 7 Scheduled Execution]] in `03_DECIDE/active/`.

**Final scope:** Three phases — (1) launchd scheduling `orchestrate.sh` via a wrapper script with date-stamped reports, (2) optional LLM summary via Ollama (llama3.2) appended to reports, (3) optional macOS native notification on findings. Local-first stack: no external API dependencies, no daemon, no framework.

Key insight: the problem isn't "how do we connect LLMs to AM?" (that's already solved — an LLM reads the vault). The problem is "how does AM do things when no human starts a session?" The minimum answer is: scheduled script execution via launchd.

**Deferred from original Wave 7 scope (validated ideas, not yet needed):**

- **Runtime Provider Layer** — LLM API abstraction layer. Deferred because a direct API call is sufficient when there's only one consumer. Revisit when multiple tools need LLM access with different requirements, or when provider-switching becomes operationally necessary.
- **Python daemon** — long-running background process for intelligent task chaining. Deferred because launchd handles simple scheduling without process management overhead. Revisit when Wave 8 introduces chained workflows where one step's output determines the next.
- **Memory architecture (SQLite, vector DB, RAG)** — deferred because the vault (~60 files) fits in context. Current memory model (markdown + YAML + CSV + git) is sufficient. SQLite is the right first step if cross-run data comparison proves necessary. Vector DB is a Stage 2 concern (needed when vault outgrows context window).
- **Model routing system** — deferred as a system. Simple three-tier approach adopted instead: Haiku-class for Level 1 (cheap/fast), Sonnet-class for Level 2 (standard), Opus-class for Level 3 (important). Pick one per tier, use them, measure later.
- **TOML with JSON for lower API fees** — deferred pending investigation of actual cost savings vs. added complexity.

### Pipeline Enforcement & Git-Ops (Wave 8 — partially promoted)

**Source:** Old roadmap Waves 6-7, Tools Evolution analysis (2026-03-17), Wave 6 process gap diagnosis

#### Wave 8.1 — Governance (promoted, complete)

**Status:** Complete. Produced [[AM — LLM Conventions]] and [[AM — Artifact Lifecycles]] as the governance prerequisite for pipeline enforcement tooling. Both adversarially audited and approved 2026-03-17.

#### Wave 8.2 — Pipeline Enforcement Tooling (next)

**Status:** Ready for proposal. The mechanical checks specified in [[AM — Artifact Lifecycles]] are the spec.

**Known mechanically checkable items (from Artifact Lifecycles — not exhaustive, the full document contains additional checks per artifact type):**

1. Every active proposal has a non-empty `## Audit` section
2. No proposal exists in `active/` with `status: draft`
3. Every completed wave has a reflection in `06_REFLECT/`
4. Every reflection has a corresponding capture seed in `01_CAPTURE/`
5. No concept has been in `status: draft` for more than 30 days without review
6. No capture item has been sitting untriaged for more than 14 days
7. Proposals are created in `proposals/` before appearing in `active/`

Additional checks from the full document include: reflection `derives_from` includes the wave's proposal, capture seed references the reflection, every active concept has non-empty `derives_from`, no proposal remains in `active/` after wave completion, governance documents have authority_weight ≥ 70 and complete schema v3 frontmatter.

**Proven need:** Wave 6 reflection was skipped and nothing detected it. Proposals have appeared in `active/` without audit.

#### Wave 8.3 — Git-Ops (needs design conversation)

**Status:** Registered. Needs its own design conversation before proposal.

AM-aware git enforcement — branch status, uncommitted changes, commit format validation, tag management. Proven friction: manual git operations in Cowork are irritating; Claude Code handles git natively but has no AM-aware rules.

### Self-Observation (deferred from original Wave 8 scope)

Self-observation instrumentation (timing, metrics, observation logging) and the self-assessment loop (observe → identify → propose → gate → execute/escalate) are valid future work but were descoped from Wave 8 to keep it focused on pipeline enforcement and git-ops. Revisit after Wave 8 is complete.

**Sub-capabilities (still valid, deferred):**
- Self-observation instrumentation (timing, metrics, observation_log.csv)
- Evolution capability (system observer, performance analyzer, improvement recommender)
- Governance validation of proposed changes (contract validator, architecture compliance, pipeline validator)
- Closed self-improvement loop with human escalation for high-stakes changes

### Operational Improvements (any wave)

**Source:** Various capture notes

- **Slack notifications** — message sent when new capture seeds, proposals, or reports are filed. Same function pattern for each. (Capture: "Message sent on new capture sees")
- **Capture seed → brief pipeline** — should every capture seed automatically produce a brief? Or is that overkill? (Capture: "Breifs")
- **Terminology refinement** — ✓ Resolved in Wave 5.2: "reflections" adopted, replacing "retrospectives." Folder, template, and all references updated.
- **Roles placement** — question whether roles should live in governance. Currently they do. (Capture: "Roles") — resolved in Wave 5.2: roles confirmed in `governance/roles/`.
- **Skills acquisition model** — building skills vs. acquiring from external marketplace. (Capture: "Skills")
- **Archived treatise rescue** — ✓ Resolved in Wave 5.2: treatise rescued to `02_KNOWLEDGE/concepts/AM — Treatise on Core Principles.md`, updated to schema v3.
- **Report lifecycle management** — daily integrity reports accumulate in `05_RECORD/reports/` (~365/year). At current scale this is manageable. Revisit when report count exceeds 500, or when cross-run trend comparison requires structured querying (at which point SQLite may also earn its place). Options: retention policy (archive reports older than N days), date-bucketed subfolders, or automated cleanup script. (Source: Wave 7 adversarial audit, IF-4)
- **Report-analytics tool suite** — cross-run comparison, trend analysis, diff between health reports. "Are broken links increasing or decreasing?" "Which tools consistently find issues?" This is where SQLite may first earn its place. Need not yet proven — requires accumulated daily reports from Wave 7. Revisit after 30+ daily reports exist. (Source: Tools Evolution analysis, 2026-03-17)

---

## Stage 2 — First External Application

### Generalized Audit Protocol (Wave 9 candidate)

**Source:** Old roadmap Wave 8.1

Extract AM's self-audit capability into a protocol for any vault or folder structure. Scan structure, identify patterns, assess quality and consistency, map relationships, produce findings and recommendations. This is the mechanical integrity layer plus semantic audit, generalized beyond AM's own schema.

### Discovery & Interview Workflow (Wave 10 candidate)

**Source:** Old roadmap Wave 8.2

Build a structured interaction workflow: ask clarifying questions, understand business/domain goals, identify pain points and existing structure, map needs to vault patterns, produce a design proposal. This is a consultative, human-in-the-loop pipeline type.

### External Vault Design & Implementation

**Source:** Old roadmap Wave 8.3

Given an audit report and discovery data: propose optimal structure, design governance, generate role and skill definitions, produce a deployment plan. Apply to Rob's business as the first real test case.

### Dual-Instance Evolution Model

**Source:** Rob, Wave 5.2 Phase 4 discussion

When Stage 2 begins, fork AM. One instance continues self-evolution (Stage 1 ongoing). A second instance is created for external application work. Both share foundational governance but evolve independently. Learnings cross-pollinate during reflections.

---

## Stage 3 — Replication

### Multi-Context Application

**Source:** Strategy Stage 3

Apply AM to multiple distinct businesses/domains. Discover what's universal methodology vs. context-specific. Refine and stabilize the approach.

### AM Starter Pack

**Source:** Capture — "Am basically starter pack"

A stripped-down, empty AM instance that guides an LLM to create the first agent, run the first instance, and start the evolution. A bootstrapping kit for new vaults. This could be the seed of a product offering.

---

## Stage 4 — Product

### Productization (form TBD)

**Source:** Strategy Stage 4

The exact form emerges from Stages 2-3. Possibilities include: consulting framework, educational package, starter pack product, SaaS platform, or some combination. Explicitly deferred until proven through replication.

---

## Explicitly Deferred

| Item | Why Deferred |
|------|-------------|
| Domain deployment (specific business agents) | Depends on Stage 2 being proven |
| Multi-vault agent networks | Depends on single external vault working first |
| AI system replication | Aspirational; requires Stage 3 at minimum |
| Portable agent OS | Premature; focus on one runtime first |

---

## How This Document Is Maintained

- **Adding items:** Capture notes that survive triage are added here, grouped by the Strategy stage they belong to. Items include source attribution (which capture note or discussion they came from).
- **Promoting items:** When a reflection identifies the next wave, the relevant register item is used to draft a proposal in `03_DECIDE/proposals/`. The register item is marked as promoted (not removed — it preserves the provenance).
- **Archiving items:** If an idea becomes irrelevant after two waves without promotion, it is a candidate for removal. Removed items are noted in the "Explicitly Deferred" table with a reason.
- **Reflection consultation:** Every wave reflection (Phase 6) reviews this register alongside the [[AM — Roadmap]] to inform what comes next.

## Related

- [[AM — Roadmap]]
- [[Agent Maestro — Strategy]]
- [[Agent Maestro — North Star]]
