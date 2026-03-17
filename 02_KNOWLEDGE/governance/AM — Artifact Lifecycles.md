---
title: "AM — Artifact Lifecycles"
type: governance
status: active
authority_weight: 70
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
    - "[[AM — Universal Workflow]]"
    - "[[AM — Integrity Layers]]"
  governs:
    - "[[AM — Future Waves Register]]"
    - "[[AM — Roadmap]]"
  related:
    - "[[AM — LLM Conventions]]"
    - "[[AM — Tool Conventions]]"
    - "[[Agent Maestro — Vault Rules]]"
tags:
  - governance
  - lifecycle
  - pipeline
  - process
  - gates
---

# AM — Artifact Lifecycles

## Purpose

Define the lifecycle rules for the primary artifact types in the Agent Maestro vault. Each lifecycle is an instance of the Irreducible Loop (Seed 1), and each transition between stages has a gate. This document specifies: what the stages are, what the gates check, what constitutes evidence of gate passage, and what is mechanically verifiable versus what requires semantic judgment. Artifact types not explicitly covered (skills, roles, templates, references, indexes) follow the Governance Document lifecycle for high-authority types and a minimal create/review/archive pattern for operational types.

This document is the bridge between [[AM — Universal Workflow]] (which defines the pattern) and the actual enforcement tooling (which verifies the pattern is followed). It answers the question: **what must happen, and how do we know it happened?**

## Principle

Every artifact in the vault has a lifecycle. That lifecycle follows the Irreducible Loop. Every transition between stages has a gate. Every gate leaves a trace. The intensity of the gate scales with the authority_weight of the artifact and the nature of the change.

Two layers enforce the gates: mechanical tools verify structural compliance (did the thing happen?), and LLM judgment assesses semantic quality (was it done well?). The mechanical layer is governed by [[AM — Tool Conventions]]. The semantic layer is governed by [[AM — LLM Conventions]]. This document defines the rules that both layers enforce, each on their side of the [[AM — Integrity Layers|Integrity Layers]] boundary.

---

## Artifact Lifecycles

### 1. Capture Item

**Location:** `01_CAPTURE/`

**Purpose:** Raw input — ideas, observations, questions, seeds. The entry point for anything new entering the vault. Captures are deliberately unstructured. They do not require YAML frontmatter, complete sentences, or any particular form. The only requirement is that they exist.

**Lifecycle:**

```
Created → Triaged → Routed → Referenced by destination
```

**Stages and gates:**

| Transition | Gate | Evidence |
|---|---|---|
| Created → Triaged | **Triage deadline:** capture items should be triaged within 14 days of creation. (14 days allows roughly two build waves to pass — long enough for context to accumulate, short enough to prevent indefinite accumulation.) | The item has been reviewed and a routing decision made. |
| Triaged → Routed | **Routing decision:** the item is sent to one of three destinations. | The destination artifact ([[AM — Future Waves Register]] entry, concept draft, or archive) exists. |
| Routed → Referenced | **Provenance link:** the destination artifact references the originating capture. For archive routing, the capture item's own `status: archived` is sufficient evidence — there is no separate destination artifact. | A wiki-link or relationship entry traces back to the capture item, or (for archive routing) the capture's archived status in `05_RECORD/archive/`. |

**Routing destinations:**

- **Future Waves Register** — the idea is valid. Add an entry to [[AM — Future Waves Register]] with source attribution. The register is the interpretation stage — ideas mature there before being promoted to proposals. Even urgent ideas pass through the register to preserve the interpretation step (Seed 3: no decision without interpretation).
- **Concept draft** — the idea names a reusable pattern or foundational concept not yet represented in the vault. Route to `02_KNOWLEDGE/concepts/` as a draft concept (see Concept lifecycle below).
- **Archive** — the idea has been absorbed, superseded, or is not relevant. Move to `05_RECORD/archive/`.

