#!/usr/bin/env python3
"""Validate the companion repository's reader routes and local links."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "companion.json"
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
COMMIT_PATTERN = re.compile(r"^[0-9a-f]{7,40}$")
CHECKSUM_PATTERN = re.compile(r"^([0-9a-f]{64})  (.+)$")


TEMPORAL_PROTOCOL_FILES = [
    "README.md",
    "participant/00-packet-route.md",
    "participant/03-practitioner-workbook.md",
    "participant/04-decision-owner-workbook.md",
    "participant/05-one-screen-handoff.md",
    "participant/06-revised-artifact-freeze-record.md",
    "facilitator-only/01-facilitator-guide.md",
    "facilitator-only/02-observation-and-scoring-rubric.md",
    "facilitator-only/03-results-and-deviation-log.md",
    "facilitator-only/04-temporal-freeze-protocol-and-record-templates.md",
    "facilitator-only/05-execution-and-access-log.md",
]


def normalized(text: str) -> str:
    """Collapse Markdown layout whitespace for exact semantic-clause checks."""

    return re.sub(r"\s+", " ", text).strip()


def require_clauses(
    errors: list[str],
    contents: dict[str, str],
    relative: str,
    clauses: list[str],
) -> None:
    """Require explicit protocol clauses in one named source file."""

    content = normalized(contents.get(relative, "")).casefold()
    for clause in clauses:
        if normalized(clause).casefold() not in content:
            errors.append(
                f"temporal protocol: {relative} lacks required semantic "
                f"invariant: {normalized(clause)}"
            )


def require_order(
    errors: list[str],
    contents: dict[str, str],
    relative: str,
    anchors: list[str],
    scope: str,
) -> None:
    """Require protocol anchors to appear once in an executable order."""

    content = normalized(contents.get(relative, "")).casefold()
    positions = [content.find(normalized(anchor).casefold()) for anchor in anchors]
    if (
        any(position < 0 for position in positions)
        or positions != sorted(positions)
        or len(set(positions)) != len(positions)
    ):
        errors.append(
            f"temporal protocol: {relative} lacks ordered {scope} sequence: "
            + " -> ".join(normalized(anchor) for anchor in anchors)
        )


def require_count(
    errors: list[str],
    contents: dict[str, str],
    relative: str,
    clause: str,
    expected: int,
) -> None:
    """Require a repeated invariant once for each governed scope."""

    content = normalized(contents.get(relative, "")).casefold()
    actual = content.count(normalized(clause).casefold())
    if actual != expected:
        errors.append(
            f"temporal protocol: {relative} requires {expected} occurrence(s) "
            f"of semantic invariant but found {actual}: {normalized(clause)}"
        )


def temporal_protocol_content_errors(contents: dict[str, str]) -> list[str]:
    """Return static semantic errors for packet 1.2.3 source instructions."""

    errors: list[str] = []
    combined = "\n".join(contents.values())
    normalized_combined = normalized(combined).casefold()
    legacy = "DATA-A-REVISED-FREEZE-RECORD-v1.md"
    if legacy in combined:
        errors.append(f"temporal protocol: legacy record identity remains: {legacy}")

    exact_identities = [
        "DATA-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt",
        "DATA-A-INITIAL-FREEZE-VERIFICATION-v1.md",
        "DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt",
        "DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt",
        "DATA-A-REVISED-FREEZE-VERIFICATION-v1.md",
        "DATA-A-HANDOFF-SHA256SUMS-v1.txt",
        "DATA-A-HANDOFF-FREEZE-VERIFICATION-v1.md",
        "DATA-B-SECTION-1-SHA256SUMS-v1.txt",
        "DATA-B-SECTION-1-FREEZE-VERIFICATION-v1.md",
        "DATA-B-SECTION-2-SHA256SUMS-v1.txt",
        "DATA-B-SECTION-2-FREEZE-VERIFICATION-v1.md",
        "DATA-B-SECTIONS-3-5-SHA256SUMS-v1.txt",
        "DATA-B-SECTIONS-3-5-FREEZE-VERIFICATION-v1.md",
    ]
    for identity in exact_identities:
        if identity not in combined:
            errors.append(f"temporal protocol: missing exact identity: {identity}")

    required_by_file = {
        "participant/00-packet-route.md": exact_identities,
        "facilitator-only/01-facilitator-guide.md": exact_identities,
        "facilitator-only/03-results-and-deviation-log.md": exact_identities,
        "README.md": exact_identities,
        "participant/04-decision-owner-workbook.md": exact_identities[7:],
        "participant/05-one-screen-handoff.md": exact_identities[3:7],
    }
    for relative, identities in required_by_file.items():
        content = contents.get(relative, "")
        for identity in identities:
            if identity not in content:
                errors.append(
                    f"temporal protocol: {relative} lacks exact identity: {identity}"
                )

    for relative, content in contents.items():
        matches = re.findall(
            r"\*\*Packet:\*\* DATA-RV-PILOT-001 version ([^\s]+)", content
        )
        if relative == "README.md":
            if "**Version:** 1.2.3" not in content:
                errors.append("temporal protocol: README.md lacks packet version 1.2.3")
        elif matches != ["1.2.3"]:
            errors.append(
                f"temporal protocol: packet version identity invalid in {relative}: "
                f"{matches or 'missing'}"
            )

    semantic_clauses = {
        "README.md": [
            "The governing manifest `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` hashes exactly the included revised detail files and does not hash itself or the later detached record.",
            "Stage B Phase 2 specifically binds every included revised Stage A artifact, its governing manifest, and its detached record, in addition to the frozen Section 1 triple.",
            "new immutable filename and a new artifact ID/version",
        ],
        "participant/00-packet-route.md": [
            "It hashes exactly the included revised artifacts, never itself or the later verification record.",
            "At every phase boundary, the next sealed phase-input manifest must hash the completed artifact, its governing manifest, and its later detached verification record.",
            "Stage B Phase 2 must bind both the frozen Section 1 triple and every included revised Stage A artifact plus its governing manifest and detached record.",
            "`DATA-B-SECTION-1-SHA256SUMS-v1.txt` over the completed export only and create that detached record.",
            "`DATA-B-SECTION-2-SHA256SUMS-v1.txt` over only the completed export and create that detached record before opening either decision aid.",
            "`DATA-B-SECTIONS-3-5-SHA256SUMS-v1.txt` over only that completed export; then create the detached record.",
            "Collect all material feedback in the external results and deviation log",
            "new immutable filename and a new artifact ID/version",
        ],
        "participant/03-practitioner-workbook.md": [
            "without listing or hashing the manifest itself or the later record",
            "new immutable filename and a new artifact ID/version",
        ],
        "participant/04-decision-owner-workbook.md": [
            "The closing evidence manifest later hashes the completed export, governing manifest, and detached record.",
            "new immutable filename and a new artifact ID/version",
        ],
        "participant/05-one-screen-handoff.md": [
            "The manifest never hashes itself or the later record.",
            "Stage B's sealed Phase 1 input manifest hashes the handoff, its governing manifest, and the detached record.",
        ],
        "participant/06-revised-artifact-freeze-record.md": [
            "It never predicts a future event and is never listed in the governing manifest whose verification it records.",
            "the facilitator creates the next sealed phase-input manifest—or the closing evidence manifest for the final scope—over every governed artifact, its governing manifest, and this detached record.",
            "new immutable filename and a new artifact ID/version for every corrected artifact",
        ],
        "facilitator-only/01-facilitator-guide.md": [
            "The manifest never lists or hashes itself or the later record.",
            "The next sealed phase-input manifest hashes each governed artifact, its governing manifest, and its detached verification record.",
            "Before Phase 2 opens, create and verify its sealed input manifest over the frozen Section 1 artifact, governing manifest, and detached record; every included revised Stage A artifact; the revised Stage A governing manifest; the revised Stage A detached record; and the scenario.",
            "new immutable filename and a new artifact ID/version",
        ],
        "facilitator-only/02-observation-and-scoring-rubric.md": [
            "no governing manifest hashes itself or its later record",
            "the next phase or closing manifest hashes the artifact, governing manifest, and record",
            "new immutable filename and new artifact ID/version for every corrected artifact",
        ],
        "facilitator-only/03-results-and-deviation-log.md": [
            "Every governing manifest excludes itself and its later detached record",
            "Every next phase/evidence manifest hashes the artifact(s), governing manifest, and detached record under literal filenames",
            "| Stage A revised set | required revised files; optional only if used | `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` / | | `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md` / | Stage B Phase 2 input / |",
            "new immutable filename and a new artifact ID/version",
        ],
    }

    replay_clauses = {
        "README.md": [
            "execution history auditable",
            "exact manifest-verification command/output/exit/time/timezone",
            "`ORCHESTRATION.md`",
            "execution and access log",
            "`DATA-A-INITIAL-FREEZE-VERIFICATION-v1.md`",
        ],
        "participant/00-packet-route.md": [
            "For every detached verification record named below",
            "exact verification command",
            "complete observed output",
            "later record-completion timestamp and timezone",
            "`ORCHESTRATION.md`",
            "`DATA-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt`",
            "`DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt`",
        ],
        "participant/06-revised-artifact-freeze-record.md": [
            "- Attempt ID:",
            "- Freeze scope and phase:",
            "- Artifact-producing actor code:",
            "- Facilitator name/code:",
            "- Exact manifest verification command:",
            "- Complete observed command output:",
            "- Observed command exit code:",
            "- Observed manifest verification timestamp:",
            "- Observed manifest verification timezone:",
            "- Record-completing actor name/code:",
            "- Record completion timestamp, explicitly later than manifest verification:",
            "- Record completion timezone:",
        ],
        "facilitator-only/01-facilitator-guide.md": [
            "execution and access log",
            "every manifest gate, file open or attempted access, artifact completion",
            "exact verification command, complete observed output, exit code",
            "explicit later record-completion timestamp and timezone",
            "undeclared `ORCHESTRATION.md`",
            "`DATA-A-INITIAL-FREEZE-VERIFICATION-v1.md`",
        ],
        "facilitator-only/02-observation-and-scoring-rubric.md": [
            "Detached-record replay identity",
            "Execution/access continuity",
            "participant input contains no undeclared orchestration or facilitator file",
        ],
        "facilitator-only/03-results-and-deviation-log.md": [
            "Facilitator execution/access log exact filename and SHA-256",
            "Declared participant-input inventory matches item by item",
            "Detached-record required-field audit",
            "Complete observed output",
            "Later record-completion timestamp/timezone",
            "| Stage A initial | required `DATA-A-INITIAL-WORKBOOK-v1.md`",
        ],
        "facilitator-only/04-temporal-freeze-protocol-and-record-templates.md": [
            "Every detached record requires attempt, phase, actor, facilitator",
            "Exact manifest-verification command",
            "Complete observed command output",
            "Observed command exit code",
            "Record completion timestamp and timezone, explicitly later than verification",
            "`ORCHESTRATION.md`",
        ],
        "facilitator-only/05-execution-and-access-log.md": [
            "Keep this log outside every sealed participant input",
            "SEALED_INPUT_MANIFEST_CREATED",
            "GOVERNING_MANIFEST_VERIFIED",
            "DETACHED_RECORD_COMPLETED",
            "NEXT_PHASE_GATE_OPENED",
            "Complete observed output",
            "Continuity binding",
        ],
    }
    for relative, clauses in semantic_clauses.items():
        require_clauses(errors, contents, relative, clauses)
    for relative, clauses in replay_clauses.items():
        require_clauses(errors, contents, relative, clauses)

    require_order(
        errors,
        contents,
        "facilitator-only/01-facilitator-guide.md",
        [
            "Finalize every governed artifact",
            "Create the governing manifest",
            "Verify that manifest",
            "Only afterward create the detached record",
            "The next sealed phase-input manifest hashes each governed artifact",
        ],
        "complete -> manifest -> verify -> detached record -> release manifest",
    )
    require_order(
        errors,
        contents,
        "participant/00-packet-route.md",
        [
            "After those bytes are complete, create",
            "Verify the manifest and capture that observed timestamp and timezone",
            "Only then complete",
            "The verified manifest plus detached record establish",
            "The next sealed phase input manifest hashes each supplied governed artifact",
        ],
        "revised Stage A freeze and release",
    )
    require_order(
        errors,
        contents,
        "participant/00-packet-route.md",
        [
            "Give it an ID/version, completion timestamp/timezone, pre-hash state `SECTION 1 COMPLETE`",
            "Then create and verify `DATA-B-SECTION-1-SHA256SUMS-v1.txt` over the completed export only",
            "and create that detached record",
        ],
        "Stage B Section 1 complete -> manifest verification -> detached record",
    )
    require_order(
        errors,
        contents,
        "participant/00-packet-route.md",
        [
            "Complete Section 2 and export it as `DATA-B-SECTION-2-DETAIL-v1.md` with ID/version, completion timestamp/timezone, pre-hash state `SECTION 2 COMPLETE`",
            "Then create and verify `DATA-B-SECTION-2-SHA256SUMS-v1.txt` over only the completed export",
            "and create that detached record before opening either decision aid",
        ],
        "Stage B Section 2 complete -> manifest verification -> detached record",
    )
    require_order(
        errors,
        contents,
        "participant/00-packet-route.md",
        [
            "Complete Sections 3-5 and export them as `DATA-B-SECTIONS-3-5-DECISION-v1.md` with ID/version, completion timestamp/timezone, pre-hash state `SECTIONS 3-5 COMPLETE`",
            "Create and verify `DATA-B-SECTIONS-3-5-SHA256SUMS-v1.txt` over only that completed export",
            "then create the detached record",
        ],
        "Stage B Sections 3-5 complete -> manifest verification -> detached record",
    )
    require_count(
        errors,
        contents,
        "participant/04-decision-owner-workbook.md",
        "Finalize the export before hashing. Do not put its own hash, a future verification timestamp, or `FROZEN` inside it.",
        3,
    )
    require_count(
        errors,
        contents,
        "participant/04-decision-owner-workbook.md",
        "created only after",
        3,
    )

    stale_self_reference_fields = [
        "Section 1 freeze timestamp and timezone:",
        "Section 1 SHA-256 or manifest reference:",
        "Section 2 freeze timestamp and timezone:",
        "Section 2 SHA-256 or manifest reference:",
        "Sections 3-5 freeze timestamp and timezone:",
        "Sections 3-5 SHA-256 or manifest reference:",
        "Separate handoff freeze timestamp/timezone",
    ]
    governed_templates = "\n".join(
        contents.get(relative, "")
        for relative in [
            "participant/03-practitioner-workbook.md",
            "participant/04-decision-owner-workbook.md",
            "participant/05-one-screen-handoff.md",
        ]
    )
    for field in stale_self_reference_fields:
        if field in governed_templates:
            errors.append(f"temporal protocol: stale self-reference field: {field}")

    practitioner = contents.get("participant/03-practitioner-workbook.md", "")
    future_handoff_fields = [
        "One-screen handoff completion timestamp/timezone",
        "Post-hash handoff verification provenance",
        "## 8. Material feedback",
    ]
    for field in future_handoff_fields:
        if field in practitioner:
            errors.append(
                "temporal protocol: revised workbook contains later handoff or "
                f"feedback field: {field}"
            )

    forbidden_correction_language = [
        "new ids/versions or filenames",
        "new id/version or filename",
        "new artifact id/version or a new immutable filename",
        "new immutable filename or a new artifact id/version",
    ]
    for phrase in forbidden_correction_language:
        if phrase in normalized_combined:
            errors.append(
                "temporal protocol: correction permits same-path or incomplete "
                f"replacement identity: {phrase}"
            )

    if "complete the material-feedback section of the practitioner workbook" in normalized_combined:
        errors.append(
            "temporal protocol: route references removed practitioner-workbook "
            "material-feedback section"
        )

    return errors


def validate_temporal_freeze_protocol(
    errors: list[str], content_overrides: dict[str, str] | None = None
) -> int:
    """Check packet 1.2.3's static temporal-order invariants."""

    packet = ROOT / "testing/ai-ready-data-reader-value-v1"
    contents: dict[str, str] = {}
    for relative in TEMPORAL_PROTOCOL_FILES:
        path = packet / relative
        if not path.is_file():
            errors.append(f"temporal protocol: missing {path.relative_to(ROOT)}")
            continue
        contents[relative] = path.read_text(encoding="utf-8")
    for path in packet.rglob("*.md"):
        relative = path.relative_to(packet).as_posix()
        contents.setdefault(relative, path.read_text(encoding="utf-8"))
    if content_overrides:
        contents.update(content_overrides)

    errors.extend(temporal_protocol_content_errors(contents))
    return len(TEMPORAL_PROTOCOL_FILES)


