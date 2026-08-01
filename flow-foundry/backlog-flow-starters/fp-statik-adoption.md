---
id: fp-statik-adoption
title: "Flow Primer Brief — STATIK Adoption"
type: flow-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related:
  - "[[statik-adoption]]"
  - "[[decision-2026-08-01-statik-adoption-triage-and-scaffold]]"
---

# Flow Primer Brief — STATIK Adoption

> Intake path 4 for the flow-foundry, backfilled: this arrived as an operator
> description in conversation, not as a formal starter. Per `foundry-spec.md`
> §1 case 4 that is workable — the setup questionnaire is answered here rather
> than skipped, so the scaffold has a real intake record behind it. Triage
> rationale: `../decision-log/2026-08-01-statik-adoption-triage-and-scaffold.md`.

## Purpose

Design a Kanban system *for a specific service* by working through STATIK —
the Systems Thinking Approach To Introducing Kanban — with the service's own
Jira board supplying the evidence wherever evidence exists, and structured
conversation supplying it wherever it does not.

It replaces two things. The first is the template rollout: copying another
team's board columns and WIP limits and calling it a Kanban implementation,
which produces a system nobody designed for a demand nobody measured. The
second is the unaided STATIK workshop, where demand and capability are
answered from memory in a room — "we get maybe five or six of those a week,"
"most things take about two weeks" — when the board already holds the real
arrival rates and the real lead-time distribution and nobody queried them.

The flow's governing principle, which every stage restates in its own terms:
**board evidence proposes, humans ratify.** A Jira board is an artifact of how
a team was once told to track work. It is strong evidence about the system and
a poor description of it. Every board-derived finding arrives as a proposal
with its derivation shown, and a human accepts, amends, or rejects it before
it becomes a design input.

## Trigger and cadence

**Trigger:** a service owner, delivery manager, or coach opens a Kanban design
cycle for one named service — either pointing the flow at that service's Jira
board (or an export of it), or declaring conversation-only mode where no usable
board exists.

**Cadence:** per service, on adoption; then on re-run when the system stops
fitting. STATIK is explicitly iterative — later steps routinely invalidate
earlier ones, and a service whose demand mix has shifted needs the analysis
again, not a patch to the old board. The flow is cadence-neutral; annually or
on significant demand change are both normal. A run covers one service, never
several at once: two services sharing a board are two runs, and Stage 01 says
so.

**Iteration is in-run, not just across runs.** Stages 03–07 may each send the
run back to an earlier stage when they surface something that invalidates it —
this is STATIK working as designed, not a flow failure, and Stage 01's mode
declaration plus each stage's Verify field are what make a loop-back safe to
take.

## Stage sketch

| # | Stage | What happens | Review intensity (est.) |
|---|---|---|---|
| 1 | Service Framing & Source Binding | Name the service, its customers, and its boundaries; bind to a Jira board, an export, or conversation-only; screen data class; inventory which fields and history are actually available; declare per STATIK step which will be evidence-grounded; elicit fitness criteria (STATIK 1) | heavy |
| 2 | Sources of Dissatisfaction | Elicit internal and external dissatisfaction separately, attribute each to a source, and connect each to the fitness criteria it threatens (STATIK 2) | heavy |
| 3 | Demand Analysis | Discover work item types at a usable abstraction level and measure arrival rate, pattern, and variability per type (STATIK 3) | light |
| 4 | Capability Analysis | Measure delivery against demand — lead-time distribution per type, throughput, predictability, due-date performance — and test it against Stage 02's fitness criteria (STATIK 4) | light |
| 5 | Workflow Modeling | Model the knowledge-discovery activities work actually passes through; separate activities from queues; set the commitment and delivery points (STATIK 5) | heavy |
| 6 | Classes of Service | Derive classes of service from observed cost-of-delay shapes; propose capacity allocation; define the policy for each class (STATIK 6) | light |
| 7 | Kanban System Design | Assemble the system — board columns, WIP limits, ticket design, explicit policies, cadences, metrics — with each element traced to the evidence that motivated it (STATIK 7) | light |
| 8 | Socialization & Rollout | Walk each stakeholder group through the design from their own point of view, capture objections as design inputs, rework, and return for agreement (STATIK 8) | heavy |

