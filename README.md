# harnessai-core

Shared firm context, skills, and templates for HarnessAI.

## What This Repo Is

This is the HarnessAI "firm brain." Every team member clones this once. Every AI tool (Claude Code, Gemini, etc.) reads from it automatically — brand voice, services, goals, and lessons learned — without any manual setup per session.

## Setup (New Team Member)

1. Install your preferred AI tool (Claude Code or Gemini CLI)
2. Clone this repo:
   ```bash
   git clone https://github.com/Backyardlesiure/harnessai-core.git
   cd harnessai-core
   ```
3. Open your AI tool inside this folder — context loads automatically
4. For client work, clone the relevant `harnessai-client-[name]` repo alongside this one

## What's Here

| Folder | Purpose |
|---|---|
| `context/` | Firm-wide context files loaded by CLAUDE.md / GEMINI.md |
| `skills/` | Reusable AI skills for proposals, audits, reports |
| `templates/` | Document templates for client deliverables |
| `brand/` | Color codes, typography, tone guidelines |

## Keeping It Current

- `context/HARNESS-GOALS.md` — update monthly
- `context/HARNESS-LEARNED.md` — add lessons as you discover them
- Commit and push — all team members pull to stay in sync
