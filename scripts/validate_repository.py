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
INDEPENDENT_PACKET_SUBDIRECTORIES = {"promoted"}
PACKET_ID = "DATA-RV-PILOT-001"
PACKET_VERSION = "1.2.8"
TEMPORAL_SCHEMA_VERSION = 7
LIVE_UPDATE_FILENAME = "DATA-A-LIVE-UPDATE-v1.md"
LIVE_UPDATE_PATH = f"participant/{LIVE_UPDATE_FILENAME}"
REVISION_PHASE_ID = "stage_a_revision"
REVISION_PRIOR_RELEASE = "stage_a_initial"
REVISION_OPENS_RELEASE = "stage_a_revised"
REVISION_MANIFEST = "DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt"
OPTIONAL_INITIAL_CONTRACT = "DATA-A-INITIAL-DATA-PRODUCT-CONTRACT-v1.md"
LIVE_UPDATE_CANONICAL_SOURCE = "facilitator-only/01-facilitator-guide.md"
LIVE_UPDATE_START_MARKER = "<!-- DATA-A-LIVE-UPDATE-v1 CANONICAL START -->"
LIVE_UPDATE_END_MARKER = "<!-- DATA-A-LIVE-UPDATE-v1 CANONICAL END -->"
REVISION_CONDITIONAL_MEMBERS = [
    {
        "filename": OPTIONAL_INITIAL_CONTRACT,
        "required_when_prior_release_artifact_included": True,
        "forbidden_when_prior_release_artifact_not_included": True,
    }
]
SYNTHETIC_CONTEXT_TEMPLATE = "participant/07-synthetic-context-record.md"
SYNTHETIC_CONTEXT_FILENAME = "DATA-SYNTHETIC-CONTEXT-v1.md"
SYNTHETIC_CONTEXT_MANIFEST = "DATA-SYNTHETIC-CONTEXT-SHA256SUMS-v1.txt"
EXECUTION_LOG_FILENAME = "DATA-EXECUTION-ACCESS-LOG-v1.jsonl"
DEBRIEF_INPUT_FILENAME = "04-decision-owner-workbook.md"
DEBRIEF_MANIFEST = "DATA-B-PHASE-4-DEBRIEF-INPUT-SHA256SUMS-v1.txt"
DEBRIEF_OUTPUT_FILENAME = "DATA-B-SECTION-6-DEBRIEF-v1.md"
RUN_RESULTS_FILENAME = "DATA-RUN-RESULTS-v1.md"
CLOSEOUT_MANIFEST = "DATA-RUN-CLOSEOUT-SHA256SUMS-v1.txt"
CLOSEOUT_RECORD = "DATA-RUN-CLOSEOUT-v1.md"
LAYOUT_TEMPLATE = "facilitator-only/06-handoff-layout-proof-record.md"
LAYOUT_RECORD = "DATA-A-HANDOFF-LAYOUT-PROOF-v1.md"
LAYOUT_PDF = "DATA-A-ONE-SCREEN-HANDOFF-v1.pdf"
HANDOFF_TEMPLATE = "participant/05-one-screen-handoff.md"
HANDOFF_PROVENANCE_START = "<!-- IMMUTABLE PROVENANCE START -->"
HANDOFF_PROVENANCE_END = "<!-- IMMUTABLE PROVENANCE END -->"
HANDOFF_READER_TARGET = 335
HANDOFF_EXAMPLE = ROOT / "examples/one-screen-handoff-miniature-v1.md"
HANDOFF_READER_SECTIONS = [
    {
        "heading": "1. Decision and beneficiary",
        "maximum_words": 55,
        "required_fields": [
            "Current decision and bounded scope",
            "Who benefits and the exact use",
        ],
    },
    {
        "heading": "2. Allowed and withheld",
        "maximum_words": 55,
        "required_fields": [
            "What the assistant may search",
            "What data or use is withheld",
        ],
    },
    {
        "heading": "3. Evidence and uncertainty",
        "maximum_words": 85,
        "required_fields": [
            "Current evidence class, mapped to each material claim",
            "Known evidence",
            "Unknown or disputed evidence",
        ],
    },
    {
        "heading": "4. Ownership, risk, and action",
        "maximum_words": 85,
        "required_fields": [
            "Assigned owner, or UNASSIGNED; assigning or acting authority, or UNKNOWN",
            "Largest unacceptable outcome",
            "Immediate next action",
            "Review date or evidence-based trigger",
        ],
    },
    {
        "heading": "5. Proof, gates, and limits",
        "maximum_words": 55,
        "required_fields": [
            "How we prove the exact policy used",
            "How corrections reach the served copy",
            "Separate model, action-authority, and release gates still unresolved, plus what this exercise cannot establish",
        ],
    },
]
SYNTHETIC_HELPER_SOURCE = "facilitator-only/07-synthetic-exact-file-access.py"
SYNTHETIC_HELPER_SHA256 = (
    "a8a5f1cee2071a1606849b3dafdd509277039a7e2dd5d39ff1a2cd2e7c70e8dd"
)
SYNTHETIC_ACCESS_PLAN = (
    "facilitator-only/08-synthetic-access-plan-and-config-template.md"
)
SYNTHETIC_RUN_HELPER = "DATA-SYNTHETIC-EXACT-FILE-ACCESS-v1.py"
SYNTHETIC_ACCESS_CONFIG = "DATA-SYNTHETIC-EXACT-FILE-ACCESS-CONFIG-v1.json"
SYNTHETIC_ACCESS_BINDING_MANIFEST = (
    "DATA-SYNTHETIC-EXACT-FILE-ACCESS-SHA256SUMS-v1.txt"
)
SYNTHETIC_ACCESS_LOG = "DATA-SYNTHETIC-EXACT-FILE-ACCESS-LOG-v1.jsonl"
ROUTE_BOUNDARY_SEQUENCE = [
    "ENTRY_BRANCH_SELECTED",
    "RUN_STARTED",
    "STAGE_A_CONTEXT_GATE_OPENED",
    "STAGE_A_STARTED",
    "HANDOFF_LAYOUT_PROOF_COMPLETED",
    "STAGE_A_MATERIAL_FEEDBACK_COMPLETED",
    "STAGE_A_ENDED",
    "STAGE_B_CONTEXT_GATE_OPENED",
    "STAGE_B_STARTED",
    "STAGE_B_SCORING_ENDED",
    "DEBRIEF_INPUT_MANIFEST_CREATED",
    "DEBRIEF_INPUT_MANIFEST_VERIFIED",
    "STAGE_B_SECTION_6_DEBRIEF_OPENED",
    "STAGE_B_SECTION_6_DEBRIEF_COMPLETED",
    "STAGE_B_ENDED",
    "RUN_RESULTS_COMPLETED",
    "LOG_CLOSED",
]


