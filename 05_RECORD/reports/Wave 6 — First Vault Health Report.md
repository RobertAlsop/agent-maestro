# Vault Health Report

**Vault:** /Users/robertalsop/Obsidian/02_Systems/Agent Maestro
**Date:** 2026-03-16T20:16:46
**Result:** FINDINGS

## Tool Summary

| Tool | Exit Code | Result | Report |
|------|-----------|--------|--------|
| Structure Check | 0 | CLEAN | Structure_Check_report.md |
| YAML Validation | 1 | FINDINGS | YAML_Validation_report.md |
| Broken Links | 1 | FINDINGS | Broken_Links_report.md |
| Orphan Detection | 1 | FINDINGS | Orphan_Detection_report.md |
| Stub Detection | 1 | FINDINGS | Stub_Detection_report.md |
| Naming Validation | 1 | FINDINGS | Naming_Validation_report.md |
| Inventory | 0 | CLEAN | Inventory_report.md |

## Combined Findings

### YAML Validation


- 02_KNOWLEDGE/templates/Template — Audit Report.md: 'created' is not ISO 8601 format: ''
- 02_KNOWLEDGE/templates/Template — Audit Report.md: 'updated' is not ISO 8601 format: ''
- 02_KNOWLEDGE/templates/Template — Concept.md: 'created' is not ISO 8601 format: ''
- 02_KNOWLEDGE/templates/Template — Concept.md: 'updated' is not ISO 8601 format: ''
- 02_KNOWLEDGE/templates/Template — Governance.md: 'created' is not ISO 8601 format: ''
- 02_KNOWLEDGE/templates/Template — Governance.md: 'updated' is not ISO 8601 format: ''
- 02_KNOWLEDGE/templates/Template — Proposal.md: 'created' is not ISO 8601 format: ''
- 02_KNOWLEDGE/templates/Template — Proposal.md: 'updated' is not ISO 8601 format: ''
- 02_KNOWLEDGE/templates/Template — Reflection.md: 'created' is not ISO 8601 format: ''
- 02_KNOWLEDGE/templates/Template — Reflection.md: 'updated' is not ISO 8601 format: ''
- 02_KNOWLEDGE/templates/Template — Role.md: 'created' is not ISO 8601 format: ''
- 02_KNOWLEDGE/templates/Template — Role.md: 'updated' is not ISO 8601 format: ''
- 02_KNOWLEDGE/templates/Template — Session Log.md: 'created' is not ISO 8601 format: ''
- 02_KNOWLEDGE/templates/Template — Session Log.md: 'updated' is not ISO 8601 format: ''
- 02_KNOWLEDGE/templates/Template — Skill.md: 'created' is not ISO 8601 format: ''
- 02_KNOWLEDGE/templates/Template — Skill.md: 'updated' is not ISO 8601 format: ''
- 05_RECORD/archive/wave_5_projects/00 Agent Maestro — Build Session Protocol v2.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_projects/01 Agent Maestro — Script Build Harness Integration Brief v1.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_projects/01 Definition Alignment Audit v2.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_projects/02 Adversarial Audit.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_projects/02 Ontology Integrity Audit.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_projects/03 Build Harness Implementation Contract v1.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_projects/03 Reasoning Path Audit.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_projects/AI Governance Authority Pack v1.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/AI Governance Authority Pack v1.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/AI Governance Authority Pack v1.md: 'type' value 'project' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/AI Governance Authority Pack v1.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/AI Governance Authority Pack v1.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Audit of Proposal v3.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Audit of Proposal v3.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Audit of Proposal v3.md: 'type' value 'audit' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Audit of Proposal v3.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Audit of Proposal v3.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Contract.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Contract.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Contract.md: 'type' value 'contract' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Contract.md: 'status' value 'completed' not in allowed values ['draft', 'active', 'archived']
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Contract.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Contract.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Foundational Brainstorm.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Foundational Brainstorm.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Foundational Brainstorm.md: 'type' value 'brainstorm' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Foundational Brainstorm.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Foundational Brainstorm.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Audit.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Audit.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Audit.md: 'type' value 'reference' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Audit.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Audit.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Reconciliation Proposal.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Reconciliation Proposal.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Reconciliation Proposal.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Reconciliation Proposal.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v1.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v1.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v1.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v1.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v3.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v3.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v3.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v3.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Treatise on Core Principles.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Treatise on Core Principles.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Treatise on Core Principles.md: 'type' value 'treatise' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Treatise on Core Principles.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Treatise on Core Principles.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/AM-Authority-Architecture-Audit-2026-03-15.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_projects/Agent Deployment Playbook.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Agent Deployment Playbook.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Agent Deployment Playbook.md: 'type' value 'project' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Agent Deployment Playbook.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Agent Deployment Playbook.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Agent Maestro Build Roadmap.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: roadmap
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 17, column 1:
    - '[[Agent Maestro — Domain Map]]'
    ^
- 05_RECORD/archive/wave_5_projects/Agent Maestro Dashboard.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: system
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 17, column 1:
    - '[[Agent Maestro — Domain Map]]'
    ^
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.1 — Improvement Proposal.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 3:
      - "[[Agent Maestro — North Star]]"
      ^
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.1 — Session Log 2026-03-14.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: project
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 27, column 1:
    - '[[Agent Maestro v0.1 — Improv ... 
    ^
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.2 — Next Phase Proposal.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: project
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 26, column 1:
    - '[[Agent Maestro v0.1 — Improv ... 
    ^
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.2 — Wave 2+3 Proposal.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.2 — Wave 2+3 Proposal.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.2 — Wave 2+3 Proposal.md: 'type' value 'project' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.2 — Wave 2+3 Proposal.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.2 — Wave 2+3 Proposal.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Build Brief.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Build Brief.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Build Brief.md: missing required field 'relationships'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Build Brief.md: 'type' value 'brief' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Improvement Proposal — Chat GPT 5.2.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Next Moves Proposal.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Next Moves Proposal.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Next Moves Proposal.md: missing required field 'relationships'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase B Output Summary.md: missing required field 'type'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase B Output Summary.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase B Output Summary.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase B Output Summary.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase B Output Summary.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase B Output Summary.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase C Output Summary.md: missing required field 'type'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase C Output Summary.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase C Output Summary.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase C Output Summary.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase C Output Summary.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase C Output Summary.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.4 — Phase D Output Summary.md: missing required field 'type'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.4 — Phase D Output Summary.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.4 — Phase D Output Summary.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.4 — Phase D Output Summary.md: 'status' value 'completed' not in allowed values ['draft', 'active', 'archived']
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.4 — Phase D Output Summary.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.4 — Phase D Output Summary.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.4 — Phase D Output Summary.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Agent Maestro — Evolution Roadmap v0.2.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Agent Maestro — Evolution Roadmap v0.2.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Agent Maestro — Evolution Roadmap v0.2.md: 'type' value 'roadmap' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Agent Maestro — Evolution Roadmap v0.2.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Agent Maestro — Evolution Roadmap v0.2.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Agent Memory Architecture.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Agent Memory Architecture.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Agent Memory Architecture.md: 'type' value 'project' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Agent Memory Architecture.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Agent Memory Architecture.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Audit Folder For Unintended Cross-Folder Links.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Audit Folder For Unintended Cross-Folder Links.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Audit Folder For Unintended Cross-Folder Links.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Audit Folder For Unintended Cross-Folder Links.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Audit Folder For Unintended Cross-Folder Links.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/CLAUDE_execution.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_projects/CLAUDE_pipelines.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_projects/CLAUDE_runtime.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_projects/CLAUDE_systems.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_projects/Controlled Vault Repair Operation v2.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Controlled Vault Repair Operation v2.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Controlled Vault Repair Operation v2.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Controlled Vault Repair Operation v2.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Controlled Vault Repair Operation v2.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Filename Refactor.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Filename Refactor.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Filename Refactor.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Filename Refactor.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Filename Refactor.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Knowledge Upgrade Prompt v2.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_projects/Next Steps.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Next Steps.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Next Steps.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Next Steps.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Next Steps.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Note Knowledge Upgrade v1.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Note Knowledge Upgrade v1.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Note Knowledge Upgrade v1.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Note Knowledge Upgrade v1.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Note Knowledge Upgrade v1.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Open Questions.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Open Questions.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Open Questions.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Open Questions.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Open Questions.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Process Unprocessed Notes Into The Vault.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Process Unprocessed Notes Into The Vault.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Process Unprocessed Notes Into The Vault.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Process Unprocessed Notes Into The Vault.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Process Unprocessed Notes Into The Vault.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/TBP Outreach Agent V1 Spec.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/TBP Outreach Agent V1 Spec.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/TBP Outreach Agent V1 Spec.md: 'type' value 'project' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/TBP Outreach Agent V1 Spec.md: 'status' value 'incubating' not in allowed values ['draft', 'active', 'archived']
- 05_RECORD/archive/wave_5_projects/TBP Outreach Agent V1 Spec.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/TBP Outreach Agent V1 Spec.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Tasks Hub.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Tasks Hub.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Tasks Hub.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Tasks Hub.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Tasks Hub.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Template Architecture Audit.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Template Architecture Audit.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Template Architecture Audit.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Template Architecture Audit.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Template Architecture Audit.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/To Do.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/To Do.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/To Do.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/To Do.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/To Do.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Vault Build.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Vault Build.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Vault Build.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Vault Build.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Vault Build.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Vault Integrity & Self-Healing Audit v2.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Vault Integrity & Self-Healing Audit v2.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Vault Integrity & Self-Healing Audit v2.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Vault Integrity & Self-Healing Audit v2.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Vault Integrity & Self-Healing Audit v2.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Vault Structure and Knowledge Upgrade v2.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Vault Structure and Knowledge Upgrade v2.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Vault Structure and Knowledge Upgrade v2.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Vault Structure and Knowledge Upgrade v2.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Vault Structure and Knowledge Upgrade v2.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Vault Template Compliance Scan.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Vault Template Compliance Scan.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Vault Template Compliance Scan.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Vault Template Compliance Scan.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Vault Template Compliance Scan.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Vault Upgrade Backlog.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Vault Upgrade Backlog.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Vault Upgrade Backlog.md: 'type' value 'project' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Vault Upgrade Backlog.md: 'status' value 'incubating' not in allowed values ['draft', 'active', 'archived']
- 05_RECORD/archive/wave_5_projects/Vault Upgrade Backlog.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Vault Upgrade Backlog.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/Weekly Reset Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/Weekly Reset Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/Weekly Reset Template.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_projects/Weekly Reset Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_projects/Weekly Reset Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_projects/review_queue_20260315_111629.md: missing required field 'type'
- 05_RECORD/archive/wave_5_projects/review_queue_20260315_111629.md: missing required field 'authority_weight'
- 05_RECORD/archive/wave_5_projects/review_queue_20260315_111629.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/review_queue_20260315_111629.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/review_queue_20260315_111629.md: missing required field 'relationships'
- 05_RECORD/archive/wave_5_projects/test_d3_note.md: missing required field 'type'
- 05_RECORD/archive/wave_5_projects/test_d3_note.md: missing required field 'status'
- 05_RECORD/archive/wave_5_projects/test_d3_note.md: missing required field 'authority_weight'
- 05_RECORD/archive/wave_5_projects/test_d3_note.md: missing required field 'created'
- 05_RECORD/archive/wave_5_projects/test_d3_note.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_projects/test_d3_note.md: missing required field 'relationships'
- 05_RECORD/archive/wave_5_projects/test_d3_note.md: missing required field 'tags'
- 05_RECORD/archive/wave_5_operational_intelligence/AI Operations.md: missing required field 'created'
- 05_RECORD/archive/wave_5_operational_intelligence/AI Operations.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_operational_intelligence/AI Operations.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_operational_intelligence/AI Operations.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_operational_intelligence/AI Operations.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_operational_intelligence/Agent Performance Measurement.md: missing required field 'created'
- 05_RECORD/archive/wave_5_operational_intelligence/Agent Performance Measurement.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_operational_intelligence/Agent Performance Measurement.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_operational_intelligence/Agent Performance Measurement.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_operational_intelligence/Agent Performance Measurement.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_operational_intelligence/Operational Agent Design.md: missing required field 'created'
- 05_RECORD/archive/wave_5_operational_intelligence/Operational Agent Design.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_operational_intelligence/Operational Agent Design.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_operational_intelligence/Operational Agent Design.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_operational_intelligence/Operational Agent Design.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template_sys.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Authority Pack Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Authority Pack Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Authority Pack Template.md: 'type' value 'authority_pack' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Authority Pack Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Authority Pack Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Authority Pack Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Authority Pack Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Authority Pack Template_sys.md: 'type' value 'authority_pack' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Authority Pack Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Authority Pack Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/CLAUDE_sys.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_templates/Concept Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Concept Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Concept Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Concept Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Concept Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Concept Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Concept Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Concept Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Decision Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Decision Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Decision Template.md: 'type' value 'decision' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Decision Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Decision Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Decision Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Decision Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Decision Template_sys.md: 'type' value 'decision' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Decision Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Decision Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Frontmatter Schema v1.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_templates/Frontmatter Schema v1_sys.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_templates/Governance Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Governance Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Governance Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Governance Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Governance Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Governance Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Governance Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Governance Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Index Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Index Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Index Template.md: 'type' value 'index' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Index Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Index Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Index Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Index Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Index Template_sys.md: 'type' value 'index' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Index Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Index Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Map Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Map Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Map Template.md: 'type' value 'map' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Map Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Map Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Map Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Map Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Map Template_sys.md: 'type' value 'map' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Map Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Map Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Modes Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Modes Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Modes Template.md: 'type' value 'modes' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Modes Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Modes Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Modes Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Modes Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Modes Template_sys.md: 'type' value 'modes' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Modes Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Modes Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/North Star Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/North Star Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/North Star Template.md: 'type' value 'north_star' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/North Star Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/North Star Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/North Star Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/North Star Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/North Star Template_sys.md: 'type' value 'north_star' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/North Star Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/North Star Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Pipeline Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Pipeline Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Pipeline Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Pipeline Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Pipeline Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Pipeline Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Pipeline Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Pipeline Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Principles Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Principles Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Principles Template.md: 'type' value 'principles' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Principles Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Principles Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Principles Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Principles Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Principles Template_sys.md: 'type' value 'principles' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Principles Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Principles Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Process Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Process Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Process Template.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Process Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Process Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Process Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Process Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Process Template_sys.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Process Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Process Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Project Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Project Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Project Template.md: 'type' value 'project' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Project Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Project Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Project Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Project Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Project Template_sys.md: 'type' value 'project' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Project Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Project Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Reference Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Reference Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Reference Template.md: 'type' value 'reference' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Reference Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Reference Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Reference Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Reference Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Reference Template_sys.md: 'type' value 'reference' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Reference Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Reference Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Registry Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Registry Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Registry Template.md: 'type' value 'registry' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Registry Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Registry Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Registry Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Registry Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Registry Template_sys.md: 'type' value 'registry' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Registry Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Registry Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Roadmap Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Roadmap Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Roadmap Template.md: 'type' value 'roadmap' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Roadmap Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Roadmap Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Roadmap Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Roadmap Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Roadmap Template_sys.md: 'type' value 'roadmap' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Roadmap Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Roadmap Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Scope Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Scope Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Scope Template.md: 'type' value 'scope' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Scope Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Scope Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Scope Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Scope Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Scope Template_sys.md: 'type' value 'scope' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Scope Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Scope Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Strategy Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Strategy Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Strategy Template.md: 'type' value 'strategy' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Strategy Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Strategy Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Strategy Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Strategy Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Strategy Template_sys.md: 'type' value 'strategy' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Strategy Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Strategy Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/System Map.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/System Map.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/System Map.md: 'type' value 'system_map' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/System Map.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/System Map.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/System Map_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/System Map_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/System Map_sys.md: 'type' value 'system_map' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/System Map_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/System Map_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/System Registry.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/System Registry.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/System Registry.md: 'type' value 'system_registry' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/System Registry.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/System Registry.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/System Registry_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/System Registry_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/System Registry_sys.md: 'type' value 'system_registry' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/System Registry_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/System Registry_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/System Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/System Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/System Template.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/System Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/System Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/System Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/System Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/System Template_sys.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/System Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/System Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Taxonomy Template.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Taxonomy Template.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Taxonomy Template.md: 'type' value 'taxonomy' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Taxonomy Template.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Taxonomy Template.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Taxonomy Template_sys.md: missing required field 'created'
- 05_RECORD/archive/wave_5_templates/Taxonomy Template_sys.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_templates/Taxonomy Template_sys.md: 'type' value 'taxonomy' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_templates/Taxonomy Template_sys.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_templates/Taxonomy Template_sys.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_templates/Template Design Doctrine.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_templates/Template Design Doctrine_sys.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_templates/Template Governance Rules.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_templates/Template Governance Rules_sys.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_templates/Template Mapping.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_templates/Template Mapping_sys.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_templates/Template Registry.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_templates/Template Registry_sys.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_templates/Template Ruleset.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_templates/Template Ruleset_sys.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/AM Python Daemon for scheduled automations..md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/AM Self Audit.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/Am basically starter pack.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/Archived Treatsie.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/Breifs.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/Memory Options.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/Message sent on new capture sees.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/Potential rule.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/Proposal — Shell Script Vault Maintenance Constellation.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/RAG vs QMD.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/Reflections.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/Roles.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/Runtime Provider Layer  Proposal v2.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/Skills.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/The 6 shell scripts every large knowledge-vault builder eventually creates.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/Toon.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_captures/agent responsibility collision.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_knowledge/AI Executive Systems.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/AI Executive Systems.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/AI Executive Systems.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/AI Executive Systems.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/AI-Native Organizations.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/AI-Native Organizations.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/AI-Native Organizations.md: 'type' value 'domain' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/AI-Native Organizations.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/AI-Native Organizations.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/AM — Evolution Roadmap — Waves 5-8.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/AM — Evolution Roadmap — Waves 5-8.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/AM — Evolution Roadmap — Waves 5-8.md: 'type' value 'roadmap' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/AM — Evolution Roadmap — Waves 5-8.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/AM — Evolution Roadmap — Waves 5-8.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/archive/wave_5_knowledge/AM — Evolution Roadmap — Waves 5-8.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Agent Taxonomy Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 3:
      - "[[Agent Maestro — Concepts Map]]"
      ^
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Concepts Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 3:
      - "[[Agent Maestro — Systems Map]]"
      ^
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Constellation Architecture Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Agent Maestro — Agent Taxon ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Domain Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 3:
      - "[[Agent Maestro — Navigation  ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Evolution Roadmap v0.2.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Evolution Roadmap v0.2.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Evolution Roadmap v0.2.md: 'type' value 'roadmap' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Evolution Roadmap v0.2.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Evolution Roadmap v0.2.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Executive Layer Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines:
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 34, column 3:
      - "[[Agent Maestro — Agent Taxon ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Governance Artifacts Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Authority Architecture Map]]"
      ^
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Governance Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 3:
      - "[[Agent Maestro — Navigation  ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Layer Model Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 33, column 3:
      - "[[Agent Maestro — Stack Map]]"
      ^
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Navigation Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Agent Maestro — Systems Map]]"
      ^
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Pack Inheritance Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Authority Architecture Map]]"
      ^
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Pipelines Map.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Pipelines Map.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Pipelines Map.md: 'type' value 'system_map' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Pipelines Map.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Pipelines Map.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Practice Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 3:
      - "[[Agent Maestro — Governance  ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Projects & Experiments Map.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Projects & Experiments Map.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Projects & Experiments Map.md: 'type' value 'system_map' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Projects & Experiments Map.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Projects & Experiments Map.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Quickstart.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Quickstart.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Quickstart.md: missing required field 'relationships'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Quickstart.md: 'type' value 'map' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Stack Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 3:
      - "[[Agent Maestro — Systems Map]]"
      ^
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Systems Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 3:
      - "[[Agent Maestro — Constellati ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Agent Organizations.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Agent Organizations.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Agent Organizations.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Agent Organizations.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Anti-Agent-Sprawl Pattern.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Anti-Agent-Sprawl Pattern.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Anti-Agent-Sprawl Pattern.md: 'type' value 'pattern' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Anti-Agent-Sprawl Pattern.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Anti-Agent-Sprawl Pattern.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Authority Architecture Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Authority Pack Compiler — M ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Authority Inheritance Pattern.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 27, column 3:
      - "[[Agent Maestro — Pack Inheri ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Authority Pack Compiler — Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Authority Architecture Map]]"
      ^
- 05_RECORD/archive/wave_5_knowledge/Authority Pack Grammar.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Authority Pack Grammar.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Authority Pack Grammar.md: 'type' value 'pattern' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Authority Pack Grammar.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Authority Pack Grammar.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Authority Systems.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Authority Systems.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Authority Systems.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Authority Systems.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Constellation Architecture Pattern.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 29, column 3:
      - "[[Agent Maestro — Constellati ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Controlled Evolution Pattern.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Controlled Evolution Pattern.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Controlled Evolution Pattern.md: 'type' value 'pattern' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Controlled Evolution Pattern.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Controlled Evolution Pattern.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Decision-Execution Separation.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Decision-Execution Separation.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Decision-Execution Separation.md: 'type' value 'pattern' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Decision-Execution Separation.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Decision-Execution Separation.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Deterministic Authority Resolution Pattern.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Deterministic Authority Resolution Pattern.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Deterministic Authority Resolution Pattern.md: 'type' value 'pattern' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Deterministic Authority Resolution Pattern.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Deterministic Authority Resolution Pattern.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Deterministic Control Surfaces.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Deterministic Control Surfaces.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Deterministic Control Surfaces.md: 'type' value 'pattern' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Deterministic Control Surfaces.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Deterministic Control Surfaces.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Evidence Over Assumptions.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Evidence Over Assumptions.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Evidence Over Assumptions.md: 'type' value 'pattern' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Evidence Over Assumptions.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Evidence Over Assumptions.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Executive-Supervisor-Specialist Pattern.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 29, column 3:
      - "[[Agent Maestro — Agent Taxon ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Governance Before Autonomy.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Governance Before Autonomy.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Governance Before Autonomy.md: 'type' value 'pattern' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Governance Before Autonomy.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Governance Before Autonomy.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Governance Compilation Pattern.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Authority Pack Compiler — M ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Governance Infrastructure.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Governance Infrastructure.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Governance Infrastructure.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Governance Infrastructure.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Governance Systems.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Governance Systems.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Governance Systems.md: 'type' value 'domain' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Governance Systems.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Governance Systems.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Host Binding Pattern.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Authority Pack Compiler — M ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Human Escalation Pattern.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Human Escalation Pattern.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Human Escalation Pattern.md: 'type' value 'pattern' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Human Escalation Pattern.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Human Escalation Pattern.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Human-Agent Collaboration.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Human-Agent Collaboration.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Human-Agent Collaboration.md: 'type' value 'domain' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Human-Agent Collaboration.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Human-Agent Collaboration.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Memory Architecture Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Agent Maestro — Systems Map]]"
      ^
