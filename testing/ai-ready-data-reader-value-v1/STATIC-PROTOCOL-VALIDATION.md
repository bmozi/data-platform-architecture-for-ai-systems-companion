# Static Temporal-Protocol Validation

**Packet:** DATA-RV-PILOT-001 version 1.2.8
**Review date:** 2026-08-30
**Result:** PASS for static source instructions after repository validation
**Evidence class:** Local static inspection, not a participant run

## Invariants checked

The packet route, facilitator guide, workbooks, handoff, detached-record
template, rubric, results log, protocol inventory, execution/access log, and
packet README, synthetic-context template, layout-proof template, synthetic
exact-file helper and plan, and structured protocol were checked for the same sequence in all six governed scopes and the
larger participant/run route:

1. initial and revised Stage A artifacts record ID/version, completion
   timestamp/timezone, and their declared complete state before hashing;
2. the Stage A handoff records the same completion metadata and `HANDOFF
   COMPLETE` before hashing;
3. Stage B Section 1, Section 2, and Sections 3-5 each record their declared
   complete pre-hash state and completion metadata before hashing;
4. each governing manifest hashes only the completed governed artifact or
   artifacts, never itself or its later record;
5. the manifest is verified and its exact command, complete output, exit code,
   observed timestamp/timezone, actors, and facilitator are captured before a
   detached verification record is created;
6. every detached record has attempt and phase identity plus an explicitly
   later record-completion timestamp/timezone;
7. the facilitator-only execution/access log records ordered gates, opens,
   completions, manifest events, verification evidence, record events, actors,
   filenames, timestamps/timezones, and continuity bindings while remaining
   outside participant input; and
8. the Stage A revision-phase manifest binds both required initial artifacts,
   the optional initial contract exactly when used and included in the initial
   governing manifest, that manifest, detached record, and exact immutable
   `DATA-A-LIVE-UPDATE-v1.md`, and verifies before the update opens; and
9. the next sealed phase-input or closing evidence manifest hashes the governed
   artifact, governing manifest, and detached record under literal filenames.
10. one mutually exclusive entry branch is selected before `RUN_STARTED`:
    real completed consent for `HUMAN`, or exact immutable
    `DATA-SYNTHETIC-CONTEXT-v1.md` plus its verified manifest for `SYNTHETIC`,
    with no fictional human-consent or human-result claim;
11. a synthetic-only byte-exact helper is selected and orchestration/context
    bound before `RUN_STARTED`; each current-phase config binds the exact
    verified sealed-input manifest filename, absolute path, and observed hash,
    and its ordered-file membership/hashes must equal that manifest on every
    invocation; its helper/config manifest verifies before the phase gate,
    every grant/refusal is logged with a serialized write-all append and fsync
    and reconciled, and no absent/drifted/wrong manifest, future/dummy hash,
    config-after-gate, general command, direct read, or ad hoc message delivery
    is allowed; helper compliance does not establish host-platform restriction,
    cross-process security isolation, or sandbox security;
12. exact Stage A and Stage B context/start checkpoints, Stage A material
    feedback/end, Stage B scoring end, gated Section 6 debrief, Stage B end,
    immutable results completion, and log close are recorded in order;
13. `DATA-B-PHASE-4-DEBRIEF-INPUT-SHA256SUMS-v1.txt` binds the final scored
    artifact/manifest/record triple plus exact `04-decision-owner-workbook.md`
    before exact `DATA-B-SECTION-6-DEBRIEF-v1.md` opens;
14. exact immutable `DATA-RUN-RESULTS-v1.md` reaches `RESULTS COMPLETE` before
    `LOG_CLOSED` without predicting the final log hash or a future closeout;
15. later external `DATA-RUN-CLOSEOUT-v1.md` binds observed hashes for the
    byte-identical closed log, the verified closeout manifest, and results; and
16. a favorable one-page claim requires a retained proof for one US Letter
    portrait PDF, margins at least 0.5 inch, body text at least 9 points,
    no more than 450 reader-facing words excluding only immutable provenance,
    and no clipping, overlap, hidden overflow, or unreadable shrinking. This is
    layout evidence, not comprehension evidence; and