**Mechanical checks (pipeline enforcement):**

- Capture items older than 14 days that are not referenced by any [[AM — Future Waves Register]] entry, concept, reflection, or archive record.
- Capture items that have been routed but whose destination artifact does not link back.

**Semantic assessment:**

- Was the routing decision sound? Did the item end up in the right destination? (Alignment audit: does the routing serve the roadmap and the North Star?)

---

### 2. Proposal

**Location:** `03_DECIDE/proposals/` (draft) → `03_DECIDE/active/` (approved) → `05_RECORD/archive/` (completed)

**Purpose:** A commitment to action. Proposals specify what will be built, why, and how. They are the contract between the proposer and the approver.

**Lifecycle:**

```
Drafted in proposals/ → Audited → Approved → Promoted to active/ → Executed → Completed → Archived
```

**Stages and gates:**

| Transition | Gate | Evidence |
|---|---|---|
| Drafted | **Location check:** proposal must be created in `03_DECIDE/proposals/`, never directly in `active/`. | File exists in `proposals/` with `status: draft`. |
| Drafted → Audited | **Audit gate:** proposal is assessed using the three audit types ([[AM — LLM Conventions\|Alignment, Integrity, Viability]]). For waves that produce governance changes or architectural shifts, the adversarial lens is applied. | `## Audit` section within the proposal is non-empty and addresses all three audit types. |
| Audited → Approved | **Human approval:** the human reviews the audit findings and approves or rejects. | `status: draft` → `status: active` in frontmatter. Human's approval is recorded in the `## Audit` section. |
| Approved → Promoted | **Promotion:** proposal is moved from `proposals/` to `active/`. The corresponding entry in [[AM — Future Waves Register]] is marked as promoted. The [[AM — Roadmap]] wave description is updated to reference the proposal. | File exists in `active/` with `status: active`. File no longer exists in `proposals/`. Register entry marked "promoted." |
| Executed → Completed | **Completion check:** all deliverables specified in the proposal have been produced. | The proposal's completion criteria are met. A reflection exists for the wave (see Reflection lifecycle). |
| Completed → Archived | **Archive:** proposal is moved to `05_RECORD/archive/` with `status: archived`. | File exists in archive with `status: archived`. |

**Mechanical checks (pipeline enforcement):**

- No proposal exists in `active/` with `status: draft`.
- No proposal exists in `active/` without a non-empty `## Audit` section.
- Every active proposal has a corresponding reflection when the wave is marked complete.
- No proposal remains in `active/` after its wave is complete (should be archived).

**Semantic assessment:**

- **Alignment:** Does this proposal serve the roadmap and the North Star? Is it the right next step?
- **Integrity:** Are the phases internally consistent? Do the design decisions support each other? Are the traceability links to Foundations accurate?
- **Viability:** Does every phase earn its place? Could any phase be removed without loss? Is the scope appropriate — neither too large nor too small?
- **Adversarial (when applicable):** Assume the proposal is flawed. What would go wrong? What has been overlooked? What assumptions are untested?

---

### 3. Concept

**Location:** `02_KNOWLEDGE/concepts/` (draft or active)

**Purpose:** A named, reusable pattern or foundational idea that serves AM's governance and architecture and is not yet represented in the vault. If an existing concept already covers the territory, the right action is to evolve that concept, not create a new one. Concepts are high-value, low-volume — the vault maintains only the concepts that earn their place. Currently there are six.

**Lifecycle:**

```
Identified → Drafted in concepts/ → Reviewed → Promoted to active
```

**Stages and gates:**