- 05_RECORD/archive/wave_5_knowledge/Memory Layer Registry.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Memory Layer Registry.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Memory Layer Registry.md: 'type' value 'map' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Memory Layer Registry.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Memory Layer Registry.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Model Workspace Protocol Pattern.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Agent Maestro — Concepts Map]]"
      ^
- 05_RECORD/archive/wave_5_knowledge/Multi-Agent Coordination.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Multi-Agent Coordination.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Multi-Agent Coordination.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Multi-Agent Coordination.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Operational Governance.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Operational Governance.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Operational Governance.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Operational Governance.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Operational Intelligence Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Agent Maestro — Systems Map]]"
      ^
- 05_RECORD/archive/wave_5_knowledge/Operational Transformation.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Operational Transformation.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Operational Transformation.md: 'type' value 'domain' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Operational Transformation.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Operational Transformation.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Organizational Intelligence.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Organizational Intelligence.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Organizational Intelligence.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Organizational Intelligence.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Pack Override Rules.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 26, column 3:
      - "[[Agent Maestro — Pack Inheri ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Pack Versioning Pattern.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 26, column 3:
      - "[[Agent Maestro — Pack Inheri ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Platformization.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Platformization.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Platformization.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Platformization.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Policy Resolution Pattern.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 26, column 3:
      - "[[Authority Pack Compiler — M ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Project Governance Map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 3:
      - "[[Agent Maestro — Governance  ... 
      ^
- 05_RECORD/archive/wave_5_knowledge/Thin-Edge Thick-Core Pattern.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Thin-Edge Thick-Core Pattern.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Thin-Edge Thick-Core Pattern.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Thin-Edge Thick-Core Pattern.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Three-Layer Memory Model.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Three-Layer Memory Model.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Three-Layer Memory Model.md: 'type' value 'pattern' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Three-Layer Memory Model.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Three-Layer Memory Model.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_knowledge/Workflow Intelligence.md: missing required field 'created'
- 05_RECORD/archive/wave_5_knowledge/Workflow Intelligence.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_knowledge/Workflow Intelligence.md: 'type' value 'domain' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_knowledge/Workflow Intelligence.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_knowledge/Workflow Intelligence.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_indexes/Artifact Taxonomy.md: missing required field 'created'
- 05_RECORD/archive/wave_5_indexes/Artifact Taxonomy.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_indexes/Artifact Taxonomy.md: 'type' value 'taxonomy' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_indexes/Artifact Taxonomy.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_indexes/Artifact Taxonomy.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_indexes/Authority Pack Registry.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Agent Maestro — Pack Inheri ... 
      ^
- 05_RECORD/archive/wave_5_indexes/Authority Packs Index.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Authority Architecture Map]]"
      ^
- 05_RECORD/archive/wave_5_indexes/Canonical Notes Index.md: missing required field 'created'
- 05_RECORD/archive/wave_5_indexes/Canonical Notes Index.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_indexes/Canonical Notes Index.md: 'type' value 'index' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_indexes/Canonical Notes Index.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_indexes/Canonical Notes Index.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_indexes/Canonical Notes Registry.md: missing required field 'created'
- 05_RECORD/archive/wave_5_indexes/Canonical Notes Registry.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_indexes/Canonical Notes Registry.md: 'type' value 'registry' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_indexes/Canonical Notes Registry.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_indexes/Canonical Notes Registry.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_indexes/Compiler Artifacts Registry.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Agent Maestro — Governance  ... 
      ^
- 05_RECORD/archive/wave_5_indexes/Constellation Index.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Agent Maestro — Systems Map]]"
      ^
- 05_RECORD/archive/wave_5_indexes/Glossary.md: missing required field 'created'
- 05_RECORD/archive/wave_5_indexes/Glossary.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_indexes/Glossary.md: 'type' value 'index' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_indexes/Glossary.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_indexes/Glossary.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_indexes/Pack Lineage Index.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Authority Architecture Map]]"
      ^
- 05_RECORD/archive/wave_5_indexes/Pack Version Registry.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Authority Architecture Map]]"
      ^
- 05_RECORD/archive/wave_5_indexes/Shared Services Index.md: missing required field 'created'
- 05_RECORD/archive/wave_5_indexes/Shared Services Index.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_indexes/Shared Services Index.md: 'type' value 'index' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_indexes/Shared Services Index.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_indexes/Shared Services Index.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_indexes/System Registry.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Agent Maestro — Constellati ... 
      ^
- 05_RECORD/archive/wave_5_reports/AM — Wave 5 — Baseline Inventory.md: missing required field 'created'
- 05_RECORD/archive/wave_5_reports/AM — Wave 5 — Baseline Inventory.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_reports/AM — Wave 5 — Baseline Inventory.md: 'type' value 'reference' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_reports/AM — Wave 5 — Baseline Inventory.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_reports/AM — Wave 5 — Baseline Inventory.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_reports/AM — Wave 5 — Final Audit Report.md: missing required field 'created'
- 05_RECORD/archive/wave_5_reports/AM — Wave 5 — Final Audit Report.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_reports/AM — Wave 5 — Final Audit Report.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_reports/AM — Wave 5 — Final Audit Report.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_roadmap/AM v1.0.0 — Design Blueprint.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_roadmap/AM — Evolution Roadmap — Waves 5-8.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_roadmap/AM — Evolution Roadmap — Waves 5-8.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_roadmap/AM — Evolution Roadmap — Waves 5-8.md: 'type' value 'roadmap' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5.2_roadmap/AM — Evolution Roadmap — Waves 5-8.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_roadmap/AM — Evolution Roadmap — Waves 5-8.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/archive/wave_5.2_roadmap/AM — Evolution Roadmap — Waves 5-8.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_memory_architecture/Context Pack Architecture.md: missing required field 'created'
- 05_RECORD/archive/wave_5_memory_architecture/Context Pack Architecture.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_memory_architecture/Context Pack Architecture.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_memory_architecture/Context Pack Architecture.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_memory_architecture/Context Pack Architecture.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_memory_architecture/Knowledge Graph Layer.md: missing required field 'created'
- 05_RECORD/archive/wave_5_memory_architecture/Knowledge Graph Layer.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_memory_architecture/Knowledge Graph Layer.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_memory_architecture/Knowledge Graph Layer.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_memory_architecture/Knowledge Graph Layer.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_memory_architecture/Memory Governance.md: missing required field 'created'
- 05_RECORD/archive/wave_5_memory_architecture/Memory Governance.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_memory_architecture/Memory Governance.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_memory_architecture/Memory Governance.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_memory_architecture/Memory Governance.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_memory_architecture/Memory Model.md: missing required field 'created'
- 05_RECORD/archive/wave_5_memory_architecture/Memory Model.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_memory_architecture/Memory Model.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_memory_architecture/Memory Model.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_memory_architecture/Memory Model.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_memory_architecture/Structured Data Layer.md: missing required field 'created'
- 05_RECORD/archive/wave_5_memory_architecture/Structured Data Layer.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_memory_architecture/Structured Data Layer.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_memory_architecture/Structured Data Layer.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_memory_architecture/Structured Data Layer.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_memory_architecture/Structured Data Registry.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 34, column 3:
      - "[[Structured Data Layer]]"
      ^
- 05_RECORD/archive/wave_5_memory_architecture/Vector Memory Layer.md: missing required field 'created'
- 05_RECORD/archive/wave_5_memory_architecture/Vector Memory Layer.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_memory_architecture/Vector Memory Layer.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_memory_architecture/Vector Memory Layer.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_memory_architecture/Vector Memory Layer.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_agent_systems/Agent Constellation.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 31, column 3:
      - "[[Agent Maestro — Systems Map]]"
      ^
- 05_RECORD/archive/wave_5_agent_systems/Agent Ecosystem.md: missing required field 'created'
- 05_RECORD/archive/wave_5_agent_systems/Agent Ecosystem.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_agent_systems/Agent Ecosystem.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_agent_systems/Agent Ecosystem.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_agent_systems/Agent Ecosystem.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_agent_systems/Agent Runtime Architecture.md: missing required field 'created'
- 05_RECORD/archive/wave_5_agent_systems/Agent Runtime Architecture.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_agent_systems/Agent Runtime Architecture.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_agent_systems/Agent Runtime Architecture.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_agent_systems/Agent Runtime Architecture.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_agent_systems/Agent System Architecture.md: missing required field 'created'
- 05_RECORD/archive/wave_5_agent_systems/Agent System Architecture.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_agent_systems/Agent System Architecture.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_agent_systems/Agent System Architecture.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_agent_systems/Agent System Architecture.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_agent_systems/Agent Workflow Architecture.md: missing required field 'created'
- 05_RECORD/archive/wave_5_agent_systems/Agent Workflow Architecture.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_agent_systems/Agent Workflow Architecture.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_agent_systems/Agent Workflow Architecture.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_agent_systems/Agent Workflow Architecture.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_agent_systems/Evolution Executive.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 34, column 3:
      - "[[Agent Maestro — Strategy]]"
      ^
- 05_RECORD/archive/wave_5_agent_systems/Executive Layer.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 31, column 3:
      - "[[Agent Maestro — Constellati ... 
      ^
- 05_RECORD/archive/wave_5_agent_systems/Executive Orchestrator.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 38, column 3:
      - "[[Agent Maestro — Four-Layer  ... 
      ^
- 05_RECORD/archive/wave_5_agent_systems/Governance Executive.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 36, column 3:
      - "[[Agent Maestro — Authority L ... 
      ^
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 35, column 3:
      - "[[Agent Maestro — Memory Arch ... 
      ^
- 05_RECORD/archive/wave_5_agent_systems/Multi-Agent Systems.md: missing required field 'created'
- 05_RECORD/archive/wave_5_agent_systems/Multi-Agent Systems.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_agent_systems/Multi-Agent Systems.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_agent_systems/Multi-Agent Systems.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_agent_systems/Multi-Agent Systems.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_agent_systems/Operations Executive.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 35, column 3:
      - "[[Agent Maestro — Workflow La ... 
      ^
- 05_RECORD/archive/wave_5_agent_systems/Shared Services.md: missing required field 'created'
- 05_RECORD/archive/wave_5_agent_systems/Shared Services.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_agent_systems/Shared Services.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_agent_systems/Shared Services.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_agent_systems/Shared Services.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_agent_systems/authority_packs.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: authority_index
    ^
expected <block end>, but found '<block sequence start>'
  in "<unicode string>", line 23, column 3:
      - MAP.vault_maintenance
      ^
- 05_RECORD/archive/wave_5_agent_systems/constellation_map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: system_map
    ^
expected <block end>, but found '<block sequence start>'
  in "<unicode string>", line 23, column 3:
      - CONST.vault_maintenance.execut ... 
      ^
- 05_RECORD/archive/wave_5_agent_systems/definition_alignment_auditor.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: agent_definition
    ^
expected <block end>, but found '<block sequence start>'
  in "<unicode string>", line 24, column 3:
      - MAP.vault_maintenance
      ^
- 05_RECORD/archive/wave_5_agent_systems/executive_link.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: agent_definition
    ^
expected <block end>, but found '<block sequence start>'
  in "<unicode string>", line 23, column 3:
      - MAP.vault_maintenance
      ^
- 05_RECORD/archive/wave_5_agent_systems/maintenance_coordinator.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: agent_definition
    ^
expected <block end>, but found '<block sequence start>'
  in "<unicode string>", line 34, column 3:
      - MAP.vault_maintenance
      ^
- 05_RECORD/archive/wave_5_agent_systems/note_processing.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: process
    ^
expected <block end>, but found '<block sequence start>'
  in "<unicode string>", line 23, column 3:
      - MAP.vault_maintenance
      ^
- 05_RECORD/archive/wave_5_agent_systems/note_processor.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: agent_definition
    ^
expected <block end>, but found '<block sequence start>'
  in "<unicode string>", line 24, column 3:
      - MAP.vault_maintenance
      ^
- 05_RECORD/archive/wave_5_agent_systems/on_demand_repair.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: process
    ^
expected <block end>, but found '<block sequence start>'
  in "<unicode string>", line 24, column 3:
      - MAP.vault_maintenance
      ^
- 05_RECORD/archive/wave_5_agent_systems/ontology_integrity_auditor.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: agent_definition
    ^
expected <block end>, but found '<block sequence start>'
  in "<unicode string>", line 24, column 3:
      - MAP.vault_maintenance
      ^
- 05_RECORD/archive/wave_5_agent_systems/scheduled_audit_cycle.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: process
    ^
expected <block end>, but found '<block sequence start>'
  in "<unicode string>", line 26, column 3:
      - MAP.vault_maintenance
      ^
- 05_RECORD/archive/wave_5_agent_systems/self_healing_repairer.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: agent_definition
    ^
expected <block end>, but found '<block sequence start>'
  in "<unicode string>", line 24, column 3:
      - MAP.vault_maintenance
      ^
- 05_RECORD/archive/wave_5_agent_systems/template_compliance_scanner.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: agent_definition
    ^
expected <block end>, but found '<block sequence start>'
  in "<unicode string>", line 24, column 3:
      - MAP.vault_maintenance
      ^
- 05_RECORD/archive/wave_5_infrastructure/AI Org Charts.md: missing required field 'created'
- 05_RECORD/archive/wave_5_infrastructure/AI Org Charts.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_infrastructure/AI Org Charts.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_infrastructure/AI Org Charts.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_infrastructure/AI Org Charts.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_infrastructure/Adoption Patterns.md: missing required field 'created'
- 05_RECORD/archive/wave_5_infrastructure/Adoption Patterns.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_infrastructure/Adoption Patterns.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_infrastructure/Adoption Patterns.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_infrastructure/Adoption Patterns.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_infrastructure/Agent Infrastructure.md: missing required field 'created'
- 05_RECORD/archive/wave_5_infrastructure/Agent Infrastructure.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_infrastructure/Agent Infrastructure.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_infrastructure/Agent Infrastructure.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_infrastructure/Agent Infrastructure.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_infrastructure/Departmental Agents.md: missing required field 'created'
- 05_RECORD/archive/wave_5_infrastructure/Departmental Agents.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_infrastructure/Departmental Agents.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_infrastructure/Departmental Agents.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_infrastructure/Departmental Agents.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_infrastructure/Escalation Models.md: missing required field 'created'
- 05_RECORD/archive/wave_5_infrastructure/Escalation Models.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_infrastructure/Escalation Models.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_infrastructure/Escalation Models.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_infrastructure/Escalation Models.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_infrastructure/Governance Integration.md: missing required field 'created'
- 05_RECORD/archive/wave_5_infrastructure/Governance Integration.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_infrastructure/Governance Integration.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_infrastructure/Governance Integration.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_infrastructure/Governance Integration.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_infrastructure/Observability.md: missing required field 'created'
- 05_RECORD/archive/wave_5_infrastructure/Observability.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_infrastructure/Observability.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_infrastructure/Observability.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_infrastructure/Observability.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_infrastructure/Platformization.md: missing required field 'created'
- 05_RECORD/archive/wave_5_infrastructure/Platformization.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_infrastructure/Platformization.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_infrastructure/Platformization.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_infrastructure/Platformization.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_infrastructure/Workspace Layer.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Agent Infrastructure]]"
      ^
- 05_RECORD/archive/wave_5_authority_architecture/00_identity.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/00_identity.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_2251.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_2251.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_2251.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_2251.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_2251.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_58e4.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_58e4.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_58e4.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_58e4.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_58e4.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_85a0.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_85a0.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_85a0.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_85a0.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_85a0.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8614.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8614.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8614.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8614.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8614.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8d22.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8d22.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8d22.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8d22.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8d22.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_bf68.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_bf68.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_bf68.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_bf68.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_bf68.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_fdde.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_fdde.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_fdde.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_fdde.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_fdde.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/01_scope.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_2c15.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_2c15.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_2c15.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_2c15.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_2c15.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_626d.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_626d.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_626d.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_626d.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_626d.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7e65.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7e65.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7e65.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7e65.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7e65.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7f34.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7f34.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7f34.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7f34.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7f34.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_9aae.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_9aae.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_9aae.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_9aae.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_9aae.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_bfb7.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_bfb7.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_bfb7.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_bfb7.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_bfb7.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_c262.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_c262.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_c262.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_c262.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_c262.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_2822.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_2822.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_2822.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_2822.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_2822.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_590e.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_590e.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_590e.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_590e.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_590e.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_5fe5.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_5fe5.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_5fe5.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_5fe5.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_5fe5.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_b0bf.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_b0bf.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_b0bf.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_b0bf.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_b0bf.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_cf9a.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_cf9a.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_cf9a.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_cf9a.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_cf9a.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_e44f.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_e44f.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_e44f.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_e44f.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_e44f.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_f721.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_f721.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_f721.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_f721.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_f721.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_0f7b.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_0f7b.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_0f7b.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_0f7b.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_0f7b.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_4d39.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_4d39.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_4d39.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_4d39.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_4d39.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_91aa.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_91aa.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_91aa.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_91aa.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_91aa.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_cbd0.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_cbd0.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_cbd0.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_cbd0.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_cbd0.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_e285.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_e285.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_e285.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_e285.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_e285.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fbe8.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fbe8.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fbe8.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fbe8.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fbe8.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fe64.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fe64.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fe64.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fe64.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fe64.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_0dce.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_0dce.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_0dce.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_0dce.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_0dce.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_30e1.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_30e1.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_30e1.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_30e1.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_30e1.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_95ee.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_95ee.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_95ee.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_95ee.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_95ee.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_b8a6.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_b8a6.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_b8a6.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_b8a6.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_b8a6.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_c642.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_c642.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_c642.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_c642.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_c642.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_ce6f.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_ce6f.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_ce6f.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_ce6f.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_ce6f.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_e614.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_e614.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_e614.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_e614.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_e614.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/05_rules.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_0f6e.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_0f6e.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_0f6e.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_0f6e.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_0f6e.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_16a1.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_16a1.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_16a1.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_16a1.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_16a1.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_1dcb.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_1dcb.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_1dcb.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_1dcb.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_1dcb.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_4c7b.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_4c7b.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_4c7b.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_4c7b.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_4c7b.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_8b3b.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_8b3b.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_8b3b.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_8b3b.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_8b3b.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_c40e.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_c40e.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_c40e.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_c40e.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_c40e.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_e057.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_e057.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_e057.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_e057.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_e057.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_11c1.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_11c1.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_11c1.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_11c1.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_11c1.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_166c.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_166c.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_166c.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_166c.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_166c.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_2928.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_2928.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_2928.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_2928.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_2928.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_d84d.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_d84d.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_d84d.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_d84d.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_d84d.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_de4e.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_de4e.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_de4e.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_de4e.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_de4e.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fbfd.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fbfd.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fbfd.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fbfd.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fbfd.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fed8.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fed8.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fed8.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fed8.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fed8.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0e49.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0e49.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0e49.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0e49.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0e49.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0f26.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0f26.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0f26.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0f26.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0f26.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_2c0e.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_2c0e.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_2c0e.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_2c0e.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_2c0e.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_635c.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_635c.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_635c.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_635c.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_635c.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_81d9.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_81d9.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_81d9.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_81d9.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_81d9.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_b821.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_b821.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_b821.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_b821.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_b821.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_d819.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_d819.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_d819.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_d819.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_d819.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0bab.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0bab.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0bab.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0bab.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0bab.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0dd6.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0dd6.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0dd6.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0dd6.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0dd6.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_1933.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_1933.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_1933.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_1933.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_1933.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_20a6.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_20a6.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_20a6.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_20a6.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_20a6.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_332a.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_332a.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_332a.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_332a.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_332a.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_3f98.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_3f98.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_3f98.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_3f98.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_3f98.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_9c3e.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_9c3e.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_9c3e.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_9c3e.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_9c3e.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_112f.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_112f.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_112f.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_112f.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_112f.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_4780.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_4780.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_4780.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_4780.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_4780.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_6af2.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_6af2.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_6af2.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_6af2.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_6af2.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_7983.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_7983.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_7983.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_7983.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_7983.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_99a2.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_99a2.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_99a2.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_99a2.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_99a2.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_e850.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_e850.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_e850.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_e850.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_e850.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_f447.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_f447.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_f447.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_f447.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_f447.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_1bc2.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_1bc2.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_1bc2.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_1bc2.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_1bc2.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_3465.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_3465.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_3465.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_3465.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_3465.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_9daa.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_9daa.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_9daa.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_9daa.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_9daa.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_b374.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_b374.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_b374.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_b374.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_b374.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_c583.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_c583.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_c583.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_c583.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_c583.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_dfa5.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_dfa5.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_dfa5.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_dfa5.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_dfa5.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_f270.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_f270.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_f270.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_f270.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_f270.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_3b31.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_3b31.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_3b31.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_3b31.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_3b31.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_4292.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_4292.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_4292.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_4292.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_4292.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_43d4.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_43d4.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_43d4.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_43d4.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_43d4.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_532d.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_532d.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_532d.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_532d.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_532d.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_9628.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_9628.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_9628.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_9628.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_9628.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_b538.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_b538.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_b538.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_b538.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_b538.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_c9c7.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_c9c7.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_c9c7.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_c9c7.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_c9c7.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_1432.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_1432.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_1432.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_1432.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_1432.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_2f8c.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_2f8c.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_2f8c.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_2f8c.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_2f8c.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_3baf.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_3baf.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_3baf.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_3baf.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_3baf.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_79ed.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_79ed.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_79ed.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_79ed.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_79ed.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_8df9.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_8df9.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_8df9.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_8df9.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_8df9.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_bce6.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_bce6.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_bce6.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_bce6.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_bce6.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_be6e.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_be6e.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_be6e.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_be6e.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_be6e.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_335f.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_335f.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_335f.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_335f.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_335f.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_655d.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_655d.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_655d.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_655d.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_655d.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_8070.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_8070.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_8070.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_8070.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_8070.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_adee.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_adee.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_adee.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_adee.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_adee.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_b46f.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_b46f.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_b46f.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_b46f.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_b46f.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_c63a.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_c63a.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_c63a.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_c63a.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_c63a.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_cd59.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_cd59.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_cd59.md: 'type' value 'authority_pack_section' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_cd59.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_cd59.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/Authority Architecture.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/Authority Architecture.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/Authority Architecture.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/Authority Architecture.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/Authority Architecture.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/Authority Inheritance.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 31, column 3:
      - "[[Authority Architecture Map]]"
      ^
