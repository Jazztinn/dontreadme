---
name: hackathon-readme
description: >-
  Create a polished, judge-ready README.md for a hackathon project, in a rich
  "submission" style (centered tech badges, demo badge-buttons, team table,
  grounded How-it-works steps, tech-stack table, project tree, and an explicit
  Judging Highlights section that maps the project to the rubric). Use this
  whenever someone is wrapping up a hackathon, demo-day, techsprint, or weekend
  build and needs a README — phrases like "write a readme for my hackathon
  project", "our submission needs a readme", "make our repo look good for the
  judges", "we're submitting in an hour and have no readme", or just "readme for
  this project" on a fresh competition repo. The skill scans the actual codebase
  to ground every command and file reference in reality, interviews the builder
  for the story only they know (problem, demo link, team), and maps the README's
  sections to the specific judging criteria of THAT event so each criterion is
  visibly addressed. Prefer this skill over writing a README freehand whenever
  the context is a competition or time-boxed build, even if the user doesn't say
  the word "hackathon."
---

# Hackathon README Builder

A hackathon README has one job a normal project README doesn't: it has to win.
Judges skim dozens of repos in minutes, often on a phone, deciding what's even
worth opening. The README is the project's first impression and often the only
artifact a judge reads before scoring. So the goal isn't "document the code" —
it's to make a busy, skeptical judge understand and believe in the project fast,
and make every claim trivially verifiable.

This skill produces a **rich submission-style README**, not a sparse one. The
reference look-and-feel lives in `references/readme-template.md` — read it before
writing, because it encodes the house style (centered badge rows, demo
badge-buttons, tables, grounded steps, a project tree, an explicit Judging
Highlights block). `references/badges.md` has copy-paste shields.io snippets.

Work the steps below in order, but stay conversational — you're helping a tired
builder cross the finish line, not filling out a form.

## Step 1 — Anchor on the judging criteria (do this first)

This is the highest-leverage thing you can do, and it's why this skill exists.
Most READMEs are written to a generic template; a winning one is written to the
rubric. Before anything else, ask:

> "Do you have the event's judging criteria or rubric handy? (e.g. 'innovation,
> technical difficulty, impact, polish', or a scoring sheet / submission-page
> prompt.) Paste it in if so — I'll make sure each one is visibly addressed. If
> not, I'll use a strong default."

Why ask first: if the rubric weights "real-world impact," lead with a vivid
problem and who it helps; if it weights "technical difficulty," put the
architecture and the hard parts up front. You'll later add a **Judging
Highlights** section near the end that names each criterion and points to how the
project meets it — this is the rubric-anchoring made visible, and judges love it
because it does their job for them. Keep a checklist: every criterion needs a
home in the README.

If they don't have a rubric, default to the four criteria nearly every event
uses some version of: **innovation/originality, technical execution,
impact/usefulness, and polish/completeness.**

Also gauge the **event's flavor**, because it changes which optional sections
belong (see Step 4):
- Academic / research / techsprint (e.g. ACM events): often rewards an AI-use
  disclosure, an ethics/data-protection note, references/citations, and
  sometimes UN SDG alignment. Include these.
- Product / startup / general weekend hack: keep it lean — skip SDGs, ethics,
  and citations unless the project genuinely involves data collection or claims
  that need backing.

When unsure, ask, or include the lighter set and mention the others are
available.

## Step 2 — Scan the repo to ground yourself in facts

Judges lose trust instantly when a README describes a project that doesn't match
the code, or when setup steps don't work. So before writing, look at what's
actually there. The house style references real file paths and shows real
commands with expected output — you can only do that by reading the repo.

- **Stack & language**: infer from manifests — `package.json`,
  `requirements.txt`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `pom.xml`,
  `Gemfile`. Note frameworks (React, Next, Vite, FastAPI, Flask, Three.js…).
  These map directly to the badge row and the tech-stack table.
- **How to run it**: read `scripts` in `package.json`, a `Makefile`,
  `docker-compose.yml`, `Procfile`, `.env.example`. The run section must match
  how the project *actually* starts, including env vars and the real dev port.
  Where you can infer expected output, show it — it signals the thing works.
- **Structure & entry points**: skim top-level dirs and the main entry file so
  the project tree and the How-it-works steps cite real files
  (`src/lib/check.js`, `app/main.py`), the way the examples do.
- **What already exists**: a partial README, LICENSE, screenshots in
  `assets/`/`docs/`/`public/`, a deployed URL in config, CI workflows. Reuse it.

If you don't have repo access (the user only describes the project), skip the
scan, lean on the interview, and say so — flag that setup commands and file
paths are placeholders to verify, rather than inventing exact ones.

## Step 3 — Interview for what code can't tell you