Two stages break the U-curve default with stated cause (full rationale in the
triage decision log):

- **Stage 02 is heavy** because every fitness criterion the rest of the flow
  measures against originates here. A missed source of dissatisfaction is not
  recoverable downstream — Stage 04 will faithfully measure the wrong thing and
  report a healthy system.
- **Stage 05 is heavy** because the commitment point is a judgment call that
  silently redefines every lead-time number Stage 04 produced, and no
  downstream stage can detect that it was set wrong.

## Data profile

Every stage after binding handles real service content — issue summaries,
descriptions, customer names in ticket text, assignee names, and in Stage 02
candid statements about what is going badly — so the whole flow runs at
`data-class: internal` in an instance. This public design copy is `public` by
construction: it carries the method and the molds, never service data.

Stage-specific boundaries:

- **Stage 01 is the classification gate.** Exports are the higher-risk carrier:
  a raw Jira export pulls every column including comments and custom fields,
  which routinely carry names, customer references, hostnames, and occasionally
  credentials pasted into a ticket. The stage screens before the data is typed
  further and halts on anything above `internal`.
- **Stage 02 is the flow's most sensitive *conversational* surface** and the
  reason its output is structured by source-and-theme rather than by speaker.
  Dissatisfaction elicitation asks people to say what is going badly, which
  reliably surfaces named individuals and inter-team friction. Attribution is
  to a *source* ("upstream requesters," "the on-call engineers"), never to a
  named person, and the stage says so to participants before it starts asking.
- **Stages 03 and 04** handle assignee data only in aggregate. Neither produces
  a per-person throughput or lead-time figure, and both decline that framing
  explicitly — individual flow metrics are a well-known way to make a Kanban
  rollout an instrument of performance management, which ends the honest
  reporting the rest of the method depends on.
- **No stage writes anything to Jira.** The flow designs a Kanban system; it
  does not configure one. Board configuration is a human act after Stage 08,
  deliberately outside this flow's boundary.

## Layer-3 inventory

**Existing skills to reference:**

- `jira-portfolio-ingest` (`produced-skills/`) — Stage 01's board binding. It
  already binds live Jira or an export, emits one normalized item set with a
  field-availability report, screens data class before typing further, and
  halts rather than auto-accepting a field map. Reused as-is.
- `provenance-stamper` (verified) — stamps and validates frontmatter on every
  artifact a run produces.
- `contract-reviewer` (verified) — pre-reviews this flowspace's own stage
  contracts before staging for the gate.

**Existing skills deliberately *not* reused** — named here so the collision
question is settled in the record rather than re-asked:

- `portfolio-profiler` — profiles a backlog's *current state* for triage:
  status/assignee/priority distributions, age ranking, field completion. Its
  unit is the item and it is point-in-time. `demand-profiler` (Stage 03) is
  longitudinal and its unit is the work item *type*. Adjacent, not
  overlapping; both briefs state the boundary in both directions.
- `closure-scorer`, `objective-keyword-mapper`, `disposition-packet-builder` —
  the `portfolio-rationalization` scoring chain. That flow decides which
  *items* deserve scrutiny; this flow designs the *system* those items flow
  through. Different unit of analysis entirely.
- `ai-refinement`'s pipeline (`context-elicitation`, `jira-commit`, and the
  rest) — refines and commits individual work items. This flow neither refines
  nor writes.

**Gaps — six candidate skill-primer-briefs:**

