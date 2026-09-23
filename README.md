# Data Platform Architecture for AI Systems — Companion

**Series:** *AI Systems Architecture Field Guides*
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
  neither artifact certifies production fitness.

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

Human practitioner validation remains pending. Facilitators can find the
retained packet versions, freeze controls, and synthetic limitations in
[Facilitator Protocol History](FACILITATOR-PROTOCOL-HISTORY.md).

## Imagine and shape what comes next

Use the [Responsible Amplification and Possible Futures
Card](examples/responsible-amplification-and-possible-futures-card.md) to begin
with a beneficial possibility, trace bias and consequences through the whole
system, compare three plausible futures, and turn one future signal into a
reversible present decision. It is `PLANNED/UNRUN` and does not prove a
forecast, fairness, safety, legality, effectiveness, or reader learning.

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

## Evidence and use boundary

This is the public reader companion to *Data Platform Architecture for AI Systems*. It provides
editable tools and constructed examples; it does not certify a design,
implementation, organization, or AI system as safe, lawful, effective, or fit
for production. Preserve every `constructed`, `scenario`, `planned`,
`unrun`, `observed`, `tested`, `reported`, `inferred`, and `unknown`
label when adapting the material.

Written content is available under
[CC BY 4.0](LICENSE-CONTENT), and executable code is available under the
[Apache License 2.0](LICENSE-CODE). Source lineage is recorded in
[PROVENANCE.md](PROVENANCE.md); local integrity checks are documented in
[VALIDATION.md](VALIDATION.md). Human learner and practitioner validation
remains a separate evidence gate.

## Continue through the series

The five public companions follow the same evidence-bounded field-guide model:

1. [API Architecture for AI Systems](https://github.com/bmozi/api-architecture-for-ai-systems-companion)
2. [Event-Driven Architecture for AI Systems](https://github.com/bmozi/event-driven-architecture-for-ai-systems-companion)
3. [Durable Workflows for AI Systems](https://github.com/bmozi/durable-workflows-for-ai-systems-companion)
4. [Data Platform Architecture for AI Systems](https://github.com/bmozi/data-platform-architecture-for-ai-systems-companion)
5. [Agentic Systems Architecture](https://github.com/bmozi/agentic-systems-architecture-companion)

## September 9 reader-review practice

[Derive and correct the supplied review queue](examples/current-edition-queue-practice.md) with supplied fictional facts.
This extends the revised book without changing older pilot evidence.
