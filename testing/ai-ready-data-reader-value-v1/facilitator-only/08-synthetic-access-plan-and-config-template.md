# Synthetic Exact-File Access Plan and Config Template

**Packet:** DATA-RV-PILOT-001 version 1.2.6
**Status:** Blank facilitator-only pre-run template; not participant input and
not an execution result

Use this template only for the `SYNTHETIC` branch. Human participants use
ordinary file surfaces and receive no terminal, repository, Git, or helper
authority. A synthetic attempt may use only the exact helper described here.
This narrow exception is not general shell permission.

## Required pre-run identities

- Attempt ID:
- Synthetic actor code and Stage A/B assignment:
- Facilitator code:
- Packet source commit and source-packet `SHA256SUMS` hash:
- Exact byte-for-byte helper source:
  `facilitator-only/07-synthetic-exact-file-access.py`
- Immutable run helper filename:
  `DATA-SYNTHETIC-EXACT-FILE-ACCESS-v1.py`
- Immutable run helper SHA-256:
- Predeclared phase access directories and actor assignments:
- Reserved immutable config path in each phase directory:
  `DATA-SYNTHETIC-EXACT-FILE-ACCESS-CONFIG-v1.json`
- Reserved helper/config binding-manifest path in each phase directory:
  `DATA-SYNTHETIC-EXACT-FILE-ACCESS-SHA256SUMS-v1.txt`
- Reserved append-only helper access-log path in each phase directory and
  outside participant input:
  `DATA-SYNTHETIC-EXACT-FILE-ACCESS-LOG-v1.jsonl`
- Exact orchestration-manifest filename and SHA-256:
- Orchestration-manifest members for this mechanism: the byte-identical run
  helper copy in every predeclared phase access directory and this plan; later
  per-phase configs and binding manifests are bound by their phase gates
- Helper/plan/orchestration creation and verification event IDs, timestamps,
  timezones, commands, complete outputs, and exit codes, all before
  `RUN_STARTED`:
- Exact actor-instruction command surface:
- Technical platform restriction state: `NOT ESTABLISHED` unless separately
  demonstrated with retained platform evidence

The actor instruction permits only this literal shape, with the immutable
helper and reserved config/manifest absolute paths fixed before `RUN_STARTED`
and only the literal current-phase filename slot selectable by the actor:

```text
python3 DATA-SYNTHETIC-EXACT-FILE-ACCESS-v1.py \
  --config DATA-SYNTHETIC-EXACT-FILE-ACCESS-CONFIG-v1.json \
  --binding-manifest DATA-SYNTHETIC-EXACT-FILE-ACCESS-SHA256SUMS-v1.txt \
  --audit-log DATA-SYNTHETIC-EXACT-FILE-ACCESS-LOG-v1.jsonl \
  --filename LITERAL_CURRENT_PHASE_FILENAME
```

For a declared optional file at its exact position, the only alternative is:

```text
python3 DATA-SYNTHETIC-EXACT-FILE-ACCESS-v1.py \
  --config DATA-SYNTHETIC-EXACT-FILE-ACCESS-CONFIG-v1.json \
  --binding-manifest DATA-SYNTHETIC-EXACT-FILE-ACCESS-SHA256SUMS-v1.txt \
  --audit-log DATA-SYNTHETIC-EXACT-FILE-ACCESS-LOG-v1.jsonl \
  --skip-optional LITERAL_CURRENT_PHASE_FILENAME
```

The helper enforces its own exact-file boundary, but it does not prove that the
host platform removes other tools. The actor is procedurally forbidden to use
a general terminal, shell, repository browser, Git command, internet tool,
direct filesystem read, undeclared message, pasted file content, or helper
selected after `RUN_STARTED`. Any such use is a stop and deviation. Ad hoc
facilitator delivery is a deviation, not transport. Do not claim technical
sandbox enforcement unless separately demonstrated; otherwise record it as
`NOT ESTABLISHED`.

## Exact per-phase JSON config