- 05_RECORD/archive/wave_5_authority_architecture/Authority Model.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/Authority Model.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/Authority Model.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/Authority Model.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/Authority Model.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/Authority Pack Compiler.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 31, column 3:
      - "[[Authority Architecture Map]]"
      ^
- 05_RECORD/archive/wave_5_authority_architecture/CLAUDE_12e0.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5_authority_architecture/Compile Failure Semantics.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/Compile Failure Semantics.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/Compile Failure Semantics.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/Compile Failure Semantics.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/Compile Failure Semantics.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/Compiled Governance Artifacts.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/Compiled Governance Artifacts.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/Compiled Governance Artifacts.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/Compiled Governance Artifacts.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/Compiled Governance Artifacts.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Inputs.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Inputs.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Inputs.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Inputs.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Inputs.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Outputs.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Outputs.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Outputs.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Outputs.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Outputs.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Pipeline.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Pipeline.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Pipeline.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Pipeline.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Pipeline.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/Host Bindings.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/Host Bindings.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/Host Bindings.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/Host Bindings.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/Host Bindings.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/Integration Manifest.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/Integration Manifest.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/Integration Manifest.md: 'type' value 'system' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5_authority_architecture/Integration Manifest.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/Integration Manifest.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/Pack Manifest.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 31, column 3:
      - "[[Agent Maestro — Governance  ... 
      ^
- 05_RECORD/archive/wave_5_authority_architecture/Pack Versioning.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 31, column 3:
      - "[[Authority Architecture Map]]"
      ^
- 05_RECORD/archive/wave_5_authority_architecture/compiled_artifact_schema.md: missing required field 'type'
- 05_RECORD/archive/wave_5_authority_architecture/compiled_artifact_schema.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/compiled_artifact_schema.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/compiled_artifact_schema.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5_authority_architecture/compiled_artifact_schema.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/archive/wave_5_authority_architecture/compiled_artifact_schema.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5_authority_architecture/test_repair.md: missing required field 'created'
- 05_RECORD/archive/wave_5_authority_architecture/test_repair.md: missing required field 'updated'
- 05_RECORD/archive/wave_5_authority_architecture/test_repair.md: missing required field 'relationships'
- 05_RECORD/archive/wave_5_authority_architecture/test_repair.md: 'type' value 'note' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/5-Layer Architecture of AI-Native Systems.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/AI Operations Conductor.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/AM North Star v1.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/AM Principles v2.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/AM Vault vs Authority Packs.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Agent Architecture Synthesis.md: missing required field 'created'
- 05_RECORD/archive/pre_wave5/Agent Architecture Synthesis.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Agent Architecture Synthesis.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/pre_wave5/Agent Architecture Synthesis.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/pre_wave5/Agent Deployment Pipeline.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Agent Deployment Pipeline.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/pre_wave5/Agent Deployment Pipeline.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/pre_wave5/Agent Infrastructure Architect.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Agent Maestro 12 Keystone Notes.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Agent Maestro 5 Super Maps.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Agent Maestro Artifacts.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Agent Maestro Domain Structure.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Agent Maestro Knowledge Graph.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Agent Maestro Maps.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Agent Maestro Vault Architecture.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Agent Maestro — Atomic Note Schema.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Agent Maestro — Note Quality Rules.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Agent Maestro — Note Quality Rules.md: missing required field 'created'
- 05_RECORD/archive/pre_wave5/Agent Maestro — Note Quality Rules.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Agent Maestro — Note Quality Rules.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/pre_wave5/Agent Maestro — Note Quality Rules.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/pre_wave5/Authority Model of an AI-Native System.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Authority Pack - Definition.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Authority Pack Compiler - Definition.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Authority Pack Grammar v1.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Canonical Artifact Taxonomy for AI-Native Systems.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Claude Vault Build Prompt.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Claude Vault Build Prompt.md: missing required field 'authority_weight'
- 05_RECORD/archive/pre_wave5/Claude Vault Build Prompt.md: missing required field 'schema_version'
- 05_RECORD/archive/pre_wave5/Claude Vault Build Prompt.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Claude Vault Build Prompt.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/Claude Vault Build Prompt.md: missing required field 'tags'
- 05_RECORD/archive/pre_wave5/Controlled Vault Repair Operation v1.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Definition Alignment Audit - Concepts.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Definition Alignment Audit v1.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Definition Alignment Audit v1.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Definition Alignment Audit v1.md: 'created' is not ISO 8601 format: 'None'
- 05_RECORD/archive/pre_wave5/Definition Alignment Audit v1.md: 'updated' is not ISO 8601 format: 'None'
- 05_RECORD/archive/pre_wave5/Definition Alignment Audit v1.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/pre_wave5/Definition Alignment Audit v1.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/pre_wave5/Definitions.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Development Pipeline.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Development Pipeline.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/pre_wave5/Development Pipeline.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/pre_wave5/Exploration Pipeline.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Exploration Pipeline.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/pre_wave5/Exploration Pipeline.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/pre_wave5/Frontmatter Update v1.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Frontmatter Upgrade Checklist.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Frontmatter Upgrade Checklist.md: missing required field 'created'
- 05_RECORD/archive/pre_wave5/Frontmatter Upgrade Checklist.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Frontmatter Upgrade Checklist.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/pre_wave5/Frontmatter Upgrade Checklist.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/pre_wave5/Frontmatter Upgrade v1.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Inception.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Intelligence Trainer.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Learning Pipeline.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Learning Pipeline.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/pre_wave5/Learning Pipeline.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: missing required field 'created'
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: 'type' value 'index' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/pre_wave5/Modes.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Modes.md: missing required field 'authority_weight'
- 05_RECORD/archive/pre_wave5/Modes.md: missing required field 'schema_version'
- 05_RECORD/archive/pre_wave5/Modes.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Modes.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/Modes.md: 'type' value 'modes' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Modes_v0.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Modes_v0.md: missing required field 'status'
- 05_RECORD/archive/pre_wave5/Modes_v0.md: missing required field 'authority_weight'
- 05_RECORD/archive/pre_wave5/Modes_v0.md: missing required field 'schema_version'
- 05_RECORD/archive/pre_wave5/Modes_v0.md: missing required field 'created'
- 05_RECORD/archive/pre_wave5/Modes_v0.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Modes_v0.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/Modes_v0.md: missing required field 'tags'
- 05_RECORD/archive/pre_wave5/Modes_v0.md: 'type' value 'modes' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Nort Star.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Nort Star.md: missing required field 'authority_weight'
- 05_RECORD/archive/pre_wave5/Nort Star.md: missing required field 'schema_version'
- 05_RECORD/archive/pre_wave5/Nort Star.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Nort Star.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/Nort Star.md: 'type' value 'north_star' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Nort Star.md: 'created' is not ISO 8601 format: 'YYYY-MM-DD'
- 05_RECORD/archive/pre_wave5/North Star.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/North Star.md: missing required field 'authority_weight'
- 05_RECORD/archive/pre_wave5/North Star.md: missing required field 'schema_version'
- 05_RECORD/archive/pre_wave5/North Star.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/North Star.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/North Star.md: 'type' value 'north_star' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Note Knowledge Upgrade Order.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Note Knowledge Upgrade Order.md: missing required field 'created'
- 05_RECORD/archive/pre_wave5/Note Knowledge Upgrade Order.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Note Knowledge Upgrade Order.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/pre_wave5/Note Knowledge Upgrade Order.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/pre_wave5/Phases of Growth.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Pipeline Template — Legacy.md: missing required field 'created'
- 05_RECORD/archive/pre_wave5/Pipeline Template — Legacy.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Pipeline Template — Legacy.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/pre_wave5/Pipeline Template — Legacy.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/pre_wave5/Portable Authority Pack - Inception.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Potential Authority Pack Templates.md: missing required field 'created'
- 05_RECORD/archive/pre_wave5/Potential Authority Pack Templates.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Potential Authority Pack Templates.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/Potential Authority Pack Templates.md: missing required field 'tags'
- 05_RECORD/archive/pre_wave5/Potential Authority Pack Templates.md: 'type' value 'archive' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Potential Roadmap — Authority Packs.md: missing required field 'created'
- 05_RECORD/archive/pre_wave5/Potential Roadmap — Authority Packs.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Potential Roadmap — Authority Packs.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/Potential Roadmap — Authority Packs.md: missing required field 'tags'
- 05_RECORD/archive/pre_wave5/Potential Roadmap — Authority Packs.md: 'type' value 'archive' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Principles.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Principles.md: missing required field 'authority_weight'
- 05_RECORD/archive/pre_wave5/Principles.md: missing required field 'schema_version'
- 05_RECORD/archive/pre_wave5/Principles.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Principles.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/Principles.md: 'type' value 'principle_set' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Principles_v0.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Principles_v0.md: missing required field 'authority_weight'
- 05_RECORD/archive/pre_wave5/Principles_v0.md: missing required field 'schema_version'
- 05_RECORD/archive/pre_wave5/Principles_v0.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Principles_v0.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/Principles_v0.md: missing required field 'tags'
- 05_RECORD/archive/pre_wave5/Principles_v0.md: 'type' value 'principles' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Principles_v0.md: 'created' is not ISO 8601 format: 'YYYY-MM-DD'
- 05_RECORD/archive/pre_wave5/Roadmap 01.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Roadmap.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Roadmap.md: missing required field 'authority_weight'
- 05_RECORD/archive/pre_wave5/Roadmap.md: missing required field 'schema_version'
- 05_RECORD/archive/pre_wave5/Roadmap.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Roadmap.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/Roadmap.md: 'type' value 'roadmap' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Roadmap_v0.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Roadmap_v0.md: missing required field 'status'
- 05_RECORD/archive/pre_wave5/Roadmap_v0.md: missing required field 'authority_weight'
- 05_RECORD/archive/pre_wave5/Roadmap_v0.md: missing required field 'schema_version'
- 05_RECORD/archive/pre_wave5/Roadmap_v0.md: missing required field 'created'
- 05_RECORD/archive/pre_wave5/Roadmap_v0.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Roadmap_v0.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/Roadmap_v0.md: missing required field 'tags'
- 05_RECORD/archive/pre_wave5/Roadmap_v0.md: 'type' value 'roadmap' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Scope.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Scope.md: missing required field 'authority_weight'
- 05_RECORD/archive/pre_wave5/Scope.md: missing required field 'schema_version'
- 05_RECORD/archive/pre_wave5/Scope.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Scope.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/Scope.md: 'type' value 'scope' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Scope_v0.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Scope_v0.md: missing required field 'status'
- 05_RECORD/archive/pre_wave5/Scope_v0.md: missing required field 'authority_weight'
- 05_RECORD/archive/pre_wave5/Scope_v0.md: missing required field 'schema_version'
- 05_RECORD/archive/pre_wave5/Scope_v0.md: missing required field 'created'
- 05_RECORD/archive/pre_wave5/Scope_v0.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Scope_v0.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/Scope_v0.md: missing required field 'tags'
- 05_RECORD/archive/pre_wave5/Scope_v0.md: 'type' value 'scope' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Starter Note Set.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Strategy.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Strategy.md: missing required field 'authority_weight'
- 05_RECORD/archive/pre_wave5/Strategy.md: missing required field 'schema_version'
- 05_RECORD/archive/pre_wave5/Strategy.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Strategy.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/Strategy.md: 'type' value 'strategy' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Strategy_v0.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Strategy_v0.md: missing required field 'authority_weight'
- 05_RECORD/archive/pre_wave5/Strategy_v0.md: missing required field 'schema_version'
- 05_RECORD/archive/pre_wave5/Strategy_v0.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Strategy_v0.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/Strategy_v0.md: missing required field 'tags'
- 05_RECORD/archive/pre_wave5/Strategy_v0.md: 'type' value 'strategy' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Strategy_v0.md: 'created' is not ISO 8601 format: 'YYYY-MM-DD'
- 05_RECORD/archive/pre_wave5/Structure & Knowledge Upgrade Prompt v1.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Structure And Knowledge Upgrade v1.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/System Design Pipeline.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/System Design Pipeline.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/pre_wave5/System Design Pipeline.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/pre_wave5/Target Repo Structure.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/The 5-Layer Architecture of Real Agent Systems & Control Substrate.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Vault Integrity & Self-Healing Audit v1.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Vault Rules Fragment.md: missing required field 'created'
- 05_RECORD/archive/pre_wave5/Vault Rules Fragment.md: missing required field 'updated'
- 05_RECORD/archive/pre_wave5/Vault Rules Fragment.md: missing required field 'relationships'
- 05_RECORD/archive/pre_wave5/Vault Rules Fragment.md: missing required field 'tags'
- 05_RECORD/archive/pre_wave5/Vault Rules Fragment.md: 'type' value 'archive' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Vault Structure and Knowledge Upgrade v0.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/Vault Structure and Knowledge Upgrade v1.md: missing required field 'title'
- 05_RECORD/archive/pre_wave5/Vault Structure and Knowledge Upgrade v1.md: 'type' value 'process' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/pre_wave5/Vault Structure and Knowledge Upgrade v1.md: 'created' is not ISO 8601 format: 'None'
- 05_RECORD/archive/pre_wave5/Vault Structure and Knowledge Upgrade v1.md: 'updated' is not ISO 8601 format: 'None'
- 05_RECORD/archive/pre_wave5/Vault Structure and Knowledge Upgrade v1.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/pre_wave5/Vault Structure and Knowledge Upgrade v1.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/pre_wave5/Workflow Architect.md: no YAML frontmatter found
- 05_RECORD/archive/pre_wave5/authority_packs.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 33, column 3:
      - "[[Authority Architecture Map]]"
      ^
- 05_RECORD/archive/pre_wave5/constellation_map.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines:
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 33, column 3:
      - "[[Agent Maestro — Systems Map]]"
      ^
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: agent_definition
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 36, column 1:
    - '[[Agent Maestro — Constellati ... 
    ^
- 05_RECORD/archive/pre_wave5/link_auditor.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 37, column 3:
      - "[[Agent Maestro — Constellati ... 
      ^
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    type: workflow_definition
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 34, column 1:
    - '[[Agent Maestro — Constellati ... 
    ^
- 05_RECORD/archive/pre_wave5/orphan_detector.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 37, column 3:
      - "[[Agent Maestro — Constellati ... 
      ^
- 05_RECORD/archive/pre_wave5/schema_validator.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 37, column 3:
      - "[[Agent Maestro — Constellati ... 
      ^
- 05_RECORD/archive/pre_wave5/vault_governance_director.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 39, column 3:
      - "[[Agent Maestro — Constellati ... 
      ^
- 05_RECORD/archive/pre_wave5/workspace_readme.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_concepts/AM — Wave 5 — Audit Framework Rubric.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/AM — Wave 5 — Audit Framework Rubric.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/AM — Wave 5 — Audit Framework Rubric.md: 'type' value 'reference' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5.2_concepts/AM — Wave 5 — Audit Framework Rubric.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/AM — Wave 5 — Audit Framework Rubric.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Agent Constellation.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 34, column 3:
      - "[[Agent Maestro — Constellati ... 
      ^
- 05_RECORD/archive/wave_5.2_concepts/Agent Ecosystem.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 29, column 3:
      - "[[Agent Maestro — Systems Map]]"
      ^
- 05_RECORD/archive/wave_5.2_concepts/Agent Maestro Layer Model.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 33, column 3:
      - "[[Agent Maestro — Stack Map]]"
      ^
- 05_RECORD/archive/wave_5.2_concepts/Agent Maestro Vault Build.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Agent Maestro Vault Build.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Agent Maestro Vault Build.md: 'type' value 'project' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5.2_concepts/Agent Maestro Vault Build.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Agent Maestro Vault Build.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Agent Orchestration.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Agent Orchestration.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Agent Orchestration.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Agent Orchestration.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Agent Organization Architecture.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Agent Organization Architecture.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Agent Organization Architecture.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Agent Organization Architecture.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Agent System.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 30, column 3:
      - "[[Agent Maestro — Systems Map]]"
      ^
- 05_RECORD/archive/wave_5.2_concepts/Agent Systems.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Agent Systems.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Agent Systems.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Agent Systems.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Agent Workflow.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Agent Workflow.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Agent Workflow.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Agent Workflow.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Agent.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Agent.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Agent.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Agent.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Authority Architecture.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Authority Architecture.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Authority Architecture.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Authority Architecture.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Authority Inheritance.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 29, column 3:
      - "[[Agent Maestro — Pack Inheri ... 
      ^
- 05_RECORD/archive/wave_5.2_concepts/Authority Model.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines:
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 34, column 3:
      - "[[Authority Architecture Map]]"
      ^
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack Compiler.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack Compiler.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack Compiler.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack Compiler.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack Versioning and Inheritance.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack Versioning and Inheritance.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack Versioning and Inheritance.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack Versioning and Inheritance.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Build Session Protocol.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Build Session Protocol.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Build Session Protocol.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Build Session Protocol.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Compiled Governance Artifact.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 34, column 3:
      - "[[Agent Maestro — Governance  ... 
      ^
- 05_RECORD/archive/wave_5.2_concepts/Compiler Artifact Schemas Reference.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Compiler Artifact Schemas Reference.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Compiler Artifact Schemas Reference.md: 'type' value 'reference' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5.2_concepts/Compiler Artifact Schemas Reference.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Compiler Artifact Schemas Reference.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Consolidation Pipeline.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Consolidation Pipeline.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Consolidation Pipeline.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Consolidation Pipeline.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Context Pack.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Context Pack.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Context Pack.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Context Pack.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Decision Authority.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Decision Authority.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Decision Authority.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Decision Authority.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Escalation Classes Reference.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Escalation Classes Reference.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Escalation Classes Reference.md: 'type' value 'reference' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5.2_concepts/Escalation Classes Reference.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Escalation Classes Reference.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Execution Architecture.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Execution Architecture.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Execution Architecture.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Execution Architecture.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Execution Authority.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Execution Authority.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Execution Authority.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Execution Authority.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Executive Agent.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 31, column 3:
      - "[[Agent Maestro — Concepts Map]]"
      ^
- 05_RECORD/archive/wave_5.2_concepts/Git Best Practices for AI-Assisted Builds v1.md: no YAML frontmatter found
- 05_RECORD/archive/wave_5.2_concepts/Governance Artifact.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 34, column 3:
      - "[[Agent Maestro — Governance  ... 
      ^
- 05_RECORD/archive/wave_5.2_concepts/Governance Schemas Reference.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Governance Schemas Reference.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Governance Schemas Reference.md: 'type' value 'reference' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5.2_concepts/Governance Schemas Reference.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Governance Schemas Reference.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Host Binding.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 22, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 33, column 3:
      - "[[Authority Pack Compiler — M ... 
      ^
- 05_RECORD/archive/wave_5.2_concepts/Host Options Evaluation.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Host Options Evaluation.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Host Options Evaluation.md: 'type' value 'reference' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5.2_concepts/Host Options Evaluation.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Host Options Evaluation.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/archive/wave_5.2_concepts/Host Options Evaluation.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Host Runtime Reference.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Host Runtime Reference.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Host Runtime Reference.md: 'type' value 'reference' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5.2_concepts/Host Runtime Reference.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Host Runtime Reference.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Human Escalation.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Human Escalation.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Human Escalation.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Human Escalation.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/LLM-Script Boundary Reference.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/LLM-Script Boundary Reference.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/LLM-Script Boundary Reference.md: 'type' value 'reference' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5.2_concepts/LLM-Script Boundary Reference.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/LLM-Script Boundary Reference.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Maintenance Pipeline.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Maintenance Pipeline.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Maintenance Pipeline.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Maintenance Pipeline.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Memory Architecture.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Memory Architecture.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Memory Architecture.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Memory Architecture.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Model Workspace Protocol.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 32, column 3:
      - "[[Agent Maestro — Systems Map]]"
      ^
- 05_RECORD/archive/wave_5.2_concepts/Note Upgrade Workflow.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Note Upgrade Workflow.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Note Upgrade Workflow.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Note Upgrade Workflow.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Operational Intelligence.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Operational Intelligence.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Operational Intelligence.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Operational Intelligence.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Operational Outcome.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Operational Outcome.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Operational Outcome.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Operational Outcome.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Pack Versioning.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 28, column 3:
      - "[[Agent Maestro — Pack Inheri ... 
      ^
