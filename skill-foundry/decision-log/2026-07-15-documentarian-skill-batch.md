---
id: decision-2026-07-15-documentarian-skill-batch
title: "Decision Log — Documentarian Skill Batch Build"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
data-class: public
related:
  - "[[sp-doc-evidence-gatherer]]"
  - "[[sp-doc-planner]]"
  - "[[sp-doc-drafter]]"
  - "[[sp-sad-diagram-maintainer]]"
  - "[[sp-doc-standards-validator]]"
  - "[[sp-confluence-page-commit]]"
  - "[[sp-doc-custodian]]"
  - "[[documentarian]]"
---

# Decision Log — 2026-07-15 — Documentarian Skill Batch Build

**What was decided:** author all seven buildable backlog starters filed
from the documentarian flowspace's Layer-3 scaffold triage —
`doc-evidence-gatherer`, `doc-planner`, `doc-drafter`,
`sad-diagram-maintainer`, `doc-standards-validator`,
`confluence-page-commit`, `doc-custodian` — each as an engine-neutral
`SKILL.md` plus adapters, staged in `review-skills/` at
`truth-level: to-review`. **By whom:** agent, on operator instruction
("Let's build the remaining skills in the backlog"). **What it affects:**
seven new folders under `review-skills/`; the seven `sp-*` primer briefs
stay unchanged in the backlog as intake records. Nothing promoted, nothing
moved to `../../produced-skills/`, nothing deployed.

**Intake path:** clean for all seven — each arrives from an `sp-*` primer
brief already sitting `to-review` in the backlog, filed by the flow-foundry
during documentarian scaffolding
(`flow-foundry/review-flowspaces/documentarian/decision-log/2026-07-15-scaffold-triage.md`).
No foreign material, no vetting checklist run.

**What was NOT built, and why — three backlog starters excluded:**

- `sp-intake-triage-assistant` — `status: dead`, dropped 2026-07-07 as not
  skill-worthy at current volume
  (`2026-07-07-skill-starter-triage-drop.md`); kept in the backlog for
  record per governance §7. The operator's "remaining skills" instruction
  is read as the buildable backlog, not as a re-file of a logged drop.
- `sp-mirror-drift-checker` — `status: dead`, dropped 2026-07-07 as
  premature (no live Confluence⇄git mirror deployed); same entry, same
  reading. Re-files when the dual-surface deployment is real.
- `sp-servicenow-kb-commit` — living but **deferred at filing** by its own
  header ("do not build yet"): no sanctioned ServiceNow integration exists,
  and its stated prerequisites (sanctioned integration confirmed;
  `kb-article` field mapping ratified; `confluence-page-commit` built AND
  verified) are not met — the third is only now staged `to-review`.
  Building it would override a deliberate deferral without the operator
  lifting it.

## Notable calls

- **`sad-diagram-maintainer` built standalone — the brief's flagged merge
  into `doc-drafter` declined.** The brief filed it separately but told the
  foundry to decide at build time. Reasons against the merge: the two
  skills' quality bars are disjoint (the drafter's defining failure mode is
  a planned open section filled with fluent prose; the maintainer's are
  byte-preservation of untouched source, render-drift detection, and a
  hard stop on non-text formats), the engine emphasis differs (maintainer
  is Copilot-primary on mirror-side sources), and the boundary between
  prose sections and diagram sources of the same `sad-update` line is
  crisp enough to declare on both sides — house boundary discipline favors
  two skills with named borders over one spec carrying two failure-mode
  families. Both specs name each other in their boundary lists; the
  brief's "if merged" clause is moot and the brief stays open as the
  standalone build's intake record.
- **Adapter coverage split by write-path, not by convenience** (the
  `2026-07-14` batch's precedent at adapter granularity).
  `confluence-page-commit` and `doc-custodian` get **Rovo only**: every
  write they make is Atlassian-side, and the documentarian Stage 06/07
  data boundaries explicitly deny Copilot the write path
  (mirroring-protocol §5 hands off) — a Copilot adapter would have no
  point of use. The other five get both adapters; of note,
  `doc-evidence-gatherer`'s Copilot adapter is deliberately narrower than
  its spec — repo-context contribution for `sad-update` jobs only, since
  the Atlassian sweep is Rovo's per the Stage 02 boundary.
- **Boundary/collision first pass** against the thirteen produced skills:
  the nearest neighbors are the accomplishments gatherers
  (`doc-evidence-gatherer` names them as near-misses and does not overlap
  their engineer-scoped territory), `workitem-validation`
  (`doc-standards-validator` is its documentarian analog on a different
  schema family — both specs say so), `jira-commit`
  (`confluence-page-commit` transplants its commit discipline to a
  different platform and payload family), and `provenance-stamper`
  (referenced by Stages 05/07 for mirror artifacts; neither new skill
  touches frontmatter). Among the seven themselves: disjoint by stage and
  by artifact (dossier → work order → draft/diagram → findings report →
  committed page → registry rows); the one shared trigger surface —
  Stage 04 `sad-update` lines — is split explicitly (prose vs.
  diagram sources) in both specs' boundary lists. Formal collision check
  re-runs at the five-point promotion gate; pre-run evidence in the
  companion entry, `2026-07-15-documentarian-skill-gate-prerun.md`.

**Next:** operator review per `foundry-spec.md` §5 (see the companion
gate-pre-run entry for what's already checked agent-side and what remains).
