---
id: platform-stakeholder-register-template
title: "Stakeholder Register Template — Domain-Neutral"
type: specification
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-03
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.3"
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[platform-stakeholder-register]]"
---

# Stakeholder Register Template — Domain-Neutral

The structure `platform-stakeholder-register.md` (the network-engineering
instance) populates. Use this template to instantiate a stakeholder register
for any other domain the `ai-refinement` flowspace is run against — copy it,
replace the bracketed placeholders with the real domain's teams and
tensions, and rename the copy per the domain (e.g.
`platform-stakeholder-register-<domain>.md`). Keep the same section shape so
Stage 02's stakeholder sweep and Stage 03's coalition/conflict-axis
annotation can read either instance without a contract change.

If no instance exists yet for a domain, Stage 01's grounding check flags
**ungrounded mode**: Stage 02 and Stage 03 ask the user directly who is
affected and where priorities conflict, instead of walking a register — a
degraded but functional path, not a blocked one.

**Role-types** (domain-neutral, reuse as-is): *Producer* (owns/builds) ·
*Consumer* (demand side) · *Constraint-setter* (guardrails) · *Operator*
(runs it) · *Adjacent* (integration seam) · *Sponsor* (money & mandate)

---

## Stakeholder register

| # | Stakeholder | Role-type | Domains | What they value most |
|---|-------------|-----------|---------|----------------------|
| 1 | **[Team A — primary producer]** | Producer | [domain tag] | [What this team optimizes for; what they resist.] |
| 2 | **[Team B — demand side]** | Consumer | [domain tag] | [What "working well" looks like from their side.] |
| 3 | **[Team C — guardrail owner]** | Constraint-setter | [domain tag] | [What they enforce; what they trade convenience for.] |
| 4 | **[Team D — runs day-2]** | Operator | [domain tag] | [Supportability concerns; what they dislike inheriting.] |
| 5 | **[Team E — integration seam]** | Adjacent | [domain tag] | [What must stay consistent at the boundary they own.] |
| 6 | **[Sponsor / leadership]** | Sponsor | ALL | [Strategic alignment, cost/value, portfolio concerns.] |

Add rows as the domain requires — this is a starting shape, not a fixed
count. The real network-engineering instance runs to 17 entries; a smaller
domain may need far fewer.

---

## Where priorities align

Natural coalitions — when a requirement pleases one member, it usually
pleases the rest. Batch their input; expect fast consensus.

- **[Coalition name]** — [stakeholder #s].
  *Shared value:* [what they co-sign on].

---

## Where priorities conflict

The tensions requirements gathering exists to *reconcile*. Each is a
negotiation point — surface it early, and attach a decision record rather
than letting it detonate mid-build.

- **[Tension name]** — [stakeholder #s]  ⟷  [stakeholder #s].
  *Bites hardest on:* [the concrete decision this tension shows up in].

Mark any tension that is a hard constraint (not a negotiable tradeoff) —
e.g. a physical, legal, or safety limit — explicitly, the way the real
instance flags "Growth vs. Physical Limits."

---

## Using this in requirements gathering

1. On each Jira epic/story, tag the stakeholders, then note **which coalition
   it satisfies** and **which conflict axis it triggers**.
2. **Aligned stakeholders** → batch their elicitation; expect quick
   agreement; capture as shared requirements.
3. **Conflict axes** → these are explicit tradeoff decisions. Don't let them
   surface late. Each needs a named decision-owner and a recorded rationale
   (which side won, and why).
4. **Define the escalation path** for this domain: who resolves a conflict
   between a producer and a constraint-setter that can't settle
   peer-to-peer, and who resolves a conflict about whether the work is worth
   doing at all. Name both explicitly — do not leave escalation implicit.
5. Watch for **multi-hat stakeholders** in the real org: where one team wears
   two of the role-types above, a "conflict" may actually be one overloaded
   team arguing with itself — a capacity problem wearing a requirements
   costume.
