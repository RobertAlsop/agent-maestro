# 01_CAPTURE

**Pipeline Stage:** Input — Perception
**Foundations Alignment:** Seed 1 (Process) — the first stage of the Irreducible Loop.

## Purpose

CAPTURE is the vault's inbox. Raw ideas, observations, drafts, and unsorted input land here before being triaged and routed to the correct pipeline stage. This is the lowest-friction entry point in the vault.

The key principle: **always capture first, validate second.** Governance constraints are minimal here — do not let structure prevent capture.

## Conventions

- **Flat structure.** No subfolders. Everything lives at the root of `01_CAPTURE/`.
- **Frontmatter is optional.** This is the one exception to Vault Rule 5. Captures may be bare notes with no frontmatter. When a note is triaged and routed out of Capture, the Triage skill is responsible for adding schema v3 frontmatter before the note moves to its destination.
- **Naming:** Use descriptive titles that capture the essence of the input. Formal naming conventions (Vault Rules 31-35) are not enforced here.
- **Linking:** Loose wiki-links are acceptable. Full relationship frontmatter is not required.

## Agent Rules

**Agents MAY:**
- Add new capture notes freely without approval
- Use this space to draft observations, questions, and preliminary ideas
- Link to notes in other pipeline folders

**Agents MUST NOT:**
- Delete or modify existing captures without human approval
- Assume captures are validated or canonical — they are working drafts

**Triage (routing out of Capture):**
- A Worker with [[Skill — Triage]] may route captures to the appropriate pipeline folder
- Triage adds frontmatter if not present and classifies the note (type, derives_from, tags)
- Routing is a Level 1 action — no escalation required unless the destination is governance (Level 3)

## Flow

Items in Capture flow downstream through triage:
- Knowledge items → `02_KNOWLEDGE/` (concepts, references)
- Proposals and decisions → `03_DECIDE/`
- Operational items → `04_EXECUTE/`
- Records and logs → `05_RECORD/`

Items also flow *into* Capture from the end of the pipeline:
- `06_REFLECT/` produces reflections, which are distilled into **capture seeds** filed here — this is how the loop closes.

## Capture Seeds

A capture seed is a structured handoff that starts the next unit of work. It follows a template, carries the `seed` tag, and uses the naming convention "Wave X.Y — Capture Seed.md".

Only one seed should be active at a time. When the work a seed describes begins, the seed is *consumed* — archived to `05_RECORD/archive/`.

Brainstorms, loose ideas, and observations can coexist alongside an active seed. They are raw input, not structured handoffs. The seed is always distinguishable by format and naming.

## Keep It Lean

Capture should not accumulate. Items should be triaged promptly. A full inbox is a sign that the pipeline isn't flowing.
