# 02_KNOWLEDGE — Interpret

This layer is the INTERPRET stage of the universal pipeline. It contains everything the system needs to understand itself and make informed decisions.

## Structure

- **governance/** — Constitutional documents (authority_weight ≥ 75). Read before building.
- **governance/roles/** — Worker and Reviewer role definitions
- **skills/** — The 7 core skill definitions
- **concepts/** — Domain knowledge, patterns, and workflow documentation
- **templates/** — Minimal v1.0.0 template set
- **references/** — External references and research
- **indexes/** — SYSTEM_MAP.md (the master inventory)

## Agent Rules

**Agents MAY:**
- Read all knowledge notes
- Create new notes following schema v3 and using available templates
- Update `02_KNOWLEDGE/indexes/SYSTEM_MAP.md` when vault structure changes

**Agents MUST NOT:**
- Modify governance documents (authority_weight ≥ 80) without human approval
- Delete or archive knowledge notes without escalation
- Create notes without frontmatter conforming to schema v3

## Key files

- `governance/Agent Maestro — Foundations.md` (authority_weight: 95) — read first
- `indexes/SYSTEM_MAP.md` — the vault inventory
