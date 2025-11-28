---
title: "Forest Fire Prediction: Generalized Additive Models (GAMs)"
date: 2025-02-20
description: "Modeling skewed environmental data using GAMs and smoothing splines to detect non-linear climatic dependencies."
tags: ["Statistics", "R", "Regression", "GAMs"]
---

## The Challenge
Environmental data is rarely "normal." The **Montesinho Forest Fire dataset** is notoriously difficult because it is:
1.  **Zero-Inflated:** Most days have 0 hectares burned.
2.  **Right-Skewed:** A few massive fires skew the mean.
3.  **Non-Linear:** Wind speed doesn't increase fire risk linearly; it has threshold effects.

## Statistical Approach
Standard Linear Regression failed to capture the complexity ($R^2$ was negligible). I advanced the analysis using:
* **Log-Transformation:** $log(x+1)$ to handle the zero-inflation and skew.
* **Generalized Additive Models (GAMs):** Using the `mgcv` library, I applied smoothing splines to meteorological variables.

## The Discovery
The GAM analysis revealed that **Temperature** and **Drought Code (DC)** have distinct non-linear curves. For example, fire risk doesn't rise consistently with temperature; it spikes after a specific thermal threshold. This interpretability is crucial for forestry management, proving that "black box" models aren't always the answer for scientific data.