17. the runtime handoff has exactly eight compact immutable provenance lines,
    five required reader sections with a 335-word combined target and exact
    section ceilings, non-clickable exact-filename pointers, and no Markdown
    detail link or copied-detail table. The handoff triple is the only Stage A
    evidence in Stage B Phase 1; the route and blank Section 1 workbook remain
    allowed, and revised detail first becomes available in verified Phase 2.
    The constructed linked miniature remains outside every participant and
    scored release.

Static checks also reject the legacy revised-record identity, future freeze
timestamps and self-hash fields in governed templates, and the old
checksum-reference fields that would require an artifact to predict its own
post-hash evidence. Per-file semantic clauses now enforce manifest exclusion,
ordered completion and verification, release-manifest triple binding, and
immutable correction identity. Fifty-nine negative mutations prove the validator
rejects manifest self-inclusion, same-path correction, missing revised Stage A
release binding, omitted complete verification output, missing attempt
identity, invalid record chronology, undeclared orchestration permission,
missing execution events, missing actor fields, and an omitted record-template
output field. They also reject live-update omission, rename, unbound release
membership, route omission, canonical wording drift, and weakening the
optional-contract branch. Closure mutations additionally reject entry-branch
omission or mixing, synthetic human-consent/result claims, missing context,
start, material-feedback, end, scoring, debrief, Section 6, or results
boundaries, an omitted or unverified debrief gate, omitted results, premature
log close, a predicted future log hash, omitted external closeout, and a
favorable one-page claim without passed proof. Six successor mutations also
reject an absent helper, helper selection after `RUN_STARTED`, overbroad helper
authority, ad hoc message delivery, future/dummy config hashes, and config
creation after its phase gate. Structured mutations refresh surrounding checksums
so rejection depends on the invariant rather than merely a stale hash.
Five v1.2.7 successor mutations additionally reject omission of exact
phase-input manifest identity/path/hash binding, failure to reverify that
manifest on every invocation, an outside-root manifest, weakened exact
membership equality, and weakened exact member-hash equality. The helper
subprocess suite separately rejects absent, drifted, outside-root, malformed,
duplicate, and config-mismatched manifests while retaining the two-phase
positive control.
Eight v1.2.8 successor mutations additionally reject an omitted provenance
marker, a wide runtime table, an omitted required reader field, a runtime
clickable detail link, a weakened 335-word target, exclusion of provenance
from page layout, premature Phase 1 detail access, and removal of the
miniature's outside-route working link.
They also reject any scored workbook source that requires the future Stage A
or Stage B end event inside governed bytes; those end facts belong only to the
facilitator log and later run results.

## Commands used

- `python3 scripts/validate_repository.py`
- `python3 scripts/test_temporal_protocol_validator.py`
- `python3 scripts/test_synthetic_exact_file_access.py`
- `python3 -m py_compile scripts/validate_repository.py scripts/test_temporal_protocol_validator.py scripts/test_synthetic_exact_file_access.py testing/ai-ready-data-reader-value-v1/facilitator-only/07-synthetic-exact-file-access.py`
- `sha256sum -c SHA256SUMS` from the packet directory
- targeted `rg` searches for the legacy identity, stale self-reference fields,
  version drift, incomplete task markers, and the complete/manifest/verify/
  detached-record ordering language
- `git diff --check`

The repository validator contains packet-specific temporal protocol checks,
the executable negative fixtures check representative adversarial drift, and
the helper subprocess suite checks partial write-all/fsync behavior, exact byte
emission, distinct two-phase logs, phase-manifest binding/equality, and bounded
refusals.
The packet's checked-in `SHA256SUMS` includes this note and every other prepared
source-packet file, excluding the manifest itself.

## Boundary

This PASS means the source instructions and literal identities are internally
consistent under static inspection. Six completed scored freeze chains remain
distinct from full participant/run-route completion. This PASS does not show that a facilitator
executed the order, that timestamps are trustworthy, that a participant
understood the materials, or that any data, AI system, control, readiness
decision, safety claim, or business result is valid. Those require an
authorized run and retained run-specific evidence.
