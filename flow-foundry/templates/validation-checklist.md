# Flowspace Validation Checklist

Run at promotion time (`to-review` → `verified`). All three gates pass, or the flowspace stays `to-review`. The completed checklist itself becomes the promotion's decision-log entry — reviewer and date at the top.

**Reviewer:** ______  **Date:** ______  **Flowspace:** ______

## Gate 1 — Structural completeness

- [ ] `HUB.md` present with valid provenance frontmatter (`type: flowspace`, `owner` set, `data-class` set)
- [ ] Stage table matches stage folders one-for-one (count, order, names)
- [ ] Stage Flow Diagram present, matches the stage table one-for-one, and follows `references/flow-diagram-guide.md` (house palette, flat chain unless a documented band split)
- [ ] Diagram rendering confirmed on GitLab (view the rendered `.md`, not the diff) and on Confluence (macro installed in the target space, or the page notes "diagram: see mirror")
- [ ] Every stage has a `CONTEXT.md` with all six fields populated — no placeholder text, no template remnants
- [ ] Review intensity set per stage; first/last stages deviate from `heavy` only with a stated reason
- [ ] Data boundary set per stage and consistent with the employer sanctioned-tool matrix
- [ ] Surfaces declared (Confluence primary + mirror path); if instantiated, mirror drift check run and clean

## Gate 2 — Layer-3 status declared

- [ ] Every stage explicitly one of: referenced skill (id resolves), inlined one-off, or flagged gap (skill-primer-brief id exists in the skill-foundry backlog)
- [ ] `HUB.md` "Known gaps" section lists every flagged gap

## Gate 3 — Human dry-run

Walk the contracts in order and confirm:

- [ ] Inputs are concretely scoped (no "whatever the previous stage produces")
- [ ] Process is actionable (verbs, not descriptions of outputs)
- [ ] Outputs are specific enough that the next stage's Inputs could be written from them without a conversation
- [ ] Verify is a real cross-stage trace check (names two stages, an artifact, and a property)
- [ ] Review fields name a real accountable human per stage
- [ ] The whole flow could be run tomorrow by someone who wasn't in the design conversation

**Result:** ☐ Promote to `verified`  ☐ Return with findings: ______
