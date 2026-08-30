#!/usr/bin/env python3
"""Negative mutation tests for the Data packet temporal protocol validator."""

from __future__ import annotations

from pathlib import Path
import sys


SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import validate_repository as validator  # noqa: E402


PACKET = validator.ROOT / "testing/ai-ready-data-reader-value-v1"


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


def main() -> int:
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

    print(
        "temporal protocol mutation tests passed: baseline accepted; "
        "self-hash/later-record, same-path correction, and missing Phase 2 "
        "binding mutations rejected"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
