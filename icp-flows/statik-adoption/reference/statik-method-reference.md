---
id: statik-method-reference
title: "STATIK Method Reference"
type: specification
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related: ["[[statik-adoption]]"]
---

# STATIK Method Reference

The method this flowspace implements, stated compactly, with the sources it was
reconstructed from. Layer-3 stable reference: it defines *the method*, not this
flowspace's procedure — the stage `CONTEXT.md` files own procedure.

## Source status — read this first

**The two source articles the operator supplied were not readable during this
build.** Both returned HTTP 403 at the egress proxy on CONNECT — an
organisation egress-policy denial for the hosts, not a paywall, a dead link, or
a retryable fault:

- `https://aktiasolutions.com/statik-kanban-implementation-kanban-rollout/`
- `https://hjavixcs.medium.com/statik-systems-thinking-approach-to-introduce-kanban-13996dbe414a`

No content from either entered this build. The method below was reconstructed
from reachable sources instead:

| Source | Used for |
|---|---|
| Kanban University — glossary, Fit for Purpose material, fitness-for-purpose score | Step 1 vocabulary; fitness criteria; commitment/delivery point definitions |
| David J. Anderson School of Management — writing on dissatisfaction and on classes of service | Step 2's internal/external split; step 6's four classes and their cost-of-delay shapes; capacity-allocation conventions |
| Practitioner write-ups: Agile Velocity, Iterators, Businessmap, VivifyScrum, Meirik, StarAgile, Softensity | Step sequence and step-level detail; corroboration across independent descriptions |
| Michael Mahlberg, "don't underestimate step 8 of STATIK" | Step 8's weight as a negotiation with design authority, not a communications exercise |

These agree on the canonical step sequence, so the **structural** risk from the
blocked sources is low.

**Residual risk, stated rather than buried:** the two blocked articles may carry
framing, worked examples, or a workshop-facilitation shape this reference does
not reflect. The Aktia piece's title suggests rollout/implementation emphasis
that would bear on Stage 08 in particular. This artifact is therefore
`truth-level: to-review`. If the operator can supply the article text, it enters
as foreign material through `skill-foundry/templates/intake-vetting-checklist.md`
— it is not folded in silently.

## What STATIK is

**S**ystems **T**hinking **A**pproach **T**o **I**ntroducing **K**anban.
Devised by David J. Anderson as the method for introducing Kanban to an existing
service. Its premise is that a Kanban system is *designed for a specific
service*, from that service's own demand, capability, and dissatisfaction —
never installed from a template.

It is a complementary practice to the Kanban Method itself: STATIK produces the
system; the Kanban Method's practices (visualize, limit WIP, manage flow, make
policies explicit, implement feedback loops, improve collaboratively) operate
and evolve it.

## The eight steps

| # | Step | The question it answers |
|---|---|---|
| 1 | Understand what makes the service fit for the customer's purpose | What do customers judge this service on? |
| 2 | Understand sources of dissatisfaction | What is wrong now — for customers, and for the people delivering? |
| 3 | Analyse demand | What arrives, from whom, how often, in what pattern? |
| 4 | Analyse capability | What does the record say we actually deliver? |
| 5 | Model the workflow | What sequence of knowledge-discovery activities does work pass through? |
| 6 | Discover classes of service | How should items of differing urgency be treated? |
| 7 | Design the kanban system | What are the board, limits, cards, policies, cadences, and metrics? |
| 8 | Socialize the design and negotiate implementation | Do the people affected understand and agree? |

Steps 1 and 8 are commonly described as the more advanced ones, needing higher
organisational maturity, and are sometimes omitted — which is why the middle six
are the most frequently taught set. **This flowspace implements all eight**, on
the reasoning that omitting step 1 leaves step 4 with nothing to measure against
and omitting step 8 is the most common cause of a technically sound system
nobody adopts.

## Step notes

**1 — Fitness for purpose.** Fitness criteria are the metrics by which a
customer in a given market segment judges whether the service is fit for their
purpose. Commonly lead time, predictability, quality, safety, and regulatory
conformance — but they are elicited, not assumed. Different customer segments
hold different criteria for the same service.

**2 — Dissatisfaction.** Asked in two directions and kept separate. *External*:
the people who depend on or are affected by the service — recipients and
dependants both. *Internal*: the delivery organisation — what prevents them from
doing a good, professional job. Dissatisfaction is the energy for change and the
thing the finished system is judged against.

**3 — Demand.** Who the customers are, what they ask for, the arrival rate (a
number per unit time) and the *pattern* of arrival over different time framings,
and their expectations. Work item type discovery happens here and is
acknowledged in the literature as non-trivial: practitioners struggle to balance
sufficient detail against a workable level of abstraction — "a cup of coffee"
may be too abstract; every item on the menu is too granular.

**4 — Capability.** Historical data for service delivery: lead time (as a
distribution, since the distribution is what indicates predictability), quality
functional and non-functional, predictability, and conformance with regulatory
requirements or standards. Analysed *per work item type*, because different
types have different distributions and merging them describes no type.

**5 — Workflow.** Modelled per work item type as the sequence of dominant
activities through which new knowledge is discovered — delivery as a
knowledge-discovery process. Explicitly *not* the organisation chart. Two points
are set here: the **commitment point**, upstream of which items are managed as
options rather than as work in progress; and the **delivery point**, past which
items may still be managed until their utility in the customer's hands is
validated.

**6 — Classes of service.** Policies defining how items are treated, derived
from cost-of-delay shape. See `classes-of-service-model.md` for the full model.

**7 — System design.** The board, the cards, kanban (WIP) limits per state and
possibly per type or class, explicit policies, cadences, and metrics. Ticket
design follows from a specific question: what does someone need to know, at each
state, to decide which item to pull next?

**8 — Socialization.** Walk stakeholders through how the system will work from
their point of view; listen; address objections — which may require adjusting
classes of service, capacity allocations, kanban limits, board design, or
reporting. Rework to accommodate what was learned, then revisit stakeholders to
confirm their concerns were adequately accommodated.

## The iteration rule

The steps are **not sequential in practice**. Learning from one informs and
changes the others, and a STATIK pass is expected to loop: later steps routinely
reveal information that invalidates earlier ones. This is the method working
correctly.

The flowspace names its three most common loop-backs (4→3, 5→4, 6→2) in
`HUB.md` and makes each detectable through a stage's Verify field, so a loop-back
is a safe move rather than a discovery made too late.

## What this reference is not

- **Not a facilitation guide.** How to run the workshops — room setup, exercise
  format, timeboxing — is out of scope. Stage-level procedure lives in the stage
  contracts; Stage 08's structure lives in
  `rollout-and-socialization-guide.md`.
- **Not a Kanban Method primer.** The six general practices operate the system
  STATIK designs; they are referenced, not taught here.
- **Not authoritative over the sources.** Where this reference and a Kanban
  University publication disagree, the publication wins and this document is
  corrected.
