# AI-Ready Data Reader-Value Pilot Packet

**Packet ID:** DATA-RV-PILOT-001
**Version:** 1.2.0
**Status:** Prepared and unrun; no participant recruited or consented
**Scenario:** Harbor Grove Housing, entirely fictional

Version 1.2.0 adds literal revised-artifact identity, a detached freeze record,
and exact Stage B transfer after a synthetic protocol audit of version 1.1.1.
It preserves the material interpretation and the sealed-delivery and staged
Stage B controls added in version 1.1.1. Synthetic work is defect-finding only.
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
7. `06-revised-artifact-freeze-record.md`, after the live-update revision; and
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
state may remain, and no revised artifact may self-declare `FROZEN`. The governing manifest
`DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` hashes exactly the included revised
detail files and does not hash itself. Complete
`DATA-A-REVISED-FREEZE-RECORD-v1.md` from the supplied
[detached record template](participant/06-revised-artifact-freeze-record.md).
It must verify freeze timestamp/timezone, filenames, IDs/versions, completion
timestamps/timezones, pre-hash states, hashes, optional disposition, and
manifest filename/hash and then establish `FROZEN` for included artifacts
before the blank handoff opens. Complete and separately freeze the handoff as
`DATA-A-ONE-SCREEN-HANDOFF-v1.md`.

### Stage B — independent manager or executive decision owner

Before the scored stage, complete and close a Stage B
[Consent and privacy notice](participant/01-consent-and-privacy.md). The
facilitator must copy the exact approved, immutable files and frozen Stage A
artifacts into a separate sealed Stage B input and hash every supplied file in
a run-specific manifest. After the recorded start time, supply in the route's
exact order:

1. [Packet route](participant/00-packet-route.md);
2. the frozen `DATA-A-ONE-SCREEN-HANDOFF-v1.md` first;
3. `04-decision-owner-workbook.md`;
4. after the Section 1 freeze, `02-scenario-and-task.md`,
   `DATA-A-REVISED-FREEZE-RECORD-v1.md`,
   `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`, and every revised detail named
   as included by the handoff;
5. `EXECUTIVE-DECISION-BRIEF.md`; and
6. `VALUE-AND-EVIDENCE-LEDGER.md`.

The handoff inventory, detached record, governing manifest, and delivered files
must match in literal filename, ID/version, completion timestamp/timezone,
pre-hash `REVISED COMPLETE` or optional `NOT USED` state, hash, and
detached-record `FROZEN` condition for included files. A rename, regenerated
copy, summary, substitution, omission, or mismatch stops detailed read-back.

Stage B has three scored freezes. Export and checksum-freeze Section 1 as
`DATA-B-SECTION-1-SCAN-v1.md` from the one-screen handoff alone. Then verify
the exact revised-detail transfer, complete Section 2, and export and
checksum-freeze `DATA-B-SECTION-2-DETAIL-v1.md`. Only after that second freeze
may the executive brief and value ledger open; complete Sections 3-5, export
`DATA-B-SECTIONS-3-5-DECISION-v1.md`, and checksum-freeze it. Keep Section 6
closed until scoring ends.

A correction after any freeze must preserve the prior artifact and use a new
immutable filename. Record exact old/new filenames, IDs/versions, hashes,
reason, correction timestamp/timezone, replacement freeze record, and
replacement manifest. Never describe a later correction as the planned
live-update revision.

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

## Evidence boundary

A completed pair may reveal comprehension, routing, unsafe certainty,
readiness-boundary, and cross-role transfer defects for the exact materials and
participants. It cannot prove the data is fit, the AI system is effective or
safe, the method works broadly, or an investment will produce business value.
