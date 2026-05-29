#!/usr/bin/env python3
"""
Gonzalo Cruz — Portfolio CLI
─────────────────────────────
pip install textual
python portfolio_cli.py

Keys: [1-7] jump to section · [↑↓] scroll · [q] quit
"""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Vertical, ScrollableContainer
from textual.widgets import Static, ListView, ListItem, Label, Footer

from rich.text import Text
from rich.table import Table
from rich.rule import Rule
from rich.console import Group
from rich.padding import Padding
from rich import box as rbox

# ── PALETTE ────────────────────────────────────────────────────────────────

P  = "#7C3AED"   # purple accent
M  = "#666666"   # muted
W  = "#EAEAEA"   # white
BG = "#0D0D0D"   # background
BC = "#141414"   # card background
BR = "#2A2A2A"   # border

NAV = [
    ("01", "About"),
    ("02", "Education"),
    ("03", "Experience"),
    ("04", "Stack"),
    ("05", "Projects"),
    ("06", "Now"),
    ("07", "Contact"),
]
SECTIONS = [name for _, name in NAV]


# ── HELPERS ────────────────────────────────────────────────────────────────

def sh(num: str, title: str):
    """Section header with rule."""
    t = Text()
    t.append(f" {num}  ", style=f"dim {M}")
    t.append(title.upper(), style=f"bold {W}")
    return Group(t, Rule(style=BR))


def entry(date: str, kind: str, title: str, org: str, desc: str) -> Text:
    t = Text()
    t.append(f"\n  {date:<18}", style=f"dim {M}")
    t.append(f"{kind}\n", style=P)
    t.append(f"  {title}\n", style=f"bold {W}")
    t.append(f"  {org}\n", style=f"dim {M}")
    t.append(f"  {desc}\n", style=f"dim {W}")
    return t


def cat_table(rows: list[tuple[str, str]]) -> Table:
    tbl = Table(box=None, show_header=False, padding=(0, 2), expand=False)
    tbl.add_column(style=W, width=22, no_wrap=True)
    tbl.add_column(style=f"dim {M}")
    for name, desc in rows:
        tbl.add_row(name, desc)
    return tbl


# ── SECTION RENDERERS ──────────────────────────────────────────────────────

def render_about():
    parts = [sh("01", "About")]

    for body in [
        "Building a machine learning system is mostly not about the model. "
        "It's about making sure the data gets there reliably, that the pipeline doesn't break at 3am, "
        "that the transformers you fit in development still make sense on the data you see in production. "
        "That's the part I find genuinely interesting — and the part most people underinvest in.",

        "Four years in Telecommunications Engineering gave me something unusual for a data scientist: "
        "real fluency with the math. Not pattern-matching on formulas, but understanding why a convolution "
        "is useful or what a Fourier transform is actually telling you. That foundation makes the jump into "
        "ML engineering feel like a natural extension rather than a context switch.",

        "I'm in my final year at URJC and running Datalab alongside coursework — a student association I "
        "founded because collaborative, project-driven learning didn't exist yet. Most of what I've built "
        "started as a question I couldn't answer from a lecture slide.",
    ]:
        t = Text(f"\n  {body}\n", style=f"dim {W}")
        parts.append(t)

    skills_lbl = Text(f"\n  SKILLS\n", style=f"bold {P}")
    parts.append(skills_lbl)

    tbl = Table(box=None, show_header=False, padding=(0, 2), expand=False)
    tbl.add_column(style=f"dim {M}", width=20, no_wrap=True)
    tbl.add_column(style=f"dim {W}")
    tbl.add_row("Data Engineering",  "Apache Airflow · Kafka · PySpark · Hadoop · HDFS · Docker")
    tbl.add_row("ML / Modeling",     "scikit-learn · PyTorch · XGBoost · SMOTE · GAM/GLM · Time Series")
    tbl.add_row("Languages & Tools", "Python · R · C · SQL · Bash · Excel")
    tbl.add_row("HPC",               "OpenMP · MPI · CUDA")
    tbl.add_row("Spoken",            "ES (Native) · EN (C2) · DE (B2) · ZH (HSK3)")
    parts.append(Padding(tbl, (0, 0, 1, 0)))

    return Group(*parts)


