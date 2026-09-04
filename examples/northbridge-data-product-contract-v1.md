# Northbridge Data-Product Contract — Constructed Example

<!-- markdownlint-disable MD013 -->

**Record ID:** NBX-DPC-001
**Record version:** 1.0.0
**Template:** [Data-Product Contract](../data-product-contract.md)
**Template source version:** Illustrative template bytes reviewed 2026-08-29<br>
**Template source SHA-256:** `9263865f63a936d0afb113b3153df70f7443dc76e3601a0019efc65b66224a05`
**Status:** `SCENARIO — conditionally approved`; not observed or executed
**Product name and version:** Northbridge Quarterly Partner-Renewal Evidence Product, NBX-PERF-3.2.1
**Contract owner:** NBX-ROLE-PRODUCT, fictional partner-performance product owner
**Effective date:** SCENARIO-Q3 review cycle only
**Review or retirement trigger:** semantic-version change, cohort-coverage breach, purpose change, source retirement, or end of SCENARIO-Q3

> **Constructed-example disclosure:** Every name, role, value, decision, and
> outcome in this record is fictional scenario material. It is not a report of
> John Briggs's experience or evidence that this template works.

## 1. Information promise

- **Plain-language promise:** Provide the fictional renewal group with a
  versioned retrospective view of partner delivery performance under the
  contract measure effective for SCENARIO-Q3.
- **Decisions or work this product supports:** Human review of quarterly
  partner renewal evidence. The product informs; it does not decide renewal.
- **Named consumer groups:** NBX-ROLE-RENEWAL and authorized analysts acting for
  that role.
- **Explicitly unsupported uses:** Daily service dispatch, customer
  compensation, public ranking, model training, autonomous partner contact,
  or automatic renewal decisions.
- **Business outcome if the promise is met:** `SCENARIO` only: the renewal group
  can compare records under one declared rule. No benefit is claimed.
- **Harm or burden if consumers rely on it incorrectly:** A partner or cohort
  could be omitted, an exception could be misclassified, or a score could be
  treated as an authorized decision.

## 2. Meaning and authority

| Term or measure | Definition | Context and time | Semantic authority | Version/change authority | Known competing definition |
| --- | --- | --- | --- | --- | --- |
| `on_time_for_renewal` | Delivery occurred inside the effective partner-contract window after approved exceptions and grace rules | SCENARIO-Q3 retrospective cutoff; contract effective time | NBX-ROLE-PARTNER-OPS, subject to the contract record | NBX-ROLE-PARTNER-OPS with NBX-ROLE-RENEWAL acceptance for this use | Buyer-promise and live-service meanings |
| `eligible_partner` | Partner-contract relationship in the fictional renewal population at the declared cutoff | SCENARIO-Q3; effective-dated identity mapping | NBX-ROLE-RENEWAL | NBX-ROLE-RENEWAL after partner-operations contribution | Current platform account status |
| `approved_exception` | Exception code authorized by the effective partner-contract rule | Per obligation and effective rule version | NBX-ROLE-PARTNER-OPS | NBX-ROLE-PARTNER-OPS | Service-recovery exception |

- **Unit of observation or grain:** One settled contractual delivery obligation,
  linked to the partner-contract relationship effective for that obligation.
- **Required dimensions or cohorts:** Partner, contract, acquisition cohort,
  region, obligation month, and exception class.
- **Interpretation warnings:** A buyer promise and a partner contract can be
  different without either record being wrong. A current partner ID does not
  establish the historical relationship.
- **Translation rules at domain boundaries:** Use NBX-SAR-001. Buyer-promise
  and service-operation meanings remain separate; translation to the renewal
  measure is lossy and requires the contract clock, approved exceptions, and
  effective-time mapping.

## 3. Sources and transformations

| Source | Authoritative for | Capture method | Expected delay/correction | Transformation reference | Lineage evidence |
| --- | --- | --- | --- | --- | --- |
| NBX-SRC-DELIVERY-07 | Delivery observations, not contract meaning | Versioned scenario snapshot | Late evidence through the declared settlement window | NBX-TR-RENEWAL-12 | NBX-PVR-001 row for NBX-SRC-DELIVERY-07 |
| NBX-SRC-CONTRACT-04 | Contract window and exception clauses | Effective-dated scenario extract | Corrected only through authorized contract process | NBX-TR-RULE-05 | NBX-PVR-001 row for NBX-SRC-CONTRACT-04 |
| NBX-SRC-IDENTITY-09 | Partner-contract relationship over time | Effective-dated scenario mapping | Correction may restate affected periods | NBX-TR-IDENTITY-08 | NBX-PVR-001 row for NBX-SRC-IDENTITY-09 |
| NBX-SRC-RENEWAL-03 | Declared eligible-partner population | Scenario cutoff export | Must be frozen before publication | NBX-TR-DENOM-02 | Deliberately missing from retained package in NBX-PVR-001 |
| NBX-SRC-OBLIGATION-11 | Eligible settled obligations within each eligible partner-contract relationship | Effective-dated scenario obligation manifest | Late or corrected obligations require a new manifest version | NBX-TR-OBLIG-DENOM-03 | Present as a scenario reference in NBX-PVR-001; verification unrun |

- **Derived fields and claim they make:** `renewal_on_time_rate` claims the
  share, within one eligible partner-contract relationship, of eligible settled
  obligations in NBX-SRC-OBLIGATION-11 classified on time under NBX-SAR-001.
  NBX-SRC-RENEWAL-03 separately determines which partner-contract
  relationships belong in the review population. The rate does not claim
  operational timeliness or partner quality in general.
