# Data Meaning, Provenance, and Permitted-Use Contract

Use this decision-facing front sheet when a data product will influence a
meaningful human, automated, or AI-supported decision. It does not replace the
five canonical data tools. It joins their current decisions so a reviewer can
see whether this exact information is fit, permitted, traceable, and operable
for one named use.

**Use boundary:** Illustrative field tool; not legal advice or production-fitness
proof. It does not authorize an API, workflow, agent, release, or business action.

## Ten-minute first pass

Name one consumer, one decision, and one information product. Record:

1. the decision supported and whether the output is descriptive, advisory,
   automated, or action-triggering;
2. the meaning, authority, version, and time boundary;
3. the source, transformation, correction, and freshness limits;
4. the allowed and prohibited purposes, inferences, and actions; and
5. the stop-trust or revalidation event.

“Everyone,” “all analytics,” and “AI” are not bounded consumers or uses. If a
downstream action is proposed, name its separate authorization owner and route
that decision to the relevant API, workflow, or agentic review.

## Contract decision card

| Field | Current decision or evidence | Resolver record |
| --- | --- | --- |
| Information product, named consumer, and decision | | [Data-Product Contract](data-product-contract.md) |
| Output role: descriptive, advisory, automated, or action-triggering | | [Data-Product Contract](data-product-contract.md) and downstream action review |
| Meaning, semantic authority, competing meanings, and change authority | | [Semantic-Authority Record](semantic-authority-record.md) |
| Sources, transformations, versions, corrections, and retrieval/index context | | [Provenance Requirements](provenance-requirements.md) |
| Freshness, coverage, quality policy, cohort limits, and failure action | | [Quality-Evidence Scorecard](quality-evidence-scorecard.md) |
| Permitted and prohibited purpose, inference, and downstream action | | [Data-Product Contract](data-product-contract.md) |
| Entitlement, classification, retention, correction, and propagation | | [Data-Product Contract](data-product-contract.md) |
| Use-specific AI fitness and remaining limits, if relevant | | [AI-Data Readiness Assessment](ai-data-readiness-assessment.md) |
| Action authorization owner and enforcement path, when applicable | | Separate API, workflow, or agentic-system record |
| Stop-trust or revalidation trigger and decision owner | | Applicable canonical record and retained evidence |

## Required revalidation gates

Suspend, narrow, or re-review the approval when any of these changes materially
affects the named use:

- semantic or source version changes;
- a source correction, cohort loss, coverage break, or freshness breach;
- an entitlement, purpose, retention, or policy change;
- retrieval-index or transformation drift; or
- a newly proposed consumer, decision, inference, AI role, or action.

A catalog entry, lineage graph, access grant, quality score, or retrieval
citation can contribute evidence. None independently proves meaning, truth,
permitted use, decision fitness, or legitimate action authority.

## Falsifiable forecast

**Prediction:** As AI makes information easier to transform, retrieve, and
reuse, organizations will increasingly approve consequential data products by
named use and revalidation trigger rather than by generic availability or a
universal “trusted” badge.

**Leading indicators:** policy-aware release gates; use-specific quality
objectives; versioned retrieval evidence; and incidents classified by semantic,
cohort, freshness, or purpose failure rather than only by job failure.

**Disconfirming condition:** generic cataloging and access controls reliably
support safe, challengeable cross-use reuse without equivalent named-use,
provenance, and revalidation records. Preserve that evidence and reconsider
the Contract's added burden.
