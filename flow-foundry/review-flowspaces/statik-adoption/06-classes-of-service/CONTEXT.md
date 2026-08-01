---
id: statik-adoption-stage-06
title: "Stage 06 — Classes of Service"
type: stage-context
stage: 6
review-intensity: light
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[statik-adoption]]"
  - "[[class-of-service-designer]]"
  - "[[classes-of-service-model]]"
---

# Stage 06 — Classes of Service

Covers **STATIK step 6**: discover the classes of service this system needs. A
class of service is a set of policies governing how a work item is selected,
sequenced, and treated — derived from the *shape of its cost of delay*, not from
how loudly it was asked for.

The distinction that must hold: **a work item type is what the work is; a class
of service is how urgent it is.** They are independent axes. The same type
appears in several classes, and a class contains several types. Collapsing them
— giving each type a fixed class — is the most common way this step is got
wrong, and it produces a system that cannot expedite anything without
reclassifying the work itself.

## Inputs

| Input | Source | Required |
|---|---|---|
| Work item type set | `work/03-work-item-types.md` | Yes |
| Demand profile per type | `work/03-demand-profile.md` | Yes |
| Customer expectation per type | `work/03-expectations.md` | Yes |
| Capability profile and fitness verdicts (recomputed if Stage 05 required it) | `work/04-capability-profile.md`, `work/04-fitness-verdicts.md` | Yes |
| Workflow model with commitment point | `work/05-workflow-model.md`, `work/05-commitment-point.md` | Yes |
| Internal and external dissatisfaction sets | `work/02-dissatisfaction-*.md` | Yes |
| Current expedite practice — how urgent work is actually handled today | Delivery team | Yes |

## Process

1. **Confirm Stage 04 is current before deriving anything.** If
   `work/05-recomputation-directive.md` carries a loop-back, this stage does not
   open until Stage 04 has been re-run from the ratified commitment point. Every
   class of service derives from lead-time and expectation figures; deriving them
   from a stale basis produces policies that look evidence-backed and are not.
2. **Identify cost-of-delay shapes from the evidence, per type and per
   requesting group.** Ask, for each kind of demand: what happens as this item is
   delayed? The four canonical shapes and what they look like in the record:
   - **Expedite** — cost of delay is immediate and severe. In the record: items
     that visibly jumped the queue, that were worked while other work was
     dropped, or that appear in incident-linked demand.
   - **Fixed date** — cost is low until a date, then steps up sharply. In the
     record: items with due dates that were genuinely consequential (regulatory,
     contractual, an external event), distinguishable from due dates that were
     administrative defaults.
   - **Standard** — cost rises gradually with delay. The default, and the
     largest share of demand in most services.
   - **Intangible** — cost is low now and potentially severe much later.
     Maintenance, upgrades, tech debt, experiments. In the record: the work that
     is repeatedly deferred, and the work the internal dissatisfaction set
     complains never gets done.
3. **Derive classes from the shapes actually present — do not install the
   canonical four by default.** A service with no genuine regulatory or
   contractual deadlines does not need a fixed-date class, and creating one
   invites its misuse as a second expedite lane. Propose only classes the
   evidence supports; name any canonical class deliberately omitted, with the
   reason.
4. **Cross-check against the intangible class specifically.** Intangible work is
   the class that never survives informal prioritisation — it loses every
   argument against work with a visible customer, and it is the direct cause of
   a large share of internal dissatisfaction in most services. If Stage 02's
   internal set complains about deferred maintenance or debt and no intangible
   class is proposed, that is a contradiction to resolve before proceeding.
5. **Test each proposed class against the dissatisfaction sets.** Every class
   should address at least one recorded dissatisfaction, and every
   flow-related dissatisfaction should be addressed by at least one class or by
   a Stage 07 design element. A dissatisfaction addressed by neither is reported
   as a candidate loop-back to Stage 02 — either the elicitation missed
   something, or the complaint is not about flow and belongs on the out-of-scope
   list.
