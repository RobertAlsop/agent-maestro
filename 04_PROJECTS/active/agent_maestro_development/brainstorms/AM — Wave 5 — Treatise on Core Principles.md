---
schema_version: 2
title: "AM — Wave 5 — Treatise on Core Principles"
type: treatise
note_class: planning
domain: agent_maestro
layer: projects
authority_weight: 65
resolution_basis: authority_weight
status: active
review_status: draft
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
owner: AgentMaestro
source_type: collaborative
relationships:
  defines:
    - "[[Foundational Elements]]"
  part_of:
    - "[[Agent Maestro — Evolution Roadmap v0.5.0]]"
  implements: []
  governs: []
  applies_to: []
  uses:
    - "[[Agent Maestro — Principles]]"
    - "[[Agent Maestro — North Star]]"
    - "[[AM — Wave 5 — Foundational Brainstorm]]"
  produces:
    - "[[Agent Maestro — Foundations]]"
  supersedes: []
  superseded_by: []
tags:
  - treatise
  - foundations
  - principles
  - wave-5
  - governance
hash: ""
---

# Agent Maestro v0.5 — Treatise on Core Principles

**Date**: 2026-03-15
**Authors**: Rob + Claude (Opus)
**Purpose**: Establish the irreducible kernel of Agent Maestro. Reconcile all principle frameworks into a unified foundation. Resolve open threads from the Foundational Brainstorm. Produce the intellectual basis for `Agent Maestro — Foundations.md`.

---

## 1. The Problem This Treatise Solves

Agent Maestro currently has 12 principles organized in three tiers, plus several additional frameworks identified during the v0.5 brainstorm (the Irreducible Loop, Seven Essential Primitives, Core System Law, authority descent chain, Seven Types of Authority, System Genesis, and a 10-level authority hierarchy). These frameworks overlap, operate at different levels of abstraction, and have never been formally reconciled.

Before Agent Maestro can consolidate its vault (Wave 5), formalize templates, or apply its governance model to external systems (Wave 8), the foundational layer must be unified. This treatise performs that unification.

---

## 2. The Kernel

The Foundational Brainstorm established seven candidate foundational elements through structured interview. This treatise examines each in detail, tests them for completeness, and refines where necessary.

### 2.1 Three Seeds

Seeds are the mechanics of any operational intelligence system. They answer the three fundamental questions: how does work flow, what must be present, and what must be obeyed.

#### Seed 1 — Process (The Irreducible Loop)

```
perception → interpretation → decision → action → memory → feedback
```

Every operation follows this loop. At the vault level: observe state → analyze meaning → decide on action → execute → record outcome → learn. At the agent level: receive input → interpret context → choose action → attempt action → log result → report back. At the document level: gather input → structure analysis → reach conclusions → propose actions → record for future → identify next questions.

**What this seed governs**: Sequencing, lifecycle, workflow design, pipeline structure, session protocol. Any process in Agent Maestro that has stages derives its stages from this loop (or a subset of it).

**Fractal instances already in Agent Maestro**:

| Level | Perception | Interpretation | Decision | Action | Memory | Feedback |
|-------|-----------|---------------|----------|--------|--------|----------|
| Build session | Input | Brief | Proposal + Audit | Build | Summary + Log | Brainstorm |
| Project lifecycle | Brief | Proposal | Contract | Build | Summary | Brainstorm |
| Agent execution | Observe state | Interpret context | Choose action | Attempt action | Log result | Self-observe |
| Governance cycle | Monitor vault | Assess alignment | Approve/reject | Apply changes | Update registries | Audit |

**The validation gate**: Between interpretation and decision, there is always a validation checkpoint. In the build session, this is the adversarial audit. In agent execution, this is the permission check. In governance, this is the escalation check. The gate is not a separate stage — it is a property of the decision stage: no decision proceeds without validation.

#### Seed 2 — Structure (The Essential Primitives)

Every system component must have or serve seven primitives:

