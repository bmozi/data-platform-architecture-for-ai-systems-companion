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


def validate_temporal_freeze_protocol(errors: list[str]) -> int:
    """Check packet 1.2.1's static temporal-order invariants."""

    packet = ROOT / "testing/ai-ready-data-reader-value-v1"
    relative_files = [
        "README.md",
        "participant/00-packet-route.md",
        "participant/03-practitioner-workbook.md",
        "participant/04-decision-owner-workbook.md",
        "participant/05-one-screen-handoff.md",
        "participant/06-revised-artifact-freeze-record.md",
        "facilitator-only/01-facilitator-guide.md",
        "facilitator-only/02-observation-and-scoring-rubric.md",
        "facilitator-only/03-results-and-deviation-log.md",
    ]
    contents: dict[str, str] = {}
    for relative in relative_files:
        path = packet / relative
        if not path.is_file():
            errors.append(f"temporal protocol: missing {path.relative_to(ROOT)}")
            continue
        contents[relative] = path.read_text(encoding="utf-8")

    combined = "\n".join(contents.values())
    legacy = "DATA-A-REVISED-FREEZE-RECORD-v1.md"
    if legacy in combined:
        errors.append(f"temporal protocol: legacy record identity remains: {legacy}")

    exact_identities = [
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
        "participant/04-decision-owner-workbook.md": exact_identities[4:],
        "participant/05-one-screen-handoff.md": exact_identities[:4],
    }
    for relative, identities in required_by_file.items():
        content = contents.get(relative, "")
        for identity in identities:
            if identity not in content:
                errors.append(
                    f"temporal protocol: {relative} lacks exact identity: {identity}"
                )

    for path in packet.rglob("*.md"):
        content = path.read_text(encoding="utf-8")
        for match in re.finditer(r"\*\*Packet:\*\* DATA-RV-PILOT-001 version ([^\s]+)", content):
            if match.group(1) != "1.2.1":
                errors.append(
                    f"temporal protocol: packet version drift in "
                    f"{path.relative_to(ROOT)}: {match.group(1)}"
                )

    guide = contents.get("facilitator-only/01-facilitator-guide.md", "")
    ordered_anchors = [
        "Finalize every governed artifact",
        "Create the governing manifest",
        "Verify that manifest",
        "Only afterward create the detached record",
    ]
    positions = [guide.find(anchor) for anchor in ordered_anchors]
    if any(position < 0 for position in positions) or positions != sorted(positions):
        errors.append(
            "temporal protocol: facilitator guide lacks the required ordered "
            "complete -> manifest -> verify -> detached-record sequence"
        )

    workbook = contents.get("participant/04-decision-owner-workbook.md", "")
    handoff = contents.get("participant/05-one-screen-handoff.md", "")
    practitioner = contents.get("participant/03-practitioner-workbook.md", "")
    stale_self_reference_fields = [
        "Section 1 freeze timestamp and timezone:",
        "Section 1 SHA-256 or manifest reference:",
        "Section 2 freeze timestamp and timezone:",
        "Section 2 SHA-256 or manifest reference:",
        "Sections 3-5 freeze timestamp and timezone:",
        "Sections 3-5 SHA-256 or manifest reference:",
        "Separate handoff freeze timestamp/timezone",
    ]
    governed_templates = workbook + "\n" + handoff
    for field in stale_self_reference_fields:
        if field in governed_templates:
            errors.append(f"temporal protocol: stale self-reference field: {field}")

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

    template = contents.get("participant/06-revised-artifact-freeze-record.md", "")
    template_anchors = [
        "create an instance only after its governing",
        "never lists or hashes itself or this later record",
        "observed manifest verification timestamp/timezone",
        "immutable replacement set",
    ]
    for anchor in template_anchors:
        if anchor.casefold() not in template.casefold():
            errors.append(f"temporal protocol: detached template lacks: {anchor}")

    return len(relative_files)


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

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print(f"companion validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1

    print(
        f"companion validation passed: {len(markdown_files)} Markdown files, "
        f"{checked_links} local links, {len(gateways)} gateway asset(s), "
        f"{checked_checksums} checksum(s), "
        f"{checked_protocol_files} temporal-protocol file(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
