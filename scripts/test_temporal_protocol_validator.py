#!/usr/bin/env python3
"""Negative mutation tests for the Data packet temporal protocol validator."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Callable


SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import validate_repository as validator  # noqa: E402


PACKET = validator.ROOT / "testing/ai-ready-data-reader-value-v1"
ROOT = validator.ROOT


def source(relative: str) -> str:
    return (PACKET / relative).read_text(encoding="utf-8")


def mutated_errors(relative: str, before: str, after: str) -> list[str]:
    original = source(relative)
    if before not in original:
        raise AssertionError(f"fixture anchor missing in {relative}: {before!r}")
    mutated = original.replace(before, after, 1)
    errors: list[str] = []
    validator.validate_temporal_freeze_protocol(errors, {relative: mutated})
    return errors


def assert_rejected(name: str, errors: list[str], expected: str) -> None:
    if not errors:
        raise AssertionError(f"{name}: mutation unexpectedly passed")
    if not any(expected in error for error in errors):
        raise AssertionError(
            f"{name}: mutation failed for the wrong reason; expected {expected!r}; "
            f"received {errors!r}"
        )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def protocol_path(repo: Path) -> Path:
    return repo / "testing/ai-ready-data-reader-value-v1/temporal-protocol.json"


def packet_manifest(repo: Path) -> Path:
    return protocol_path(repo).parent / "SHA256SUMS"


def refresh_packet_checksum(repo: Path, target: Path) -> None:
    manifest = packet_manifest(repo)
    relative = "./" + target.relative_to(manifest.parent).as_posix()
    replacement = f"{sha256(target)}  {relative}"
    lines = manifest.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.endswith(f"  {relative}"):
            lines[index] = replacement
            break
    else:
        raise AssertionError(f"packet manifest has no entry for {relative}")
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")


def load_protocol(repo: Path) -> dict:
    return json.loads(protocol_path(repo).read_text(encoding="utf-8"))


def write_protocol(repo: Path, protocol: dict) -> None:
    path = protocol_path(repo)
    path.write_text(json.dumps(protocol, indent=2) + "\n", encoding="utf-8")
    refresh_packet_checksum(repo, path)


def update_critical_document(
    repo: Path, relative: str, transform: Callable[[str], str]
) -> None:
    protocol = load_protocol(repo)
    target = protocol_path(repo).parent / relative
    original = target.read_text(encoding="utf-8")
    updated = transform(original)
    if updated == original:
        raise AssertionError(f"mutation did not change {relative}")
    target.write_text(updated, encoding="utf-8")
    refresh_packet_checksum(repo, target)
    for item in protocol["critical_documents"]:
        if item["path"] == relative:
            item["sha256"] = sha256(target)
            break
    else:
        raise AssertionError(f"critical document missing: {relative}")
    write_protocol(repo, protocol)


def copied_repo(temp_root: Path) -> Path:
    target = temp_root / "repo"
    shutil.copytree(
        ROOT,
        target,
        ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
    )
    return target


def run_validator(repo: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "scripts/validate_repository.py"],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )


def assert_repo_rejected(
    name: str, mutation: Callable[[Path], None], expected: str
) -> None:
    with tempfile.TemporaryDirectory(prefix=f"data-temporal-{name}-") as directory:
        repo = copied_repo(Path(directory))
        mutation(repo)
        result = run_validator(repo)
        output = result.stdout + result.stderr
        if result.returncode == 0:
            raise AssertionError(f"{name}: validator accepted forbidden mutation")
        if expected not in output:
            raise AssertionError(
                f"{name}: expected {expected!r} in validator output:\n{output}"
            )


def mutate_missing_verification_output(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["verification"]["required_observation_fields"].remove("complete_output")
    write_protocol(repo, protocol)


def mutate_missing_attempt_identity(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["detached_record"]["required_fields"].remove("attempt_id")
    write_protocol(repo, protocol)


def mutate_record_chronology(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["detached_record"]["record_completion_must_follow_verification"] = False
    write_protocol(repo, protocol)


def mutate_orchestration_permission(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["participant_input_policy"]["undeclared_orchestration_forbidden"] = False
    write_protocol(repo, protocol)


def mutate_missing_execution_event(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["execution_access_log"]["required_event_sequence"].remove(
        "GOVERNING_MANIFEST_VERIFIED"
    )
    write_protocol(repo, protocol)


def mutate_missing_execution_actor(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["execution_access_log"]["required_row_fields"].remove("actor")
    write_protocol(repo, protocol)


def mutate_record_template_omission(repo: Path) -> None:
    update_critical_document(
        repo,
        "participant/06-revised-artifact-freeze-record.md",
        lambda content: content.replace("- Complete observed command output:\n", "", 1),
    )


def main() -> int:
    positive = run_validator(ROOT)
    if positive.returncode != 0:
        sys.stderr.write(positive.stdout + positive.stderr)
        raise AssertionError("positive control: clean repository did not validate")

    baseline: list[str] = []
    validator.validate_temporal_freeze_protocol(baseline)
    if baseline:
        raise AssertionError(f"baseline temporal protocol failed: {baseline!r}")

    self_hash_errors = mutated_errors(
        "facilitator-only/01-facilitator-guide.md",
        "The manifest never lists or hashes itself or the later record.",
        "The manifest lists and hashes itself and the later record.",
    )
    assert_rejected(
        "self-hash and later-record inclusion",
        self_hash_errors,
        "lacks required semantic invariant",
    )

    correction_errors = mutated_errors(
        "participant/06-revised-artifact-freeze-record.md",
        "new immutable replacement set with a new immutable filename and a new artifact\n"
        "ID/version for every corrected artifact",
        "new immutable replacement set with new IDs/versions or filenames",
    )
    assert_rejected(
        "same-path-or correction language",
        correction_errors,
        "correction permits same-path",
    )

    release_errors = mutated_errors(
        "facilitator-only/03-results-and-deviation-log.md",
        "Stage B Phase 2 input / |\n| Stage A handoff",
        "|\n| Stage A handoff",
    )
    assert_rejected(
        "missing revised-set Phase 2 release binding",
        release_errors,
        "Stage A revised set",
    )

    repo_cases = [
        (
            "missing-verification-output",
            mutate_missing_verification_output,
            "verification must capture command, complete output",
        ),
        (
            "missing-attempt-identity",
            mutate_missing_attempt_identity,
            "detached record fields omit replay identity or evidence",
        ),
        (
            "record-chronology",
            mutate_record_chronology,
            "record completion must follow verification",
        ),
        (
            "orchestration-permission",
            mutate_orchestration_permission,
            "undeclared orchestration is not forbidden",
        ),
        (
            "missing-execution-event",
            mutate_missing_execution_event,
            "execution event sequence invalid",
        ),
        (
            "missing-execution-actor",
            mutate_missing_execution_actor,
            "execution log row fields incomplete",
        ),
        (
            "record-template-omission",
            mutate_record_template_omission,
            "lacks required semantic invariant: - Complete observed command output:",
        ),
    ]
    for name, mutation, expected in repo_cases:
        assert_repo_rejected(name, mutation, expected)

    print(
        "temporal protocol mutation tests passed: full positive control and "
        "semantic baseline accepted; 10 adversarial omissions or permissions rejected"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
