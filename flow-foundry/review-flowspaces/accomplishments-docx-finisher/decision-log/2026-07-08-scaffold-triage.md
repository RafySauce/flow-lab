---
id: decision-2026-07-08-accomplishments-docx-finisher-scaffold-triage
title: "Decision Log — Accomplishments Docx Finisher Scaffold"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-08
updated: 2026-07-08
owner: operator
source: human+ai
data-class: public
related: ["[[fp-accomplishments-docx-finisher]]", "[[accomplishments-digest]]"]
---

# Decision Log — 2026-07-08 — Accomplishments Docx Finisher Scaffold

**What was decided:** scaffold a new companion flowspace,
`accomplishments-docx-finisher`, as a clean-path build from
`fp-accomplishments-docx-finisher` (filed and confirmed in the same
session). **By whom:** agent, on direct operator instruction, alongside the
Stage 6 addition to `accomplishments-digest` — see that flowspace's own
`decision-log/2026-07-08-copilot-handoff-revision.md` for the paired
rationale (why two flowspaces, not one). **What it affects:** new flowspace
staged here at `to-review`; two skill-primer-briefs
(`sp-repo-context-enricher`, `sp-accomplishments-docx-stylizer`) filed to
`skill-foundry/backlog-skill-starters/`.

## Why this flowspace has no independent entry point

Every other flowspace in this repo (`ai-refinement`, `accomplishments-digest`
itself) starts on a human trigger phrase. This one deliberately doesn't — its
Stage 1 Inputs are scoped entirely to a handoff file, and its `HUB.md`
states plainly it never starts on its own. This is a genuine structural
departure worth flagging for the operator's dry-run: confirm that a
flowspace whose only trigger is another flowspace's optional stage is an
acceptable shape, or whether it should instead be folded back as stages 6–8
of the source flow after all (rejected above, but worth the operator's own
look before promotion).

## Decisions and alternatives

1. **Terminal artifact is a file, not a Confluence page.** Every other
   flowspace here ends with a publish-to-Confluence step; this one ends with
   sharing a `.docx` directly. `HUB.md`'s Surfaces section states this
   explicitly rather than forcing the file into a Confluence-page pattern
   that doesn't fit.
2. **No independent data profile beyond what the handoff authorizes.** The
   flowspace's own Layer-3 inventory and both stage contracts repeatedly
   tie back to "the handoff's authorized scope" rather than granting this
   flow any standing repo access of its own — deliberate, since an
   always-on repo-access grant would outlive any single run and become a
   standing risk the handoff mechanism is specifically designed to avoid.

## Assumption (operator to confirm or amend)

- **J1 — one companion run per source-flow Stage-6 firing, always paired.**
  The design assumes a strict 1:1 pairing (one `accomplishments-digest` run
  → at most one `accomplishments-docx-finisher` run). Amendment path: if
  engineers want to re-run styling against an updated house template without
  re-running the whole source flow, that's a new trigger condition ("re-style
  an existing handoff") this design doesn't yet support — flag as a future
  revision if it comes up in practice, not the current build.
