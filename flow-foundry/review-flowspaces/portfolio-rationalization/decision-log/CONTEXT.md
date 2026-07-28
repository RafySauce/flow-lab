# Decision Log — Portfolio Rationalization (instance)

This flowspace's own logged calls, as `YYYY-MM-DD-<slug>.md` entries per
`methodology/governance-and-audit.md`.

Empty in this public design copy — it holds no run history, because runs happen
in the instance (`methodology/mirroring-protocol.md`). Build-time decisions
about this flowspace's *design* live in the foundry's log, not here:
`flow-foundry/decision-log/2026-07-28-portfolio-rationalization-triage-and-scaffold.md`.

In an instance, each cycle writes here. What a cycle is expected to record:

| Entry | Written by | Contents |
|---|---|---|
| Cycle scope and binding | Stage 01 | Project/space, JQL filter verbatim, source mode, item count, completion denominator, field map, degraded signals, data-class screen result |
| Lens exploration record | Stage 02 | Which lenses the operator examined and what they observed |
| Dictionary version and adjudications | Stage 03 | Dictionary id + `artifact-version`, every human-assignment adjudication, every override with its reason |
| Scoring record | Stage 04 | Model `artifact-version`, calibration status, score distribution, Stage 02 sanity-check result |
| Pack record | Stage 05 | Band counts, demotion count, packets routed per assignee |
| Cycle record | Stage 06 | Dispositions with rationales, divergences, deferrals with blockers, dictionary and calibration feedback, no-writes confirmation |
| Verify results | Every stage | One line per stage's cross-stage trace check |

Two instantiation-time decisions also belong here, written once rather than per
cycle: the **status→adjustment mapping** (`reference/close-score-model.md`
§3.5, mapping the instance's real workflow statuses onto the model's table) and
the **completion-denominator choice** (`reference/export-and-field-requirements.md`
§4, whether always-empty system columns are excluded).
