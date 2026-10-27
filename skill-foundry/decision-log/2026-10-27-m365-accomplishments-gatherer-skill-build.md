---
id: decision-2026-10-27-m365-accomplishments-gatherer-skill-build
title: "Decision Log — m365-accomplishments-gatherer Skill Build"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-27
updated: 2026-10-27
owner: operator
source: human+ai
data-class: public
related:
  - "[[m365-accomplishments-gatherer]]"
  - "[[sp-m365-accomplishments-gatherer]]"
  - "[[doc-evidence-gatherer]]"
---

# Decision Log — 2026-10-27 — m365-accomplishments-gatherer Skill Build

**What was decided:** build `m365-accomplishments-gatherer` from its primer
brief and stage it in `review-skills/m365-accomplishments-gatherer/` at
`truth-level: to-review`. **By whom:** agent, on the operator's explicit
go-ahead to build the five accomplishments-digest 2.0 briefs. **Triage:**
skill-primer-brief, clean path; the brief is transcribed, not re-explored.
The brief stays in the backlog as the intake record.

1. **Reuse, not widening.** The scoped sweep, strictest mail/chat screen, and
   halt rule come from `doc-evidence-gatherer`; that skill was not edited and
   its "not an accomplishments gatherer" boundary is restated here from the
   other side.
2. **Declared skip and paste path are distinct.** Graph unreachable yields the
   one-line skip (brief's definition of done). A user pasting material is
   handled as a labeled reduced-input path, following the `START-HERE.md`
   degrade pattern, so a chat session still gets useful output without
   claiming a search ran.
3. **Filters before content.** Exclusions are applied as search filters; only
   counts survive. A filter miss is treated as a failure to report, not
   something to silently clean up.
4. **Ownership and resolution tightened.** CC, forward, or attendance alone
   never counts; this guards the brief's named failure modes.
5. **Catalog and stage wiring not touched.** Cataloging is a promotion-time
   act; Stage 4's `Layer-3: TBD` line and `produced-skills/CONTEXT.md` are
   left for the operator.

## Five-point gate — status

Not run; the gate is the operator's. Owed: spec review (diagram matches Method
one-for-one), live test on a Graph-capable Copilot engine with synthetic data
against the eight review criteria, trigger check (including the
`doc-evidence-gatherer` near-miss), boundary/collision check against
`doc-evidence-gatherer`, and a recorded review entry. Nothing has run on-engine.
