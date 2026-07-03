# Review — Flowspaces (STAGED FOR THE HUMAN GATE)

Finished builds awaiting quick human review and promotion. When the
flow-foundry completes a scaffold and its agent-side pre-checks, it moves the
flowspace here from `../backlog-flow-starters/` — at `truth-level: to-review`,
never higher. Staging here is the one queue move the foundry makes itself: it
says "built, pre-checked, ready for your review," so the operator finds
review-ready work without digging through the backlog.

Everything leaves this folder by a human hand, one of two ways:

- **Promoted** — the operator confirms the three validation gates
  (`../templates/validation-checklist.md`), stamps `truth-level: verified`,
  records the review evidence as a decision-log entry per
  `methodology/governance-and-audit.md` §4, and moves the flowspace to
  `../../icp-flows/`.
- **Returned** — back to `../backlog-flow-starters/` with findings for rework
  (or dropped, with a logged reason).

The foundry never moves anything *out* of this folder.
