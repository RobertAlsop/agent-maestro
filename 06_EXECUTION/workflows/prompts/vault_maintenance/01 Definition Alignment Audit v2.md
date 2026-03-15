# Definition Alignment Audit

You are performing a concept definition alignment audit for the Agent Maestro knowledge system.

Goal:  
Ensure that concepts across the vault remain consistent, clearly defined, and properly linked as the ontology evolves.

Scope:  
Scan the entire Agent-Maestro folder.

Important:  
This is an audit only.

Do NOT modify files.  
Do NOT rename notes.  
Do NOT change frontmatter.  
Do NOT introduce new concepts.

Your role is to detect definition inconsistencies and recommend small improvements that strengthen the ontology.

---

PRIMARY FOCUS

The audit should concentrate on notes that define concepts, including notes located in:

02_KNOWLEDGE/concepts  
02_KNOWLEDGE/domains  
02_KNOWLEDGE/patterns  
05_SYSTEMS

These layers collectively define the conceptual framework of the discipline.

Also review relevant **system maps** to ensure definitions align with the relationships expressed in those maps.

Where relevant, cross-check **registry anchors** including:

- Canonical Notes Registry
    
- System Registry
    
- Authority Pack Registry
    
- Pack Version Registry
    
- Compiler Artifacts Registry
    

This ensures that definitions remain aligned with the canonical anchors of the ontology.

---

CHECK FOR

1. Definition dependencies
    

Detect important conceptual relationships that are not explicitly referenced.

Examples of relationships to check:

Agent → Agent Workflow  
Agent Workflow → Operational Outcome  
Agent Orchestration → Agent Workflow  
Agent Systems → Agent  
Authority Architecture → Authority Pack  
Authority Pack → Decision Authority / Execution Authority  
Context Pack → Memory Architecture  
Operational Intelligence → Agent Systems

Report missing references or missing conceptual links.

---

2. Boundary clarity
    

Check that related concepts have clear conceptual boundaries.

Focus especially on concept pairs that commonly drift:

Agent Workflow vs Agent Orchestration  
Decision Authority vs Execution Authority  
Memory Architecture vs Context Pack  
Operational Intelligence vs Agent Systems  
Authority Architecture vs Authority Pack

Report any notes where boundaries appear blurred.

---

3. Definition consistency
    

Check whether key terms are used consistently across the vault.

Important vocabulary includes:

agent  
workflow  
orchestration  
authority  
context  
operational intelligence  
memory architecture

Report any inconsistencies in how these terms are defined or used.

---

4. Concept duplication
    

Detect notes that may represent the same concept under different names.

If duplication exists, report:

- the notes involved
    
- the overlapping definition
    
- a suggested resolution (merge, redefine boundaries, or convert one into a pattern/example)
    

---

5. Circular definitions
    

Identify definitions that rely only on referencing each other without explaining the concept clearly.

Example:  
Concept A defined only in terms of Concept B, while Concept B is defined only in terms of Concept A.

---

6. Missing conceptual anchors
    

Check whether core concepts link to the systems or patterns that implement them.

Examples:

Concept notes should often link to:

- related system architecture notes
    
- relevant patterns
    
- relevant pipelines
    

Report missing conceptual anchors where appropriate.

---

OUTPUT FORMAT

Produce a structured report titled:

AGENT MAESTRO CONCEPT ALIGNMENT REPORT

Sections:

1. Missing Concept Links
    
2. Boundary Clarifications
    
3. Definition Inconsistencies
    
4. Potential Concept Duplication
    
5. Circular Definition Risks
    
6. Suggested Improvements
    

Each issue should include:

- note name
    
- nature of the issue
    
- recommended small fix
    

---

IMPORTANT PRINCIPLE

The goal is to maintain a stable and coherent ontology.

Only suggest minimal adjustments that improve clarity and consistency.

Do not introduce new conceptual layers unless absolutely necessary.