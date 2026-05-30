# Client Vetting Framework for HarnessAI.ca

## Overview

This framework evaluates prospective clients across four key dimensions to ensure they're a strong fit for one of our service paths: **QuickWin**, **AI Organizational Assessment**, **Maintain & Optimize**, **Teach Yourself**, or a **Bespoke Project**.

This document is intended to be used as a specification to build a web-based intake/evaluation form on the HarnessAI.ca website. The form will store client information in a backend database, becoming a documented record for both prospective and active clients.

## Business Context (for the developer building this)

- **HarnessAI.ca** is an AI consulting firm with two co-founders (Tyrell Foreman, Jordan Schellenberg) working ~half-time on the business.
- **Target market: small businesses, roughly 1–100 employees** — primarily trades/contractors and agriculture/rural businesses in southern Alberta. Anything larger is out of scope for current capacity.
- Capacity model: 10 clients each (20 total), ~6 hours per client per month on the maintain product line.
- Target billable rate: **$250 CAD/hour**.
- Subscription pricing for Maintain & Optimize: **$1,250–$1,500/month** per client.
- Revenue target: $15,000/month total from Maintain & Optimize alone ($90K/yr per co-founder from this product line).
- Because slots are scarce (only 10 each), client fit must be carefully vetted before committing.

## Service Paths (Products)

1. **QuickWin** — Short engagement to build trust, learn each other, and deliver value fast. Foot-in-the-door product.
2. **AI Organizational Assessment** — Alternative entry point. A diagnostic engagement that produces a roadmap.
3. **Maintain & Optimize** — Ongoing monthly subscription where HarnessAI handles build, maintain, debug, and optimize.
4. **Teach Yourself (Enablement)** — Ongoing relationship where HarnessAI teaches the client to maintain, debug, and build on their own.
5. **Bespoke Project** — One-off custom build, scoped and quoted individually. No fixed price; pricing is estimated from scope against the $250/hr target rate. Used for well-defined, finite projects that don't fit the recurring or entry products. Does not consume a Maintain & Optimize slot, but the co-founder must confirm capacity before committing.

The vetting framework determines which path a prospective client fits best.

## Scoring Rubric

Each dimension is scored **1–5**. A client must score **at least 3** on each dimension to move forward. Total score guides path recommendation.

### Dimension 1: Organizational Readiness

| Score | Description |
| :-: | :-- |
| 1 | No executive buy-in, no budget allocated, change management not considered. |
| 2 | Interest expressed but budget uncertain, leadership commitment unclear. |
| 3 | Clear budget allocated, executive sponsor identified, basic change awareness. |
| 4 | Strong budget commitment, executive champion engaged, change plan sketched. |
| 5 | Full alignment, dedicated resources, detailed change strategy, stakeholder mapping done. |

### Dimension 2: Technical Capability & Learning Willingness

| Score | Description |
| :-: | :-- |
| 1 | Minimal technical infrastructure, no interest in learning or hands-on involvement. |
| 2 | Basic infrastructure, hesitant about technical depth, prefers consultant-led only. |
| 3 | Solid infrastructure, willing to learn, open to hands-on participation. |
| 4 | Strong technical team, eager to upskill, wants to own the build path. |
| 5 | Advanced technical capability, proactive learners, driving their own ideation and iteration. |

### Dimension 3: Collaborative Engagement & Tool Adoption

| Score | Description |
| :-: | :-- |
| 1 | Passive, waiting for solutions, won't generate ideas or feedback. |
| 2 | Minimal engagement, slow to iterate, feedback is reactive only. |
| 3 | Engaged, provides feedback, willing to iterate and test ideas. |
| 4 | Highly collaborative, generates ideas proactively, actively shapes tools and approach. |
| 5 | Strategic partner, constant ideation, rapidly tests and refines, drives continuous improvement. |

### Dimension 4: Culture Fit & Goal Alignment

| Score | Description |
| :-: | :-- |
| 1 | Misaligned values, unclear success metrics, minimal shared vision. |
| 2 | Partial alignment, vague goals, some friction on approach. |
| 3 | Clear goals, shared values on innovation and problem solving, good rapport. |
| 4 | Strong alignment, ambitious shared vision, aligned on timelines and outcomes. |
| 5 | Exceptional fit, mutual energy, values perfectly aligned, excited partnership potential. |