def render_education():
    return Group(
        sh("02", "Education"),
        entry("2024 — Present", "CURRENT",
              "B.S. Data Science & Engineering", "URJC · Madrid",
              "Final year (exp. 2027). Two full academic years in one (2024–2025). "
              "Coursework: ML, Distributed Systems, Deep Learning, HPC, Statistical Inference."),
        Rule(style=BR),
        entry("2019 — 2023", "TRANSFERRED",
              "B.S. Telecommunications Engineering", "UC3M · Madrid",
              "120+ credits in Networking, Physics, and Signal Processing. "
              "Transferred to specialize in Data Science. The math carries directly into ML engineering."),
        Rule(style=BR),
        entry("2019", "CERTIFICATION",
              "Certificate of Advanced English — C2", "Cambridge Assessment",
              "Highest level of the Cambridge English suite."),
    )


def render_experience():
    return Group(
        sh("03", "Experience"),
        entry("2025 — Present", "COMMUNITY  ★ FEATURED",
              "Founder & President — Datalab", "URJC · Madrid",
              "Founded the first data science student association at URJC. "
              "Strategic roadmap, legal registration, community from zero. "
              "Goal: make it easier for students to work on real problems together."),
        Rule(style=BR),
        entry("2020 — Present", "TEACHING · 5 YEARS",
              "Math & Physics Tutor", "Self-employed · Madrid",
              "Five years tutoring high school students in mathematics and physics — "
              "calculus, linear algebra, mechanics, electromagnetism. "
              "Teaching this long forces you to explain things clearly."),
    )


def render_stack():
    parts = [sh("04", "Stack")]

    categories = [
        ("Engineering", [
            ("Apache Airflow",  "DAG orchestration; TaskFlow API — 2 pipeline projects"),
            ("Apache Kafka",    "Event streaming, acks=all producers, sub-batch delivery"),
            ("PySpark",         "DStreams windowed aggregation with inverse reduction"),
            ("Hadoop / HDFS",   "MapReduce on 314MB+ datasets; YARN job submission"),
            ("Docker / Compose","Containerized Hadoop clusters and Kafka brokers"),
            ("pandas / NumPy",  "Chunked 1M+ row processing without OOM"),
        ]),
        ("ML & Statistics", [
            ("scikit-learn",    "Classification pipelines, RFECV, PCA, SMOTE"),
            ("PyTorch",         "CNNs, LLM fine-tuning, custom training loops"),
            ("XGBoost",         "Gradient boosting for churn and risk prediction"),
            ("Time Series",     "SARIMA, forecasting, decomposition, stationarity"),
            ("R / mgcv",        "GAMs, GLMs, Gamma/Inverse Gaussian, inference"),
            ("From scratch",    "Naive Bayes, AdaBoost, K-NN — hand-rolled and benchmarked"),
        ]),
        ("High Performance Computing", [
            ("OpenMP", "Shared-memory parallelism, loop parallelization"),
            ("MPI",    "Distributed-memory communication, collective operations"),
            ("CUDA",   "GPU kernel programming, memory hierarchy, parallel reduction"),
        ]),
        ("Other", [
            ("C",           "Systems programming, memory management, HPC coursework"),
            ("Excel",       "Data analysis, pivot tables, advanced formulas"),
            ("Claude Code", "Agentic coding, extended context engineering"),
        ]),
    ]

    for cat_name, rows in categories:
        parts.append(Text(f"\n  {cat_name}", style=f"bold {P}"))
        parts.append(Padding(cat_table(rows), (0, 0, 1, 0)))

    return Group(*parts)


