#!/usr/bin/env python3
"""Render the CV from cv.toml into its three output views.

One canonical source (`cv.toml`) feeds three artifacts:

  CV.md          machine-readable Markdown, for LLM agents and diffs
  cv/cv.json     JSON Resume schema (v1.0.0) for structured tooling
  cv/index.html  interactive human view: index, accordions, print CSS

The LaTeX sources (`CV.tex`, `CV_print.tex`) are deliberately *not*
generated — the published PDF is a hand-tuned design artifact. Content
changes have to be applied there by hand; this script exists so the
HTML, Markdown and JSON views can never disagree with each other.

Usage:
    python3 build_cv.py            # write all three outputs
    python3 build_cv.py --check    # exit 1 if outputs are stale (CI)
"""

from __future__ import annotations

import argparse
import json
import logging
import shutil
import sys
from pathlib import Path
from string import Template
from typing import Any


def _load_tomllib() -> Any:
    """Import tomllib, re-executing under a 3.11+ interpreter when needed.

    The canonical CV source is TOML, which only entered the stdlib in 3.11.
    Rather than die with a bare ImportError on an older interpreter, hand the
    script to uv (which can supply 3.11) and let it carry on.
    """
    try:
        import tomllib
    except ModuleNotFoundError:
        uv = shutil.which("uv")
        if uv is None:
            sys.exit(
                "build_cv.py needs Python 3.11+ (tomllib). Install uv, or run it with python3.11."
            )
        print("[build_cv] Python < 3.11 — re-running under 3.11 via uv", file=sys.stderr)
        sys.stdout.flush()
        sys.stderr.flush()
        import os

        os.execv(
            uv,
            [
                uv,
                "run",
                "--python",
                "3.11",
                "--no-project",
                "python",
                __file__,
                *sys.argv[1:],
            ],
        )
        raise  # unreachable: execv only returns if it fails
    return tomllib


tomllib = _load_tomllib()

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "cv.toml"
MARKDOWN_OUT = ROOT / "CV.md"
JSON_OUT = ROOT / "cv" / "cv.json"
HTML_OUT = ROOT / "cv" / "index.html"

SITE_URL = "https://gonzalo-cruz.github.io/portfolio"
PDF_URL = f"{SITE_URL}/CV.pdf"
HTML_URL = f"{SITE_URL}/cv/"
MARKDOWN_URL = f"{SITE_URL}/CV.md"
JSON_URL = f"{SITE_URL}/cv/cv.json"

MONTHS = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)

logger = logging.getLogger("build_cv")


# ── helpers ──────────────────────────────────────────────────


def load_source(path: Path = SOURCE) -> dict[str, Any]:
    """Parse the canonical TOML source."""
    with path.open("rb") as handle:
        return tomllib.load(handle)


def fmt_date(value: str) -> str:
    """Turn '2026-09' into 'Sep 2026'. Empty input stays empty."""
    if not value:
        return ""
    year, _, month = value.partition("-")
    if not month:
        return year
    return f"{MONTHS[int(month) - 1]} {year}"


def fmt_range(start: str, end: str) -> str:
    """Human-readable date range; an empty end means 'present'."""
    return f"{fmt_date(start)} – {fmt_date(end) or 'present'}"


def texts(items: list[Any] | None) -> list[str]:
    """Allow both `["line"]` and `[{text = "line"}]` for highlight lists."""
    if not items:
        return []
    out: list[str] = []
    for item in items:
        out.append(item["text"] if isinstance(item, dict) else str(item))
    return out


def slug(value: str) -> str:
    """Stable anchor id: ASCII-ish, lowercase, hyphenated."""
    keep = [c.lower() if c.isalnum() else "-" for c in value]
    return "-".join(part for part in "".join(keep).split("-") if part)


