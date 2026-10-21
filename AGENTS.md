# AGENTS.md — portfolio

Personal portfolio site (static HTML/CSS/JS) plus an interactive terminal
version (`portfolio_cli.py`, Textual). Published from `main`.

## Build & run

```bash
# Serve the site locally
python3 -m http.server 8000        # http://localhost:8000

# Terminal portfolio
uvx --with textual python portfolio_cli.py
```

There is no build step — `index.html` is served as-is and loads `css/styles.css`
and `js/main.js` directly.

## Checks

```bash
pre-commit run --all-files         # whitespace, YAML, large files, ruff
uvx ruff check portfolio_cli.py build_cv.py
python3 build_cv.py --check        # CV outputs match cv.toml
```

## Layout

- `index.html` — the whole site
- `css/styles.css`, `js/main.js` — styles and behaviour
- `portfolio_cli.py` — Textual TUI version
- `cv.toml` — **canonical CV source**. Edit this, not the outputs.
- `build_cv.py` — renders `CV.md`, `cv/cv.json`, `cv/index.html` from `cv.toml`
- `llms.txt` — stable pointers for agents
- `CV.tex` / `CV_print.tex` — LaTeX sources
- `CV.pdf` / `CV_print.pdf` — published CVs (tracked on purpose)

## The CV pipeline

One source, four views. `cv.toml` is canonical; three of the views are generated
so they can never drift. The PDF is not generated — it is a hand-tuned design
artifact, updated by hand when content changes materially.

```bash
python3 build_cv.py            # regenerate CV.md, cv/cv.json, cv/index.html
python3 build_cv.py --check    # CI: fail if the outputs are stale
```

Needs Python 3.11+ (`tomllib`). On older interpreters the script re-executes
itself through `uv` if it is installed.

```bash
uv run --python 3.11 --no-project python build_cv.py
```

Layout convention in `cv.toml`: `start`/`end` are `YYYY-MM` (empty end =
present), `tracks` are `de | ml | ai` and drive the role lens on the HTML page,
`tier` is `primary` (own accordion) or `compact` (one line).

## Rules

- Match the voice in `~/.agents/AGENTS.md`.
- Keep `index.html` accessible and responsive; no new frameworks unless asked.
- Never commit LaTeX build artifacts (`*.aux`, `*.log`, `*.out`) — they are gitignored.
- Frontend work: read the `frontend-design-taste` skill first.
