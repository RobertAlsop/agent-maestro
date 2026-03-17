# 02_KNOWLEDGE — Interpret

**Pipeline Stage:** Interpret — Interpretation
**Foundations Alignment:** Seed 1 (Process) — the second stage of the Irreducible Loop, where raw input becomes understood knowledge.

## Purpose

This layer contains everything the system needs to understand itself and make informed decisions. Governance defines the rules. Skills define the capabilities. Concepts define the domain. Protocols define how things are done. Templates provide patterns for creating new notes.

## Structure

- **governance/** — Constitutional documents (authority_weight ≥ 80 = canonical). Read [[Agent Maestro — Foundations]] before doing anything.
  - **governance/roles/** — [[Role — Worker]] and [[Role — Reviewer]] definitions
- **skills/** — The 7 core skill definitions (Triage, Validate, Audit, Propose, Gate, Summarize, Escalate)
- **concepts/** — Foundational domain concepts (minimum viable set, authority_weight 50-59)
- **protocols/** — Operational procedures and workflows. Git conventions are now in governance/ as [[AM — Git Conventions]].
- **templates/** — Schema v3 templates for creating new notes

## Agent Rules

**Agents MAY:**
- Read all knowledge notes
- Create new concept or reference notes following schema v3 and using available templates
- Update `SYSTEM_MAP.md` (vault root) when vault structure changes

**Agents MUST NOT:**
- Modify governance documents (authority_weight ≥ 80) without human approval (Level 3)
- Delete or archive knowledge notes without escalation
- Introduce new concepts without Reviewer evaluation (see Vault Rule 49)

## Concept Conventions

Concepts are tiered by authority weight:
- **Foundational concepts (50-59):** Load-bearing — referenced by governance or skills. Removing one creates a gap.
- **Operational concepts (30-49):** Introduced during waves, earned through use. Valuable but not load-bearing.

New concepts are introduced through the wave lifecycle per [[Agent Maestro — Vault Rules|Vault Rule 49]].

## Key Files

- `governance/Agent Maestro — Foundations.md` (authority_weight: 95) — read first
- `governance/Agent Maestro — North Star.md` (authority_weight: 97) — the supreme document
- `SYSTEM_MAP.md` (vault root) — the vault inventory
