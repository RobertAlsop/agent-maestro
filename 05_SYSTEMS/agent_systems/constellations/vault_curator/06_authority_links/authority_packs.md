---
id: CONST.vault_curator.authority.index
type: authority_index
note_class: governance
domain: vault_governance
layer: systems
scope: null

canonical: false
authority_weight: 80
resolution_basis: authority_weight
schema_version: 2

status: active
review_status: approved
version: 1

created: 2026-03-14
updated: 2026-03-14
last_reviewed: null
review_cycle: quarterly

owner: AgentMaestro

relationships:
  defines: []
  part_of:
    - "[[CONST.vault_curator.map]]"
  implements: []
  governs: []
  inherits_from: []
  applies_to:
    - "[[Vault Curator constellation]]"
  uses: []
  produces: []

map: "[[CONST.vault_curator.map]]"
maps:
  - "[[Authority Architecture Map]]"

related: []
related_maps:
  - "[[Authority Architecture Map]]"
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - authority
  - governance
  - constellation
  - vault_curator

hash: ""
---

# Vault Curator Authority Packs

## Purpose

Index of all authority packs and compiled artifacts for the [[Vault Curator constellation]]. These authority packs govern the decision rights and execution scope for each agent in the constellation.

## Authority Pack Definitions

All authority pack YAML files are source definitions that contain roles, authorities, constraints, and decision contracts.

### 1. Executive Authority Pack
**File**: `vault_curator_executive.yaml`

**Role**: Vault Governance Director

**Authority Type**: Decision Authority

**Scope**:
- Set maintenance priorities
- Approve non-destructive fixes
- Review escalations from Supervisor
- Escalate destructive actions to human

**Key Decisions**:
- `APPROVE_NON_DESTRUCTIVE` — fix links, schema corrections (yes/no)
- `ESCALATE_DESTRUCTIVE` — pass deletions to human (required)
- `PRIORITIZE_AUDITS` — choose which audits to run (yes/no)

**Escalation Path**: → human_operator

**Authority Inheritance**: None (top-level executive)

**Constraints**:
- Cannot execute deletions unilaterally
- Must escalate all destructive actions
- Decision log must record all approvals

---

### 2. Supervisor Authority Pack
**File**: `vault_curator_supervisor.yaml`

**Role**: Integrity Coordinator

**Authority Type**: Coordination Authority

**Scope**:
- Receive priorities from Executive
- Delegate tasks to Specialists
- Execute safe fixes (link repair, schema correction, backlinks)
- Aggregate audit results
- Escalate destructive actions to Executive

**Key Decisions**:
- `DELEGATE_TASK` — assign work to specialists (yes/no)
- `EXECUTE_SAFE_FIX` — apply non-destructive corrections (yes/no)
- `ESCALATE_DESTRUCTIVE` — flag deletions for Executive (required)

**Escalation Path**: → Executive (Vault Governance Director)

**Authority Inheritance**: Inherits scope from Executive

**Constraints**:
- Can only execute safe, non-destructive fixes
- Cannot delete or remove links
- Must aggregate results before escalating
- All fixes must preserve content integrity

---

### 3. Link Auditor Authority Pack
**File**: `vault_curator_link_auditor.yaml`

**Role**: Link Auditor

**Authority Type**: Execution Authority

**Scope**:
- Scan vault files
- Extract link references
- Verify link destinations
- Generate audit report
- Write execution log

**Key Decisions**:
- None (specialist executes delegated task only)

**Escalation Path**: → Supervisor (Integrity Coordinator)

**Authority Inheritance**: Inherits task scope from Supervisor

**Constraints**:
- Can only execute delegated audit task
- Cannot modify vault content
- Cannot make decisions
- Must write results to designated artifact location

---

### 4. Schema Validator Authority Pack
**File**: `vault_curator_schema_validator.yaml`

**Role**: Schema Validator

**Authority Type**: Execution Authority

**Scope**:
- Parse frontmatter from all files
- Validate against schema standard
- Check required fields
- Generate validation report
- Write execution log

**Key Decisions**:
- None (specialist executes delegated task only)

**Escalation Path**: → Supervisor (Integrity Coordinator)

**Authority Inheritance**: Inherits task scope from Supervisor

**Constraints**:
- Can only execute delegated validation task
- Cannot modify vault content
- Cannot make decisions
- Must write results to designated artifact location

---

### 5. Orphan Detector Authority Pack
**File**: `vault_curator_orphan_detector.yaml`

**Role**: Orphan Detector

**Authority Type**: Execution Authority

**Scope**:
- Build link graph
- Analyze connectivity
- Identify orphaned nodes
- Classify orphan types
- Generate detection report
- Write execution log

**Key Decisions**:
- None (specialist executes delegated task only)

**Escalation Path**: → Supervisor (Integrity Coordinator)

**Authority Inheritance**: Inherits task scope from Supervisor

**Constraints**:
- Can only execute delegated detection task
- Cannot modify vault content
- Cannot make decisions
- Must write results to designated artifact location

---

## Compiled Artifacts

Authority packs are compiled by the Authority Pack Compiler at runtime into binary/JSON artifacts that are deployed to each agent's workspace.

### Compiled Artifact Locations

Each specialist workspace contains a compiled authority artifact:

```
workspaces/link_auditor/authority/
  └── vault_curator_link_auditor.compiled.json
```

When the constellation executes, compiled artifacts are populated into:
- `workspaces/<specialist_name>/authority/`

These compiled artifacts contain:
- Parsed authority definitions
- Resolved decision contracts
- Authority inheritance chains
- Constraint validations

### Compilation Process

Authority packs are compiled via:
- **Tool**: Authority Pack Compiler
- **Input**: YAML authority pack definitions
- **Output**: Compiled JSON artifacts
- **Storage**: Each workspace's `authority/` directory
- **Timing**: At constellation execution time

For details: [[Authority Pack Compiler — Map]]

---

## Authority Hierarchy

```
human_operator (final authority on destructive actions)
  ↑
Executive: Vault Governance Director
  ├→ Supervisor: Integrity Coordinator
  │   ├→ Link Auditor (execution)
  │   ├→ Schema Validator (execution)
  │   └→ Orphan Detector (execution)
```

**Authority Flow**:
1. Human sets strategic direction (vault maintenance priority)
2. Executive receives priorities, makes high-level decisions
3. Supervisor coordinates specialists, executes safe fixes
4. Specialists execute audits, return results
5. Supervisor escalates destructive actions back to Executive
6. Executive escalates to human if destructive action needed

---

## Pack Compilation Registry

| Pack Name | Agent Role | Authority Type | Status | Compiled Artifact |
|-----------|-----------|------------------|--------|-------------------|
| vault_curator_executive.yaml | Executive | Decision | Active | (runtime compiled) |
| vault_curator_supervisor.yaml | Supervisor | Coordination | Active | (runtime compiled) |
| vault_curator_link_auditor.yaml | Link Auditor | Execution | Active | vault_curator_link_auditor.compiled.json |
| vault_curator_schema_validator.yaml | Schema Validator | Execution | Active | (runtime compiled) |
| vault_curator_orphan_detector.yaml | Orphan Detector | Execution | Active | (runtime compiled) |

All packs compiled together at constellation activation.

---

## Related Concepts

- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
- [[Authority Pack]]
- [[Authority Pack Compiler — Map]]
- [[Decision Authority]]
- [[Execution Authority]]
- [[CONST.vault_curator.agent.executive]]
- [[CONST.vault_curator.agent.supervisor]]