TEMPORAL_PROTOCOL_FILES = [
    "README.md",
    "participant/00-packet-route.md",
    LIVE_UPDATE_PATH,
    SYNTHETIC_CONTEXT_TEMPLATE,
    "participant/03-practitioner-workbook.md",
    "participant/04-decision-owner-workbook.md",
    "participant/05-one-screen-handoff.md",
    "participant/06-revised-artifact-freeze-record.md",
    "facilitator-only/01-facilitator-guide.md",
    "facilitator-only/02-observation-and-scoring-rubric.md",
    "facilitator-only/03-results-and-deviation-log.md",
    "facilitator-only/04-temporal-freeze-protocol-and-record-templates.md",
    "facilitator-only/05-execution-and-access-log.md",
    LAYOUT_TEMPLATE,
    SYNTHETIC_ACCESS_PLAN,
]

GOVERNED_OR_SCORED_SOURCE_FILES = [
    "participant/03-practitioner-workbook.md",
    "participant/04-decision-owner-workbook.md",
    "participant/05-one-screen-handoff.md",
]


def belongs_to_independent_subpackage(path: Path, packet: Path) -> bool:
    """Return true when a path is governed by its own nested manifest."""

    relative = path.relative_to(packet)
    return bool(relative.parts) and relative.parts[0] in INDEPENDENT_PACKET_SUBDIRECTORIES


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
    """Return static semantic errors for packet 1.2.8 source instructions."""

    errors: list[str] = []
    combined = "\n".join(contents.values())
    normalized_combined = normalized(combined).casefold()
    legacy = "DATA-A-REVISED-FREEZE-RECORD-v1.md"
    if legacy in combined:
        errors.append(f"temporal protocol: legacy record identity remains: {legacy}")

    handoff_source = contents.get(HANDOFF_TEMPLATE, "")
    for marker in [HANDOFF_PROVENANCE_START, HANDOFF_PROVENANCE_END]:
        if handoff_source.count(marker) != 1:
            errors.append(
                "temporal protocol: handoff immutable provenance marker must "
                f"appear exactly once: {marker}"
            )
    if re.search(r"(?m)^\s*\|[^\n]*\|\s*$", handoff_source):
        errors.append(
            "temporal protocol: handoff template permits a wide Markdown table"
        )
    if re.search(r"\[[^\]]+\]\([^)]+\)", handoff_source):
        errors.append(
            "temporal protocol: runtime handoff template permits a clickable "
            "Markdown detail link before Stage B Phase 2"
        )
    provenance_match = re.search(
        re.escape(HANDOFF_PROVENANCE_START)
        + r"\n(?P<body>.*?)\n"
        + re.escape(HANDOFF_PROVENANCE_END),
        handoff_source,
        flags=re.DOTALL,
    )
    provenance_lines = (
        re.findall(r"(?m)^- ", provenance_match.group("body"))
        if provenance_match
        else []
    )
    if len(provenance_lines) != 8:
        errors.append(
            "temporal protocol: handoff immutable provenance block must contain "
            "exactly eight compact lines"
        )
    for section in HANDOFF_READER_SECTIONS:
        heading = section["heading"]
        if heading not in handoff_source:
            errors.append(
                f"temporal protocol: handoff template lacks reader section: {heading}"
            )
        for field in section["required_fields"]:
            if field not in normalized(handoff_source).replace("`", ""):
                errors.append(
                    "temporal protocol: handoff template lacks required reader "
                    f"field: {field}"
                )
        if f"{section['maximum_words']} words maximum" not in handoff_source:
            errors.append(
                "temporal protocol: handoff template lacks exact section word "
                f"ceiling: {heading} / {section['maximum_words']}"
            )
    if not HANDOFF_EXAMPLE.is_file():
        errors.append(
            "temporal protocol: constructed handoff miniature outside scored "
            "release is missing"
        )
    else:
        example_content = HANDOFF_EXAMPLE.read_text(encoding="utf-8")
        for clause in [
            "not a packet artifact, freeze, run, or result",
            "outside the scored packet",
            "must never be supplied during a participant route",
        ]:
            if clause.casefold() not in normalized(example_content).casefold():
                errors.append(
                    "temporal protocol: constructed handoff miniature lacks "
                    f"outside-route boundary: {clause}"
                )
        if not re.search(r"\[[^\]]+\]\([^)]+\)", example_content):
            errors.append(
                "temporal protocol: constructed handoff miniature lacks its "
                "outside-route working detail link"
            )

    exact_identities = [
        LIVE_UPDATE_FILENAME,
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

    closure_identities = [
        SYNTHETIC_CONTEXT_FILENAME,
        SYNTHETIC_CONTEXT_MANIFEST,
        EXECUTION_LOG_FILENAME,
        LAYOUT_RECORD,
        LAYOUT_PDF,
        DEBRIEF_MANIFEST,
        DEBRIEF_OUTPUT_FILENAME,
        RUN_RESULTS_FILENAME,
        CLOSEOUT_MANIFEST,
        CLOSEOUT_RECORD,
    ]
    for identity in closure_identities:
        if identity not in combined:
            errors.append(f"temporal protocol: missing closure identity: {identity}")

    access_identities = [
        SYNTHETIC_RUN_HELPER,
        SYNTHETIC_ACCESS_CONFIG,
        SYNTHETIC_ACCESS_BINDING_MANIFEST,
        SYNTHETIC_ACCESS_LOG,
    ]
    for identity in access_identities:
        if identity not in combined:
            errors.append(
                f"temporal protocol: missing synthetic access identity: {identity}"
            )

    for relative in GOVERNED_OR_SCORED_SOURCE_FILES:
        content = contents.get(relative, "")
        for future_event in ["STAGE_A_ENDED", "STAGE_B_ENDED"]:
            if future_event in content:
                errors.append(
                    f"temporal protocol: {relative} requires future stage-end fact "
                    f"inside governed/scored source: {future_event}"
                )

    required_by_file = {
        "participant/00-packet-route.md": exact_identities,
        "facilitator-only/01-facilitator-guide.md": exact_identities,
        "facilitator-only/03-results-and-deviation-log.md": exact_identities,
        "README.md": exact_identities,
        "participant/04-decision-owner-workbook.md": exact_identities[8:],
        "participant/05-one-screen-handoff.md": exact_identities[4:8],
    }
    for relative, identities in required_by_file.items():
        content = contents.get(relative, "")
        for identity in identities:
            if identity not in content:
                errors.append(
                    f"temporal protocol: {relative} lacks exact identity: {identity}"
                )

    for relative in [
        "README.md",
        "participant/00-packet-route.md",
        "facilitator-only/01-facilitator-guide.md",
        "facilitator-only/03-results-and-deviation-log.md",
        "facilitator-only/04-temporal-freeze-protocol-and-record-templates.md",
    ]:
        content = contents.get(relative, "")
        for identity in closure_identities:
            if identity not in content:
                errors.append(
                    f"temporal protocol: {relative} lacks closure identity: {identity}"
                )

    for relative in [
        "README.md",
        "participant/00-packet-route.md",
        SYNTHETIC_CONTEXT_TEMPLATE,
        "facilitator-only/01-facilitator-guide.md",
        "facilitator-only/02-observation-and-scoring-rubric.md",
        "facilitator-only/03-results-and-deviation-log.md",
        "facilitator-only/04-temporal-freeze-protocol-and-record-templates.md",
        "facilitator-only/05-execution-and-access-log.md",
        SYNTHETIC_ACCESS_PLAN,
    ]:
        content = contents.get(relative, "")
        for identity in access_identities:
            if identity not in content:
                errors.append(
                    f"temporal protocol: {relative} lacks synthetic access identity: "
                    f"{identity}"
                )

    for relative, content in contents.items():
        if relative == LIVE_UPDATE_PATH:
            continue
        matches = re.findall(
            rf"\*\*Packet:\*\* {PACKET_ID} version ([^\s]+)", content
        )
        if relative == "README.md":
            if f"**Version:** {PACKET_VERSION}" not in content:
                errors.append(
                    f"temporal protocol: README.md lacks packet version {PACKET_VERSION}"
                )
        elif matches != [PACKET_VERSION]:
            errors.append(
                f"temporal protocol: packet version identity invalid in {relative}: "
                f"{matches or 'missing'}"
            )

    semantic_clauses = {
        "README.md": [
            "select exactly one entry branch for the entire attempt",
            "Six completed artifact/manifest/verification/detached-record chains do not by themselves complete the route.",
            "complete immutable `DATA-RUN-RESULTS-v1.md` before `LOG_CLOSED`",
            "Layout evidence is not comprehension evidence.",
            "exact immutable participant/run input `DATA-A-LIVE-UPDATE-v1.md`",
            "The optional contract must be present in both manifests when used and absent from both when not used.",
            "The governing manifest `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` hashes exactly the included revised detail files and does not hash itself or the later detached record.",
            "Stage B Phase 2 specifically binds every included revised Stage A artifact, its governing manifest, and its detached record, in addition to the frozen Section 1 triple.",
            "new immutable filename and a new artifact ID/version",
            "Human participants use ordinary file surfaces and receive no terminal, repository, Git, or helper authority.",
            "Do not create future phase configs with guessed or dummy hashes; create each only from the observed verified phase-input manifest before its gate.",
            "On every invocation the helper hashes and parses that exact phase-input manifest",
            "requires its complete flat filename/hash set to equal `ordered_files` before enforcing the config-defined read order.",
            "technical platform restriction/security is `NOT ESTABLISHED` unless separately demonstrated.",
        ],
        "participant/01-consent-and-privacy.md": [
            "This notice is for the `HUMAN` entry branch only.",
            "A blank human notice never counts as synthetic consent.",
        ],
        "participant/00-packet-route.md": [
            "The branches are mutually exclusive.",
            "Any fictional human affirmation or human-result claim is a stop.",
            "Record `RUN_RESULTS_COMPLETED` before `LOG_CLOSED`.",
            "All six scored freeze chains may be complete while the full route remains incomplete.",
            "`DATA-A-LIVE-UPDATE-v1.md`. The optional contract must be present in both manifests when used and absent from both when not used.",
            "Only after that revision-phase input manifest verifies, open `DATA-A-LIVE-UPDATE-v1.md`",
            "It hashes exactly the included revised artifacts, never itself or the later verification record.",
            "At every phase boundary, the next sealed phase-input manifest must hash the completed artifact, its governing manifest, and its later detached verification record.",
            "Stage B Phase 2 must bind both the frozen Section 1 triple and every included revised Stage A artifact plus its governing manifest and detached record.",
            "`DATA-B-SECTION-1-SHA256SUMS-v1.txt` over the completed export only and create that detached record.",
            "`DATA-B-SECTION-2-SHA256SUMS-v1.txt` over only the completed export and create that detached record before opening either decision aid.",
            "`DATA-B-SECTIONS-3-5-SHA256SUMS-v1.txt` over only that completed export; then create the detached record.",
            "Collect all material feedback in the external run-specific results record",
            "new immutable filename and a new artifact ID/version",
            "No ad hoc facilitator message may substitute for a declared file.",
            "For every synthetic phase, the facilitator creates the phase config only after all current input bytes exist and before that phase gate opens.",
            "The config records that manifest's exact filename, absolute path, and SHA-256.",
            "On every invocation the helper rehashes and parses the manifest and requires complete flat filename/hash equality with `ordered_files`",
            "technical platform restriction is `NOT ESTABLISHED` unless separately demonstrated.",
        ],
        "participant/03-practitioner-workbook.md": [
            "Live-update input exact filename: `DATA-A-LIVE-UPDATE-v1.md`",
            "Optional initial contract disposition matched both the initial and revision-phase manifests",
            "without listing or hashing the manifest itself or the later record",
            "new immutable filename and a new artifact ID/version",
        ],
        "participant/02-scenario-and-task.md": [
            "Only then open exact immutable `DATA-A-LIVE-UPDATE-v1.md`.",
            "The optional initial data-product contract must be included in the revision-phase manifest exactly when it was used and included in the initial governing manifest.",
        ],
        "participant/04-decision-owner-workbook.md": [
            "Keep this section closed until the facilitator records `STAGE_B_SCORING_ENDED`",
            "Export this section separately as exactly `DATA-B-SECTION-6-DEBRIEF-v1.md`.",
            "The closing evidence manifest later hashes the completed export, governing manifest, and detached record.",
            "new immutable filename and a new artifact ID/version",
        ],
        "participant/05-one-screen-handoff.md": [
            "The completed file targets one US Letter portrait page with every margin at least 0.5 inch, body text at least 9 points",
            "no more than 450 reader-facing words excluding only immutable provenance metadata",
            "non-clickable exact-filename pointer",
            "Stage B Section 1 receives the handoff before revised detail is released in Section 2",
            "Even `LAYOUT PASSED` is local layout evidence, not proof that a person can scan, understand, or use the handoff.",
            "The manifest never hashes itself or the later record.",
            "Stage B's sealed Phase 1 input manifest hashes the handoff, its governing manifest, and the detached record.",
        ],
        "participant/06-revised-artifact-freeze-record.md": [
            "Live-update participant input exact filename: `DATA-A-LIVE-UPDATE-v1.md`",
            "Optional `DATA-A-INITIAL-DATA-PRODUCT-CONTRACT-v1.md` was included exactly when it appeared in the initial governing manifest and otherwise absent",
            "It never predicts a future event and is never listed in the governing manifest whose verification it records.",
            "the facilitator creates the next sealed phase-input manifest—or the closing evidence manifest for the final scope—over every governed artifact, its governing manifest, and this detached record.",
            "new immutable filename and a new artifact ID/version for every corrected artifact",
        ],
        "facilitator-only/01-facilitator-guide.md": [
            "Select exactly one entry branch before `RUN_STARTED` and keep it for the whole attempt.",
            "Record `RUN_RESULTS_COMPLETED` before `LOG_CLOSED`",
            "only then create `DATA-RUN-CLOSEOUT-v1.md` binding all three observed hashes",
            "sealed participant input `DATA-A-LIVE-UPDATE-v1.md`",
            "The optional contract must be present in both manifests when used and absent from both when not used.",
            "The manifest never lists or hashes itself or the later record.",
            "The next sealed phase-input manifest hashes each governed artifact, its governing manifest, and its detached verification record.",
            "Before Phase 2 opens, create and verify its sealed input manifest over the frozen Section 1 artifact, governing manifest, and detached record; every included revised Stage A artifact; the revised Stage A governing manifest; the revised Stage A detached record; and the scenario.",
            "new immutable filename and a new artifact ID/version",
            "Do not predict later participant artifact hashes or use dummy hashes.",
            "A config created after its phase gate, shared cross-phase helper log, ad hoc message delivery, or unreconciled helper row is a stop and deviation.",
            "bind the exact verified phase-input manifest filename, absolute path, and SHA-256.",
            "On every invocation the helper must rehash and parse that phase-input manifest and require complete flat membership/hash equality with `ordered_files`",
            "record that state as `NOT ESTABLISHED` unless separate retained evidence demonstrates it.",
        ],
        "facilitator-only/02-observation-and-scoring-rubric.md": [
            "Entry-branch integrity",
            "Full-route closure",
            "Results and external closeout",
            "Literal layout proof",
            "Revision-input integrity",
            "exact immutable `DATA-A-LIVE-UPDATE-v1.md`",
            "no governing manifest hashes itself or its later record",
            "the next phase or closing manifest hashes the artifact, governing manifest, and record",
            "new immutable filename and new artifact ID/version for every corrected artifact",
            "Synthetic exact-file access integrity",
            "on every invocation the helper parses and hashes the phase manifest, requires complete flat config/manifest membership/hash equality",
            "Platform restriction claim boundary",
            "helper compliance is not sandbox proof",
        ],
        "facilitator-only/03-results-and-deviation-log.md": [
            "This checked-in file is a source template, not a completed result.",
            "state `RESULTS COMPLETE`, then record `RUN_RESULTS_COMPLETED` before `LOG_CLOSED`",
            "No predicted final closed-log hash or future closeout timestamp appears in this record",
            "A favorable one-page or one-screen claim without the completed proof record",
            "Immutable live-update participant input exact filename/hash: `DATA-A-LIVE-UPDATE-v1.md` /",
            "included in both the initial and revision-phase manifests when used, and absent from both when not used",
            "Every governing manifest excludes itself and its later detached record",
            "Every next phase/evidence manifest hashes the artifact(s), governing manifest, and detached record under literal filenames",
            "| Stage A revised set | required revised files; optional only if used | `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` / | | `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md` / | Stage B Phase 2 input / |",
            "new immutable filename and a new artifact ID/version",
            "Future/dummy config hashes or config created after its phase gate: none / deviation ID / `NOT APPLICABLE — HUMAN`",
            "Exact verified phase-input manifest filename/absolute path/SHA-256 bound by each config, plus config/manifest membership/hash equality result:",
            "Every config and helper invocation matched the exact verified phase-input manifest membership/hashes",
            "Technical platform restriction/security result: `NOT ESTABLISHED` unless separately demonstrated / `NOT APPLICABLE — HUMAN`",
        ],
        "facilitator-only/04-temporal-freeze-protocol-and-record-templates.md": [
            "Select exactly `HUMAN` or `SYNTHETIC` once before `RUN_STARTED`.",
            "Their completion does not establish full-route closure.",
            "Complete the blank results template as exact `DATA-RUN-RESULTS-v1.md`, state `RESULTS COMPLETE`, before `LOG_CLOSED`.",
            "The closeout record is later external provenance.",
            "exact immutable `DATA-A-LIVE-UPDATE-v1.md`",
            "conditional `DATA-A-INITIAL-DATA-PRODUCT-CONTRACT-v1.md` exactly when it was used and appears in the initial governing manifest, and otherwise not",
            "Verify this manifest before opening the live update.",
            "Do not invent future artifact hashes.",
            "On every invocation, the helper rehashes and parses the bound phase-input manifest",
            "through an explicitly serialized write-all loop and fsync",
            "helper-only procedural compliance separately, and keep technical platform restriction/security `NOT ESTABLISHED` unless separately demonstrated",
        ],
        "facilitator-only/05-execution-and-access-log.md": [
            "The branch is selected once before `RUN_STARTED`.",
            "Required whole-route boundary sequence",
            "`LOG_CLOSED` cannot precede it.",
            "The closeout record is later external provenance.",
            "exact immutable `DATA-A-LIVE-UPDATE-v1.md`",
            "The optional contract must be absent here when it was not used.",
            "An absent, drifted, outside-root, malformed, duplicate, path-bearing, self-listing, or mismatched phase-input manifest; future/dummy hashes; config creation after the gate; shared cross-phase helper logs; changed helper/config bytes; general commands; direct reads; and ad hoc message delivery are stops.",
            "On every invocation, the helper rehashes and parses that phase-input manifest and requires exact config/manifest filename membership and hash equality before any target read.",
            "The helper uses a serialized write-all append and fsync",
            "Its boundary is observed separately from host-platform restriction, which remains `NOT ESTABLISHED` unless proved.",
        ],
        SYNTHETIC_CONTEXT_TEMPLATE: [
            "not consent and not a result",
            "`SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA`",
            "Any blank required field, branch mixing, fictional human affirmation, human result claim, absent or after-start helper, overbroad helper authority, or ad hoc message delivery stops the run before scored input opens.",
            "Every later per-phase config must bind the exact verified phase-input manifest flat filename, absolute path inside sealed input, and observed SHA-256.",
            "On every invocation, the helper must rehash and parse that manifest and require exact config/manifest membership and member-hash equality",
            "Technical platform restriction/security state: `NOT ESTABLISHED` unless separately demonstrated with retained platform evidence",
        ],
        SYNTHETIC_ACCESS_PLAN: [
            "Human participants use ordinary file surfaces and receive no terminal, repository, Git, or helper authority.",
            "Before `RUN_STARTED`, select and verify the helper, predeclare every phase access directory",
            "Create a distinct immutable config and helper/config binding manifest only when that phase's complete input bytes exist, but always before the current phase gate opens.",
            "The helper enforces its own exact-file boundary, but it does not prove that the host platform removes other tools.",
            "Ad hoc facilitator delivery is a deviation, not transport.",
            "Future/dummy hashes",
            "flat filename/hash set must equal the exact verified phase-input manifest named, located, and hashed by the three `phase_input_manifest_*` fields.",
            "The helper rehashes and parses that manifest on every invocation",
            "explicitly serialized write-all loop and fsyncs one JSONL row",
            "technical platform restriction/security remains `NOT ESTABLISHED` unless separately demonstrated",
        ],
        LAYOUT_TEMPLATE: [
            "one US Letter portrait page",
            "every margin is at least 0.5 inch",
            "body text is at least 9 points",
            "no more than 450 words excluding only immutable provenance metadata",
            "it does not test whether a person can scan, understand, or use the handoff",
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
        "participant/00-packet-route.md",
        [
            "record `STAGE_B_SCORING_ENDED`",
            "Create and verify `DATA-B-PHASE-4-DEBRIEF-INPUT-SHA256SUMS-v1.txt`",
            "Open Section 6 only after that gate",
            "Record `STAGE_B_SECTION_6_DEBRIEF_COMPLETED`, then `STAGE_B_ENDED`",
            "Complete the immutable run-specific results record",
            "Record `RUN_RESULTS_COMPLETED` before `LOG_CLOSED`",
            "Create and verify `DATA-RUN-CLOSEOUT-SHA256SUMS-v1.txt`",
            "Only afterward complete `DATA-RUN-CLOSEOUT-v1.md`",
        ],
        "scoring end -> debrief -> stage end -> results -> log close -> closeout",
    )
    require_order(
        errors,
        contents,
        "facilitator-only/05-execution-and-access-log.md",
        [
            f"{index}. `{event}`"
            for index, event in enumerate(ROUTE_BOUNDARY_SEQUENCE, start=1)
        ],
        "whole-route boundary",
    )
    require_order(
        errors,
        contents,
        "participant/00-packet-route.md",
        [
            "Create and verify `DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt`",
            "Only after that revision-phase input manifest verifies, open `DATA-A-LIVE-UPDATE-v1.md`",
        ],
        "revision manifest verification -> immutable live-update open",
    )
    require_order(
        errors,
        contents,
        "facilitator-only/01-facilitator-guide.md",
        [
            "Create and verify `DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt`",
            "Only after that revision-phase input manifest verifies, deliver and open sealed participant input `DATA-A-LIVE-UPDATE-v1.md`",
        ],
        "revision manifest verification -> immutable live-update delivery",
    )
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
    """Check packet 1.2.8's static temporal-order invariants."""

    packet = ROOT / "testing/ai-ready-data-reader-value-v1"
    contents: dict[str, str] = {}
    for relative in TEMPORAL_PROTOCOL_FILES:
        path = packet / relative
        if not path.is_file():
            errors.append(f"temporal protocol: missing {path.relative_to(ROOT)}")
            continue
        contents[relative] = path.read_text(encoding="utf-8")
    for path in packet.rglob("*.md"):
        if belongs_to_independent_subpackage(path, packet):
            continue
        relative = path.relative_to(packet).as_posix()
        contents.setdefault(relative, path.read_text(encoding="utf-8"))
    if content_overrides:
        contents.update(content_overrides)

    errors.extend(temporal_protocol_content_errors(contents))
    return len(TEMPORAL_PROTOCOL_FILES)


def canonical_blockquote(content: str, start: str, end: str) -> str | None:
    """Extract one canonical Markdown blockquote as exact participant bytes."""

    if content.count(start) != 1 or content.count(end) != 1:
        return None
    _, remainder = content.split(start, 1)
    block, _ = remainder.split(end, 1)
    lines = block.strip("\n").splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    extracted: list[str] = []
    for line in lines:
        if line == ">":
            extracted.append("")
        elif line.startswith("> "):
            extracted.append(line[2:])
        else:
            return None
    return "\n".join(extracted) + "\n"


def protocol_target(packet: Path, raw: object, field: str, errors: list[str]) -> Path | None:
    """Resolve one declared packet-relative protocol path without escape."""

    if not isinstance(raw, str) or not raw:
        errors.append(f"temporal protocol JSON: {field} must be a relative path")
        return None
    target = (packet / raw).resolve()
    try:
        target.relative_to(packet.resolve())
    except ValueError:
        errors.append(f"temporal protocol JSON: {field} escapes packet")
        return None
    return target


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
    expected_synthetic_fields = [
        "packet_id_version",
        "attempt_id",
        "fictional_scenario_only",
        "no_human_consent_or_result",
        "stage_a_actor",
        "stage_b_actor",
        "facilitator",
        "orchestration_aided_status",
        "orchestration_manifest_identity",
        "evidence_root",
        "retention_boundary",
        "access_boundary",
        "source_helper_identity",
        "run_helper_identity",
        "predeclared_phase_access_directories",
        "per_phase_config_schema",
        "per_phase_input_manifest_identity_path_hash",
        "per_phase_binding_manifest_identity",
        "per_phase_access_log_identity",
        "actor_instruction_invocation",
        "helper_selected_and_verified_before_run",
        "helper_boundary_state",
        "technical_platform_restriction_state",
        "ad_hoc_message_delivery_forbidden",
        "run_start_timestamp_timezone",
        "pre_scored_log_checkpoint",
    ]
    expected_results_fields = [
        "packet_attempt_actor_facilitator_identity",
        "source_and_orchestration_manifest_identity",
        "six_freeze_chain_results",
        "final_pre_close_log_checkpoint",
        "input_open_artifact_verification_record_boundary_counts",
        "interventions_deviations_stops_rejected_attempts",
        "semantic_inventions_layout_failures_variances",
        "reader_value_scores_domain_gate_findings",
        "protocol_state",
        "synthetic_behavior_state",
        "synthetic_helper_or_human_surface_identity",
        "phase_input_manifest_config_binding",
        "per_phase_helper_log_reconciliation",
        "technical_platform_restriction_state",
        "layout_state",
        "human_state",
        "data_readiness_state",
        "real_world_state",
        "decision_and_evidence_limits",
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
    expected_synthetic_phase_gate_sequence = [
        "SEALED_INPUT_MANIFEST_CREATED",
        "SEALED_INPUT_MANIFEST_VERIFIED",
        "SYNTHETIC_ACCESS_CONFIG_CREATED",
        "SYNTHETIC_ACCESS_BINDING_MANIFEST_CREATED",
        "SYNTHETIC_ACCESS_BINDING_MANIFEST_VERIFIED",
        "PHASE_GATE_OPENED",
        "FILE_OPENED_OR_ACCESS_ATTEMPT_RECORDED",
    ]
    expected_synthetic_helper_event_fields = [
        "helper_access_log_path",
        "helper_access_event_id",
        "phase_input_manifest_filename",
        "phase_input_manifest_path",
        "phase_input_manifest_sha256",
        "helper_config_sha256",
        "helper_binding_manifest_sha256",
        "helper_outcome",
    ]

    if protocol.get("schema_version") != TEMPORAL_SCHEMA_VERSION:
        errors.append(
            f"temporal protocol JSON: schema_version must be {TEMPORAL_SCHEMA_VERSION}"
        )
    if protocol.get("packet_id") != PACKET_ID:
        errors.append("temporal protocol JSON: packet_id mismatch")
    if protocol.get("packet_version") != PACKET_VERSION:
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

    entry_branch = protocol.get("entry_branch")
    expected_entry_branch = {
        "selection_event": "ENTRY_BRANCH_SELECTED",
        "selection_required_before": "RUN_STARTED",
        "mutually_exclusive": True,
        "mixed_branch_forbidden": True,
        "human": {
            "consent_template_path": "participant/01-consent-and-privacy.md",
            "completed_real_person_consent_required": True,
            "blank_consent_stops": True,
            "synthetic_context_forbidden": True,
        },
        "synthetic": {
            "context_template_path": SYNTHETIC_CONTEXT_TEMPLATE,
            "run_record_filename": SYNTHETIC_CONTEXT_FILENAME,
            "manifest": SYNTHETIC_CONTEXT_MANIFEST,
            "manifest_members": [SYNTHETIC_CONTEXT_FILENAME],
            "manifest_verified_before_scored_input": True,
            "human_consent_claim_forbidden": True,
            "human_result_claim_forbidden": True,
            "required_literal": "SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA",
            "required_fields": expected_synthetic_fields,
        },
    }
    if entry_branch != expected_entry_branch:
        errors.append(
            "temporal protocol JSON: entry branch must preserve exact mutually exclusive "
            "human-consent or synthetic-context semantics"
        )
    for path, label in [
        (
            expected_entry_branch["human"]["consent_template_path"],
            "human consent template",
        ),
        (SYNTHETIC_CONTEXT_TEMPLATE, "synthetic context template"),
    ]:
        target = protocol_target(packet, path, label, errors)
        if target and not target.is_file():
            errors.append(f"temporal protocol JSON: missing {label} {path}")

    expected_synthetic_access = {
        "applies_only_to_branch": "SYNTHETIC",
        "human_branch_ordinary_file_surfaces_only": True,
        "source_helper_path": SYNTHETIC_HELPER_SOURCE,
        "source_helper_sha256": SYNTHETIC_HELPER_SHA256,
        "plan_template_path": SYNTHETIC_ACCESS_PLAN,
        "run_helper_filename": SYNTHETIC_RUN_HELPER,
        "helper_selected_before_event": "RUN_STARTED",
        "declared_in_orchestration_manifest": True,
        "declared_in_synthetic_context": True,
        "predeclared_phase_directories_required": True,
        "config_filename": SYNTHETIC_ACCESS_CONFIG,
        "config_schema_version": 2,
        "config_created_after_verified_phase_input_manifest": True,
        "config_created_before_event": "CURRENT_PHASE_GATE_OPENED",
        "future_or_dummy_hashes_forbidden": True,
        "phase_input_manifest_identity_required": True,
        "phase_input_manifest_absolute_path_required": True,
        "phase_input_manifest_sha256_required": True,
        "phase_input_manifest_verified_every_invocation": True,
        "phase_input_manifest_must_be_inside_input_root": True,
        "phase_input_manifest_flat_members_only": True,
        "phase_input_manifest_duplicate_members_forbidden": True,
        "phase_input_manifest_self_entry_forbidden": True,
        "config_membership_must_equal_phase_manifest": True,
        "config_hashes_must_equal_phase_manifest": True,
        "read_order_may_be_config_defined_after_exact_membership": True,
        "binding_manifest": SYNTHETIC_ACCESS_BINDING_MANIFEST,
        "binding_manifest_members": ["run_helper", "current_phase_config"],
        "binding_manifest_verified_before_event": "CURRENT_PHASE_GATE_OPENED",
        "access_log_filename": SYNTHETIC_ACCESS_LOG,
        "fixed_audit_log_argument_required": True,
        "distinct_log_per_phase": True,
        "access_log_outside_participant_input": True,
        "current_phase_flat_filename_allowlist_only": True,
        "read_order_enforced": True,
        "target_sha256_enforced": True,
        "optional_skip_only_when_declared": True,
        "every_access_or_refusal_logged": True,
        "execution_log_reconciliation_required": True,
        "serial_invocation_required": True,
        "actor_instruction_exact_helper_only": True,
        "helper_grants_general_terminal_or_shell": False,
        "repository_browsing_allowed": False,
        "git_allowed": False,
        "internet_allowed": False,
        "direct_filesystem_read_allowed": False,
        "undeclared_message_input_allowed": False,
        "ad_hoc_message_delivery_allowed": False,
        "technical_platform_restriction_default_state": "NOT ESTABLISHED",
        "sandbox_security_claimed": False,
    }
    if protocol.get("synthetic_exact_file_access") != expected_synthetic_access:
        errors.append(
            "temporal protocol JSON: synthetic exact-file access must preserve "
            "pre-run helper identity, exact phase-input manifest binding and "
            "membership/hash equality, current-phase observed-hash gating, "
            "bounded authority, refusal logging, and the platform non-claim"
        )
    helper_source = protocol_target(
        packet,
        expected_synthetic_access["source_helper_path"],
        "synthetic exact-file helper source",
        errors,
    )
    if helper_source and not helper_source.is_file():
        errors.append("temporal protocol JSON: synthetic exact-file helper is missing")
    elif helper_source and sha256(helper_source) != SYNTHETIC_HELPER_SHA256:
        errors.append("temporal protocol JSON: protected synthetic helper hash mismatch")
    access_plan = protocol_target(
        packet,
        expected_synthetic_access["plan_template_path"],
        "synthetic access plan template",
        errors,
    )
    if access_plan and not access_plan.is_file():
        errors.append("temporal protocol JSON: synthetic access plan is missing")

    route_closure = protocol.get("route_closure")
    expected_route_closure = {
        "six_scored_freeze_chains": expected_release_ids,
        "freeze_chain_completion_is_full_route_completion": False,
        "required_boundary_sequence": ROUTE_BOUNDARY_SEQUENCE,
        "stage_a_explanation_forbidden_before": "STAGE_B_SCORING_ENDED",
        "debrief_phase_input": {
            "manifest": DEBRIEF_MANIFEST,
            "created_after": "STAGE_B_SCORING_ENDED",
            "verified_before_open": True,
            "required_members": [
                "DATA-B-SECTIONS-3-5-DECISION-v1.md",
                "DATA-B-SECTIONS-3-5-SHA256SUMS-v1.txt",
                "DATA-B-SECTIONS-3-5-FREEZE-VERIFICATION-v1.md",
                DEBRIEF_INPUT_FILENAME,
            ],
        },
        "debrief_output": {
            "filename": DEBRIEF_OUTPUT_FILENAME,
            "state": "DEBRIEF COMPLETE",
            "completed_before": "STAGE_B_ENDED",
            "may_modify_scored_bytes": False,
        },
    }
    if route_closure != expected_route_closure:
        errors.append(
            "temporal protocol JSON: full-route closure boundaries, debrief gate, or "
            "six-freeze-chain distinction invalid"
        )

    run_results = protocol.get("run_results")
    expected_run_results = {
        "source_template": "facilitator-only/03-results-and-deviation-log.md",
        "filename": RUN_RESULTS_FILENAME,
        "state": "RESULTS COMPLETE",
        "completion_event": "RUN_RESULTS_COMPLETED",
        "completed_before_log_close": True,
        "required_fields": expected_results_fields,
        "predicted_final_closed_log_hash_forbidden": True,
        "future_closeout_timestamp_forbidden": True,
    }
    if run_results != expected_run_results:
        errors.append(
            "temporal protocol JSON: immutable run-results identity, fields, or "
            "pre-close ordering invalid"
        )
    results_template = protocol_target(
        packet,
        expected_run_results["source_template"],
        "run-results source template",
        errors,
    )
    if results_template and not results_template.is_file():
        errors.append(
            "temporal protocol JSON: run-results source template is missing"
        )

    external_closeout = protocol.get("external_closeout")
    expected_external_closeout = {
        "created_after": "LOG_CLOSED",
        "closed_log_filename": EXECUTION_LOG_FILENAME,
        "closed_log_copy_byte_identical": True,
        "manifest": CLOSEOUT_MANIFEST,
        "manifest_members": [EXECUTION_LOG_FILENAME, RUN_RESULTS_FILENAME],
        "record": CLOSEOUT_RECORD,
        "record_created_after_manifest_verification": True,
        "required_record_bindings": [
            "closed_log_sha256",
            "closeout_manifest_sha256",
            "run_results_sha256",
        ],
        "closed_log_may_predict_external_hash_or_closeout_time": False,
    }
    if external_closeout != expected_external_closeout:
        errors.append(
            "temporal protocol JSON: later external closeout identity, membership, "
            "or observed-hash binding invalid"
        )

    handoff_layout = protocol.get("handoff_layout_proof")
    expected_handoff_layout = {
        "source_template": LAYOUT_TEMPLATE,
        "record": LAYOUT_RECORD,
        "markdown": "DATA-A-ONE-SCREEN-HANDOFF-v1.md",
        "pdf": LAYOUT_PDF,
        "target": {
            "page_size": "US Letter",
            "orientation": "portrait",
            "maximum_pages": 1,
            "minimum_margin_inches": 0.5,
            "minimum_body_text_points": 9,
            "maximum_reader_facing_words": 450,
            "word_count_excludes_only": "immutable provenance metadata",
            "clipping_allowed": False,
            "overlap_allowed": False,
            "hidden_overflow_allowed": False,
            "unreadable_shrinking_allowed": False,
        },
        "participant_template_contract": {
            "provenance_start_marker": HANDOFF_PROVENANCE_START,
            "provenance_end_marker": HANDOFF_PROVENANCE_END,
            "provenance_maximum_compact_lines": 8,
            "provenance_excluded_from_reader_word_count": True,
            "provenance_excluded_from_page_layout": False,
            "markdown_table_allowed": False,
            "copied_detail_allowed": False,
            "detail_transfer": "non-clickable exact-filename pointers",
            "runtime_markdown_detail_links_allowed": False,
            "combined_reader_target_words": HANDOFF_READER_TARGET,
            "hard_reader_maximum_words": 450,
            "reader_sections": HANDOFF_READER_SECTIONS,
        },
        "required_evidence": [
            "generated_markdown",
            "generated_pdf",
            "page_count",
            "rendering_command",
            "tool_versions",
            "pdf_sha256",
        ],
        "favorable_claim_requires_passed_proof": True,
        "proves_human_comprehension": False,
    }
    if handoff_layout != expected_handoff_layout:
        errors.append(
            "temporal protocol JSON: one-page US Letter handoff proof contract or "
            "non-comprehension boundary invalid"
        )

    expected_handoff_detail_boundary = {
        "runtime_handoff_reference": "non-clickable exact-filename pointers",
        "runtime_markdown_detail_links_forbidden": True,
        "stage_b_phase_1": {
            "manifest": "DATA-B-PHASE-1-INPUT-SHA256SUMS-v1.txt",
            "only_stage_a_evidence_is_handoff_triple": True,
            "route_and_blank_section_1_workbook_allowed": True,
            "revised_detail_allowed": False,
        },
        "stage_b_phase_2": {
            "manifest": "DATA-B-PHASE-2-INPUT-SHA256SUMS-v1.txt",
            "revised_detail_first_allowed": True,
            "requires_revised_artifacts_manifest_and_detached_record": True,
        },
        "constructed_miniature": {
            "path": "examples/one-screen-handoff-miniature-v1.md",
            "outside_packet": True,
            "participant_or_scored_input_allowed": False,
            "working_link_allowed_only_here": True,
        },
    }
    if protocol.get("handoff_detail_access_boundary") != expected_handoff_detail_boundary:
        errors.append(
            "temporal protocol JSON: handoff-only Phase 1 and detail-later "
            "Phase 2 access boundary invalid"
        )
    layout_template = protocol_target(
        packet,
        LAYOUT_TEMPLATE,
        "handoff layout proof source template",
        errors,
    )
    if layout_template and not layout_template.is_file():
        errors.append(
            "temporal protocol JSON: handoff layout proof source template is missing"
        )

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
    if (
        execution.get("synthetic_phase_gate_sequence")
        != expected_synthetic_phase_gate_sequence
    ):
        errors.append(
            "temporal protocol JSON: synthetic config/binding creation and "
            "verification must follow phase-input verification and precede the gate"
        )
    if (
        execution.get("synthetic_helper_event_binding_fields")
        != expected_synthetic_helper_event_fields
    ):
        errors.append(
            "temporal protocol JSON: synthetic helper events lack exact "
            "per-phase access-log reconciliation fields"
        )

    if protocol.get("next_release_bindings") != [
        "governed_artifacts",
        "governing_manifest",
        "detached_verification_record",
    ]:
        errors.append("temporal protocol JSON: next-release triple is invalid")

    revision_input = protocol.get("revision_phase_input")
    if not isinstance(revision_input, dict):
        errors.append("temporal protocol JSON: revision_phase_input must be an object")
        revision_input = {}
    else:
        if revision_input.get("id") != REVISION_PHASE_ID:
            errors.append("temporal protocol JSON: revision phase input identity invalid")
        if revision_input.get("prior_release") != REVISION_PRIOR_RELEASE:
            errors.append(
                "temporal protocol JSON: revision phase input must bind stage_a_initial"
            )
        if revision_input.get("opens_release") != REVISION_OPENS_RELEASE:
            errors.append(
                "temporal protocol JSON: revision phase input must open stage_a_revised"
            )
        if revision_input.get("manifest") != REVISION_MANIFEST:
            errors.append(
                f"temporal protocol JSON: revision input manifest must be {REVISION_MANIFEST}"
            )
        if revision_input.get("manifest_verified_before_open") is not True:
            errors.append(
                "temporal protocol JSON: revision manifest must verify before live-update open"
            )
        if revision_input.get("conditional_members") != REVISION_CONDITIONAL_MEMBERS:
            errors.append(
                "temporal protocol JSON: optional initial contract membership semantics weakened"
            )
        if revision_input.get("allow_other_members") is not False:
            errors.append(
                "temporal protocol JSON: revision manifest must reject undeclared members"
            )

        live_update = revision_input.get("immutable_participant_input")
        if not isinstance(live_update, dict):
            errors.append(
                "temporal protocol JSON: immutable live-update input must be an object"
            )
        else:
            if live_update.get("filename") != LIVE_UPDATE_FILENAME:
                errors.append(
                    f"temporal protocol JSON: immutable live-update filename must be {LIVE_UPDATE_FILENAME}"
                )
            if live_update.get("path") != LIVE_UPDATE_PATH:
                errors.append(
                    f"temporal protocol JSON: immutable live-update path must be {LIVE_UPDATE_PATH}"
                )
            live_path = protocol_target(
                packet,
                live_update.get("path"),
                "immutable live-update input",
                errors,
            )
            live_hash = live_update.get("sha256")
            if not isinstance(live_hash, str) or not re.fullmatch(
                r"[0-9a-f]{64}", live_hash
            ):
                errors.append("temporal protocol JSON: invalid immutable live-update SHA-256")
            elif live_path and live_path.is_file() and sha256(live_path) != live_hash:
                errors.append(
                    "temporal protocol JSON: immutable live-update input hash mismatch"
                )
            if live_path and not live_path.is_file():
                errors.append(
                    f"temporal protocol JSON: missing immutable live-update input {LIVE_UPDATE_PATH}"
                )

            if live_update.get("canonical_facilitator_source") != LIVE_UPDATE_CANONICAL_SOURCE:
                errors.append(
                    "temporal protocol JSON: immutable live-update canonical source invalid"
                )
            if live_update.get("canonical_start_marker") != LIVE_UPDATE_START_MARKER:
                errors.append(
                    "temporal protocol JSON: immutable live-update canonical start marker invalid"
                )
            if live_update.get("canonical_end_marker") != LIVE_UPDATE_END_MARKER:
                errors.append(
                    "temporal protocol JSON: immutable live-update canonical end marker invalid"
                )
            canonical_path = protocol_target(
                packet,
                live_update.get("canonical_facilitator_source"),
                "live-update canonical facilitator source",
                errors,
            )
            if (
                live_path
                and live_path.is_file()
                and canonical_path
                and canonical_path.is_file()
            ):
                canonical = canonical_blockquote(
                    canonical_path.read_text(encoding="utf-8"),
                    LIVE_UPDATE_START_MARKER,
                    LIVE_UPDATE_END_MARKER,
                )
                if canonical is None:
                    errors.append(
                        "temporal protocol JSON: canonical facilitator live-update block missing or malformed"
                    )
                elif live_path.read_text(encoding="utf-8") != canonical:
                    errors.append(
                        "temporal protocol JSON: immutable live-update input differs from canonical facilitator wording"
                    )

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
    release_map = {
        item.get("id"): item for item in releases if isinstance(item, dict)
    }
    initial_release = release_map.get(REVISION_PRIOR_RELEASE)
    if isinstance(initial_release, dict):
        initial_artifacts = initial_release.get("artifacts", [])
        if not isinstance(initial_artifacts, list):
            initial_artifacts = []
        required_initial_names = [
            artifact.get("filename")
            for artifact in initial_artifacts
            if isinstance(artifact, dict)
            and artifact.get("optional") is not True
            and isinstance(artifact.get("filename"), str)
        ]
        optional_initial_names = [
            artifact.get("filename")
            for artifact in initial_artifacts
            if isinstance(artifact, dict)
            and artifact.get("optional") is True
            and isinstance(artifact.get("filename"), str)
        ]
        if required_initial_names != [
            "DATA-A-INITIAL-WORKBOOK-v1.md",
            "DATA-A-INITIAL-READINESS-ASSESSMENT-v1.md",
        ]:
            errors.append(
                "temporal protocol JSON: required Stage A initial artifact branch invalid"
            )
        if optional_initial_names != [OPTIONAL_INITIAL_CONTRACT]:
            errors.append(
                "temporal protocol JSON: optional Stage A initial contract branch invalid"
            )
        expected_revision_members = [
            *required_initial_names,
            initial_release.get("governing_manifest"),
            initial_release.get("detached_record"),
            LIVE_UPDATE_FILENAME,
        ]
        if revision_input.get("required_members") != expected_revision_members:
            errors.append(
                "temporal protocol JSON: revision input omits or changes required manifest members"
            )
        declared_conditional_members = revision_input.get("conditional_members", [])
        if not isinstance(declared_conditional_members, list):
            declared_conditional_members = []
        conditional_names = [
            item.get("filename")
            for item in declared_conditional_members
            if isinstance(item, dict)
        ]
        if conditional_names != optional_initial_names:
            errors.append(
                "temporal protocol JSON: revision input conditional members do not match optional initial artifacts"
            )
        if revision_input.get("manifest") != initial_release.get(
            "next_release_manifest"
        ):
            errors.append(
                "temporal protocol JSON: revision input manifest is not bound to stage_a_initial"
            )
        if initial_release.get("next_release_additional_inputs") != [
            LIVE_UPDATE_FILENAME
        ]:
            errors.append(
                "temporal protocol JSON: stage_a_initial must declare exact immutable live-update input"
            )
    else:
        errors.append("temporal protocol JSON: stage_a_initial release missing")

    final_release = release_map.get("stage_b_sections_3_5")
    if isinstance(final_release, dict):
        final_artifacts = final_release.get("artifacts", [])
        final_names = [
            artifact.get("filename")
            for artifact in final_artifacts
            if isinstance(artifact, dict)
            and isinstance(artifact.get("filename"), str)
        ]
        expected_debrief_members = [
            *final_names,
            final_release.get("governing_manifest"),
            final_release.get("detached_record"),
            DEBRIEF_INPUT_FILENAME,
        ]
        debrief_input = (
            route_closure.get("debrief_phase_input", {})
            if isinstance(route_closure, dict)
            else {}
        )
        if debrief_input.get("required_members") != expected_debrief_members:
            errors.append(
                "temporal protocol JSON: debrief input manifest does not bind the "
                "final scored artifact triple and exact Section 6 input"
            )
        if final_release.get("next_release_manifest") != DEBRIEF_MANIFEST:
            errors.append(
                "temporal protocol JSON: final scored release does not open the exact "
                "debrief manifest"
            )
        if final_release.get("next_release_additional_inputs") != [
            DEBRIEF_INPUT_FILENAME
        ]:
            errors.append(
                "temporal protocol JSON: final scored release must add only the exact "
                "Section 6 input"
            )
    else:
        errors.append("temporal protocol JSON: stage_b_sections_3_5 release missing")

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
        additional_inputs = release.get("next_release_additional_inputs", [])
        if not isinstance(additional_inputs, list) or not all(
            isinstance(value, str) and value for value in additional_inputs
        ):
            errors.append(
                f"temporal protocol JSON: {release_id} next_release_additional_inputs invalid"
            )
            additional_inputs = []
        if (
            release_id != REVISION_PRIOR_RELEASE
            and LIVE_UPDATE_FILENAME in additional_inputs
        ):
            errors.append(
                f"temporal protocol JSON: immutable live update bound to wrong release {release_id}"
            )
        expected_additional_inputs = {
            REVISION_PRIOR_RELEASE: [LIVE_UPDATE_FILENAME],
            "stage_b_sections_3_5": [DEBRIEF_INPUT_FILENAME],
        }.get(release_id, [])
        if additional_inputs != expected_additional_inputs:
            errors.append(
                f"temporal protocol JSON: {release_id} next-release additional input "
                "inventory invalid"
            )

    critical = protocol.get("critical_documents", [])
    expected_markdown = {
        path.relative_to(packet).as_posix()
        for path in packet.rglob("*.md")
        if not belongs_to_independent_subpackage(path, packet)
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
            and not belongs_to_independent_subpackage(path, checksum_path.parent)
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
