---
type: project
note_class: execution
domain:
layer: execution

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Project Template"

status: active
review_status: approved
version: 1

created_date:
last_modified:

owner:

relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to: []
  uses: []
  produces: []



source_type: human_authored
supersedes: []
superseded_by: []

tags: []

hash:
---

# Purpose
Define a bounded initiative with a specific objective.

# Context
Projects organize coordinated work over time toward a defined outcome.

# Relationships
Explain how this project connects to systems, pipelines, or strategy.

# Scope

## Objective
The primary result this project is intended to achieve.

## Deliverables
Concrete outputs expected from the project.

## Constraints
Limits, assumptions, or non-negotiable conditions.

## Success Criteria
How success will be judged.

## Risks
Known uncertainties, blockers, or failure conditions that may affect the project.

# Standard Subfolders

Projects that follow the Build Session Protocol should organize artifacts into these subfolders:

| Subfolder | Purpose | Lifecycle Stage |
|-----------|---------|----------------|
| `brainstorms/` | Exploratory notes, hypotheses, raw ideas | Stage 0 (Brainstorm) |
| `briefs/` | Structured briefs and roadmaps | Stage 2 (Brief) |
| `proposals/` | Build contracts and proposals | Stage 3 (Proposal) |
| `audits/` | Adversarial audits and alignment reviews | Stage 4 (Audit) |
| `contracts/` | Approved build contracts | Stage 3 → 5 (Approval) |
| `summaries/` | Output summaries and session logs | Stage 6 (Summary) |