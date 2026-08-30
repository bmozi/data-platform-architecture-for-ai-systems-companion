# Synthetic Context Record Template

**Packet:** DATA-RV-PILOT-001 version 1.2.7
**Status:** Blank synthetic-branch template; not consent and not a result

Use this template only when the run selects the synthetic branch. A synthetic
rehearsal has no human participant and cannot obtain or claim human consent.
Do not complete the human consent form with fictional names, initials,
affirmations, or signatures.

Complete the immutable run instance as exactly
`DATA-SYNTHETIC-CONTEXT-v1.md`. Finish every field before creating
`DATA-SYNTHETIC-CONTEXT-SHA256SUMS-v1.txt` over that record alone. Verify the
manifest and record the verification in the external execution/access log
before any scored file opens. The context record may name its later manifest,
but it must not predict the manifest hash, verification time, final log hash,
or closeout time.

## Required synthetic context

- Packet ID/version: `DATA-RV-PILOT-001` / `1.2.7`
- Attempt ID:
- Required literal: `SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA`
- Scenario boundary: fictional Harbor Grove scenario only
- Human consent state: not applicable; no human participant
- Human comprehension, usability, and practitioner-result state: `UNRUN`
- Data-readiness and real-world result state: `UNRUN`
- Synthetic Stage A actor code:
- Synthetic Stage B actor code:
- Facilitator code:
- Orchestration-aided: yes / no
- Exact orchestration manifest filename and SHA-256:
- Evidence root:
- Retention boundary:
- Access boundary:
- Exact helper source path and SHA-256:
  `facilitator-only/07-synthetic-exact-file-access.py` /
- Immutable run helper filename and SHA-256:
  `DATA-SYNTHETIC-EXACT-FILE-ACCESS-v1.py` /
- Predeclared phase access directories, helper-copy hashes, and actor assignments:
- Exact per-phase config filename/schema:
  `DATA-SYNTHETIC-EXACT-FILE-ACCESS-CONFIG-v1.json` / schema 2
- Required per-phase verified input-manifest filename/absolute path/SHA-256
  binding and exact config membership/hash equality:
- Exact per-phase helper/config binding-manifest filename:
  `DATA-SYNTHETIC-EXACT-FILE-ACCESS-SHA256SUMS-v1.txt`
- Exact distinct per-phase external access-log filename:
  `DATA-SYNTHETIC-EXACT-FILE-ACCESS-LOG-v1.jsonl`
- Exact actor-instruction helper invocation and prohibition on every other
  command, direct read, or undeclared message:
- Helper/plan/orchestration selected and verified before `RUN_STARTED`, with
  event IDs/timestamps/timezones:
- Helper boundary state: exact-file allowlist/order/hash/refusal logging enabled
- Technical platform restriction/security state: `NOT ESTABLISHED` unless
  separately demonstrated with retained platform evidence
- Ad hoc facilitator message delivery: prohibited
- Run start timestamp:
- Run start timezone:
- Pre-scored execution-log checkpoint event ID and entry SHA-256:
- Context-record completion timestamp/timezone:
- Context-record pre-hash state: `CONTEXT COMPLETE`
- Later manifest exact filename:
  `DATA-SYNTHETIC-CONTEXT-SHA256SUMS-v1.txt`

Every later per-phase config must bind the exact verified phase-input manifest
flat filename, absolute path inside sealed input, and observed SHA-256. On
every invocation, the helper must rehash and parse that manifest and require
exact config/manifest membership and member-hash equality before reading a
target. An absent, drifted, wrong, outside-root, malformed, duplicate,
path-bearing, self-listing, or mismatched manifest stops the run.

## Synthetic non-claim

This context authorizes only one declared synthetic defect-finding attempt. It
does not establish human consent, comprehension, usability, practitioner
benefit, data readiness, privacy or safety effectiveness, production fitness,
cost, ROI, or business value. A synthetic behavior or layout result, if later
retained, must remain separately labeled and limited to its exact attempt.

Any blank required field, branch mixing, fictional human affirmation, human
result claim, absent or after-start helper, overbroad helper authority, or ad
hoc message delivery stops the run before scored input opens. Later per-phase
configs are allowed only for predeclared phase directories and must be created,
bound, and verified before the applicable phase gate.