| Primitive | Question | Example at vault level | Example at note level |
|-----------|----------|----------------------|----------------------|
| **State** | What is true right now? | Current vault inventory, health metrics | Current frontmatter values |
| **Goal** | What is this trying to achieve? | North Star declaration | Note's stated purpose |
| **Policy** | What is allowed or forbidden? | Authority packs, governance docs | Authority weight, review status |
| **Memory** | What from the past informs the present? | Session logs, state change log, knowledge graph | Relationships, references, version history |
| **Tools** | What actions can be taken? | Tool registry, shell scripts, MCP adapters | Edit, archive, promote, link |
| **Control** | Who decides and who can stop? | Escalation rules, human gates | Approval requirements, ownership |
| **Feedback** | How do we know if it worked? | Observation logs, audit reports | Validation results, audit verdicts |

**What this seed governs**: Templates, schemas, frontmatter design, component architecture. Any template in Agent Maestro should ensure its instances address all seven primitives (or explicitly note which are not applicable and why).

**Relationship to the Irreducible Loop**: The seven primitives and the six loop stages are not independent. State feeds Perception. Goal drives Interpretation. Policy constrains Decision. Tools enable Action. Memory records outcomes. Feedback closes the loop. Control governs the entire cycle. The two seeds are complementary views of the same system — Process is the temporal view (how things flow), Structure is the spatial view (what must be present).

#### Seed 3 — Constraint (The Authority Hierarchy)

From highest authority to lowest, every action must pass through a chain of constraint:

| Level | What it defines | Violation consequence |
|-------|----------------|----------------------|
| 1. Design intent | Why does this system exist? | System has no purpose — everything below is arbitrary |
| 2. Definition | What are the named things? | Components are ambiguous — cannot be governed |
| 3. Schema | What shape must they take? | Instances are unpredictable — cannot be validated |
| 4. Validation | Does this instance conform? | Non-conforming instances enter the system — integrity fails |
| 5. Routing | Where does this action go? | Actions reach wrong handlers — unpredictable behavior |
| 6. Execution | The action itself | Action fails or produces wrong outcome |

**The chain rule**: No level may bypass the one above it. Execution without routing is uncontrolled. Routing without validation is unsafe. Validation without schema is arbitrary. Schema without definition is meaningless. Definition without design intent is purposeless.

**What this seed governs**: Permission checking, authority pack design, escalation rules, the compiler pipeline, governance document hierarchy. Every authority_weight in the vault is an expression of this hierarchy — higher weight means closer to design intent.

### 2.2 One Meta-Principle

#### Fractal Design

*Every layer of Agent Maestro is built from the same fundamental principles, applied at different levels of abstraction.*

This is not decoration. It is the mechanism by which Agent Maestro achieves its strategic target. When the consolidation process used on this vault IS the consolidation process offered to external vaults, internal development IS external capability building. When the build session protocol used by a human and Claude IS the protocol an autonomous constellation follows, human-assisted work IS the training ground for autonomous work.

Fractal Design implies:

- **Composability**: If the same pattern exists at every level, components at one level can be recombined at another. An agent template works for any agent. A pipeline template works for any pipeline. An audit template works at any scale.
- **Reflexivity**: The system can apply its own patterns to itself. Agent Maestro can audit Agent Maestro using Agent Maestro's audit tools. This is not circular — it is the definition of self-governance.
- **Portability**: Patterns proven at one level transfer to others without redesign. The three audit types (Alignment, Integrity, Viability) work on a single note, a constellation, or an entire vault.

### 2.3 Three Laws

Laws are universal constraints. Unlike seeds (which describe mechanics) or the meta-principle (which describes design philosophy), laws are rules that must always hold. Violating a law means the system is broken.

#### Law 1 — Direction of Authority

*Purpose descends; accountability ascends.*

Every component's purpose is defined by and in service to the layer above it. The vault serves the human. The constellation serves the vault. The agent serves the constellation. The pipeline serves the workflow that invokes it. At the top, the North Star declares the human's intent. At every other level, purpose is received, not generated.

