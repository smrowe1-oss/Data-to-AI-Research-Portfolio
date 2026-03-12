# 🤖 Agentic Workflow: High-Fidelity Systematic Evidence Synthesis
### *Replicating Q1 Research Rigor through AI Orchestration*

Building on my experience leading an **Overview of Systematic Reviews for CA: A Cancer Journal for Clinicians**, I have developed a multi-agent workflow that automates the "Evidence-to-Implementation" pipeline. This system ensures that AI-generated syntheses maintain the highest standards of clinical accuracy and methodological transparency.

---

## 🏗️ The Multi-Agent Architecture
I utilize a "Principal-Agent" model where specialized AI agents perform discrete tasks under strict clinical guardrails.

### 1. The Search & Protocol Agent (The Librarian)
* **Goal:** Replicate **PRISMA** and **Cochrane** search standards.
* **Logic:** Formulates complex Boolean queries and executes searches across medical databases. It ensures that the "Source Material" is high-quality (e.g., prioritized Q1 journals).
* **Technical Guardrail:** Uses a pre-defined **PROSPERO**-style protocol to prevent "scope creep."

### 2. The Screening Agent (The Qualitative Expert)
* **Goal:** Perform Title/Abstract and Full-Text screening with 100% fidelity.
* **Logic:** Applies inclusion/exclusion criteria based on my **Situational Analysis** and **NPT** frameworks. It looks for "Acceptability" and "Suitability" markers in the text.
* **Technical Guardrail:** Employs **Double-Blind Verification** (two LLMs screen independently and a third reconciles conflicts).

### 3. The Appraisal Agent (The Methodological Critic)
* **Goal:** Evaluate study quality using **AMSTAR 2** and **CASP** checklists.
* **Logic:** Identifies risk of bias, funding conflicts, and methodological weaknesses—preventing the AI from treating "weak evidence" as "clinical fact."

### 4. The Synthesis Agent (The Lead Investigator)
* **Goal:** Generate a **Qualitative Meta-Synthesis** or Evidence Summary.
* **Logic:** Replicates the high-level synthesis logic used in my **WCMICS** and **Cancer Council** consultancies. It organizes findings into "Clinical Implementation Themes."

---

## 🛠️ Technical Stack & Validation

| Step | AI Tooling | Validation Metric |
| :--- | :--- | :--- |
| **Data Extraction** | Claude 3.5 Sonnet / Python | 1:1 match with source PDF data |
| **Quality Assessment** | Gemini 1.5 Pro | Alignment with AMSTAR 2 criteria |
| **Thematic Coding** | Dedoose + LLM API | Inter-rater reliability (IRR) checks |

---

## 📈 Impact: Scaling Q1 Standards
This workflow allows me to perform an **Umbrella Review** in days rather than months, without sacrificing the rigor required for a Q1 publication. 

* **For Clinicians:** It provides rapid, evidence-based answers to urgent clinical questions (e.g., PPH management updates).
* **For Tech Partners:** It provides a "Truth-Engine" for healthcare AI, ensuring that the RAG (Retrieval-Augmented Generation) pipelines are grounded in peer-reviewed reality.
