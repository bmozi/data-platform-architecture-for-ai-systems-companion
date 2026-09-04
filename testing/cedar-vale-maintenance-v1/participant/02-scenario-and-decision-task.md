# Cedar Vale Scenario and Decision Task

<!-- markdownlint-disable MD013 -->

**File ID:** DATA-TEST-CVM-SCENARIO-001
**File version:** 1.0.0
**Packet:** DATA-TEST-CVM-001 version 1.0.0
**Status:** Fictional participant fixture; `UNRUN`
**Recommended participant role:** Data architect, analytics engineer, data
product lead, governance practitioner, or equivalent
**Timebox:** To be declared by the authorized execution owner before use

## Disclosure

Cedar Vale Conservatory, every identifier, record, role, number, defect, and
decision below are constructed. Nothing is observed history, a legal opinion,
an experiment result, a safety claim, or John Briggs's experience.

## Your task

You are reviewing whether one versioned data package is fit for one named AI
role. Choose the **smallest useful subset** of the five illustrative companion
templates. Do not fill a template merely because it is available. For each
chosen asset, record the bounded decision the scenario permits, what remains
unknown, and the stop or reconsideration trigger.

The named AI role is:

> Use the current approved-procedure corpus, CVM-CORPUS-MANUALS-2.0.0, as
> context for a proposed system that drafts a non-authoritative inspection
> checklist for a human technician assigned to current-generation pump model
> CV-PUMP-G3. The technician must inspect the cited procedure before use. The
> proposed system cannot issue a work order, declare an inspection complete,
> alter equipment, schedule maintenance, or rank failure risk.

The decision under review is data fitness for that role. Model behavior,
interface design, workflow authority, physical safety, technician procedure,
and release are separate decisions.

## Illustrative assets available

- [Data-Product Contract](../../../data-product-contract.md)
- [Semantic-Authority Record](../../../semantic-authority-record.md)
- [Quality-Evidence Scorecard](../../../quality-evidence-scorecard.md)
- [AI-Data Readiness Assessment](../../../ai-data-readiness-assessment.md)
- [Provenance Requirements](../../../provenance-requirements.md)

Use the [response workbook](03-response-workbook.md) to select and apply assets.

## Scenario context

Cedar Vale is a fictional conservatory with three generations of water-
circulation equipment. Its facilities group already has a versioned internal
information promise, CVM-DPC-BASE-004 version 2.1.0: current approved procedures
support technician preparation for assigned equipment. The supplied record
also names its consumer, support owner, current purpose, and retirement rule.
Its fictional purpose addendum, CVM-PURPOSE-12 version 1.1.0, permits the exact
current-procedure data to be supplied as context for a non-authoritative draft
reviewed by the assigned technician. The addendum does not approve a model,
workflow, interface, physical procedure, action, or release. Decide from these
facts whether the named task needs a new or changed information-promise record.

The review package contains four fixture groups.

### A. Procedure corpus proposed for the named use

- Corpus ID: CVM-CORPUS-MANUALS-2.0.0.
- Population: twelve fictional procedure documents for CV-PUMP-G3.
- Each document carries a stable document ID, revision, effective interval,
  equipment-model scope, fictional facilities-engineering authority, status,
  and source-object reference.
- Scenario inventory CVM-MANIFEST-PROC-020 accounts for all twelve expected
  current CV-PUMP-G3 procedures. Superseded revisions are excluded from the
  current alias but retained in the fictional history set.
- The named corpus excludes work orders, inspection outcomes, staff notes,
  incident narratives, personal information, and prior risk scores.
- The fictional CVM-PURPOSE-12 record permits the exact current procedures to
  be supplied as context for the named draft-checklist role and assigned
  technician. It does not decide whether a system is ready to perform that
  role.
- No retrieval, generation, citation, entitlement, abstention, usability,
  security, release, or field-use test has run. The package states only the
  data-side conditions the scenario author wants reviewed.

### B. Work-order field

The work-order feed includes `inspection_complete`. Maintenance coordinators
use it to mean every scheduled checklist item was recorded. Technicians use it
to mean the physical inspection occurred and unresolved hazards were
escalated. A vendor export sets it when a mobile form is submitted.

No accountable Cedar Vale role is named for defining or changing the shared
term. Technical custody belongs to the maintenance-platform team, but the
scenario gives that team no authority to settle the operational meaning. The
term is not required in CVM-CORPUS-MANUALS-2.0.0 and must not be used by the
named checklist-drafting role. A later proposal may seek to use it for
inspection status or model evaluation.

### C. Historical risk-table fixture

A separate historical failure-risk table, CVM-RISK-1.4.0, shows an aggregate
fixture value labeled `SCENARIO 98% work-order linkage`. The legacy
CV-PUMP-G1 cohort has a fixture condition labeled `SCENARIO 61% linkage`
because predecessor controller identifiers were not fully mapped. No detector
produced these values; they are authored conditions.

The facilities group had proposed using CVM-RISK-1.4.0 to compare failure risk
across all pump generations. Decide what the two supplied linkage conditions
permit or stop for that proposal. CVM-RISK-1.4.0 is not part of the named
CV-PUMP-G3 procedure corpus and is not needed to draft the bounded checklist.

### D. Archived risk-output fixture

One archived risk output, CVM-RISK-OUT-778, names transformation
CVM-TR-RISK-11 but does not retain the effective predecessor-controller mapping
version. Decide what may and may not be reconstructed from the retained chain.
The output is not part of CVM-CORPUS-MANUALS-2.0.0. The scenario provides no
basis to substitute today's mapping for the absent historical version.

For the proposed procedure corpus, all twelve source-object references,
document revisions, authority records, effective intervals, model scopes, and
manifest entries are present as scenario facts. No executed reconstruction or
integrity test is claimed.

## Separate unresolved gates

- CVM-AI-REL-004 — proposed system release; accountable owner not yet assigned.
- CVM-AI-AUTH-006 — model, workflow, and tool-authority review; accountable
  owner not yet assigned.
- CVM-AI-SAFE-003 — equipment-safety and field-procedure review; accountable
  owner not yet assigned.

None can be approved by a data-fitness record. The absence of accountable
owners is a stop for release, not an instruction to invent owners.

## Constraints

- Do not assume access implies permission for AI-mediated use.
- Do not claim that scenario inventory proves real completeness or control
  effectiveness.
- Preserve every supplied meaning, cohort-specific condition, absent historical
  version, and unresolved separate gate without silently repairing it.
- A bounded data-fitness pass may coexist with a stopped release when the data
  decision is narrower and its conditions are met.
- It is acceptable—and expected—to mark fields not applicable with a reason.
- Do not invent law, policy, approval, test execution, or organizational facts.

## No-coaching rule

Once the timed attempt begins, the facilitator may clarify file location,
record a technical access problem, or restate these written instructions. The
facilitator may not recommend an asset, interpret a field, identify a defect,
name the expected decision, or confirm whether an answer is correct. Record all
requests and any supplied help. Stop on unblinding, fixture drift, missing
consent, confidentiality risk, or material tool failure.

## Deliverable

Submit one response workbook plus completed copies of only the templates you
selected. Do not overwrite the blank templates or this fixture. Give every
output a participant-assigned file ID and version. Label every conclusion
`SCENARIO DECISION`, every absent result `UNRUN`, and every unresolved fact
`UNKNOWN` or `DISPUTED` as appropriate.