- 05_RECORD/archive/wave_5.2_concepts/Pure Agent Concepts.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Pure Agent Concepts.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Pure Agent Concepts.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Pure Agent Concepts.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Registry Anchoring.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Registry Anchoring.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Registry Anchoring.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Registry Anchoring.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Self-Observation Specification.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Self-Observation Specification.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Self-Observation Specification.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Self-Observation Specification.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/archive/wave_5.2_concepts/Self-Observation Specification.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Shared Services.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 29, column 3:
      - "[[Agent Maestro — Systems Map]]"
      ^
- 05_RECORD/archive/wave_5.2_concepts/Specialist Agent.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 29, column 3:
      - "[[Agent Maestro — Concepts Map]]"
      ^
- 05_RECORD/archive/wave_5.2_concepts/Supervisor Agent.md: YAML parse error: while parsing a block mapping
  in "<unicode string>", line 17, column 3:
      defines: []
      ^
expected <block end>, but found '-'
  in "<unicode string>", line 30, column 3:
      - "[[Agent Maestro — Concepts Map]]"
      ^
- 05_RECORD/archive/wave_5.2_concepts/Tool Registry Design.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Tool Registry Design.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Tool Registry Design.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Tool Registry Design.md: 'relationships' missing sub-field 'related'
- 05_RECORD/archive/wave_5.2_concepts/Tool and Action Class Reference.md: missing required field 'created'
- 05_RECORD/archive/wave_5.2_concepts/Tool and Action Class Reference.md: missing required field 'updated'
- 05_RECORD/archive/wave_5.2_concepts/Tool and Action Class Reference.md: 'type' value 'reference' not in allowed values ['governance', 'concept', 'skill', 'role', 'pipeline', 'log', 'report', 'proposal']
- 05_RECORD/archive/wave_5.2_concepts/Tool and Action Class Reference.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/archive/wave_5.2_concepts/Tool and Action Class Reference.md: 'relationships' missing sub-field 'related'
- 05_RECORD/logs/sessions/Session Log — SES-002 — 2026-03-14.md: missing required field 'created'
- 05_RECORD/logs/sessions/Session Log — SES-002 — 2026-03-14.md: missing required field 'updated'
- 05_RECORD/logs/sessions/Session Log — SES-002 — 2026-03-14.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/logs/sessions/Session Log — SES-002 — 2026-03-14.md: 'relationships' missing sub-field 'related'
- 05_RECORD/logs/sessions/Session Log — SES-003 — 2026-03-14.md: missing required field 'type'
- 05_RECORD/logs/sessions/Session Log — SES-003 — 2026-03-14.md: missing required field 'created'
- 05_RECORD/logs/sessions/Session Log — SES-003 — 2026-03-14.md: missing required field 'updated'
- 05_RECORD/logs/sessions/Session Log — SES-003 — 2026-03-14.md: 'status' value 'completed' not in allowed values ['draft', 'active', 'archived']
- 05_RECORD/logs/sessions/Session Log — SES-003 — 2026-03-14.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/logs/sessions/Session Log — SES-003 — 2026-03-14.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/logs/sessions/Session Log — SES-003 — 2026-03-14.md: 'relationships' missing sub-field 'related'
- 05_RECORD/logs/sessions/Session Log — SES-004 — 2026-03-15.md: missing required field 'type'
- 05_RECORD/logs/sessions/Session Log — SES-004 — 2026-03-15.md: missing required field 'created'
- 05_RECORD/logs/sessions/Session Log — SES-004 — 2026-03-15.md: missing required field 'updated'
- 05_RECORD/logs/sessions/Session Log — SES-004 — 2026-03-15.md: 'status' value 'completed' not in allowed values ['draft', 'active', 'archived']
- 05_RECORD/logs/sessions/Session Log — SES-004 — 2026-03-15.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/logs/sessions/Session Log — SES-004 — 2026-03-15.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/logs/sessions/Session Log — SES-004 — 2026-03-15.md: 'relationships' missing sub-field 'related'
- 05_RECORD/logs/sessions/Session Log — SES-005 — 2026-03-15.md: missing required field 'type'
- 05_RECORD/logs/sessions/Session Log — SES-005 — 2026-03-15.md: missing required field 'created'
- 05_RECORD/logs/sessions/Session Log — SES-005 — 2026-03-15.md: missing required field 'updated'
- 05_RECORD/logs/sessions/Session Log — SES-005 — 2026-03-15.md: 'status' value 'completed' not in allowed values ['draft', 'active', 'archived']
- 05_RECORD/logs/sessions/Session Log — SES-005 — 2026-03-15.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/logs/sessions/Session Log — SES-005 — 2026-03-15.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/logs/sessions/Session Log — SES-005 — 2026-03-15.md: 'relationships' missing sub-field 'related'
- 05_RECORD/logs/sessions/Session Log — SES-006 — 2026-03-15.md: missing required field 'type'
- 05_RECORD/logs/sessions/Session Log — SES-006 — 2026-03-15.md: missing required field 'created'
- 05_RECORD/logs/sessions/Session Log — SES-006 — 2026-03-15.md: missing required field 'updated'
- 05_RECORD/logs/sessions/Session Log — SES-006 — 2026-03-15.md: 'status' value 'completed' not in allowed values ['draft', 'active', 'archived']
- 05_RECORD/logs/sessions/Session Log — SES-006 — 2026-03-15.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/logs/sessions/Session Log — SES-006 — 2026-03-15.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/logs/sessions/Session Log — SES-006 — 2026-03-15.md: 'relationships' missing sub-field 'related'
- 05_RECORD/logs/sessions/Session Log — SES-007 — 2026-03-15.md: missing required field 'type'
- 05_RECORD/logs/sessions/Session Log — SES-007 — 2026-03-15.md: missing required field 'created'
- 05_RECORD/logs/sessions/Session Log — SES-007 — 2026-03-15.md: missing required field 'updated'
- 05_RECORD/logs/sessions/Session Log — SES-007 — 2026-03-15.md: 'status' value 'completed' not in allowed values ['draft', 'active', 'archived']
- 05_RECORD/logs/sessions/Session Log — SES-007 — 2026-03-15.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/logs/sessions/Session Log — SES-007 — 2026-03-15.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/logs/sessions/Session Log — SES-007 — 2026-03-15.md: 'relationships' missing sub-field 'related'
- 05_RECORD/logs/sessions/Session Log — SES-008 — 2026-03-15.md: missing required field 'type'
- 05_RECORD/logs/sessions/Session Log — SES-008 — 2026-03-15.md: missing required field 'created'
- 05_RECORD/logs/sessions/Session Log — SES-008 — 2026-03-15.md: missing required field 'updated'
- 05_RECORD/logs/sessions/Session Log — SES-008 — 2026-03-15.md: 'status' value 'completed' not in allowed values ['draft', 'active', 'archived']
- 05_RECORD/logs/sessions/Session Log — SES-008 — 2026-03-15.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/logs/sessions/Session Log — SES-008 — 2026-03-15.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/logs/sessions/Session Log — SES-008 — 2026-03-15.md: 'relationships' missing sub-field 'related'
- 05_RECORD/logs/sessions/Session Log — SES-009 — 2026-03-15.md: missing required field 'created'
- 05_RECORD/logs/sessions/Session Log — SES-009 — 2026-03-15.md: missing required field 'updated'
- 05_RECORD/logs/sessions/Session Log — SES-009 — 2026-03-15.md: 'status' value 'completed' not in allowed values ['draft', 'active', 'archived']
- 05_RECORD/logs/sessions/Session Log — SES-009 — 2026-03-15.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/logs/sessions/Session Log — SES-009 — 2026-03-15.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/logs/sessions/Session Log — SES-009 — 2026-03-15.md: 'relationships' missing sub-field 'related'
- 05_RECORD/logs/sessions/Session Log — SES-010 — 2026-03-15.md: missing required field 'type'
- 05_RECORD/logs/sessions/Session Log — SES-010 — 2026-03-15.md: missing required field 'created'
- 05_RECORD/logs/sessions/Session Log — SES-010 — 2026-03-15.md: missing required field 'updated'
- 05_RECORD/logs/sessions/Session Log — SES-010 — 2026-03-15.md: 'status' value 'completed' not in allowed values ['draft', 'active', 'archived']
- 05_RECORD/logs/sessions/Session Log — SES-010 — 2026-03-15.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/logs/sessions/Session Log — SES-010 — 2026-03-15.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/logs/sessions/Session Log — SES-010 — 2026-03-15.md: 'relationships' missing sub-field 'related'
- 05_RECORD/logs/sessions/Session Log — SES-012 — 2026-03-15.md: missing required field 'created'
- 05_RECORD/logs/sessions/Session Log — SES-012 — 2026-03-15.md: missing required field 'updated'
- 05_RECORD/logs/sessions/Session Log — SES-012 — 2026-03-15.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/logs/sessions/Session Log — SES-012 — 2026-03-15.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/logs/sessions/Session Log — SES-012 — 2026-03-15.md: 'relationships' missing sub-field 'related'
- 05_RECORD/logs/sessions/Session Log — SES-013 — 2026-03-15.md: missing required field 'created'
- 05_RECORD/logs/sessions/Session Log — SES-013 — 2026-03-15.md: missing required field 'updated'
- 05_RECORD/logs/sessions/Session Log — SES-013 — 2026-03-15.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/logs/sessions/Session Log — SES-013 — 2026-03-15.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/logs/sessions/Session Log — SES-013 — 2026-03-15.md: 'relationships' missing sub-field 'related'
- 05_RECORD/logs/sessions/Session Log — SES-014 — 2026-03-15.md: missing required field 'created'
- 05_RECORD/logs/sessions/Session Log — SES-014 — 2026-03-15.md: missing required field 'updated'
- 05_RECORD/logs/sessions/Session Log — SES-014 — 2026-03-15.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/logs/sessions/Session Log — SES-014 — 2026-03-15.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/logs/sessions/Session Log — SES-014 — 2026-03-15.md: 'relationships' missing sub-field 'related'
- 05_RECORD/logs/sessions/Session Log — SES-015 — 2026-03-15.md: missing required field 'created'
- 05_RECORD/logs/sessions/Session Log — SES-015 — 2026-03-15.md: missing required field 'updated'
- 05_RECORD/logs/sessions/Session Log — SES-015 — 2026-03-15.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/logs/sessions/Session Log — SES-015 — 2026-03-15.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/logs/sessions/Session Log — SES-015 — 2026-03-15.md: 'relationships' missing sub-field 'related'
- 05_RECORD/logs/sessions/Session Log — SES-016 — 2026-03-15.md: missing required field 'created'
- 05_RECORD/logs/sessions/Session Log — SES-016 — 2026-03-15.md: missing required field 'updated'
- 05_RECORD/logs/sessions/Session Log — SES-016 — 2026-03-15.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/logs/sessions/Session Log — SES-016 — 2026-03-15.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/logs/sessions/Session Log — SES-016 — 2026-03-15.md: 'relationships' missing sub-field 'related'
- 05_RECORD/logs/sessions/Session Log — SES-017 — 2026-03-15.md: missing required field 'created'
- 05_RECORD/logs/sessions/Session Log — SES-017 — 2026-03-15.md: missing required field 'updated'
- 05_RECORD/logs/sessions/Session Log — SES-017 — 2026-03-15.md: 'relationships' missing sub-field 'derives_from'
- 05_RECORD/logs/sessions/Session Log — SES-017 — 2026-03-15.md: 'relationships' missing sub-field 'governs'
- 05_RECORD/logs/sessions/Session Log — SES-017 — 2026-03-15.md: 'relationships' missing sub-field 'related'

### Broken Links


