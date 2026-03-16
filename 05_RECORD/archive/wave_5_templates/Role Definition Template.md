---
title: "Role Definition Template"
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
    - "[[Skill Definition Template]]"
    - "[[General Note Template]]"
tags:
  - template
  - role
---

# Role Definition Template

## Purpose

Template for defining agent roles in Agent Maestro. A role defines authority boundaries — what an agent is allowed to do, must escalate, and must not do.

## Template

```yaml
---
title: "Role — [Name]"
type: role
status: draft
authority_weight: 70
schema_version: 3
created: ""
updated: ""
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
  governs: []
  related: []
tags:
  - role
---
```

### Required Sections

**Purpose** — What this role exists to do.

**Escalation Level** — The maximum decision level this role can exercise (Level 1, Level 2, or Level 3).

**Authorized Skills** — Which skills this role can use.

**Allowed Actions** — What this role may do without escalation.

**Must Escalate** — Actions that require escalation to a higher authority (ultimately human).

**Must Not** — Actions this role is explicitly forbidden from taking. Violations indicate a governance failure.

**D6 Constraints** — How this role interacts with other roles to maintain separation of powers.
