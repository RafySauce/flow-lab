---
id: decision-2026-10-21-source-repo-protocol-rename-and-citation-sweep
title: "Decision Log — Source-Repo Protocol Rename and Citation Sweep"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-21
updated: 2026-10-21
owner: operator
source: human+ai
data-class: public
related:
  - "[[source-repo-protocol]]"
  - "[[engine-handoff-contract]]"
  - "[[2026-10-21-engine-handoff-contract-and-published-copies]]"
---

# Decision Log — 2026-10-21 — Source-Repo Protocol Rename and Citation Sweep

**What was decided:** `methodology/mirroring-protocol.md` is renamed
`methodology/source-repo-protocol.md` (`id` `source-repo-protocol`, version
3.0 → 3.1, section numbers unchanged), and the citing documents are swept to
match.

**By whom:** agent, on the operator's explicit instruction, working from the
operator's cleanup handoff. The operator chose: rename, log pure path and
section-number fixes as one mechanical correction, and run the full pass.

## Decisions and alternatives

1. **Rename.** The old name described machinery retired in 2.0. *Alternative
   considered:* keep the historical name (rejected by the operator).
2. **One mechanical-correction entry for path and section-number fixes.**
   These files keep their `truth-level` and version: every `mirroring-protocol`
   → `source-repo-protocol` path/id change, and every "handoff shape (§5)" →
   §4. The four HUBs are already `to-review`; their Surfaces wording was
   corrected without a version bump, so the `ai-refinement` 1.26 version note
   in protocol §6 still matches the source.
3. **Content rewrites are real revisions and drop to `to-review`.** Where a
   document described retired machinery (structure mapping, sync, drift
   check, "mirror"), it was rewritten to the source-repo / published-copy
   model and bumped. Dropped from `verified`: both Confluence instantiation
   guides; `documentation-standards`, `doc-type-registry`,
   `collaborative-sections-protocol`, `custody-model` (documentarian
   references); skills `bulk-child-creation`, `provenance-stamper`,
   `servicenow-ticket-ingest`, `confluence-page-commit`; and the
   `sp-servicenow-ticket-ingest` brief.
4. **Decision logs keep the old name.** They are append-only records of what
   was true when written (`governance-and-audit.md` §7). Their
   `[[mirroring-protocol]]` links and path citations are deliberately left.
   The frontmatter schema has no `aliases` field, so those wikilinks no longer
   resolve.
5. **Handoff citations moved §5 → §4.** Where the receiver is blind to the
   source-repo (Rovo committing to Confluence), the citation also points to the
   commit packet in `engine-handoff-contract.md`.

6. **Confluence provenance label (operator-specified).** Rovo stamps each
   Confluence page it commits with `<flow>-flow-v<version>` (for
   `documentarian`, `documentarian-flow-v<version>`), the same way
   `jira-commit` stamps `refine-ai-flow-v<version>`: the version is the
   producing flow's `HUB.md` `artifact-version`, not the committing skill's.
   Applied on create and update; an update replaces the earlier
   `<flow>-flow-v*` label so a page carries one; shown in the preview with its
   meaning (AI-produced, pending team review, removed by the team once
   reviewed). In a packet run the version comes from the packet header.
   Specified in `confluence-page-commit` 1.1, documentarian Stage 06,
   `documentation-standards` 1.1, and the documentarian commit packet 1.1. It
   replaces the `src-human-ai` / `dc-internal` / truth-level labels, which
   belonged to the retired mapping. *Open:* whether the tenant accepts a `.`
   in labels; fallback `v1-3`, recorded in the instantiated guide.
   *Maintenance coupling (as for Jira):* a `HUB.md` version bump changes the
   label value, so published copies and packets must carry the new version.
7. **Rovo leaves `provenance-stamper`.** With the page-property mapping gone,
   Rovo's only provenance duty is the label above, owned by
   `confluence-page-commit`. The stamper's engines narrow to Copilot, and its
   Confluence batch-check trigger and page-property clause are removed.
8. **Second batch: "mirror" terminology swept, meaning unchanged.** In stage
   contexts (`documentarian` 04, 05, 07, `accomplishments-digest` 06 and its
   template, the `documentarian` HUB stage table), skills `contract-reviewer`,
   `doc-custodian`, `doc-standards-validator`, `sad-diagram-maintainer`, and
   their starter briefs, "mirror" now reads source-repo and "Confluence page
   tree" reads published Confluence copy. Logged as mechanical corrections:
   `truth-level` unchanged. In `sp-mirror-drift-checker` the §4 cites are marked
   old §4, retired in 2.0; `sp-provenance-stamper` carries a superseded-in-part
   note. Intentionally left: historical changelog and decision-log mentions.

## Judgment calls the operator should check

- **HUB Surfaces.** "Primary: Confluence" became "Deliverable destination"
  and/or "Published copy (interim)", depending on the flow. For
  `accomplishments-digest` and `documentarian`, the Confluence tree is
  treated as both the destination for outputs and the Rovo-readable copy.
- **`custody-model` doc registry.** It lived "in Confluence (primary) and
  mirrored". It now says only that it lives in the documentation space as an
  external-system surface. Where its authoritative record lives is not
  decided here.
- **ServiceNow wording.** "Already sanctioned as a read target" became "an
  external system skills may read from in principle", which is all §2 says.

## Not done in this pass

- Publishing `ai-refinement` 1.26 to the static and Confluence copies and
  updating the protocol §6 version note; the on-engine runs (which should now
  include checking the Confluence label lands); the `documentarian` Stage 02
  boundary decision; confirming the tenant's label character rules. All remain
  operator tasks.