- 02_KNOWLEDGE/concepts/Authority Architecture.md: broken wiki-link [[Role — Worker\]]
- 02_KNOWLEDGE/concepts/Authority Architecture.md: broken wiki-link [[Agent Maestro — Foundations\]]
- 02_KNOWLEDGE/concepts/Authority Architecture.md: broken wiki-link [[Role — Reviewer\]]
- 02_KNOWLEDGE/governance/Agent Maestro — Vault Rules.md: broken wiki-link [[Note Title]]
- 02_KNOWLEDGE/skills/Skill — Validate.md: broken wiki-link [[...]]
- 02_KNOWLEDGE/templates/Template — Concept.md: concept note has zero body wiki-links
- 02_KNOWLEDGE/templates/Template — Governance.md: governance note has zero body wiki-links
- 03_DECIDE/active/Proposal — Wave 6 Mechanical Integrity.md: broken wiki-link [[wiki-links]]
- 03_DECIDE/active/Proposal — Wave 6 Mechanical Integrity.md: broken wiki-link [[wiki-links]]
- 05_RECORD/archive/Wave 5.2 — Phase 4 Capture Seed.md: broken wiki-link [[Wave 5.2 — Phases 1–3 Retrospective]]
- 05_RECORD/archive/Wave 5.2 — Phase 4 Capture Seed.md: broken relationship link 'Wave 5.2 — Phases 1–3 Retrospective'
- 05_RECORD/archive/pre_wave5/Agent Deployment Pipeline.md: broken wiki-link [[02_Systems/Agent Maestro/03_PIPELINES/development/Development Pipeline]]
- 05_RECORD/archive/pre_wave5/Agent Deployment Pipeline.md: broken wiki-link [[02_Systems/Agent Maestro/03_PIPELINES/development/Development Pipeline]]
- 05_RECORD/archive/pre_wave5/Agent Deployment Pipeline.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
- 05_RECORD/archive/pre_wave5/Agent Maestro — Note Quality Rules.md: broken relationship link '02_KNOWLEDGE'
- 05_RECORD/archive/pre_wave5/Claude Vault Build Prompt.md: broken wiki-link [[Claude Note Quality Rules]]
- 05_RECORD/archive/pre_wave5/Frontmatter Upgrade Checklist.md: broken relationship link '02_KNOWLEDGE'
- 05_RECORD/archive/pre_wave5/Learning Pipeline.md: broken wiki-link [[02_Systems/Agent Maestro/03_PIPELINES/development/Development Pipeline]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Ecosystem]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Inheritance]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Model]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/01_CAPTURE/inbox/Authority Pack Compiler]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Pack Versioning]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/domains/Platformization]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Shared Services]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Bartram/06_EXECUTION/tasks/Next Steps]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Bartram/06_EXECUTION/tasks/To Do]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/06_EXECUTION/weekly_planning/Weekly Reset Template]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/03_PIPELINES/development/Development Pipeline]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Bartram/03_PIPELINES/maintenance_pipeline/Maintenance Pipeline]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/02_authority_domain]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/06_control_gates]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/09_decision_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/07_evidence_requirements]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/10_execution_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/13_extension_points]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/12_failure_semantics]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/04_governed_actions]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/03_governed_entities]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/00_identity]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/11_integration_contract]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/05_rules]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/01_scope]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/08_state_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/02_authority_domain]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/06_control_gates]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/09_decision_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/07_evidence_requirements]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/10_execution_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/13_extension_points]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/12_failure_semantics]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/04_governed_actions]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/03_governed_entities]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/00_identity]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/11_integration_contract]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/05_rules]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/01_scope]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/08_state_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/02_authority_domain]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/06_control_gates]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/09_decision_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/07_evidence_requirements]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/10_execution_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/13_extension_points]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/12_failure_semantics]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/04_governed_actions]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/03_governed_entities]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/00_identity]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/11_integration_contract]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/05_rules]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/01_scope]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/08_state_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/02_authority_domain]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/06_control_gates]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/09_decision_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/07_evidence_requirements]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/10_execution_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/13_extension_points]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/12_failure_semantics]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/04_governed_actions]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/03_governed_entities]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/00_identity]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/11_integration_contract]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/05_rules]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/01_scope]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/08_state_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/02_authority_domain]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/06_control_gates]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/09_decision_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/07_evidence_requirements]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/10_execution_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/13_extension_points]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/12_failure_semantics]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/04_governed_actions]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/03_governed_entities]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/00_identity]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/11_integration_contract]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/05_rules]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/01_scope]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/08_state_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/02_authority_domain]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/06_control_gates]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/09_decision_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/07_evidence_requirements]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/10_execution_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/13_extension_points]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/12_failure_semantics]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/04_governed_actions]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/03_governed_entities]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/00_identity]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/11_integration_contract]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/05_rules]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/01_scope]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/08_state_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/02_authority_domain]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/06_control_gates]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/09_decision_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/07_evidence_requirements]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/10_execution_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/13_extension_points]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/12_failure_semantics]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/04_governed_actions]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/03_governed_entities]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/00_identity]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/11_integration_contract]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/05_rules]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/01_scope]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/08_state_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/02_authority_domain]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/06_control_gates]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/09_decision_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/07_evidence_requirements]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/10_execution_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/13_extension_points]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/12_failure_semantics]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/04_governed_actions]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/03_governed_entities]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/00_identity]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/11_integration_contract]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/05_rules]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/01_scope]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/memory_authority/08_state_interaction]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Ecosystem]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Inheritance]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Model]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/domains/Platformization]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Pack Versioning]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Shared Services]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/indexes/Glossary]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/indexes/System Registry]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/99_ARCHIVE/AGENT_MAESTRO/99_ARCHIVE/Modes]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Obsidian/88_TEMPLATES/system_governance/Principles]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/99_ARCHIVE/AGENT_MAESTRO/99_ARCHIVE/Roadmap]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/99_ARCHIVE/AGENT_MAESTRO/99_ARCHIVE/Scope]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Bartram/04_PROJECTS/production_pipeline/playbook/Strategy]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[Claude Note Quality Rules]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/99_ARCHIVE/AGENT_MAESTRO/99_ARCHIVE/Modes]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Obsidian/88_TEMPLATES/system_governance/North Star]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Obsidian/88_TEMPLATES/system_governance/Principles]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/99_ARCHIVE/AGENT_MAESTRO/99_ARCHIVE/Roadmap]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Agent Maestro/99_ARCHIVE/AGENT_MAESTRO/99_ARCHIVE/Scope]]
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: broken wiki-link [[02_Systems/Bartram/04_PROJECTS/production_pipeline/playbook/Strategy]]
- 05_RECORD/archive/pre_wave5/Note Knowledge Upgrade Order.md: broken relationship link '02_KNOWLEDGE'
- 05_RECORD/archive/pre_wave5/System Design Pipeline.md: broken wiki-link [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/Authority Architecture]]
- 05_RECORD/archive/pre_wave5/System Design Pipeline.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
- 05_RECORD/archive/pre_wave5/authority_packs.md: broken wiki-link [[Vault Curator constellation]]
- 05_RECORD/archive/pre_wave5/authority_packs.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
- 05_RECORD/archive/pre_wave5/authority_packs.md: broken wiki-link [[CONST.vault_curator.agent.executive]]
- 05_RECORD/archive/pre_wave5/authority_packs.md: broken wiki-link [[CONST.vault_curator.agent.supervisor]]
- 05_RECORD/archive/pre_wave5/authority_packs.md: broken relationship link 'CONST.vault_curator.map'
- 05_RECORD/archive/pre_wave5/authority_packs.md: broken relationship link 'Vault Curator constellation'
- 05_RECORD/archive/pre_wave5/constellation_map.md: broken relationship link 'CONST.vault_curator.agent.executive'
- 05_RECORD/archive/pre_wave5/constellation_map.md: broken relationship link 'CONST.vault_curator.agent.supervisor'
- 05_RECORD/archive/pre_wave5/constellation_map.md: broken relationship link 'CONST.vault_curator.agent.specialist.link_auditor'
- 05_RECORD/archive/pre_wave5/constellation_map.md: broken relationship link 'CONST.vault_curator.agent.specialist.schema_validator'
- 05_RECORD/archive/pre_wave5/constellation_map.md: broken relationship link 'CONST.vault_curator.agent.specialist.orphan_detector'
- 05_RECORD/archive/pre_wave5/constellation_map.md: broken relationship link '02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation'
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken wiki-link [[Vault Curator constellation]]
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken wiki-link [[CONST.vault_curator.agent.specialist.link_auditor]]
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken wiki-link [[CONST.vault_curator.agent.specialist.schema_validator]]
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken wiki-link [[CONST.vault_curator.agent.specialist.orphan_detector]]
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken wiki-link [[06_authority_links/vault_curator_supervisor.yaml]]
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken wiki-link [[Coordination Authority]]
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken wiki-link [[CONST.vault_curator.agent.executive]]
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken relationship link 'CONST.vault_curator.map'
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken relationship link 'CONST.vault_curator.agent.specialist.link_auditor'
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken relationship link 'CONST.vault_curator.agent.specialist.schema_validator'
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken relationship link 'CONST.vault_curator.agent.specialist.orphan_detector'
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken relationship link 'Vault Curator constellation'
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken relationship link '06_authority_links/vault_curator_supervisor.yaml'
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken relationship link 'Aggregated Audit Report'
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken relationship link 'Escalation Queue'
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken relationship link 'CONST.vault_curator.agent.executive'
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken relationship link 'CONST.vault_curator.agent.specialist.link_auditor'
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken relationship link 'CONST.vault_curator.agent.specialist.schema_validator'
- 05_RECORD/archive/pre_wave5/integrity_coordinator.md: broken relationship link 'CONST.vault_curator.agent.specialist.orphan_detector'
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken wiki-link [[Vault Curator constellation]]
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken wiki-link [[link_text]]
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken wiki-link [[link]]
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken wiki-link [[Non-Existent Concept]]
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken wiki-link [[Deleted Reference]]
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken wiki-link [[06_authority_links/vault_curator_link_auditor.yaml]]
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken wiki-link [[Vault Link Architecture]]
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken wiki-link [[CONST.vault_curator.agent.supervisor]]
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken relationship link 'CONST.vault_curator.map'
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken relationship link 'Vault Curator constellation'
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken relationship link '06_authority_links/vault_curator_link_auditor.yaml'
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken relationship link 'Link Audit Report (CSV)'
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken relationship link 'CONST.vault_curator.agent.supervisor'
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken relationship link 'CONST.vault_curator.agent.specialist.schema_validator'
- 05_RECORD/archive/pre_wave5/link_auditor.md: broken relationship link 'CONST.vault_curator.agent.specialist.orphan_detector'
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[Vault Curator constellation]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[Vault Curator constellation]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[CONST.vault_curator.agent.executive]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[CONST.vault_curator.agent.supervisor]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[CONST.vault_curator.agent.specialist.link_auditor]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[link]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[CONST.vault_curator.agent.specialist.schema_validator]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[CONST.vault_curator.agent.specialist.orphan_detector]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[CONST.vault_curator.agent.supervisor]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[CONST.vault_curator.agent.supervisor]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[CONST.vault_curator.agent.supervisor]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[CONST.vault_curator.agent.executive]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[CONST.vault_curator.agent.supervisor]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[CONST.vault_curator.agent.supervisor]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[Vault Curator constellation]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[CONST.vault_curator.agent.executive]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[CONST.vault_curator.agent.supervisor]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken relationship link 'CONST.vault_curator.map'
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken relationship link 'Vault Curator constellation'
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken relationship link 'CONST.vault_curator.agent.executive'
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken relationship link 'CONST.vault_curator.agent.supervisor'
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken relationship link 'CONST.vault_curator.agent.specialist.link_auditor'
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken relationship link 'CONST.vault_curator.agent.specialist.schema_validator'
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken relationship link 'CONST.vault_curator.agent.specialist.orphan_detector'
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken relationship link 'Audit Report'
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken relationship link 'Execution Log'
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken relationship link 'CONST.vault_curator.agent.executive'
- 05_RECORD/archive/pre_wave5/maintenance_cycle.md: broken relationship link 'CONST.vault_curator.agent.supervisor'
- 05_RECORD/archive/pre_wave5/orphan_detector.md: broken wiki-link [[Vault Curator constellation]]
- 05_RECORD/archive/pre_wave5/orphan_detector.md: broken wiki-link [[link]]
- 05_RECORD/archive/pre_wave5/orphan_detector.md: broken wiki-link [[06_authority_links/vault_curator_orphan_detector.yaml]]
- 05_RECORD/archive/pre_wave5/orphan_detector.md: broken wiki-link [[Vault Graph Structure]]
- 05_RECORD/archive/pre_wave5/orphan_detector.md: broken wiki-link [[CONST.vault_curator.agent.supervisor]]
- 05_RECORD/archive/pre_wave5/orphan_detector.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
- 05_RECORD/archive/pre_wave5/orphan_detector.md: broken relationship link 'CONST.vault_curator.map'
- 05_RECORD/archive/pre_wave5/orphan_detector.md: broken relationship link 'Vault Curator constellation'
- 05_RECORD/archive/pre_wave5/orphan_detector.md: broken relationship link '06_authority_links/vault_curator_orphan_detector.yaml'
- 05_RECORD/archive/pre_wave5/orphan_detector.md: broken relationship link 'Orphan Detection Report (CSV)'
- 05_RECORD/archive/pre_wave5/orphan_detector.md: broken relationship link 'CONST.vault_curator.agent.supervisor'
- 05_RECORD/archive/pre_wave5/orphan_detector.md: broken relationship link 'CONST.vault_curator.agent.specialist.link_auditor'
- 05_RECORD/archive/pre_wave5/orphan_detector.md: broken relationship link 'CONST.vault_curator.agent.specialist.schema_validator'
- 05_RECORD/archive/pre_wave5/schema_validator.md: broken wiki-link [[Vault Curator constellation]]
- 05_RECORD/archive/pre_wave5/schema_validator.md: broken wiki-link [[06_authority_links/vault_curator_schema_validator.yaml]]
- 05_RECORD/archive/pre_wave5/schema_validator.md: broken wiki-link [[Frontmatter Schema]]
- 05_RECORD/archive/pre_wave5/schema_validator.md: broken wiki-link [[CONST.vault_curator.agent.supervisor]]
- 05_RECORD/archive/pre_wave5/schema_validator.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
- 05_RECORD/archive/pre_wave5/schema_validator.md: broken relationship link 'CONST.vault_curator.map'
- 05_RECORD/archive/pre_wave5/schema_validator.md: broken relationship link 'Vault Curator constellation'
- 05_RECORD/archive/pre_wave5/schema_validator.md: broken relationship link '06_authority_links/vault_curator_schema_validator.yaml'
- 05_RECORD/archive/pre_wave5/schema_validator.md: broken relationship link 'Schema Validation Report (CSV)'
- 05_RECORD/archive/pre_wave5/schema_validator.md: broken relationship link 'CONST.vault_curator.agent.supervisor'
- 05_RECORD/archive/pre_wave5/schema_validator.md: broken relationship link 'CONST.vault_curator.agent.specialist.link_auditor'
- 05_RECORD/archive/pre_wave5/schema_validator.md: broken relationship link 'CONST.vault_curator.agent.specialist.orphan_detector'
- 05_RECORD/archive/pre_wave5/vault_governance_director.md: broken wiki-link [[Vault Curator constellation]]
- 05_RECORD/archive/pre_wave5/vault_governance_director.md: broken wiki-link [[06_authority_links/vault_curator_executive.yaml]]
- 05_RECORD/archive/pre_wave5/vault_governance_director.md: broken wiki-link [[CONST.vault_curator.agent.supervisor]]
- 05_RECORD/archive/pre_wave5/vault_governance_director.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
- 05_RECORD/archive/pre_wave5/vault_governance_director.md: broken relationship link 'CONST.vault_curator.map'
- 05_RECORD/archive/pre_wave5/vault_governance_director.md: broken relationship link 'CONST.vault_curator.agent.supervisor'
- 05_RECORD/archive/pre_wave5/vault_governance_director.md: broken relationship link 'Vault Curator constellation'
- 05_RECORD/archive/pre_wave5/vault_governance_director.md: broken relationship link '06_authority_links/vault_curator_executive.yaml'
- 05_RECORD/archive/pre_wave5/vault_governance_director.md: broken relationship link 'Execution Log'
- 05_RECORD/archive/pre_wave5/vault_governance_director.md: broken relationship link 'CONST.vault_curator.agent.supervisor'
- 05_RECORD/archive/pre_wave5/vault_governance_director.md: broken relationship link 'CONST.vault_curator.agent.specialist.link_auditor'
- 05_RECORD/archive/pre_wave5/vault_governance_director.md: broken relationship link 'CONST.vault_curator.agent.specialist.schema_validator'
- 05_RECORD/archive/pre_wave5/vault_governance_director.md: broken relationship link 'CONST.vault_curator.agent.specialist.orphan_detector'
- 05_RECORD/archive/pre_wave5/workspace_readme.md: broken wiki-link [[Vault Curator constellation]]
- 05_RECORD/archive/pre_wave5/workspace_readme.md: broken wiki-link [[Missing Concept]]
- 05_RECORD/archive/pre_wave5/workspace_readme.md: broken wiki-link [[Vault Curator constellation]]
- 05_RECORD/archive/pre_wave5/workspace_readme.md: broken wiki-link [[CONST.vault_curator.agent.specialist.link_auditor]]
- 05_RECORD/archive/pre_wave5/workspace_readme.md: broken wiki-link [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
- 05_RECORD/archive/pre_wave5/workspace_readme.md: broken wiki-link [[Modular Workspace Protocol]]
- 05_RECORD/archive/wave_5.2_captures/RAG vs QMD.md: broken wiki-link [[001 Screenshot 2026-03-02 at 19.42.38.png]]
- 05_RECORD/archive/wave_5.2_captures/The 6 shell scripts every large knowledge-vault builder eventually creates.md: broken wiki-link [[old_name]]
- 05_RECORD/archive/wave_5.2_captures/The 6 shell scripts every large knowledge-vault builder eventually creates.md: broken wiki-link [[new_name]]
- 05_RECORD/archive/wave_5.2_concepts/AM — Wave 5 — Audit Framework Rubric.md: broken relationship link 'Audit Framework'
- 05_RECORD/archive/wave_5.2_concepts/AM — Wave 5 — Audit Framework Rubric.md: broken relationship link '02_KNOWLEDGE'
- 05_RECORD/archive/wave_5.2_concepts/AM — Wave 5 — Audit Framework Rubric.md: broken relationship link '03_PIPELINES'
- 05_RECORD/archive/wave_5.2_concepts/AM — Wave 5 — Audit Framework Rubric.md: broken relationship link '04_PROJECTS'
- 05_RECORD/archive/wave_5.2_concepts/AM — Wave 5 — Audit Framework Rubric.md: broken relationship link '05_SYSTEMS'
- 05_RECORD/archive/wave_5.2_concepts/AM — Wave 5 — Audit Framework Rubric.md: broken relationship link '06_EXECUTION'
- 05_RECORD/archive/wave_5.2_concepts/AM — Wave 5 — Audit Framework Rubric.md: broken relationship link '88_TEMPLATES'
- 05_RECORD/archive/wave_5.2_concepts/AM — Wave 5 — Audit Framework Rubric.md: broken relationship link '99_ARCHIVE'
- 05_RECORD/archive/wave_5.2_concepts/AM — Wave 5 — Audit Framework Rubric.md: broken relationship link 'Audit Taxonomy'
- 05_RECORD/archive/wave_5.2_concepts/Agent Workflow.md: broken wiki-link [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]]
- 05_RECORD/archive/wave_5.2_concepts/Consolidation Pipeline.md: broken relationship link 'Consolidation Process'
- 05_RECORD/archive/wave_5.2_concepts/Consolidation Pipeline.md: broken relationship link 'State Change Logger'
- 05_RECORD/archive/wave_5.2_concepts/Consolidation Pipeline.md: broken relationship link 'Consolidation Audit Report'
- 05_RECORD/archive/wave_5.2_concepts/Execution Architecture.md: broken wiki-link [[GovernedAgent]]
- 05_RECORD/archive/wave_5.2_concepts/Execution Architecture.md: broken wiki-link [[Tool Interface]]
- 05_RECORD/archive/wave_5.2_concepts/Execution Architecture.md: broken wiki-link [[Workflow Engine]]
- 05_RECORD/archive/wave_5.2_concepts/Execution Architecture.md: broken wiki-link [[Tool Registry]]
- 05_RECORD/archive/wave_5.2_concepts/Execution Architecture.md: broken relationship link 'Execution Layer Model'
- 05_RECORD/archive/wave_5.2_concepts/Execution Architecture.md: broken relationship link 'Execution Adapter Pattern'
- 05_RECORD/archive/wave_5.2_concepts/Execution Architecture.md: broken relationship link 'Tool Interface'
- 05_RECORD/archive/wave_5.2_concepts/Execution Architecture.md: broken relationship link 'Workflow Engine'
- 05_RECORD/archive/wave_5.2_concepts/Execution Architecture.md: broken relationship link 'GovernedAgent'
- 05_RECORD/archive/wave_5.2_concepts/Execution Architecture.md: broken relationship link 'Tool Registry'
- 05_RECORD/archive/wave_5.2_concepts/Host Options Evaluation.md: broken relationship link 'Host Binding Strategy'
- 05_RECORD/archive/wave_5.2_concepts/LLM-Script Boundary Reference.md: broken wiki-link [[Note Title]]
- 05_RECORD/archive/wave_5.2_concepts/LLM-Script Boundary Reference.md: broken relationship link 'LLM-Script Boundary'
- 05_RECORD/archive/wave_5.2_concepts/LLM-Script Boundary Reference.md: broken relationship link 'Vault Maintenance Constellation'
- 05_RECORD/archive/wave_5.2_concepts/Note Upgrade Workflow.md: broken relationship link 'Note Upgrade Process'
- 05_RECORD/archive/wave_5.2_concepts/Note Upgrade Workflow.md: broken relationship link '02_KNOWLEDGE'
- 05_RECORD/archive/wave_5.2_concepts/Note Upgrade Workflow.md: broken relationship link '05_SYSTEMS'
- 05_RECORD/archive/wave_5.2_concepts/Operational Outcome.md: broken wiki-link [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]]
- 05_RECORD/archive/wave_5.2_concepts/Operational Outcome.md: broken wiki-link [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]]
- 05_RECORD/archive/wave_5.2_concepts/Registry Anchoring.md: broken relationship link '02_KNOWLEDGE'
- 05_RECORD/archive/wave_5.2_concepts/Self-Observation Specification.md: broken wiki-link [[GovernedAgent]]
- 05_RECORD/archive/wave_5.2_concepts/Self-Observation Specification.md: broken wiki-link [[Workflow Engine]]
- 05_RECORD/archive/wave_5.2_concepts/Self-Observation Specification.md: broken wiki-link [[State Change Logger]]
- 05_RECORD/archive/wave_5.2_concepts/Self-Observation Specification.md: broken relationship link 'Self-Observation Framework'
- 05_RECORD/archive/wave_5.2_concepts/Self-Observation Specification.md: broken relationship link 'Agent Performance Metrics'
- 05_RECORD/archive/wave_5.2_concepts/Self-Observation Specification.md: broken relationship link 'GovernedAgent'
- 05_RECORD/archive/wave_5.2_concepts/Self-Observation Specification.md: broken relationship link 'Workflow Engine'
- 05_RECORD/archive/wave_5.2_concepts/Self-Observation Specification.md: broken relationship link 'State Change Logger'
- 05_RECORD/archive/wave_5.2_concepts/Self-Observation Specification.md: broken relationship link 'Observation Log'
- 05_RECORD/archive/wave_5.2_concepts/Tool Registry Design.md: broken wiki-link [[Tool Interface]]
- 05_RECORD/archive/wave_5.2_concepts/Tool Registry Design.md: broken wiki-link [[GovernedAgent]]
- 05_RECORD/archive/wave_5.2_concepts/Tool Registry Design.md: broken relationship link 'Tool Registry'
- 05_RECORD/archive/wave_5.2_concepts/Tool Registry Design.md: broken relationship link 'Execution Adapter Pattern'
- 05_RECORD/archive/wave_5.2_concepts/Tool Registry Design.md: broken relationship link 'Tool Interface'
- 05_RECORD/archive/wave_5.2_concepts/Tool Registry Design.md: broken relationship link 'GovernedAgent'
- 05_RECORD/archive/wave_5.2_governance/Wave 5.2 — Capture Seed (consumed).md: broken wiki-link [[Wave 5.1 — Design Session Retrospective]]
- 05_RECORD/archive/wave_5.2_governance/Wave 5.2 — Capture Seed (consumed).md: broken relationship link 'Wave 5.1 — Design Session Retrospective'
- 05_RECORD/archive/wave_5.2_roadmap/AM — Evolution Roadmap — Waves 5-8.md: broken relationship link 'Wave 5'
- 05_RECORD/archive/wave_5.2_roadmap/AM — Evolution Roadmap — Waves 5-8.md: broken relationship link 'Wave 6'
- 05_RECORD/archive/wave_5.2_roadmap/AM — Evolution Roadmap — Waves 5-8.md: broken relationship link 'Wave 7'
- 05_RECORD/archive/wave_5.2_roadmap/AM — Evolution Roadmap — Waves 5-8.md: broken relationship link 'Wave 8'
- 05_RECORD/archive/wave_5_agent_systems/Evolution Executive.md: broken wiki-link [[Agent Maestro — Four-Layer Model]]
- 05_RECORD/archive/wave_5_agent_systems/Evolution Executive.md: broken wiki-link [[EXEC.governance_executive]]
- 05_RECORD/archive/wave_5_agent_systems/Evolution Executive.md: broken wiki-link [[EXEC.operations_executive]]
- 05_RECORD/archive/wave_5_agent_systems/Evolution Executive.md: broken wiki-link [[EXEC.knowledge_executive]]
- 05_RECORD/archive/wave_5_agent_systems/Evolution Executive.md: broken wiki-link [[Agent Maestro — System Evolution Framework]]
- 05_RECORD/archive/wave_5_agent_systems/Evolution Executive.md: broken wiki-link [[Agent Maestro — Decision Framework]]
- 05_RECORD/archive/wave_5_agent_systems/Evolution Executive.md: broken wiki-link [[Agent Maestro — Optimization Patterns Map]]
- 05_RECORD/archive/wave_5_agent_systems/Evolution Executive.md: broken wiki-link [[Agent Maestro — Strategic Initiative Tracking]]
- 05_RECORD/archive/wave_5_agent_systems/Evolution Executive.md: broken relationship link 'Agent Maestro — System Evolution Framework'
- 05_RECORD/archive/wave_5_agent_systems/Evolution Executive.md: broken relationship link 'Agent Maestro — Optimization Patterns Map'
- 05_RECORD/archive/wave_5_agent_systems/Executive Orchestrator.md: broken wiki-link [[Agent Maestro — Four-Layer Model]]
- 05_RECORD/archive/wave_5_agent_systems/Executive Orchestrator.md: broken wiki-link [[Agent Maestro — Authority Layer Map]]
- 05_RECORD/archive/wave_5_agent_systems/Executive Orchestrator.md: broken wiki-link [[Agent Maestro — Workspace Layer]]
- 05_RECORD/archive/wave_5_agent_systems/Executive Orchestrator.md: broken wiki-link [[Agent Maestro — Pipelines]]
- 05_RECORD/archive/wave_5_agent_systems/Executive Orchestrator.md: broken wiki-link [[Agent Maestro — Decision Framework]]
- 05_RECORD/archive/wave_5_agent_systems/Executive Orchestrator.md: broken relationship link 'Agent Maestro — Four-Layer Model'
- 05_RECORD/archive/wave_5_agent_systems/Governance Executive.md: broken wiki-link [[Agent Maestro — Authority Layer Map]]
- 05_RECORD/archive/wave_5_agent_systems/Governance Executive.md: broken wiki-link [[Agent Maestro — Four-Layer Model]]
- 05_RECORD/archive/wave_5_agent_systems/Governance Executive.md: broken wiki-link [[Agent Maestro — Authority Architecture]]
- 05_RECORD/archive/wave_5_agent_systems/Governance Executive.md: broken wiki-link [[Agent Maestro — Authority Layer Map]]
- 05_RECORD/archive/wave_5_agent_systems/Governance Executive.md: broken wiki-link [[Agent Maestro — Decision Framework]]
- 05_RECORD/archive/wave_5_agent_systems/Governance Executive.md: broken wiki-link [[Agent Maestro — Governance Schemas Reference]]
- 05_RECORD/archive/wave_5_agent_systems/Governance Executive.md: broken relationship link 'Agent Maestro — Authority Architecture'
- 05_RECORD/archive/wave_5_agent_systems/Governance Executive.md: broken relationship link 'Agent Maestro — Authority Layer Map'
- 05_RECORD/archive/wave_5_agent_systems/Governance Executive.md: broken relationship link 'Agent Maestro — Governance Schemas Map'
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: broken wiki-link [[Agent Maestro — Four-Layer Model]]
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: broken wiki-link [[Agent Maestro — Memory Architecture]]
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: broken wiki-link [[Agent Maestro — Memory Architecture]]
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: broken wiki-link [[Agent Maestro — Knowledge Graph Layer]]
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: broken wiki-link [[Agent Maestro — Knowledge Layer]]
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: broken wiki-link [[EXEC.governance_executive]]
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: broken wiki-link [[EXEC.operations_executive]]
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: broken wiki-link [[Agent Maestro — Four-Layer Model]]
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: broken wiki-link [[Agent Maestro — Knowledge Graph Structure Map]]
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: broken wiki-link [[Agent Maestro — Structured Data Layer]]
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: broken wiki-link [[Agent Maestro — Vector Memory Layer]]
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: broken relationship link 'Agent Maestro — Knowledge Layer'
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: broken relationship link 'Agent Maestro — Memory Architecture'
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: broken relationship link 'Agent Maestro — Knowledge Graph Layer'
- 05_RECORD/archive/wave_5_agent_systems/Knowledge Executive.md: broken relationship link 'Agent Maestro — Knowledge Graph Structure Map'
- 05_RECORD/archive/wave_5_agent_systems/Operations Executive.md: broken wiki-link [[Agent Maestro — Pipelines]]
- 05_RECORD/archive/wave_5_agent_systems/Operations Executive.md: broken wiki-link [[Agent Maestro — Workflow Layer Map]]
- 05_RECORD/archive/wave_5_agent_systems/Operations Executive.md: broken wiki-link [[Agent Maestro — Pipelines]]
- 05_RECORD/archive/wave_5_agent_systems/Operations Executive.md: broken wiki-link [[Agent Maestro — Workspace Layer]]
- 05_RECORD/archive/wave_5_agent_systems/Operations Executive.md: broken wiki-link [[Agent Maestro — Four-Layer Model]]
- 05_RECORD/archive/wave_5_agent_systems/Operations Executive.md: broken wiki-link [[EXEC.knowledge_executive]]
- 05_RECORD/archive/wave_5_agent_systems/Operations Executive.md: broken wiki-link [[EXEC.evolution_executive]]
- 05_RECORD/archive/wave_5_agent_systems/Operations Executive.md: broken wiki-link [[Agent Maestro — Decision Framework]]
- 05_RECORD/archive/wave_5_agent_systems/Operations Executive.md: broken wiki-link [[Agent Maestro — Pipeline Contract Map]]
- 05_RECORD/archive/wave_5_agent_systems/Operations Executive.md: broken relationship link 'Agent Maestro — Pipelines'
- 05_RECORD/archive/wave_5_agent_systems/Operations Executive.md: broken relationship link 'Agent Maestro — Workflow Layer Map'
- 05_RECORD/archive/wave_5_agent_systems/Operations Executive.md: broken relationship link 'Agent Maestro — Workspace Layer'
- 05_RECORD/archive/wave_5_agent_systems/Operations Executive.md: broken relationship link 'Agent Maestro — Pipeline Contract Map'
- 05_RECORD/archive/wave_5_agent_systems/note_processing.md: broken wiki-link [[scheduled_audit_cycle.md]]
- 05_RECORD/archive/wave_5_agent_systems/note_processing.md: broken wiki-link [[on_demand_repair.md]]
- 05_RECORD/archive/wave_5_agent_systems/note_processing.md: broken wiki-link [[executive_link.md]]
- 05_RECORD/archive/wave_5_agent_systems/on_demand_repair.md: broken wiki-link [[scheduled_audit_cycle.md]]
- 05_RECORD/archive/wave_5_agent_systems/on_demand_repair.md: broken wiki-link [[note_processing.md]]
- 05_RECORD/archive/wave_5_agent_systems/on_demand_repair.md: broken wiki-link [[executive_link.md]]
- 05_RECORD/archive/wave_5_agent_systems/scheduled_audit_cycle.md: broken wiki-link [[on_demand_repair.md]]
- 05_RECORD/archive/wave_5_agent_systems/scheduled_audit_cycle.md: broken wiki-link [[note_processing.md]]
- 05_RECORD/archive/wave_5_agent_systems/scheduled_audit_cycle.md: broken wiki-link [[executive_link.md]]
- 05_RECORD/archive/wave_5_agent_systems/self_healing_repairer.md: broken wiki-link [[wiki-link]]
- 05_RECORD/archive/wave_5_authority_architecture/compiled_artifact_schema.md: broken relationship link 'Agent Maestro — Authority Architecture'
- 05_RECORD/archive/wave_5_infrastructure/Observability.md: broken wiki-link [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]]
- 05_RECORD/archive/wave_5_knowledge/AM — Evolution Roadmap — Waves 5-8.md: broken relationship link 'Wave 5'
- 05_RECORD/archive/wave_5_knowledge/AM — Evolution Roadmap — Waves 5-8.md: broken relationship link 'Wave 6'
- 05_RECORD/archive/wave_5_knowledge/AM — Evolution Roadmap — Waves 5-8.md: broken relationship link 'Wave 7'
- 05_RECORD/archive/wave_5_knowledge/AM — Evolution Roadmap — Waves 5-8.md: broken relationship link 'Wave 8'
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Domain Map.md: broken wiki-link [[02_Systems/Bartram/02_KNOWLEDGE/concepts/Glossary]]
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Executive Layer Map.md: broken wiki-link [[EXEC.pack.executive_orchestrator]]
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Executive Layer Map.md: broken wiki-link [[EXEC.pack.governance_executive]]
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Executive Layer Map.md: broken wiki-link [[EXEC.pack.operations_executive]]
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Executive Layer Map.md: broken wiki-link [[EXEC.pack.knowledge_executive]]
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Executive Layer Map.md: broken wiki-link [[EXEC.pack.evolution_executive]]
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Layer Model Map.md: broken wiki-link [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]]
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Navigation Map.md: broken wiki-link [[02_Systems/Bartram/02_KNOWLEDGE/concepts/Glossary]]
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Pipelines Map.md: broken wiki-link [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]]
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Pipelines Map.md: broken wiki-link [[02_Systems/Bartram/03_PIPELINES/maintenance_pipeline/Maintenance Pipeline]]
- 05_RECORD/archive/wave_5_knowledge/Evidence Over Assumptions.md: broken wiki-link [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]]
- 05_RECORD/archive/wave_5_knowledge/Evidence Over Assumptions.md: broken wiki-link [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]]
- 05_RECORD/archive/wave_5_knowledge/Memory Architecture Map.md: broken wiki-link [[Memory Authority]]
- 05_RECORD/archive/wave_5_operational_intelligence/AI Operations.md: broken wiki-link [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]]
- 05_RECORD/archive/wave_5_operational_intelligence/Agent Performance Measurement.md: broken wiki-link [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]]
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Audit of Proposal v3.md: broken relationship link 'Agent Maestro — Evolution Roadmap v0.5.0'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Contract.md: broken relationship link 'Wave 5'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Contract.md: broken relationship link 'Agent Maestro — Evolution Roadmap v0.5.0'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Contract.md: broken relationship link 'v0.5.0 Release'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Foundational Brainstorm.md: broken relationship link 'Foundational Elements'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Foundational Brainstorm.md: broken relationship link 'Audit Taxonomy'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Foundational Brainstorm.md: broken relationship link 'Project Lifecycle'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Foundational Brainstorm.md: broken relationship link 'Agent Maestro — Evolution Roadmap v0.5.0'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Audit.md: broken wiki-link [[02_KNOWLEDGE/patterns/\]]
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Audit.md: broken wiki-link [[Agent Systems\]]
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Audit.md: broken wiki-link [[Memory Architecture\]]
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Audit.md: broken relationship link '02_KNOWLEDGE/governance'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Reconciliation Proposal.md: broken wiki-link [[02_KNOWLEDGE/patterns/\]]
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Reconciliation Proposal.md: broken wiki-link [[02_KNOWLEDGE/patterns]]
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Reconciliation Proposal.md: broken wiki-link [[Agent Systems\]]
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Reconciliation Proposal.md: broken wiki-link [[Memory Architecture\]]
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Reconciliation Proposal.md: broken relationship link '02_KNOWLEDGE/governance'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v1.md: broken relationship link 'Wave 5'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v1.md: broken relationship link 'Agent Maestro — Evolution Roadmap v0.5.0'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v1.md: broken relationship link 'v0.5.0 Release'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v3.md: broken relationship link 'Wave 5'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v3.md: broken relationship link 'Agent Maestro — Evolution Roadmap v0.5.0'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v3.md: broken relationship link 'v0.5.0 Release'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Treatise on Core Principles.md: broken relationship link 'Foundational Elements'
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Treatise on Core Principles.md: broken relationship link 'Agent Maestro — Evolution Roadmap v0.5.0'
- 05_RECORD/archive/wave_5_projects/Agent Deployment Playbook.md: broken wiki-link [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]]
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.1 — Improvement Proposal.md: broken wiki-link [[wiki-links]]
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.1 — Improvement Proposal.md: broken wiki-link [[target]]
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.1 — Improvement Proposal.md: broken wiki-link [[links]]
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.1 — Improvement Proposal.md: broken relationship link '01_CAPTURE/inbox/Authority Pack Compiler'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase B Output Summary.md: broken relationship link 'Agent Maestro v0.3'
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase C Output Summary.md: broken relationship link 'Agent Maestro v0.3.2'
- 05_RECORD/archive/wave_5_projects/Tasks Hub.md: broken wiki-link [[02_Systems/Bartram/06_EXECUTION/tasks/Next Steps]]
- 05_RECORD/archive/wave_5_projects/Tasks Hub.md: broken wiki-link [[02_Systems/Bartram/06_EXECUTION/tasks/To Do]]
- 05_RECORD/archive/wave_5_projects/To Do.md: broken wiki-link [[02_Systems/Bartram/06_EXECUTION/tasks/Next Steps]]
- 05_RECORD/archive/wave_5_projects/Vault Upgrade Backlog.md: broken relationship link '02_KNOWLEDGE'
- 05_RECORD/archive/wave_5_reports/AM — Wave 5 — Baseline Inventory.md: broken relationship link 'Law 2 — Action Properties'
- 05_RECORD/archive/wave_5_templates/Concept Template.md: concept note has zero body wiki-links
- 05_RECORD/archive/wave_5_templates/Concept Template_sys.md: concept note has zero body wiki-links
- 05_RECORD/archive/wave_5_templates/General Note Template.md: concept note has zero body wiki-links
- 05_RECORD/archive/wave_5_templates/Governance Template.md: governance note has zero body wiki-links
- 05_RECORD/archive/wave_5_templates/Governance Template_sys.md: governance note has zero body wiki-links
- 05_RECORD/archive/wave_5_templates/Template Governance Rules.md: broken wiki-link [[Parent Map]]
- 05_RECORD/archive/wave_5_templates/Template Governance Rules.md: broken wiki-link [[Secondary Map]]
- 05_RECORD/archive/wave_5_templates/Template Governance Rules_sys.md: broken wiki-link [[Parent Map]]
- 05_RECORD/archive/wave_5_templates/Template Governance Rules_sys.md: broken wiki-link [[Secondary Map]]
- 05_RECORD/archive/wave_5_templates/Template Registry.md: broken wiki-link [[Parent Map]]
- 05_RECORD/archive/wave_5_templates/Template Registry.md: broken wiki-link [[Secondary Map]]
- 05_RECORD/archive/wave_5_templates/Template Registry_sys.md: broken wiki-link [[Parent Map]]
- 05_RECORD/archive/wave_5_templates/Template Registry_sys.md: broken wiki-link [[Secondary Map]]
- 05_RECORD/archive/wave_5_templates/Template Ruleset.md: broken wiki-link [[MAP.agent_ecosystem]]
- 05_RECORD/archive/wave_5_templates/Template Ruleset.md: broken wiki-link [[MAP.agent_governance]]
- 05_RECORD/archive/wave_5_templates/Template Ruleset_sys.md: broken wiki-link [[MAP.agent_ecosystem]]
- 05_RECORD/archive/wave_5_templates/Template Ruleset_sys.md: broken wiki-link [[MAP.agent_governance]]
- 05_RECORD/logs/sessions/Session Log — SES-015 — 2026-03-15.md: broken wiki-link [[02_Systems/Agent Maestro/...]]
- 05_RECORD/logs/sessions/Session Log — SES-015 — 2026-03-15.md: broken wiki-link [[Note Title]]

