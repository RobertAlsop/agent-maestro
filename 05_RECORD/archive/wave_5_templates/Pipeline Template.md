---
schema_version: 2
title: "Pipeline Template"
type: pipeline
note_class: execution
domain: "{{domain}}"
layer: pipes
authority_weight: 65
resolution_basis: authority_weight
status: draft
review_status: draft
version: 1
created_date: "{{date}}"
last_modified: "{{date}}"
owner: AgentMaestro
source_type: "{{source_type}}"
relationships:
  defines: []
  part_of: []
  implements:
    - "[[Agent Maestro — Foundations]]"
  governs: []
  inherits_from: []
  applies_to: []
  uses: []
  produces: []
  supersedes: []
  superseded_by: []
tags:
  - pipeline
  - "{{domain}}"
hash: ""
---

# {{Pipeline Name}}

## Purpose

{{One sentence: what does this pipeline accomplish and for whom?}}

## Traceability

**Derives from**: {{Which kernel element(s) does this pipeline instantiate? e.g., "Process seed (Irreducible Loop) applied to {{domain}}"}}

## Stages

Map stages to the Irreducible Loop where applicable:

```
1. {{Stage Name}} (Perception)
       ↓
2. {{Stage Name}} (Interpretation)
       ↓
3. {{Stage Name}} (Validation gate)
       ↓
4. {{Stage Name}} (Action)
       ↓
5. {{Stage Name}} (Memory)
       ↓
6. {{Stage Name}} (Feedback)
```

### Stage 1 — {{Stage Name}}

**Loop mapping**: Perception
**Executor**: {{Script / LLM / Human}}
**Input**: {{What triggers or feeds this stage}}
**Action**: {{What happens}}
**Exit condition**: {{When is this stage complete?}}

### Stage 2 — {{Stage Name}}

**Loop mapping**: Interpretation
**Executor**: {{Script / LLM / Human}}
**Input**: {{Output of Stage 1}}
**Action**: {{What happens}}
**Exit condition**: {{When is this stage complete?}}

### Stage 3 — {{Stage Name}}

**Loop mapping**: Validation gate (Decision)
**Executor**: {{Script / LLM / Human}}
**Input**: {{Output of Stage 2}}
**Action**: {{Validate, approve, or reject}}
**Exit condition**: {{Approval criteria met}}

### Stage 4 — {{Stage Name}}

**Loop mapping**: Action
**Executor**: {{Script / LLM / Human}}
**Input**: {{Approved output of Stage 3}}
**Action**: {{Execute the primary work}}
**Exit condition**: {{Work complete, verifiable outcome}}

### Stage 5 — {{Stage Name}}

**Loop mapping**: Memory
**Executor**: {{Script / LLM / Human}}
**Input**: {{Output of Stage 4}}
**Action**: {{Record outcomes, update logs, create artifacts}}
**Exit condition**: {{All outcomes logged per Law 2}}

### Stage 6 — {{Stage Name}}

**Loop mapping**: Feedback
**Executor**: {{Script / LLM / Human}}
**Input**: {{Logged outcomes from Stage 5}}
**Action**: {{Evaluate what worked, what didn't, what's next}}
**Exit condition**: {{Forward-looking insights captured}}

---

## Entry Conditions

- {{What must be true before this pipeline runs?}}

## Exit Conditions

- {{What must be true for this pipeline to be considered complete?}}

## Cadence

| Trigger | Response |
|---------|----------|
| {{Event or schedule}} | {{Run full pipeline / specific stages}} |

## Relationships

- {{Parent pipeline or protocol, if any}}
- {{What governance documents does this implement?}}
- {{What does this pipeline produce?}}
