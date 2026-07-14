---
id: governance-and-audit
title: "Governance and Audit — The Gates"
type: specification
artifact-version: "1.1"
status: living
truth-level: to-review
created: 2026-07-02
updated: 2026-07-03
source: human+ai
data-class: public
related: ["[[provenance-spec]]", "[[mirroring-protocol]]"]
---

# Governance and Audit

The controls that make an AI-heavy pipeline defensible: what gets checked, by whom, when, and what evidence it leaves. These are house practice, designed to be legible to workplace compliance frameworks (human-oversight expectations of the kind analyzed for EU AI Act Article 14; the "govern / map / measure / manage" framing of NIST AI RMF) without claiming conformance to any of them. **Your employer's policies override this document everywhere they touch.**

---

## 1. The standing rule

> **Every AI-generated work product is the responsibility of its human owner.** AI output is unverified by default. It becomes reliable only after a qualified human has quality-gated it (is it correct, complete, fit for purpose?) and source-reviewed it (are its claims, code, and citations actually grounded?). The structures below exist to make that review cheap, visible, and provable — not optional.

---

## 2. Gate 1 — Data classification at intake

Before any content enters an AI tool or an ICP structure:

1. Classify it (`data-class`: public / internal / confidential / restricted — or your employer's scheme).
2. Check the classification against the **sanctioned-tool matrix** — a one-page, employer-policy-derived table of which data classes may enter which tools (Rovo, Copilot, each surface). Maintain yours internally; this repo deliberately does not guess at it.
3. Stamp `data-class` in the artifact's frontmatter/page properties. Highest-classified content in the document sets the class.

A stage's **Data boundary** field (stage-contract extension) re-applies this check per stage: what class may this stage's engine see? A handoff into a stage whose boundary excludes the receiving engine is invalid.

## 3. Gate 2 — Foreign-material vetting

External starters (vendor prompts, public repos, colleagues' templates, READMEs) pass the [intake vetting checklist](../skill-foundry/templates/intake-vetting-checklist.md) before normalization: provenance, maintenance, **license/IP**, and a security read (including prompt-injection review of any instructions the material would have an agent execute). Failing material is dropped with a logged reason. Vetting is required, not optional; dropping is a normal outcome.

## 4. Gate 3 — Human verification

`truth-level: verified` is promoted only by a human, only with evidence:

- **Who** reviewed, **when**, and **what they checked** — recorded as a decision-log entry (git mirror) or a sign-off comment/property (Confluence). A Confluence version change-comment naming the reviewer is acceptable *supplementary* evidence alongside either of those (see `mirroring-protocol.md` §7), but does not by itself satisfy the rule — it still needs who/when/what-checked.
- For flowspaces: the three validation gates in `flow-foundry/foundry-spec.md` (structural completeness, Layer-3 status declared, human dry-run).
- For skills: the review checklist in `skill-foundry/foundry-spec.md`, including a live test on the target engine.
- The `Verify` field of a stage contract defines the check; **running it leaves a record** — a one-line result in the run's decision log, not a silent nod.

Agents and foundries never perform this promotion, never move artifacts to `completed-*` folders, and never mark reviews passed. If you automate everything else, do not automate this.

## 5. The decision log

Each foundry (and each instantiated flowspace) carries a `decision-log/` folder — `YYYY-MM-DD-<slug>.md`, stamped `type: decision-log`. An entry is earned by any non-obvious call:

- a triage drop and its reason,
- a security or license flag,
- a structural choice (stage added/merged, boundary redrawn),
- a verified promotion (the review evidence itself),
- a deviation from a contract mid-run and why.

Entry shape — keep it to ~10 lines: **what was decided / by whom / the alternatives considered / the reason / what it affects.** The log is the audit trail *and* the improvement corpus: a periodic read-through of accumulated entries is how the foundries themselves get revised.

## 6. AI-contribution disclosure

The `source` field (`human` / `human+ai` / `ai`) is the disclosure mechanism, stamped at authoring time and preserved through revisions. Where a deliverable leaves the ICP structure (a report shipped to stakeholders, code merged to a product repo), carry the disclosure with it in whatever form the destination supports — a footer, a PR description line, a page property. Do not strip provenance at the boundary; that is where it matters most.

## 7. Retention and supersession

- Nothing is silently deleted: retired artifacts go `status: dead`; replaced ones go `status: replaced` + `superseded-by`.
- Specs and foundries carry changelogs; version bumps are dated and reasoned.
- Decision logs are append-only.

## 8. Periodic audit pass

Quarterly (or before any formal review), run and record:

1. **Drift check** on the Confluence⇄git mirror (`mirroring-protocol.md` §4) — can be CQL-driven (`mirroring-protocol.md` §7) rather than manual page-by-page review.
2. **Gate sampling** — pick N recent `verified` artifacts; confirm each has review evidence (provenance rule 5).
3. **Classification sampling** — pick N artifacts; confirm `data-class` matches content and no boundary was crossed. CQL can surface pages missing a `data-class` label as a starting list (`mirroring-protocol.md` §7).
4. **Backlog hygiene** — starters stuck in backlogs older than a set age are re-triaged or dropped.
5. **Decision-log synthesis** — read the quarter's entries; propose foundry/spec revisions from what they teach.

The audit pass produces one decision-log entry summarizing findings and actions.

---

## Changelog

- **1.1** (2026-07-03) — Noted CQL-driven drift/classification sampling and Confluence version change-comments as supplementary (not sufficient) review evidence, per `mirroring-protocol.md` §7.
- **1.0** (2026-07-02) — Initial gates.