| Transition | Gate | Evidence |
|---|---|---|
| Identified | **Origin:** the concept was identified through practice, not speculation. It emerged from a wave's work or a reflection's insight. | The originating reflection or wave artifact references the concept. |
| Identified → Drafted | **Draft creation:** concept is created in `02_KNOWLEDGE/concepts/` with `status: draft`. Must have proper schema v3 frontmatter including `derives_from` tracing to the Foundations. | File exists with `status: draft`. |
| Drafted → Reviewed | **Review gate:** a reviewer (not the author) assesses the concept using the three audit types. For new concepts, the adversarial lens is appropriate. | `## Audit` section within the concept is non-empty. |
| Reviewed → Active | **Promotion:** `status: draft` → `status: active`. | Status change in frontmatter. Concept is referenced by at least one other active document. |

**Concept promotion protocol:**

At the end of every wave, the reflection should ask: **did this wave surface any concepts strong enough for `02_KNOWLEDGE/concepts/`?** A concept earns promotion when:

- It was identified through practice, not speculation.
- It names something that would leave a gap if removed.
- It has clear relationships to existing governance or concepts.
- It has a defined purpose that serves the Foundations.

If a concept is identified, it is drafted during the reflection phase and reviewed by a different agent or in a different session (D6). The review applies all three audit types:

- **Alignment:** Does this concept serve the Foundations? Does it derive from a Seed, Law, or Derived Principle?
- **Integrity:** Is the definition clear and non-contradictory? Does it conflict with or duplicate existing concepts?
- **Viability:** If this concept were removed, would anything break? Is it actively needed, or is it speculative?

**Mechanical checks (pipeline enforcement):**

- No concept has been in `status: draft` for more than 30 days without review. (30 days allows roughly one full wave cycle for review to occur — generous enough that review isn't rushed, tight enough that drafts don't stagnate.)
- Every active concept has a non-empty `derives_from` relationship.
- Every concept created during a wave is referenced in that wave's reflection.

**Semantic assessment:**

- The three audit types as described above, applied during review.

---

### 4. Reflection

**Location:** `06_REFLECT/`

**Purpose:** Close the loop. A reflection evaluates what happened, what was learned, and what comes next. It is the feedback stage of the Irreducible Loop, and it always produces a capture seed that feeds the next cycle.

**Lifecycle:**

```
Wave/phase completes → Reflection filed → Capture seed created → Concept promotion check
```

**Stages and gates:**

| Transition | Gate | Evidence |
|---|---|---|
| Wave completes → Reflection filed | **Completion gate:** every completed wave must have a reflection in `06_REFLECT/`. | File exists with proper frontmatter. `derives_from` includes the wave's proposal. |
| Reflection filed → Capture seed created | **Seed gate:** every reflection must produce a capture seed in `01_CAPTURE/`. | A capture seed exists that references the reflection. |
| Reflection filed → Concept check | **Promotion check:** the reflection explicitly addresses whether any concepts emerged from the wave's work. | The reflection contains a section or statement addressing concept promotion (even if the answer is "no new concepts"). |

**Reflection quality guidelines:**

A reflection should address:

- **What happened:** narrative of the wave's work, key decisions, artifacts produced.
- **What was learned:** insights about AM, about the process, about the domain.
- **What comes next:** seeds for future work, identified gaps, proposed direction.
- **Whether the wave's original question was answered:** every wave in the roadmap asks a question. The reflection should answer it.

**Mechanical checks (pipeline enforcement):**

- Every completed wave has a corresponding reflection in `06_REFLECT/`.
- Every reflection has a corresponding capture seed in `01_CAPTURE/`.
- The reflection's `derives_from` includes the wave's proposal.
- The capture seed references the reflection.

**Semantic assessment:**

- **Alignment:** Does the reflection accurately serve the wave's stated purpose? Does it answer the wave's question?
- **Integrity:** Does the narrative match what actually happened? Are the lessons coherent?
- **Viability:** Is the reflection substantive — does it contain real insight — or does it merely satisfy the template?

---

### 5. Session Log

**Location:** `05_RECORD/logs/sessions/`

**Purpose:** Operational record of a working session. Session logs are leaf artifacts — they are produced, not referenced. They serve Law 2 (accountability) by recording what happened during each session.

