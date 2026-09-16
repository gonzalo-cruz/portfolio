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
uvx ruff check portfolio_cli.py
```

## Layout

- `index.html` — the whole site
- `css/styles.css`, `js/main.js` — styles and behaviour
- `portfolio_cli.py` — Textual TUI version
- `CV.tex` / `CV_print.tex` — LaTeX sources
- `CV.pdf` / `CV_print.pdf` — published CVs (tracked on purpose)

## Rules

- Match the voice in `~/.agents/AGENTS.md`.
- Keep `index.html` accessible and responsive; no new frameworks unless asked.
- Never commit LaTeX build artifacts (`*.aux`, `*.log`, `*.out`) — they are gitignored.
- Frontend work: read the `frontend-design-taste` skill first.
