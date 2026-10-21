# Gonzalo Cruz Gómez

**Data & AI Engineer** · Madrid, Spain

- Email: gonza.c.gomez03@gmail.com
- GitHub: https://github.com/gonzalo-cruz
- LinkedIn: https://www.linkedin.com/in/gonzalo-cruz-gomez-788516235
- Portfolio: https://gonzalo-cruz.github.io/portfolio/
- Availability: Open to junior data, ML and AI engineering roles from mid-2027

## Summary

Final-year Data Science & Engineering student at URJC (graduating June 2027), currently on Repsol's Data Intelligence Platform team. Builds data systems end to end: orchestration, streaming, and models that hold up on real data. Founder of Asociación Datalab. Three years of Telecommunications Engineering at UC3M before switching to data.

## Experience

### Data Intelligence Platform Intern — Repsol

Sep 2026 – Mar 2027 · Madrid, Spain

Talent Energy internship on the Data Intelligence Platform team at Repsol's Madrid Campus, running in parallel with the final year of the degree.

### Founder & President — Asociación Datalab

May 2025 – present · URJC, Madrid

Started the association because project-driven learning didn't exist at the university yet.

- Handled legal registration and defined the strategic roadmap from zero.
- Organised technical workshops and coordinated the first collaborative data projects.

### Mathematics & Physics Tutor — Self-employed

Sep 2021 – present · Madrid, Spain

Tutored high-school students through calculus, linear algebra, mechanics and electromagnetism, including Selectividad preparation.

- 100% pass rate over five years; 90% of students improved by at least three grade points.
- Built individual study plans per student rather than a shared syllabus.

## Projects

### TripAdvisor Restaurants Pipeline

Data Engineering / MLOps · Sep 2025 – Jan 2026

<https://github.com/gonzalo-cruz/Tripadvisor-restaurants-pipeline>

Full-stack data system over European restaurant data: a five-task Airflow DAG for ETL plus ML plus streaming, a distributed clustering stage, and a web app on top.

- Orchestrated a five-task Airflow DAG over 1M+ rows in 50k-row chunks — extract, clean, EDA, preprocess (normalisation, OHE or label encoding by cardinality, incremental PCA), stream to Kafka — so the pipeline stays memory-safe on a laptop.
- Applied PySpark ML KMeans with automatic K selection via silhouette scoring (K = 10–80); every parameter (chunk size, thresholds, Kafka config) lives in one config.toml read at runtime.
- Built two Spark Structured Streaming consumers — a fast filter path and an ML-scored path computing centroid distances — writing timestamped classifications in real time.
- Shipped a FastAPI + React/Vite app: restaurant search by cosine similarity within clusters, plus a live scoring tab pushing classifications to the browser over Server-Sent Events.
- Streamed to Kafka with a fault-tolerant producer (acks=all, sub-batch delivery).

Keywords: Airflow, PySpark, Kafka, Spark Streaming, FastAPI, React, Docker, Python

### Stroke Risk Prediction

Applied ML · Imbalanced classification · Feb 2025 – May 2025

<https://github.com/gonzalo-cruz/Predictive-stroke-analysis>

Binary classification of stroke risk on 5,110 patients at roughly 5% positive rate, where a false negative costs far more than a false positive.

- Optimised for recall over accuracy and moved the decision threshold explicitly, since the clinical cost of a missed stroke dominates the cost of a false alarm.
- Rebalanced with SMOTE and selected features with RFECV rather than hand-picking.
- Benchmarked an MLP against a logistic-regression baseline (0.88 recall, 0.84 AUC); kept AUC-ROC and F1 as the reported metrics.

Keywords: scikit-learn, TensorFlow, SMOTE, RFECV, SVM, imbalanced-learn

### Real-Time Hashtag Trending

Streaming / Distributed · Oct 2025 – Dec 2025

<https://github.com/gonzalo-cruz/real-time-twitter-hashtag-analysis>

Continuous ranking of trending hashtags over a live tweet feed, using Spark DStreams and a five-minute sliding window.

- Filtered to US-only tweets before aggregation to keep the ranking meaningful instead of dominated by non-English noise.
- Implemented the window with a reduceByKeyAndWindow inverse function, so each slide costs the interval rather than the whole window.

Keywords: PySpark, DStreams, Windowing, TCP sockets, Python

### Hadoop Sentiment Analysis

Data Engineering · Mar 2025 – Jun 2025

<https://github.com/gonzalo-cruz/Twitter-sentiment-analysis-hadoop>

AFINN-111 sentiment scoring over a 314MB Twitter corpus on a cluster built from scratch rather than borrowed.

- Stood up HDFS and YARN across containers with Docker Compose, including the deploy script, instead of using a pre-built image.
- Wrote the MapReduce job to score each tweet against the AFINN-111 lexicon and aggregate by term.

Keywords: Hadoop, MapReduce, HDFS, YARN, Docker Compose

### Forest Fire Spread Prediction

Statistical Modeling · Apr 2025 – Jun 2025

