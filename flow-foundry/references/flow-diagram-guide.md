# Stage Flow Diagram Guide — syntax and convention

Every flowspace the foundry scaffolds carries a `## Stage Flow Diagram` section in
its `HUB.md`, placed right after the purpose paragraph and before `## Stage table`.
It's a Mermaid `flowchart LR`: one node per stage, in numeric order, chained left
to right, colored by review intensity. It is a visual complement to the Stage table,
not a replacement — the table stays the source of truth for review intensity, data
boundary, and Layer-3 status; the diagram is the at-a-glance sequence map.

This is a house practice reinstated from the homelab implementation this foundry
was ported from (see `foundry-spec.md` changelog) — the original work edition
dropped it as "diagrams optional, Confluence rendering varies." With GitLab as
the sole source of truth (`methodology/mirroring-protocol.md`), that concern is
gone entirely: **the diagram is a gate-checked requirement, and there is one
rendering surface to confirm.**

---

## Rendering — one surface

GitLab renders Mermaid natively: fenced ` ```mermaid ` blocks render in issues,
MRs, wikis, and markdown files viewed through the GitLab UI (not in raw/diff
view). No setup needed — use standard Mermaid syntax, and avoid
GitLab-unsupported Mermaid features (check GitLab's supported-diagram-types doc
if a diagram fails to render). Confirm rendering by viewing the rendered `.md`
file, not the diff.

---

## Syntax cheatsheet

Four node shapes cover nearly every flowspace:

| Shape | Syntax | Use for |
|---|---|---|
| Stadium | `Start(["label"])` | none by default — flowspaces don't have a separate trigger node; stage 1 is the entry |
| Rectangle | `S1["1. Stage Name<br/>review: <intensity>"]` | An ordinary stage |
| Diamond | `Gate{"label"}` | Reserved — flowspaces are stage sequences, not branchy; see discipline below |
| Subroutine | `Ref[/"label"/]` | A stage that hands its output to another flowspace or an external system |

Edges: `-->` for the normal path. `-.->|"label"|` (dashed, labeled) is reserved for a
loop-back — only alongside a documented band split (see below).

Multi-line node labels use `<br/>` inside the quoted string, e.g.:
`S1["1. Intake<br/>review: heavy"]`

---

## House dark palette — review-intensity colors

Every node gets a `classDef` by its **review intensity**, per the U-curve mapping
in the stage's `CONTEXT.md`:

```
classDef heavy   fill:#78350f,stroke:#fbbf24,color:#fef3c7
classDef light   fill:#1e3a8a,stroke:#60a5fa,color:#dbeafe
classDef gap     fill:#7f1d1d,stroke:#f87171,color:#fee2e2
```

| Role | Color | Meaning |
|---|---|---|
| `heavy` | amber | A judgment stage — direction-setting or final alignment (U-curve default: first and last stage) |
| `light` | blue | A constrained-execution stage |
| `gap` | rose | Layer-3 status is `TBD — brief filed`; the stage's skill doesn't exist yet |

Each value is a dark fill, a saturated mid-tone stroke, and a light near-white text
tint — the same fill/stroke/text formula the homelab source used, already known
to render well on GitLab. **Reuse these exact hex values** — don't invent new
ones per flowspace.

A stage colored `gap` also keeps whatever review-intensity color it would otherwise
have as a secondary signal isn't needed — `gap` overrides on the diagram, but the
Stage table still carries the real review intensity once the skill lands.

---

## Base shape — the flat chain (default)

Most flowspaces are purely linear with no documented sub-grouping. Default to this
shape — a flat chain, no subgraph:

```mermaid
flowchart LR
    S1["1. Stage Name<br/>review: heavy"]:::heavy --> S2["2. Stage Name<br/>review: light"]:::light
    S2 --> S3["3. Stage Name<br/>review: heavy"]:::heavy

    classDef heavy fill:#78350f,stroke:#fbbf24,color:#fef3c7
    classDef light fill:#1e3a8a,stroke:#60a5fa,color:#dbeafe
    classDef gap fill:#7f1d1d,stroke:#f87171,color:#fee2e2
```

## Stage bands — only for a genuine documented topology split

Add `subgraph` bands **only** when the flowspace's own `HUB.md` already documents a
real high-level grouping — e.g. a set-once-foundation stage separate from a
per-item pipeline. Don't invent a grouping that isn't written down; a flat chain
that matches `HUB.md` exactly beats a banded diagram that imposes structure the
flowspace doesn't actually have.

When a band is warranted:
- Title format: circled number + name, e.g. `① Foundation — built once`,
  `② Per-Item Pipeline — repeats per item`.
- Frame style (dark theme, neutral so it doesn't compete with the intensity colors
  inside it): `style <ID> fill:#0f172a,stroke:#475569,stroke-width:1px,color:#e2e8f0`
- Nodes inside a band keep their normal intensity `classDef` coloring — the band
  frame is structural, not another color signal.

## Loop annotation — only alongside a genuine documented topology split

If (and only if) bands are in use because `HUB.md` documents a set-once-foundation +
per-item-loop topology, add **one** dashed loop-back edge labeled with the restart
condition. Don't add a loop without the band that explains it.

---

## Worked example — weekly-status-report style flowspace (flat chain)

A straight 4-stage pipeline: intake, draft, review, publish. No documented
sub-grouping, so it stays flat.

```mermaid
flowchart LR
    S1["1. Intake<br/>review: heavy"]:::heavy --> S2["2. Draft<br/>review: light"]:::light
    S2 --> S3["3. Peer Review<br/>review: light"]:::light
    S3 --> S4["4. Publish<br/>review: heavy"]:::heavy

    classDef heavy fill:#78350f,stroke:#fbbf24,color:#fef3c7
    classDef light fill:#1e3a8a,stroke:#60a5fa,color:#dbeafe
    classDef gap fill:#7f1d1d,stroke:#f87171,color:#fee2e2
```

---

## Checklist before shipping a flowspace's Stage Flow Diagram

- [ ] `flowchart LR`, one node per stage, numbered, in the same order as the Stage table
- [ ] Every node's review-intensity color matches its row in the Stage table (or
      `gap` if Layer-3 is `TBD`)
- [ ] Flat chain by default; a band appears only if `HUB.md` documents that topology
      split, with a circled-number title and the dark slate frame style
- [ ] A loop-back edge appears only alongside a documented band split
- [ ] `classDef` and band-frame colors match the house palette above exactly
- [ ] **Rendering confirmed on GitLab** by viewing the rendered `.md` file (not
      the diff)