Before `RUN_STARTED`, select and verify the helper, predeclare every phase
access directory, and bind each byte-identical run helper copy in the
orchestration manifest and synthetic context. Create a distinct immutable
config and helper/config binding manifest only when that phase's complete
input bytes exist, but always before the current phase gate opens. The run may
stage identical config filenames in separate predeclared phase directories.
Every config has exactly these keys:

```json
{
  "schema_version": 1,
  "packet_id": "DATA-RV-PILOT-001",
  "packet_version": "1.2.6",
  "attempt_id": "DATA-SYN-...",
  "actor_code": "DATA-A-SYN-...",
  "stage": "A",
  "phase_id": "stage-a-initial",
  "input_root": "/absolute/sealed/current-phase/input",
  "ordered_files": [
    {
      "filename": "00-packet-route.md",
      "sha256": "64-lowercase-hex",
      "optional": false
    }
  ],
  "access_log": "/absolute/facilitator/stage-a-initial/DATA-SYNTHETIC-EXACT-FILE-ACCESS-LOG-v1.jsonl",
  "binding_manifest_filename": "DATA-SYNTHETIC-EXACT-FILE-ACCESS-SHA256SUMS-v1.txt",
  "timezone": "America/Denver",
  "helper_selected_before_event": "RUN_STARTED",
  "config_created_before_event": "CURRENT_PHASE_GATE_OPENED",
  "immutable_after_creation": true
}
```

Before the applicable phase gate, record the config SHA-256, binding-manifest
SHA-256, phase sealed-input manifest identity/hash, access-log initial state,
creation and verification event IDs, timestamps/timezones, commands, complete
outputs, and exit codes. The config and binding manifest become immutable at
that point.

The `ordered_files` array is the current phase's complete filename allowlist
and exact read order. It contains hashes from that phase's verified sealed
input manifest. The optional data-product contract has `"optional": true` at
its route position; every other file is required. The config grants no path
slot, glob, directory listing, arbitrary command, message, or later-added
member. Future/dummy hashes are forbidden; every hash must be observed from
the already verified current phase input.

Each phase uses a distinct predeclared external directory and a distinct
same-named helper access log. A shared cross-phase helper log is forbidden
because its immutable config identity changes at the phase boundary. The run
results sum and reconcile all per-phase helper-log rows with the corresponding
external execution/access-log events.

The binding manifest contains exactly the byte-for-byte run helper and this
phase's config. The orchestration manifest separately binds every pre-run
helper copy and the plan. The completed synthetic context names and hashes the
pre-run helper copies, plan, predeclared phase directories, and config schema.
Each later phase gate binds its config and helper/config manifest. No helper,
helper authority, invocation shape, phase directory, or message transport may
be added or changed after `RUN_STARTED`; a config may be created later only
for an already declared phase and before that phase's gate.

## Required access/refusal evidence

The helper appends and fsyncs one JSONL row for every granted read, optional skip, or
refusal. The external execution/access log records the corresponding
`FILE_OPENED_OR_ACCESS_ATTEMPT_RECORDED` event and binds its helper access-log
event ID. A refusal never advances read order. Hash mismatch, wrong filename,
wrong order, wrong phase, exhausted allowlist, required-file skip, malformed
config, changed helper/config, or undeclared access is a stop or explicit
deviation. Invoke the helper serially; concurrent invocations are outside the
declared local durability model and are a stop.

Before each phase gate opens, the facilitator verifies the phase's sealed
input manifest, helper/config binding manifest, immutable config, expected next
filename, and unchanged helper identity. Phase advancement changes which
already declared config the exact actor instruction references; it does not
mutate a config or grant new authority.

## Non-claim

This mechanism can make the helper's exact-file boundary and file chronology
auditable. It does not prove that the host platform technically removed other
tools or that its sandbox is secure. Technical platform restriction/security
remains `NOT ESTABLISHED` unless separately demonstrated. It also does not prove that
a human used the materials or that any data, control, system, safety outcome,
or business result is valid.
