# Northbridge Quality-Evidence Scorecard — Constructed Example

<!-- markdownlint-disable MD013 -->

**Record ID:** NBX-QES-001
**Record version:** 1.0.0
**Template:** [Quality-Evidence Scorecard](../quality-evidence-scorecard.md)
**Template source version:** Revision 2 working template
**Template source SHA-256:** `2f84e13d131da06771011ab694ce1abce0f94d8f15591019a2858bf3545a7d16`
**Status:** `SCENARIO — authored failing condition; all protocols unrun`
**Data product and version:** NBX-PERF-3.2.1
**Consumer use:** Human review of individual partner-renewal evidence in SCENARIO-Q3
**Decision owner:** NBX-ROLE-RENEWAL
**Assessment interval:** SCENARIO-Q3 settlement cutoff
**Event-time, effective-time, or processing-time basis:** Event time with effective contract time and a fixed processing cutoff
**Supported population and denominator:** Population is the eligible partner-contract relationships declared by NBX-SRC-RENEWAL-03; each included partner's rate denominator is the eligible settled obligations in NBX-SRC-OBLIGATION-11
**Declared exclusions and unknowns:** Open obligations, unresolved identities, and unresolved acquisition-era translations remain explicit unknowns, not silent exclusions

> **Constructed-example disclosure:** The values below are fictional inputs
> written to expose a decision. `SCENARIO PASS` and `SCENARIO FAIL` are not
> detector outputs, experiment results, or proof of fitness or harm.

## 1. Use and consequence

- **Decision, automation, analysis, or model supported:** Human consideration
  of partner renewal. No automated renewal or ranking is supported.
- **Consumers and affected subjects:** Fictional renewal reviewers and partner
  organizations represented in the scenario records.
- **Consequence of false positive, false negative, omission, delay, or drift:**
  A partner's evidence could be overstated, understated, omitted, stale, or
  compared under the wrong rule.
- **Use-specific stop-trust condition:** Stop partner-level renewal use when any
  eligible partner or required acquisition cohort cannot be reconciled to the
  declared partner population, or when an included partner's obligations cannot
  be reconciled to the distinct obligation denominator and semantic version.

## 2. Executable quality policy

| Named dimension or objective | Population, denominator, and exclusions | Indicator/query/probe, version, and numerator or rule | Time basis and window | Measurement point, evidence source, and dependencies | Threshold and rationale | Breach action and owner |
| --- | --- | --- | --- | --- | --- | --- |
| NBX-QM-ALL-01 completeness | All declared eligible partner-contract relationships; no silent cohort exclusion | NBX-QRY-RECON-04; matched eligible partner IDs / declared eligible partner IDs | SCENARIO-Q3 cutoff | Publication gate; NBX-SRC-RENEWAL-03; identity map NBX-SRC-IDENTITY-09 | 100% accounted for as present, validly excluded, or explicit unknown; individual renewal cannot tolerate unexplained omission | Stop publication; NBX-ROLE-RENEWAL owns decision, NBX-ROLE-RELIABILITY investigates |
| NBX-QM-COHORT-04 cohort coverage | Each acquisition cohort separately | Same reconciliation grouped by acquisition cohort; no averaging across cohorts | SCENARIO-Q3 cutoff | Publication gate; cohort key and effective identity mapping | No cohort with unexplained missing eligible partner | Quarantine affected publication and preserve negative result |
| NBX-QM-RULE-02 validity | Scored settled obligations | Resolved contract, semantic, exception, and identity versions / scored obligations | Obligation event time plus cutoff | Transformation output; NBX-SAR-001 and NBX-TR-RENEWAL-12 | 100% resolved or classified `unknown`; never coerce unknown to pass/fail | Stop affected partner score; NBX-ROLE-PARTNER-OPS resolves meaning |
| NBX-QM-FRESH-03 timeliness | Corrections eligible within the declared settlement window | Corrections incorporated by cutoff / eligible corrections received | Processing cutoff | Ingestion log and source snapshot | All eligible corrections incorporated or explicitly disclosed | Defer publication or disclose a narrower frozen window |
| NBX-QM-PROV-05 reconstruction coverage | Every published partner score | Required retained links present / required links listed in NBX-PVR-001 | Publication version | Evidence package before decision | All required links present for consequential partner score | Stop use and repair the evidence package |
| NBX-QM-DENOM-06 obligation-denominator integrity | Eligible settled obligations within each included partner-contract relationship; open obligations excluded explicitly | Obligations accounted for under NBX-TR-OBLIG-DENOM-03 / obligations in NBX-SRC-OBLIGATION-11 | Obligation event time and SCENARIO-Q3 settlement cutoff | Partner-rate assembly; obligation manifest, contract version, and NBX-SAR-001 | Every included or excluded obligation has a reason and version; no silent denominator loss | Stop the affected partner rate; NBX-ROLE-RELIABILITY investigates and NBX-ROLE-PARTNER-OPS resolves meaning |