## Discovery Call Script & Behavioral Markers

### Opening

"Thanks for making time. Before we dive in, I want to understand your situation, your team, and what success looks like for you. This is really about figuring out if we're a good fit for each other."

### Key Questions

**1. Can you walk me through a challenge your organization faced recently where you wished you had an AI solution?**

- *Listen for:* Specific problem, not vague. Do they reference their team? Do they own the problem or blame others?
- *Marker:* Clarity and ownership suggest readiness and collaboration.

**2. What does your team look like on the technical side? What's their comfort with new tools and learning?**

- *Listen for:* Honest assessment, names and roles, growth mindset or defensiveness.
- *Marker:* Self-awareness and candor on capability.

**3. If we build something for you, what does success look like in 6 months?**

- *Listen for:* Specific, measurable outcomes. Do they mention adoption, training, culture? Or just features?
- *Marker:* Strategic thinking vs. surface-level thinking.

**4. Walk me through how decisions get made in your organization. Who needs to be on board?**

- *Listen for:* Clear chain, executive visibility, or scattered and unclear.
- *Marker:* Organizational clarity and readiness.

**5. Have you tried to adopt new tools or processes before? What worked, what didn't?**

- *Listen for:* Honesty about failures, lessons learned, or glossing over problems.
- *Marker:* Learning orientation and self-awareness.

**6. What's your budget ballpark for this, and is it already approved?**

- *Listen for:* Clear number, approved, or vague and contingent.
- *Marker:* Financial readiness.

**7. If we build this together, how involved do you want to be in the process?**

- *Listen for:* Want to learn and iterate, or hand it off entirely.
- *Marker:* Determines which service path fits (Maintain vs. Teach Yourself).

**8. What does your gut tell you about bringing AI into your business?**

- *Listen for:* Enthusiasm, skepticism, fear, curiosity, or indifference.
- *Marker:* Culture fit and genuine interest.

### Behavioral Markers During the Call

| Marker | What to watch |
| :-- | :-- |
| **Engagement** | Asking questions back? Leaning in or checking out? Taking notes? |
| **Clarity** | Answers feel thought through or off the cuff? |
| **Collaboration** | Do they say "we" and reference their team, or mostly "I"? |
| **Honesty** | Admit uncertainties or paint everything as simple? |
| **Energy** | Sound excited or obligated? |
| **Ownership** | Take responsibility for problems or blame external factors? |

## Scoring Summary & Path Recommendation

After the call, score each dimension and calculate total.

| Total Score | Interpretation |
| :-: | :-- |
| **17–20** | Strong fit. All four dimensions at 3+. Proceed with path matching. |
| **13–16** | Good fit. Likely proceed. Note any weak dimensions to monitor. |
| **9–12** | Marginal fit. Revisit specific weak areas before committing. |
| **8 or lower** | Not a good fit for current capacity. Suggest revisit in 6–12 months or refer out. |

### Path Assignment Logic

- **QuickWin** → Moderate readiness, moderate collaboration, wants quick value proof. Use as entry point regardless of long-term path.
- **AI Organizational Assessment** → Strong readiness but unclear scope or strategy. Diagnostic-first.
- **Maintain & Optimize** → Strong readiness, strong collaboration, clear goals. Moderate-to-low technical capability. Wants ongoing partnership.
- **Teach Yourself** → Strong readiness, strong technical capability, high learning willingness. Wants to own the build and maintain path.
- **Bespoke Project** → A specific, well-defined one-off need with no appetite for an ongoing relationship. Score thresholds still apply, but path is driven by scope (finite deliverable) rather than ongoing-fit. Quote custom against scope and the $250/hr target.

## Data Schema (for the web form / database)

Suggested fields for the prospective client record:

### Company / Contact Info

- company_name (string, required)
- primary_contact_name (string, required)
- primary_contact_role (string)
- primary_contact_email (string, required)
- primary_contact_phone (string)
- company_size (enum: 1-10, 11-25, 26-50, 51-100, 100+ [out of target])
- industry (string)
- location (string)
- website (string)
- referral_source (string)
- intake_date (datetime, auto)
- status (enum: prospect, in_discovery, vetted, active, declined, paused, churned)