def render_projects():
    parts = [sh("05", "Projects")]

    projects = [
        ("01", "Data Engineering / MLOps", "TripAdvisor Restaurants Pipeline",
         "★ FEATURED",
         "Full-stack data system: Airflow DAG on 1M+ rows, PySpark ML KMeans with auto-K selection "
         "(silhouette, K=10–80), dual Spark Structured Streaming consumers, FastAPI + React web app "
         "with SSE live scoring.",
         ["Airflow", "PySpark", "Kafka", "Spark Streaming", "FastAPI", "React", "Docker"],
         "github.com/gonzalo-cruz/SD2-proyecto"),

        ("02", "Streaming / Distributed", "Real-Time Hashtag Trending",
         "O(slide interval) not O(window size)",
         "PySpark DStreams with inverse reduction (invFunc). 5-min sliding window, 10s slides. "
         "30× cheaper per update than naive full-window recomputation.",
         ["PySpark", "DStreams", "Windowing", "Python"],
         "github.com/gonzalo-cruz/real-time-twitter-hashtag-analysis"),

        ("03", "Data Engineering", "Hadoop Sentiment Analysis",
         "314MB dataset · fully Dockerized cluster",
         "AFINN-111 sentiment scoring via MapReduce on a Dockerized Hadoop cluster (HDFS + YARN). "
         "Automated HDFS upload and job submission script.",
         ["Hadoop", "MapReduce", "HDFS/YARN", "Docker Compose", "Python"],
         "github.com/gonzalo-cruz/Twitter-sentiment-analysis-hadoop"),

        ("04", "Applied ML", "Stroke Risk Prediction",
         "0.88 Recall · 0.84 AUC",
         "Binary classification on heavily imbalanced medical data. Deliberately optimized for Recall. "
         "SMOTE + RFECV + threshold tuning. Diagnosed RBF-SVM's failure mode (majority-class collapse).",
         ["scikit-learn", "SMOTE", "RFECV", "SVM", "MLP", "Python"],
         "github.com/gonzalo-cruz/Predictive-stroke-analysis"),

        ("05", "ML from Scratch", "Bank Customer Churn",
         "Manual NB: 34.55% Recall vs library 23.24%",
         "XGBoost + hand-rolled Naive Bayes, AdaBoost, K-NN from math first principles. "
         "The scratch implementation beat the library on Recall. K-Means segmentation before boosting.",
         ["R", "XGBoost", "PCA", "K-Means", "AdaBoost"],
         "github.com/gonzalo-cruz/Bank-customer-churn"),

        ("06", "Statistical Modeling", "Forest Fire Prediction",
         "GAMs found non-linearities invisible to OLS and GLMs",
         "OLS → Gamma GLM → Inverse Gaussian GLM → GAMs with smoothing splines (mgcv). "
         "GAMs revealed threshold effects for temperature and Drought Code that parametric models missed.",
         ["R", "GAM", "GLM", "mgcv", "tidyverse"],
         "github.com/gonzalo-cruz/Forest-fires-prediction"),

        ("07", "Embedded Systems", "Dual-Mode RC Robot",
         "TIM2 capture · TIM3 PWM · USART2 Bluetooth",
         "STM32 Nucleo-L152RE. Autonomous (ultrasonic, 3 distance thresholds) + Bluetooth RC mode. "
         "Fully interrupt-driven C firmware with soft PWM braking.",
         ["C", "STM32", "HAL", "PWM", "Bluetooth", "Embedded"],
         "github.com/gonzalo-cruz/RC-object-avoiding-robot"),

        ("08", "Statistical Inference", "Whitehead Sample Size Analysis",
         "Score Test vs Exact Binomial vs Wilcoxon at p=0.003",
         "Whitehead (1983) unified theory: Fisher Information → Score Statistics → minimum sample n. "
         "Monte Carlo validation of theoretical vs empirical Type I error rates.",
         ["R", "MLE", "Score Test", "Monte Carlo", "R Markdown"],
         "github.com/gonzalo-cruz/Whitehead-sample-size-IE"),

        ("09", "Time Series / Forecasting", "Time Series Analysis with SARIMA",
         "Kaggle competition · awarded",
         "Box-Jenkins methodology on four structurally different series. "
         "ADF/KPSS stationarity, ACF/PACF order selection, AIC/BIC grid search, residual diagnostics.",
         ["Python", "SARIMA", "statsmodels", "pandas", "Kaggle"],
         "github.com/gonzalo-cruz/time-series-analysis"),
    ]

    for num, cat, title, callout, desc, tags, url in projects:
        t = Text()
        t.append(f"\n  {num}  ", style=f"bold {P}")
        t.append(f"{cat}\n", style=f"dim {M}")
        t.append(f"  {title}", style=f"bold {W}")
        if callout:
            t.append(f"  [{callout}]", style=P)
        t.append(f"\n  {desc}\n", style=f"dim {W}")
        t.append("  ")
        for tag in tags:
            t.append(f" {tag} ", style=f"reverse dim")
            t.append(" ")
        t.append(f"\n  ↗  {url}\n", style=f"dim {P}")
        parts.append(t)
        parts.append(Rule(style=BR))

    return Group(*parts)