## 3. Evidence coverage

| Objective/measure ID and evidence reference | Result | Population and exclusions | False-alarm evidence | Miss/negative/mutation evidence | Last challenged | What it does not prove | Retention |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NBX-QM-ALL-01 / NBX-EV-Q01 | `SCENARIO aggregate display: green` | Aggregate row count only; not the declared partner population | None; protocol unrun | Authored acquisition-cohort mutation shows why aggregate count can mislead | Never; unrun | Completeness, correct meaning, or cohort coverage | No result exists; future retention authority and interval required |
| NBX-QM-COHORT-04 / NBX-EV-Q02 | `SCENARIO FAIL` | Acquisition-era cohort has an unresolved partner population and identity translation | None; protocol unrun | The missing cohort is the authored negative fixture, not a detected incident | Never; unrun | Detector sensitivity, actual omission, or consequence | No result exists; future retention authority and interval required |
| NBX-QM-RULE-02 / NBX-EV-Q03 | `SCENARIO CONDITIONAL` | Current-contract cohorts only; acquisition-era mapping unknown | None; protocol unrun | Missing historical mapping should preserve `unknown` | Never; unrun | Correctness or completeness of the fictional rules | No result exists; future retention authority and interval required |
| NBX-QM-FRESH-03 / NBX-EV-Q04 | `SCENARIO UNKNOWN` | No executed correction-window test | None | No mutations executed | Never; unrun | Timeliness | No result exists; future retention authority and interval required |
| NBX-QM-PROV-05 / NBX-PVR-001 | `SCENARIO FAIL` | Named renewal product; eligible-partner population snapshot missing while the settled-obligation source is named separately | None; protocol unrun | Deliberately removed partner-population link is an authored fixture | Never; unrun | Reconstruction behavior or detection | No result exists; future retention authority and interval required |
| NBX-QM-DENOM-06 / NBX-EV-Q06 | `SCENARIO PRESENT/UNRUN` | Settled-obligation denominator for an included partner; no executed reconciliation | None; protocol unrun | Future mutation would omit, duplicate, or reclassify one obligation | Never; unrun | Denominator correctness, detector behavior, or partner-population completeness | No result exists; future retention authority and interval required |

## 4. Response and recovery

- **Warn, quarantine, stop publication, degrade, or continue conditionally:** Stop
  partner-level renewal use and quarantine NBX-PERF-3.2.1. A separately
  authorized aggregate trend could be considered only after its own contract
  and evidence gate; this record does not authorize it.
- **Consumer notification:** Fictional NBX-ROLE-PRODUCT sends the stopped-use
  notice, affected cohort, missing evidence, and next review trigger to
  NBX-ROLE-RENEWAL.
- **Correction, replay, and backfill:** Restore the versioned partner
  population; pin the separate settled-obligation denominator; resolve or
  preserve unknown historical identities; rerun the declared reconciliations;
  publish a new product version only after review.
- **Historical restatement:** Preserve NBX-PERF-3.2.1 as stopped, link any
  corrected successor, and identify potentially affected scenario decisions.
- **Root-cause and recurrence evidence:** Retain the missing-link condition,
  failed cohort state, query version, false-alarm and miss results if later run,
  decision, owner, and any bypass attempt.

## 5. Decision

- **Current fitness:** `SCENARIO — unfit for partner-level renewal use in the
  authored condition; protocols remain unrun`.
- **Conditions:** Restore and freeze the partner-population source
  NBX-SRC-RENEWAL-03, resolve the historical translation or keep the cohort
  unknown and excluded from the decision, freeze the distinct obligation
  source NBX-SRC-OBLIGATION-11, then execute the predeclared checks under an
  authorized DATA-X protocol.
- **Unmeasured risks:** All control performance, false alarms, misses, other
  cohorts, operational burden, usability, legal sufficiency, and real outcomes.
- **Evidence owner:** Fictional NBX-ROLE-RELIABILITY.
- **Review date or trigger:** Evidence-package repair and a separately
  authorized run; no date is implied.
- **Last challenge outcome and retained gaps:** No challenge occurred. The
  constructed negative fixture retains the cohort and provenance gaps.

## Cross-record effects

The stop applies to NBX-DPC-001 and prevents NBX-ADR-001 from approving the
named data version. NBX-SAR-001 defines the unresolved historical translation.
NBX-PVR-001 identifies the missing partner-population evidence and the distinct
settled-obligation denominator. Completing this
scorecard does not change DATA-X002, DATA-X005, or DATA-X006 from `unrun`.
