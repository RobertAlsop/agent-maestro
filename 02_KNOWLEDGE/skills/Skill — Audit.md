---
title: "Skill — Audit"
type: skill
status: active
authority_weight: 60
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from: ["Agent Maestro — Foundations"]
  governs: []
  related: ["Skill — Validate", "Skill — Propose", "Skill — Escalate"]
tags: [skill, audit, alignment, integrity, viability]
---

## Purpose

Audit is deep evaluation. Where Validate checks rules, Audit applies judgment. It answers: **is this good?** — aligned with intent, internally sound, and earning its place.

Audit is parameterized: the same skill applied through three lenses.

## Pipeline Stages Served

REFLECT (primary). Also called at high-stakes gate transitions (e.g., proposal → contract for governance changes).

## The Three Lenses

### Alignment (top-down)
Does this serve what's above it? Is it traceable to the Foundations?
- Core question: "Does this artifact implement its parent's intent?"
- Check: `derives_from` chain traces to Foundations or appropriate governance doc
- Failure signal: artifact drifts from stated purpose; unclear parent

### Integrity (horizontal)
Is this internally sound and correctly connected?
- Core question: "Are all parts consistent with each other and with their peers?"
- Check: No internal contradictions; all links resolve; relationships accurately described
- Failure signal: contradictory statements; orphaned sections; stale links

### Viability (bottom-up)
Is this earning its place? Could it be simplified?
- Core question: "What would be lost if this were removed or merged?"
- Check: Apply Law 3 (Economy) — only what is necessary survives
- Failure signal: duplication of something else; rarely referenced; over-engineered for current scale

## Adversarial Audit

A special mode: the auditor actively tries to find reasons the artifact should not proceed. Used at the highest-stakes transitions (governance changes, new capability claims). The standard for an adversarial audit is: **can I find a principled objection? If yes, it must be resolved before the artifact advances.**

## Process

1. Identify which lens(es) to apply (default: all three).
2. For each lens, apply the core question and check.
3. Document findings: pass, warning, or failure for each lens.
4. If any lens fails: generate a finding with evidence.
5. If findings require action: hand off to Propose or Escalate.

## Output

An audit report with findings per lens. Each finding states: lens, observation, evidence, recommended action (repair / archive / escalate / accept).
