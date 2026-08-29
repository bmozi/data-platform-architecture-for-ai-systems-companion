# Northbridge AI-Data Readiness Assessment — Constructed Example

<!-- markdownlint-disable MD013 -->

**Record ID:** NBX-ADR-001
**Record version:** 1.0.0
**Template:** [AI-Data Readiness Assessment](../ai-data-readiness-assessment.md)
**Template source version:** Working template bytes reviewed 2026-08-29
**Template source SHA-256:** `ce26ff34047d1ddad2a289aa30bec132b99bb7dcf3472dd3bf8d4e7726cc2a7d`
**Status:** `SCENARIO — deferred data-fitness decision; all evaluation unrun`
**Named AI use:** Generate a draft evidence summary from NBX-PERF-3.2.1 for an authorized human renewal reviewer
**Decision or action supported:** Human review only; no ranking, renewal decision, partner contact, or intervention
**System and release stage:** Fictional pre-release design review; no system executed
**Assessment owner:** NBX-ROLE-AI-DATA
**Separate release gate ID and accountable owner:** NBX-REL-AI-007, NBX-ROLE-RELEASE; unresolved and outside this assessment
**Separate model, agent, workflow, or tool-authority gate ID and accountable owner:** NBX-AUTH-AI-009, NBX-ROLE-AI-AUTHORITY; unresolved and outside this assessment

> **Constructed-example disclosure:** All details and outcomes are fictional
> scenario material. No model, retrieval path, prompt, evaluation, control, or
> release was run. This record does not establish data fitness, system safety,
> legality, usability, quality, or benefit.

**Scope guard:** Any future outcome under this record could address only the
named data version's fitness for the named draft-summary use. It could not
approve the model, workflow, interface, human-review design, tool authority,
partner decision, consequential action, or release.

## 1. Use boundary

- **Users and affected parties:** Fictional authorized renewal reviewers and
  partner organizations represented in the evidence.
- **Model or retrieval role:** Structured product fields supplied as context to
  draft a traceable summary. The model is not a source of partner facts.
- **Consequence and reversibility:** A misleading draft could affect reviewer
  attention. The draft must be reviewable, discardable, and unable to commit a
  renewal or contact a partner.
- **Human review or escalation:** NBX-ROLE-RENEWAL checks cited evidence and may
  reject the draft. Semantic or population disputes route to the authorities
  named in NBX-SAR-001 and NBX-DPC-001.
- **Prohibited outputs or uses:** Partner ranking, eligibility determination,
  adverse characterization, autonomous action, training reuse, or disclosure
  outside the renewal purpose.
- **Required abstention or stop conditions:** Missing source citation,
  unresolved identity or meaning, failed cohort coverage, broken provenance,
  expired purpose, unsupported inference, or unavailable human review.

## 2. Meaning and fitness

| Required information | Meaning authority | Intended representation | Known ambiguity, bias, or gap | Fitness evidence |
| --- | --- | --- | --- | --- |
| Contractual on-time classification | NBX-SAR-001 / NBX-ROLE-PARTNER-OPS | Value plus semantic version and source references | Acquisition-era identity translation unresolved | `SCENARIO CONDITIONAL`; no executed evidence |
| Eligible renewal population | NBX-ROLE-RENEWAL | Versioned partner-population object and cohort | Partner-population artifact deliberately missing in NBX-PVR-001 | `SCENARIO FAIL`; no executed evidence |
| Eligible settled obligations within one included partner | NBX-ROLE-PARTNER-OPS | NBX-SRC-OBLIGATION-11 and NBX-TR-OBLIG-DENOM-03 | Scenario references are present, but integrity and reconstruction are unrun | `SCENARIO PRESENT/UNRUN`; no executed evidence |
| Cohort coverage | NBX-QES-001 / NBX-ROLE-RENEWAL | Per-cohort reconciliation and explicit unknowns | Acquisition-era cohort red while aggregate display appears green | `SCENARIO FAIL`; no executed evidence |
| Exception rationale | NBX-ROLE-PARTNER-OPS | Approved code, rule version, and citation | Service and contract exceptions differ | `SCENARIO UNKNOWN`; protocols unrun |

- **Training, evaluation, retrieval, context, or monitoring role:**
  Inference-time context for a draft summary; not training, fine-tuning,
  labeling, or autonomous action.
- **Population and coverage limits:** Only eligible SCENARIO-Q3 partner-contract
  relationships with resolved source, identity, semantic, and purpose evidence.
- **Temporal validity:** Only NBX-PERF-3.2.1 at the declared cutoff; no live or
  future-state claim.

## 3. Provenance and reproducibility

- **Source and version evidence:** Required by NBX-PVR-001; partner-population
  source NBX-SRC-RENEWAL-03 is deliberately absent. The separate
  settled-obligation source NBX-SRC-OBLIGATION-11 is named as a scenario
  reference; no integrity or reconstruction check has run.
- **Transformation and feature lineage:** Planned NBX-TR-RENEWAL-12 and
  NBX-CTX-RENEWAL-02 references; not executed.