- **Reprocessing or correction policy:** Publish a new product patch version,
  retain the superseded output, disclose affected periods and cohorts, and
  notify the renewal owner before reuse.
- **Source or transformation changes requiring consumer review:** Any
  source-authority change, mapping
  logic change, semantic major or minor change, denominator change, new cohort,
  exception-rule change, or change in correction window.

## 4. Service and quality promise

| Consumer use | Freshness | Completeness/cohort coverage | Accuracy/validity rule | Availability | Failure action |
| --- | --- | --- | --- | --- | --- |
| SCENARIO-Q3 human renewal review | Frozen after settlement window; no real-time claim | Every eligible partner must reconcile by acquisition cohort, and every included partner's settled-obligation denominator must reconcile separately; unexplained omissions are not permitted | Every scored obligation must resolve to effective contract, identity, exception, and obligation-manifest versions | Available during the fictional review window after evidence gate | Stop partner-level renewal use; quarantine affected publication; notify NBX-ROLE-RENEWAL |

- **Publication and support owner:** NBX-ROLE-PRODUCT.
- **Incident and escalation path:** NBX-ROLE-RELIABILITY investigates;
  NBX-ROLE-PARTNER-OPS resolves semantic or source disputes;
  NBX-ROLE-RENEWAL decides whether the review can proceed under a narrower use.
- **Stop-trust conditions:** NBX-QES-001 cohort failure; unresolved semantic
  dispute; missing partner-population, obligation-denominator, or identity
  version; expired purpose or entitlement; or unreviewed semantic change.
- **Evidence retained:** Product version, source snapshots, code/configuration,
  semantic version, cohort reconciliation, quality results, policy version,
  approval record, correction notices, and negative or stopped decisions.

## 5. Access, purpose, and lifecycle

- **Classification:** `SCENARIO — restricted internal partner information`.
- **Approved purposes:** Human-reviewed SCENARIO-Q3 renewal evidence only.
- **Prohibited purposes:** External disclosure, unrelated commercial analysis,
  training, public ranking, autonomous outreach, or action delegation.
- **Tenant, row, column, document, or cohort entitlements:** Partner-row access
  limited to authorized renewal analysts; direct contact fields excluded from
  this product; cohort views require the declared purpose.
- **Sensitive and derived-sensitive fields:** Partner score, exception class,
  contract relationship, and small-cohort indicators are treated as restricted
  in this scenario.
- **Retention, deletion, and correction requirements:** Retain the decision
  package for the fictional review period declared by NBX-POL-RET-03; propagate
  authorized corrections while preserving the superseded decision receipt.
- **Downstream propagation obligations:** Carry product, semantic, purpose,
  cohort, and correction versions. Consumers must not strip the unsupported-use
  declaration.

## 6. Evolution

- **Compatibility promise:** Patch versions correct data without changing the
  approved meaning; minor versions add backward-compatible fields; semantic or
  population changes require a major version and consumer decision.
- **Consumer notification and migration:** NBX-ROLE-PRODUCT sends a versioned
  change record to NBX-ROLE-RENEWAL before use.
- **Dataset and semantic versioning:** Product NBX-PERF-3.2.1 binds to
  NBX-SAR-001 version 1.0.0 and the listed source versions.
- **Deprecation and retirement:** Retire after the SCENARIO-Q3 decision window
  or immediately when a stop-trust condition cannot be resolved.
- **Reversal plan:** Revoke the publication alias, preserve the stopped receipt,
  restore only a previously approved version for its declared use, and require
  a fresh gate for republished data.

## 7. Evidence gate

| Promise | Evidence source | Coverage | Last result/date | What it does not prove | Owner |
| --- | --- | --- | --- | --- | --- |
| Eligible-population coverage | NBX-QES-001, NBX-QM-COHORT-04 | Acquisition cohorts in SCENARIO-Q3 | `SCENARIO FAIL`; authored condition, not executed | Detection accuracy, absence of other omissions, or harm | NBX-ROLE-RELIABILITY |
| Meaning authority | NBX-SAR-001 | Renewal definition and two translations | `SCENARIO CONDITIONAL` | Legal sufficiency or agreement outside the scenario | NBX-ROLE-PARTNER-OPS |
| Reconstruction | NBX-PVR-001 | Named renewal output chain | `SCENARIO INSUFFICIENT` | Whether any real output can be reproduced | NBX-ROLE-PRODUCT |
| AI data fitness | NBX-ADR-001 | Human-reviewed renewal-support role | `SCENARIO DEFERRED` | Model, workflow, action, or release approval | NBX-ROLE-AI-DATA |

**Decision:** `SCENARIO — conditionally approved as a contract definition, but
publication and partner-level use are stopped by NBX-QES-001 and NBX-PVR-001.`
**Conditions and unknowns:** Restore and verify the acquisition-cohort
partner-population link, resolve the historical identity translation, verify
the separately versioned settled-obligation denominator, and rerun the
consumer-specific evidence gate. No run has occurred.
**Approvers and authority:** Fictional role allocation only: NBX-ROLE-PRODUCT
owns publication, NBX-ROLE-PARTNER-OPS owns contract meaning, and
NBX-ROLE-RENEWAL owns fitness acceptance for the renewal decision.
