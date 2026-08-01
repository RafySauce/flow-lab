---
id: statik-adoption-stage-01
title: "Stage 01 — Service Framing & Source Binding"
type: stage-context
stage: 1
review-intensity: heavy
artifact-version: "1.1"
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
  - "[[board-evidence-requirements]]"
  - "[[statik-method-reference]]"
---

# Stage 01 — Service Framing & Source Binding

Covers **STATIK step 1** (understand what makes the service fit for the
customer's purpose) plus the source binding STATIK assumes but does not specify.
Naming the service and naming its customer are the same conversation, so they
happen together.

## Inputs

| Input | Source | Required |
|---|---|---|
| Trigger phrase ("Run STATIK", "design a Kanban system for this service", "I want to introduce Kanban here") | Service owner / delivery manager / coach | Yes |
| Service name and one-sentence description of what it delivers | Operator | Yes |
| Source mode declaration — live Jira, Jira export, live ServiceNow, ServiceNow export, or conversation-only | Operator | Yes |
| Jira board / project key / saved filter identifying the service's work | Operator | Only in live-Jira mode |
| Export file with the columns listed in `reference/board-evidence-requirements.md` §2 | Operator | Only in Jira export mode |
| ServiceNow table (`incident`, `sc_request`/`sc_req_item`, or a named custom table) and encoded query/view identifying the service's work | Operator | Only in live-ServiceNow mode |
| ServiceNow export file with the columns listed in `reference/board-evidence-requirements.md` §7 | Operator | Only in ServiceNow export mode |
| Existing service definition, SLA, or OLA documentation | Confluence or operator paste | No — recorded as a gap if absent |
| Names of the customer groups the service delivers to | Operator | Yes |

## Process

1. **Frame the service, not the team.** Ask what the service *delivers* and to
   whom. Record the answer as a service, not an org unit: "change requests for
   the network estate" is a service; "the Network Engineering team" is not.
   STATIK models the flow of work, not the organisation chart, and framing the
   run around a team is the error that makes every later stage model the wrong
   system.
2. **Name the customers explicitly, and separate them into recipients and
   dependants.** Recipients ask for the service's output; dependants are
   affected by it without asking (downstream teams, auditors, on-call). Both
   generate fitness criteria; only recipients usually get asked. Record each
   customer group with a one-line statement of what they come to this service
   *for*.
3. **Test the single-service assumption and halt if it fails.** If the bound
   board carries work for more than one service — two distinct customer sets
   with distinct purposes — stop and say so plainly. Two services are two runs.
   Do not offer to filter one out silently: which items belong to which service
   is exactly the judgment that must be made deliberately, and a wrong split
   propagates into every downstream number. Offer the operator the choice of
   re-binding to a filtered scope they define, or splitting into two runs.
4. **Bind the source.** In live-Jira or Jira-export mode, invoke
   `jira-portfolio-ingest`. In live-ServiceNow or ServiceNow-export mode,
   invoke `servicenow-ticket-ingest` (`produced-skills/servicenow-ticket-ingest/`,
   verified — built 2026-08-01; no on-engine test yet, see `HUB.md` Known
   gaps). Both skills produce the identical normalized item set and
   field-availability report shape, so Stages 03–05 never need to branch on
   which ticketing system a service actually uses. Whichever skill is bound
   owns the data-class screen, the field map
   confirmation, and the halt conditions (count mismatch, pagination
   truncation, missing hard-required field) — do not duplicate them here. A
   service that genuinely tracks work in both systems binds both and records
   the split explicitly rather than merging silently. In conversation-only
   mode, skip binding entirely and record the reason.
5. **Inventory history separately from fields.** The field-availability report
   says which *columns* exist; it does not say whether status-transition history
   is available. Check and record separately: are per-item state-entry and
   state-exit timestamps retrievable, or only Created and Resolved? This single
   answer determines whether Stage 04 can report per-state residency (which is
   what makes a WIP limit defensible) or only end-to-end lead time. Record it
   even when the answer is "not checked" — see the open item in `HUB.md`.
6. **Elicit fitness criteria (STATIK step 1).** For each customer group, ask
   what makes this service fit for their purpose — what they judge it on. Drive
   toward the standard axes without leading: lead time, predictability, quality,
   safety, regulatory conformance. Each criterion must end up stated as
   something measurable in principle, with the customer group that holds it. A
   criterion nobody can name a measure for is recorded as unmeasurable rather
   than dropped — Stage 02 often reveals it was the real one.
7. **Emit the mode declaration.** Per STATIK step (1–8), state whether it will be
   evidence-grounded or conversation-only in this run, and why. This is the
   artifact that stops a later stage from claiming empirical support it does not
   have. Apply the sufficiency floors in
   `reference/board-evidence-requirements.md` §3: a step is evidence-grounded
   only if the data actually clears them, not merely if a board was bound.
8. **Present the frame for ratification and stop.** Service, customers, fitness
   criteria, bound scope with item count, history availability, and the mode
   declaration — presented together, confirmed before Stage 02 opens.

`Layer-3: jira-portfolio-ingest` (steps 4–5, Jira board binding only) ·
`Layer-3: servicenow-ticket-ingest` (steps 4–5, ServiceNow binding only — verified, built 2026-08-01) ·
`Layer-3: inline (one-off — service framing, customer separation, fitness-criteria elicitation, mode declaration)`

## Outputs

| Artifact | Shape | Lands in |
|---|---|---|
| Service frame | Service name, one-sentence delivery statement, and a table of customer groups each tagged `recipient` or `dependant` with what they come for | `work/01-service-frame.md` |
| Fitness criteria set | 3–7 criteria, each with: the criterion, the customer group holding it, the axis (lead time / predictability / quality / safety / regulatory), and how it could be measured — or `unmeasurable` with the reason | `work/01-fitness-criteria.md` |
| Bound item set + field-availability report | `jira-portfolio-ingest`'s or `servicenow-ticket-ingest`'s canonical outputs (identical shape), unmodified, tagged with the source system bound | `work/01-bound-set.md` |
| History-availability finding | One of `full transition history` / `created and resolved only` / `not checked` / `n-a (conversation-only)`, with what was checked | `work/01-history-availability.md` |
| Mode declaration | A table, one row per STATIK step 1–8: step, `evidence-grounded` or `conversation-only`, and the one-line reason (which floor was met or missed) | `work/01-mode-declaration.md` |

## Verify

Trace **Stage 01 → Stage 04**: every STATIK step that Stage 01's mode
declaration marks `evidence-grounded` must be backed by a specific, named
availability finding, not by the mere fact that a board was bound. Concretely:
if the declaration marks step 4 (capability) evidence-grounded, then the
history-availability finding must say `full transition history` **and** the
bound set must clear the per-type completed-item floor in
`reference/board-evidence-requirements.md` §3 — check both, by name, and record
which.

The failure mode this catches: Stage 01 binds a board successfully, marks every
step evidence-grounded on that basis, and Stage 04 then reports a lead-time
distribution computed from eleven items with no state history — a number that
looks empirical and is not. Running this check leaves a one-line result in the
run's decision log.

## Review

- **Reviewer:** the service owner, jointly with whoever will run the resulting
  Kanban system day to day. Both, not either — the service frame is the one
  artifact that binds all eight stages, and a frame only the owner recognizes
  produces a system the team will not use.
- **Intensity:** `heavy` — U-curve default for a first stage, and independently
  warranted: the service definition, the customer set, and the fitness criteria
  are the axes everything downstream is measured against.
- **Evidence:** a decision-log entry naming both reviewers, the date, the
  ratified service frame, and any customer group or fitness criterion that was
  contested and how it was resolved.

## Data boundary

- **Max data-class this stage handles:** `internal`
- **Sanctioned engines for this stage:** Rovo, Copilot — per the employer
  sanctioned-tool matrix.
- This stage is the flow's classification gate. Exports are the higher-risk
  carrier: a raw Jira export pulls every column including comments and custom
  fields, which routinely carry names, customer references, hostnames, and
  occasionally credentials pasted into a ticket. Screen before the data is typed
  further; halt on anything above `internal` and route it to the employer-side
  instance rather than continuing.
- Customer group names are recorded as *groups* ("the field operations teams"),
  not as named individuals, from this stage onward.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
