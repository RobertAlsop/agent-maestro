---
type: system
note_class: architecture
domain: ai_governance
layer: systems

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Compile Failure Semantics"

status: active
review_status: approved
version: 1

created_date: 2026-03-12
last_modified: 2026-03-12

owner: AgentMaestro

relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to: []
  uses: []
  produces: []



source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - system
  - compiler
  - governance

hash: ""
---

# Compile Failure Semantics

## Purpose

Defines what the Authority Pack Compiler]] does when compilation cannot complete — the failure modes, error classifications, and response requirements at each pipeline stage.

## Core Rule

When compilation fails, no partial compiled artifact is produced. Compilation is atomic: it either produces a fully valid artifact or nothing. This prevents partial governance from being accidentally deployed.

## Failure Classification

| Failure Code | Description | Severity | Required Response |
|---|---|---|---|
| `FAIL.SCHEMA` | Input pack fails schema validation | Error | Fix pack schema; resubmit |
| `FAIL.LINEAGE` | Inheritance graph has missing or cyclic references | Error | Fix pack lineage declarations |
| `FAIL.OVERRIDE` | Override declared but violates `non_overridable` rule | Error | Remove or redesign override |
| `FAIL.CONFLICT` | Policy conflict unresolvable by [[Policy Resolution Pattern]] | Error | Redesign conflicting rules; may need human decision |
| `FAIL.INCOMPLETE` | Required pack sections missing | Error | Complete pack before compiling |
| `FAIL.BINDING` | Host binding fails | Error | Verify host identifier and runtime compatibility |
| `WARN.OVERRIDE` | Override declared but unusual (not an error) | Warning | Review and acknowledge |
| `WARN.DEPTH` | Inheritance depth exceeds recommended limit | Warning | Consider architecture review |

## Failure Response

1. Compiler halts the pipeline at the failed stage
2. A failure report is generated (not registered as a compiled artifact)
3. The failure is logged with: stage, failure code, affected pack/section, and reason
4. No deployment may proceed until failure is resolved

## Relationships

- Authority Pack Compiler]] — the system whose failures this defines
- [[Compiler Pipeline]] — the pipeline stages that generate these failures
- [[Policy Resolution Pattern]] — FAIL.CONFLICT is triggered when resolution fails
- [[Authority Pack Compiler — Map]]
