<p align="center">
  <img src="https://em-content.zobj.net/source/apple/391/trophy_1f3c6.png" width="120" />
</p>

<h1 align="center">dontreadme</h1>

<p align="center">
  <strong>the readme judges actually read</strong>
</p>

<p align="center">
  <a href="#beforeafter">Before/After</a> •
  <a href="#install">Install</a> •
  <a href="#what-it-does">What It Does</a> •
  <a href="#how-it-works">How It Works</a> •
  <a href="./hackathon-readme/SKILL.md">Skill spec</a>
</p>

---

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) / Codex **skill** that writes a polished, judge-ready `README.md` for a hackathon project in minutes. It scans your actual repo so every command and file path is real, interviews you for the story only you know, and maps the README straight to the **event's judging rubric** so each criterion is visibly addressed.

Most READMEs document code. A winning one is written to the rubric. This writes to the rubric.

## Before / After

<table>
<tr>
<td width="50%">

### 🗒️ Freehand README

> "# MyProject
> A hackathon project.
>
> ## Setup
> npm install
> npm start"

Judge skims, learns nothing, closes tab.

</td>
<td width="50%">

### 🏆 dontreadme

> Centered hero + tech badges → demo & video buttons → team table → the problem → how it works (citing **real files**) → verified run commands → **Judging Highlights** mapping every rubric criterion.

Judge understands, believes, scores high.

</td>
</tr>
</table>

```
┌─────────────────────────────────────────┐
│  RUBRIC CRITERIA ADDRESSED  ████████ ALL │
│  COMMANDS GROUNDED IN REPO  ████████ 100%│
│  TIME TO JUDGE-READY        ████████ ~min│
│  INVENTED DEMO LINKS        ░░░░░░░░ 0   │
└─────────────────────────────────────────┘
```

> [!IMPORTANT]
> The skill never fabricates a demo URL, a metric, or a teammate. Missing facts
> become clearly-marked `<!-- TODO -->` placeholders — a judge tests things, and
> a broken claim costs more than a missing one.

## Install

Drop the skill folder where your agent looks for skills.

```bash
# Claude Code (user-level)
git clone https://github.com/Jazztinn/dontreadme.git
cp -r dontreadme/hackathon-readme ~/.claude/skills/
```

**Trigger:** say *"write a readme for my hackathon project"*, *"make our repo look good for the judges"*, or *"we submit in an hour and have no readme"* — on any competition or time-boxed build, even without the word "hackathon."

## What It Does

| Step | What |
|---|---|
| **Anchor on the rubric** | Asks for the event's judging criteria first. Orders the README so the highest-weighted criteria sit highest. Falls back to a strong default (innovation, execution, impact, polish) if none given. |
| **Scan the repo** | Infers stack from manifests, run commands from `package.json` / `Makefile` / `.env.example`, structure from entry files — so every command and path is real. |
| **Interview** | One friendly batch for what code can't tell: pitch, problem, demo + video, the hard part, metrics, team, what's next. Skippable. |
| **Write** | Rich submission-style README: centered badges, demo badge-buttons, team table, grounded How-it-works, tech-stack table, project tree, **Judging Highlights**. |
| **Close the loop** | Confirms every rubric criterion has a home, then lists remaining placeholders to fill before submitting. |

## How It Works

1. **Rubric first** — `SKILL.md` Step 1 makes the agent ask for criteria and keep a checklist; every criterion must end up with a home in the README.
2. **Ground in facts** — Step 2 reads manifests and scripts so setup steps actually run and file references actually exist (`hackathon-readme/SKILL.md`).
3. **Interview for the story** — Step 3 batches the human-only questions (problem, demo, the hard part).
4. **House style** — output follows `references/readme-template.md` (hero, nav bar, badge rows, before/after, stat box, alert callouts) with copy-paste shields.io snippets in `references/badges.md`.
5. **Judging Highlights** — a section near the end names each criterion and points to how the project meets it — doing the judge's job for them.

## Project Structure

```text
dontreadme/
├── hackathon-readme/
│   ├── SKILL.md                    # the skill: 5-step workflow
│   ├── references/
│   │   ├── readme-template.md      # house-style skeleton (menu, not form)
│   │   └── badges.md               # copy-paste shields.io snippets
│   └── evals/
│       ├── evals.json              # 3 eval prompts
│       └── fixtures/               # sample hackathon repos (Next.js, FastAPI)
└── README.md                       # you here
```

## License

MIT.
