#  Heart Disease Detection System

A hybrid cardiovascular risk assessment system combining a **Rule-Based Expert System** and a **Decision Tree ML Model**, featuring a Streamlit web interface.

---

##  Setup

```bash
pip install -r requirements.txt
streamlit run ui/app.py
```

---

## Run Each Step

```bash
# Step 2 — Visualizations (5 figures)
python notebooks/data_visualization.py

# Step 4 — Train Decision Tree
python ml_model/train_model.py

# Step 5 — Compare systems
python reports/generate_comparison.py

# Step 3+4+5 — Full Streamlit UI
streamlit run ui/app.py

# Expert System CLI (interactive)
python rule_based_system/expert_system.py
```

---

##  Features Used

| Feature | Description |
|---------|-------------|
| `oldpeak` | ST depression (normalised 0–1) |
| `exang` | Exercise-induced angina (0/1) |
| `thalach` | Max heart rate (normalised 0–1) |
| `cp` | Chest pain type (0=asymptomatic … 3=typical) |
| `ca` | Major vessels coloured (0–4) |
| `thal` | Thalassemia (0=unknown, 1=normal, 2=fixed, 3=reversible) |
| `slope` | ST slope (0=down, 1=flat, 2=up) |
| `sex` | 1=Male, 0=Female |

---

##  Expert System Rules (12 rules)

| # | Condition | Risk |
|---|-----------|------|
| 1 | Exercise-induced angina (exang=1) |  HIGH |
| 2 | ST depression > 0.4 |  HIGH |
| 3 | Major vessels ≥ 2 |  HIGH |
| 4 | Reversible thalassemia (thal=3) |  HIGH |
| 5 | Asymptomatic chest pain in male |  HIGH |
| 6 | Max HR < 0.35 (very low) |  HIGH |
| 7 | Downsloping ST (slope=0) |  MODERATE |
| 8 | 1 vessel coloured (ca=1) |  MODERATE |
| 9 | Moderate ST depression in male |  MODERATE |
| 10 | Low HR + flat slope |  MODERATE |
| 11 | Fixed thalassemia (thal=2) |  MODERATE |
| 12 | All clear |  LOW |

---

##  Project Structure

```
Heart_Disease_Detection/
├── data/
│   └── cleaned_data.csv
├── notebooks/
│   ├── data_visualization.py
│   └── figures/  (8 plots)
├── rule_based_system/
│   └── expert_system.py
├── ml_model/
│   ├── train_model.py
│   ├── decision_tree_model.joblib
│   └── metrics.json
├── reports/
│   ├── generate_comparison.py
│   └── accuracy_comparison.md
├── ui/
│   └── app.py
├── requirements.txt
└── README.md
```
