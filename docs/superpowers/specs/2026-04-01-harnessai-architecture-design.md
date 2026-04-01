# HarnessAI — File Architecture Design
_Date: 2026-04-01 | Status: Approved_

---

## Business Context

**Company:** HarnessAI — AI consulting firm, Lethbridge, Alberta, Canada
**Domain:** harnessai.ca
**Team:** Tyrell (founder/owner), Jordan (founder/owner, jordan@youthone.ca), + 1 future member
**Phase:** Brand development + infrastructure setup

---

## Architecture: Hub + Spoke

One central `harnessai-core` GitHub repo holds all shared firm context. Each client engagement gets its own repo. Documents and assets live in Google Drive.

```
GitHub
├── harnessai-core          ← Firm brain (context, skills, brand, templates)
├── harnessai-client-[name] ← One repo per client engagement
└── harnessai-website       ← harnessai.ca (future)

Google Drive
└── HarnessAI (folder ID: 1DOwSDk90yhDWlhujUYktEouDZ8HmNpB0)
    ├── 00-Admin/
    ├── 01-Brand/
    ├── 02-Sales/
    ├── 03-Clients/
    └── 04-Operations/
```

---

## Core Repo Structure (`harnessai-core`)

```
harnessai-core/
│
├── CLAUDE.md              ← Auto-loads all context/ files for Claude Code
├── GEMINI.md              ← Auto-loads all context/ files for Gemini CLI
├── AGENTS.md              ← Generic fallback for other AI tools
├── README.md              ← Setup instructions for new team members
│
├── context/
│   ├── HARNESS-MISSION.md     ← What HarnessAI is, who it serves, why it exists
│   ├── HARNESS-BRAND.md       ← Colors, tone, tagline, voice examples
│   ├── HARNESS-SERVICES.md    ← Audit / Quick Win / Full Harness pricing + scope
│   ├── HARNESS-GOALS.md       ← Current quarter priorities (update monthly)
│   └── HARNESS-LEARNED.md     ← Accumulated lessons across all engagements
│
├── skills/
│   ├── harness-proposal/      ← Draft proposals in HarnessAI voice + format
│   ├── harness-audit/         ← Run the AI Audit workflow
│   └── harness-report/        ← Generate client-facing reports
│
├── templates/
│   ├── proposal-template.md
│   ├── audit-report-template.md
│   ├── scope-of-work-template.md
│   └── client-onboarding-template.md
│
├── brand/
│   ├── colors.md              ← Hex codes, font specs, usage rules
│   └── voice-guide.md         ← Tone examples, what to say / not say
│
└── docs/superpowers/specs/    ← Design docs (this file lives here post-repo creation)
```

**CLAUDE.md root content:**
```
@context/HARNESS-MISSION.md
@context/HARNESS-BRAND.md
@context/HARNESS-SERVICES.md
@context/HARNESS-GOALS.md
@context/HARNESS-LEARNED.md
```

Any team member who opens Claude Code inside `harnessai-core` instantly loads the full firm context. No manual setup per session.

---

## Client Repo Structure (`harnessai-client-[name]`)

```
harnessai-client-[name]/
├── CLAUDE.md              ← Loads core context + this client's context
├── README.md              ← Project summary
│
├── context/
│   ├── CLIENT-PROFILE.md  ← Who they are, their business, key contacts
│   ├── CLIENT-GOALS.md    ← What we're solving for them
│   └── CLIENT-LEARNED.md  ← Discoveries during the engagement
│
└── deliverables/
    ├── audit/
    ├── implementations/
    └── reports/
```

---

## Google Drive Structure

**Shared Drive Folder ID:** `1DOwSDk90yhDWlhujUYktEouDZ8HmNpB0`

```
HarnessAI/
├── 00-Admin/       ← Contracts, invoices, legal
├── 01-Brand/       ← Logos, photos, website assets, QR codes
├── 02-Sales/       ← Proposals, pitch deck, pricing sheets
├── 03-Clients/
│   └── [Client Name]/
│       ├── Signed Contract
│       ├── Proposals
│       ├── Reports
│       └── Assets
└── 04-Operations/  ← SOPs, team resources, onboarding docs
```

---

## How Context Loading Works

Each team member clones `harnessai-core` once. Opening any AI tool (Claude Code, Gemini CLI) inside that folder automatically loads the full firm context — brand voice, services, goals, and accumulated lessons.

For client work, they also clone the relevant client repo. That repo's `CLAUDE.md` references core context so both load together in one session.

**Result:** Jordan using Gemini on his machine, Tyrell using Claude Code on his — same firm brain, same AI instructions, no manual setup.

---

## Collaboration Model

- **GitHub:** Code, AI context files, skills, templates (version-controlled)
- **Google Drive:** Documents, proposals, contracts, brand assets, client files
- **Ownership:** Fully shared — all team members have access to all repos and Drive folders
- **AI tools:** Each person uses their preferred tool; CLAUDE.md + GEMINI.md + AGENTS.md ensure consistent AI behavior across tools

---

## Services Reference

| Service | Price | Scope |
|---|---|---|
| The AI Audit | $500 | 90-min session, top 3 opportunities, written action plan |
| The Quick Win | $1,500 | One AI tool end-to-end in 2 weeks, measurable result |
| The Full Harness | $3,500–$5,000 | Full integration, team training, 90 days follow-up |

---

## Brand Quick Reference

- **Tagline:** "AI tools that work as hard as you do."
- **Colors:** Deep charcoal/navy + warm amber/burnt orange
- **Typography:** Strong clean sans-serif
- **Tone:** Plain spoken, confident, zero jargon
- **Target:** Trades & contractors, agriculture & rural businesses in southern Alberta