| Candidate | Capability | Stage |
|---|---|---|
| `sp-fitness-and-dissatisfaction-profiler` | Fitness-criteria elicitation plus separated internal/external dissatisfaction, each attributed to a source and linked to the criterion it threatens | 1–2 |
| `sp-demand-profiler` | Work item type discovery at a usable abstraction level; arrival rate, pattern, and variability per type | 3 |
| `sp-flow-capability-analyzer` | Lead-time distribution with percentiles, throughput, predictability, due-date performance — per type, tested against the fitness criteria | 4 |
| `sp-workflow-modeler` | Knowledge-discovery activity states, activity-vs-queue separation, commitment and delivery points | 5 |
| `sp-class-of-service-designer` | Classes of service from observed cost-of-delay shapes, with capacity allocation and per-class policy | 6 |
| `sp-kanban-system-designer` | Board columns, WIP limits, ticket design, explicit policies, cadences, metrics — each traced to its motivating evidence | 7 |

**Stage 08 is inline, by decision.** STATIK step 8 is a human negotiation whose
structure is specific to the design being socialized; there is no reusable
capability another flowspace would invoke. Its structure lives as reference
material instead.

**Reference material this flowspace must carry** (Layer-3 stable rules, not
skills): the STATIK method reference with its sources and the note that the two
operator-supplied articles were unreachable; the board-evidence requirements
with the live-vs-export-vs-conversation parity contract; the classes-of-service
and cost-of-delay model; the Kanban system design canvas; and the rollout and
socialization guide that carries Stage 08's inline structure.

## Source-repo

- **Source-repo:** the operator's internal GitLab instance repo,
  `flowspaces/statik-adoption/` — set at instantiation, sole source of truth
  for the instance.
- **External systems read:** Jira — one board, project, or filter per run,
  read-only, via the engine's native Jira capability. Confluence optionally, to
  publish the resulting system design; that write is a human act at Stage 08,
  not a flow-driven one.
- **External systems written:** none. The flow produces a design; a human
  configures the board.

## Open questions

Surfaced for the operator rather than silently decided during setup:

1. **The history delta on `jira-portfolio-ingest`.** That skill emits a
   point-in-time normalized item set. Stage 04's capability analysis needs
   status-transition *history* — timestamps for when each item entered and left
   each state — which the skill does not carry. Three options, none chosen
   here: extend `jira-portfolio-ingest` with an optional history mode (changes
   a promoted skill that another flowspace depends on); have
   `flow-capability-analyzer` request history itself (splits ingest across two
   skills); or accept the degrade path permanently and derive capability from
   created/resolved dates only (loses per-state residency, which is what makes
   a WIP limit defensible). `flow-capability-analyzer` declares history as an
   input requirement with a stated degrade path, so the flow runs either way,
   but the choice is an operator call.
2. **What counts as sufficient board history to claim an evidence-grounded
   demand or capability analysis.** The design asserts a floor — a full
   demand-arrival cycle, with a stated preference for at least 30 completed
   items per work item type before a lead-time distribution is reported as a
   distribution rather than as a list of observations. That floor is reasoned,
   not empirically calibrated against this operator's boards, and it is the
   kind of number that quietly becomes policy. Operator ratification before the
   first live run.
3. **Whether capacity allocation percentages are proposed at all.** Stage 06
   can propose starting allocations per class of service, and the literature
   offers conventional figures (fixed-date around 20%, intangible 10–20%). The
   risk is that a proposed number is adopted as an answer when the whole point
   of STATIK is deriving it from this service's own demand. Current design:
   propose only where Stage 03's measured demand mix supports it, cite that
   mix, and state the convention separately as context rather than as a
   recommendation. Operator confirms this is the right balance.
4. **Whether the flow should ever write to Jira.** Read-only by decision. If a
   later cycle wants the designed board actually configured — columns created,
   WIP limits set, a ticket template applied — that is a new skill and a Stage
   08 branch, not a tweak. Recorded so the boundary is a decision rather than
   an omission.
5. **Multi-service boards.** The design requires one service per run and makes
   Stage 01 halt when the bound board serves several. Whether the more common
   real case is instead "one board, several services, and no clean way to
   separate them" — which would need a service-separation step rather than a
   halt — is unresolved and depends on the operator's actual board estate.
6. **The two blocked source articles** (see the triage decision log). If their
   text can be supplied, it enters as foreign material through the intake
   vetting checklist and may revise Stage 08 in particular.