def validate_temporal_protocol_json(errors: list[str]) -> int:
    """Validate the normative machine-readable replay protocol."""

    packet = ROOT / "testing/ai-ready-data-reader-value-v1"
    protocol_path = packet / "temporal-protocol.json"
    if not protocol_path.is_file():
        errors.append("temporal protocol JSON is missing")
        return 0
    try:
        protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"temporal protocol JSON is invalid: {exc}")
        return 0

    expected_order = [
        "completed_artifacts",
        "artifact_only_manifest",
        "successful_manifest_verification",
        "detached_verification_record",
        "next_release_manifest",
    ]
    expected_verification_fields = [
        "exact_command",
        "complete_output",
        "exit_code",
        "timestamp",
        "timezone",
    ]
    expected_record_fields = [
        "attempt_id",
        "phase",
        "artifact_actor",
        "facilitator",
        "manifest_verifier",
        "exact_verification_command",
        "complete_observed_output",
        "exit_code",
        "verification_timestamp",
        "verification_timezone",
        "record_completing_actor",
        "record_completion_timestamp",
        "record_completion_timezone",
    ]
    expected_events = [
        "SEALED_INPUT_MANIFEST_CREATED",
        "SEALED_INPUT_MANIFEST_VERIFIED",
        "PHASE_GATE_OPENED",
        "FILE_OPENED_OR_ACCESS_ATTEMPT_RECORDED",
        "ARTIFACT_COMPLETED",
        "GOVERNING_MANIFEST_CREATED",
        "GOVERNING_MANIFEST_VERIFIED",
        "DETACHED_RECORD_COMPLETED",
        "NEXT_RELEASE_MANIFEST_CREATED",
        "NEXT_RELEASE_MANIFEST_VERIFIED",
        "NEXT_PHASE_GATE_OPENED",
    ]
    expected_log_fields = [
        "event_id",
        "prior_event_id",
        "phase",
        "event_type",
        "filename_or_surface",
        "actor",
        "facilitator",
        "timestamp",
        "timezone",
        "verification_command",
        "complete_observed_output",
        "exit_code",
        "continuity_binding",
        "outcome_or_deviation",
    ]
    expected_release_ids = [
        "stage_a_initial",
        "stage_a_revised",
        "stage_a_handoff",
        "stage_b_section_1",
        "stage_b_section_2",
        "stage_b_sections_3_5",
    ]
    expected_states = {
        "stage_a_initial": "INITIAL COMPLETE",
        "stage_a_revised": "REVISED COMPLETE",
        "stage_a_handoff": "HANDOFF COMPLETE",
        "stage_b_section_1": "SECTION 1 COMPLETE",
        "stage_b_section_2": "SECTION 2 COMPLETE",
        "stage_b_sections_3_5": "SECTIONS 3-5 COMPLETE",
    }

    if protocol.get("schema_version") != 2:
        errors.append("temporal protocol JSON: schema_version must be 2")
    if protocol.get("packet_id") != "DATA-RV-PILOT-001":
        errors.append("temporal protocol JSON: packet_id mismatch")
    if protocol.get("packet_version") != "1.2.3":
        errors.append("temporal protocol JSON: packet_version mismatch")
    if protocol.get("causal_order") != expected_order:
        errors.append("temporal protocol JSON: causal order is invalid")
    if protocol.get("governing_manifest_members") != ["governed_artifacts"]:
        errors.append("temporal protocol JSON: manifest membership is invalid")
    if protocol.get("governing_manifest_excludes") != [
        "governing_manifest",
        "detached_verification_record",
    ]:
        errors.append("temporal protocol JSON: manifest exclusions are invalid")

    verification = protocol.get("verification", {})
    if verification.get("must_succeed") is not True:
        errors.append("temporal protocol JSON: manifest verification must succeed")
    if verification.get("observed_timestamp_timezone_required") is not True:
        errors.append("temporal protocol JSON: verification timestamp/timezone is required")
    if verification.get("required_observation_fields") != expected_verification_fields:
        errors.append(
            "temporal protocol JSON: verification must capture command, complete output, "
            "exit code, timestamp, and timezone"
        )

    record = protocol.get("detached_record", {})
    if record.get("created_after") != "successful_manifest_verification":
        errors.append("temporal protocol JSON: detached record is not later")
    if record.get("excluded_from_described_manifest") is not True:
        errors.append("temporal protocol JSON: detached record must be excluded")
    if record.get("claims_self_hash") is not False:
        errors.append("temporal protocol JSON: detached record claims self-hash")
    if record.get("required_fields") != expected_record_fields:
        errors.append(
            "temporal protocol JSON: detached record fields omit replay identity or evidence"
        )
    if record.get("record_completion_must_follow_verification") is not True:
        errors.append("temporal protocol JSON: record completion must follow verification")

    input_policy = protocol.get("participant_input_policy", {})
    if input_policy.get("declared_route_files_only") is not True:
        errors.append("temporal protocol JSON: participant input is not declared-only")
    if input_policy.get("undeclared_orchestration_forbidden") is not True:
        errors.append("temporal protocol JSON: undeclared orchestration is not forbidden")
    if input_policy.get("forbidden_examples") != [
        "ORCHESTRATION.md",
        "run note",
        "hidden prompt",
        "facilitator file",
    ]:
        errors.append("temporal protocol JSON: forbidden participant-input examples incomplete")

    execution = protocol.get("execution_access_log", {})
    if execution.get("path") != "facilitator-only/05-execution-and-access-log.md":
        errors.append("temporal protocol JSON: execution log path mismatch")
    if execution.get("facilitator_only") is not True:
        errors.append("temporal protocol JSON: execution log must be facilitator-only")
    if execution.get("excluded_from_participant_input") is not True:
        errors.append("temporal protocol JSON: execution log must be excluded from input")
    if execution.get("continuity_binding_required") is not True:
        errors.append("temporal protocol JSON: execution continuity binding required")
    if execution.get("required_event_sequence") != expected_events:
        errors.append("temporal protocol JSON: execution event sequence invalid")
    if execution.get("required_row_fields") != expected_log_fields:
        errors.append("temporal protocol JSON: execution log row fields incomplete")

    if protocol.get("next_release_bindings") != [
        "governed_artifacts",
        "governing_manifest",
        "detached_verification_record",
    ]:
        errors.append("temporal protocol JSON: next-release triple is invalid")

    correction = protocol.get("correction_policy", {})
    if correction.get("preserve_prior_release") is not True:
        errors.append("temporal protocol JSON: correction must preserve prior release")
    if correction.get("allow_overwrite") is not False:
        errors.append("temporal protocol JSON: correction cannot permit overwrite")
    if correction.get("allow_same_filename") is not False:
        errors.append("temporal protocol JSON: correction must require new filename")
    if correction.get("required_new_identity") != [
        "filename",
        "artifact_id",
        "version",
        "sha256",
        "governing_manifest",
        "detached_verification_record",
    ]:
        errors.append("temporal protocol JSON: correction identity is incomplete")

    releases = protocol.get("release_chains", [])
    release_ids = [item.get("id") for item in releases if isinstance(item, dict)]
    if release_ids != expected_release_ids:
        errors.append("temporal protocol JSON: release chain IDs/order invalid")
    for release in releases:
        if not isinstance(release, dict) or release.get("id") not in expected_states:
            continue
        release_id = release["id"]
        artifacts = release.get("artifacts", [])
        if not artifacts:
            errors.append(f"temporal protocol JSON: {release_id} has no artifacts")
        for artifact in artifacts:
            if artifact.get("state") != expected_states[release_id]:
                errors.append(f"temporal protocol JSON: {release_id} state mismatch")
            if not artifact.get("filename"):
                errors.append(f"temporal protocol JSON: {release_id} filename missing")
        for field in ["governing_manifest", "detached_record", "next_release_manifest"]:
            if not release.get(field):
                errors.append(f"temporal protocol JSON: {release_id} {field} missing")

    critical = protocol.get("critical_documents", [])
    expected_markdown = {
        path.relative_to(packet).as_posix() for path in packet.rglob("*.md")
    }
    found_markdown = {
        item.get("path") for item in critical if isinstance(item, dict)
    }
    if found_markdown != expected_markdown:
        errors.append("temporal protocol JSON: critical Markdown inventory mismatch")
    for item in critical:
        if not isinstance(item, dict) or not isinstance(item.get("path"), str):
            errors.append("temporal protocol JSON: invalid critical document entry")
            continue
        target = packet / item["path"]
        if not target.is_file():
            errors.append(f"temporal protocol JSON: missing critical document {item['path']}")
        elif item.get("sha256") != sha256(target):
            errors.append(f"temporal protocol JSON: critical hash mismatch {item['path']}")

    return 1