**Lifecycle:**

```
Session begins → Log created → Session ends → Log filed
```

**Stages and gates:**

| Transition | Gate | Evidence |
|---|---|---|
| Session begins → Log created | **Session ID:** each session gets a unique ID (SES-XXX). | File exists with session ID in filename. |
| Session ends → Log filed | **Minimum content:** the log records what was done, what was decided, and any deferrals. | File is not empty. |

Session logs are lightweight operational artifacts. They do not require semantic audit. Their primary function is traceability — if a question arises about when or why something was decided, the session log provides the answer.

**Mechanical checks:**

- Session logs are exempt from orphan detection (leaf artifacts).
- Legacy session logs (pre-schema v3, specifically SES-002 through SES-008) are exempt from strict YAML validation. Future session logs should use schema v3 frontmatter but are validated at Level 1 intensity only.

**Semantic assessment:**

- None required for individual session logs. Session logs may be reviewed in aggregate as part of self-observation (future wave).

---

### 6. Report

**Location:** `05_RECORD/reports/`

**Purpose:** A structured summary produced by a tool or an LLM that captures the state of something at a point in time — vault health, wave progress, audit findings. Reports are reference artifacts: they are consumed by other work (reflections, audits, proposals) but are not themselves promoted or evolved.

**Lifecycle:**

```
Generated → Current → Superseded → Archived or overwritten
```

**Stages and gates:**

| Transition | Gate | Evidence |
|---|---|---|
| Generated → Current | **Existence:** the report was produced and saved to `05_RECORD/reports/`. | File exists in the reports folder. |
| Current → Superseded | **Newer report:** a subsequent report of the same type has been generated. | A newer report with the same scope exists. |
| Superseded → Archived | **Retention decision:** tool-generated health reports are ephemeral and may be overwritten. Manually-created reports (wave summaries, audit reports) that contain unique analysis should be archived to `05_RECORD/archive/` when superseded. | For ephemeral reports: overwritten in place. For archivable reports: moved to archive with `status: archived`. |

Reports come in two flavours. **Ephemeral reports** (tool-generated health reports, scan results) are overwritten each run and excluded from git — they serve the current session only. **Archivable reports** (manually authored wave summaries, audit reports) contain unique analysis and follow the standard archive path when superseded.

**Mechanical checks:**

- Reports are exempt from orphan detection (they are consumed, not linked to).
- Ephemeral reports are excluded from git tracking (`.gitignore`).

**Semantic assessment:**

- None required for ephemeral reports. Archivable reports may be reviewed as part of the Finishing Ritual if they inform the reflection.

---

### 7. Governance Document

**Location:** `02_KNOWLEDGE/governance/`

**Purpose:** Constitutional documents that define how AM operates. High authority_weight (≥ 70). Changes are always Level 3 — human approval required.

**Lifecycle:**

```
Need identified → Drafted → Reviewed → Human approved → Active → Evolved through proposals
```

**Stages and gates:**

| Transition | Gate | Evidence |
|---|---|---|
| Need identified | **Provenance:** the need for a new governance document is identified in a reflection, proposal, or conversation. | The originating artifact references the need. |
| Drafted → Reviewed | **Full audit:** all three audit types applied with adversarial lens. | `## Audit` section with thorough assessment. |
| Reviewed → Approved | **Human approval (Level 3):** governance documents always require human sign-off. | Human approval recorded. `status: draft` → `status: active`. |
| Active → Evolved | **Change trail:** modifications to active governance are proposed, discussed, and approved before being made. | Git history provides the change trail. For major changes, a proposal or the session log documents the rationale. |

**Mechanical checks:**

- All governance documents have authority_weight ≥ 70.
- All governance documents are in `02_KNOWLEDGE/governance/`.
- All governance documents have complete schema v3 frontmatter.

**Semantic assessment:**

