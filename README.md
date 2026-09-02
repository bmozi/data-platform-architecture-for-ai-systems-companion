# Data Platform Architecture for AI Systems — Companion

**Series:** *AI Systems Architecture Field Guides*
**Previous working title:** *Architecting Data Platforms in the Age of AI*.

Turn one important number, dataset, or source into a maintained information
promise for a named use—with meaning, ownership, lineage, quality, access, and
stop-trust conditions visible.

## The problem you may recognize first

You may have arrived because you need a lakehouse, a pipeline, a RAG stack,
embeddings, or “AI-ready data.” If teams calculate the same term differently, a
model cannot show which version informed its answer, or a green pipeline
produces information nobody will defend, the problem is data-platform
architecture before it is storage selection.

A data platform is the people, rules, and machinery that turn records into
maintained information products for named uses—not merely the place data is
stored. Start with [The AI-Ready Data Journey](AI-READY-DATA-JOURNEY.md) when
the immediate question is what readiness means and how to reach it.

This companion helps you produce a first reviewable result. It does not certify
data, a platform, an AI use, or an organization as trusted, fair, lawful, or
ready for production.

## The book-and-companion contract

- **The book teaches the judgment:** which information promise matters, who
  owns meaning, what makes data fit for one use, when access is legitimate, and
  what evidence should stop trust.
- **The companion provides the moves:** data-product contracts, semantic-
  authority records, quality scorecards, provenance requirements, readiness
  assessments, and constructed examples.
- **Use the book as the required learning resource:** read the relevant book
  chapters before treating an exercise output as an architecture decision. The
  repository intentionally does not reproduce the book's explanations,
  tradeoffs, or narrative. A reader can inspect and try the tools without the
  book, but the intended result—sound judgment about meaning, authority,
  fitness, and limits—requires the book and this companion together.
- **The book stands alone:** this repository extends *Data Platform
  Architecture for AI Systems* without replacing its reasoning or narrative;
  neither artifact is a certification of production readiness.

## Production presentation status

This repository is **owner-approved for presentation and intended distribution
of the exact reviewed package; human validation remains pending**. The deterministic
local gate is the command in [VALIDATION.md](VALIDATION.md); it checks required
entry points, local links, gateway language, examples, packet checksums, and
the reader-value protocol. [PROVENANCE.md](PROVENANCE.md) records source and
evidence boundaries, and [LICENSE-STATUS.md](LICENSE-STATUS.md) records the
approved distribution scope. The owner decision is recorded in
[OWNER-RELEASE-APPROVAL.md](OWNER-RELEASE-APPROVAL.md).

Do not label this companion `Piloted`, `Practitioner-tested`, or `Production`
until all of these are separately evidenced: a completed human cold-reader
route with an independent decision owner; retained observations and any
negative findings; a revised and repeated route where needed; approval of the
corresponding book edition and companion terms; and final accessibility,
security, rights, and publication review. A local validation pass proves
repository integrity only.

## Start here

Use [START-HERE.md](START-HERE.md), alongside the relevant chapters of the
book, to take one information product through a thirty-minute first pass. You
will name the consumer, decision, meaning, owner, source, and stop-trust
condition, then test one proposed AI use separately.

## Core assets

| Need | Start with |
| --- | --- |
| Define an information promise | [Data-Product Contract](data-product-contract.md) |
| Decide who may define meaning | [Semantic-Authority Record](semantic-authority-record.md) |
| Make fitness evidence executable | [Quality-Evidence Scorecard](quality-evidence-scorecard.md) |
| Preserve source and transformation history | [Provenance Requirements](provenance-requirements.md) |
| Assess one bounded AI use | [AI-Data Readiness Assessment](ai-data-readiness-assessment.md) |
| Separate fast aggregation from trusted meaning | [Northbridge Data-Structures Architecture Bridge](examples/northbridge-data-structures-architecture-bridge.md) |

Use [INDEX.md](INDEX.md) for role- and outcome-based routes and
[BOOK-TO-COMPANION-MAP.md](BOOK-TO-COMPANION-MAP.md) to reconnect each tool to
the book's reasoning.

## Use it across roles

[Role-Based Paths](ROLE-BASED-PATHS.md), the [Team Workshop](TEAM-WORKSHOP.md),
and the [Executive Decision Brief](EXECUTIVE-DECISION-BRIEF.md) turn readiness
from a data-team slogan into a cross-functional decision. Use the
[Value and Evidence Ledger](VALUE-AND-EVIDENCE-LEDGER.md) to prioritize one
valuable use, then exercise assumptions with the [Failure Lab](FAILURE-LAB.md)
and [Pilot Route](PILOT-AND-USABILITY.md).

The prepared reader-value packet is `DATA-RV-PILOT-001` version 1.2.8. Stage A
freezes exact revised details through a detached record before opening its
one-screen handoff; Stage B reads that handoff first, verifies the same literal
files only after Section 1 freezes, then freezes its decision in three stages.
Version 1.2.8 responds to retained synthetic attempt
`DATA-SYN-20260830-006`, whose semantically useful handoff failed the literal
layout gate at two pages and 640 reader-facing words. The redesigned blank uses
five budgeted reader sections, a 335-word target, eight compact immutable
provenance lines, non-clickable exact-filename pointers, and no copied-detail
table. The handoff triple is the only Stage A evidence in Phase 1; the route
and blank Section 1 workbook remain allowed. Revised detail first becomes
available in Phase 2. Version 1.2.8 preserves v1.2.7's exact phase-input
manifest binding, v1.2.6's synthetic-only pre-run checksum-bound exact-file
helper, v1.2.5's full-route and one-page layout controls, and v1.2.4's exact
immutable Stage A live update and optional-contract branch. Each per-phase
config binds its exact verified sealed-input manifest filename/path/hash, and the helper
rehashes and parses that manifest and proves exact member/hash equality on
every invocation before it reads a target. Human participants still use
ordinary file surfaces without terminal or repository access. Helper
procedural compliance is not sandbox or cross-process security proof;
technical platform restriction is `NOT ESTABLISHED` unless separately
demonstrated. Six scored freeze chains do not alone establish full-route
completion. The packet remains unrun with
people and carries no human, practitioner, data-readiness, safety, business-
value, or real-world validation. The v1.2.7 source remains preserved at commit
`a4b88a34d11a267a140e5bf67c69f4bc68a1d43a`.

## Development boundary

This is an owner-approved companion package. Constructed examples and blank
test logs are not production or usability evidence. Human learner/practitioner
validation remains pending; see [OWNER-RELEASE-APPROVAL.md](OWNER-RELEASE-APPROVAL.md).
Source lineage is recorded in [PROVENANCE.md](PROVENANCE.md), and local
validation is described in [VALIDATION.md](VALIDATION.md).
