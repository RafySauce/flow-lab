---
id: fp-comms-builder
title: "Flow Primer Brief — Comms Builder"
type: flow-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-11-07
updated: 2026-11-07
owner: operator
source: human+ai
data-class: public
related:
  - "[[comms-builder]]"
  - "[[executive-slide-digest]]"
  - "[[sp-comms-context-linker]]"
  - "[[sp-audience-mapper]]"
  - "[[sp-comms-plan-builder]]"
  - "[[sp-comms-drafter]]"
  - "[[sp-deck-stylizer]]"
---

# Flow Primer Brief — Comms Builder

> Intake path 4 for the flow-foundry, backfilled: this arrived as a bare
> conversation ("we need to get communications out to a specified audience
> regarding xyz"), not as a formal starter. Per `foundry-spec.md` §1 case 4
> that is workable — the nine setup questions are answered below so the
> scaffold has a real intake record behind it.

## Purpose

Save a delivery lead or service owner the hours it takes to get key
communications out to the right stakeholders — application owners, technical
owners, and business users — about changes to shared services, platform
changes, key projects, and CVE or incident response plans. The flow decides
whether the ask is a **one-off** message or a **campaign**, and produces the
matching pack: audience design, templated message drafts, links to the
source records, and — for a campaign — a comms plan with a timeline visual,
a validation tracker, and implementation meeting materials. It recurs every
time a change, project milestone, or response plan needs stakeholders told.

Changes are the first primary use case, not the only one.

## Trigger and cadence

**Trigger:** a request of the shape "we need to get communications out to
<audience> regarding <subject>", optionally with a linked change, incident,
CVE record, or Jira item.

**Cadence:** on demand. A team running a platform roadmap may run it weekly;
a single response plan runs it once and then re-runs Stage 5 for updates.

## Stage sketch

| # | Stage | What happens | Review intensity (est.) |
|---|---|---|---|
| 1 | Frame & triage | User states subject, audience in plain words, deadline, linked records. Flow proposes comms type and lane (one-off or campaign) with reasons; user steers | heavy |
| 2 | Link source records | Read-only pull of named change/incident/CVE records and Jira items: window, impact, affected services, actions. Cited, never pasted | light |
| 3 | Audience design | Segments (default: application owners, technical owners, business users), what changes for each, what each must do, channel per segment | heavy |
| 4 | Comms plan & timeline | Campaign only. Touchpoints against the key date, owners, channels, validation tracker, Mermaid gantt as rendered image + raw source | light |
| 5 | Draft messages | One draft per segment per touchpoint from the operator's template folder, or plain defaults | light |
| 6 | Meeting materials | Campaign with an implementation event only. Run-of-show, bridge agenda, roles, go/no-go checkpoints, short deck | light |
| 7 | Align & approve | User reviews the whole pack against Stage 1's framing | heavy |
| 8 | Publish & hand off | Pack delivered in chat; Rovo-bound items (Confluence plan page, Jira comment) emitted as `.md` commit packets the user pastes into Rovo; emails stay drafts | heavy |

**Lanes.** One-off: 1 → (2 if records linked) → 3 (lite) → 5 → 7 → 8.
Campaign: all eight, with 6 only when an implementation event exists.
The flow suggests a campaign for (a) large-scale changes touching many
stakeholders, (b) changes that need specific validation from application
teams, and (c) projects with many different stakeholders. The user decides.

## Data profile

Work-item and change-record content (summaries, windows, affected services,
impact statements), audience descriptions by role or group, and the user's
own framing. The instance runs at `data-class: internal`. Two boundaries:

- **Response plans (CVE, incident).** Comms carry impact, timing, and the
  actions people must take. Exploit details, configurations, IP addresses,
  and control descriptions never enter a draft; they stay in the security
  record and are linked by number only. Stage 2 may *read* records at
  `confidential`; nothing above `internal` leaves Stage 2.
- **Audiences are groups and roles, never named individuals.** Distribution
  lists and team names are fine; people's names are not carried into plans
  or drafts unless the user adds them at Stage 7.

This public design copy is `public` by construction.

## Layer-3 inventory

**Existing material reused:**

| Piece | Used at | How |
|---|---|---|
| `cab-change-manifest` (review-skills, to-review) | 2 | Pattern only: self-validated source access, cite-not-paste. Not called — it is CAB-window scoped |
| statik-adoption `reference/rollout-and-socialization-guide.md` | 3 | Per-group "what changes for you" view is the segment view's ancestor |
| ai-refinement `platform-stakeholder-register-template.md` | 3 | Grounds segments when a register exists |
| `confluence-page-commit` (produced-skills, verified) | 8 | Run by the Rovo executor from the commit packet |
| `methodology/engine-handoff-contract.md` | 8 | Commit packet shape for Rovo-bound items |
| `executive-slide-digest` (review-flowspaces, to-review) | — | Sibling. Exec status-deck asks route there |

**Gaps — five skill-primer-briefs filed:**

| Brief | Capability | Stage |
|---|---|---|
| `sp-comms-context-linker` | Pull named change/incident/CVE/Jira records into a cited context sheet, data rule enforced | 2 |
| `sp-audience-mapper` | Turn an audience description into segments with per-segment impact, action, channel | 3 |
| `sp-comms-plan-builder` | Touchpoint plan, validation tracker, Mermaid gantt colored from the design-system binding | 4 |
| `sp-comms-drafter` | Draft messages per segment per touchpoint from templates; callable standalone for a quick one-off | 5 |
| `sp-deck-stylizer` | Generalized `.pptx` stylizer driven by a design-system binding; shared with `executive-slide-digest` later | 6 |

**Deliberately not reused:** `jira-commit` (create-only; a Jira comment is a
Rovo executor action carried in the commit packet instead).

## Source-repo

The operator's internal GitLab instance, `flowspaces/comms-builder/`, set at
instantiation. External systems: ServiceNow and Jira read at Stage 2;
Confluence and Jira written only by the Rovo executor from Stage 8's packet.
Outlook drafts are created by the user. The flow sends nothing.

## Setup questionnaire answers

1. **Name + slug:** Comms Builder, `comms-builder`.
2. **Purpose:** above.
3. **Stages:** eight, designed with the operator 2026-11-06.
4. **Source-repo mapping:** above.
5. **Review intensity:** heavy at 1, 3, 7, 8; light at 2, 4, 5, 6. Stage 3 is
   heavy because who gets told what is the flow's central judgment.
6. **Data boundary:** `internal` everywhere except Stage 2 reads up to
   `confidential`. Engine: Copilot for every stage; Rovo only as the executor
   of Stage 8's packets.
7. **Layer-3 status:** above.
8. **Intake path:** clean design from this backfilled brief.
9. **Stakeholder register:** optional. Without one, Stage 3 runs ungrounded
   and asks the user directly.

## Open questions

- [NEEDS INPUT] Can Copilot in the operator's tenant render Mermaid to an
  image? If not, Stage 4 ships the raw Mermaid plus the table fallback and
  the user renders it in an approved tool.
- [NEEDS INPUT] Does the instance Confluence have a Mermaid macro?
- [NEEDS INPUT] Is there a house comms team, template set, or approval step
  for internal announcements that Stage 7 should route to?
- [NEEDS INPUT] The operator's template folder path (set in the binding
  config at instantiation).
