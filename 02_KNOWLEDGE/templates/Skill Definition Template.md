---
title: "Skill Definition Template"
type: concept
status: active
authority_weight: 60
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Vault Rules]]"
  governs: []
  related:
    - "[[Role Definition Template]]"
    - "[[General Note Template]]"
tags:
  - template
  - skill
---

# Skill Definition Template

## Purpose

Template for defining core skills in Agent Maestro. Each skill is a concrete, testable capability that agents can load and execute.

## Template

```yaml
---
title: "Skill — [Name]"
type: skill
status: draft
authority_weight: 50
schema_version: 3
created: ""
updated: ""
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
  governs: []
  related: []
tags:
  - skill
---
```

### Required Sections

**Purpose** — What this skill does, in one sentence.

**Derives From** — Which Foundations elements (seeds, laws, principles) this skill implements.

**Input** — What the skill needs to operate. What context, data, or artifacts it expects.

**Process** — The steps the skill follows. Clear enough that any model can execute them.

**Output** — What the skill produces. What artifacts, decisions, or state changes result.

**Judgment Criteria** — How the skill makes decisions when rules don't fully cover the situation. What principles it applies.

**Success Conditions** — How to verify the skill executed correctly.

**Pipeline Stages Served** — Which pipeline stages use this skill.

**Authorized Roles** — Which roles (Worker, Reviewer) can use this skill.