def render_now():
    cells = [
        ("BUILDING",
         "A quantitative study of whether Chinese, Spanish, and English online communities "
         "express systematically different sentiment toward global tech products — with an explicit "
         "methodology to separate genuine cultural difference from model bias. Fine-tuning XLM-RoBERTa "
         "on 200k+ multilingual posts; back-translation controls, LLM zero-shot baselines, "
         "per-language calibration."),
        ("STUDYING",
         "PyTorch from scratch — writing the training loop manually before touching the Trainer API. "
         "Cross-lingual transfer, temperature scaling calibration, SentencePiece tokenization of Chinese "
         "and how it interacts with sentiment predictions."),
        ("LEARNING",
         "Chinese — working towards HSK4. The NLP project and the language study are feeding "
         "each other in ways that feel productive."),
        ("SEEKING",
         "Internship or junior role in data engineering or ML systems. "
         "Based in Madrid, open to remote. Available immediately."),
    ]

    parts = [sh("06", "Now")]
    for label, text in cells:
        t = Text()
        t.append(f"\n  {label}\n", style=f"bold {P}")
        t.append(f"  {text}\n", style=f"dim {W}")
        parts.append(t)

    parts.append(Text(f"\n  — Updated May 2026\n", style=f"dim {M}"))
    return Group(*parts)


def render_contact():
    t = Text()
    t.append(f"\n  LET'S\n", style=f"bold {W}")
    t.append(f"  TALK.\n\n", style=f"bold {P}")
    t.append(
        "  Looking for internships, junior roles, or just interesting conversations\n"
        "  about data engineering and ML systems. Based in Madrid, open to remote.\n\n",
        style=f"dim {W}",
    )

    tbl = Table(box=None, show_header=False, padding=(0, 2), expand=False)
    tbl.add_column(style=f"dim {M}", width=12, no_wrap=True)
    tbl.add_column(style=W)
    tbl.add_row("Email",     "gonza.c.gomez03@gmail.com")
    tbl.add_row("GitHub",    "github.com/gonzalo-cruz")
    tbl.add_row("LinkedIn",  "linkedin.com/in/gonzalo-cruz-gomez-788516235")
    tbl.add_row("Portfolio", "gonzalo-cruz.github.io/portfolio/")

    return Group(sh("07", "Contact"), Padding(t, (1, 0)), Padding(tbl, (0, 0, 2, 0)))


RENDERERS = {
    "About":      render_about,
    "Education":  render_education,
    "Experience": render_experience,
    "Stack":      render_stack,
    "Projects":   render_projects,
    "Now":        render_now,
    "Contact":    render_contact,
}


