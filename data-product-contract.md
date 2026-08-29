# Data-Product Contract

Use this when other people, software, or AI will rely on shared information.
The contract makes the information promise, owner, intended use, and stop-trust
conditions visible before a table or pipeline quietly becomes authoritative.

## Ten-minute first contract

Complete these five lines before the full template:

1. **This information helps this named consumer:**
2. **make this decision or do this work:**
3. **using this plain-language meaning and time boundary:**
4. **under the authority of this owner and source version:**
5. **and they must stop trusting it when:**

If the answer is “everyone,” “all analytics,” or “AI,” the use is still too
broad. A dependable data product makes a bounded promise to named consumers.

### Miniature example

| First-pass line | Northbridge partner-service answer |
| --- | --- |
| Named consumer | Service operations investigating delayed shipments. |
| Decision or work | Decide which open shipment still has time for useful intervention. |
| Meaning and time | Current intervention status as of the stated refresh time; it is not the contractual or quarterly meaning of “on time.” |
| Authority and source | Service operations owns the meaning; the versioned shipment and exception sources supply the recorded state. |
| Stop-trust condition | Required cohorts disappear, source corrections stop propagating, freshness exceeds the decision window, or the semantic version changes without consumer review. |

See the
[complete Northbridge Data-Product Contract](examples/northbridge-data-product-contract-v1.md)
for the comprehensive record and its constructed evidence boundary.

## Plain-language vocabulary

- **Data product:** a maintained information promise for named consumers—not
  merely a table, file, or storage location.
- **Consumer:** the person, team, application, workflow, or AI use relying on
  the information.
- **Semantic authority:** the role allowed to define what a term or measure
  means for the stated context.
- **Grain:** what one row or record represents.
- **Lineage:** the sources, transformations, versions, and policies that
  produced the information.
- **Fitness for use:** whether this exact information is good enough for this
  exact decision.
- **Stop-trust condition:** evidence that tells consumers to pause, narrow, or
  reject use until the problem is resolved.

**Status:** Working template
**Product name and version:**
**Contract owner:**
**Effective date:**
**Review or retirement trigger:**

## 1. Information promise

- Plain-language promise:
- Decisions or work this product supports:
- Named consumer groups:
- Explicitly unsupported uses:
- Business outcome if the promise is met:
- Harm or burden if consumers rely on it incorrectly:

## 2. Meaning and authority

| Term or measure | Definition | Context and time | Semantic authority | Version/change authority | Known competing definition |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

- Unit of observation or grain:
- Required dimensions or cohorts:
- Interpretation warnings:
- Translation rules at domain boundaries:

## 3. Sources and transformations

| Source | Authoritative for | Capture method | Expected delay/correction | Transformation reference | Lineage evidence |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

- Derived fields and claim they make:
- Reprocessing or correction policy:
- Source or transformation changes requiring consumer review:

## 4. Service and quality promise

| Consumer use | Freshness | Completeness/cohort coverage | Accuracy/validity rule | Availability | Failure action |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

- Publication and support owner:
- Incident and escalation path:
- Stop-trust conditions:
- Evidence retained:

## 5. Access, purpose, and lifecycle

- Classification:
- Approved purposes:
- Prohibited purposes:
- Tenant, row, column, document, or cohort entitlements:
- Sensitive and derived-sensitive fields:
- Retention, deletion, and correction requirements:
- Downstream propagation obligations:

## 6. Evolution

- Compatibility promise:
- Consumer notification and migration:
- Dataset and semantic versioning:
- Deprecation and retirement:
- Reversal plan:

## 7. Evidence gate

| Promise | Evidence source | Coverage | Last result/date | What it does not prove | Owner |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

**Decision:** approve / conditionally approve / reject / defer
**Conditions and unknowns:**
**Approvers and authority:**

## Outside-team comprehension test

Give the five-line contract to someone who neither owns the source nor built the
pipeline. Ask them what the information means, which decision it supports, who
may change the meaning, and when they must stop using it. If they answer with a
platform name or need private context, revise the contract before adding more
machinery.
