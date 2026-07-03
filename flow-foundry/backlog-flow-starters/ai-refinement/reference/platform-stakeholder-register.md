---
id: platform-stakeholder-register
title: "Platform-as-a-Product — Internal Stakeholder Register"
type: clipping
artifact-version: "1.0"
status: living
truth-level: claimed
created: 2026-07-03
updated: 2026-07-03
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
---

> **Ingest note (house):** operator-supplied requirements-source map for the
> platform work portfolio, captured as-is per the clipping convention (its
> original frontmatter is preserved in the fenced block below). Team names are
> the generic mid-size-enterprise shape by the document's own declaration —
> public-safe. Consumed as Layer-3 by `ai-refinement` Stages 02 (stakeholder
> sweep) and 03 (coalition / conflict-axis annotation, escalation routing).
> Content below this line is the source material, unreviewed (`claimed`).

```yaml
title: Platform-as-a-Product — Internal Stakeholder Register
type: stakeholder-register
purpose: Requirements gathering & synthesis for the platform work portfolio
platform-domains: [network-engineering, dc-networking, perimeter-security, voice-video, corporate-services]
org-shape: mid-size (enterprise-structured)
status: draft
created: 2026-06-30
```

# Platform-as-a-Product — Internal Stakeholder Register

A requirements-source map for the platform portfolio. It answers *whose needs and
limits define what each platform should do* — not *who to keep in the loop*. Each
entry is a taggable stakeholder on a Jira work item.

**Domain legend:** `NE` Network Engineering · `DC` Data Center Networking · `PS` Perimeter Security · `VV` Voice & Video · `CS` Corporate Services (badging) · `ALL` cross-cutting

**Role-types:** *Producer* (owns/builds) · *Consumer* (demand side) · *Constraint-setter* (guardrails) · *Operator* (runs it) · *Adjacent* (integration seam) · *Sponsor* (money & mandate)

> Team names below are the generic shape for a mid-size, enterprise-structured shop.
> Swap in your real org units. Where one real team wears several of these hats, that
> overlap is itself signal — it's where capacity strain and requirement-conflicts live.

---

## Stakeholder register

| # | Stakeholder | Role-type | Domains | What they value most |
|---|-------------|-----------|---------|----------------------|
| 1 | **Network Engineering** | Producer | NE | A consistent, predictable transport fabric; fewer snowflakes; clean change windows and low MTTR. Standardization that keeps the network legible. |
| 2 | **Data Center Networking** *(us)* | Producer | DC | Throughput, low east-west latency, non-blocking fabric at scale, and capacity headroom. Being consulted *early* on DC builds before power/space/cooling lock in. Not being the bottleneck for compute and storage. |
| 3 | **Perimeter Security Engineering** | Producer / Constraint | PS | Enforceable, auditable edge control with minimal exception sprawl. Clear rule ownership. Not becoming the "yes to every firewall exception" desk. |
| 4 | **Unified Communications** | Producer | VV | Call and meeting quality (jitter, loss, MOS), availability during high-visibility events, and seamless cross-device experience — especially for exec/VIP use. |
| 5 | **Corporate Services (Badging/AV)** | Producer | CS | Access that works day-one and revokes day-zero; tight physical↔logical identity integration; low friction for employees; audit-ready access records. |
| 6 | **Cyber Security** *(SOC · Sec Eng · GRC · Vuln Mgmt)* | Constraint-setter | ALL | Risk reduction, telemetry everywhere, control coverage, and defensibility. Will trade convenience for logging, segmentation, and least privilege. |
| 7 | **Identity & Access (IAM)** | Constraint / Adjacent | PS, CS, ALL | One authoritative identity, clean joiner/mover/leaver lifecycle, least-privilege entitlements, fast deprovisioning. No orphaned access. |
| 8 | **Compliance & Risk** *(Audit · Risk · Legal · Privacy)* | Constraint-setter | ALL | Evidence, traceability, and framework/regulatory alignment. Documented, repeatable processes; no undocumented change or unsigned exceptions. |
| 9 | **Systems / Server** *(Compute · Virt · Storage · DBA)* | Consumer / Adjacent | DC | Network that "just works" for their workloads — capacity and latency for vMotion, replication, storage traffic — plus fast, self-service provisioning. |
| 10 | **Application Development** *(+ Data/Analytics · DevOps)* | Consumer | NE, PS | Speed and self-service; low-friction access to network and security resources; not being blocked. Good developer experience over gatekeeping. |
| 11 | **Lines of Business** *(BU liaisons · sponsors · shadow-IT lens)* | Consumer / Sponsor | ALL | Business outcomes, cost transparency, and reliability of what they depend on. Autonomy — resists standardization that removes their control or adds friction. |
| 12 | **Cloud** | Adjacent / Consumer | NE, PS, DC | Consistent hybrid connectivity, identity federation, and policy parity between on-prem and cloud. Reliable interconnect and IaC-compatible automation. |
| 13 | **Facilities / Physical Security** | Adjacent | DC, CS | Life-safety and code compliance; power/space/cooling limits respected; reliability of building and access systems. Being consulted before DC and badging builds. |
| 14 | **HR / HRIS** | Adjacent | CS | Accurate employee-lifecycle data, timely feeds downstream, minimal manual work, and strict protection of personnel PII per employment law. |
| 15 | **End-User Services & ITSM** *(Service Desk · EUC · Change/Incident/Problem)* | Operator | VV, CS, ALL | Supportability and day-2 operability, ticket deflection, change discipline, and clear runbooks. Dislikes being handed unsupportable platforms. |
| 16 | **IT Leadership** *(CIO/CTO/VP · CISO · Enterprise Architecture)* | Sponsor | ALL | Strategic alignment, cost/value, balanced risk posture, and predictable portfolio delivery. Org reputation. |
| 17 | **Portfolio & Sourcing** *(PMO · Finance/FinOps · Procurement · Telecom contracts)* | Sponsor | ALL | Clean intake and prioritization, budget adherence, vendor value and contract leverage, and honest resource-capacity visibility. |

