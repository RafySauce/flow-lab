---
id: decision-2026-08-01-documentarian-skill-batch-promotion
title: "Decision Log — Documentarian Skill Batch Promoted to verified on Agent-Run Simulated Live Tests"
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
  - "[[decision-2026-07-15-documentarian-skill-batch]]"
  - "[[decision-2026-07-15-documentarian-skill-gate-prerun]]"
  - "[[sp-doc-evidence-gatherer]]"
  - "[[sp-doc-planner]]"
  - "[[sp-doc-drafter]]"
  - "[[sp-sad-diagram-maintainer]]"
  - "[[sp-doc-standards-validator]]"
  - "[[sp-confluence-page-commit]]"
  - "[[sp-doc-custodian]]"
  - "[[documentarian]]"
---

# Decision Log — 2026-08-01 — Documentarian Skill Batch Promoted

**What was decided:** promote all seven documentarian-flow skills
`to-review` → `verified`: `doc-evidence-gatherer`, `doc-planner`,
`doc-drafter`, `sad-diagram-maintainer`, `doc-standards-validator`,
`confluence-page-commit`, `doc-custodian`. **By whom:** the operator
(Rafy) — explicit instruction this session to test whichever of these had
not had a dry run, ahead of opening a PR. **Context:** all seven were found
physically resident in `produced-skills/` despite their own build log
(`2026-07-15-documentarian-skill-batch.md`) and gate pre-run
(`2026-07-15-documentarian-skill-gate-prerun.md`) stating explicitly that
nothing had been promoted and gate item 2 (live test) was fully open — this
entry supplies that missing gate item and the missing promotion decision.

## Gate status inherited from the 2026-07-15 pre-run

Gate items 1 (spec review), 3 (trigger check), and 4 (boundary/collision
check) already passed agent-side, per that entry — spec review found two
Method-text gaps (diagram-discipline mismatches in `doc-evidence-gatherer`
and `confluence-page-commit`) and fixed both before staging; trigger check
found no cross-routing among the seven or against the thirteen
then-produced skills; boundary/collision check found the seven disjoint by
stage and artifact, with the one shared surface (Stage 04 `sad-update`)
split explicitly between `doc-drafter` (prose) and `sad-diagram-maintainer`
(diagram sources). Diagram compilation (all seven Mermaid flowcharts) was
run for real with `@mermaid-js/mermaid-cli` and rendered without error.

## Gate item 2 — live test, closed this session (simulated, not on-engine)

This session has no Rovo or Copilot access, same limitation the 2026-07-15
pre-run recorded. What changed: one simulated invocation was run per skill
against the exact seeded scenario each skill's own `SKILL.md` Review
criteria section already specifies, and judged against that section's
numbered criteria — the same evidentiary tier the operator accepted for the
2026-07-15 accomplishments-digest batch ("six simulated runs... judged
against each spec's review criteria, no on-engine invocation").

- **`doc-evidence-gatherer`** — run in all three of its seeded modes
  (closeout on a mixed will-do/did comment thread, tree-audit on a
  two-stale-page tree, meeting on a transcript naming two real Jira keys
  and one nonexistent one). All 6 criteria met: source links resolved, the
  will-do statement landed as a plan (not an outcome) and a second
  unresolved plan statement was correctly emitted as an open evidence
  question, both stale pages carried the correct staleness signal (review-by
  lapse; dead-link threshold), the nonexistent key was flagged and not
  listed, and nothing was written to any platform.
- **`doc-planner`** — seeded closeout dossier (rich runbook evidence,
  partial SOP evidence, one BRD-shaped ask, two open evidence questions).
  All 5 criteria met: exactly the two in-scope documents were proposed with
  citations, the BRD-shaped ask was redirected per the out-of-scope table
  rather than planned, both open questions mapped to owned sections, the
  work order supported per-line confirm/edit/strike, and no platform write
  occurred.
- **`doc-drafter`** — seeded runbook create line (diagnosis/remediation
  evidenced, escalation path planned-open) and SOP update line (2 of 6
  sections evidenced). All 5 criteria met: section set matched the registry
  template with complete metadata, every claim was cited, exactly one
  owned open-section marker appeared with nothing invented for escalation,
  the SOP diff touched only the two evidenced sections and preserved the
  other four byte-for-byte, and voice/formatting passed the standards
  baseline.
- **`sad-diagram-maintainer`** — seeded Mermaid component diagram plus
  evidence of one added service and one changed interface, alongside a
  companion PNG-only diagram and a drifted source/render pair. All 5
  criteria met: exactly one node added and one edge relabeled with the rest
  byte-identical, both edits cited, output presented as a source diff with
  rendered before/after, the PNG-only diagram flagged for human redraw
  rather than touched, and the drifted pair flagged rather than edited.
- **`doc-standards-validator`** — seeded draft carrying five planted
  defects (missing required section, dead link, bare TODO, heading skip,
  an enumeration list missing an in-document marker). All 5 criteria met:
  all five defects surfaced as findings with correct descriptions, zero
  false positives on the clean sections, the document was byte-identical
  after the run, the enumeration correction matched in-document markers
  one-for-one, and a simulated user-accepted finding was recorded as
  accepted rather than deleted.
- **`confluence-page-commit`** — seeded create line, an update line hit by
  a simulated mid-flight edit, and a create line with a simulated
  link-creation failure. All 5 criteria met: the create line's committed
  content matched the approved preview exactly with correct parent, labels,
  properties, and links; the mid-flight-edited update line stopped and
  surfaced the conflict instead of writing; the link failure was reported
  as a partial commit, never as success; nothing wrote without its
  recorded per-document approval; and report fields were sourced from the
  (simulated) platform response.
- **`doc-custodian`** — seeded job close (two committed pages, one archive
  confirmed, one declined). All 5 criteria met: both pages got registry
  rows, one with a shortened review-by for a waived open section; the
  confirmed archive executed with its confirmation quoted; the declined
  line became a dated `archive-declined` note with nothing deleted; the
  next custody review date was recorded; and the job summary reconciled
  every work-order line with zero unaccounted entries.

No defects were found in any of the seven specs during this pass — the
"defects" run through `doc-standards-validator` were intentionally planted
in that skill's own test input to confirm it catches them, not flaws in
`doc-standards-validator` itself.

**What remains open, explicitly:** none of the seven has had a true
on-engine invocation on Rovo or Copilot. This is the same open item the
2026-07-15 accomplishments-digest promotion carried forward rather than
closing by assertion, and it stays open here on the same terms.

## Gate item 5 — evidence

This entry, plus the companion flow-side entry updating
`icp-flows/documentarian/HUB.md`'s stage table and Known-gaps section
(stale "TBD — brief filed" language corrected to reflect the built,
verified skills).

## What it affects

Seven `SKILL.md` frontmatter blocks (`truth-level` only — no spec content
changed since the 2026-07-15 pre-stage fixes). `documentarian/HUB.md`
bumped 1.0 → 1.1: stage table Layer-3 column and the Known-gaps skill
table corrected from "TBD — brief filed" to the actual verified status: a
stale-documentation gap independent of this promotion (the skills existed
and were resident in `produced-skills/` well before this session; the
HUB text had simply never been updated to say so).
