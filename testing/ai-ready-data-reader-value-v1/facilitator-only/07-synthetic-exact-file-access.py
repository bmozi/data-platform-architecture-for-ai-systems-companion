#!/usr/bin/env python3
"""Read one exact sealed synthetic input through a checksum-bound phase gate."""

from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


PACKET_ID = "DATA-RV-PILOT-001"
PACKET_VERSION = "1.2.8"
SCHEMA_VERSION = 2
RUN_HELPER_FILENAME = "DATA-SYNTHETIC-EXACT-FILE-ACCESS-v1.py"
RUN_CONFIG_FILENAME = "DATA-SYNTHETIC-EXACT-FILE-ACCESS-CONFIG-v1.json"
RUN_BINDING_MANIFEST = "DATA-SYNTHETIC-EXACT-FILE-ACCESS-SHA256SUMS-v1.txt"
RUN_ACCESS_LOG = "DATA-SYNTHETIC-EXACT-FILE-ACCESS-LOG-v1.jsonl"
HASH_LINE = re.compile(r"^([0-9a-f]{64})  \./([^/]+)$")
CONFIG_KEYS = {
    "schema_version",
    "packet_id",
    "packet_version",
    "attempt_id",
    "actor_code",
    "stage",
    "phase_id",
    "input_root",
    "phase_input_manifest_filename",
    "phase_input_manifest_path",
    "phase_input_manifest_sha256",
    "ordered_files",
    "access_log",
    "binding_manifest_filename",
    "timezone",
    "helper_selected_before_event",
    "config_created_before_event",
    "immutable_after_creation",
}
FILE_KEYS = {"filename", "sha256", "optional"}


class BoundaryError(RuntimeError):
    """A request crossed the declared exact-file boundary."""


class LoggedBoundaryError(BoundaryError):
    """A refused request already has an append-only helper-log row."""


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def resolved_outside(root: Path, candidate: Path) -> bool:
    try:
        candidate.relative_to(root)
    except ValueError:
        return True
    return False


def parse_manifest_bytes(value: bytes) -> dict[str, str]:
    entries: dict[str, str] = {}
    try:
        lines = value.decode("utf-8").splitlines()
    except UnicodeDecodeError as exc:
        raise BoundaryError("checksum manifest is not UTF-8") from exc
    for line in lines:
        match = HASH_LINE.fullmatch(line)
        if not match or match.group(2) in entries:
            raise BoundaryError("checksum manifest is malformed or has duplicate members")
        entries[match.group(2)] = match.group(1)
    return entries


def parse_manifest(path: Path) -> dict[str, str]:
    return parse_manifest_bytes(path.read_bytes())


