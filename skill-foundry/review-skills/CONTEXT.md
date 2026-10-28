# Review — Skills (STAGED FOR THE HUMAN GATE)

Finished builds awaiting quick human review and promotion. When the
skill-foundry completes a spec and its agent-side pre-checks, it
moves the skill folder (`<skill-slug>/SKILL.md`) here from
`../backlog-skill-starters/` — at `truth-level: to-review`, never higher.
Staging here is the one queue move the foundry makes itself: it says "built,
pre-checked, ready for your review," so the operator finds review-ready work
without digging through the backlog. The primer brief (`sp-<slug>.md`) stays
in the backlog as the intake record.

Everything leaves this folder by a human hand, one of two ways:

- **Promoted** — the operator confirms the five-point review gate
  (`../foundry-spec.md` §4, including the live test on the target engine), stamps
  `truth-level: verified`, records the review evidence as a decision-log entry
  per `methodology/governance-and-audit.md` §4, and moves the skill to
  `../../produced-skills/`.
- **Returned** — back to `../backlog-skill-starters/` with findings for rework
  (or dropped, with a logged reason).

The foundry never moves anything *out* of this folder.

## Staged now

All at `truth-level: to-review`. Each `SKILL.md` frontmatter is authoritative; this list is a pointer.

| Skill | Version | Demanded by | Primer brief |
|---|---|---|---|
| [`m365-accomplishments-gatherer`](m365-accomplishments-gatherer/SKILL.md) | 1.0 | `accomplishments-digest` Stage 4 | `sp-m365-accomplishments-gatherer` |
| [`servicenow-accomplishments-gatherer`](servicenow-accomplishments-gatherer/SKILL.md) | 1.0 | `accomplishments-digest` Stage 5 | `sp-servicenow-accomplishments-gatherer` |
| [`accomplishments-correlator`](accomplishments-correlator/SKILL.md) | 1.0 | `accomplishments-digest` Stage 6 | `sp-accomplishments-correlator` |
| [`accomplishments-drafter`](accomplishments-drafter/SKILL.md) | 2.0 (revision of the verified 1.0) | `accomplishments-digest` Stage 7 | `sp-accomplishments-drafter-revision` |
| [`accomplishments-docx-stylizer`](accomplishments-docx-stylizer/SKILL.md) | 2.0 (revision of the verified 1.0) | `accomplishments-digest` Stage 9 | `sp-accomplishments-docx-stylizer-revision` |
| [`executive-slide-drafter`](executive-slide-drafter/SKILL.md) | 1.0 | `executive-slide-digest` Stage 3 | `sp-executive-slide-drafter` |
| [`executive-slide-pptx-stylizer`](executive-slide-pptx-stylizer/SKILL.md) | 1.0 | `executive-slide-digest` Stage 5 | `sp-executive-slide-pptx-stylizer` |
| [`process-decomposition`](process-decomposition/SKILL.md) | 1.0 | `ai-refinement` Stage 01 (repetitive, procedure-driven parents) | `sp-process-decomposition` |
| [`export-log`](export-log/SKILL.md) | 1.0 | Standalone — a sanitized record of a working session against any flow or skill | `sp-export-log` |
| [`cab-change-manifest`](cab-change-manifest/SKILL.md) | 1.1 | Standalone — a change manifest for an upcoming CAB from ServiceNow | `sp-cab-change-manifest` |
