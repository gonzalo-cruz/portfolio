# Portfolio — Gonzalo Cruz Gómez

Personal portfolio site and CV for Gonzalo Cruz Gómez, Data Science & Engineering student at URJC.

Live at: **https://gonzalo-cruz.github.io/portfolio/**

## Contents

- `index.html` — single-file portfolio site (vanilla HTML/CSS/JS)
- `cv/` — interactive CV with an index, expandable detail per entry, and a print stylesheet
- `CV.pdf` — up-to-date curriculum vitae (one page, the submission artifact)
- `CV.md` — machine-readable CV for agents
- `cv/cv.json` — the same CV in JSON Resume format
- `llms.txt` — stable pointers so agents fetch the Markdown instead of scraping HTML
- `cv.toml` — the canonical CV source; `build_cv.py` renders the Markdown, JSON and HTML views from it

## CV

One source, four views. Edit `cv.toml`, then:

```bash
python3 build_cv.py     # or: uv run --python 3.11 --no-project python build_cv.py
```

The LaTeX CV is hand-tuned and stays that way. To recompile the PDF:

```bash
pdflatex CV.tex
```