- **Alignment:** Does this governance document serve the Foundations? Can every rule be traced upward to a Seed, Law, or Derived Principle?
- **Integrity:** Is it internally consistent? Does it conflict with other governance documents? When documents conflict, does the higher authority_weight win?
- **Viability:** Is every section earning its place? Has practice evolved past any of the rules?

---

## The Gate Principle

All gates in this document follow a single principle from the Foundations:

> **Seed 3 (Constraint):** No execution without routing. No routing without validation. No validation without schema. No schema without definition. No definition without design intent.

The gates are not bureaucracy. They are the Constraint seed made operational. Each gate exists because skipping it has caused — or would cause — a real problem. The proposal lifecycle gate exists because a proposal once bypassed audit and went directly to `active/`. The reflection gate exists because a wave once completed without a reflection. The capture triage gate exists because ideas can sit indefinitely without being processed.

When a gate feels too heavy, the answer is not to remove it — it is to reduce its intensity to match the escalation level. A Level 1 gate is a simple mechanical check. A Level 3 gate is a thorough audit with human approval. The pattern is always the same; only the intensity varies.

---

## Finishing Rituals

Certain lifecycle transitions cluster together at the end of a wave. These form a **finishing ritual** — a checklist that ensures the loop closes completely:

1. **Reflection filed** in `06_REFLECT/` — addresses what happened, what was learned, what comes next, and whether the wave's question was answered.
2. **Capture seed created** in `01_CAPTURE/` — the reflection's seeds become the next cycle's input.
3. **Concept promotion check** — did this wave surface any concepts strong enough for `02_KNOWLEDGE/concepts/`? If yes, draft them. If no, note it in the reflection.
4. **Proposal archived** — the completed wave's proposal is moved from `active/` to `05_RECORD/archive/` with `status: archived`.
5. **Consumed artifacts archived** — brainstorms, intermediate drafts, and other pipeline artifacts that were consumed during the wave are moved to archive.
6. **Roadmap updated** — the completed wave is marked with ✓ in [[AM — Roadmap]] and its outcome is summarized.
7. **SYSTEM_MAP updated** — the vault inventory reflects the current state. Mandatory when the wave changes vault structure, adds or removes documents, or reorganizes content ([[Agent Maestro — Vault Rules|Vault Rule 22]]); standard practice otherwise.

Not every wave requires all seven steps (Law 3), but the first four are mandatory for every wave. Steps 5–6 are standard practice. Step 7 is conditional (see above).

---

## Relationship to Other Governance

**Authority chain:** [[Agent Maestro — Foundations]] → [[AM — Universal Workflow]] → **AM — Artifact Lifecycles** → pipeline enforcement tooling.

This document defines *what must happen* in each lifecycle. [[AM — LLM Conventions]] defines *how* the LLM performs the semantic assessment at each gate. [[AM — Tool Conventions]] defines *how* the tools perform the mechanical checks. [[AM — Universal Workflow]] defines the underlying pattern that all lifecycles instantiate.

The mechanical checks listed in this document are the specification for pipeline enforcement tooling (Wave 8). The semantic assessments are the specification for LLM behavior during reviews and audits.

## When It Applies

When creating, reviewing, promoting, archiving, or assessing any artifact in the vault. When designing pipeline enforcement tools. When performing the finishing ritual at the end of a wave. When triaging capture items.

## Related

- [[Agent Maestro — Foundations]] — the kernel (Seed 1: Process, Seed 3: Constraint)
- [[AM — Universal Workflow]] — the pattern this document instantiates for specific artifact types
- [[AM — LLM Conventions]] — governs the semantic assessment at each gate
- [[AM — Tool Conventions]] — governs the mechanical checks at each gate
- [[AM — Integrity Layers]] — the architectural separation between mechanical and semantic enforcement
- [[Agent Maestro — Vault Rules]] — the structural rules that mechanical checks enforce
- [[AM — Roadmap]] — updated as part of the finishing ritual