### Orphan Detection


- 01_CAPTURE/Wave 7 — Brainstorm.md: orphan — no inbound links from any other file
- 02_KNOWLEDGE/templates/Template — Audit Report.md: orphan — no inbound links from any other file
- 02_KNOWLEDGE/templates/Template — Concept.md: orphan — no inbound links from any other file
- 02_KNOWLEDGE/templates/Template — Governance.md: orphan — no inbound links from any other file
- 02_KNOWLEDGE/templates/Template — Proposal.md: orphan — no inbound links from any other file
- 02_KNOWLEDGE/templates/Template — Reflection.md: orphan — no inbound links from any other file
- 02_KNOWLEDGE/templates/Template — Role.md: orphan — no inbound links from any other file
- 02_KNOWLEDGE/templates/Template — Session Log.md: orphan — no inbound links from any other file
- 02_KNOWLEDGE/templates/Template — Skill.md: orphan — no inbound links from any other file
- 05_RECORD/archive/Wave 5.2 — Phase 4 Capture Seed.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/5-Layer Architecture of AI-Native Systems.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/AI Operations Conductor.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/AM North Star v1.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/AM Principles v2.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/AM Vault vs Authority Packs.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Agent Architecture Synthesis.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Agent Infrastructure Architect.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Agent Maestro 12 Keystone Notes.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Agent Maestro 5 Super Maps.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Agent Maestro Artifacts.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Agent Maestro Domain Structure.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Agent Maestro Knowledge Graph.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Agent Maestro Maps.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Agent Maestro Vault Architecture.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Agent Maestro — Atomic Note Schema.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Authority Model of an AI-Native System.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Authority Pack - Definition.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Authority Pack Compiler - Definition.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Authority Pack Grammar v1.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Canonical Artifact Taxonomy for AI-Native Systems.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Controlled Vault Repair Operation v1.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Definition Alignment Audit - Concepts.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Definitions.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Frontmatter Update v1.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Frontmatter Upgrade Checklist.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Frontmatter Upgrade v1.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Inception.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Intelligence Trainer.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Modes.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Modes_v0.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/North Star.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Note Knowledge Upgrade Order.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Phases of Growth.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Pipeline Template — Legacy.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Portable Authority Pack - Inception.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Potential Authority Pack Templates.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Potential Roadmap — Authority Packs.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Principles.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Principles_v0.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Roadmap 01.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Roadmap.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Roadmap_v0.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Scope.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Scope_v0.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Starter Note Set.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Strategy.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Strategy_v0.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Structure & Knowledge Upgrade Prompt v1.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Structure And Knowledge Upgrade v1.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Target Repo Structure.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/The 5-Layer Architecture of Real Agent Systems & Control Substrate.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Vault Integrity & Self-Healing Audit v1.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Vault Rules Fragment.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Vault Structure and Knowledge Upgrade v0.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/Workflow Architect.md: orphan — no inbound links from any other file
- 05_RECORD/archive/pre_wave5/constellation_map.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/AM Python Daemon for scheduled automations..md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/AM Self Audit.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/Am basically starter pack.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/Archived Treatsie.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/Breifs.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/Memory Options.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/Message sent on new capture sees.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/Potential rule.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/Proposal — Shell Script Vault Maintenance Constellation.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/RAG vs QMD.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/Reflections.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/Roles.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/Runtime Provider Layer  Proposal v2.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/Skills.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/The 6 shell scripts every large knowledge-vault builder eventually creates.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/Toon.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_captures/agent responsibility collision.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack Versioning and Inheritance.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_concepts/Git Best Practices for AI-Assisted Builds v1.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_concepts/Pure Agent Concepts.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_concepts/Registry Anchoring.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5.2_governance/Wave 5.2 — Capture Seed (consumed).md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_agent_systems/constellation_map.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_agent_systems/definition_alignment_auditor.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_agent_systems/executive_link.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_agent_systems/maintenance_coordinator.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_agent_systems/note_processing.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_agent_systems/note_processor.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_agent_systems/on_demand_repair.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_agent_systems/ontology_integrity_auditor.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_agent_systems/scheduled_audit_cycle.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_agent_systems/self_healing_repairer.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_agent_systems/template_compliance_scanner.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/00_identity.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_2251.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_58e4.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_85a0.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8614.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8d22.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_bf68.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_fdde.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/01_scope.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_2c15.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_626d.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7e65.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7f34.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_9aae.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_bfb7.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_c262.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_2822.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_590e.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_5fe5.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_b0bf.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_cf9a.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_e44f.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_f721.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_0f7b.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_4d39.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_91aa.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_cbd0.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_e285.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fbe8.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fe64.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_0dce.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_30e1.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_95ee.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_b8a6.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_c642.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_ce6f.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_e614.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/05_rules.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_0f6e.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_16a1.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_1dcb.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_4c7b.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_8b3b.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_c40e.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_e057.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_11c1.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_166c.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_2928.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_d84d.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_de4e.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fbfd.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fed8.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0e49.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0f26.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_2c0e.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_635c.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_81d9.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_b821.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_d819.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0bab.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0dd6.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_1933.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_20a6.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_332a.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_3f98.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_9c3e.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_112f.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_4780.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_6af2.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_7983.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_99a2.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_e850.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_f447.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_1bc2.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_3465.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_9daa.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_b374.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_c583.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_dfa5.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_f270.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_3b31.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_4292.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_43d4.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_532d.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_9628.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_b538.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_c9c7.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_1432.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_2f8c.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_3baf.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_79ed.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_8df9.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_bce6.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_be6e.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_335f.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_655d.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_8070.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_adee.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_b46f.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_c63a.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_cd59.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/CLAUDE_12e0.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/compiled_artifact_schema.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_authority_architecture/test_repair.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_indexes/Glossary.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_infrastructure/Platformization.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_knowledge/Deterministic Authority Resolution Pattern.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_knowledge/Memory Layer Registry.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_knowledge/Platformization.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/00 Agent Maestro — Build Session Protocol v2.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/01 Agent Maestro — Script Build Harness Integration Brief v1.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/01 Definition Alignment Audit v2.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/02 Adversarial Audit.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/02 Ontology Integrity Audit.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/03 Build Harness Implementation Contract v1.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/03 Reasoning Path Audit.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/AM-Authority-Architecture-Audit-2026-03-15.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.2 — Wave 2+3 Proposal.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Improvement Proposal — Chat GPT 5.2.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase B Output Summary.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.4 — Phase D Output Summary.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/CLAUDE_execution.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/CLAUDE_pipelines.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/CLAUDE_runtime.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/CLAUDE_systems.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/Knowledge Upgrade Prompt v2.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/Next Steps.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/TBP Outreach Agent V1 Spec.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/To Do.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/Vault Upgrade Backlog.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/Weekly Reset Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/review_queue_20260315_111629.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_projects/test_d3_note.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Authority Pack Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Authority Pack Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/CLAUDE_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Concept Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Concept Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Decision Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Decision Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Frontmatter Schema v1.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Frontmatter Schema v1_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Governance Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Governance Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Index Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Index Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Map Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Map Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Modes Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Modes Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/North Star Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/North Star Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Pipeline Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Principles Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Principles Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Process Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Process Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Project Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Project Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Reference Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Reference Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Registry Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Registry Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Roadmap Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Roadmap Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Scope Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Scope Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Strategy Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Strategy Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/System Map.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/System Map_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/System Registry_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/System Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/System Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Taxonomy Template.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Taxonomy Template_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Template Design Doctrine.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Template Design Doctrine_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Template Governance Rules.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Template Governance Rules_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Template Mapping.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Template Mapping_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Template Registry.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Template Registry_sys.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Template Ruleset.md: orphan — no inbound links from any other file
- 05_RECORD/archive/wave_5_templates/Template Ruleset_sys.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-002 — 2026-03-14.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-003 — 2026-03-14.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-004 — 2026-03-15.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-005 — 2026-03-15.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-006 — 2026-03-15.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-007 — 2026-03-15.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-008 — 2026-03-15.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-009 — 2026-03-15.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-010 — 2026-03-15.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-012 — 2026-03-15.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-013 — 2026-03-15.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-014 — 2026-03-15.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-015 — 2026-03-15.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-016 — 2026-03-15.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-017 — 2026-03-15.md: orphan — no inbound links from any other file
- 05_RECORD/logs/sessions/Session Log — SES-018 — 2026-03-16.md: orphan — no inbound links from any other file

### Stub Detection


- 05_RECORD/archive/wave_5.2_captures/AM Python Daemon for scheduled automations..md: empty file
- 05_RECORD/archive/wave_5.2_captures/AM Self Audit.md: empty file
- 05_RECORD/archive/wave_5_authority_architecture/test_repair.md: heading only, no substantive content

### Naming Validation


