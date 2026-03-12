# 📈 Project: PowerBI Executive Implementation Dashboard
### *Visualizing RE-AIM Metrics for Clinical Leadership*

This project bridges the gap between **SQL Data Engineering** and **Executive Decision-Making**. It demonstrates how I use Data Visualization to track the "Normalization" (NPT) of AI tools in real-time.

---

## 🖼️ The Executive View
I architected this dashboard to answer the three critical questions every Hospital Board asks:
1. **Reach:** Are we serving our diverse patient population (CALD)?
2. **Adoption:** Are clinicians actually using the AI, or is there 'Algorithm Aversion'?
3. **Effectiveness:** Is the AI improving clinical outcomes compared to the baseline?

---

## 🛠️ Technical Workflow (SQL to PowerBI)

1. **The Data Source:** Connecting to the `ai_clinical_interactions` SQL table (see my SQL scripts in this folder).
2. **The Logic (DAX):** I utilize DAX (Data Analysis Expressions) to calculate the **Adoption Rate** as a rolling average, allowing leadership to see if trust in the AI is growing over time.
3. **The Visualization:** * **Heat Maps:** To show 'Adoption' across different wards (Maternity vs. Oncology).
    * **Trend Lines:** To monitor 'Fidelity' and 'System Drift' (Maintenance).

---

## 🤖 Researcher's Note: The "Power" in PowerBI
From a **Foucauldian** perspective, a dashboard is a tool of 'Visibility.' By making the AI's performance visible to the Board, we ensure **Algorithmic Accountability**. 

Using the **RE-AIM** framework as my visual guide, I ensure that the 'Effectiveness' of the tool is never decoupled from its 'Reach.' This prevents 'Innovation Bias' where a tool works for the majority but fails vulnerable populations.
