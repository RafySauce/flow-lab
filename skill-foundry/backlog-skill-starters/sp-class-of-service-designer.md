---
id: sp-class-of-service-designer
title: "Skill Primer Brief — Class of Service Designer"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related: ["[[statik-adoption]]", "[[classes-of-service-model]]", "[[demand-profiler]]"]
---

# Skill Primer Brief — Class of Service Designer

> Intake path 1 for the skill-foundry, from the `statik-adoption` flow-foundry
> Layer-3 gap triage. Filed as
> `skill-foundry/backlog-skill-starters/sp-class-of-service-designer.md`.

## Purpose

Derives a service's **classes of service** from the observed shape of cost of
delay, writes an operational policy for each, and proposes capacity allocation
only where measured demand supports it (STATIK step 6).

It replaces two failures: installing the canonical four classes as a template
regardless of whether the service's demand contains them, and the subtler one —
deriving one class per work item type, which reads as a valid design and is in
fact the type set renamed.

## Triggering intent

**Fires on** — Stage 06 of `statik-adoption`, and standalone on:

- "What classes of service does this team need?"
- "How should we handle urgent work without wrecking everything else?"
- "Our maintenance work never gets done — how do we protect it?"
- "Set up expedite properly."

**Does not fire on (near-misses):**

- **Discovering work item types.** That is `demand-profiler`. Type is *what the
  work is*; class is *how urgent it is*. They are independent axes and this skill
  refuses to collapse them — see the load-bearing rule below.
- **Prioritizing a specific backlog or ranking items.** That is
  `closure-scorer` / `disposition-packet-builder` territory in
  `portfolio-rationalization`. This designs the *policy* by which items are
  treated, not the ranking of a particular set.
- **Setting a single work item's priority field.** That is `ai-refinement`'s
  field work. A Jira priority value is not a class of service.
- **Designing the board or the limits.** That is `kanban-system-designer`, which
  consumes this skill's classes and policies.

## Method sketch

1. **Confirm the capability analysis is current** before deriving anything. If a
   commitment-point recomputation is outstanding, stop — every class derives from
   lead-time and expectation figures, and deriving from a stale basis produces
   policies that look evidence-backed and are not.
2. **Identify cost-of-delay shapes from the evidence,** per type and per
   requesting group, against the four canonical shapes: expedite (immediate,
   severe), fixed date (step change at a date), standard (gradual rise),
   intangible (low now, potentially severe later). Cite the evidence for each —
   items that visibly jumped the queue, due dates with genuine consequences,
   repeatedly deferred work.
3. **Derive only the classes the evidence supports.** A service with no genuine
   regulatory or contractual deadlines does not need a fixed-date class, and
   creating one invites its use as a second expedite lane. Record every canonical
   class deliberately omitted, with the reason.
4. **Cross-check the intangible class specifically.** Intangible work loses every
   informal prioritisation argument and is the direct cause of a large share of
   internal dissatisfaction in most services. Internal dissatisfaction about
   deferred maintenance with no proposed intangible class is a contradiction to
   resolve before proceeding, not a judgment call.
5. **Test every class against the dissatisfaction sets.** Each class should
   address at least one recorded dissatisfaction; each flow-related dissatisfaction
   should be addressed by a class or flagged for the design stage. Anything
   addressed by neither is reported as a candidate loop-back to the elicitation.
6. **Write an operational policy per class** — selection rule, sequencing rule,
   WIP treatment, board signal, and (for expedite) the invocation trigger and
   authorising role. A class without an operational policy is a label.
7. **Constrain expedite explicitly.** Propose a hard concurrent limit
   (conventionally one) and the invocation policy. An expedite lane without both
   becomes the default lane within a quarter, at which point the class system has
   been destroyed and nobody can say when.
8. **Propose capacity allocation only where the measured demand mix supports it,
   and cite the mix.** Where it does not, propose no number and say so.
   Conventional figures (fixed date ~20%, intangible 10–20%) are stated
   **separately, as context, explicitly not as a recommendation** — the point of
   STATIK is deriving these from this service's own demand, and a conventional
   number offered alongside a design is adopted as an answer far more often than
   it is argued with. Always framed as a starting point tuned at the cadences.

### The load-bearing rule

**Classes must be independent of types.** At least one class must carry more than
one type, and at least one type must be able to appear in more than one class. If
neither holds, the derivation collapsed into a renaming and must be redone — or
the service is a genuine exception and that must be stated as such.

The failure this prevents is specific: a one-class-per-type system cannot
expedite a change without relabelling it as an incident, so the first genuinely
urgent change corrupts the type data permanently — and the board looks fine
throughout.

### Known failure modes to guard against

- **One class per type** — the collapse above.
- **Installing the canonical four by default** — the template rollout this flow
  exists to replace.
- **Treating the Jira priority field as a class of service.** Priority is set by
  the requester with no policy attached and no cap on the top value; a class is a
  policy the *service* applies with capacity behind it.
- **Unconstrained expedite** — no concurrent limit, no invocation policy.
- **Fixed-date class where due dates are administrative defaults.**
- **Presenting conventional allocation figures as derived.**
- **Naming individuals in the expedite invocation policy** rather than roles.

## Inputs and data boundary

Reads: the work item type set and demand profile; per-type customer expectations;
the capability profile and fitness verdicts; the workflow model and commitment
point; both dissatisfaction sets; and the delivery team's account of how urgent
work is actually handled today (which is usually where the real, undocumented
expedite policy lives).

Max data-class: `internal`. Expedite invocation policy names **roles**, never
individuals — the policy outlives the postholder, and naming individuals in a
governance artifact is both a data-handling problem and a maintenance one.

Engines: Rovo and Copilot, per the employer matrix.

## Demand source

`statik-adoption` flowspace Layer-3 triage, 2026-08-01. No house skill covers
classes of service; the model it derives against is
`icp-flows/.../reference/classes-of-service-model.md` (carried with the
flowspace).

## Definition of done

1. The independence test is enforced: a derivation yielding exactly one class per
   type is caught and reported as a collapse, not passed through.
2. A service whose evidence contains no genuine fixed dates yields no fixed-date
   class, with the omission recorded and reasoned.
3. Internal dissatisfaction about deferred maintenance with no proposed intangible
   class raises the contradiction before proceeding.
4. Every class carries all five policy elements; a class missing its selection or
   sequencing rule fails.
5. Expedite always carries a concurrent limit and an invocation policy naming an
   authorising role, never an individual.
6. Capacity allocation is proposed only with the demand figures cited; a run with
   an insufficient demand mix produces an explicit no-proposal.
7. Conventional figures appear only in a separately-labelled context block, never
   in the proposal table.
8. A class addressing no recorded dissatisfaction is flagged.
9. A test feeding a Jira priority field as the proposed class basis is declined
   with the stated distinction.
10. A stale capability basis (outstanding recomputation) stops the run.