def esc(value: str) -> str:
    """Escape for HTML text and attribute contexts."""
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def visible(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Primary-tier entries, in source order."""
    return [e for e in entries if e.get("tier") == "primary"]


def compact(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Compact-tier entries, in source order."""
    return [e for e in entries if e.get("tier") == "compact"]


# ── Markdown view ────────────────────────────────────────────


def render_markdown(cv: dict[str, Any]) -> str:
    """Agent-first Markdown: hierarchical headings, one claim per bullet."""
    basics = cv["basics"]
    meta = cv["meta"]
    lines: list[str] = [f"# {basics['name']}", ""]
    lines.append(f"**{basics['label']}** · {basics['city']}, {basics['country']}")
    lines.append("")
    lines.append(f"- Email: {basics['email']}")
    for profile in basics.get("profiles", []):
        lines.append(f"- {profile['network']}: {profile['url']}")
    lines.append(f"- Portfolio: {basics['url']}")
    if basics.get("availability"):
        lines.append(f"- Availability: {basics['availability']}")
    lines += ["", "## Summary", "", basics["summary"]]

    lines += ["", "## Experience"]
    for job in cv.get("work", []):
        lines += ["", f"### {job['position']} — {job['name']}", ""]
        where = f"{fmt_range(job['start'], job['end'])}"
        if job.get("location"):
            where += f" · {job['location']}"
        lines.append(where)
        if job.get("summary"):
            lines += ["", job["summary"]]
        highlights = texts(job.get("highlights"))
        if highlights:
            lines.append("")
            lines += [f"- {line}" for line in highlights]

    lines += ["", "## Projects"]
    for project in cv.get("projects", []):
        lines += ["", f"### {project['name']}", ""]
        header = [project.get("kind", ""), fmt_range(project["start"], project["end"])]
        if project.get("status"):
            header.append(project["status"])
        lines.append(" · ".join(part for part in header if part))
        lines.append("")
        if project.get("url"):
            lines.append(f"<{project['url']}>")
            lines.append("")
        lines.append(project.get("summary", ""))
        highlights = texts(project.get("highlights"))
        if highlights:
            lines.append("")
            lines += [f"- {line}" for line in highlights]
        if project.get("keywords"):
            lines += ["", f"Keywords: {', '.join(project['keywords'])}"]

    lines += ["", "## Education"]
    for school in cv.get("education", []):
        lines += ["", f"### {school['study_type']} {school['area']} — {school['institution']}", ""]
        span = fmt_range(school["start"], school["end"])
        if school.get("status"):
            span += f" · {school['status']}"
        lines.append(span)
        if school.get("summary"):
            lines += ["", school["summary"]]
        if school.get("courses"):
            lines += ["", f"Coursework: {', '.join(school['courses'])}"]

    lines += ["", "## Skills"]
    for skill in cv.get("skills", []):
        lines.append(f"- **{skill['name']}:** {', '.join(skill['keywords'])}")

    if cv.get("languages"):
        lines += ["", "## Languages"]
        lines += [f"- {entry['language']} — {entry['fluency']}" for entry in cv["languages"]]

    lines += ["", "## Certifications"]
    for cert in cv.get("certificates", []):
        lines.append(f"- {cert['name']} — {cert['issuer']}, {fmt_date(cert['date'])}")

    lines += [
        "",
        "---",
        "",
        f"Canonical source: cv.toml · updated {meta['updated']} · v{meta['version']}",
        f"Interactive version: {HTML_URL}",
        f"PDF: {PDF_URL}",
        "",
    ]
    return "\n".join(lines)


# ── JSON view (JSON Resume v1.0.0) ───────────────────────────


def render_json(cv: dict[str, Any]) -> str:
    """JSON Resume document, plus a meta block pointing at the source."""
    basics = cv["basics"]
    payload: dict[str, Any] = {
        "$schema": (
            "https://raw.githubusercontent.com/jsonresume/resume-schema/v1.0.0/schema.json"
        ),
        "basics": {
            "name": basics["name"],
            "label": basics["label"],
            "email": basics["email"],
            "url": basics["url"],
            "summary": basics["summary"],
            "location": {
                "city": basics["city"],
                "country": basics["country"],
                "countryCode": basics["country_code"],
            },
            "profiles": [
                {
                    "network": profile["network"],
                    "username": profile["username"],
                    "url": profile["url"],
                }
                for profile in basics.get("profiles", [])
            ],
        },
        "work": [
            {
                "name": job["name"],
                "position": job["position"],
                "location": job.get("location", ""),
                "url": job.get("url", ""),
                "startDate": job["start"],
                "endDate": job.get("end", ""),
                "summary": job.get("summary", ""),
                "highlights": texts(job.get("highlights")),
            }
            for job in cv.get("work", [])
        ],
        "projects": [
            {
                "name": project["name"],
                "description": project.get("summary", ""),
                "highlights": texts(project.get("highlights")),
                "keywords": project.get("keywords", []),
                "url": project.get("url", ""),
                "startDate": project["start"],
                "endDate": project["end"],
            }
            for project in cv.get("projects", [])
        ],
        "education": [
            {
                "institution": school["institution"],
                "url": school.get("url", ""),
                "area": school["area"],
                "studyType": school["study_type"],
                "startDate": school["start"],
                "endDate": school["end"],
                "courses": school.get("courses", []),
            }
            for school in cv.get("education", [])
        ],
        "skills": [
            {
                "name": skill["name"],
                "level": skill.get("level", ""),
                "keywords": skill["keywords"],
            }
            for skill in cv.get("skills", [])
        ],
        "languages": [
            {"language": entry["language"], "fluency": entry["fluency"]}
            for entry in cv.get("languages", [])
        ],
        "certificates": [
            {"name": cert["name"], "issuer": cert["issuer"], "date": cert["date"]}
            for cert in cv.get("certificates", [])
        ],
        "meta": {
            "canonical": "cv.toml",
            "updated": cv["meta"]["updated"],
            "version": cv["meta"]["version"],
            "availability": basics.get("availability", ""),
            "generatedBy": "build_cv.py",
            "humanReadable": HTML_URL,
            "markdown": MARKDOWN_URL,
            "pdf": PDF_URL,
        },
    }
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


# ── HTML view ────────────────────────────────────────────────

STYLES = """
:root {
  --bg: #f2efe6;
  --bg-surface: #ebe7dc;
  --text: #161616;
  --text-muted: #5a5a55;
  --text-faint: #8c8c84;
  --accent: #002fa7;
  --accent-subtle: #e7ebf7;
  --on-accent: #fff;
  --rule: #c9c4b6;
  --rule-light: #dcd7c9;
  --font-display: "Syne", "DM Sans", sans-serif;
  --font-sans: "DM Sans", system-ui, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", monospace;
  --space-2xs: 0.5rem;
  --space-xs: 0.75rem;
  --space-sm: 1rem;
  --space-md: 1.5rem;
  --space-lg: 2rem;
  --space-xl: 3rem;
  --space-2xl: 4rem;
  --reading: 68ch;
  --duration: 220ms;
  --ease: cubic-bezier(0.16, 1, 0.3, 1);
  color-scheme: light;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0f0e0c;
    --bg-surface: #171512;
    --text: #ece9e0;
    --text-muted: #9a9589;
    --text-faint: #6b665a;
    --accent: #7d94ff;
    --accent-subtle: #161b3a;
    --on-accent: #0f0e0c;
    --rule: #2a2822;
    --rule-light: #23211c;
    color-scheme: dark;
  }
}

* { box-sizing: border-box; }

html { -webkit-text-size-adjust: 100%; }

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: var(--font-sans);
  font-size: 16px;
  line-height: 1.6;
}

a { color: var(--accent); text-decoration-thickness: 1px; text-underline-offset: 3px; }
a:hover { text-decoration-thickness: 2px; }

.page {
  display: grid;
  grid-template-columns: 13rem minmax(0, 1fr);
  gap: var(--space-2xl);
  max-width: 74rem;
  margin: 0 auto;
  padding: var(--space-xl) var(--space-lg) var(--space-2xl);
}

/* ── index rail ── */
.index {
  position: sticky;
  top: var(--space-md);
  align-self: start;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  line-height: 1.9;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
.index-title {
  margin: 0 0 var(--space-sm);
  color: var(--text-faint);
  font-weight: 500;
  line-height: 1;
}
.index ol { margin: 0; padding: 0; list-style: none; }
.index a {
  display: grid;
  grid-template-columns: 1.75rem 1fr;
  color: var(--text-muted);
  text-decoration: none;
  border-top: 1px solid var(--rule-light);
  padding: 0.35rem 0;
}
.index a:hover { color: var(--text); }
.index a.is-active { color: var(--accent); }
.index .num { color: var(--text-faint); }
.index a.is-active .num { color: var(--accent); }

/* ── masthead ── */
header {
  border-top: 2px solid var(--text);
  padding-top: var(--space-sm);
}
h1 {
  margin: var(--space-2xs) 0 0;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: clamp(2.4rem, 7vw, 4.4rem);
  line-height: 0.95;
  letter-spacing: -0.03em;
}
h1 .surname { display: block; color: var(--accent); }
.lede {
  margin: var(--space-md) 0 0;
  max-width: var(--reading);
  font-size: 1.08rem;
  color: var(--text-muted);
}
.contact {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem 1.25rem;
  margin: var(--space-md) 0 0;
  padding: 0;
  list-style: none;
  font-family: var(--font-mono);
  font-size: 0.78rem;
}
.actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: var(--space-md);
}
.btn {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: var(--text);
  background: transparent;
  border: 1px solid var(--rule);
  padding: 0.5rem 0.8rem;
  cursor: pointer;
  text-decoration: none;
  transition: border-color var(--duration) var(--ease),
              background var(--duration) var(--ease);
}
.btn:hover { border-color: var(--accent); color: var(--accent); }
.btn-primary { background: var(--accent); border-color: var(--accent); color: var(--on-accent); }
.btn-primary:hover { background: var(--accent); color: var(--on-accent); opacity: 0.88; }

/* ── sections ── */
section { margin-top: var(--space-2xl); }
.section-head {
  display: grid;
  grid-template-columns: 3.5rem minmax(0, 1fr);
  align-items: baseline;
  border-top: 2px solid var(--text);
  padding-top: 0.6rem;
  margin-bottom: var(--space-md);
}
.section-num {
  font-family: var(--font-mono);
  font-size: 1.6rem;
  font-weight: 500;
  color: var(--accent);
  line-height: 1;
}
h2 {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.3rem, 2.5vw, 1.7rem);
  font-weight: 700;
  letter-spacing: -0.01em;
  text-transform: uppercase;
}
.section-note {
  grid-column: 2;
  margin: 0.25rem 0 0;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--text-faint);
}
.prose { max-width: var(--reading); }
.prose p { margin: 0 0 var(--space-sm); }

/* ── lens ── */
.lens {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.4rem;
  margin-bottom: var(--space-md);
  font-family: var(--font-mono);
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
.lens-label { color: var(--text-faint); margin-right: 0.25rem; }
.lens button {
  font: inherit;
  color: var(--text-muted);
  background: transparent;
  border: 1px solid var(--rule);
  padding: 0.3rem 0.6rem;
  cursor: pointer;
  transition: color var(--duration) var(--ease),
              border-color var(--duration) var(--ease);
}
.lens button:hover { color: var(--text); border-color: var(--text-muted); }
.lens button[aria-pressed="true"] {
  color: var(--on-accent);
  background: var(--accent);
  border-color: var(--accent);
}
.lens-count { color: var(--text-faint); margin-left: 0.25rem; }

/* ── accordions ── */
details.entry {
  border-top: 1px solid var(--rule);
  transition: opacity var(--duration) var(--ease);
}
details.entry:last-of-type { border-bottom: 1px solid var(--rule); }
details.entry[hidden] { display: none; }
details.entry.dimmed { opacity: 0.4; }
summary {
  display: grid;
  grid-template-columns: 1.2rem minmax(0, 1fr) auto;
  gap: 0 var(--space-sm);
  align-items: baseline;
  padding: 0.9rem 0;
  cursor: pointer;
  list-style: none;
}
summary::-webkit-details-marker { display: none; }
summary::before {
  content: "+";
  font-family: var(--font-mono);
  font-size: 0.9rem;
  color: var(--accent);
  line-height: 1.4;
}
details[open] > summary::before { content: "–"; }
summary:hover .entry-title { color: var(--accent); }
.entry-head { grid-column: 2; }
.entry-title {
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 700;
  letter-spacing: -0.01em;
  transition: color var(--duration) var(--ease);
}
.entry-org { color: var(--text-muted); font-size: 0.92rem; }
.entry-date {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--text-faint);
  white-space: nowrap;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.entry-meta {
  grid-column: 2 / -1;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--text-faint);
  margin-top: 0.15rem;
}
.entry-hook {
  grid-column: 2 / -1;
  margin: 0.35rem 0 0;
  font-size: 0.92rem;
  color: var(--text-muted);
  max-width: var(--reading);
}
.entry-body {
  padding: 0 0 var(--space-md) 1.2rem;
  max-width: var(--reading);
}
.entry-body ul { margin: 0; padding-left: 1.1rem; }
.entry-body li { margin-bottom: 0.5rem; font-size: 0.94rem; }
.entry-body li::marker { color: var(--accent); }
.status {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--accent);
  background: var(--accent-subtle);
  padding: 0.1rem 0.4rem;
  margin-left: 0.4rem;
  vertical-align: 0.15em;
}
.keywords {
  margin: var(--space-sm) 0 0;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--text-faint);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.also {
  margin: var(--space-md) 0 0;
  padding: 0;
  list-style: none;
  font-size: 0.9rem;
}
.also li {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: var(--space-sm);
  border-top: 1px solid var(--rule-light);
  padding: 0.5rem 0;
  color: var(--text-muted);
}
.also .also-name { color: var(--text); font-weight: 600; }
.also .also-date {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--text-faint);
  white-space: nowrap;
}

/* ── skills ── */
.skill-row {
  display: grid;
  grid-template-columns: 11rem minmax(0, 1fr);
  gap: var(--space-sm);
  border-top: 1px solid var(--rule-light);
  padding: 0.6rem 0;
}
.skill-name {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-faint);
  padding-top: 0.15rem;
}
.skill-tags { display: flex; flex-wrap: wrap; gap: 0.35rem 0.5rem; }
.tag {
  font-size: 0.88rem;
  border-bottom: 1px solid var(--rule);
}

/* ── footer ── */
footer {
  margin-top: var(--space-2xl);
  border-top: 2px solid var(--text);
  padding-top: var(--space-sm);
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--text-faint);
  line-height: 1.9;
}
footer a { color: var(--text-muted); }

/* ── narrow screens ── */
@media (max-width: 900px) {
  .page { grid-template-columns: 1fr; gap: var(--space-lg); }
  .index { position: static; }
  .index ol { display: flex; flex-wrap: wrap; gap: 0 1rem; }
  .index a { border-top: 0; }
  .index a.is-active { color: var(--accent); }
  .section-head { grid-template-columns: 2.25rem minmax(0, 1fr); }
  .section-num { font-size: 1.1rem; }
  .skill-row { grid-template-columns: 1fr; gap: 0.25rem; }
}

@media (max-width: 600px) {
  summary { grid-template-columns: 1.2rem minmax(0, 1fr); }
  .entry-date { grid-column: 2; margin-top: 0.1rem; }
  .entry-meta, .entry-hook { grid-column: 2; }
  .entry-head .entry-org { display: block; }
  .also li { grid-template-columns: 1fr; gap: 0.15rem; }
}

@media (prefers-reduced-motion: reduce) {
  * { transition-duration: 1ms !important; animation-duration: 1ms !important; }
}

/* ── print: one page, everything open, no chrome ── */
@page { size: A4; margin: 13mm 14mm; }

@media print {
  :root {
    --bg: #fff;
    --text: #000;
    --text-muted: #222;
    --text-faint: #555;
    --accent: #002fa7;
    --rule: #999;
    --rule-light: #ccc;
  }
  body { font-size: 8.6pt; line-height: 1.36; }
  .page { display: block; max-width: none; padding: 0; }
  .index, .actions, .lens, .lede { display: none !important; }
  header { border-top: 1px solid var(--text); padding-top: 0.3rem; }
  h1 { font-size: 1.9rem; margin-top: 0.2rem; }
  .contact { font-size: 0.68rem; margin-top: 0.4rem; }
  section { margin-top: 0.85rem; }
  .section-head { margin-bottom: 0.35rem; padding-top: 0.3rem; }
  h2 { font-size: 0.95rem; }
  .section-num { font-size: 0.9rem; }
  .section-note { display: none; }
  .prose p { margin-bottom: 0.25rem; }
  summary { padding: 0.22rem 0; }
  .entry-title { font-size: 0.92rem; }
  .entry-org { font-size: 0.78rem; }
  .entry-head .entry-org { display: block; }
  .entry-date, .entry-meta { font-size: 0.6rem; }
  .entry-hook { margin-top: 0.1rem; font-size: 0.8rem; }
  .entry-body { padding-bottom: 0.25rem; }
  .entry-body li { font-size: 0.78rem; margin-bottom: 0.1rem; }
  .keywords { font-size: 0.6rem; margin-top: 0.2rem; }
  .entry-link { display: none !important; }
  details.entry { break-inside: auto; opacity: 1 !important; }
  details.entry[hidden] { display: block !important; }
  details > summary { break-after: avoid; }
  .also { margin-top: 0.4rem; }
  .also li { padding: 0.25rem 0; font-size: 0.78rem; }
  .skill-row { padding: 0.28rem 0; }
  .skill-name { font-size: 0.6rem; }
  .tag { font-size: 0.78rem; }
  footer { display: none; }
  p, li { orphans: 2; widows: 2; }
  .entry-body li { break-inside: avoid; }
  .entry-body p { break-before: avoid; }
  details:not([open]) > *:not(summary) {
    display: block !important;
    content-visibility: visible !important;
  }
  a { color: #000; text-decoration: none; }
  .status { background: none; border: 1px solid var(--rule); color: #000; }
}
"""

SCRIPT = """
(function () {
  "use strict";

  // Open every accordion before printing, so a browser print (Ctrl+P)
  // never depends on whether the reader happened to expand a section.
  function openAll() {
    document.querySelectorAll("details").forEach(function (node) {
      node.open = true;
    });
  }
  window.addEventListener("beforeprint", openAll);

  // Scroll-spy for the index rail.
  var links = Array.prototype.slice.call(
    document.querySelectorAll(".index a[href^='#']")
  );
  var sections = links
    .map(function (link) { return document.getElementById(link.hash.slice(1)); })
    .filter(Boolean);

  if ("IntersectionObserver" in window && sections.length) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          links.forEach(function (link) {
            link.classList.toggle(
              "is-active",
              link.hash.slice(1) === entry.target.id
            );
          });
        });
      },
      { rootMargin: "-15% 0px -70% 0px" }
    );
    sections.forEach(function (section) { observer.observe(section); });
  }

  // Role lens: dim entries that don't carry the selected track. Nothing is
  // removed from the DOM, so scraping, find-in-page and print still see it.
  var lensButtons = Array.prototype.slice.call(
    document.querySelectorAll(".lens button")
  );
  var lensCount = document.getElementById("lensCount");
  var entries = Array.prototype.slice.call(document.querySelectorAll("[data-tracks]"));

  function applyLens(lens) {
    var shown = 0;
    entries.forEach(function (entry) {
      var tracks = entry.getAttribute("data-tracks").split(" ");
      var matches = lens === "all" || tracks.indexOf(lens) !== -1;
      entry.classList.toggle("dimmed", !matches);
      if (matches) shown += 1;
    });
    lensButtons.forEach(function (button) {
      button.setAttribute(
        "aria-pressed",
        String(button.getAttribute("data-lens") === lens)
      );
    });
    if (lensCount) {
      lensCount.textContent =
        lens === "all" ? "" : shown + " / " + entries.length + " entries";
    }
    try {
      sessionStorage.setItem("cv_lens", lens);
    } catch (e) { /* private mode */ }
  }

  lensButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      applyLens(button.getAttribute("data-lens"));
    });
  });

  var saved = null;
  try { saved = sessionStorage.getItem("cv_lens"); } catch (e) { /* ignore */ }
  if (saved) applyLens(saved);
})();
"""


def build_index(cv: dict[str, Any]) -> str:
    """Numbered index entries, one per rendered section."""
    sections = [
        ("profile", "Profile"),
        ("experience", "Experience"),
        ("projects", "Projects"),
        ("education", "Education"),
        ("skills", "Skills"),
    ]
    items = []
    for number, (anchor, title) in enumerate(sections, start=1):
        items.append(
            f'<li><a href="#{anchor}">'
            f'<span class="num">{number:02d}</span><span>{title}</span></a></li>'
        )
    return "\n        ".join(items)


def build_section_head(number: int, title: str, note: str = "") -> str:
    """Section header: oversized mono numeral plus display title."""
    note_html = f'<p class="section-note">{esc(note)}</p>' if note else ""
    return (
        f'<div class="section-head">'
        f'<span class="section-num">{number:02d}</span>'
        f"<h2>{esc(title)}</h2>{note_html}</div>"
    )


def build_lens(cv: dict[str, Any]) -> str:
    """Role lens controls."""
    lens = cv["lens"]
    buttons = "".join(
        f'<button type="button" data-lens="{key}" '
        f'aria-pressed="{"true" if key == "all" else "false"}">'
        f"{esc(lens['labels'][key])}</button>"
        for key in lens["order"]
    )
    return (
        '<div class="lens" role="group" aria-label="Filter by role">'
        '<span class="lens-label">Lens</span>'
        f"{buttons}"
        '<span class="lens-count" id="lensCount"></span>'
        "</div>"
    )


def entry_tracks(tracks: list[str]) -> str:
    """Render the data-tracks attribute, or nothing when there are no tracks.

    Emitting an empty attribute would make the role lens treat the entry as
    matching no lens at all, so it would stay dimmed whatever was selected.
    """
    return f' data-tracks="{" ".join(tracks)}"' if tracks else ""


def build_entry(
    title: str,
    org: str,
    date: str,
    meta: str,
    hook: str,
    body: list[str],
    tracks: list[str],
    status: str = "",
    keywords: list[str] | None = None,
    url: str = "",
    link_label: str = "Repository",
    open_by_default: bool = False,
) -> str:
    """One accordion entry. Closed state must stay skimmable on its own."""
    anchor = slug(f"{title} {org}")
    status_html = f'<span class="status">{esc(status)}</span>' if status else ""
    meta_html = f'<span class="entry-meta">{esc(meta)}</span>' if meta else ""
    hook_html = f'<p class="entry-hook">{esc(hook)}</p>' if hook else ""

    body_parts: list[str] = []
    if body:
        body_parts.append("<ul>" + "".join(f"<li>{esc(line)}</li>" for line in body) + "</ul>")
    if keywords:
        body_parts.append(f'<p class="keywords">{esc(" · ".join(keywords))}</p>')
    if url:
        body_parts.append(
            f'<p class="keywords entry-link"><a href="{esc(url)}" target="_blank" '
            f'rel="noopener">{esc(link_label)} ↗</a></p>'
        )
    body_html = f'<div class="entry-body">{"".join(body_parts)}</div>' if body_parts else ""

    org_html = f' <span class="entry-org">· {esc(org)}</span>' if org else ""
    title_html = f'<span class="entry-title">{esc(title)}{status_html}</span>'
    tracks_attr = entry_tracks(tracks)
    open_attr = " open" if open_by_default else ""

    return (
        f'<details class="entry" id="{anchor}"{tracks_attr}{open_attr}>'
        "<summary>"
        f'<span class="entry-head">{title_html}{org_html}</span>'
        f'<span class="entry-date">{esc(date)}</span>'
        f"{meta_html}{hook_html}"
        "</summary>"
        f"{body_html}"
        "</details>"
    )


def build_json_ld(cv: dict[str, Any]) -> str:
    """schema.org Person, so agents and crawlers get structure for free."""
    basics = cv["basics"]
    person: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": basics["name"],
        "jobTitle": basics["label"],
        "email": f"mailto:{basics['email']}",
        "url": HTML_URL,
        "description": basics["summary"],
        "address": {
            "@type": "PostalAddress",
            "addressLocality": basics["city"],
            "addressCountry": basics["country_code"],
        },
        "alumniOf": [
            {"@type": "CollegeOrUniversity", "name": school["institution"]}
            for school in cv.get("education", [])
        ],
        "worksFor": [
            {"@type": "Organization", "name": job["name"]}
            for job in cv.get("work", [])
            if not job.get("end")
        ],
        "knowsLanguage": [
            {"@type": "Language", "name": entry["language"]} for entry in cv.get("languages", [])
        ],
        "knowsAbout": sorted(
            {keyword for skill in cv.get("skills", []) for keyword in skill["keywords"]}
        ),
        "sameAs": [profile["url"] for profile in basics.get("profiles", [])],
    }
    blob = json.dumps(person, indent=2, ensure_ascii=False)
    return f'<script type="application/ld+json">\n{blob}\n</script>'


