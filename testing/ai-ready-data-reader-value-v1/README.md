# AI-Ready Data Reader-Value Pilot Packet

**Packet ID:** DATA-RV-PILOT-001
**Version:** 1.2.2
**Status:** Prepared and unrun; no participant recruited or consented
**Scenario:** Harbor Grove Housing, entirely fictional

Version 1.2.2 preserves version 1.2.1's non-circular freeze order while making
the release chain and correction identity explicit and executable. It preserves
the AI-ready-data content, literal artifact identity, sealed delivery, and
staged Stage B controls. Every governed freeze follows one observable order:
complete artifacts, create their governing manifest, verify it and capture the
exact event, then create a detached verification record. Synthetic work is
defect-finding only. Version 1.2.1 remains preserved at source commit `9921757`
and version 1.2.0 at `6921313`; do not relabel an older run as 1.2.2. A 1.2.2
correction produces a new immutable artifact set, governing manifest, and
detached record rather than overwriting old evidence.
This version remains **PREPARED/UNRUN** with people and supports no
human-validation, usability, privacy, safety, readiness, value, or
incident-status claim.

## What this packet tests

This packet asks whether the plain-language AI-ready data journey helps a
practitioner and an independent decision owner move from “we have data” to a
bounded readiness decision:

`AVAILABLE -> UNDERSTANDABLE -> FIT FOR ONE USE -> TRACEABLE -> OPERABLE ->`
`DECISION-READY`

It does not replace or alter the Cedar Vale DATA-X006 candidate. Cedar Vale
continues to test detailed template routing by experienced practitioners. This
packet separately tests recognition, explanation, use-specific readiness,
failure discovery, outside-team transfer, and management/executive legibility.

## Two stages

### Stage A — practitioner or domain/product participant

Before the scored stage, complete and close the
[Consent and privacy notice](participant/01-consent-and-privacy.md). The
facilitator must copy the exact approved, immutable files into a sealed flat
Stage A input and hash every supplied file in a run-specific manifest that does
not list or hash itself. Then supply
only, in the order governed by the packet route:

1. [Packet route](participant/00-packet-route.md)
2. [Scenario and task](participant/02-scenario-and-task.md)
3. [Practitioner workbook](participant/03-practitioner-workbook.md), Section 1
   before any teaching or template asset
4. `AI-READY-DATA-JOURNEY.md`
5. `ai-data-readiness-assessment.md`
6. `data-product-contract.md`, only if the participant decides it answers a
   separate needed question
7. `06-revised-artifact-freeze-record.md`, after the revised governing
   manifest has been successfully verified; and
8. [One-Screen Handoff](participant/05-one-screen-handoff.md), only after that
   record verifies

Do not supply the Northbridge completion, the repository failure lab,
facilitator-only materials, executive brief, or value ledger during Stage A.
The short Northbridge miniature embedded inside the supplied assessment, and
inside the optional contract if opened, remains part of that supplied file.
The linked full Northbridge examples are withheld and must not be opened.

Freeze the initial detailed artifact before the live update. The planned update
creates the first revised set; it is not a correction of already frozen revised
bytes. Required revised-detail filenames are:

- `DATA-A-REVISED-WORKBOOK-v1.md`;
- `DATA-A-REVISED-READINESS-ASSESSMENT-v1.md`; and
- `DATA-A-REVISED-DATA-PRODUCT-CONTRACT-v1.md`, only when the optional contract
  was opened and completed.

Every included revised file must contain its artifact ID, version, completion
timestamp/timezone, and pre-hash state `REVISED COMPLETE`; the optional
contract is `REVISED COMPLETE` when used or `NOT USED` otherwise. No `DRAFT`,
`PENDING`, `PENDING FREEZE`, `AWAITING FREEZE`, blank, or equivalent incomplete
state may remain. A governed artifact may name its later detached record but
may not embed its own hash, the record hash, a future verification time, or
self-declare `FROZEN`. The governing manifest
`DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` hashes exactly the included revised
detail files and does not hash itself or the later detached record. Verify the
manifest, capture the exact observed timestamp/timezone, and only afterward
complete `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md` from the supplied
[detached record template](participant/06-revised-artifact-freeze-record.md).
It records that observed verification event, filenames, IDs/versions,
completion timestamps/timezones, pre-hash states, hashes, optional
disposition, and manifest filename/hash. The detached record then establishes
`FROZEN` for included exact bytes before the blank handoff opens.

Complete the handoff as `DATA-A-ONE-SCREEN-HANDOFF-v1.md` with ID/version,
completion timestamp/timezone, pre-hash `HANDOFF COMPLETE`, and a filename-only
pointer to its later detached record. Then create and verify
`DATA-A-HANDOFF-SHA256SUMS-v1.txt` over the handoff alone, capture the observed
verification time/timezone, and create
`DATA-A-HANDOFF-FREEZE-VERIFICATION-v1.md`. The sealed Stage B Phase 1 input
manifest hashes the handoff, governing manifest, and detached record.

