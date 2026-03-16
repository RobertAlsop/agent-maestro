# Exact architecture used to prevent agent responsibility collision

Large AI teams usually converge on a **layered orchestration architecture with bounded domains and explicit handoffs**.

The clean version looks like this:

## Layered architecture

Layer 0 — System of Record  
Vault / Repo / Knowledge Base  
  
Layer 1 — Mechanical Integrity Layer  
Shell scripts, CI checks, schedulers  
  
Layer 2 — Triage & Routing Layer  
Supervisor + Structural Drift Analyst  
  
Layer 3 — Specialist Audit Layer  
Definition Auditor  
Ontology Auditor  
Template Scanner  
Note Processor  
Other specialists  
  
Layer 4 — Controlled Repair Layer  
Self-Healing Repairer / Fix Executor  
  
Layer 5 — Validation & Change Control  
Re-run checks  
Commit  
Push  
Escalate if needed

## Why this works

It prevents collisions because each layer has a different question:

### Layer 1 — Mechanical layer

“Is the structure mechanically valid?”

### Layer 2 — Routing layer

“What kind of problem is this, and who owns it?”

### Layer 3 — Specialist layer

“What does this mean in domain terms?”

### Layer 4 — Repair layer

“What change should actually be made?”

### Layer 5 — Validation layer

“Did the fix succeed safely?”

## Anti-collision rules large teams use

### 1. Single owner per problem type

Each class of issue has one primary owner.

Example:

- YAML syntax → shell
    
- template semantics → Template Compliance Scanner
    
- definition drift → Definition Alignment Auditor
    

No shared ownership.

### 2. Specialists audit, repairer repairs

Specialists should usually **diagnose**, not directly modify.

One dedicated repair agent applies fixes.

That stops five agents from all “helpfully” editing the same note.

### 3. Supervisor never does specialist work

The supervisor routes, prioritizes, and enforces policy.

It does not become a wildcard agent.

### 4. Handoffs use structured tickets

Every issue becomes a structured work item:

- issue ID
    
- source
    
- severity
    
- owner
    
- authority level
    
- required action
    
- validation criteria
    

This is a huge collision reducer.

### 5. Validation is separate from repair

The repairer should not be the final judge of its own work.

Re-run shell checks and, where needed, a separate semantic validation pass.

### 6. Default to read-only specialists

Auditors should produce findings, not edits, unless explicitly granted repair authority.

### 7. Escalation thresholds are explicit

High-authority surfaces always escalate:

- governance
    
- ontology roots
    
- canonical maps
    
- system-wide templates
    

## Recommended command model

Use this flow:

Scripts detect  
↓  
Routing agent classifies issue type  
↓  
Specialist audits and recommends  
↓  
Repairer executes within authority  
↓  
Validator confirms  
↓  
Committer records

## Practical responsibility matrix

|Function|Owner|
|---|---|
|Missing file/folder|Shell constellation|
|Broken link|Shell constellation|
|Malformed YAML|Shell constellation|
|Duplicate frontmatter ID|Shell constellation|
|Definitional contradiction|Definition Alignment Auditor|
|Ontology inconsistency|Ontology Integrity Auditor|
|Wrong note-class structure|Template Compliance Scanner|
|Capture triage|Note Processor|
|Semantic repair execution|Self-Healing Repairer|
|Cross-specialist issue routing|Structural Drift Analyst|
|Priority / authority / escalation|Supervisor|

## The simplest rule to remember

**Mechanics below, meaning above, repair centralized.**

That one sentence prevents most collisions.

---

# Recommended final combined model

Your full maintenance stack should be:

Vault  
↓  
Shell Script Vault Maintenance Constellation  
↓  
Structural Drift Analyst  
↓  
Maintenance Supervisor  
↓  
Specialist Auditors  
↓  
Self-Healing Repairer  
↓  
Validation + Auto-Commit