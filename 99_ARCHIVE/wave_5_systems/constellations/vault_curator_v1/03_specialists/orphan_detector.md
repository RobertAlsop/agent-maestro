---
type: agent_definition
note_class: architecture
domain: vault_governance
layer: systems

canonical: false
authority_weight: 70
resolution_basis: authority_weight
schema_version: 2
title: "orphan_detector"

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
    - "[[06_authority_links/vault_curator_orphan_detector.yaml]]"
  produces:
    - "[[Orphan Detection Report (CSV)]]"

  - "[[Agent Maestro — Constellation Architecture Map]]"

  - "[[CONST.vault_curator.agent.supervisor]]"
  - "[[CONST.vault_curator.agent.specialist.link_auditor]]"
  - "[[CONST.vault_curator.agent.specialist.schema_validator]]"
  - "[[Agent Maestro — Agent Taxonomy Map]]"

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - agent
  - specialist
  - vault_governance
  - orphan_detection

hash: ""
---

# Orphan Detector

## Agent Role

**Specialist Agent** for the [[Vault Curator constellation]].

Responsible for detecting orphaned content, identifying notes without incoming links, and generating orphan reports.

## Authority Type

**Execution Authority**

- Scope: Orphan detection, connectivity analysis, report generation
- Level: Low (executes delegated tasks only)
- Escalation Path: → Integrity Coordinator (Supervisor)

## Responsibilities

### Primary Responsibilities

1. **Detect Orphaned Content**
   - Identify notes with no incoming links (true orphans)
   - Identify notes referenced only in archive or deprecated contexts
   - Find disconnected component graphs in vault link structure
   - Detect unreachable nodes (not linked from any map)

2. **Analyze Connectivity**
   - Build bidirectional link graph of entire vault
   - Identify outgoing links from each note
   - Identify incoming backlinks to each note
   - Calculate link degree (centrality) for each note
   - Find isolated clusters or poorly connected regions

3. **Classify Orphan Types**
   - **True Orphan**: No incoming links from any note
   - **Weakly Connected**: Linked only by orphans or deprecated content
   - **Unmapped**: Not reachable from system maps
   - **Dead End**: Has many outgoing links but receives none
   - **Potential Archive**: Old date, no recent references

4. **Generate Orphan Report**
   - Output structured CSV report with columns:
     - `file_path` — path to orphaned note
     - `orphan_type` — TRUE_ORPHAN / WEAKLY_CONNECTED / UNMAPPED / DEAD_END / POTENTIAL_ARCHIVE
     - `incoming_link_count` — number of backlinks (0 for true orphans)
     - `outgoing_link_count` — number of forward links
     - `created_date` — when note was created
     - `last_updated` — last modification date
     - `connectivity_score` — 0-100 (lower = more orphaned)
   - Report location: `workspaces/link_auditor/artifacts/orphan_detection_report.csv`

5. **Record Execution**
   - Log execution timestamp
   - Record files scanned, orphans found, connectivity analysis results
   - Write to `artifacts/logs/execution.log`

## Execution Pattern

```
Receive Execution Task (from Supervisor)
    ↓
Build Link Graph
    ├→ Extract all [[link]] references
    ├→ Create node for each file
    ├→ Create edges for all links
    └→ Compute bidirectional graph
    ↓
Analyze Connectivity
    ├→ Calculate incoming links per node
    ├→ Calculate outgoing links per node
    ├→ Identify isolated nodes (orphans)
    ├→ Find weakly connected components
    └→ Calculate connectivity scores
    ↓
Classify Orphan Types
    ├→ TRUE_ORPHAN
    ├→ WEAKLY_CONNECTED
    ├→ UNMAPPED
    ├→ DEAD_END
    └→ POTENTIAL_ARCHIVE
    ↓
Generate CSV Report
    ├→ file_path | orphan_type | incoming_links | outgoing_links | created | updated | score
    └→ Write to artifacts/orphan_detection_report.csv
    ↓
Write Execution Log
    └→ Write to artifacts/logs/execution.log
    ↓
Report Complete (to Supervisor)
```

## Output Artifacts

**Primary Output**: `workspaces/link_auditor/artifacts/orphan_detection_report.csv`

Example format:
```
file_path,orphan_type,incoming_link_count,outgoing_link_count,created_date,last_updated,connectivity_score
02_KNOWLEDGE/experiments/old_idea.md,TRUE_ORPHAN,0,2,2025-06-01,2025-07-15,0
05_SYSTEMS/deprecated/old_system.md,POTENTIAL_ARCHIVE,1,0,2025-01-01,2025-10-30,15
```

**Execution Log**: `workspaces/link_auditor/artifacts/logs/execution.log`

## Analysis Methodology

**Connectivity Score**: (incoming_links * 2 + outgoing_links) / (max_links_in_vault + 1) * 100

- Score 0-20: Likely orphan (candidate for review/archival)
- Score 20-50: Weakly connected (consider promoting via maps)
- Score 50+: Well integrated (good connectivity)

## Authority Pack

Link to authority pack: **[[06_authority_links/vault_curator_orphan_detector.yaml]]**

Compiled at runtime into workspace `authority/` directory.

## Python Script Reference

Implementation: `05_SYSTEMS/infrastructure/tools/orphan_detector.py`

## Related Concepts

- [[Specialist Agent]]
- [[Execution Authority]]
- [[Vault Graph Structure]]
- [[CONST.vault_curator.agent.supervisor]]
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
