# Stage B Decision-Owner Workbook

**Packet:** DATA-RV-PILOT-001 version 1.2.6
**Status:** Blank independent read-back record

- Reviewer code:
- Broad role and experience band, optional:
- Stage A exact revised filenames, IDs/versions, states, and hashes:
- Exact Stage B start recorded before first scored file opened, with timezone:
- End time and timezone:
- Sealed Stage B input manifest:
- Undeclared orchestration, facilitator, hidden-prompt, or run-note file
  present: none / stop and deviation
- Prior involvement with Stage A: none required for first calibration

Do not ask the Stage A participant to explain or repair the artifact until
Sections 1–5 are frozen.

Never silently replace a frozen workbook. For any correction after a freeze,
preserve the old file and use a new immutable filename and a new artifact
ID/version. Record exact old/new immutable filenames, IDs/versions, hashes,
reason, correction timestamp/timezone, replacement detached verification
record, and replacement manifest in the run log. The planned Stage A
live-update revision is not a post-freeze correction.

## 1. One-screen scan

Read the frozen one-screen handoff before the scenario or detailed artifacts.
Answer from that handoff alone.

- Exact use and beneficiary:
- Current bounded decision:
- What the assistant may search and what is withheld:
- Owner, or `UNASSIGNED`:
- Assigning/acting authority, or `UNKNOWN`:
- Evidence known and still unknown:
- Unacceptable outcome and immediate next action:
- Review date or evidence trigger:
- Could you find those items on one screen without verbal repair? yes / partly /
  no
- Missing, ambiguous, or terminology-dense item:

Complete this scan before opening the scenario or detailed Stage A work.

- Export filename: `DATA-B-SECTION-1-SCAN-v1.md`
- Section 1 artifact ID/version:
- Section 1 completion timestamp/timezone:
- Section 1 pre-hash state: `SECTION 1 COMPLETE`
- Post-hash verification provenance: see
  `DATA-B-SECTION-1-FREEZE-VERIFICATION-v1.md`, created only after
  `DATA-B-SECTION-1-SHA256SUMS-v1.txt` verifies

Finalize the export before hashing. Do not put its own hash, a future
verification timestamp, or `FROZEN` inside it.

## 2. Detailed read-back

Before answering, verify `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md`,
`DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`, and every included
handoff-linked revised detail. Literal filenames, IDs/versions, completion
timestamps/timezones, pre-hash `REVISED COMPLETE` states, hashes, and
detached-record `FROZEN` conditions must match. The optional contract must be
consistently `NOT USED` or present as `REVISED COMPLETE` and later frozen.
Reject a rename, regenerated copy, summary, substitution, omission, mismatch,
premature artifact self-declaration of `FROZEN`, or absent freeze.

- Revised transfer verification: pass / stop / deviation ID

- What exact AI use is being considered?
- Which information is allowed to influence it?
- Which information or use is prohibited?
- What does “ready” mean here?
- When must the system abstain or stop trusting the information?
- Who has final say on meaning, correction, operation, and the readiness
  decision? Use `UNASSIGNED` where no owner exists.
- Which model, action, and release gates remain separate?

Complete and govern Section 2 before opening `EXECUTIVE-DECISION-BRIEF.md` or
`VALUE-AND-EVIDENCE-LEDGER.md`.

- Export filename: `DATA-B-SECTION-2-DETAIL-v1.md`
- Section 2 artifact ID/version:
- Section 2 completion timestamp/timezone:
- Section 2 pre-hash state: `SECTION 2 COMPLETE`
- Post-hash verification provenance: see
  `DATA-B-SECTION-2-FREEZE-VERIFICATION-v1.md`, created only after
  `DATA-B-SECTION-2-SHA256SUMS-v1.txt` verifies

Finalize the export before hashing. Do not put its own hash, a future
verification timestamp, or `FROZEN` inside it.

## 3. Investment legibility

- Capability this information could unlock:
- Beneficiary:
- Current friction or exposure:
- Specific readiness gaps requiring investment:
- Operating commitment after a pilot:
- Largest unacceptable outcome:
- Baseline or value evidence available now:
- Benefit, cost, or burden still unknown:

## 4. Bounded decision

Choose one: `EXPLORE` / `PROCEED BOUNDED` / `INVEST` / `HOLD` / `STOP`

- Scope and conditions:
- Withheld uses or authority:
- Evidence required before expansion:
- Accountable owner, or `UNASSIGNED`:
- Assigning or acting authority, or `UNKNOWN`:
- Reconsideration date or evidence-based trigger:

Do not invent an owner, authority, or date. An explicit gap is valid decision
evidence.

## 5. Transfer finding

- Could you make the decision without verbal repair? yes / partly / no
- Missing or ambiguous information:
- Technical language that obscured value or exposure:
- Universal-readiness or ROI claim that lacked support:
- One-screen item that required the detailed artifacts to discover:
- Smallest change that would improve the handoff:

Export Sections 3-5 together as `DATA-B-SECTIONS-3-5-DECISION-v1.md` and
complete its manifest/verification sequence before any debrief or Stage A
explanation.

- Sections 3-5 artifact ID/version:
- Sections 3-5 completion timestamp/timezone:
- Sections 3-5 pre-hash state: `SECTIONS 3-5 COMPLETE`
- Post-hash verification provenance: see
  `DATA-B-SECTIONS-3-5-FREEZE-VERIFICATION-v1.md`, created only after
  `DATA-B-SECTIONS-3-5-SHA256SUMS-v1.txt` verifies

Finalize the export before hashing. Do not put its own hash, a future
verification timestamp, or `FROZEN` inside it. The closing evidence manifest
later hashes the completed export, governing manifest, and detached record.

## 6. Debrief after scoring

Keep this section closed until the facilitator records
`STAGE_B_SCORING_ENDED` and verifies
`DATA-B-PHASE-4-DEBRIEF-INPUT-SHA256SUMS-v1.txt` over the frozen Sections 3-5
artifact, its governing manifest, its detached record, and this exact debrief
input. Debrief access before both events is a stop.

- Stage A explanation that changed your interpretation:
- Decision changed after discussion:
- Why:

Export this section separately as exactly `DATA-B-SECTION-6-DEBRIEF-v1.md`.
Record its completion timestamp/timezone and state `DEBRIEF COMPLETE`. Do not
edit Sections 1-5 or use the debrief to upgrade a frozen score. After export,
stop; the facilitator owns every later route-boundary event in the external
execution/access log and run results.

## Frozen-artifact correction register

Use this only for a later change to already frozen bytes, never for the planned
live-update revision.

| Section | Reason | Correction timestamp/timezone | Exact old filename, ID/version, SHA-256 | Exact new filename, ID/version, SHA-256 | Replacement detached record and manifest |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