# ── WIDGETS ────────────────────────────────────────────────────────────────

class HeroPanel(Static):
    """Left-panel hero: status, name, specs."""

    def render(self):
        status = Text()
        status.append("GCG_001", style=f"dim {M}")
        status.append("    ", style="")
        status.append("● OPEN TO WORK", style=P)

        name = Text()
        name.append("\nGONZALO\n", style=f"bold {W}")
        name.append("CRUZ.", style=f"bold {P}")
        name.append("█\n", style=f"{P} blink")

        tbl = Table(
            box=rbox.SIMPLE,
            show_header=False,
            padding=(0, 0),
            border_style=BR,
            expand=True,
        )
        tbl.add_column(style=f"dim {M}", no_wrap=True)
        tbl.add_column(style=W, no_wrap=True)
        tbl.add_row("Location", "Madrid, ES")
        tbl.add_row("Seeking",  "Internship")
        tbl.add_row("Degree",   "DS&E · URJC")
        tbl.add_row("Avail.",   "Immediate")

        return Group(status, name, tbl)


# ── APP ────────────────────────────────────────────────────────────────────

class Portfolio(App):
    """Gonzalo Cruz — interactive portfolio CLI."""

    TITLE = "Gonzalo Cruz"
    SUB_TITLE = "Data Science & Engineering"

    CSS = """
    Screen {
        layout: horizontal;
        background: #0D0D0D;
    }

    #sidebar {
        width: 26;
        height: 100%;
        background: #141414;
        border-right: solid #2A2A2A;
        padding: 1 1;
    }

    HeroPanel {
        height: auto;
    }

    #nav {
        height: auto;
        background: #141414;
        border: none;
        margin-top: 1;
    }

    #nav > ListItem {
        background: #141414;
        color: #666666;
        padding: 0 1;
    }

    #nav > ListItem.--highlight {
        background: #7C3AED;
        color: #EAEAEA;
    }

    #nav > ListItem:hover {
        background: #222222;
        color: #EAEAEA;
    }

    #main {
        width: 1fr;
        height: 100%;
        background: #0D0D0D;
        padding: 1 3;
    }

    #content {
        height: auto;
    }

    Footer {
        background: #141414;
        border-top: solid #2A2A2A;
        color: #555555;
        height: 1;
    }
    """

    BINDINGS = [
        Binding("1", "jump(0)", "About",      show=True),
        Binding("2", "jump(1)", "Education",  show=True),
        Binding("3", "jump(2)", "Experience", show=True),
        Binding("4", "jump(3)", "Stack",      show=True),
        Binding("5", "jump(4)", "Projects",   show=True),
        Binding("6", "jump(5)", "Now",        show=True),
        Binding("7", "jump(6)", "Contact",    show=True),
        Binding("q", "quit",    "Quit",       show=True),
    ]

    def compose(self) -> ComposeResult:
        with Vertical(id="sidebar"):
            yield HeroPanel()
            yield Static(Rule(style=BR))
            yield ListView(
                *[
                    ListItem(Label(f"  {n}  {name}"), id=f"nav-{i}")
                    for i, (n, name) in enumerate(NAV)
                ],
                id="nav",
            )
        with ScrollableContainer(id="main"):
            yield Static(id="content")
        yield Footer()

    def on_mount(self) -> None:
        self._show(0)

    def _show(self, idx: int) -> None:
        self.query_one("#content", Static).update(RENDERERS[SECTIONS[idx]]())
        self.query_one("#nav", ListView).index = idx
        self.query_one("#main", ScrollableContainer).scroll_home(animate=False)

    def action_jump(self, idx: int) -> None:
        self._show(idx)

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        idx = int(event.item.id.split("-")[1])
        self._show(idx)


if __name__ == "__main__":
    Portfolio().run()
