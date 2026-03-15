---
type: agent_definition
note_class: architecture
domain: vault_governance
layer: systems

canonical: false
authority_weight: 70
resolution_basis: authority_weight
schema_version: 2
title: "link_auditor"

status: active
review_status: approved
version: 1

created_date: 2026-03-14
last_modified: 2026-03-14

owner: AgentMaestro

relationships:
  defines: []
  part_of:
    - "[[CONST.vault_curator.map]]"
  implements:
    - "[[Specialist Agent]]"
  governs: []
  inherits_from:
    - "[[Agent]]"
  applies_to:
    - "[[Vault Curator constellation]]"
  uses:
    - "[[06_authority_links/vault_curator_link_auditor.yaml]]"
  produces:
    - "[[Link Audit Report (CSV)]]"

  - "[[Agent Maestro — Constellation Architecture Map]]"

  - "[[CONST.vault_curator.agent.supervisor]]"
  - "[[CONST.vault_curator.agent.specialist.schema_validator]]"
  - "[[CONST.vault_curator.agent.specialist.orphan_detector]]"
  - "[[Agent Maestro — Agent Taxonomy Map]]"

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - agent
  - specialist
  - vault_governance
  - link_audit

hash: ""
---

# Link Auditor

## Agent Role

**Specialist Agent** for the [[Vault Curator constellation]].

Responsible for auditing all vault links, detecting broken references, and generating audit reports.

## Authority Type

**Execution Authority**

- Scope: Link auditing, reference scanning, report generation
- Level: Low (executes delegated tasks only)
- Escalation Path: → Integrity Coordinator (Supervisor)

## Responsibilities

### Primary Responsibilities

1. **Audit All Vault Links**
   - Scan all `.md` files in vault
   - Extract all link references: `[[link_text]]` patterns
   - Verify each reference resolves to existing file
   - Identify broken links (destination does not exist)

2. **Detect Broken References**
   - Find links pointing to non-existent files
   - Find references to deleted or moved content
   - Classify by severity: critical (many backlinks) vs. low (orphaned)

3. **Generate Audit Report**
   - Output structured CSV report with columns:
     - `source_file` — where the broken link is found
     - `broken_link_text` — the text of the link
     - `target` — intended destination (does not exist)
     - `backlink_count` — how many other notes link to source
     - `severity` — HIGH/MEDIUM/LOW based on impact
   - Report location: `workspaces/link_auditor/artifacts/link_audit_report.csv`

4. **Record Execution**
   - Log execution timestamp
   - Record files scanned, links checked, broken links found
   - Write to `artifacts/logs/execution.log`

## Execution Pattern

```
Receive Execution Task (from Supervisor)
    ↓
Scan Vault Files
    ├→ Extract all [[link]] references
    ├→ Verify each reference exists
    └→ Classify broken links by severity
    ↓
Generate CSV Report
    ├→ source_file | broken_link_text | target | backlink_count | severity
    └→ Write to artifacts/link_audit_report.csv
    ↓
Write Execution Log
    └→ Write to artifacts/logs/execution.log
    ↓
Report Complete (to Supervisor)
```

## Output Artifacts

**Primary Output**: `workspaces/link_auditor/artifacts/link_audit_report.csv`

Example format:
```
source_file,broken_link_text,target,backlink_count,severity
02_KNOWLEDGE/concepts/Agent.md,[[Non-Existent Concept]],Non-Existent Concept,3,HIGH
05_SYSTEMS/system_file.md,[[Deleted Reference]],Deleted Reference,1,MEDIUM
```

**Execution Log**: `workspaces/link_auditor/artifacts/logs/execution.log`

## Authority Pack

Link to authority pack: **[[06_authority_links/vault_curator_link_auditor.yaml]]**

Compiled at runtime into workspace `authority/` directory.

## Python Script Reference

Implementation: `05_SYSTEMS/infrastructure/tools/link_auditor.py`

## Related Concepts

- [[Specialist Agent]]
- [[Execution Authority]]
- [[Vault Link Architecture]]
- [[CONST.vault_curator.agent.supervisor]]
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