Accountability flows in the opposite direction. Agents report to constellations. Constellations report to the vault. The vault reports to the human. Escalations ascend. Logs ascend. Audit findings ascend.

**Why this is a law, not a seed**: The seeds describe mechanics that exist at every level. This law describes the *direction* in which those mechanics operate. You could build a system with all three seeds and still have it broken if purpose flows sideways or accountability doesn't reach the top.

**Subsumes existing Principle 2** (Authority Over Intelligence) — "authority matters more than the model" is a specific case of purpose descending through the authority hierarchy.

**Subsumes existing Principle 7** (Human Escalation Pattern) — "humans hold final authority on irreversible actions" is a specific case of accountability ascending to the top of the hierarchy.

#### Law 2 — Action Properties

*All actions must be verifiable, reversible, and accountable.*

- **Verifiable**: Every action can be observed and confirmed. No invisible mutations. No hidden state changes. Logging is not optional.
- **Reversible**: Every action can be undone (or its effects can be recovered from). Archive over delete. Checkpoint before destructive changes. Version control as standard.
- **Accountable**: Every action has an attributed source. No anonymous modifications. Every state change log entry has an agent_id, timestamp, and rationale.

**Why this is a law**: These three properties are the minimum conditions for a governed system. Without verifiability, you cannot audit. Without reversibility, you cannot recover from errors. Without accountability, you cannot trace cause to effect. Remove any one and the system is ungovernable.

**Subsumes existing Principle 4** (Transparency by Design) — "all system actions must be observable and auditable" is the verifiability property.

**Subsumes existing Principle 9** (Evidence Over Assumptions) — "behaviour validated through events and outcomes" is a consequence of verifiability applied to system evaluation.

#### Law 3 — Economy

*Only what is necessary.*

Every component must earn its place. If a principle can be merged with another without loss, merge it. If a pipeline has no consumer, archive it. If a note duplicates knowledge held elsewhere, remove the duplicate. If an agent has no defined purpose, it should not exist.

This law operates at every level: principles (are all 12 needed?), documents (does every note earn its place?), pipelines (are all 7 used?), agents (does every agent have work?), fields (does every frontmatter field serve a purpose?), folders (does every folder contain necessary content?).

**Why this is a law, not a meta-principle**: A meta-principle guides design thinking. A law constrains outcomes. Economy is not a suggestion to "try to keep things lean" — it is a hard rule that everything must justify its existence. The consolidation audit (Wave 5) is the enforcement mechanism for this law.

**Subsumes existing Principle 10** (Real Systems First) — "theory validated in real operational environments only" is Economy applied to validation — don't build theoretical systems.

**Subsumes existing Principle 12** (Anti-Agent-Sprawl) — "every agent must have defined purpose, authority, and outcomes" is Economy applied to agent design.

---

## 3. Reconciliation of All Frameworks

### 3.1 The Seven Types of Authority

Rob's framework identifies seven types of authority: Governance, Execution, Decision, Operation, Conception, Memory, Interface.

**Analysis**: These are instantiations of the Constraint seed at the organizational level. They answer: "What kinds of authority does a governed system need?" Each maps to a specific domain of the authority hierarchy:

| Authority Type | What it governs | Constraint seed level |
|---------------|----------------|----------------------|
| Conception | Design intent — why things exist and what shape they take | Levels 1–2 (Design intent, Definition) |
| Governance | Policy — what rules apply system-wide | Level 3 (Schema) |
| Decision | Judgment calls — approval, rejection, escalation | Level 4 (Validation) |
| Operation | Day-to-day execution within established patterns | Levels 5–6 (Routing, Execution) |
| Execution | Direct action on the system | Level 6 (Execution) |
| Memory | What is remembered and how | Structure seed — Memory primitive |
| Interface | How the system communicates with external systems and humans | Structure seed — Tools + Feedback primitives |

