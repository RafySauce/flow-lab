---
id: documentarian-stage-07
title: "Stage 07 — Custody & Close"
type: stage-context
stage: 7
review-intensity: heavy
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related:
  - "[[documentarian]]"
  - "[[custody-model]]"
  - "[[sp-doc-custodian]]"
---

# Stage 07 — Custody & Close

## Inputs

| Input | Source | Required |
|---|---|---|
| Committed page URLs + labels/properties for every work-order line committed this job | Stage 06 | Yes |
| Confirmed doc work order (including archive-proposal lines and struck lines) | Stage 03 | Yes |
| Audit report preamble (tree-audit jobs) | Stage 03 | If applicable |
| Recorded open-section waivers | Stage 06 | If applicable |
| Doc-registry index (current state) | `../reference/custody-model.md` → registry location set at instantiation | Yes |
| Per-item archive confirmations | User | If archive lines exist |

## Process

`Layer-3: TBD — skill-primer-brief filed (sp-doc-custodian). The
archive-confirmation dialogue (step 3) is inline — the judgment protocol is
this flowspace's own. provenance-stamper (verified, produced-skills/) is
referenced for stamping any run artifacts landing in the git mirror.`

Runs once per job, after the Band ③ loop drains. This stage is the seam
where standing agent-custodians eventually attach — its contract is written
so a scheduled custodial run can execute it without a preceding Bands ②–③
authoring pass (registry upkeep and review scheduling stand alone).

1. **Registry bookkeeping** — update the doc-registry index per
   `../reference/custody-model.md`: one row per document touched this job
   (id, doc type, surface, owner, last-verified date, review-by date,
   status). New documents get rows; updated documents get refreshed
   last-verified and review-by dates; waived open sections are noted on the
   row until resolved.
2. **Freshness stamping** — set each committed page's review-by page property
   per its doc type's cadence in the registry (the custody model defines the
   cadences). A document with waived open sections gets a shortened
   review-by, so the open sections resurface instead of fossilizing.
3. **Archive execution — per-item human confirmation, no exception** — for
   each archive line in the work order: present the page, the staleness
   evidence from the audit/dossier, and what links to it; obtain an explicit
   per-item confirmation; then archive per the tenant's confirmed mechanism
   (archive space, archive label, or native archiving — fixed at
   instantiation per the custody model). **Archive, never delete.** A
   declined confirmation converts the line to a registry note
   (`archive-declined`, with date) rather than silently vanishing.
4. **Custody scheduling** — record the next custody review date for the
   touched tree/space (the custody model's cadence), so the next tree-audit
   job has a due date rather than depending on someone remembering.
5. **Session close** — produce the job summary: work-order lines committed /
   waived / struck, archive actions taken / declined, registry rows touched,
   open sections outstanding with owners, handoff packages produced. The
   summary is the run's record for the decision log.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Updated doc-registry index rows | Future runs, custodial audits | per the custody-model row shape |
| Review-by page properties set | Confluence pages (custody metadata) | page properties |
| Archive actions record (executed / declined, per item, with confirmations) | Run decision log, audit | list |
| Next custody review date for the touched tree | Future tree-audit trigger | date + scope |
| Job summary | User / audit | structured summary |

## Verify

Cross-stage trace: every page URL Stage 06 committed this job has a
corresponding registry row with a review-by date, and every archive action
executed has a matching per-item user confirmation recorded — count them:
committed pages = touched registry rows (for this job's lines); archives
executed = archive confirmations. The failures these catch are committed
documents falling outside custody (unstamped, untracked — the exact failure
this flow exists to prevent) and an archive without its confirmation.
Running these checks leaves a one-line result in the run's decision log.

- [ ] Every Stage 06 committed page has a registry row (new or refreshed)
- [ ] Every registry row touched this job carries a review-by date per its
      type's cadence (shortened where open sections were waived)
- [ ] Every executed archive has a recorded per-item confirmation; declined
      archives converted to `archive-declined` registry notes
- [ ] Nothing was deleted
- [ ] Next custody review date recorded for the touched scope
- [ ] Job summary produced and matches the work order line-for-line
      (committed / waived / struck accounted for)

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** heavy — last stage per the U-curve default, and
  independently: archive and lifecycle calls are judgment about what the
  organization keeps relying on, not mechanics; this is also the boundary a
  future agent-custodian operates at, so its review discipline is the
  precedent that mode inherits.
- **Evidence:** the job summary, the archive-confirmation records, and the
  registry rows cited in the run's decision log entry.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo — registry rows, page
  properties, and archive actions are all Atlassian-side writes.
- Archive actions move content within the tenant; nothing leaves the
  platform, and nothing is destroyed.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