---

## Where priorities align

Natural coalitions — when a requirement pleases one member, it usually pleases the
rest. Batch their input; expect fast consensus.

- **The Standards Coalition** — Network Engineering (1), DC Networking (2), Perimeter (3), Cyber (6), Compliance (8).
  *Shared value:* consistency, fewer exceptions, documented change. Co-signs anything that reduces snowflakes and enforces standards.

- **The Identity Backbone** — IAM (7), HR/HRIS (14), Corporate Services (5), Cyber (6).
  *Shared value:* authoritative identity and a clean joiner/mover/leaver lifecycle. Badging and access are only correct if this is correct — strong mutual interest.

- **The Performance & Availability Bloc** — DC Networking (2), Systems/Server (9), Cloud (12), Unified Comms (4).
  *Shared value:* capacity, low latency, resilience. Aligns on investment in a performant, redundant fabric.

- **The Assurance Cluster** — Cyber (6), Compliance & Risk (8), IAM (7), Perimeter (3).
  *Shared value:* logging, evidence, least privilege, defensibility. The requirements that make audits survivable.

- **The Delivery Line** — IT Leadership (16), Portfolio & Sourcing (17), End-User Services/ITSM (15).
  *Shared value:* predictable, prioritized, supportable, cost-justified delivery.

---

## Where priorities conflict

The tensions requirements gathering exists to *reconcile*. Each is a negotiation
point — surface it early, and attach a decision record rather than letting it
detonate mid-build.

- **Speed vs. Control** — App Dev (10) + Lines of Business (11)  ⟷  Perimeter (3) + Cyber (6) + Compliance (8).
  *Bites hardest on:* self-service network and firewall provisioning. This is the defining platform-as-a-product tension — how much can you hand out without a gate.

- **Standardization vs. Autonomy** — Network (1) + DC (2) + Corporate Services (5)  ⟷  Lines of Business (11) *(and shadow-IT)*.
  *Bites on:* absorbing BU-owned AV, local firewall rules, or local access control into the platform. Your resistant-stakeholder energy lives here.

- **Performance vs. Segmentation** — Systems/Server (9) + Unified Comms (4)  ⟷  Perimeter (3) + Cyber (6).
  *Bites on:* microsegmentation and inline inspection that add hops and latency to east-west and real-time traffic.

- **Cost vs. Headroom** — Portfolio & Sourcing (17) + IT Finance  ⟷  all producer teams (1–5).
  *Bites on:* redundancy, capacity headroom, and refresh cycles — the first things squeezed when the envelope tightens.

- **Growth vs. Physical Limits** — DC Networking (2) + Systems/Server (9)  ⟷  Facilities (13).
  *Bites on:* fabric and compute expansion hitting power, cooling, and space ceilings. A hard constraint, not a negotiable one.

- **Velocity vs. Stability** — App Dev (10) + Cloud (12)  ⟷  Network Engineering (1) + End-User Services/ITSM (15).
  *Bites on:* change frequency vs. stable windows and supportability. Fast movers vs. the people who hold the pager.

- **Access Richness vs. Data Minimization** — IAM (7) + Cyber (6) + Corporate Services (5)  ⟷  HR (14) + Compliance/Privacy (8).
  *Bites on:* how much personnel and identity-attribute data flows for access decisions. Useful signal vs. privacy exposure.

---

## Using this in requirements gathering

1. On each Jira epic/story, tag the stakeholders, then note **which coalition it satisfies** and **which conflict axis it triggers**.
2. **Aligned stakeholders** → batch their elicitation; expect quick agreement; capture as shared requirements.
3. **Conflict axes** → these are your explicit tradeoff decisions. Don't let them surface late. Each needs a named decision-owner and a recorded rationale (which side won, and why).
4. **Producers (1–5) synthesize.** A conflict between a producer and a constraint-setter that can't be settled peer-to-peer escalates to **IT Leadership (16)**; a conflict about *what's worth doing at all* escalates to **Portfolio & Sourcing (17)**.
5. Watch the **multi-hat teams** in your real org: where one team is both producer and operator (or the sponsor sits one rung above the producer), a "conflict" may actually be one overloaded team arguing with itself — a capacity problem wearing a requirements costume.