6. **Write the policy for each class, in operational terms.** Selection rule
   (how an item of this class is picked up), sequencing rule (its order relative
   to other classes), WIP treatment (whether it may exceed limits and by how
   much), and the visual signal on the board. A class without an operational
   policy is a label; the policies are what make it real.
7. **Propose capacity allocation only where the measured demand mix supports
   it, and cite the mix.** Where Stage 03's arrival rates give a defensible
   starting split, propose it with the figures behind it. Where they do not, say
   so and propose no number. Conventional figures from the literature
   (fixed-date around 20%, intangible 10–20%) are stated **separately, as
   context**, explicitly not as a recommendation for this service — the entire
   point of STATIK is deriving these from this service's own demand. Allocation
   is a starting point to be adjusted at the cadences Stage 07 designs, and it
   is presented that way.
8. **Constrain expedite explicitly.** Expedite capacity is conventionally a
   single item at a time, and the constraint is the point: an expedite lane
   without a hard limit becomes the default lane within a quarter, at which
   point the class system has been destroyed and nobody will be able to say
   when. Propose the limit, and propose the trigger that authorises an expedite
   — who can invoke it, on what grounds.
9. **Present the classes, policies, allocation, and the omitted-class rationale,
   then stop for ratification.**

`Layer-3: class-of-service-designer`

## Outputs

| Artifact | Shape | Lands in |
|---|---|---|
| Class of service set | Per class: name, cost-of-delay shape, the evidence it was derived from, which types can carry it, and which dissatisfaction(s) it addresses | `work/06-classes-of-service.md` |
| Per-class policy | Selection rule, sequencing rule, WIP treatment, board signal, and (for expedite) the invocation trigger and authoriser | `work/06-class-policies.md` |
| Capacity allocation proposal | Per class: proposed share with the demand figures behind it, or `no proposal — demand mix does not support one`; conventional figures stated separately as context | `work/06-capacity-allocation.md` |
| Omitted-class rationale | Canonical classes deliberately not created, each with the reason | `work/06-omitted-classes.md` |
| Unaddressed dissatisfaction list | Flow-related dissatisfactions no class addresses, as candidate loop-backs to Stage 02 | `work/06-unaddressed.md` |

## Verify

Trace **Stage 03 → Stage 06**: the class of service set must be genuinely
independent of the work item type set. Check explicitly that at least one class
can carry more than one type, and that at least one type can appear in more than
one class — and if neither holds, state why the service is genuinely an
exception rather than letting the collapse pass.

The failure mode this catches: classes of service are derived one-per-type
("changes are standard, incidents are expedite"), which reads as a valid design
and is in fact just the type set renamed. Such a system cannot expedite a change
without relabelling it as an incident, so the first genuinely urgent change
corrupts the type data permanently — and by then the board looks fine. Running
this check leaves a one-line result in the run's decision log.

## Review

- **Reviewer:** the service owner, with the customer groups confirming that the
  classes match how they actually experience urgency. A class set ratified only
  internally reliably under-represents fixed-date and expedite demand, because
  the people who feel that pressure are outside the room.
- **Intensity:** `light` — constrained execution. The shapes are derived from
  Stage 03 and Stage 04 evidence against a fixed model, and the reviewer accepts
  or amends against it. The judgment that would make this heavy — whether to
  propose allocation numbers at all — is settled by the design rule in step 7
  rather than re-litigated per run.
- **Evidence:** a decision-log entry naming the reviewers, the date, the ratified
  class set, every canonical class omitted with its reason, and whether capacity
  allocation was proposed or withheld.

## Data boundary

- **Max data-class this stage handles:** `internal`
- **Sanctioned engines for this stage:** Rovo, Copilot — per the employer
  sanctioned-tool matrix.
- Expedite invocation policy names *roles*, never individuals — "the on-call
  incident manager", not a person's name. The policy outlives the postholder,
  and naming individuals in a governance artifact is both a data-handling
  problem and a maintenance one.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