- **Document, chunk, embedding, and index versions:** Not applicable to this
  bounded structured-context scenario. If retrieval is added, a new assessment
  is required.
- **Labels or annotations and authority:** Contract classifications bind to
  NBX-SAR-001. No generated label may replace an unresolved authority decision.
- **Ability to reconstruct a result:** `SCENARIO INSUFFICIENT` under
  NBX-PVR-001; no result exists to reconstruct.
- **Correction and deletion propagation:** Required through the product-version
  and decision-package chain; behavior untested.

## 4. Rights, access, and purpose

- **Classification and sensitivity:** `SCENARIO — restricted internal partner
  information`.
- **Approved collection and use purpose:** Existing scenario authority covers
  human renewal analysis. Whether it covers AI-assisted draft generation is
  unresolved under NBX-POL-PURPOSE-08 and must not be inferred from read access.
- **Consent, contract, policy, or other authority:** Fictional policy decision
  required; this record supplies no legal conclusion.
- **Tenant, subject, row, column, and document entitlements:** Named reviewer,
  partner rows within assignment, excluded direct contact fields, and
  purpose-bound context assembly.
- **Derived-data and model-output restrictions:** Drafts inherit the restricted
  purpose, may not be used for training, and must retain product and evidence
  references.
- **Retention and deletion:** Subject to the separate fictional retention
  decision. No schedule is declared legally sufficient.

## 5. Quality and evaluation

| Risk or required behavior | Dataset/evaluation design | Threshold or acceptance rule | Result | What remains unknown |
| --- | --- | --- | --- | --- |
| Omitted cohort | Per-cohort partner-population reconciliation before context assembly | Any unexplained eligible-partner omission stops use | `SCENARIO FAIL`; authored fixture, not a run | Detection behavior and other cohorts |
| Unsupported statement | Compare every draft statement with supplied product fields and cited evidence | No unsupported partner claim; abstain where evidence is unknown | `UNRUN` | Model behavior, reviewer detection, burden |
| Meaning substitution | Include competing meanings and unresolved historical mapping in negative cases | Never convert `unknown` or buyer meaning to contract result | `UNRUN` | Error and abstention rates |
| Broken evidence link | Remove one provenance edge from the fixture | Context assembly must stop before generation | `UNRUN`; break exists only as a scenario condition | Whether any control detects it |
| Purpose or role change | Vary reviewer role and purpose independently | Deny context when either is outside scope | `UNRUN` | Enforcement and false denials |

- **Slice/cohort coverage:** Acquisition cohort is mandatory and currently
  fails the scenario condition.
- **Leakage and contamination checks:** Planned; no corpus or model run exists.
- **Staleness and drift monitoring:** Product, semantic, purpose, and cutoff
  changes require reassessment; no monitor was evaluated.
- **Retrieval attribution and citation checks:** Structured source references
  required in every draft; behavior unrun.
- **Adversarial and misuse tests:** Ranking prompt, autonomous-action request,
  cross-partner access, stale version, unsupported causal claim, and missing
  citation are planned negative cases only.

## 6. Operational control

- **Refresh and version policy:** Pin one approved product version; any source,
  semantic, denominator, transformation, purpose, or model change requires a
  fresh assessment.
- **Stop-trust signals:** NBX-QES-001 failure, NBX-PVR-001 insufficiency,
  unresolved purpose, missing citation, reviewer unavailable, or release-gate
  withdrawal.
- **Incident owner:** Not assigned to a person; fictional role
  NBX-ROLE-AI-OPERATIONS is proposed only.
- **Rollback, quarantine, or disabling path:** Required in NBX-REL-AI-007 but
  not designed or executed. The current state is no release.
- **Reassessment triggers:** Repair of the cohort and provenance evidence,
  purpose decision, semantic change, new data role, model or context change,
  or proposed action authority.

## 7. Decision

**Outcome:** `SCENARIO — defer data fitness for NBX-PERF-3.2.1 and the named
draft-summary use.`
**Scope and conditions:** The narrow role is defined, but NBX-QES-001 stops the
consumer use, NBX-PVR-001 is insufficient, and AI-assisted-purpose authority is
unresolved. Repair does not imply approval; it only permits reconsideration.
**Rejected or unresolved uses:** Training, ranking, autonomous outreach,
renewal decisions, partner intervention, and all other product versions.
**Evidence required to expand scope:** Authorized purpose, restored
partner-population chain, pinned settled-obligation denominator, resolved or
preserved historical unknowns, executed cohort checks, negative AI-use tests,
independent review, and retained limitations.
**Data-fitness approvers and authority:** Fictional NBX-ROLE-AI-DATA with
NBX-ROLE-RENEWAL acceptance and the separate semantic, security, and purpose
authorities. No person accepted this role.
**Separate gates still required or unresolved:** NBX-REL-AI-007 and
NBX-AUTH-AI-009 remain unresolved. No data decision may change their state.
