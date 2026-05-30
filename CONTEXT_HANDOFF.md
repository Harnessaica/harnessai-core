# HarnessAI Context Handoff — for Claude Code Session

## Project: Client Vetting Web Form & Database

You're being handed a spec ([CLIENT_VETTING_FRAMEWORK.md](./CLIENT_VETTING_FRAMEWORK.md)) to build a client intake and evaluation system for HarnessAI.ca. This document gives you the conversational context behind the spec so you understand the "why."

## Who is HarnessAI?

- AI consulting firm based in Lethbridge, Alberta (Tyrell is the founder; one co-founder named Rev who handles parallel automation work).
- Tyrell also runs Backyard Leisure (pool/spa retail, 30+ years) and TubSupplies.ca (Shopify).
- HarnessAI is being actively built out alongside those other businesses.
- The two co-founders intend to work roughly half-time on HarnessAI.

## Product Mix (Service Paths)

1. **QuickWin** — Quick foot-in-the-door engagement to build trust and prove value fast.
2. **AI Organizational Assessment** — Alternative diagnostic entry product.
3. **Maintain & Optimize** — Ongoing monthly subscription. HarnessAI builds, maintains, debugs, and optimizes.
4. **Teach Yourself** — Ongoing relationship where the client learns to maintain/build on their own with HarnessAI guidance.

## Economics (drives why vetting matters)

- Billable rate target: **$250 CAD/hour**.
- Maintain & Optimize subscription: **$1,250–$1,500/month** per client = ~6 hours/month/client.
- Capacity: **10 clients per co-founder** (20 total max).
- Revenue from Maintain product alone: $15K/month total ($7.5K each, ~$90K/yr each).
- Because slots are scarce, **client fit must be vetted carefully**.

## Why this tool exists

With only 10 slots per co-founder, every bad-fit client is enormously costly — lost momentum, billing disputes, energy drain, opportunity cost on a better-fit client. Tyrell wants a structured way to:

1. Score every prospect across four dimensions (Organizational Readiness, Technical Capability & Learning Willingness, Collaborative Engagement, Culture Fit & Goal Alignment).
2. Run a consistent discovery call with predefined questions and behavioral markers.
3. Store all of this in a database accessible via the HarnessAI.ca website backend (login-gated, co-founders only).
4. Use the scoring to recommend a path (QuickWin / Assessment / Maintain / Teach Yourself / decline).

## What to build

A web-based intake form and database on the HarnessAI.ca website backend. The spec document ([CLIENT_VETTING_FRAMEWORK.md](./CLIENT_VETTING_FRAMEWORK.md)) contains:

- Full scoring rubric (1–5 across four dimensions).
- Discovery call script with 8 key questions and what to listen for.
- 6 behavioral markers to score during the call.
- Suggested database schema (fields, types, enums).
- Implementation notes (auth, UX, live scoring, dashboard ideas).

## Tyrell's stack preferences (from prior context)

- Python / Flask common in his existing projects.
- Railway for cloud hosting.
- Vercel for frontends.
- Cloudflare DNS.
- GitHub as single source of truth (he syncs Dell shop workstation ↔ MacBook Air at home through GitHub).
- He keeps CLAUDE.md and TASKS.md files per project.
- He has a global /checkpoint slash command for session context preservation.

Use whatever fits best, but lean into his existing stack so this integrates with his other projects rather than introducing new tooling.

## First steps for the Claude Code session

1. Confirm the target repo (likely a HarnessAI website repo — ask Tyrell which one).
2. Read CLIENT_VETTING_FRAMEWORK.md as the source of truth.
3. Propose: tech stack confirmation, file structure, and milestone breakdown.
4. Create a TASKS.md for this build.
5. Start with the data model, then a minimal working form, then auth, then polish.
