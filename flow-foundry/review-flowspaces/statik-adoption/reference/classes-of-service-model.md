---
id: classes-of-service-model
title: "Classes of Service Model — Cost of Delay, Policy, and Allocation"
type: specification
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related: ["[[statik-adoption]]", "[[statik-method-reference]]"]
---

# Classes of Service Model

The model Stage 06 derives against. Layer-3 stable reference.

## The distinction that must hold

**A work item type is what the work is. A class of service is how urgent it
is.** They are independent axes:

- The same *type* appears in several classes — a routine firewall change is
  usually standard, is fixed-date when tied to an audit, and is expedite during
  an incident. It is the same kind of work each time.
- The same *class* contains several types — an expedite lane carries incidents,
  changes, and requests alike.

Collapsing the axes (one class per type: "changes are standard, incidents are
expedite") is the most common failure of this step. It reads as a valid design
and is in fact the type set renamed. The system then cannot expedite a change
without relabelling it as an incident, so the first genuinely urgent change
corrupts the type data permanently — and the board looks fine throughout.

Stage 06's Verify field tests exactly this: at least one class must carry more
than one type, and at least one type must be able to appear in more than one
class.

**The Jira priority field is not a class of service.** Priority is usually
set by the requester, at request time, with no policy attached and no
constraint on how many items can carry the top value. A class of service is a
policy the *service* applies, with capacity behind it. Where a board's priority
field happens to correlate with genuine urgency, that is corroborating evidence
for Stage 06 — never a substitute for the derivation.

## The four canonical classes

Derived from the *shape of the cost of delay* — how the cost of not delivering
changes over time.

| Class | Cost-of-delay shape | Typical policy shape |
|---|---|---|
| **Expedite** | Immediate and severe from the moment of arrival | Pull immediately, drop other work if needed, may exceed WIP limits, hard limit on concurrent expedites (conventionally one) |
| **Fixed date** | Low until a date, then a sharp step up | Scheduled backwards from the date, pulled to start with enough buffer, not expedited before it needs to be |
| **Standard** | Rises gradually with delay | Pulled in customer-agreed order or per an explicit sequencing policy; the bulk of demand in most services |
| **Intangible** | Low now, potentially severe much later | Protected by an explicit capacity allocation, because it loses every informal prioritisation argument |

### Notes that matter in practice

**Expedite must be constrained or it consumes the system.** An expedite lane
without a hard concurrent limit and an explicit invocation policy becomes the
default lane within a quarter, at which point the class system has been
destroyed and nobody can say when it happened. Stage 06 proposes both the limit
and the trigger: who may invoke an expedite, on what grounds.

**Fixed date is not "has a due date."** Most due dates on most boards are
administrative defaults. A fixed-date class exists where missing the date has a
genuine step-change consequence — regulatory, contractual, or tied to an
external event that will not move. Creating a fixed-date class where none of
these exist invites its use as a second expedite lane.

**Intangible is the class that does not survive informal prioritisation.**
Maintenance, upgrades, technical debt, experiments — work whose value is real
and hard to quantify, which loses to work with a visible waiting customer every
time. It cannot be protected by good intentions: it needs a policy-based
capacity allocation, WIP limits to ensure it is done properly when done, and
organisational acceptance that reducing risk is a valuable outcome. In most
services, a large share of Stage 02's *internal* dissatisfaction is intangible
work that never gets capacity — Stage 06 checks for exactly this contradiction.

**Derive only the classes the evidence supports.** Installing all four by
default is the template rollout this flow exists to replace. A service with no
genuine regulatory or contractual deadlines does not need a fixed-date class.
Stage 06 records every canonical class deliberately omitted, with its reason.

## Per-class policy shape

A class without an operational policy is a label. Each class carries:

| Element | The question it answers |
|---|---|
| **Selection rule** | How does an item of this class get picked up? |
| **Sequencing rule** | Where does it go relative to other classes? |
| **WIP treatment** | May it exceed limits? By how much? What is displaced? |
| **Board signal** | How is it visually distinguished — colour, lane, marker? |
| **Invocation** (expedite only) | Who may invoke it, on what grounds, with what record? |

## Capacity allocation

Allocation reserves a share of capacity per class so that a class with weak
informal standing (intangible, above all) actually gets worked.

**This flowspace's design rule, which is deliberately conservative:** Stage 06
proposes a starting allocation **only where Stage 03's measured demand mix
supports one**, and cites that mix. Where it does not, no number is proposed and
the absence is stated.

Conventional figures from the literature — fixed date around 20%, intangible
10–20%, the remainder to urgency-driven standard work — are stated **separately,
as context, explicitly not as a recommendation for this service.** The entire
point of STATIK is deriving these from this service's own demand, and a
conventional number offered alongside a design is adopted as an answer far more
often than it is argued with.

Whether this is the right balance — versus offering conventional numbers as a
starting point to be argued down — is open question 3 in the primer brief, for
the operator to settle.

Allocation is always a **starting point tuned at the cadences Stage 07 designs**,
never a fixed property of the system, and it is presented that way at Stage 08.

## Failure modes Stage 06 guards against

- **One class per type** — the axis collapse above. Verify catches it.
- **Unconstrained expedite** — no concurrent limit, no invocation policy.
- **Fixed-date class with no genuine fixed dates** — becomes expedite lane two.
- **No intangible class despite internal dissatisfaction about deferred
  maintenance** — a contradiction Stage 06 resolves before proceeding.
- **Allocation numbers presented as derived when they are conventional** — the
  reason the two are separated in the output.
- **Classes that address no recorded dissatisfaction** — a class nobody needed,
  which adds ceremony and will be ignored.
