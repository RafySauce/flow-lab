---
id: decision-2026-07-14-accomplishments-digest-skill-batch
title: "Decision Log — Accomplishments Digest / Docx Finisher Skill Batch Build"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-14
updated: 2026-07-14
owner: operator
source: human+ai
data-class: public
related:
  - "[[sp-jira-accomplishments-gatherer]]"
  - "[[sp-confluence-contribution-gatherer]]"
  - "[[sp-accomplishments-drafter]]"
  - "[[sp-repo-context-enricher]]"
  - "[[sp-accomplishments-docx-stylizer]]"
  - "[[accomplishments-digest]]"
  - "[[accomplishments-docx-finisher]]"
---

# Decision Log — 2026-07-14 — Accomplishments Digest / Docx Finisher Skill Batch Build

**What was decided:** author all five backlog starters filed from the two
performance-review flowspaces' Layer-3 triage — `jira-accomplishments-
gatherer`, `confluence-contribution-gatherer`, `accomplishments-drafter`
(from `accomplishments-digest`), and `repo-context-enricher`,
`accomplishments-docx-stylizer` (from `accomplishments-docx-finisher`) —
each as an engine-neutral `SKILL.md` plus adapters, staged in
`review-skills/` at `truth-level: to-review`. **By whom:** agent, on
operator instruction ("let's build the skills then test. then work through
the open items"). **What it affects:** five new folders under
`review-skills/` (`jira-accomplishments-gatherer/`,
`confluence-contribution-gatherer/`, `accomplishments-drafter/`,
`repo-context-enricher/`, `accomplishments-docx-stylizer/`); the five `sp-*`
primer briefs stay unchanged in the backlog as intake records. Nothing
promoted, nothing moved to `../../produced-skills/`, nothing deployed.

**Intake path:** clean for all five — each arrives from an `sp-*` primer
brief already sitting `to-review` in the backlog, filed by the flow-foundry
during flowspace scaffolding (see
`2026-07-08-accomplishments-digest-gap-briefs.md` and
`2026-07-08-docx-finisher-gap-briefs.md`). No foreign material, no vetting
checklist run.

**Why all five in one batch, not built incrementally as each flowspace
reaches its stage:** all five are demand-loop closures for the same
performance-review pipeline the operator is actively completing; building
them together let cross-digest consistency get checked directly (see
below) rather than assumed across separate sessions.

## Notable calls

- **Adapter coverage split by data-access need, not by convenience.**
  `jira-accomplishments-gatherer` and `confluence-contribution-gatherer` get
  both adapters (Rovo native-first, Copilot via the workspace's sanctioned
  Jira/Confluence connector as fallback) — same pattern as the already-
  produced `jira-commit` skill, since both briefs leave the door open to a
  sanctioned Copilot-side integration pending confirmation at instantiation.
  `accomplishments-drafter` gets both adapters per its brief's explicit
  "either engine is fine" (pure synthesis, no native-access constraint).
  `repo-context-enricher` and `accomplishments-docx-stylizer` get **Copilot
  only, no Rovo adapter** — both briefs state Copilot as the reason their
  stage exists at all (repository/file access Rovo doesn't have in this
  pairing), so a Rovo adapter would have no point of use, mirroring the
  `contract-reviewer` precedent's "don't build ahead of demand" call at
  adapter granularity (`2026-07-07-foundry-support-skill-batch.md`).
- **Cross-digest initiative-naming consistency made explicit.** The Jira and
  Confluence gatherers' specs both instruct grouping by the same
  working-area names where an initiative spans both platforms (e.g.
  "Checkout reliability"), so `accomplishments-drafter` can merge under one
  theme heading at Stage 4 rather than needing its own reconciliation pass —
  this wasn't spelled out in either brief individually but falls out of
  reading both alongside the drafter's brief together.
- **Buried-exclusion enforcement widened at the drafter.** The
  `accomplishments-drafter` brief's known failure mode — an excluded item
  resurfacing from a ticket/page's supporting detail rather than its
  headline — is written into Method step 6 and Review criterion 5 as a
  full-draft scan, not a headline-only check; this is the spec's answer to
  the brief's own stated risk, not new scope.
- Boundary/collision first pass against the seven already-produced skills
  (five `ai-refinement` skills, `contract-reviewer`, `provenance-stamper`):
  no territory overlap — those operate on work-item/foundry-artifact
  content, these five on Jira/Confluence gathering and accomplishments-
  document synthesis/styling. Among the five themselves: disjoint by
  construction (two platform-specific gatherers, one synthesis-only
  drafter, one repo-enrichment stage, one formatting-only stylizer). Formal
  collision check re-runs at the five-point promotion gate; pre-run
  evidence in the companion entry,
  `2026-07-14-accomplishments-digest-skill-gate-prerun.md`.

**Next:** operator review per `foundry-spec.md` §5 (see the companion
gate-pre-run entry for what's already checked agent-side and what remains).