The repo gives facts; the builder gives the story and the proof. Ask for these
in one friendly batch, and make clear they can skip anything:

- **One-line pitch** → becomes the tagline blockquote.
- **Problem / inspiration** → concrete, human, ideally a specific moment.
- **Live demo + video** → the single most-clicked asset. Surface both near the
  top as badge-buttons. If there's no video, gently note a 2-min one helps a lot.
- **Screenshots / GIF / mascot or logo** → even one image lifts perceived polish;
  the examples center a mascot/preview image up top.
- **The hard part** → what was technically tricky or what they're proud of; gold
  for technical-execution scoring and for "How it works."
- **Headline results / metrics** → if the project measured anything, a small
  results table is very persuasive.
- **Team** → names + roles (and links) for the team table.
- **What's next** → roadmap/scaling shows vision.
- **Event extras** (only if relevant per Step 1) → AI tools used, data/consent
  details, citations.

Don't block on answers. If they're out of time, draft with clearly-marked
placeholders like `<!-- TODO: add demo link -->` so nothing important is
silently dropped — never fabricate a demo URL, a metric, or a teammate.

## Step 4 — Write the README

Produce a single `README.md` at the project root (or where the user wants),
following `references/readme-template.md`. The full ordered skeleton is in that
file; here's the shape and which parts are core vs. optional.

**Core (almost always include):**
1. Title + optional centered logo/mascot image
2. Centered tech badge row (from `references/badges.md`)
3. Event/submission line + tagline blockquote
4. Demo + video as badge-buttons (and dataset/Colab links if they exist)
5. Team table
6. Problem (or "Why this matters")
7. Solution / What it does
8. How it works — numbered steps citing real files
9. Tech stack table
10. Run locally — verified commands, with expected output where possible
11. Project structure tree
12. Roadmap / What's next
13. **Judging Highlights** — one bullet per criterion, mapping the project to it
14. License

**Optional (include based on event flavor and what's real):**
- A nav bar of anchor links under the hero (3–6 key sections) — turns a long
  scroll into one tap for a judge skimming on a phone.
- Headline results / metrics table + error/analysis tables (data projects); link
  the raw data or a reproduction command so the numbers are re-runnable.
- A **before/after** 50/50 table when the project improves on a status quo
  (faster, cheaper, fewer steps) — it makes the win visual instead of claimed.
- An ASCII **stat box** under the hero for a project with one killer number.
- `> [!IMPORTANT]` / `> [!NOTE]` GitHub alert callouts to spotlight the one
  caveat or key fact a skimming judge must not miss (use sparingly).
- Mermaid pipeline diagram (multi-stage systems)
- Demo flow / "what works offline" style walkthrough
- AI-use disclosure (academic events)
- Data protection / privacy / ethics (projects involving people or data)
- UN SDG alignment (impact-oriented academic events)
- References & citations, acknowledgments
- Current status checklist + pre-judging polish todos

Adapt emphasis and ordering to the Step-1 rubric: the criteria that matter most
should appear highest. Don't pad — every section should earn its place. A lean
product hack might use only the core set; a research techsprint might use most of
the optional set. Match the project, not a checklist.

Style notes that matter for judging:
- **Lead with the strongest thing** — innovation, engineering, or impact,
  whichever is the hook.
- **Show, don't tell** — a demo badge-button, a GIF, a one-command setup, and an
  expected-output block beat adjectives. Every impressive claim should be
  verifiable. A before/after table, a stat box, or a reproducible benchmark turns
  a claim into proof the judge can see or re-run.
- **Make the hero do work** — centered title, optional logo/mascot, badge row,
  and one sharp tagline should let a judge grasp what this is and why it's good
  before scrolling. Put the demo/video buttons here, where the first click lands.
- **Ground everything in the repo** — real file paths, real commands, the real
  dev port. This is what makes the README trustworthy and is the through-line of
  the example style.
- **Be honest** — don't claim features that don't exist; judges test things, and
  a broken claim costs more than a missing feature. Mark unfinished work under
  "what's next" or a status checklist, not as done.
- **Keep it skimmable** — short paragraphs, meaningful headers, tables over
  walls of prose, readable top-to-bottom on a phone in two minutes.

## Step 5 — Close the loop against the rubric

Before handing over, take each criterion from Step 1 and confirm the Judging
Highlights section (and the body) addresses it; if any criterion lacks a home,
add it. Then tell the user what you did — e.g. "Your rubric weighted impact and
technical difficulty; I led with the problem for impact and added a 'why this was
hard' note under How it works, and the Judging Highlights block names all four."
Finally, list any remaining placeholders (demo link, screenshots, metrics) so
they know exactly what to fill in before submitting.
