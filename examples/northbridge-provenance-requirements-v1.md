# Northbridge Provenance Requirements — Constructed Example

<!-- markdownlint-disable MD013 -->

**Record ID:** NBX-PVR-001
**Record version:** 1.0.0
**Template:** [Provenance Requirements](../provenance-requirements.md)
**Template source version:** Working template bytes reviewed 2026-08-29
**Template source SHA-256:** `cb0bd8759e40bf2c3da9ecce3c4355745563ce3a9140d4e2cb781124401ddbe3`
**Status:** `SCENARIO — insufficient; one deliberate link break; verification unrun`
**Information product or output:** Partner NBX-P-1842 renewal evidence row and population context in NBX-PERF-3.2.1
**Consequential use:** Human-reviewed SCENARIO-Q3 partner renewal
**Provenance owner:** NBX-ROLE-PRODUCT
**Retention period and authority:** Fictional NBX-POL-RET-03 decision-package interval; not a legal conclusion

> **Constructed-example disclosure:** This chain is fictional. Its missing link
> is deliberately authored to demonstrate an insufficient decision. It is not
> an observed control failure, a legal record, or evidence that a real output
> can or cannot be reconstructed.

## 1. Reconstruction question

Can an authorized fictional reviewer identify the exact source observations,
historical partner relationship, contract and semantic rules, eligible partner
population, settled-obligation denominator, transformation, quality gate,
purpose, product version, and human decision context that produced the
NBX-P-1842 renewal evidence row—and can the reviewer distinguish reconstruction
of that row from proof that the product included every eligible partner?

## 2. Required chain

| Layer | Required identifier and version | Authority or owner | Evidence captured | Integrity/retention | Failure consequence |
| --- | --- | --- | --- | --- | --- |
| Source delivery records | NBX-SRC-DELIVERY-07 snapshot SCENARIO-Q3-A | NBX-ROLE-SOURCE-OPS | Scenario record IDs, event time, correction state | Expected immutable fixture and digest before run | Cannot show which observations supported the score |
| Contract source | NBX-SRC-CONTRACT-04 version 17 | NBX-ROLE-CONTRACT-CUSTODY | Effective contract window and exceptions | Expected versioned snapshot | Cannot establish contractual meaning |
| Partner identity | NBX-SRC-IDENTITY-09 version 9 | NBX-ROLE-PARTNER-OPS | Effective-time partner-contract mapping | Partial: predecessor translation unresolved | Affected cohort must remain unknown |
| Eligible partner population | NBX-SRC-RENEWAL-03 snapshot SCENARIO-Q3-D | NBX-ROLE-RENEWAL | **DELIBERATE BREAK: identifier named, retained object absent** | `SCENARIO MISSING`; no digest | Cannot prove that every eligible partner-contract relationship entered the product |
| Eligible settled-obligation denominator | NBX-SRC-OBLIGATION-11 snapshot SCENARIO-Q3-O | NBX-ROLE-PARTNER-OPS | Scenario obligation IDs, inclusion/exclusion reason, contract version, and NBX-TR-OBLIG-DENOM-03 | Expected frozen bytes and digest before run; verification unrun | Cannot reconstruct an included partner's rate if absent or altered |
| Capture and ingestion | NBX-INGEST-22 config 4 | NBX-ROLE-RELIABILITY | Planned source offsets, correction markers, run ID | No executed run | Capture behavior remains unknown |
| Transformation | NBX-TR-RENEWAL-12 commit FIXTURE-C12 | NBX-ROLE-PRODUCT | Scenario code/config reference | Expected frozen bytes before run | Cannot reconstruct classifications without exact logic |
| Obligation-denominator transformation | NBX-TR-OBLIG-DENOM-03 commit FIXTURE-D03 | NBX-ROLE-PRODUCT with NBX-ROLE-PARTNER-OPS meaning authority | Scenario inclusion/exclusion logic and source-manifest binding | Expected frozen bytes before run; no executed result | Cannot show which settled obligations entered an included partner's rate |
| Semantic definition | NBX-SAR-001 version 1.0.0 | NBX-ROLE-PARTNER-OPS | Definition, authority, effective interval, dissent | Present as constructed record | Wrong or current meaning could be substituted |
| Dataset/materialization | NBX-PERF-3.2.1 | NBX-ROLE-PRODUCT | Scenario schema, partition list, output identity | No materialized data executed | Artifact identity and output remain untested |
| Quality and reconciliation | NBX-QES-001 version 1.0.0 | NBX-ROLE-RELIABILITY | Scenario thresholds and stop action | Failing authored condition; no run | Stopped use cannot be treated as fit |
| Purpose and entitlement | NBX-POL-PURPOSE-08 version 3 | NBX-ROLE-SECURITY | Renewal-purpose and role mapping | Scenario reference only | Read access could be mistaken for use authority |
| AI context assembly | NBX-CTX-RENEWAL-02 version 1 | NBX-ROLE-AI-DATA | Planned field selection and prompt-context reference | Not assembled or tested | Cannot reconstruct what an AI component received |
| Output/decision/consumer | NBX-DEC-RENEWAL-1842 candidate reference; no decision exists | NBX-ROLE-RENEWAL | Required reviewer, time, input versions, disposition | Blank; no decision occurred | Cannot claim a renewal outcome or rationale |

