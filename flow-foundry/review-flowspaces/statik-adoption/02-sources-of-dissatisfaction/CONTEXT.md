---
id: statik-adoption-stage-02
title: "Stage 02 — Sources of Dissatisfaction"
type: stage-context
stage: 2
review-intensity: heavy
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
  - "[[fitness-and-dissatisfaction-profiler]]"
  - "[[statik-method-reference]]"
---

# Stage 02 — Sources of Dissatisfaction

Covers **STATIK step 2**. Dissatisfaction is the method's engine: it is what
makes a Kanban system worth designing and what the finished system is judged
against. STATIK asks the question in two directions — of the customers, and of
the people delivering the service — and keeps the two answers separate.

## Inputs

| Input | Source | Required |
|---|---|---|
| Service frame (service, customer groups tagged recipient/dependant) | `work/01-service-frame.md` | Yes |
| Fitness criteria set | `work/01-fitness-criteria.md` | Yes |
| Mode declaration | `work/01-mode-declaration.md` | Yes |
| Bound item set (for corroborating signal only) | `work/01-bound-set.md` | No — absent in conversation-only mode |
| Access to people in each customer group, and to the delivery team | Operator arranges | Yes — this stage cannot be run from the board alone |

## Process

1. **State the attribution rule before asking anything.** Tell participants, in
   the room or in the request: dissatisfaction will be recorded against a
   *source* ("upstream requesters", "the on-call engineers"), never against a
   named person, and the written output will carry no individual attributions.
   Say it first. This stage asks people to describe what is going badly, and an
   unstated attribution rule reliably produces either a sanitized set of
   non-answers or a set of complaints about colleagues — both useless, the
   second harmful.
2. **Elicit external dissatisfaction — ask the customers.** For each customer
   group from the service frame, including dependants (who are routinely
   skipped and routinely have the sharpest complaints): what about this service
   frustrates you? What do you work around? What do you not ask us for any more
   because it is not worth it? That last question is the highest-yield one — it
   surfaces demand that has stopped arriving, which no board can show.
3. **Elicit internal dissatisfaction — ask the delivery organisation.** What
   prevents you from doing a good, professional job here? Where does work sit?
   What do you get interrupted for? What do you have to do twice? Internal
   dissatisfaction is asked *separately and in different words*, not as the same
   question pointed inward — the people delivering a service are dissatisfied by
   different things than the people receiving it, and merging the two questions
   loses that.
4. **Keep internal and external separate through to the output.** Do not merge
   them into one ranked list. The distinction is load-bearing at Stage 08:
   external dissatisfaction is what justifies the change to stakeholders,
   internal dissatisfaction is what the team will judge the change by, and a
   design that resolves only one of them fails at socialization for reasons
   nobody can articulate if the two were merged.
5. **Attribute each item to a source and connect it to a fitness criterion.**
   Every recorded dissatisfaction names the source it came from and the fitness
   criterion (from Stage 01) it threatens. Two exceptions get their own explicit
   handling rather than being forced:
   - **Dissatisfaction with no matching criterion** means Stage 01's elicitation
     missed a criterion. Add it, and say so — this is a normal and valuable
     outcome, not a defect.
   - **Dissatisfaction that is not about flow at all** (tooling, staffing,
     interpersonal, a wrong product decision) is recorded in a clearly separate
     "out of scope for this system design" list and handed back to the operator.
     A Kanban system will not fix it, and quietly carrying it forward means
     Stage 08 promises something the design cannot deliver.
6. **Corroborate with board signal where the mode declaration allows it, and
   label it as corroboration.** Aged items, high blocked counts, reopen rates,
   and long queue residency can support a stated dissatisfaction. They cannot
   discover one — a board records the work that arrived, never the frustration
   of the person who stopped sending it. Board signal that contradicts a stated
   dissatisfaction is reported as a discrepancy for the reviewer to resolve, not
   used to overrule the person who said it.
7. **Present internal and external sets, the added criteria, and the
   out-of-scope list, and stop for ratification.**

`Layer-3: fitness-and-dissatisfaction-profiler`

## Outputs

| Artifact | Shape | Lands in |
|---|---|---|
| External dissatisfaction set | Table: statement, source group, threatened fitness criterion, corroborating board signal or `none`, and `recipient`/`dependant` | `work/02-dissatisfaction-external.md` |
| Internal dissatisfaction set | Same shape, sourced from the delivery organisation | `work/02-dissatisfaction-internal.md` |
| Fitness-criteria amendments | Criteria added or reworded because Stage 02 surfaced them, each with the dissatisfaction that prompted it | `work/02-criteria-amendments.md` |
| Out-of-scope list | Dissatisfactions a Kanban system will not address, with a one-line reason each, for operator routing | `work/02-out-of-scope.md` |
| Discrepancy list | Stated dissatisfactions the board signal contradicts, unresolved, for the reviewer | `work/02-discrepancies.md` |

## Verify

Trace **Stage 01 → Stage 02**: every fitness criterion in
`work/01-fitness-criteria.md` (as amended by `work/02-criteria-amendments.md`)
must appear as the threatened criterion of at least one dissatisfaction item, or
be explicitly marked `no dissatisfaction reported` — and every dissatisfaction
item must name a criterion that exists in the amended set. Check both directions
and record the counts.

The failure mode this catches, in both directions: a fitness criterion nobody is
dissatisfied about is usually one the team assumed rather than heard, and it
will drive Stage 06 and Stage 07 design decisions that address nothing; a
dissatisfaction pointing at a criterion that is not in the set means Stage 01's
elicitation was incomplete and Stage 04 is about to measure against the wrong
axis. Running this check leaves a one-line result in the run's decision log.

## Review

- **Reviewer:** the service owner, with at least one representative from each
  customer group having confirmed their own group's entries. Confirmation is per
  group and by that group — the service owner cannot ratify what a dependant
  team said on the dependant team's behalf.
- **Intensity:** `heavy` — **breaks the U-curve default with cause.** Every
  fitness criterion the rest of the flow measures against originates or is
  corrected here. A missed source of dissatisfaction is not recoverable
  downstream: Stage 04 will faithfully measure the wrong thing and report a
  healthy system, and nothing later in the flow can detect the omission.
- **Evidence:** a decision-log entry naming the reviewer, the date, which
  customer groups confirmed their own entries, which did not and why, and any
  discrepancy resolved or left open.

## Data boundary

- **Max data-class this stage handles:** `internal`
- **Sanctioned engines for this stage:** Rovo, Copilot — per the employer
  sanctioned-tool matrix.
- This is the flow's most sensitive conversational surface. Elicited statements
  routinely name individuals and describe inter-team friction. The attribution
  rule in step 1 is a **data-handling constraint, not a facilitation
  preference**: individual names are removed at the point of recording, not at
  the point of publishing, so no artifact in the run ever carries them.
- Raw elicitation notes, if kept at all, stay in `work/` (Layer-4, transient,
  gitignored at instantiation) and never enter the run record.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