def render_html(cv: dict[str, Any]) -> str:
    """The interactive page: index rail, accordions, lens, print styles."""
    basics = cv["basics"]
    first, _, last = basics["name"].partition(" ")
    surname = last or first

    template = Template(
        """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>$title</title>
<meta name="description" content="$description">
<meta name="author" content="$author">
<link rel="canonical" href="$url">
<link rel="alternate" type="text/markdown" href="$markdown_href" title="CV as Markdown">
<link rel="alternate" type="application/json" href="$json_href" title="CV as JSON Resume">
<meta property="og:type" content="profile">
<meta property="og:title" content="$title">
<meta property="og:description" content="$description">
<meta property="og:url" content="$url">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400..800&family=DM+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="icon" type="image/svg+xml" href="../favicon.svg">
<style>$styles</style>
$json_ld
</head>
<body>
<div class="page">

<nav class="index" aria-label="CV sections">
    <p class="index-title">Index</p>
    <ol>
        $index_items
    </ol>
</nav>

<main>

<header>
    <h1>$first<span class="surname">$surname.</span></h1>
    <p class="lede">$tagline</p>
    <ul class="contact">
        <li><a href="mailto:$email">$email</a></li>
        <li><a href="$github">github</a></li>
        <li><a href="$linkedin">linkedin</a></li>
        <li><a href="$pdf_href">pdf</a></li>
    </ul>
    <div class="actions">
        <a class="btn" href="$markdown_href">Plain markdown</a>
        <a class="btn" href="$json_href">JSON Resume</a>
        <a class="btn btn-primary" href="$pdf_href" download="Gonzalo-Cruz-CV.pdf">Download CV.pdf</a>
    </div>
</header>

<section id="profile">
    $profile_head
    <div class="prose">
        <p>$summary</p>
        <p><strong>$availability</strong></p>
    </div>
</section>

<section id="experience">
    $experience_head
    $experience_entries
</section>

<section id="projects">
    $projects_head
    $lens
    $project_entries
    $also
</section>

<section id="education">
    $education_head
    $education_entries
</section>

<section id="skills">
    $skills_head
    $skill_rows
    $cert_rows
</section>

<footer>
    <p>Generated from <code>cv.toml</code> — the Markdown and JSON views are rendered from the
    same file, so they cannot disagree. Academic dates and the LaTeX PDF are hand-maintained.</p>
    <p>
        <a href="$markdown_href">CV.md</a> ·
        <a href="$json_href">cv.json</a> ·
        <a href="$pdf_href">CV.pdf</a> ·
        <a href="../">portfolio</a>
    </p>
</footer>

</main>
</div>
<script>$script</script>
</body>
</html>
"""
    )

    experience = []
    for job in cv.get("work", []):
        experience.append(
            build_entry(
                title=job["position"],
                org=job["name"],
                date=fmt_range(job["start"], job["end"]),
                meta=" · ".join(job.get("tags", [])),
                hook=job.get("hook", ""),
                body=texts(job.get("highlights")),
                tracks=job.get("tracks", []),
                url=job.get("url", ""),
                link_label="Website",
                open_by_default=bool(job.get("open", False)),
            )
        )

    projects = []
    for project in visible(cv.get("projects", [])):
        projects.append(
            build_entry(
                title=project["name"],
                org="",
                date=fmt_range(project["start"], project["end"]),
                meta=project.get("kind", ""),
                hook=project.get("hook", ""),
                body=texts(project.get("highlights")),
                tracks=project.get("tracks", []),
                status=project.get("status", ""),
                keywords=project.get("keywords"),
                url=project.get("url", ""),
            )
        )

    also_items = "".join(
        f"<li{entry_tracks(project.get('tracks', []))}>"
        f'<span><span class="also-name">{esc(project["name"])}</span> — '
        f"{esc(project.get('summary', ''))}</span>"
        f'<span class="also-date">{esc(fmt_range(project["start"], project["end"]))}'
        f"</span></li>"
        for project in compact(cv.get("projects", []))
    )
    also_html = f'<ul class="also">{also_items}</ul>' if also_items else ""

    education = []
    for school in cv.get("education", []):
        education.append(
            build_entry(
                title=f"{school['study_type']} {school['area']}",
                org=school["institution"],
                date=fmt_range(school["start"], school["end"]),
                meta=" · ".join(school.get("courses", [])),
                hook=school.get("summary", ""),
                body=[],
                tracks=[],
                status=school.get("status", ""),
            )
        )

    skill_rows = "".join(
        f'<div class="skill-row"><span class="skill-name">{esc(skill["name"])}</span>'
        f'<span class="skill-tags">'
        + "".join(f'<span class="tag">{esc(word)}</span>' for word in skill["keywords"])
        + "</span></div>"
        for skill in cv.get("skills", [])
    )

    cert_rows = "".join(
        f'<div class="skill-row"><span class="skill-name">Certification</span>'
        f'<span class="skill-tags"><span class="tag">'
        f"{esc(cert['name'])} — {esc(cert['issuer'])}, {esc(fmt_date(cert['date']))}"
        f"</span></span></div>"
        for cert in cv.get("certificates", [])
    )

    github = next(
        (
            profile["url"]
            for profile in basics.get("profiles", [])
            if profile["network"] == "GitHub"
        ),
        "",
    )
    linkedin = next(
        (
            profile["url"]
            for profile in basics.get("profiles", [])
            if profile["network"] == "LinkedIn"
        ),
        "",
    )

    summary = basics["summary"]

    return template.substitute(
        title=f"{basics['name']} — {basics['label']}",
        description=summary[:180].rsplit(" ", 1)[0] + "…",
        author=basics["name"],
        url=HTML_URL,
        markdown_href="../CV.md",
        json_href="cv.json",
        pdf_href="../CV.pdf",
        styles=STYLES,
        json_ld=build_json_ld(cv),
        index_items=build_index(cv),
        first=esc(first),
        surname=esc(surname),
        label=esc(basics["label"]),
        tagline=esc(basics.get("tagline", basics["label"])),
        email=esc(basics["email"]),
        github=esc(github),
        linkedin=esc(linkedin),
        summary=esc(summary),
        availability=esc(basics.get("availability", "")),
        profile_head=build_section_head(1, "Profile"),
        experience_head=build_section_head(2, "Experience", "click a row for detail"),
        experience_entries="".join(experience),
        projects_head=build_section_head(
            3, "Projects", "closed rows carry the claim; open ones carry the evidence"
        ),
        lens=build_lens(cv),
        project_entries="".join(projects),
        also=also_html,
        education_head=build_section_head(4, "Education"),
        education_entries="".join(education),
        skills_head=build_section_head(5, "Technical skills"),
        skill_rows=skill_rows,
        cert_rows=cert_rows,
        script=SCRIPT,
    )


# ── entry point ──────────────────────────────────────────────


def build(check: bool = False) -> int:
    """Render every output; in check mode, compare against what's on disk."""
    cv = load_source()
    outputs = {
        MARKDOWN_OUT: render_markdown(cv),
        JSON_OUT: render_json(cv),
        HTML_OUT: render_html(cv),
    }

    stale: list[Path] = []
    for path, content in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == content:
            logger.info("up to date: %s", path.relative_to(ROOT))
            continue
        stale.append(path)
        if not check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            logger.info("wrote: %s", path.relative_to(ROOT))

    if check and stale:
        for path in stale:
            logger.error("stale: %s — run python3 build_cv.py", path.relative_to(ROOT))
        return 1

    if not stale:
        logger.info("nothing to do")
    return 0


def main(argv: list[str] | None = None) -> int:
    """Parse arguments and run the build."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify the generated files match cv.toml; exit 1 if they don't",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="debug logging")
    args = parser.parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(message)s",
    )
    return build(check=args.check)


if __name__ == "__main__":
    sys.exit(main())
