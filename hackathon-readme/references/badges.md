# Badge snippets (shields.io)

Copy-paste these into the centered `<p align="center"> ... </p>` block at the top
of the README. Only include badges for tech the project *actually* uses — the
repo scan tells you which. The house style uses `style=for-the-badge` for the
main tech row and the demo buttons; `style=flat-square` is fine for a secondary
row of smaller/supporting tech.

General form:
`https://img.shields.io/badge/<LABEL>-<HEXCOLOR>?style=for-the-badge&logo=<SIMPLEICON>&logoColor=white`

- `<LABEL>`: text on the badge; URL-encode spaces as `%20`, e.g. `Google%20Colab`.
- `<HEXCOLOR>`: brand color without `#`.
- `<SIMPLEICON>`: a simpleicons.org slug (e.g. `python`, `react`, `nextdotjs`).
  Omit `&logo=...` if there's no good icon. Use `logoColor=black` on light badges.

## Common tech

```markdown
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white"/>
<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
<img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white"/>
<img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white"/>
<img src="https://img.shields.io/badge/Tailwind-38BDF8?style=for-the-badge&logo=tailwindcss&logoColor=white"/>
<img src="https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=threedotjs&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white"/>
<img src="https://img.shields.io/badge/Supabase-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white"/>
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white"/>
<img src="https://img.shields.io/badge/Gemini-8E75FF?style=for-the-badge&logo=googlegemini&logoColor=white"/>
<img src="https://img.shields.io/badge/🤗%20Hugging%20Face-FFD21E?style=for-the-badge&logoColor=black"/>
<img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=black"/>
```

## Demo / action buttons (link-wrapped)

```markdown
<p align="center">
  <a href="<demo-url>">
    <img src="https://img.shields.io/badge/Live%20Demo-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Live Demo"/>
  </a>
</p>
<p align="center">
  <a href="<colab-url>">
    <img src="https://img.shields.io/badge/Run%20in%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Run in Colab"/>
  </a>
</p>
<p align="center">
  <a href="<hf-dataset-url>">
    <img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Dataset-blue?style=for-the-badge" alt="Dataset"/>
  </a>
</p>
```

## Custom / team / status badges

```markdown
<img src="https://img.shields.io/badge/Team-<Name>-F7D26A?style=for-the-badge&labelColor=1C1410" />
<img src="https://img.shields.io/badge/Offline--First-PWA-8FD9B6?style=for-the-badge&labelColor=1C1410" />
```
(`--` renders as a literal hyphen; `labelColor` tints the left half.)

## CI status badge (if the repo has GitHub Actions)

```markdown
[![<workflow>](https://github.com/<user>/<repo>/actions/workflows/<file>.yml/badge.svg)](https://github.com/<user>/<repo>/actions/workflows/<file>.yml)
```
