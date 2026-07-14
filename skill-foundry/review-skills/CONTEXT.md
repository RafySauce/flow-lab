# Review — Skills (STAGED FOR THE HUMAN GATE)

Finished builds awaiting quick human review and promotion. When the
skill-foundry completes a spec + adapters and its agent-side pre-checks, it
moves the skill folder (`<skill-slug>/SKILL.md` + `adapters/`) here from
`../backlog-skill-starters/` — at `truth-level: to-review`, never higher.
Staging here is the one queue move the foundry makes itself: it says "built,
pre-checked, ready for your review," so the operator finds review-ready work
without digging through the backlog. The primer brief (`sp-<slug>.md`) stays
in the backlog as the intake record.

Everything leaves this folder by a human hand, one of two ways:

- **Promoted** — the operator confirms the five-point review gate
  (`../foundry-spec.md` §5, including the live test per adapter), stamps
  `truth-level: verified`, records the review evidence as a decision-log entry
  per `methodology/governance-and-audit.md` §4, and moves the skill to
  `../../produced-skills/`.
- **Returned** — back to `../backlog-skill-starters/` with findings for rework
  (or dropped, with a logged reason).

The foundry never moves anything *out* of this folder.