**Recommendation**: The Seven Types of Authority are a useful *classification system* for authority packs and agent roles, but they are not foundational elements. They are derived from the Constraint seed and Structure seed. They should exist as a reference document in `02_KNOWLEDGE/concepts/` — useful for designing authority packs and constellations, but not part of the kernel.

**Possible simplification**: Seven types may be more than necessary. Operation and Execution overlap. Conception could fold into Governance (design intent IS a governance concern). A minimum viable set might be four: Governance (policy + design), Decision (judgment), Execution (action), and Memory (knowledge). Interface is arguably a tool concern, not an authority type. This simplification should be tested during the governance body review in Wave 5.

### 3.2 The 10-Level Authority Hierarchy

Rob's framework: Root Principle → Kernel Invariants → Structural Law → Schema Law → Process Law → Policy Law → Routing Law → Tools → Runtime → Tests.

**Analysis**: This is the Constraint seed expanded to maximum resolution. The Constraint seed's 6 levels (Design intent → Definition → Schema → Validation → Routing → Execution) capture the essential chain. The 10-level version adds finer distinctions (separating Structural Law from Schema Law, splitting Process Law from Policy Law, distinguishing Tools from Runtime from Tests).

**Recommendation**: The 6-level version belongs in the kernel (Constraint seed). The 10-level version is a detailed reference for implementors who need to make fine-grained authority decisions. It should exist as a reference in `02_KNOWLEDGE/concepts/` — an expanded view of the Constraint seed, useful when designing complex authority hierarchies, but not required for everyday governance.

### 3.3 System Genesis

Rob's framework: Possibility → Instantiation → Observation.

**Analysis**: This describes how systems come into being, not how they operate. The three seeds describe operating systems. System Genesis describes the moment before operation begins — the transition from "this system could exist" to "this system does exist" to "we can see what this system is doing."

**Recommendation**: System Genesis is a *lifecycle concept*, not a foundational element. It sits naturally in the Evolution Constellation's knowledge base (Wave 7) — the constellation that observes, assesses, and proposes improvements needs to understand how systems are born. For now, it should be noted as a concept in `02_KNOWLEDGE/concepts/` but does not enter the kernel.

Interestingly, System Genesis maps to the first three stages of the Irreducible Loop: Possibility ≈ Perception (seeing that something could exist), Instantiation ≈ Decision + Action (choosing to create it and creating it), Observation ≈ Feedback (seeing what it does). This is the Loop applied to system creation rather than system operation — another fractal instance.

### 3.4 The Authority Descent Chain

Rob's framework: no execution without routing → no routing without validation → no validation without schema → no schema without definition → no definition without design intent.

**Analysis**: This IS the Constraint seed, stated as a chain of negations. Each "no X without Y" corresponds to a level in the hierarchy. The chain form is actually more powerful than the hierarchy form for runtime enforcement — it gives you a checklist: before executing, check routing. Before routing, check validation. And so on.

**Recommendation**: Both forms (hierarchy and chain) should exist in Foundations.md. The hierarchy is the structural view (for designers). The chain is the operational view (for runtime enforcement). Same seed, two representations.

---

## 4. The Principle Merge Strategy

### 4.1 How the Existing 12 Are Absorbed

The seven foundational elements absorb all 12 existing principles. No principle is lost — each is either elevated (became a seed, law, or meta-principle), subsumed (its content is expressed more precisely by a foundational element), or retained as a derived principle (still useful at the operational level but now explicitly derived from the kernel).