Only layers relevant to the bounded scenario are listed. This record does not
claim the list is exhaustive for a real organization.

## 3. Corrections and descendants

- **Source correction process:** Authoritative fictional source role issues a
  new version, preserves the superseded reference, and identifies affected
  descendants.
- **Descendant discovery:** Follow product-version, transformation-run,
  semantic-version, and decision-package edges from the corrected record.
- **Recompute, restate, quarantine, or notify rule:** Quarantine the affected
  output; recompute under a new version only after partner-population,
  settled-obligation, and identity evidence are resolved; notify
  NBX-ROLE-RENEWAL of superseded material.
- **Deletion and retention propagation:** Follow the fictional purpose and
  retention decision; preserve only the minimum decision receipt authorized by
  that decision. This is a scenario rule, not legal advice.
- **Historical reproducibility after correction:** Preserve the original
  artifact identity and decision context where authorized. Do not replace the
  old input with today's corrected record and call the result reproduction.

## 4. Access and challenge

- **Who may inspect the chain:** Fictional authorized renewal reviewer,
  provenance owner, and control reviewer within their purpose and entitlement.
- **Who may challenge meaning or source authority:** Partner operations,
  contract custody, renewal owner, security, and affected product owner.
- **Who may correct each layer:** Only the named layer authority; platform
  custody cannot silently repair business meaning or policy.
- **Audit and disclosure constraints:** Restricted partner and contract fields
  remain purpose-bound; a reviewer may receive a redacted proof where the
  fictional policy permits it.
- **Evidence unavailable by design and consequence:** The eligible-partner
  population snapshot is deliberately absent. Therefore product-level partner
  coverage cannot be reconstructed and the use remains stopped. The distinct
  settled-obligation source needed for an included partner's rate is named as a
  scenario reference, but no reconstruction or integrity test has run.

## 5. Verification

| Test | Expected result | Actual result/date | Negative or mutation case | Remaining gap |
| --- | --- | --- | --- | --- |
| Trace output to source | Every scored obligation links to delivery, contract, and historical identity versions | `UNRUN`; no date | Remove one source link and require an explicit failure | All control behavior unknown |
| Reproduce with pinned versions | Included partner's rate matches from the pinned obligation denominator, while product-population completeness is evaluated separately | `UNRUN`; no date | Change one source, semantic, dependency, partner-population, and obligation-denominator version independently | Individual-rate behavior and product-population coverage remain untested; product baseline lacks the partner-population object |
| Propagate correction or deletion | Authorized descendants are found and handled under the declared policy | `UNRUN`; no date | Orphan one descendant and retain the miss | Coverage unknown |
| Enforce purpose and entitlement | Only the declared reviewer and renewal purpose can inspect required evidence | `UNRUN`; no date | Change role, purpose, partner, and time separately | Enforcement unknown |
| Detect missing or altered link | A missing required partner-population or settled-obligation object produces the scoped stop before publication | `UNRUN`; no date | Deliberately absent NBX-SRC-RENEWAL-03; future separate obligation mutation | Detection and false-alarm behavior unknown |

**Decision:** `SCENARIO — insufficient for product-level partner-renewal use.`
**Conditions and reconsideration trigger:** Restore the exact partner-population
snapshot with identity, version, integrity, and authority evidence; freeze the
distinct settled-obligation source; resolve or preserve the acquisition-era
unknown; then execute a separately authorized verification protocol. No
evidence-state transition is implied.

## Cross-record effects

NBX-DPC-001 requires both partner-population and settled-obligation evidence.
NBX-QES-001 uses the missing partner-population link as a product-level stop and
tests the obligation denominator separately. NBX-SAR-001 prevents substitution
of today's identity meaning. NBX-ADR-001 must remain deferred for
NBX-PERF-3.2.1 even if a model or interface appears plausible.
