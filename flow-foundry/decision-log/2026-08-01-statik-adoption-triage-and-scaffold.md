---
id: decision-2026-08-01-statik-adoption-triage-and-scaffold
title: "Decision — STATIK Adoption: triage, source vetting, and scaffold calls"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related:
  - "[[fp-statik-adoption]]"
  - "[[statik-adoption]]"
---

# Decision — STATIK Adoption: triage, source vetting, and scaffold calls

## Context

The operator asked for an ICP flow and associated skills implementing a
**STATIK adoption method** — STATIK being the *Systems Thinking Approach To
Introducing Kanban*, David J. Anderson's method for designing a Kanban system
for an existing service rather than imposing a template on it. The stated
grounding was "analysis of the kinds of work on the board": the flow should
derive its answers from a real Jira board where it can, and from conversation
with the user where it cannot.

Two source URLs were supplied:

- `https://aktiasolutions.com/statik-kanban-implementation-kanban-rollout/`
- `https://hjavixcs.medium.com/statik-systems-thinking-approach-to-introduce-kanban-13996dbe414a`

## Decisions

### 1. Triage: case 4 — bare conversation, not a formal starter

Per `foundry-spec.md` §1, this arrived as an operator description in
conversation, not as a filed `flow-primer-brief`. Case 4 ("bare conversation")
is workable, and the remedy is stated: run the setup questionnaire and backfill
the missing structure rather than guessing. Done —
`backlog-flow-starters/fp-statik-adoption.md` is the backfilled intake record,
and the nine questionnaire answers are visible in it.

It is **not** case 3 (not flowspace-worthy). STATIK is multi-stage by
construction, recurs per service and per re-run, and carries judgment at
several distinct boundaries — the definition of a flowspace rather than a
skill.

### 2. Source vetting: both supplied URLs were unreachable; build proceeded on
reachable equivalents

Both URLs returned **HTTP 403 at the egress proxy on CONNECT** — an
organization egress-policy denial for the hosts `aktiasolutions.com` and
`hjavixcs.medium.com`, recorded in the proxy's own failure log. This is not a
paywall, a dead link, or a retryable network fault, and per
`/root/.ccr/README.md` a policy denial is reported rather than routed around.
No content from either URL entered this build.

The method was instead reconstructed from reachable sources: Kanban
University's glossary and Fit-for-Purpose material, the David J. Anderson
School of Management writing on dissatisfaction and classes of service, and
several practitioner write-ups (Agile Velocity, Iterators, Businessmap,
VivifyScrum, Meirik, Michael Mahlberg on step 8). These agree on the canonical
step sequence, so the **structural** risk from the two blocked URLs is low.

**Residual risk, stated rather than buried:** the two blocked articles may
carry framing, worked examples, or a workshop-facilitation shape that this
build does not reflect — the Aktia piece's title in particular suggests
rollout/implementation emphasis that would bear on Stage 08. The reference
artifact `reference/statik-method-reference.md` is therefore stamped
`truth-level: to-review` with its sources named inline, and it carries an
explicit note that the two operator-supplied sources are **unread**. If the
operator can supply the article text, it enters as foreign material through
`skill-foundry/templates/intake-vetting-checklist.md` — it is not folded in
silently.

### 3. Eight stages, tracking STATIK's eight steps one-for-one

The flowspace uses one stage per STATIK step, plus intake folded into Stage 01
alongside step 1's service framing. The alternative — compressing to five or
six stages by merging demand with capability, or classes-of-service with system
design — was rejected for a specific reason: **the flow's auditability against
the published method is a feature.** A reviewer should be able to hold the
flowspace against any STATIK description and see the correspondence without
translation. Merging steps would make every future disagreement about the
method a disagreement about this flowspace's structure too.

Stage 01 absorbs the intake/source-binding work (which STATIK assumes rather
than specifies) together with step 1's fitness-for-purpose framing, because
binding the service and naming its customer are the same conversation.

### 4. Two deliberate U-curve breaks, with stated cause

The U-curve default (`icp-primer.md` §3.9) is heavy / light … light / heavy.
Two middle stages break it:

- **Stage 02 (Dissatisfaction) is heavy.** Every fitness criterion the rest of
  the flow measures against originates here. A missed source of dissatisfaction
  is not recoverable downstream — Stage 04 will faithfully measure the wrong
  thing and report a healthy system.
- **Stage 05 (Workflow Modeling) is heavy.** This is the highest-judgment
  content in the flow. The board's configured statuses are *not* the workflow —
  they are one team's historical guess at it — and the commitment point in
  particular is a judgment call that silently redefines every lead-time number
  Stage 04 produced. A wrong commitment point invalidates the capability
  analysis without any downstream stage being able to detect it.

This mirrors the precedent set by `fp-portfolio-rationalization`, whose Stage 3
breaks the same default for the same class of reason.

### 5. Board evidence proposes; humans ratify — never the reverse

The load-bearing design rule, and the reason this flow is worth building rather
than running a STATIK workshop unaided: **the Jira board is treated as evidence
about the system, not as a description of it.** Board-derived findings enter
every stage as *proposals with their derivation shown*, and a human ratifies,
amends, or rejects each one.