def markdown_links(path: Path):
    in_fence = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.lstrip()
        if stripped.startswith(chr(96) * 3) or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK_PATTERN.finditer(line):
            yield number, match.group(1).strip()


def local_target(source: Path, raw: str) -> Path | None:
    target = raw
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(" ", 1)[0]
    parsed = urlsplit(target)
    if parsed.scheme or target.startswith("//") or target.startswith("#"):
        return None
    decoded = unquote(parsed.path)
    if not decoded:
        return None
    if decoded.startswith("/"):
        raise ValueError("absolute local path")
    resolved = (source.parent / decoded).resolve()
    try:
        resolved.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError("link escapes repository") from exc
    return resolved


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    errors: list[str] = []
    if not MANIFEST.is_file():
        print("missing companion.json", file=sys.stderr)
        return 1

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"invalid companion.json: {exc}", file=sys.stderr)
        return 1

    if manifest.get("schema_version") != 1:
        errors.append("companion.json: schema_version must be 1")
    if not COMMIT_PATTERN.fullmatch(str(manifest.get("source_commit", ""))):
        errors.append("companion.json: source_commit must be a 7-40 character Git hash")

    required = manifest.get("required_files")
    if not isinstance(required, list) or not required:
        errors.append("companion.json: required_files must be a non-empty list")
        required = []
    for relative in required:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    checksum_manifests = manifest.get("checksum_manifests", [])
    if not isinstance(checksum_manifests, list):
        errors.append("companion.json: checksum_manifests must be a list")
        checksum_manifests = []
    checked_checksums = 0
    for relative in checksum_manifests:
        checksum_path = ROOT / relative
        if not checksum_path.is_file():
            errors.append(f"missing checksum manifest: {relative}")
            continue
        listed_targets: set[Path] = set()
        for number, line in enumerate(
            checksum_path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            match = CHECKSUM_PATTERN.fullmatch(line)
            if not match:
                errors.append(f"{relative}:{number}: invalid SHA256SUMS line")
                continue
            expected, raw_target = match.groups()
            target = (checksum_path.parent / raw_target).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{relative}:{number}: checksum target escapes repository")
                continue
            if not target.is_file():
                errors.append(f"{relative}:{number}: missing checksum target: {raw_target}")
                continue
            listed_targets.add(target)
            checked_checksums += 1
            if sha256(target) != expected:
                errors.append(f"{relative}:{number}: checksum mismatch: {raw_target}")
        packet_files = {
            path.resolve()
            for path in checksum_path.parent.rglob("*")
            if path.is_file()
            and path != checksum_path
            and "__pycache__" not in path.parts
        }
        for unlisted in sorted(packet_files - listed_targets):
            errors.append(
                f"{relative}: packet file missing from checksum manifest: "
                f"{unlisted.relative_to(checksum_path.parent)}"
            )

    gateways = manifest.get("gateway_assets")
    if not isinstance(gateways, list) or not gateways:
        errors.append("companion.json: gateway_assets must be a non-empty list")
        gateways = []
    for gateway in gateways:
        relative = gateway.get("path", "")
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing gateway asset: {relative}")
            continue
        content = path.read_text(encoding="utf-8").casefold()
        phrases = [gateway.get("first_pass", ""), *gateway.get("required_language", [])]
        for phrase in phrases:
            if not phrase or phrase.casefold() not in content:
                errors.append(f"{relative}: missing required gateway language: {phrase!r}")
        for example in gateway.get("examples", []):
            if not (ROOT / example).is_file():
                errors.append(f"{relative}: missing comprehensive example: {example}")

    markdown_files = sorted(
        path for path in ROOT.rglob("*.md") if ".git" not in path.parts
    )
    checked_links = 0
    for source in markdown_files:
        for line, raw in markdown_links(source):
            try:
                target = local_target(source, raw)
            except ValueError as exc:
                errors.append(f"{source.relative_to(ROOT)}:{line}: {exc}: {raw}")
                continue
            if target is None:
                continue
            checked_links += 1
            if not target.exists():
                errors.append(
                    f"{source.relative_to(ROOT)}:{line}: missing local link target: {raw}"
                )

    checked_protocol_files = validate_temporal_freeze_protocol(errors)
    checked_protocol_json = validate_temporal_protocol_json(errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print(f"companion validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1

    print(
        f"companion validation passed: {len(markdown_files)} Markdown files, "
        f"{checked_links} local links, {len(gateways)} gateway asset(s), "
        f"{checked_checksums} checksum(s), "
        f"{checked_protocol_files} temporal-protocol file(s), "
        f"{checked_protocol_json} temporal-protocol JSON file(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