| # | Existing Principle | Disposition | Absorbed By |
|---|---|---|---|
| 1 | Governance Before Autonomy | **Elevated** — became the validation gate in the Process seed | Seed 1 (Process) + Seed 3 (Constraint) |
| 2 | Authority Over Intelligence | **Elevated** — became Law 1 (purpose descends) | Law 1 |
| 3 | Deterministic Control Surfaces | **Retained as derived** — operationalizes the Control primitive | Seed 2 (Structure — Control) |
| 4 | Transparency by Design | **Elevated** — became the verifiability property in Law 2 | Law 2 |
| 5 | Intelligence Through Constraints | **Elevated** — this IS Seed 3 stated as a design philosophy | Seed 3 (Constraint) |
| 6 | Three-Layer Memory Model | **Retained as derived** — operationalizes the Memory primitive for this specific vault | Seed 2 (Structure — Memory) |
| 7 | Human Escalation Pattern | **Elevated** — became a specific case of Law 1 (accountability ascends to human) | Law 1 |
| 8 | Composable Architecture | **Elevated** — became an implication of Fractal Design | Meta-principle (Fractal Design) |
| 9 | Evidence Over Assumptions | **Elevated** — became a consequence of Law 2 (verifiability) | Law 2 |
| 10 | Real Systems First | **Subsumed** — Economy applied to validation | Law 3 |
| 11 | Controlled Evolution Pattern | **Retained as derived** — operationalizes the feedback stage + constraint seed for system changes | Seed 1 (Process — feedback) + Seed 3 |
| 12 | Anti-Agent-Sprawl | **Subsumed** — Economy applied to agent design | Law 3 |

### 4.2 Proposed New Principle Set

The kernel (3 seeds + 1 meta-principle + 3 laws = 7 elements) is the foundational layer. Below it, a small set of **derived principles** operationalize the kernel for Agent Maestro specifically. These are the principles that tell you how to apply the kernel in practice.

**Proposed derived principles** (candidates — to be confirmed during Wave 5 governance review):

| # | Derived Principle | Derives From | What it operationalizes |
|---|---|---|---|
| D1 | **Deterministic Control Surfaces** | Seed 2 (Control) + Law 2 (verifiable) | Agent actions must be reproducible, traceable, and explainable. The Control primitive is implemented through deterministic interfaces, not probabilistic ones. |
| D2 | **Three-Layer Memory Model** | Seed 2 (Memory) | Knowledge is organized in three layers: Knowledge Graph (structured relationships), Vector Memory (semantic search), Structured Data (CSV, registry). Each layer has distinct responsibilities. |
| D3 | **Controlled Evolution** | Seed 1 (feedback) + Seed 3 (Constraint) | System changes proceed through graduated experiments within governance. No jumps. Evolution is a governed process, not an uncontrolled mutation. |
| D4 | **Human Sovereignty** | Law 1 (purpose descends) | Humans hold final authority at the top of every authority chain. No autonomous action may be irreversible without human approval. Escalation to human is always available. |
| D5 | **Governance Before Autonomy** | Seed 3 (Constraint) + Seed 1 (validation gate) | No system capability is deployed without governance being in place first. Govern, then operate, then scale. Never the reverse. |

**Five derived principles**, down from twelve. Each is explicitly traced to its foundational element. Each does unique work that the kernel alone doesn't make specific enough.

**What was removed and why**:

| Removed | Why |
|---------|-----|
| Authority Over Intelligence (#2) | Fully elevated to Law 1. The law is stronger and more precise. |
| Transparency by Design (#4) | Fully elevated to Law 2. "Verifiable" is more precise than "transparent." |
| Intelligence Through Constraints (#5) | Fully elevated to Seed 3. The seed IS this principle, universalized. |
| Composable Architecture (#8) | Fully elevated to Fractal Design implication. Composability follows necessarily from fractal self-similarity. |
| Evidence Over Assumptions (#9) | Fully elevated to Law 2 consequence. If all actions are verifiable, evidence is the default. |
| Real Systems First (#10) | Subsumed by Law 3. "Only what is necessary" implies "don't build what isn't real." |
| Anti-Agent-Sprawl (#12) | Subsumed by Law 3. "Only what is necessary" applied to agents specifically. |

### 4.3 The Complete Hierarchy

```
┌─────────────────────────────────────────────────┐
│              FOUNDATIONAL KERNEL                 │
│                                                  │
│  Seeds:         Process · Structure · Constraint │
│  Meta-principle: Fractal Design                  │
│  Laws:          Direction · Properties · Economy │
│                                                  │
│  (7 elements — irreducible)                      │
├─────────────────────────────────────────────────┤
│           DERIVED PRINCIPLES                     │
│                                                  │
│  D1. Deterministic Control Surfaces              │
│  D2. Three-Layer Memory Model                    │
│  D3. Controlled Evolution                        │
│  D4. Human Sovereignty                           │
│  D5. Governance Before Autonomy                  │
│                                                  │
│  (5 principles — each traced to kernel)          │
├─────────────────────────────────────────────────┤
│        OPERATIONAL PATTERNS                      │
│                                                  │
│  Authority packs, pipeline contracts,            │
│  templates, audit checklists, agent configs      │
│                                                  │
│  (Many — all derived from above)                 │
└─────────────────────────────────────────────────┘
```

This three-level structure is itself fractal: kernel constrains principles, principles constrain patterns, patterns constrain instances. Purpose descends through the levels (Law 1). Each level is the minimum viable expression of the one above it (Law 3). The same structure appears at every abstraction level in the vault (Fractal Design).

---

## 5. Testing the Kernel for Completeness

### 5.1 The Mission Test

Agent Maestro's mission: **designing, governing, and evolving operational intelligence systems**.

| Mission verb | Kernel coverage |
|---|---|
| **Designing** | Seed 2 (what to include) + Seed 1 (how it flows) + Seed 3 (what constrains it) + Fractal (apply same pattern everywhere) + Law 3 (minimum viable) = complete design toolkit |
| **Governing** | Seed 3 (authority hierarchy) + Law 1 (direction of authority) + Law 2 (action properties) + three audit types (Alignment, Integrity, Viability) = complete governance toolkit |
| **Evolving** | Seed 1 (feedback loop) + Fractal (self-application) + Law 2 (reversible) + D3 (controlled evolution) = complete evolution toolkit |

**Verdict**: The kernel covers the mission.

### 5.2 The Who/What/How/Why/Where/When Test

| Question | Kernel element | Coverage |
|---|---|---|
| **Why** | Law 1 (purpose descends from North Star) + Seed 2 (Goal primitive) | ✓ |
| **What** | Seed 2 (Structure — what must exist) | ✓ |
| **How** | Seed 1 (Process — how work flows) + Seed 3 (Constraint — how behavior is governed) | ✓ |
| **Who** | Seed 3 (authority hierarchy defines who is permitted) + Law 1 (accountability traces to whom) | ✓ |
| **Where** | Seed 2 (Structure) × Fractal (same pattern at every level) → generates organizational layout | ✓ |
| **When** | Seed 1 (Process defines sequence) + Seed 3 (Constraint defines gates/conditions) | ✓ |

**Verdict**: No gaps.

### 5.3 The Adversarial Test

Can the kernel be gamed or bypassed?

**Attack 1**: "I'll follow the Loop but skip the validation gate." → Seed 3 (Constraint) prevents this: no execution without validation. Law 2 makes the bypass observable (verifiable). D5 (Governance Before Autonomy) makes this a governance violation.

**Attack 2**: "I'll claim everything is necessary to avoid Economy pruning." → Law 3 is enforceable through the Viability audit. "Necessary" is measured against the Goal primitive (Seed 2): does this component serve its goal? If the answer requires sophistry, it fails.

**Attack 3**: "I'll create a self-referential governance loop where the system approves its own changes." → Law 1 prevents this: purpose descends from the human. The top of every authority chain is a human. D4 (Human Sovereignty) makes this explicit.

**Attack 4**: "I'll add a new foundational element to the kernel." → The kernel is protected by Law 3 (only what is necessary) and by its own Constraint seed (changes to design intent — level 1 — require the highest authority). Adding to the kernel is a governance-level decision requiring human approval.

**Verdict**: The kernel is defensible. Not invulnerable (no system is), but the attack surface is small and each attack has a clear defense.

### 5.4 Are There Missing Laws?

The brainstorm identified "three laws" but noted Rob suspected there may be more. Let me examine candidates:

**Candidate: "No action without permission"** — This is already covered by Seed 3 (Constraint hierarchy) + Law 1 (purpose/authority descends). The authority hierarchy IS the permission system.

**Candidate: "All changes must be logged"** — This is a specific case of Law 2 (verifiable + accountable). If all actions are verifiable and accountable, logging is the mechanism. The law is more fundamental than the mechanism.

**Candidate: "The system must be observable"** — Again, covered by Law 2 (verifiable). Observability is how verifiability is implemented.

**Candidate: "Governance must be self-consistent"** — This is what the Integrity audit checks. It's an operational requirement derived from Seed 3 (the constraint hierarchy must be internally coherent), not a separate law.

**Verdict**: Three laws appear sufficient. Additional candidates are either covered by existing elements or are operational patterns derived from the kernel. If a fourth law emerges during Wave 5 implementation, Law 3 (Economy) ensures we only add it if it's truly necessary.

---

## 6. Implications for Agent Maestro Architecture

### 6.1 Template Strategy

Every template in Agent Maestro should embed the relevant primitives from Seed 2 (Structure). The minimum viable template set, in priority order:

| Template | Embeds | Priority | Rationale |
|----------|--------|----------|-----------|
| **Note template** | All 7 primitives via frontmatter fields | Highest | Every note is an instance of the Structure seed |
| **Pipeline template** | Loop stages (Seed 1) + entry/exit conditions (Seed 3) | High | Every pipeline is an instance of the Process seed |
| **Project template** | 6 subfolders (Loop-mapped) + artifact templates | High | Every project follows the Loop lifecycle |
| **Audit template** | 3 audit types + checklists + severity scales | High | Every audit applies the same three checks |
| **Agent template** | 7 primitives + authority pack reference + escalation rules | Medium | Every agent is a Structure seed instance with Constraint bindings |
| **Brainstorm template** | Loop structure (P→I→D→A→M→F) | Medium | This treatise and the brainstorm before it model the format |
| **Authority pack template** | Constraint hierarchy levels + permission matrix | Medium | Every authority pack is a Constraint seed instance |

### 6.2 Audit Taxonomy (Confirmed)

Three audit types, each checking a different relationship:

| Audit | Direction | Question | Checks |
|-------|-----------|----------|--------|
| **Alignment** | Top-down | Does this serve what's above it? | Law 1, Seed 3 |
| **Integrity** | Horizontal | Is this internally sound? | Seed 2 (all primitives present), Seed 1 (loop completes) |
| **Viability** | Bottom-up | Is this earning its place? | Law 3 |

The adversarial method (assume it's wrong, try to prove it) is applied within any of the three types. It is a lens, not a type.

### 6.3 Build Session Protocol

The brainstorm proposed a 10th stage (Brainstorm / Forward Look). With the treatise's analysis, the full Build Session Protocol maps to the Irreducible Loop:

| Loop Stage | Protocol Stage(s) | Stage # |
|---|---|---|
| Perception | Input | 1 |
| Interpretation | Brief / Roadmap | 2 |
| Validation gate | Proposal + Adversarial Audit | 3, 4 |
| Decision | (Human approval — between 4 and 5) | — |
| Action | Build | 5 |
| Memory | Output Summary + Workflow Extraction + Session Log + Git | 6, 7, 8, 9 |
| Feedback | Brainstorm / Forward Look | 10 |

The protocol is a direct instantiation of the Process seed. This should be explicitly stated in the protocol document.

### 6.4 Project Folder Structure

Six subfolders, mapped to the Loop, as confirmed in the brainstorm: `briefs/`, `proposals/`, `audits/`, `contracts/`, `summaries/`, `brainstorms/`. Each folder gets a template for its artifact type.

Roadmaps move to `02_KNOWLEDGE/strategy/` — they are strategic knowledge assets with authority_weight 75, referenced by multiple projects.

### 6.5 Minimum Viable Constellations

The kernel informs what constellations Agent Maestro needs. Each constellation maps to a foundational concern:

| Concern | Constellation | Kernel basis |
|---------|--------------|-------------|
| Keeping the vault healthy | **Maintenance** | Seed 2 (are all primitives intact?) + Law 2 (are all actions logged?) + Viability audit |
| Ensuring governance alignment | **Governance** | Seed 3 (is the constraint hierarchy consistent?) + Alignment audit + Integrity audit |
| Improving the system over time | **Evolution** | Seed 1 (feedback loop) + Fractal (self-application) + D3 (controlled evolution) |

Three constellations. Each maps to a seed. Maintenance ensures Structure is intact. Governance ensures Constraints are respected. Evolution ensures the Process loop feeds back into improvement.

This is the minimum viable set. Additional constellations (e.g., for external vault audit in Wave 8) are derived from these three by applying Fractal Design — the same capabilities, applied to a different target.

---

## 7. What Foundations.md Should Contain

Based on this treatise, the governance document `Agent Maestro — Foundations.md` should contain:

1. **The kernel declaration**: Three seeds, one meta-principle, three laws. Concise definitions. No lengthy explanation (that's what this treatise is for).
2. **The derived principles**: Five principles, each explicitly traced to the kernel element(s) it operationalizes.
3. **The hierarchy diagram**: Kernel → Derived Principles → Operational Patterns.
4. **The constraint chain**: Both hierarchy and chain-of-negation forms of the Constraint seed.
5. **The audit taxonomy**: Three types (Alignment, Integrity, Viability) with one-line definitions.

What Foundations.md should NOT contain:

- Extended rationale (that's this treatise)
- Framework reconciliation (that's this treatise)
- Implementation details (that's templates and operational documents)
- The Seven Types of Authority, 10-level hierarchy, or System Genesis (these are reference documents, not kernel elements)

The document should have `authority_weight: 95` — higher than the current Principles document (90) — because it is the foundation from which principles are derived.

---

## 8. Open Questions Resolved

From the Foundational Brainstorm's section 3.2:

| ID | Question | Resolution |
|---|---|---|
| Q1 | What is the exact revised principle set? | **Resolved**: 5 derived principles (D1–D5), section 4.2 |
| Q2 | How many laws are there? | **Resolved**: Three. Additional candidates tested and found to be covered (section 5.4) |
| Q3 | Where do roadmaps live? | **Resolved**: `02_KNOWLEDGE/strategy/` |
| Q4 | Minimum viable template set? | **Resolved**: 7 templates in priority order (section 6.1) |
| Q5 | How do the Seven Types of Authority and 10-level hierarchy relate? | **Resolved**: Both are derived from the Constraint seed at different levels of detail (sections 3.1, 3.2) |
| Q6 | Brainstorm document template? | **Resolved**: Follow the Irreducible Loop structure (P→I→D→A→M→F) as demonstrated by this treatise and the brainstorm |

---

## 9. Conclusion

Agent Maestro's foundational kernel is seven elements: three seeds (Process, Structure, Constraint), one meta-principle (Fractal Design), and three laws (Direction of Authority, Action Properties, Economy). These seven elements are irreducible — removing any one creates a gap that the remaining six cannot fill. They are complete — every existing principle, framework, and architectural decision in Agent Maestro can be traced to them. They are fractal — they apply at every level of abstraction from a single frontmatter field to the entire vault architecture.

The existing 12 principles reduce to 5 derived principles, each explicitly grounded in the kernel. The remaining 7 of the original 12 are not lost — they are elevated into the kernel itself, where they hold more power and wider applicability.

This treatise feeds `Agent Maestro — Foundations.md`. The foundations document feeds the revised Wave 5 proposal. Wave 5 applies the foundations to every layer of the vault. The fractal continues.

---

**This treatise is complete. It feeds the next artifact: `Agent Maestro — Foundations.md`.**