- 02_KNOWLEDGE/CLAUDE.md: duplicate filename (also at 01_CAPTURE/CLAUDE.md)
- 02_KNOWLEDGE/governance/CLAUDE.md: duplicate filename (also at 01_CAPTURE/CLAUDE.md)
- 02_KNOWLEDGE/templates/Template — Audit Report.md: title 'Audit Report — [Subject]' does not match filename 'Template — Audit Report'
- 02_KNOWLEDGE/templates/Template — Proposal.md: title 'Proposal — [Title]' does not match filename 'Template — Proposal'
- 02_KNOWLEDGE/templates/Template — Reflection.md: title 'Wave X.Y — Reflection' does not match filename 'Template — Reflection'
- 02_KNOWLEDGE/templates/Template — Role.md: title 'Role — [Name]' does not match filename 'Template — Role'
- 02_KNOWLEDGE/templates/Template — Session Log.md: title 'Session Log — SES-XXX — YYYY-MM-DD' does not match filename 'Template — Session Log'
- 02_KNOWLEDGE/templates/Template — Skill.md: title 'Skill — [Name]' does not match filename 'Template — Skill'
- 03_DECIDE/CLAUDE.md: duplicate filename (also at 01_CAPTURE/CLAUDE.md)
- 04_EXECUTE/CLAUDE.md: duplicate filename (also at 01_CAPTURE/CLAUDE.md)
- 05_RECORD/CLAUDE.md: duplicate filename (also at 01_CAPTURE/CLAUDE.md)
- 05_RECORD/archive/pre_wave5/CLAUDE.md: duplicate filename (also at 01_CAPTURE/CLAUDE.md)
- 05_RECORD/archive/pre_wave5/Pipeline Template — Legacy.md: title 'Pipeline Template' does not match filename 'Pipeline Template — Legacy'
- 05_RECORD/archive/wave_5.2_concepts/Agent.md: duplicate filename (also at 02_KNOWLEDGE/concepts/Agent.md)
- 05_RECORD/archive/wave_5.2_concepts/Agent.md: duplicate title 'Agent' (also in 02_KNOWLEDGE/concepts/Agent.md)
- 05_RECORD/archive/wave_5.2_concepts/Authority Architecture.md: duplicate filename (also at 02_KNOWLEDGE/concepts/Authority Architecture.md)
- 05_RECORD/archive/wave_5.2_concepts/Authority Architecture.md: duplicate title 'Authority Architecture' (also in 02_KNOWLEDGE/concepts/Authority Architecture.md)
- 05_RECORD/archive/wave_5.2_concepts/Memory Architecture.md: duplicate filename (also at 02_KNOWLEDGE/concepts/Memory Architecture.md)
- 05_RECORD/archive/wave_5.2_concepts/Memory Architecture.md: duplicate title 'Memory Architecture' (also in 02_KNOWLEDGE/concepts/Memory Architecture.md)
- 05_RECORD/archive/wave_5.2_concepts/Operational Intelligence.md: duplicate filename (also at 02_KNOWLEDGE/concepts/Operational Intelligence.md)
- 05_RECORD/archive/wave_5.2_concepts/Operational Intelligence.md: duplicate title 'Operational Intelligence' (also in 02_KNOWLEDGE/concepts/Operational Intelligence.md)
- 05_RECORD/archive/wave_5.2_governance/Wave 5.2 — Capture Seed (consumed).md: title 'Wave 5.2 — Capture Seed' does not match filename 'Wave 5.2 — Capture Seed (consumed)'
- 05_RECORD/archive/wave_5.2_roadmap/AM — Evolution Roadmap — Waves 5-8.md: title 'Agent Maestro — Evolution Roadmap v0.5.0' does not match filename 'AM — Evolution Roadmap — Waves 5-8'
- 05_RECORD/archive/wave_5_agent_systems/Agent Constellation.md: duplicate filename (also at 05_RECORD/archive/wave_5.2_concepts/Agent Constellation.md)
- 05_RECORD/archive/wave_5_agent_systems/Agent Constellation.md: duplicate title 'Agent Constellation' (also in 05_RECORD/archive/wave_5.2_concepts/Agent Constellation.md)
- 05_RECORD/archive/wave_5_agent_systems/Agent Ecosystem.md: duplicate filename (also at 05_RECORD/archive/wave_5.2_concepts/Agent Ecosystem.md)
- 05_RECORD/archive/wave_5_agent_systems/Agent Ecosystem.md: duplicate title 'Agent Ecosystem' (also in 05_RECORD/archive/wave_5.2_concepts/Agent Ecosystem.md)
- 05_RECORD/archive/wave_5_agent_systems/CLAUDE.md: duplicate filename (also at 01_CAPTURE/CLAUDE.md)
- 05_RECORD/archive/wave_5_agent_systems/Shared Services.md: duplicate filename (also at 05_RECORD/archive/wave_5.2_concepts/Shared Services.md)
- 05_RECORD/archive/wave_5_agent_systems/Shared Services.md: duplicate title 'Shared Services' (also in 05_RECORD/archive/wave_5.2_concepts/Shared Services.md)
- 05_RECORD/archive/wave_5_agent_systems/authority_packs.md: duplicate filename (also at 05_RECORD/archive/pre_wave5/authority_packs.md)
- 05_RECORD/archive/wave_5_agent_systems/authority_packs.md: title 'Vault Maintenance — Authority Packs Index' does not match filename 'authority_packs'
- 05_RECORD/archive/wave_5_agent_systems/constellation_map.md: duplicate filename (also at 05_RECORD/archive/pre_wave5/constellation_map.md)
- 05_RECORD/archive/wave_5_agent_systems/constellation_map.md: title 'Vault Maintenance Constellation — Map' does not match filename 'constellation_map'
- 05_RECORD/archive/wave_5_agent_systems/definition_alignment_auditor.md: title 'Definition Alignment Auditor — Specialist' does not match filename 'definition_alignment_auditor'
- 05_RECORD/archive/wave_5_agent_systems/executive_link.md: title 'Vault Maintenance — Executive Link to Knowledge Executive' does not match filename 'executive_link'
- 05_RECORD/archive/wave_5_agent_systems/maintenance_coordinator.md: title 'Maintenance Coordinator — Supervisor' does not match filename 'maintenance_coordinator'
- 05_RECORD/archive/wave_5_agent_systems/note_processing.md: title 'Note Processing Workflow' does not match filename 'note_processing'
- 05_RECORD/archive/wave_5_agent_systems/note_processor.md: title 'Note Processor — Specialist' does not match filename 'note_processor'
- 05_RECORD/archive/wave_5_agent_systems/on_demand_repair.md: title 'On-Demand Repair Workflow' does not match filename 'on_demand_repair'
- 05_RECORD/archive/wave_5_agent_systems/ontology_integrity_auditor.md: title 'Ontology Integrity Auditor — Specialist' does not match filename 'ontology_integrity_auditor'
- 05_RECORD/archive/wave_5_agent_systems/scheduled_audit_cycle.md: title 'Scheduled Audit Cycle — Workflow' does not match filename 'scheduled_audit_cycle'
- 05_RECORD/archive/wave_5_agent_systems/self_healing_repairer.md: title 'Self-Healing Repairer — Specialist' does not match filename 'self_healing_repairer'
- 05_RECORD/archive/wave_5_agent_systems/template_compliance_scanner.md: title 'Template Compliance Scanner — Specialist' does not match filename 'template_compliance_scanner'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_2251.md: duplicate title '00_identity' (also in 05_RECORD/archive/wave_5_authority_architecture/00_identity.md)
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_2251.md: title '00_identity' does not match filename '00_identity_2251'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_58e4.md: duplicate title '00_identity' (also in 05_RECORD/archive/wave_5_authority_architecture/00_identity.md)
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_58e4.md: title '00_identity' does not match filename '00_identity_58e4'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_85a0.md: duplicate title '00_identity' (also in 05_RECORD/archive/wave_5_authority_architecture/00_identity.md)
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_85a0.md: title '00_identity' does not match filename '00_identity_85a0'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8614.md: duplicate title '00_identity' (also in 05_RECORD/archive/wave_5_authority_architecture/00_identity.md)
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8614.md: title '00_identity' does not match filename '00_identity_8614'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8d22.md: duplicate title '00_identity' (also in 05_RECORD/archive/wave_5_authority_architecture/00_identity.md)
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8d22.md: title '00_identity' does not match filename '00_identity_8d22'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_bf68.md: duplicate title '00_identity' (also in 05_RECORD/archive/wave_5_authority_architecture/00_identity.md)
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_bf68.md: title '00_identity' does not match filename '00_identity_bf68'
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_fdde.md: duplicate title '00_identity' (also in 05_RECORD/archive/wave_5_authority_architecture/00_identity.md)
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_fdde.md: title '00_identity' does not match filename '00_identity_fdde'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_2c15.md: duplicate title '01_scope' (also in 05_RECORD/archive/wave_5_authority_architecture/01_scope.md)
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_2c15.md: title '01_scope' does not match filename '01_scope_2c15'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_626d.md: duplicate title '01_scope' (also in 05_RECORD/archive/wave_5_authority_architecture/01_scope.md)
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_626d.md: title '01_scope' does not match filename '01_scope_626d'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7e65.md: duplicate title '01_scope' (also in 05_RECORD/archive/wave_5_authority_architecture/01_scope.md)
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7e65.md: title '01_scope' does not match filename '01_scope_7e65'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7f34.md: duplicate title '01_scope' (also in 05_RECORD/archive/wave_5_authority_architecture/01_scope.md)
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7f34.md: title '01_scope' does not match filename '01_scope_7f34'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_9aae.md: duplicate title '01_scope' (also in 05_RECORD/archive/wave_5_authority_architecture/01_scope.md)
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_9aae.md: title '01_scope' does not match filename '01_scope_9aae'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_bfb7.md: duplicate title '01_scope' (also in 05_RECORD/archive/wave_5_authority_architecture/01_scope.md)
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_bfb7.md: title '01_scope' does not match filename '01_scope_bfb7'
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_c262.md: duplicate title '01_scope' (also in 05_RECORD/archive/wave_5_authority_architecture/01_scope.md)
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_c262.md: title '01_scope' does not match filename '01_scope_c262'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_2822.md: duplicate title '02_authority_domain' (also in 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain.md)
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_2822.md: title '02_authority_domain' does not match filename '02_authority_domain_2822'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_590e.md: duplicate title '02_authority_domain' (also in 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain.md)
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_590e.md: title '02_authority_domain' does not match filename '02_authority_domain_590e'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_5fe5.md: duplicate title '02_authority_domain' (also in 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain.md)
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_5fe5.md: title '02_authority_domain' does not match filename '02_authority_domain_5fe5'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_b0bf.md: duplicate title '02_authority_domain' (also in 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain.md)
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_b0bf.md: title '02_authority_domain' does not match filename '02_authority_domain_b0bf'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_cf9a.md: duplicate title '02_authority_domain' (also in 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain.md)
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_cf9a.md: title '02_authority_domain' does not match filename '02_authority_domain_cf9a'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_e44f.md: duplicate title '02_authority_domain' (also in 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain.md)
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_e44f.md: title '02_authority_domain' does not match filename '02_authority_domain_e44f'
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_f721.md: duplicate title '02_authority_domain' (also in 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain.md)
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_f721.md: title '02_authority_domain' does not match filename '02_authority_domain_f721'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_0f7b.md: duplicate title '03_governed_entities' (also in 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities.md)
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_0f7b.md: title '03_governed_entities' does not match filename '03_governed_entities_0f7b'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_4d39.md: duplicate title '03_governed_entities' (also in 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities.md)
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_4d39.md: title '03_governed_entities' does not match filename '03_governed_entities_4d39'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_91aa.md: duplicate title '03_governed_entities' (also in 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities.md)
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_91aa.md: title '03_governed_entities' does not match filename '03_governed_entities_91aa'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_cbd0.md: duplicate title '03_governed_entities' (also in 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities.md)
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_cbd0.md: title '03_governed_entities' does not match filename '03_governed_entities_cbd0'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_e285.md: duplicate title '03_governed_entities' (also in 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities.md)
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_e285.md: title '03_governed_entities' does not match filename '03_governed_entities_e285'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fbe8.md: duplicate title '03_governed_entities' (also in 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities.md)
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fbe8.md: title '03_governed_entities' does not match filename '03_governed_entities_fbe8'
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fe64.md: duplicate title '03_governed_entities' (also in 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities.md)
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fe64.md: title '03_governed_entities' does not match filename '03_governed_entities_fe64'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_0dce.md: duplicate title '04_governed_actions' (also in 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions.md)
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_0dce.md: title '04_governed_actions' does not match filename '04_governed_actions_0dce'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_30e1.md: duplicate title '04_governed_actions' (also in 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions.md)
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_30e1.md: title '04_governed_actions' does not match filename '04_governed_actions_30e1'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_95ee.md: duplicate title '04_governed_actions' (also in 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions.md)
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_95ee.md: title '04_governed_actions' does not match filename '04_governed_actions_95ee'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_b8a6.md: duplicate title '04_governed_actions' (also in 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions.md)
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_b8a6.md: title '04_governed_actions' does not match filename '04_governed_actions_b8a6'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_c642.md: duplicate title '04_governed_actions' (also in 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions.md)
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_c642.md: title '04_governed_actions' does not match filename '04_governed_actions_c642'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_ce6f.md: duplicate title '04_governed_actions' (also in 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions.md)
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_ce6f.md: title '04_governed_actions' does not match filename '04_governed_actions_ce6f'
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_e614.md: duplicate title '04_governed_actions' (also in 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions.md)
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_e614.md: title '04_governed_actions' does not match filename '04_governed_actions_e614'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_0f6e.md: duplicate title '05_rules' (also in 05_RECORD/archive/wave_5_authority_architecture/05_rules.md)
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_0f6e.md: title '05_rules' does not match filename '05_rules_0f6e'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_16a1.md: duplicate title '05_rules' (also in 05_RECORD/archive/wave_5_authority_architecture/05_rules.md)
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_16a1.md: title '05_rules' does not match filename '05_rules_16a1'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_1dcb.md: duplicate title '05_rules' (also in 05_RECORD/archive/wave_5_authority_architecture/05_rules.md)
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_1dcb.md: title '05_rules' does not match filename '05_rules_1dcb'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_4c7b.md: duplicate title '05_rules' (also in 05_RECORD/archive/wave_5_authority_architecture/05_rules.md)
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_4c7b.md: title '05_rules' does not match filename '05_rules_4c7b'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_8b3b.md: duplicate title '05_rules' (also in 05_RECORD/archive/wave_5_authority_architecture/05_rules.md)
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_8b3b.md: title '05_rules' does not match filename '05_rules_8b3b'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_c40e.md: duplicate title '05_rules' (also in 05_RECORD/archive/wave_5_authority_architecture/05_rules.md)
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_c40e.md: title '05_rules' does not match filename '05_rules_c40e'
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_e057.md: duplicate title '05_rules' (also in 05_RECORD/archive/wave_5_authority_architecture/05_rules.md)
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_e057.md: title '05_rules' does not match filename '05_rules_e057'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_11c1.md: duplicate title '06_control_gates' (also in 05_RECORD/archive/wave_5_authority_architecture/06_control_gates.md)
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_11c1.md: title '06_control_gates' does not match filename '06_control_gates_11c1'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_166c.md: duplicate title '06_control_gates' (also in 05_RECORD/archive/wave_5_authority_architecture/06_control_gates.md)
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_166c.md: title '06_control_gates' does not match filename '06_control_gates_166c'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_2928.md: duplicate title '06_control_gates' (also in 05_RECORD/archive/wave_5_authority_architecture/06_control_gates.md)
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_2928.md: title '06_control_gates' does not match filename '06_control_gates_2928'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_d84d.md: duplicate title '06_control_gates' (also in 05_RECORD/archive/wave_5_authority_architecture/06_control_gates.md)
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_d84d.md: title '06_control_gates' does not match filename '06_control_gates_d84d'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_de4e.md: duplicate title '06_control_gates' (also in 05_RECORD/archive/wave_5_authority_architecture/06_control_gates.md)
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_de4e.md: title '06_control_gates' does not match filename '06_control_gates_de4e'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fbfd.md: duplicate title '06_control_gates' (also in 05_RECORD/archive/wave_5_authority_architecture/06_control_gates.md)
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fbfd.md: title '06_control_gates' does not match filename '06_control_gates_fbfd'
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fed8.md: duplicate title '06_control_gates' (also in 05_RECORD/archive/wave_5_authority_architecture/06_control_gates.md)
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fed8.md: title '06_control_gates' does not match filename '06_control_gates_fed8'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0e49.md: duplicate title '07_evidence_requirements' (also in 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements.md)
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0e49.md: title '07_evidence_requirements' does not match filename '07_evidence_requirements_0e49'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0f26.md: duplicate title '07_evidence_requirements' (also in 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements.md)
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0f26.md: title '07_evidence_requirements' does not match filename '07_evidence_requirements_0f26'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_2c0e.md: duplicate title '07_evidence_requirements' (also in 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements.md)
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_2c0e.md: title '07_evidence_requirements' does not match filename '07_evidence_requirements_2c0e'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_635c.md: duplicate title '07_evidence_requirements' (also in 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements.md)
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_635c.md: title '07_evidence_requirements' does not match filename '07_evidence_requirements_635c'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_81d9.md: duplicate title '07_evidence_requirements' (also in 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements.md)
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_81d9.md: title '07_evidence_requirements' does not match filename '07_evidence_requirements_81d9'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_b821.md: duplicate title '07_evidence_requirements' (also in 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements.md)
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_b821.md: title '07_evidence_requirements' does not match filename '07_evidence_requirements_b821'
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_d819.md: duplicate title '07_evidence_requirements' (also in 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements.md)
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_d819.md: title '07_evidence_requirements' does not match filename '07_evidence_requirements_d819'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0bab.md: duplicate title '08_state_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0bab.md: title '08_state_interaction' does not match filename '08_state_interaction_0bab'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0dd6.md: duplicate title '08_state_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0dd6.md: title '08_state_interaction' does not match filename '08_state_interaction_0dd6'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_1933.md: duplicate title '08_state_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_1933.md: title '08_state_interaction' does not match filename '08_state_interaction_1933'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_20a6.md: duplicate title '08_state_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_20a6.md: title '08_state_interaction' does not match filename '08_state_interaction_20a6'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_332a.md: duplicate title '08_state_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_332a.md: title '08_state_interaction' does not match filename '08_state_interaction_332a'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_3f98.md: duplicate title '08_state_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_3f98.md: title '08_state_interaction' does not match filename '08_state_interaction_3f98'
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_9c3e.md: duplicate title '08_state_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_9c3e.md: title '08_state_interaction' does not match filename '08_state_interaction_9c3e'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_112f.md: duplicate title '09_decision_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_112f.md: title '09_decision_interaction' does not match filename '09_decision_interaction_112f'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_4780.md: duplicate title '09_decision_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_4780.md: title '09_decision_interaction' does not match filename '09_decision_interaction_4780'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_6af2.md: duplicate title '09_decision_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_6af2.md: title '09_decision_interaction' does not match filename '09_decision_interaction_6af2'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_7983.md: duplicate title '09_decision_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_7983.md: title '09_decision_interaction' does not match filename '09_decision_interaction_7983'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_99a2.md: duplicate title '09_decision_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_99a2.md: title '09_decision_interaction' does not match filename '09_decision_interaction_99a2'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_e850.md: duplicate title '09_decision_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_e850.md: title '09_decision_interaction' does not match filename '09_decision_interaction_e850'
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_f447.md: duplicate title '09_decision_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_f447.md: title '09_decision_interaction' does not match filename '09_decision_interaction_f447'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_1bc2.md: duplicate title '10_execution_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_1bc2.md: title '10_execution_interaction' does not match filename '10_execution_interaction_1bc2'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_3465.md: duplicate title '10_execution_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_3465.md: title '10_execution_interaction' does not match filename '10_execution_interaction_3465'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_9daa.md: duplicate title '10_execution_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_9daa.md: title '10_execution_interaction' does not match filename '10_execution_interaction_9daa'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_b374.md: duplicate title '10_execution_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_b374.md: title '10_execution_interaction' does not match filename '10_execution_interaction_b374'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_c583.md: duplicate title '10_execution_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_c583.md: title '10_execution_interaction' does not match filename '10_execution_interaction_c583'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_dfa5.md: duplicate title '10_execution_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_dfa5.md: title '10_execution_interaction' does not match filename '10_execution_interaction_dfa5'
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_f270.md: duplicate title '10_execution_interaction' (also in 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction.md)
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_f270.md: title '10_execution_interaction' does not match filename '10_execution_interaction_f270'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_3b31.md: duplicate title '11_integration_contract' (also in 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract.md)
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_3b31.md: title '11_integration_contract' does not match filename '11_integration_contract_3b31'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_4292.md: duplicate title '11_integration_contract' (also in 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract.md)
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_4292.md: title '11_integration_contract' does not match filename '11_integration_contract_4292'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_43d4.md: duplicate title '11_integration_contract' (also in 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract.md)
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_43d4.md: title '11_integration_contract' does not match filename '11_integration_contract_43d4'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_532d.md: duplicate title '11_integration_contract' (also in 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract.md)
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_532d.md: title '11_integration_contract' does not match filename '11_integration_contract_532d'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_9628.md: duplicate title '11_integration_contract' (also in 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract.md)
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_9628.md: title '11_integration_contract' does not match filename '11_integration_contract_9628'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_b538.md: duplicate title '11_integration_contract' (also in 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract.md)
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_b538.md: title '11_integration_contract' does not match filename '11_integration_contract_b538'
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_c9c7.md: duplicate title '11_integration_contract' (also in 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract.md)
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_c9c7.md: title '11_integration_contract' does not match filename '11_integration_contract_c9c7'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_1432.md: duplicate title '12_failure_semantics' (also in 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics.md)
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_1432.md: title '12_failure_semantics' does not match filename '12_failure_semantics_1432'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_2f8c.md: duplicate title '12_failure_semantics' (also in 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics.md)
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_2f8c.md: title '12_failure_semantics' does not match filename '12_failure_semantics_2f8c'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_3baf.md: duplicate title '12_failure_semantics' (also in 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics.md)
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_3baf.md: title '12_failure_semantics' does not match filename '12_failure_semantics_3baf'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_79ed.md: duplicate title '12_failure_semantics' (also in 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics.md)
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_79ed.md: title '12_failure_semantics' does not match filename '12_failure_semantics_79ed'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_8df9.md: duplicate title '12_failure_semantics' (also in 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics.md)
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_8df9.md: title '12_failure_semantics' does not match filename '12_failure_semantics_8df9'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_bce6.md: duplicate title '12_failure_semantics' (also in 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics.md)
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_bce6.md: title '12_failure_semantics' does not match filename '12_failure_semantics_bce6'
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_be6e.md: duplicate title '12_failure_semantics' (also in 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics.md)
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_be6e.md: title '12_failure_semantics' does not match filename '12_failure_semantics_be6e'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_335f.md: duplicate title '13_extension_points' (also in 05_RECORD/archive/wave_5_authority_architecture/13_extension_points.md)
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_335f.md: title '13_extension_points' does not match filename '13_extension_points_335f'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_655d.md: duplicate title '13_extension_points' (also in 05_RECORD/archive/wave_5_authority_architecture/13_extension_points.md)
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_655d.md: title '13_extension_points' does not match filename '13_extension_points_655d'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_8070.md: duplicate title '13_extension_points' (also in 05_RECORD/archive/wave_5_authority_architecture/13_extension_points.md)
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_8070.md: title '13_extension_points' does not match filename '13_extension_points_8070'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_adee.md: duplicate title '13_extension_points' (also in 05_RECORD/archive/wave_5_authority_architecture/13_extension_points.md)
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_adee.md: title '13_extension_points' does not match filename '13_extension_points_adee'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_b46f.md: duplicate title '13_extension_points' (also in 05_RECORD/archive/wave_5_authority_architecture/13_extension_points.md)
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_b46f.md: title '13_extension_points' does not match filename '13_extension_points_b46f'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_c63a.md: duplicate title '13_extension_points' (also in 05_RECORD/archive/wave_5_authority_architecture/13_extension_points.md)
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_c63a.md: title '13_extension_points' does not match filename '13_extension_points_c63a'
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_cd59.md: duplicate title '13_extension_points' (also in 05_RECORD/archive/wave_5_authority_architecture/13_extension_points.md)
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_cd59.md: title '13_extension_points' does not match filename '13_extension_points_cd59'
- 05_RECORD/archive/wave_5_authority_architecture/Authority Architecture.md: duplicate filename (also at 02_KNOWLEDGE/concepts/Authority Architecture.md)
- 05_RECORD/archive/wave_5_authority_architecture/Authority Architecture.md: duplicate title 'Authority Architecture' (also in 02_KNOWLEDGE/concepts/Authority Architecture.md)
- 05_RECORD/archive/wave_5_authority_architecture/Authority Inheritance.md: duplicate filename (also at 05_RECORD/archive/wave_5.2_concepts/Authority Inheritance.md)
- 05_RECORD/archive/wave_5_authority_architecture/Authority Inheritance.md: duplicate title 'Authority Inheritance' (also in 05_RECORD/archive/wave_5.2_concepts/Authority Inheritance.md)
- 05_RECORD/archive/wave_5_authority_architecture/Authority Model.md: duplicate filename (also at 05_RECORD/archive/wave_5.2_concepts/Authority Model.md)
- 05_RECORD/archive/wave_5_authority_architecture/Authority Model.md: duplicate title 'Authority Model' (also in 05_RECORD/archive/wave_5.2_concepts/Authority Model.md)
- 05_RECORD/archive/wave_5_authority_architecture/Authority Pack Compiler.md: duplicate filename (also at 05_RECORD/archive/wave_5.2_concepts/Authority Pack Compiler.md)
- 05_RECORD/archive/wave_5_authority_architecture/Authority Pack Compiler.md: duplicate title 'Authority Pack Compiler' (also in 05_RECORD/archive/wave_5.2_concepts/Authority Pack Compiler.md)
- 05_RECORD/archive/wave_5_authority_architecture/CLAUDE.md: duplicate filename (also at 01_CAPTURE/CLAUDE.md)
- 05_RECORD/archive/wave_5_authority_architecture/Pack Versioning.md: duplicate filename (also at 05_RECORD/archive/wave_5.2_concepts/Pack Versioning.md)
- 05_RECORD/archive/wave_5_authority_architecture/Pack Versioning.md: duplicate title 'Pack Versioning' (also in 05_RECORD/archive/wave_5.2_concepts/Pack Versioning.md)
- 05_RECORD/archive/wave_5_authority_architecture/compiled_artifact_schema.md: title 'Compiled Authority Pack — Artifact Format' does not match filename 'compiled_artifact_schema'
- 05_RECORD/archive/wave_5_indexes/CLAUDE.md: duplicate filename (also at 01_CAPTURE/CLAUDE.md)
- 05_RECORD/archive/wave_5_knowledge/AM — Evolution Roadmap — Waves 5-8.md: duplicate filename (also at 05_RECORD/archive/wave_5.2_roadmap/AM — Evolution Roadmap — Waves 5-8.md)
- 05_RECORD/archive/wave_5_knowledge/AM — Evolution Roadmap — Waves 5-8.md: duplicate title 'Agent Maestro — Evolution Roadmap v0.5.0' (also in 05_RECORD/archive/wave_5.2_roadmap/AM — Evolution Roadmap — Waves 5-8.md)
- 05_RECORD/archive/wave_5_knowledge/AM — Evolution Roadmap — Waves 5-8.md: title 'Agent Maestro — Evolution Roadmap v0.5.0' does not match filename 'AM — Evolution Roadmap — Waves 5-8'
- 05_RECORD/archive/wave_5_knowledge/Platformization.md: duplicate filename (also at 05_RECORD/archive/wave_5_infrastructure/Platformization.md)
- 05_RECORD/archive/wave_5_knowledge/Platformization.md: duplicate title 'Platformization' (also in 05_RECORD/archive/wave_5_infrastructure/Platformization.md)
- 05_RECORD/archive/wave_5_memory_architecture/CLAUDE.md: duplicate filename (also at 01_CAPTURE/CLAUDE.md)
- 05_RECORD/archive/wave_5_projects/Agent Maestro — Evolution Roadmap v0.2.md: duplicate filename (also at 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Evolution Roadmap v0.2.md)
- 05_RECORD/archive/wave_5_projects/Agent Maestro — Evolution Roadmap v0.2.md: duplicate title 'Agent Maestro — Evolution Roadmap v0.2' (also in 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Evolution Roadmap v0.2.md)
- 05_RECORD/archive/wave_5_projects/CLAUDE.md: duplicate filename (also at 01_CAPTURE/CLAUDE.md)
- 05_RECORD/archive/wave_5_projects/review_queue_20260315_111629.md: title 'Escalation Review Queue — 2026-03-15 11:16' does not match filename 'review_queue_20260315_111629'
- 05_RECORD/archive/wave_5_projects/test_d3_note.md: title 'D3 Test Updated' does not match filename 'test_d3_note'
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template_sys.md: duplicate title 'Authority Pack Section Template' (also in 05_RECORD/archive/wave_5_templates/Authority Pack Section Template.md)
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template_sys.md: title 'Authority Pack Section Template' does not match filename 'Authority Pack Section Template_sys'
- 05_RECORD/archive/wave_5_templates/Authority Pack Template_sys.md: duplicate title 'Authority Pack Template' (also in 05_RECORD/archive/wave_5_templates/Authority Pack Template.md)
- 05_RECORD/archive/wave_5_templates/Authority Pack Template_sys.md: title 'Authority Pack Template' does not match filename 'Authority Pack Template_sys'
- 05_RECORD/archive/wave_5_templates/CLAUDE.md: duplicate filename (also at 01_CAPTURE/CLAUDE.md)
- 05_RECORD/archive/wave_5_templates/Concept Template_sys.md: duplicate title 'Concept Template' (also in 05_RECORD/archive/wave_5_templates/Concept Template.md)
- 05_RECORD/archive/wave_5_templates/Concept Template_sys.md: title 'Concept Template' does not match filename 'Concept Template_sys'
- 05_RECORD/archive/wave_5_templates/Decision Template_sys.md: duplicate title 'Decision Template' (also in 05_RECORD/archive/wave_5_templates/Decision Template.md)
- 05_RECORD/archive/wave_5_templates/Decision Template_sys.md: title 'Decision Template' does not match filename 'Decision Template_sys'
- 05_RECORD/archive/wave_5_templates/Governance Template_sys.md: duplicate title 'Governance Template' (also in 05_RECORD/archive/wave_5_templates/Governance Template.md)
- 05_RECORD/archive/wave_5_templates/Governance Template_sys.md: title 'Governance Template' does not match filename 'Governance Template_sys'
- 05_RECORD/archive/wave_5_templates/Index Template_sys.md: duplicate title 'Index Template' (also in 05_RECORD/archive/wave_5_templates/Index Template.md)
- 05_RECORD/archive/wave_5_templates/Index Template_sys.md: title 'Index Template' does not match filename 'Index Template_sys'
- 05_RECORD/archive/wave_5_templates/Map Template_sys.md: duplicate title 'Map Template' (also in 05_RECORD/archive/wave_5_templates/Map Template.md)
- 05_RECORD/archive/wave_5_templates/Map Template_sys.md: title 'Map Template' does not match filename 'Map Template_sys'
- 05_RECORD/archive/wave_5_templates/Modes Template_sys.md: duplicate title 'Modes Template' (also in 05_RECORD/archive/wave_5_templates/Modes Template.md)
- 05_RECORD/archive/wave_5_templates/Modes Template_sys.md: title 'Modes Template' does not match filename 'Modes Template_sys'
- 05_RECORD/archive/wave_5_templates/North Star Template_sys.md: duplicate title 'North Star Template' (also in 05_RECORD/archive/wave_5_templates/North Star Template.md)
- 05_RECORD/archive/wave_5_templates/North Star Template_sys.md: title 'North Star Template' does not match filename 'North Star Template_sys'
- 05_RECORD/archive/wave_5_templates/Pipeline Template.md: duplicate title 'Pipeline Template' (also in 05_RECORD/archive/pre_wave5/Pipeline Template — Legacy.md)
- 05_RECORD/archive/wave_5_templates/Pipeline Template_sys.md: duplicate title 'Pipeline Template' (also in 05_RECORD/archive/pre_wave5/Pipeline Template — Legacy.md)
- 05_RECORD/archive/wave_5_templates/Pipeline Template_sys.md: title 'Pipeline Template' does not match filename 'Pipeline Template_sys'
- 05_RECORD/archive/wave_5_templates/Principles Template_sys.md: duplicate title 'Principles Template' (also in 05_RECORD/archive/wave_5_templates/Principles Template.md)
- 05_RECORD/archive/wave_5_templates/Principles Template_sys.md: title 'Principles Template' does not match filename 'Principles Template_sys'
- 05_RECORD/archive/wave_5_templates/Process Template_sys.md: duplicate title 'Process Template' (also in 05_RECORD/archive/wave_5_templates/Process Template.md)
- 05_RECORD/archive/wave_5_templates/Process Template_sys.md: title 'Process Template' does not match filename 'Process Template_sys'
- 05_RECORD/archive/wave_5_templates/Project Template_sys.md: duplicate title 'Project Template' (also in 05_RECORD/archive/wave_5_templates/Project Template.md)
- 05_RECORD/archive/wave_5_templates/Project Template_sys.md: title 'Project Template' does not match filename 'Project Template_sys'
- 05_RECORD/archive/wave_5_templates/Reference Template_sys.md: duplicate title 'Reference Template' (also in 05_RECORD/archive/wave_5_templates/Reference Template.md)
- 05_RECORD/archive/wave_5_templates/Reference Template_sys.md: title 'Reference Template' does not match filename 'Reference Template_sys'
- 05_RECORD/archive/wave_5_templates/Registry Template_sys.md: duplicate title 'Registry Template' (also in 05_RECORD/archive/wave_5_templates/Registry Template.md)
- 05_RECORD/archive/wave_5_templates/Registry Template_sys.md: title 'Registry Template' does not match filename 'Registry Template_sys'
- 05_RECORD/archive/wave_5_templates/Roadmap Template_sys.md: duplicate title 'Roadmap Template' (also in 05_RECORD/archive/wave_5_templates/Roadmap Template.md)
- 05_RECORD/archive/wave_5_templates/Roadmap Template_sys.md: title 'Roadmap Template' does not match filename 'Roadmap Template_sys'
- 05_RECORD/archive/wave_5_templates/Scope Template_sys.md: duplicate title 'Scope Template' (also in 05_RECORD/archive/wave_5_templates/Scope Template.md)
- 05_RECORD/archive/wave_5_templates/Scope Template_sys.md: title 'Scope Template' does not match filename 'Scope Template_sys'
- 05_RECORD/archive/wave_5_templates/Strategy Template_sys.md: duplicate title 'Strategy Template' (also in 05_RECORD/archive/wave_5_templates/Strategy Template.md)
- 05_RECORD/archive/wave_5_templates/Strategy Template_sys.md: title 'Strategy Template' does not match filename 'Strategy Template_sys'
- 05_RECORD/archive/wave_5_templates/System Map_sys.md: duplicate title 'System Map' (also in 05_RECORD/archive/wave_5_templates/System Map.md)
- 05_RECORD/archive/wave_5_templates/System Map_sys.md: title 'System Map' does not match filename 'System Map_sys'
- 05_RECORD/archive/wave_5_templates/System Registry.md: duplicate filename (also at 05_RECORD/archive/wave_5_indexes/System Registry.md)
- 05_RECORD/archive/wave_5_templates/System Registry.md: duplicate title 'System Registry' (also in 05_RECORD/archive/wave_5_indexes/System Registry.md)
- 05_RECORD/archive/wave_5_templates/System Registry_sys.md: duplicate title 'System Registry' (also in 05_RECORD/archive/wave_5_indexes/System Registry.md)
- 05_RECORD/archive/wave_5_templates/System Registry_sys.md: title 'System Registry' does not match filename 'System Registry_sys'
- 05_RECORD/archive/wave_5_templates/System Template_sys.md: duplicate title 'System Template' (also in 05_RECORD/archive/wave_5_templates/System Template.md)
- 05_RECORD/archive/wave_5_templates/System Template_sys.md: title 'System Template' does not match filename 'System Template_sys'
- 05_RECORD/archive/wave_5_templates/Taxonomy Template_sys.md: duplicate title 'Taxonomy Template' (also in 05_RECORD/archive/wave_5_templates/Taxonomy Template.md)
- 05_RECORD/archive/wave_5_templates/Taxonomy Template_sys.md: title 'Taxonomy Template' does not match filename 'Taxonomy Template_sys'
- 06_REFLECT/CLAUDE.md: duplicate filename (also at 01_CAPTURE/CLAUDE.md)
- CLAUDE.md: duplicate filename (also at 01_CAPTURE/CLAUDE.md)
- SYSTEM_MAP.md: duplicate filename (also at 05_RECORD/archive/wave_5_knowledge/SYSTEM_MAP.md)

