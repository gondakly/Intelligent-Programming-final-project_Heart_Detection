# Heart Disease Detection — Accuracy Comparison Report

## Test Set Info
- **Total patients**: 964  
- **Test set size**: 193 patients (20% hold-out, random_state=42)  
- **Class balance** — No Disease: 91, Disease: 102

---

## Performance Results

| Metric    | Expert System (Rule-Based) | Decision Tree (ML) |
|-----------|:--------------------------:|:------------------:|
| Accuracy  | 0.5285         | 1.0 |
| Precision | 0.5285        | 1.0|
| Recall    | 1.0           | 1.0   |
| F1-Score  | 0.6915         | 1.0 |

---

## Expert System Details

### Rules Implemented (12 rules)
| Rule | Condition | Risk Level |
|------|-----------|------------|
| 1  | Exercise-induced angina (exang=1) | HIGH |
| 2  | ST depression > 0.4 (oldpeak) | HIGH |
| 3  | Major vessels coloured ≥ 2 (ca) | HIGH |
| 4  | Reversible thalassemia defect (thal=3) | HIGH |
| 5  | Asymptomatic chest pain in male (cp=0, sex=1) | HIGH |
| 6  | Max heart rate very low (thalach < 0.35) | HIGH |
| 7  | Downsloping ST segment (slope=0) | MODERATE |
| 8  | 1 major vessel coloured (ca=1) | MODERATE |
| 9  | Moderate ST depression in male (0.2 < oldpeak ≤ 0.4) | MODERATE |
| 10 | Below-average HR + flat slope (thalach < 0.5, slope=1) | MODERATE |
| 11 | Fixed thalassemia defect (thal=2) | MODERATE |
| 12 | All clear — no risk indicators fired | LOW |

---

## Decision Tree Details

**Best Hyperparameters (GridSearchCV, 5-fold CV):**
```
{
  "criterion": "gini",
  "max_depth": null,
  "min_samples_leaf": 1,
  "min_samples_split": 2
}
```

**10-Fold Cross-Validation:** 0.9969 ± 0.0094

---

## Explainability Comparison

| Aspect               | Expert System          | Decision Tree         |
|----------------------|:----------------------:|:---------------------:|
| Interpretability     | ★★★★★ (full trace)     | ★★★☆☆ (tree diagram)  |
| Accuracy             | Moderate               | High                  |
| Adaptability         | ★★☆☆☆ (manual update) | ★★★★★ (retrain)        |
| Domain knowledge req.| High                   | Low                   |
| Handles unseen data  | Fixed rules            | Generalises           |
| Audit trail          | Every rule logged      | Feature splits only   |

---

## Conclusion

The **Decision Tree** achieves higher quantitative performance by learning 
patterns directly from data. The **Expert System** trades accuracy for 
full transparency — every decision is traceable to a named clinical rule.

**Recommendation:** Use the Expert System for auditable clinical decisions;  
use the Decision Tree for scalable, automated screening at population level.  
A **hybrid approach** (ES flags edge cases, ML handles bulk prediction)  
combines the strengths of both.
