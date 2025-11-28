## The Challenge
Stroke is a leading cause of mortality worldwide. In medical diagnostics, there is often a trade-off between **model interpretability** (knowing *why* a decision was made) and **predictive power** (catching complex, non-linear patterns).

This project explores that trade-off by modeling the **Healthcare Stroke Dataset** using two distinct approaches: a traditional Logistic Regression pipeline and a Multi-Layer Perceptron (MLP).

## Methodology
1.  **Preprocessing:** Handled class imbalance using bootstrap sampling and normalized continuous variables (BMI, Glucose).
2.  **Feature Selection:** Implemented Wrapper Methods to identify the most significant biomarkers.
3.  **Model 1 (Linear):** Logistic Regression with Regularization. This highlighted factors like *Age* and *Hypertension* as key linear drivers.
4.  **Model 2 (Non-Linear):** An MLP (Neural Network) designed to capture complex interactions that linear models miss.

## Results
We prioritized the **F1-Score** over Accuracy due to the dangerous nature of False Negatives in medicine.

While the Neural Network offered higher potential for capturing complexity, the Logistic Regression provided robust results with the added benefit of clinical interpretability. This project highlighted that in medical AI, "black box" models must justify their complexity with significant performance gains to be viable.