def load_config(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or set(value) != CONFIG_KEYS:
        raise BoundaryError("config keys differ from the exact schema")
    if value["schema_version"] != SCHEMA_VERSION:
        raise BoundaryError("config schema version mismatch")
    if value["packet_id"] != PACKET_ID or value["packet_version"] != PACKET_VERSION:
        raise BoundaryError("packet identity mismatch")
    if value["stage"] not in ["A", "B"]:
        raise BoundaryError("stage must be A or B")
    for field in ["attempt_id", "actor_code", "phase_id", "timezone"]:
        if not isinstance(value[field], str) or not value[field]:
            raise BoundaryError(f"config field {field} is blank")
    try:
        ZoneInfo(value["timezone"])
    except ZoneInfoNotFoundError as exc:
        raise BoundaryError("config timezone is invalid") from exc
    if value["helper_selected_before_event"] != "RUN_STARTED":
        raise BoundaryError("helper was not selected before RUN_STARTED")
    if value["config_created_before_event"] != "CURRENT_PHASE_GATE_OPENED":
        raise BoundaryError("config was not created before the current phase gate")
    if value["immutable_after_creation"] is not True:
        raise BoundaryError("helper config is not immutable")
    if value["binding_manifest_filename"] != RUN_BINDING_MANIFEST:
        raise BoundaryError("binding manifest identity mismatch")
    phase_manifest_filename = value["phase_input_manifest_filename"]
    if (
        not isinstance(phase_manifest_filename, str)
        or not phase_manifest_filename
        or Path(phase_manifest_filename).name != phase_manifest_filename
        or "/" in phase_manifest_filename
        or "\\" in phase_manifest_filename
    ):
        raise BoundaryError("phase-input manifest filename is not one flat identity")
    phase_manifest_path = value["phase_input_manifest_path"]
    if not isinstance(phase_manifest_path, str) or not Path(
        phase_manifest_path
    ).is_absolute():
        raise BoundaryError("phase-input manifest path must be absolute")
    if Path(phase_manifest_path) != Path(phase_manifest_path).resolve():
        raise BoundaryError("phase-input manifest path must be canonical")
    if Path(phase_manifest_path).name != phase_manifest_filename:
        raise BoundaryError("phase-input manifest path/filename identity mismatch")
    if not isinstance(value["phase_input_manifest_sha256"], str) or not re.fullmatch(
        r"[0-9a-f]{64}", value["phase_input_manifest_sha256"]
    ):
        raise BoundaryError("phase-input manifest SHA-256 is invalid")
    ordered = value["ordered_files"]
    if not isinstance(ordered, list) or not ordered:
        raise BoundaryError("ordered_files must be a non-empty list")
    names: list[str] = []
    for item in ordered:
        if not isinstance(item, dict) or set(item) != FILE_KEYS:
            raise BoundaryError("ordered file entry differs from the exact schema")
        filename = item["filename"]
        if (
            not isinstance(filename, str)
            or not filename
            or Path(filename).name != filename
            or "/" in filename
            or "\\" in filename
        ):
            raise BoundaryError("ordered filename is not one literal flat filename")
        if not isinstance(item["sha256"], str) or not re.fullmatch(
            r"[0-9a-f]{64}", item["sha256"]
        ):
            raise BoundaryError("ordered file SHA-256 is invalid")
        if not isinstance(item["optional"], bool):
            raise BoundaryError("ordered file optional flag is not Boolean")
        names.append(filename)
    if len(names) != len(set(names)):
        raise BoundaryError("ordered filenames are not unique")
    return value


def validate_boundary(
    config_path: Path, manifest_path: Path, audit_log_path: Path
) -> tuple[dict, str, str]:
    helper_path = Path(__file__).resolve()
    config_path = config_path.resolve()
    manifest_path = manifest_path.resolve()
    audit_log_path = audit_log_path.resolve()
    if helper_path.name != RUN_HELPER_FILENAME:
        raise BoundaryError("helper was not copied under its exact run filename")
    if config_path.name != RUN_CONFIG_FILENAME:
        raise BoundaryError("config filename mismatch")
    if manifest_path.name != RUN_BINDING_MANIFEST:
        raise BoundaryError("binding manifest filename mismatch")
    if not (
        helper_path.parent
        == config_path.parent
        == manifest_path.parent
        == audit_log_path.parent
    ):
        raise BoundaryError(
            "helper, config, binding manifest, and audit log are not co-located"
        )
    if audit_log_path.name != RUN_ACCESS_LOG:
        raise BoundaryError("audit-log filename mismatch")

    config = load_config(config_path)
    entries = parse_manifest(manifest_path)
    expected_members = {helper_path.name, config_path.name}
    if set(entries) != expected_members:
        raise BoundaryError("binding manifest must contain exactly helper and config")
    if entries[helper_path.name] != sha256(helper_path):
        raise BoundaryError("helper hash differs from binding manifest")
    if entries[config_path.name] != sha256(config_path):
        raise BoundaryError("config hash differs from binding manifest")

    input_root = Path(config["input_root"])
    access_log = Path(config["access_log"])
    if not input_root.is_absolute() or not input_root.is_dir():
        raise BoundaryError("input_root must be an existing absolute directory")
    if not access_log.is_absolute() or access_log.name != RUN_ACCESS_LOG:
        raise BoundaryError("access_log must use the exact absolute filename")
    if access_log.resolve() != audit_log_path:
        raise BoundaryError("config access_log differs from the fixed audit-log argument")
    input_root = input_root.resolve()
    phase_input_manifest = Path(config["phase_input_manifest_path"]).resolve()
    if phase_input_manifest.parent != input_root:
        raise BoundaryError("phase-input manifest is outside the sealed input root")
    if not phase_input_manifest.is_file():
        raise BoundaryError("phase-input manifest is absent")
    phase_manifest_bytes = phase_input_manifest.read_bytes()
    if sha256_bytes(phase_manifest_bytes) != config["phase_input_manifest_sha256"]:
        raise BoundaryError("phase-input manifest hash differs from the config")
    phase_entries = parse_manifest_bytes(phase_manifest_bytes)
    if config["phase_input_manifest_filename"] in phase_entries:
        raise BoundaryError("phase-input manifest lists itself")
    ordered_entries = {
        item["filename"]: item["sha256"] for item in config["ordered_files"]
    }
    if phase_entries != ordered_entries:
        raise BoundaryError(
            "config ordered_files membership/hashes differ from the phase-input manifest"
        )
    access_parent = access_log.parent.resolve()
    if not resolved_outside(input_root, access_parent):
        raise BoundaryError("access log must remain outside participant input")
    return config, sha256(config_path), sha256(manifest_path)


def load_access_rows(path: Path, config: dict, config_hash: str, binding_hash: str) -> list[dict]:
    if not path.exists():
        return []
    rows: list[dict] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise BoundaryError(f"access log row {number} is invalid JSON") from exc
        if row.get("event_id") != f"ACCESS-{number:06d}":
            raise BoundaryError("access log continuity is invalid")
        if row.get("attempt_id") != config["attempt_id"]:
            raise BoundaryError("access log attempt identity mismatch")
        if row.get("actor_code") != config["actor_code"]:
            raise BoundaryError("access log actor identity mismatch")
        if row.get("stage") != config["stage"] or row.get("phase_id") != config["phase_id"]:
            raise BoundaryError("access log stage or phase identity mismatch")
        if row.get("config_sha256") != config_hash:
            raise BoundaryError("access log config binding mismatch")
        if row.get("binding_manifest_sha256") != binding_hash:
            raise BoundaryError("access log manifest binding mismatch")
        if row.get("phase_input_manifest_filename") != config[
            "phase_input_manifest_filename"
        ]:
            raise BoundaryError("access log phase-input manifest filename mismatch")
        if row.get("phase_input_manifest_path") != config["phase_input_manifest_path"]:
            raise BoundaryError("access log phase-input manifest path mismatch")
        if row.get("phase_input_manifest_sha256") != config[
            "phase_input_manifest_sha256"
        ]:
            raise BoundaryError("access log phase-input manifest hash mismatch")
        rows.append(row)
    return rows


def append_access(
    path: Path,
    rows: list[dict],
    config: dict,
    config_hash: str,
    binding_hash: str,
    action: str,
    filename: str,
    outcome: str,
    detail: str,
) -> None:
    now = datetime.now(ZoneInfo(config["timezone"])).isoformat(timespec="seconds")
    row = {
        "event_id": f"ACCESS-{len(rows) + 1:06d}",
        "attempt_id": config["attempt_id"],
        "actor_code": config["actor_code"],
        "stage": config["stage"],
        "phase_id": config["phase_id"],
        "action": action,
        "filename": filename,
        "outcome": outcome,
        "detail": detail,
        "timestamp": now,
        "timezone": config["timezone"],
        "config_sha256": config_hash,
        "binding_manifest_sha256": binding_hash,
        "phase_input_manifest_filename": config["phase_input_manifest_filename"],
        "phase_input_manifest_path": config["phase_input_manifest_path"],
        "phase_input_manifest_sha256": config["phase_input_manifest_sha256"],
    }
    if not path.parent.is_dir():
        raise BoundaryError("predeclared access-log directory does not exist")
    encoded = (json.dumps(row, separators=(",", ":")) + "\n").encode("utf-8")
    serialized_write_all_fsync(path, encoded)


def serialized_write_all_fsync(path: Path, encoded: bytes) -> None:
    """Append every byte and fsync; callers must serialize helper invocations."""

    descriptor = os.open(path, os.O_APPEND | os.O_CREAT | os.O_WRONLY, 0o600)
    try:
        view = memoryview(encoded)
        while view:
            written = os.write(descriptor, view)
            if written <= 0:
                raise OSError("append write made no progress")
            view = view[written:]
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def append_preboundary_refusal(
    audit_log: Path,
    config_path: Path,
    manifest_path: Path,
    action: str,
    filename: str,
    detail: str,
) -> None:
    """Retain a refusal even when helper/config binding cannot be trusted."""

    audit_log = audit_log.resolve()
    helper_path = Path(__file__).resolve()
    if audit_log.name != RUN_ACCESS_LOG or audit_log.parent != helper_path.parent:
        raise BoundaryError("fixed audit-log path is outside the helper directory")
    raw_config: dict = {}
    try:
        loaded = json.loads(config_path.read_text(encoding="utf-8"))
        if isinstance(loaded, dict):
            raw_config = loaded
    except (OSError, json.JSONDecodeError):
        pass
    timezone = raw_config.get("timezone")
    try:
        now = datetime.now(ZoneInfo(timezone)).isoformat(timespec="seconds")
    except (TypeError, ValueError, ZoneInfoNotFoundError):
        now = datetime.now().astimezone().isoformat(timespec="seconds")
        timezone = str(datetime.now().astimezone().tzinfo)
    existing = (
        audit_log.read_text(encoding="utf-8").splitlines()
        if audit_log.exists()
        else []
    )

    def observed_hash(path: Path) -> str:
        try:
            return sha256(path)
        except OSError:
            return "UNAVAILABLE"

    row = {
        "event_id": f"ACCESS-{len(existing) + 1:06d}",
        "attempt_id": raw_config.get("attempt_id", "UNVERIFIED"),
        "actor_code": raw_config.get("actor_code", "UNVERIFIED"),
        "stage": raw_config.get("stage", "UNVERIFIED"),
        "phase_id": raw_config.get("phase_id", "UNVERIFIED"),
        "action": action,
        "filename": filename,
        "outcome": "ACCESS_REFUSED",
        "detail": f"preboundary refusal: {detail}",
        "timestamp": now,
        "timezone": timezone,
        "config_sha256": observed_hash(config_path),
        "binding_manifest_sha256": observed_hash(manifest_path),
        "phase_input_manifest_filename": raw_config.get(
            "phase_input_manifest_filename", "UNVERIFIED"
        ),
        "phase_input_manifest_path": raw_config.get(
            "phase_input_manifest_path", "UNVERIFIED"
        ),
        "phase_input_manifest_sha256": raw_config.get(
            "phase_input_manifest_sha256", "UNVERIFIED"
        ),
    }
    if not audit_log.parent.is_dir():
        raise BoundaryError("predeclared audit-log directory does not exist")
    encoded = (json.dumps(row, separators=(",", ":")) + "\n").encode("utf-8")
    serialized_write_all_fsync(audit_log, encoded)


def completed_filenames(rows: list[dict]) -> list[str]:
    return [
        row["filename"]
        for row in rows
        if row.get("outcome") in ["ACCESS_GRANTED", "OPTIONAL_SKIPPED"]
    ]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Open one checksum-bound file in the declared phase order."
    )
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--binding-manifest", required=True, type=Path)
    parser.add_argument("--audit-log", required=True, type=Path)
    request = parser.add_mutually_exclusive_group(required=True)
    request.add_argument("--filename")
    request.add_argument("--skip-optional")
    args = parser.parse_args()

    try:
        config, config_hash, binding_hash = validate_boundary(
            args.config, args.binding_manifest, args.audit_log
        )
        access_log = Path(config["access_log"])
        rows = load_access_rows(access_log, config, config_hash, binding_hash)
        completed = completed_filenames(rows)
        ordered = config["ordered_files"]
        expected_prefix = [item["filename"] for item in ordered[: len(completed)]]
        if completed != expected_prefix:
            raise BoundaryError("access log does not match the declared read order")
        requested = args.filename or args.skip_optional
        if len(completed) >= len(ordered):
            append_access(
                access_log,
                rows,
                config,
                config_hash,
                binding_hash,
                "READ" if args.filename else "SKIP_OPTIONAL",
                requested,
                "ACCESS_REFUSED",
                "phase allowlist already exhausted",
            )
            raise LoggedBoundaryError("phase allowlist already exhausted")

        expected = ordered[len(completed)]
        action = "READ" if args.filename else "SKIP_OPTIONAL"
        if requested != expected["filename"]:
            append_access(
                access_log,
                rows,
                config,
                config_hash,
                binding_hash,
                action,
                requested,
                "ACCESS_REFUSED",
                f"expected next filename {expected['filename']}",
            )
            raise LoggedBoundaryError(f"expected next filename {expected['filename']}")
        if args.skip_optional:
            if expected["optional"] is not True:
                append_access(
                    access_log,
                    rows,
                    config,
                    config_hash,
                    binding_hash,
                    action,
                    requested,
                    "ACCESS_REFUSED",
                    "required file cannot be skipped",
                )
                raise LoggedBoundaryError("required file cannot be skipped")
            append_access(
                access_log,
                rows,
                config,
                config_hash,
                binding_hash,
                action,
                requested,
                "OPTIONAL_SKIPPED",
                "actor declined the optional file at its declared position",
            )
            return 0

        if Path(requested).name != requested or "/" in requested or "\\" in requested:
            append_access(
                access_log,
                rows,
                config,
                config_hash,
                binding_hash,
                action,
                requested,
                "ACCESS_REFUSED",
                "request was not one literal flat filename",
            )
            raise LoggedBoundaryError("request was not one literal flat filename")
        target = (Path(config["input_root"]) / requested).resolve()
        input_root = Path(config["input_root"]).resolve()
        if target.parent != input_root or not target.is_file():
            append_access(
                access_log,
                rows,
                config,
                config_hash,
                binding_hash,
                action,
                requested,
                "ACCESS_REFUSED",
                "target is absent or outside the flat sealed input",
            )
            raise LoggedBoundaryError("target is absent or outside the flat sealed input")
        content = target.read_bytes()
        if sha256_bytes(content) != expected["sha256"]:
            append_access(
                access_log,
                rows,
                config,
                config_hash,
                binding_hash,
                action,
                requested,
                "ACCESS_REFUSED",
                "target SHA-256 differs from the immutable config",
            )
            raise LoggedBoundaryError("target SHA-256 differs from the immutable config")
        append_access(
            access_log,
            rows,
            config,
            config_hash,
            binding_hash,
            action,
            requested,
            "ACCESS_GRANTED",
            "exact bytes emitted after allowlist, order, path, and hash checks",
        )
        sys.stdout.buffer.write(content)
        return 0
    except (BoundaryError, OSError, json.JSONDecodeError) as exc:
        if not isinstance(exc, LoggedBoundaryError):
            requested = args.filename or args.skip_optional
            try:
                append_preboundary_refusal(
                    args.audit_log,
                    args.config,
                    args.binding_manifest,
                    "READ" if args.filename else "SKIP_OPTIONAL",
                    requested,
                    str(exc),
                )
            except (BoundaryError, OSError, json.JSONDecodeError) as log_exc:
                print(f"REFUSAL LOG FAILED: {log_exc}", file=sys.stderr)
        print(f"ACCESS REFUSED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
