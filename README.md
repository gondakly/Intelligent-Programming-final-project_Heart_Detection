#  Heart Disease Detection System

A hybrid cardiovascular risk assessment system combining a **Rule-Based Expert System** and a **Decision Tree ML Model**, featuring a Streamlit web interface.

---
# Heart Disease Dataset Description

## 1. Project Context
This dataset is used to build a diagnostic tool for heart disease. It combines patient demographic data with clinical test results to classify the risk level of a patient.

## 2. Statistical Summary
| Feature | Data Type | Mean | Min | Max | Missing Values |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Age** | int64 | 54.43 | 29 | 77 | 0 |
| **Trestbps** | int64 | 131.61 | 94 | 200 | 0 |
| **Cholesterol** | int64 | 246.00 | 126 | 564 | 0 |
| **Thalach** | int64 | 149.11 | 71 | 202 | 0 |
| **Oldpeak** | float64 | 1.07 | 0.0 | 6.2 | 2 |

## 3. Attribute Information
- **Sex**: (1 = male; 0 = female)
- **Chest Pain (cp)**: Type of pain (0-3). Value 0 is typical angina, whereas 3 is asymptomatic.
- **Fasting Blood Sugar (fbs)**: > 120 mg/dl is signaled as 1.
- **Exang**: Angina resulting from exercise (1 = yes).
- **Ca**: Number of major vessels (0-4) visible under fluoroscopy. Higher numbers often correlate with higher risk.
- **Target**: The predicted attribute. 0 = Low Risk (No Disease), 1 = High Risk (Heart Disease).

## 4. Observations
- The dataset is relatively balanced between heart disease (51.3%) and no heart disease (48.7%).
- There are minor missing values in `restecg` and `oldpeak` that require median/mean imputation during the processing step.
- Features like `thalach` (Max Heart Rate) and `cp` (Chest Pain) show high correlation with the target variable.


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
