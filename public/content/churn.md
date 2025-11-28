## The Challenge
Predicting customer churn is standard; understanding the mathematics behind the prediction is engineering.

For this project, I didn't just train models—I also **built the algorithms from scratch**. The goal was to predict which customers would leave the bank while benchmarking my custom implementations against production-grade libraries like `caret` and `xgboost`.

## Engineering "From Scratch"
I manually implemented the following mathematical concepts in R (matrix algebra only):
* **Naive Bayes:** Calculating prior and posterior probabilities manually.
* **AdaBoost:** Writing the iterative weight update loop to focus on misclassified samples.
* **K-NN:** Calculating Euclidean distance matrices without using `class::knn`.

## Key Findings
The most surprising result was in the **Naive Bayes** comparison. My manual implementation actually achieved a **higher Recall (34.55%)** than the standard package version (23.24%) in identifying churners, albeit with a trade-off in precision.

Ultimately, **XGBoost** was selected as the production model for its ability to handle non-linear relationships between Credit Score and Balance.