<https://github.com/gonzalo-cruz/Forest-fires-prediction>

Predicting burned area in Montesinho Natural Park from meteorological covariates, on data that is zero-inflated and heavily right-skewed — the case where OLS quietly fails.

- Compared GLM and GAM fits by cross-validated RMSE; GAMs won because the covariate effects are not linear.
- Handled high skew, missing values and near-zero-variance predictors with log transforms, imputation and feature selection before modelling.

Keywords: R, mgcv, GAM, GLM, cross-validation

### Bank Customer Churn

ML from first principles · Nov 2024 – Jan 2025

<https://github.com/gonzalo-cruz/Bank-customer-churn>

Churn prediction on 10,000 customers with Naive Bayes, AdaBoost and K-NN implemented from the maths in base R, then compared against library versions.

- Reimplemented each algorithm from its mathematical definition to check understanding, then compared against the off-the-shelf implementation.
- The from-scratch Naive Bayes reached 34.55% recall against the library's 23.24% — the gap came from how smoothing was handled on rare categories.

Keywords: R, Naive Bayes, AdaBoost, K-NN, PCA, K-Means

### Cross-Lingual Sentiment Study

NLP Research · Sep 2026 – Jun 2027 · in progress

<https://github.com/gonzalo-cruz>

Ongoing study of cross-lingual sentiment transfer between Spanish and English with XLM-R, focused on evaluation rather than headline F1.

- Building the evaluation harness first: per-language slices, label-distribution shifts and error analysis instead of a single aggregate score.
- Fine-tuning on a 4GB-VRAM GPU, which forces explicit choices about batch size, gradient accumulation and fp16.

Keywords: XLM-R, PyTorch, Hugging Face, Evaluation, Multilingual NLP

### Final Degree Thesis — ANN over multimodal data

Thesis (TFG) · 15 ECTS · Sep 2026 – Jun 2027 · in progress

<https://github.com/gonzalo-cruz>

Final degree thesis on approximate nearest-neighbour search over multimodal data, on an existing algorithm owned by the advising group. Definitive title pending.

- First phase is a codebase audit and profiling of the existing implementation, not a rewrite.
- Rebuilding parts of it in Polars, with MLflow for experiment tracking and Airflow for the benchmark runs.

Keywords: Python, ANN, Multimodal, Benchmarking, Profiling

### Time Series Analysis with SARIMA

Forecasting · Feb 2025 – Apr 2025

<https://github.com/gonzalo-cruz/time-series-analysis>

Four series forecast following Box-Jenkins — identify, estimate, diagnose, repeat — with grid search, Fourier terms and temporal windowing.

Keywords: Python, statsmodels, SARIMA

### Whitehead Sample Size Analysis

Statistical Inference · May 2025 – Jun 2025

<https://github.com/gonzalo-cruz/Whitehead-sample-size-IE>

Minimum n to detect a deviation from p₀ = 0.003, comparing Score Test, exact binomial and Wilcoxon at the edge of their validity.

Keywords: R, MLE, Score Test, Monte Carlo

### Dual-Mode RC Robot

Embedded / Robotics · Sep 2024 – Dec 2024

<https://github.com/gonzalo-cruz/RC-object-avoiding-robot>

STM32 Nucleo-L152RE vehicle with autonomous ultrasonic avoidance or manual Bluetooth control, on interrupt-driven firmware (TIM2 capture, TIM3 PWM).

Keywords: C, STM32, PWM, Bluetooth

## Education

### B.S. Data Science & Engineering — Universidad Rey Juan Carlos (URJC)

Sep 2024 – Jun 2027 · final year

Final year, graduating June 2027. Completed two full academic years in one (2024–2025).

Coursework: Machine Learning, Distributed Systems, Deep Learning, HPC, Statistical Inference, Non-Relational Databases, Visualisation

### B.S. Telecommunications Engineering — Universidad Carlos III de Madrid (UC3M)

Sep 2019 – Jun 2023 · transferred

120+ credits in networking, physics and signal processing. Transferred to specialise in data science.

## Skills
- **Programming:** Python, R, SQL, C, Bash
- **Data engineering:** Airflow, Kafka, PySpark, Hadoop, Docker, Polars, DuckDB, FastAPI
- **Modeling:** PyTorch, scikit-learn, XGBoost, MLflow, mgcv, Hugging Face, LLM fine-tuning
- **Tools:** Git / GitHub, Linux, React / Vite, LaTeX, Claude Code (agentic)
- **Spoken:** Spanish — native, English — C2, German — B1, Chinese — HSK3

## Languages
- Spanish — Native
- English — C2 — Cambridge
- German — B1
- Chinese — HSK3

## Certifications
- Certificate of Advanced English (C2) — Cambridge Assessment, Jun 2019

---

Canonical source: cv.toml · updated 2026-10-21 · v1.1
Interactive version: https://gonzalo-cruz.github.io/portfolio/cv/
PDF: https://gonzalo-cruz.github.io/portfolio/CV.pdf