The failure mode this guards against is specific and, left unguarded, near
certain: a board's issue types are an administrative artifact, and mistaking
them for STATIK work item types produces a Kanban system designed around Jira's
configuration rather than around the actual demand. The same trap applies to
statuses versus knowledge-discovery activities (Stage 05) and to priority
fields versus classes of service (Stage 06). Each stage names its own version
of this trap.

### 6. Conversation-only mode is a first-class path, not a degrade

STATIK predates and does not require a ticketing system, and the flow must run
for a service with no board, a board too young to carry history, or a team
whose board does not reflect how they actually work. Conversation-only is
therefore a supported intake path declared at Stage 01 — not a fallback
triggered by failure. Stage 01's mode declaration states per STATIK step which
are evidence-grounded and which are conversation-only, and that declaration
travels with the run so no later stage silently claims empirical support it
does not have.

### 7. Layer-3: one reuse, six gaps, one inline

`jira-portfolio-ingest` (promoted, `produced-skills/`) is reused at Stage 01
for board binding. It already does exactly what is needed — bind live Jira or
an export, emit one normalized item set with a field-availability report,
screen data class before typing further, halt rather than auto-accept a field
map — and rebuilding it would be a collision.

**Named delta, not silently absorbed:** `jira-portfolio-ingest` emits a
*point-in-time* item set. STATIK's capability analysis (Stage 04) needs
*history* — status-transition timestamps — which that skill does not carry.
This is recorded as an open question in the primer brief rather than resolved
here by inventing a second ingest skill: the right answer (extend the existing
skill, or have `flow-capability-analyzer` request history itself) is an
operator call. `flow-capability-analyzer` declares history as an input
requirement with a stated degrade path, so the flow is runnable either way.

Six gaps filed as skill-primer-briefs in
`../skill-foundry/backlog-skill-starters/`:
`sp-fitness-and-dissatisfaction-profiler`, `sp-demand-profiler`,
`sp-flow-capability-analyzer`, `sp-workflow-modeler`,
`sp-class-of-service-designer`, `sp-kanban-system-designer`.

**Stage 08 (Socialization & Rollout) is deliberately inline, not a skill.**
STATIK step 8 is a human negotiation — walk each stakeholder group through the
design from their point of view, absorb objections, rework, return for
agreement. Its structure is real but is specific to *this* design being
socialized; there is no reusable capability here that another flowspace would
invoke. Per `foundry-spec.md` §4 case 2, that is an inline one-off. The
structure it needs lives as reference material
(`reference/rollout-and-socialization-guide.md`) rather than as a skill.

### 8. Collision check against the existing portfolio skills

`portfolio-profiler` and `demand-profiler` both count things on a Jira board,
and the boundary needs to be explicit or the two will drift into each other:

- `portfolio-profiler` answers **"what is in the backlog right now, and how
  well-formed is it?"** — status/assignee/priority distributions, age ranking,
  field completion. Its unit is the *item*, its purpose is triage, and it is
  point-in-time.
- `demand-profiler` answers **"what kinds of work arrive here, how often, and
  how evenly?"** — work item type discovery and arrival rate/pattern over time.
  Its unit is the *type*, its purpose is system design, and it is inherently
  longitudinal.

Both briefs state this boundary in their own words, in both directions.

### 9. Agent-side pre-checks: structural only

`foundry-spec.md` §5 stages a build once "the scaffold, Layer-3 triage, and
agent-side pre-checks are complete." What was actually checked, stated plainly so
the operator knows what the gate still has to do:

**Checked (gate 1, structural completeness — partial):**

- Stage folders match the `HUB.md` stage table one-for-one — 8 and 8.
- The Stage Flow Diagram matches the stage table one-for-one — 8 nodes, same
  order, `classDef` values copied verbatim from the house palette.
- Frontmatter present and valid on every stamped artifact; every
  `type: stage-context` carries `stage` and `review-intensity`, and each matches
  its `HUB.md` row.
- `truth-level` is `to-review` everywhere except the two decision logs (which
  record events); nothing self-declares `verified`.
- `data-class: public` throughout — no employer content entered the repo.
- Source-repo mapping declared; every reference artifact linked from `HUB.md`
  exists.

**Checked (gate 2, Layer-3 status declared):** every stage is explicitly one of
referenced skill (Stage 01), built-but-ungated skill (Stages 02–07), or inline
one-off (Stage 08).

**Not checked — outstanding for the operator:**

- **Mermaid rendering on GitLab has not been confirmed**, because this session had
  no GitLab surface. Gate 1 requires viewing the rendered `.md`, not the diff.
- **`contract-reviewer` was not run** against the eight stage contracts. They were
  authored to the populated-vs-present standard, but that is an authoring claim,
  not a review result.
- **Gate 3, the human dry-run**, is the operator's by definition — walking the
  contracts in order and confirming Inputs are concretely scoped, Process is
  actionable, Outputs are specific enough to write the next Inputs from, and each
  Verify is a real cross-stage check.

## Follow-ups for the operator

1. **`produced-skills/CONTEXT.md` has drifted.** The folder holds 25 skills;
   the "Available skills" table lists 13. Twelve promoted skills are absent
   from the catalog — including `jira-portfolio-ingest` and `portfolio-profiler`,
   which this build reuses and references. `foundry-spec.md` §5 makes updating
   that table part of promotion. Flagged, not fixed: the catalog is operator-owned.
2. **The two blocked source URLs** remain unread — see decision 2.
3. **The ingest history delta** — see decision 7.
