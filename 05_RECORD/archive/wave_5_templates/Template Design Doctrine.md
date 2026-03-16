## Purpose

Define how templates govern knowledge structure inside the vault so the system remains **consistent, machine-readable, and evolvable**.

Templates ensure:

- predictable structure
    
- stable semantics
    
- machine-readable knowledge
    
- scalable architecture
    

Without templates, vault entropy grows rapidly.

---

## Principles

### 1. Templates define structural contracts

Templates are not suggestions.

They are **structural contracts** that determine:

- how knowledge is written
    
- how notes relate
    
- how AI agents reason over the vault.
    

---

### 2. Frontmatter defines machine semantics

Frontmatter exists for:

- identity
    
- authority
    
- relationships
    
- lifecycle
    

The note body exists for **human-readable knowledge**.

---

### 3. Bodies expose reasoning structure

All templates expose consistent sections:

Purpose  
Context  
Relationships  
Type-specific structure

This enables predictable parsing by AI agents.

---

### 4. Templates evolve slowly

Template changes are **system changes**.

If a template changes:

1. update the template
    
2. document the change
    
3. decide whether migration is required
    

Avoid frequent template churn.

---

### 5. Add templates only when structurally necessary

New templates should only be created when:

- the note type has a **different reasoning structure**
    
- the note requires **different frontmatter defaults**
    
- the note represents a **distinct system artifact**
    

Do not create templates simply for convenience.

---

### 6. Maps remain the primary navigation layer

The vault is navigated through:

- maps
    
- relationships
    
- queries
    

Not folder hierarchies.

This follows the vault principles of **systems over files** and **maps over hierarchies**.

Principles

---

### 7. Template drift must be corrected immediately

If a note diverges from its template:

- repair the structure
    
- update missing sections
    
- restore frontmatter
    

Consistency is critical.

---

## Governance Documents

The template system is governed by these documents, listed in authority order:

1. **Frontmatter Schema v1** — canonical field definitions and controlled vocabularies
2. **Note Templates** (22 templates) — canonical structural contracts
3. **Template Mapping** — folder-to-template assignment guide
4. **Template Registry** — canonical type-to-template mapping
5. **Template Ruleset** — validation rules and per-template specifications
6. **Template Design Doctrine** (this document) — design principles and philosophy
7. **Template Governance Rules** — creation, modification, and compliance policy

If any governance document contradicts the Frontmatter Schema or the templates themselves, the lower-authority document must be corrected.