## Combined Warnings

### YAML Validation


- 05_RECORD/archive/wave_5_projects/AI Governance Authority Pack v1.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Audit of Proposal v3.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Contract.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Foundational Brainstorm.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Audit.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Governance Reconciliation Proposal.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v1.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Proposal v3.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/AM — Wave 5 — Treatise on Core Principles.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Agent Deployment Playbook.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.2 — Wave 2+3 Proposal.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Build Brief.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Next Moves Proposal.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase B Output Summary.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.3 — Phase C Output Summary.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Agent Maestro v0.4 — Phase D Output Summary.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Agent Maestro — Evolution Roadmap v0.2.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Agent Memory Architecture.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Audit Folder For Unintended Cross-Folder Links.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Controlled Vault Repair Operation v2.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Filename Refactor.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Next Steps.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Note Knowledge Upgrade v1.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Open Questions.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Process Unprocessed Notes Into The Vault.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/TBP Outreach Agent V1 Spec.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Tasks Hub.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Template Architecture Audit.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/To Do.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Vault Build.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Vault Integrity & Self-Healing Audit v2.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Vault Structure and Knowledge Upgrade v2.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Vault Template Compliance Scan.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Vault Upgrade Backlog.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/Weekly Reset Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/review_queue_20260315_111629.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_projects/test_d3_note.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_operational_intelligence/AI Operations.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_operational_intelligence/Agent Performance Measurement.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_operational_intelligence/Operational Agent Design.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Authority Pack Section Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Authority Pack Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Authority Pack Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Concept Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Concept Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Decision Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Decision Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Governance Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Governance Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Index Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Index Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Map Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Map Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Modes Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Modes Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/North Star Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/North Star Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Pipeline Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Pipeline Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Principles Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Principles Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Process Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Process Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Project Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Project Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Reference Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Reference Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Registry Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Registry Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Roadmap Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Roadmap Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Scope Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Scope Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Strategy Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Strategy Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/System Map.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/System Map_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/System Registry.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/System Registry_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/System Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/System Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Taxonomy Template.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_templates/Taxonomy Template_sys.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/AI Executive Systems.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/AI-Native Organizations.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/AM — Evolution Roadmap — Waves 5-8.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Evolution Roadmap v0.2.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Pipelines Map.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Projects & Experiments Map.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Agent Maestro — Quickstart.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Agent Organizations.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Anti-Agent-Sprawl Pattern.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Authority Pack Grammar.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Authority Systems.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Controlled Evolution Pattern.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Decision-Execution Separation.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Deterministic Authority Resolution Pattern.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Deterministic Control Surfaces.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Evidence Over Assumptions.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Governance Before Autonomy.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Governance Infrastructure.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Governance Systems.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Human Escalation Pattern.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Human-Agent Collaboration.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Memory Layer Registry.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Multi-Agent Coordination.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Operational Governance.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Operational Transformation.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Organizational Intelligence.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Platformization.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Thin-Edge Thick-Core Pattern.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Three-Layer Memory Model.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_knowledge/Workflow Intelligence.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_indexes/Artifact Taxonomy.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_indexes/Canonical Notes Index.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_indexes/Canonical Notes Registry.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_indexes/Glossary.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_indexes/Shared Services Index.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_reports/AM — Wave 5 — Baseline Inventory.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_reports/AM — Wave 5 — Final Audit Report.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_roadmap/AM — Evolution Roadmap — Waves 5-8.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_memory_architecture/Context Pack Architecture.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_memory_architecture/Knowledge Graph Layer.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_memory_architecture/Memory Governance.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_memory_architecture/Memory Model.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_memory_architecture/Structured Data Layer.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_memory_architecture/Vector Memory Layer.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_agent_systems/Agent Ecosystem.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_agent_systems/Agent Runtime Architecture.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_agent_systems/Agent System Architecture.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_agent_systems/Agent Workflow Architecture.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_agent_systems/Multi-Agent Systems.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_agent_systems/Shared Services.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_infrastructure/AI Org Charts.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_infrastructure/Adoption Patterns.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_infrastructure/Agent Infrastructure.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_infrastructure/Departmental Agents.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_infrastructure/Escalation Models.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_infrastructure/Governance Integration.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_infrastructure/Observability.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_infrastructure/Platformization.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/00_identity.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_2251.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_58e4.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_85a0.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8614.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_8d22.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_bf68.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/00_identity_fdde.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/01_scope.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_2c15.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_626d.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7e65.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_7f34.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_9aae.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_bfb7.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/01_scope_c262.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_2822.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_590e.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_5fe5.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_b0bf.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_cf9a.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_e44f.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/02_authority_domain_f721.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_0f7b.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_4d39.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_91aa.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_cbd0.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_e285.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fbe8.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/03_governed_entities_fe64.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_0dce.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_30e1.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_95ee.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_b8a6.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_c642.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_ce6f.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/04_governed_actions_e614.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/05_rules.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_0f6e.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_16a1.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_1dcb.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_4c7b.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_8b3b.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_c40e.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/05_rules_e057.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_11c1.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_166c.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_2928.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_d84d.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_de4e.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fbfd.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/06_control_gates_fed8.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0e49.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_0f26.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_2c0e.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_635c.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_81d9.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_b821.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/07_evidence_requirements_d819.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0bab.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_0dd6.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_1933.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_20a6.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_332a.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_3f98.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/08_state_interaction_9c3e.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_112f.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_4780.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_6af2.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_7983.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_99a2.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_e850.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/09_decision_interaction_f447.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_1bc2.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_3465.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_9daa.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_b374.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_c583.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_dfa5.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/10_execution_interaction_f270.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_3b31.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_4292.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_43d4.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_532d.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_9628.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_b538.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/11_integration_contract_c9c7.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_1432.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_2f8c.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_3baf.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_79ed.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_8df9.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_bce6.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/12_failure_semantics_be6e.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_335f.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_655d.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_8070.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_adee.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_b46f.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_c63a.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/13_extension_points_cd59.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/Authority Architecture.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/Authority Model.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/Compile Failure Semantics.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/Compiled Governance Artifacts.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Inputs.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Outputs.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/Compiler Pipeline.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/Host Bindings.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/Integration Manifest.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/compiled_artifact_schema.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5_authority_architecture/test_repair.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/Agent Architecture Synthesis.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/Agent Deployment Pipeline.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/Agent Maestro — Note Quality Rules.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/Definition Alignment Audit v1.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/Development Pipeline.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/Exploration Pipeline.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/Frontmatter Upgrade Checklist.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/Learning Pipeline.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/Master Index — Generated.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/Note Knowledge Upgrade Order.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/Pipeline Template — Legacy.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/Potential Authority Pack Templates.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/Potential Roadmap — Authority Packs.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/System Design Pipeline.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/Vault Rules Fragment.md: schema_version is 2, expected 3
- 05_RECORD/archive/pre_wave5/Vault Structure and Knowledge Upgrade v1.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/AM — Wave 5 — Audit Framework Rubric.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Agent Maestro Vault Build.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Agent Orchestration.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Agent Organization Architecture.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Agent Systems.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Agent Workflow.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Agent.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Authority Architecture.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack Compiler.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack Versioning and Inheritance.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Authority Pack.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Build Session Protocol.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Compiler Artifact Schemas Reference.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Consolidation Pipeline.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Context Pack.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Decision Authority.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Escalation Classes Reference.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Execution Architecture.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Execution Authority.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Governance Schemas Reference.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Host Options Evaluation.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Host Runtime Reference.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Human Escalation.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/LLM-Script Boundary Reference.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Maintenance Pipeline.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Memory Architecture.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Note Upgrade Workflow.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Operational Intelligence.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Operational Outcome.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Pure Agent Concepts.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Registry Anchoring.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Self-Observation Specification.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Tool Registry Design.md: schema_version is 2, expected 3
- 05_RECORD/archive/wave_5.2_concepts/Tool and Action Class Reference.md: schema_version is 2, expected 3
- 05_RECORD/logs/sessions/Session Log — SES-002 — 2026-03-14.md: schema_version is 2, expected 3
- 05_RECORD/logs/sessions/Session Log — SES-003 — 2026-03-14.md: schema_version is 2, expected 3
- 05_RECORD/logs/sessions/Session Log — SES-004 — 2026-03-15.md: schema_version is 2, expected 3
- 05_RECORD/logs/sessions/Session Log — SES-005 — 2026-03-15.md: schema_version is 2, expected 3
- 05_RECORD/logs/sessions/Session Log — SES-006 — 2026-03-15.md: schema_version is 2, expected 3
- 05_RECORD/logs/sessions/Session Log — SES-007 — 2026-03-15.md: schema_version is 2, expected 3
- 05_RECORD/logs/sessions/Session Log — SES-008 — 2026-03-15.md: schema_version is 2, expected 3
- 05_RECORD/logs/sessions/Session Log — SES-009 — 2026-03-15.md: schema_version is 2, expected 3
- 05_RECORD/logs/sessions/Session Log — SES-010 — 2026-03-15.md: schema_version is 2, expected 3
- 05_RECORD/logs/sessions/Session Log — SES-012 — 2026-03-15.md: schema_version is 2, expected 3
- 05_RECORD/logs/sessions/Session Log — SES-013 — 2026-03-15.md: schema_version is 2, expected 3
- 05_RECORD/logs/sessions/Session Log — SES-014 — 2026-03-15.md: schema_version is 2, expected 3
- 05_RECORD/logs/sessions/Session Log — SES-015 — 2026-03-15.md: schema_version is 2, expected 3
- 05_RECORD/logs/sessions/Session Log — SES-016 — 2026-03-15.md: schema_version is 2, expected 3
- 05_RECORD/logs/sessions/Session Log — SES-017 — 2026-03-15.md: schema_version is 2, expected 3

