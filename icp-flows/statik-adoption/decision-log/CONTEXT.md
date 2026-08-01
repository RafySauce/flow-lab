# Decision Log — STATIK Adoption (instance)

This flowspace's own logged calls, as `YYYY-MM-DD-<slug>.md` entries per
`methodology/governance-and-audit.md`.

Empty in this public design copy — it holds no run history, because runs happen
in the instance (`methodology/mirroring-protocol.md`). Build-time decisions about
this flowspace's *design* live in the foundry's log, not here:
`flow-foundry/decision-log/2026-08-01-statik-adoption-triage-and-scaffold.md`.

In an instance, each run writes here. What a run is expected to record:

| Entry | Written by | Contents |
|---|---|---|
| Service frame and binding | Stage 01 | Service name, customer groups with recipient/dependant tags, source mode, JQL/filter verbatim where live, item count, field map, history-availability finding, data-class screen result, and the mode declaration per STATIK step |
| Dissatisfaction record | Stage 02 | Which customer groups were asked, which confirmed their own entries, which were unreachable and why, fitness-criteria amendments, out-of-scope routing, unresolved discrepancies |
| Demand record | Stage 03 | Ratified type count, the abstraction level chosen and the alternatives shown, every type marked `below floor` or `unmeasured`, issue-type disagreements accepted or rejected |
| Capability record | Stage 04 | Measurement basis used, observation window, every `unavailable` section with its cause, split candidates raised |
| Workflow record | Stage 05 | Ratified commitment and delivery points, activity/queue marks, whether a recomputation loop-back was triggered, board disagreements accepted or rejected |
| Class record | Stage 06 | Ratified class set, every canonical class omitted with its reason, whether capacity allocation was proposed or withheld and on what evidence |
| Design record | Stage 07 | Every WIP limit marked `starting point` rather than derived, every element flagged `convention — no evidence trace`, every unaddressed dissatisfaction accepted as such |
| Agreement record | Stage 08 | Per-group agreement-test results, every interest objection escalated and how the owner decided it, named risks with owners, the agreed re-run trigger |
| Loop-back record | Any stage | Which stage looped back to which, what triggered it, and which outputs were superseded — the superseded version stays in the record with its reason |
| Verify results | Every stage | One line per stage's cross-stage trace check |

Two instantiation-time decisions also belong here, written once rather than
per run:

1. **The sufficiency floors** (`reference/board-evidence-requirements.md` §3) —
   ratified or amended against this operator's actual boards. They are reasoned
   defaults, not calibrated figures, and they become policy the moment a run
   uses them.
2. **The capacity-allocation stance** (`reference/classes-of-service-model.md`) —
   whether Stage 06 keeps the conservative rule (propose only where measured
   demand supports it) or offers conventional figures as a starting point.

The history resolution (`reference/board-evidence-requirements.md` §4) is no
longer an instantiation-time choice — resolved at design time 2026-08-01 (the
degrade path is permanent); see `HUB.md`'s Known gaps.