### Discovery Call Notes

- discovery_call_date (datetime)
- discovery_call_attendees (array of strings)
- notes_q1_recent_challenge (text)
- notes_q2_technical_team (text)
- notes_q3_success_in_6mo (text)
- notes_q4_decision_making (text)
- notes_q5_past_adoption (text)
- notes_q6_budget (text)
- notes_q7_involvement (text)
- notes_q8_gut_feeling (text)
- additional_notes (text)

### Behavioral Markers (1–5 each)

- marker_engagement (int 1-5)
- marker_clarity (int 1-5)
- marker_collaboration (int 1-5)
- marker_honesty (int 1-5)
- marker_energy (int 1-5)
- marker_ownership (int 1-5)

### Scoring (1–5 each, with optional justification text)

- score_organizational_readiness (int 1-5)
- score_organizational_readiness_notes (text)
- score_technical_capability (int 1-5)
- score_technical_capability_notes (text)
- score_collaborative_engagement (int 1-5)
- score_collaborative_engagement_notes (text)
- score_culture_fit (int 1-5)
- score_culture_fit_notes (text)
- total_score (int, computed: sum of four dimension scores)

### Outcome

- recommended_path (enum: QuickWin, AI_Org_Assessment, Maintain_Optimize, Teach_Yourself, Bespoke_Project, Decline, Revisit_Later)
- decision (enum: accept, decline, hold)
- decision_rationale (text)
- evaluator (string — which co-founder ran the call)
- evaluator_secondary (string — second co-founder's independent review, optional)

### Post-Acceptance Onboarding

Once a prospect is accepted and signed, the same record extends into onboarding. These fields turn the vetted prospect into an active client engagement.

#### Engagement

- engagement_service (enum: QuickWin, AI_Org_Assessment, Maintain_Optimize, Teach_Yourself, Bespoke_Project)
- engagement_start_date (date)
- price_agreed (decimal, CAD — for Bespoke_Project, the custom-quoted total)
- quote_basis (text — for Bespoke_Project: estimated hours × rate and scope assumptions behind the quote)
- sow_signed (boolean)
- sow_link (URL — Google Drive)
- contract_signed_date (date)

#### Their Business (operational detail beyond intake)

- team_size (int)
- key_tools_in_use (array of strings — software/spreadsheets/etc.)
- main_pain_point (text — confirmed at onboarding, may differ from intake)

#### Access Needed

- access_items (array of {system_name, status: requested/granted/declined, granted_date})

#### Linked Files (Google Drive)

- proposal_url (URL)
- signed_contract_url (URL)
- deliverables_url (URL)

#### Onboarding Notes

- onboarding_notes (text — anything else relevant from initial conversations)

## Onboarding Checklist (post-signing, off-form)

A quick checklist the co-founder can run after a record moves to `active` status:

- [ ] Engagement service confirmed and start date set
- [ ] Price agreed and SOW signed
- [ ] Industry, team size, key tools captured
- [ ] Main pain point confirmed (may differ from intake)
- [ ] Access requested for all required systems/tools
- [ ] Google Drive client folder created (proposal, contract, deliverables linked)
- [ ] Kickoff meeting scheduled

## Implementation Notes for Claude Code

When building this on the HarnessAI.ca website backend:

1. **Auth**: Restrict the form/database to logged-in co-founders only. No public access.
2. **Form UX**: Single-page form ideally, with sections that mirror this document (Company Info → Discovery Notes → Markers → Scoring → Outcome).
3. **Live total score**: Calculate and display total score as the four dimension scores are entered.
4. **Path recommendation hint**: Once all four dimensions are scored, show a suggested path based on the logic above (but allow override).
5. **Storage**: Database-backed (Postgres or similar). Each client record should be editable and have a version history if possible.
6. **Search/filter**: Allow filtering by status, score, recommended path, intake date.
7. **Export**: Allow CSV export of all client records for analysis.
8. **Future**: Consider a dashboard view showing current capacity (X of 10 slots filled per co-founder) and pipeline health.

## Revision History

- v1.0 — Initial framework (drafted from discovery conversation about HarnessAI service model and vetting needs).
