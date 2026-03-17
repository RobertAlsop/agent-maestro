# Operating Principles

A distilled methodology for governing systems with AI. Extracted from the Agent Maestro project (9 build waves, 13 detection tools, ~175 governance documents). These are the principles that actually changed how work gets done — not the full framework, just what transfers.

This document is designed to be dropped into any project vault and referenced by Claude when doing structural, strategic, or operational work.

---

## The Loop

Every piece of work — from reorganising a folder to redesigning a business process — follows the same six stages:

1. **Perceive** — What's actually here? What's the current state? Look before you think.
2. **Interpret** — What does it mean? What patterns, problems, or opportunities are present?
3. **Decide** — What are we going to do about it? Commit to a specific action.
4. **Act** — Do it. Scoped, bounded, reversible where possible.
5. **Record** — What happened? What changed? Write it down.
6. **Reflect** — Did it work? What did we learn? What's next?

Reflect feeds back into Perceive. The loop never ends — it closes and reopens.

**When something goes wrong, expand to all six stages.** Most mistakes come from skipping one: acting without perceiving (fixing the wrong thing), deciding without interpreting (solving a symptom), acting without recording (losing track of what changed).

**The loop scales.** A five-minute task compresses the stages into moments. A multi-week project makes each stage explicit with deliverables and checkpoints. The pattern is the same; the formality changes.

---

## Detect Before You Fix

Never change a system you haven't measured. Before improving anything:

1. **Understand the current state mechanically.** What files exist? What's the structure? What are the actual numbers? Don't rely on memory or assumptions — look.
2. **Separate what you can check with rules from what requires judgment.** "Is this file valid YAML?" is a rule. "Is this the right strategy?" is judgment. Handle them differently.
3. **Check rules first, then apply judgment.** Mechanical problems (broken links, missing files, inconsistent naming) are cheap to find and unambiguous to fix. Fix those before spending cognitive effort on strategic questions.

This prevents the most common AI failure mode: confidently restructuring something based on a misunderstanding of what's actually there.

---

## Escalation — Not Everything Needs the Same Rigour

Three levels of decision-making:

**Level 1 — Automatic.** The rules cover it. A file needs renaming to match a convention. A broken link needs fixing. The action is obvious, bounded, and reversible. Just do it.

**Level 2 — Judgment.** The principles apply but the answer isn't mechanical. "Should we restructure this section?" "Is this process serving its purpose?" Think it through, document the reasoning, proceed.

**Level 3 — Human decision.** The change is irreversible, architectural, or touches something foundational. Don't act — present the options with evidence and let the human decide.

**The rule of thumb:** If you can undo it in 30 seconds, it's Level 1. If you need to explain your reasoning, it's Level 2. If you're not sure the human would agree, it's Level 3.

When in doubt, escalate. The cost of asking is always lower than the cost of an unauthorized change.

---

## Propose Before Building

Before making significant changes to any system:

1. **State the problem.** What's wrong or missing? Be specific.
2. **Describe the proposed change.** What will you create, modify, or remove?
3. **Identify what it affects.** What existing things will be touched?
4. **Name what you're NOT doing.** Scope boundaries prevent drift.
5. **Get agreement before starting.**

This discipline prevents the most expensive kind of wasted work: building the wrong thing well. A five-sentence proposal that gets corrected costs minutes. A polished deliverable that misses the point costs hours.

---

## Conventions Govern Forward

When you establish a new convention (naming scheme, folder structure, process):

- It applies from now on. It doesn't retroactively apply to everything that came before.
- Pre-convention history is documented, not falsified. Don't rename old files to match new patterns if it would misrepresent when the convention was followed.
- Items that can be fixed without falsifying the record — fix them. Items that can't — acknowledge them and move on.

This prevents an endless cleanup treadmill and keeps the historical record honest.

---

## Seven Questions for Any System

When examining or building any system — a business, a vault, a process, a website — check whether these seven things are present and clear:

| Question | What it reveals |
|----------|----------------|
| **What is true right now?** | Current state — the facts, not the aspirations. |
| **What is this trying to achieve?** | Purpose — the goal this system serves. |
| **What is allowed or forbidden?** | Constraints — the rules, policies, boundaries. |
| **What from the past informs the present?** | Memory — history, decisions, context. |
| **What actions can be taken?** | Tools — the actual capabilities available. |
| **Who decides and who can stop?** | Control — authority, ownership, escalation paths. |
| **How do we know if it worked?** | Feedback — metrics, signals, review mechanisms. |

If something feels incomplete or stuck, one of these is missing. The most common gaps: no clear feedback mechanism (you're flying blind), no defined control (nobody owns it), or the stated goal doesn't match the actual state (aspiration-reality mismatch).

---

## Separation of Powers

The person who builds something should not be the person who reviews it. The person who proposes a change should not be the person who approves it.

In practice with AI: when Claude builds something, have Claude review it in a separate pass — or review it yourself. Don't let the same reasoning process that created a thing also validate it. Fresh eyes (even simulated ones) catch what the builder's eyes skip.

---

## Economy

Every component must earn its place. If a process, document, tool, or structure can be removed without loss of function or understanding, it should be removed.

This applies to:
- Governance (don't create rules for problems that don't exist yet)
- Documentation (don't write docs nobody will read)
- Tools (don't automate what you do once a month)
- Structure (don't create folders you won't use)

The test: "If I deleted this, what would break?" If the answer is "nothing" — delete it.

---

## How to Use This Document

**For Claude:** When starting structural work on this vault — auditing, reorganising, building new systems — read this document first. Apply the Loop. Detect before fixing. Escalate appropriately. Propose before building.

**For the human:** These principles are a thinking tool, not a compliance framework. Use them when approaching complex decisions. Skip them for quick tasks. Return to them when something feels off — the answer is usually in the Loop or the Seven Questions.

---

*Distilled from Agent Maestro v0.8.3 — a self-governing vault that proved these principles across 9 build waves. The full framework lives in the Agent Maestro vault for reference. These are the parts that transfer to any domain.*