### Stage B — independent manager or executive decision owner

Before the scored stage, complete and close a Stage B
[Consent and privacy notice](participant/01-consent-and-privacy.md). The
facilitator must copy the exact approved, immutable files and frozen Stage A
artifacts into a separate sealed Stage B input and hash every supplied file in
a run-specific manifest. After the recorded start time, supply in the route's
exact order:

1. [Packet route](participant/00-packet-route.md);
2. the frozen `DATA-A-ONE-SCREEN-HANDOFF-v1.md`, its governing manifest, and
   detached record, with the handoff opened first for substantive reading;
3. `04-decision-owner-workbook.md`;
4. after the Section 1 freeze, `02-scenario-and-task.md`,
   `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md`,
   `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`, and every revised detail named
   as included by the handoff;
5. `EXECUTIVE-DECISION-BRIEF.md`; and
6. `VALUE-AND-EVIDENCE-LEDGER.md`.

The handoff inventory, detached record, governing manifest, and delivered files
must match in literal filename, ID/version, completion timestamp/timezone,
pre-hash `REVISED COMPLETE` or optional `NOT USED` state, hash, and
detached-record `FROZEN` condition for included files. A rename, regenerated
copy, summary, substitution, omission, or mismatch stops detailed read-back.

Stage B has three scored freezes. For each export, first record its ID/version,
completion timestamp/timezone, and declared complete pre-hash state. Then hash
only the completed export in its governing manifest, verify the manifest and
capture the exact time/timezone, and only afterward create its detached record.
Use these exact triples:

| Scope | Governed artifact | Governing manifest | Detached verification record |
| --- | --- | --- | --- |
| Section 1 | `DATA-B-SECTION-1-SCAN-v1.md` | `DATA-B-SECTION-1-SHA256SUMS-v1.txt` | `DATA-B-SECTION-1-FREEZE-VERIFICATION-v1.md` |
| Section 2 | `DATA-B-SECTION-2-DETAIL-v1.md` | `DATA-B-SECTION-2-SHA256SUMS-v1.txt` | `DATA-B-SECTION-2-FREEZE-VERIFICATION-v1.md` |
| Sections 3-5 | `DATA-B-SECTIONS-3-5-DECISION-v1.md` | `DATA-B-SECTIONS-3-5-SHA256SUMS-v1.txt` | `DATA-B-SECTIONS-3-5-FREEZE-VERIFICATION-v1.md` |

The next sealed phase-input manifest hashes the prior artifact, governing
manifest, and detached record. Stage B Phase 2 specifically binds every
included revised Stage A artifact, its governing manifest, and its detached
record, in addition to the frozen Section 1 triple. The closing evidence
manifest does the same for Sections 3-5. Only after the Section 2 detached
record verifies may the executive brief and value ledger open. Keep Section 6
closed until scoring ends.

A correction after any freeze must preserve the prior artifact and use both a
new immutable filename and a new artifact ID/version. Record exact old/new
filenames, IDs/versions, hashes, reason, correction timestamp/timezone,
replacement governing manifest, and replacement detached record. Never
describe a later correction as the planned live-update revision.

The first calibration round uses a different person for Stage B. Keep the
Stage A participant unavailable during the initial read-back.

## Facilitator only

- [Facilitator guide](facilitator-only/01-facilitator-guide.md)
- [Observation and scoring rubric](facilitator-only/02-observation-and-scoring-rubric.md)
- [Results and deviation log](facilitator-only/03-results-and-deviation-log.md)

Never supply these files before the scored stages end.

## Execution prerequisites

Before recruitment, assign an accountable execution owner and approve
recruitment, consent, storage, access, retention, deletion, facilitator and
evaluator relationships, and any required ethics, legal, privacy, or
organizational review. Freeze and hash the exact packet and referenced assets.

The checked-in `SHA256SUMS` records the prepared source packet. For each stage,
the facilitator copies the exact immutable files into its sealed flat input and
creates a run-specific manifest that hashes every supplied file under its exact
local filename while excluding itself. Any byte change requires a new manifest; a meaning change
requires a new version.

See [Static protocol validation](STATIC-PROTOCOL-VALIDATION.md) for the local
temporal-order review. That review checks instructions and packet bytes; it is
not a human run or evidence that the procedure was executed successfully.

## Evidence boundary

A completed pair may reveal comprehension, routing, unsafe certainty,
readiness-boundary, and cross-role transfer defects for the exact materials and
participants. It cannot prove the data is fit, the AI system is effective or
safe, the method works broadly, or an investment will produce business value.
