#!/usr/bin/env python3
"""Positive and negative subprocess tests for the synthetic exact-file helper."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SOURCE_HELPER = (
    ROOT
    / "testing/ai-ready-data-reader-value-v1/facilitator-only/07-synthetic-exact-file-access.py"
)
HELPER = "DATA-SYNTHETIC-EXACT-FILE-ACCESS-v1.py"
CONFIG = "DATA-SYNTHETIC-EXACT-FILE-ACCESS-CONFIG-v1.json"
MANIFEST = "DATA-SYNTHETIC-EXACT-FILE-ACCESS-SHA256SUMS-v1.txt"
ACCESS_LOG = "DATA-SYNTHETIC-EXACT-FILE-ACCESS-LOG-v1.jsonl"
PHASE_INPUT_MANIFEST = "DATA-PHASE-INPUT-SHA256SUMS-v1.txt"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def make_phase(
    root: Path,
    phase_id: str,
    actor: str,
    members: list[tuple[str, bytes, bool]],
    hash_overrides: dict[str, str] | None = None,
) -> Path:
    phase = root / phase_id
    inputs = phase / "input"
    inputs.mkdir(parents=True)
    shutil.copyfile(SOURCE_HELPER, phase / HELPER)
    ordered = []
    manifest_lines = []
    for filename, content, optional in members:
        target = inputs / filename
        target.write_bytes(content)
        observed_hash = sha256(target)
        manifest_lines.append(f"{observed_hash}  ./{filename}\n")
        ordered.append(
            {
                "filename": filename,
                "sha256": (hash_overrides or {}).get(filename, observed_hash),
                "optional": optional,
            }
        )
    phase_manifest = inputs / PHASE_INPUT_MANIFEST
    phase_manifest.write_text("".join(manifest_lines), encoding="utf-8")
    config = {
        "schema_version": 2,
        "packet_id": "DATA-RV-PILOT-001",
        "packet_version": "1.2.7",
        "attempt_id": "DATA-SYN-TEST-001",
        "actor_code": actor,
        "stage": "A" if actor.startswith("DATA-A") else "B",
        "phase_id": phase_id,
        "input_root": str(inputs.resolve()),
        "phase_input_manifest_filename": PHASE_INPUT_MANIFEST,
        "phase_input_manifest_path": str(phase_manifest.resolve()),
        "phase_input_manifest_sha256": sha256(phase_manifest),
        "ordered_files": ordered,
        "access_log": str((phase / ACCESS_LOG).resolve()),
        "binding_manifest_filename": MANIFEST,
        "timezone": "America/Denver",
        "helper_selected_before_event": "RUN_STARTED",
        "config_created_before_event": "CURRENT_PHASE_GATE_OPENED",
        "immutable_after_creation": True,
    }
    (phase / CONFIG).write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    (phase / MANIFEST).write_text(
        f"{sha256(phase / HELPER)}  ./{HELPER}\n"
        f"{sha256(phase / CONFIG)}  ./{CONFIG}\n",
        encoding="utf-8",
    )
    return phase


def refresh_config_binding(phase: Path) -> None:
    (phase / MANIFEST).write_text(
        f"{sha256(phase / HELPER)}  ./{HELPER}\n"
        f"{sha256(phase / CONFIG)}  ./{CONFIG}\n",
        encoding="utf-8",
    )


def invoke(phase: Path, option: str, value: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [
            sys.executable,
            str(phase / HELPER),
            "--config",
            str(phase / CONFIG),
            "--binding-manifest",
            str(phase / MANIFEST),
            "--audit-log",
            str(phase / ACCESS_LOG),
            option,
            value,
        ],
        cwd=phase,
        capture_output=True,
        check=False,
    )


def access_rows(phase: Path) -> list[dict]:
    path = phase / ACCESS_LOG
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_partial_write_all(root: Path) -> None:
    spec = importlib.util.spec_from_file_location(
        "synthetic_exact_file_helper", SOURCE_HELPER
    )
    if spec is None or spec.loader is None:
        raise AssertionError("could not load exact-file helper for write-all test")
    helper_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper_module)
    target = root / "partial-write-all.jsonl"
    expected = b'{"partial":"write-all"}\n'
    real_write = helper_module.os.write

    def partial_write(descriptor: int, value: memoryview) -> int:
        return real_write(descriptor, value[: min(3, len(value))])

    with (
        mock.patch.object(helper_module.os, "write", side_effect=partial_write),
        mock.patch.object(
            helper_module.os, "fsync", wraps=helper_module.os.fsync
        ) as fsync_call,
    ):
        helper_module.serialized_write_all_fsync(target, expected)
    require(
        target.read_bytes() == expected,
        "write-all loop lost bytes on partial write",
    )
    require(fsync_call.call_count == 1, "write-all path did not fsync exactly once")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="data-exact-file-helper-") as directory:
        root = Path(directory)
        require_partial_write_all(root)

        phase_one = make_phase(
            root,
            "stage-a-initial",
            "DATA-A-SYN-TEST",
            [
                ("first.md", b"exact first bytes\n", False),
                ("second.md", b"exact second bytes\n", False),
                ("optional.md", b"optional bytes\n", True),
            ],
        )
        wrong_order = invoke(phase_one, "--filename", "second.md")
        require(wrong_order.returncode == 2, "wrong-order request was not refused")
        first = invoke(phase_one, "--filename", "first.md")
        require(first.returncode == 0, "first exact-file request failed")
        require(first.stdout == b"exact first bytes\n", "helper changed emitted bytes")
        required_skip = invoke(phase_one, "--skip-optional", "second.md")
        require(required_skip.returncode == 2, "required-file skip was not refused")
        second = invoke(phase_one, "--filename", "second.md")
        require(second.returncode == 0, "second exact-file request failed")
        optional = invoke(phase_one, "--skip-optional", "optional.md")
        require(optional.returncode == 0, "declared optional skip failed")
        outcomes = [row["outcome"] for row in access_rows(phase_one)]
        require(
            outcomes
            == [
                "ACCESS_REFUSED",
                "ACCESS_GRANTED",
                "ACCESS_REFUSED",
                "ACCESS_GRANTED",
                "OPTIONAL_SKIPPED",
            ],
            f"unexpected phase-one access chronology: {outcomes}",
        )
        first_grant = access_rows(phase_one)[1]
        require(
            first_grant["phase_input_manifest_filename"] == PHASE_INPUT_MANIFEST
            and first_grant["phase_input_manifest_path"]
            == str((phase_one / "input" / PHASE_INPUT_MANIFEST).resolve())
            and first_grant["phase_input_manifest_sha256"]
            == sha256(phase_one / "input" / PHASE_INPUT_MANIFEST),
            "helper row omitted exact phase-input manifest filename/path/hash",
        )

        phase_two = make_phase(
            root,
            "stage-b-section-1",
            "DATA-B-SYN-TEST",
            [("handoff.md", b"phase two handoff\n", False)],
        )
        handoff = invoke(phase_two, "--filename", "handoff.md")
        require(handoff.returncode == 0, "distinct second-phase request failed")
        require(handoff.stdout == b"phase two handoff\n", "phase-two bytes changed")
        require(len(access_rows(phase_two)) == 1, "phase-two log was not distinct")
        require(len(access_rows(phase_one)) == 5, "phase-one log changed across phases")

        absent_manifest = make_phase(
            root,
            "absent-phase-manifest",
            "DATA-A-SYN-MISSING",
            [("input.md", b"missing manifest bytes\n", False)],
        )
        (absent_manifest / "input" / PHASE_INPUT_MANIFEST).unlink()
        require(
            invoke(absent_manifest, "--filename", "input.md").returncode == 2,
            "absent phase-input manifest was not refused",
        )

        drifted_manifest = make_phase(
            root,
            "drifted-phase-manifest",
            "DATA-A-SYN-MANIFEST-DRIFT",
            [("input.md", b"manifest drift bytes\n", False)],
        )
        with (drifted_manifest / "input" / PHASE_INPUT_MANIFEST).open(
            "a", encoding="utf-8"
        ) as stream:
            stream.write("\n")
        require(
            invoke(drifted_manifest, "--filename", "input.md").returncode == 2,
            "drifted phase-input manifest was not refused",
        )

        wrong_manifest = make_phase(
            root,
            "wrong-phase-manifest",
            "DATA-A-SYN-WRONG-MANIFEST",
            [("input.md", b"wrong manifest bytes\n", False)],
        )
        wrong_path = wrong_manifest / "WRONG-PHASE-INPUT-SHA256SUMS-v1.txt"
        shutil.copyfile(wrong_manifest / "input" / PHASE_INPUT_MANIFEST, wrong_path)
        config_path = wrong_manifest / CONFIG
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["phase_input_manifest_filename"] = wrong_path.name
        config["phase_input_manifest_path"] = str(wrong_path.resolve())
        config["phase_input_manifest_sha256"] = sha256(wrong_path)
        config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
        refresh_config_binding(wrong_manifest)
        require(
            invoke(wrong_manifest, "--filename", "input.md").returncode == 2,
            "phase-input manifest outside the sealed input was not refused",
        )

        membership_mismatch = make_phase(
            root,
            "manifest-membership-mismatch",
            "DATA-A-SYN-MEMBERS",
            [
                ("first.md", b"member one\n", False),
                ("second.md", b"member two\n", False),
            ],
        )
        config_path = membership_mismatch / CONFIG
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["ordered_files"].pop()
        config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
        refresh_config_binding(membership_mismatch)
        require(
            invoke(membership_mismatch, "--filename", "first.md").returncode == 2,
            "config/manifest membership mismatch was not refused",
        )

        duplicate_manifest = make_phase(
            root,
            "duplicate-manifest-member",
            "DATA-A-SYN-DUPLICATE",
            [("input.md", b"duplicate bytes\n", False)],
        )
        manifest_path = duplicate_manifest / "input" / PHASE_INPUT_MANIFEST
        line = manifest_path.read_text(encoding="utf-8")
        manifest_path.write_text(line + line, encoding="utf-8")
        config_path = duplicate_manifest / CONFIG
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["phase_input_manifest_sha256"] = sha256(manifest_path)
        config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
        refresh_config_binding(duplicate_manifest)
        require(
            invoke(duplicate_manifest, "--filename", "input.md").returncode == 2,
            "duplicate phase-manifest member was not refused",
        )

        malformed_manifest = make_phase(
            root,
            "malformed-phase-manifest",
            "DATA-A-SYN-MALFORMED",
            [("input.md", b"malformed bytes\n", False)],
        )
        manifest_path = malformed_manifest / "input" / PHASE_INPUT_MANIFEST
        manifest_path.write_text("not-a-checksum-line\n", encoding="utf-8")
        config_path = malformed_manifest / CONFIG
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["phase_input_manifest_sha256"] = sha256(manifest_path)
        config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
        refresh_config_binding(malformed_manifest)
        require(
            invoke(malformed_manifest, "--filename", "input.md").returncode == 2,
            "malformed phase-input manifest was not refused",
        )

        broad = make_phase(
            root,
            "path-request",
            "DATA-A-SYN-PATH",
            [("allowed.md", b"allowed\n", False)],
        )
        path_request = invoke(broad, "--filename", "../secret.md")
        require(path_request.returncode == 2, "path request was not refused")
        glob_request = invoke(broad, "--filename", "*.md")
        require(glob_request.returncode == 2, "glob request was not refused")
        require(
            [row["outcome"] for row in access_rows(broad)]
            == ["ACCESS_REFUSED", "ACCESS_REFUSED"],
            "path/glob refusals were not logged",
        )

        config_manifest_hash_mismatch = make_phase(
            root,
            "config-manifest-hash-mismatch",
            "DATA-A-SYN-HASH",
            [("input.md", b"real bytes\n", False)],
            {"input.md": "0" * 64},
        )
        hash_result = invoke(config_manifest_hash_mismatch, "--filename", "input.md")
        require(
            hash_result.returncode == 2,
            "config/phase-manifest member-hash mismatch was not refused",
        )
        require(
            access_rows(config_manifest_hash_mismatch)[0]["outcome"]
            == "ACCESS_REFUSED",
            "manifest-hash mismatch refusal not logged",
        )

        target_drift = make_phase(
            root,
            "target-drift",
            "DATA-A-SYN-TARGET-DRIFT",
            [("input.md", b"original target bytes\n", False)],
        )
        (target_drift / "input" / "input.md").write_bytes(b"changed target bytes\n")
        require(
            invoke(target_drift, "--filename", "input.md").returncode == 2,
            "target drift after manifest verification was not refused",
        )

        config_drift = make_phase(
            root,
            "config-drift",
            "DATA-A-SYN-CONFIG",
            [("input.md", b"config bytes\n", False)],
        )
        with (config_drift / CONFIG).open("a", encoding="utf-8") as stream:
            stream.write("\n")
        require(
            invoke(config_drift, "--filename", "input.md").returncode == 2,
            "config drift was not refused",
        )
        require(
            access_rows(config_drift)[0]["outcome"] == "ACCESS_REFUSED",
            "config-drift refusal was not logged",
        )

        helper_drift = make_phase(
            root,
            "helper-drift",
            "DATA-A-SYN-HELPER",
            [("input.md", b"helper bytes\n", False)],
        )
        with (helper_drift / HELPER).open("a", encoding="utf-8") as stream:
            stream.write("\n# drift\n")
        require(
            invoke(helper_drift, "--filename", "input.md").returncode == 2,
            "helper drift was not refused",
        )
        require(
            access_rows(helper_drift)[0]["outcome"] == "ACCESS_REFUSED",
            "helper-drift refusal was not logged",
        )

        config_after_gate = make_phase(
            root,
            "config-after-gate",
            "DATA-A-SYN-GATE",
            [("input.md", b"gate bytes\n", False)],
        )
        config_path = config_after_gate / CONFIG
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["config_created_before_event"] = "CURRENT_PHASE_GATE_CLOSED"
        config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
        (config_after_gate / MANIFEST).write_text(
            f"{sha256(config_after_gate / HELPER)}  ./{HELPER}\n"
            f"{sha256(config_path)}  ./{CONFIG}\n",
            encoding="utf-8",
        )
        require(
            invoke(config_after_gate, "--filename", "input.md").returncode == 2,
            "config-after-gate declaration was not refused",
        )
        require(
            access_rows(config_after_gate)[0]["outcome"] == "ACCESS_REFUSED",
            "config-after-gate refusal was not logged",
        )

        overbroad_config = make_phase(
            root,
            "overbroad-config",
            "DATA-A-SYN-BROAD",
            [("input.md", b"bounded bytes\n", False)],
        )
        config_path = overbroad_config / CONFIG
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["ordered_files"][0]["filename"] = "../secret.md"
        config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
        (overbroad_config / MANIFEST).write_text(
            f"{sha256(overbroad_config / HELPER)}  ./{HELPER}\n"
            f"{sha256(config_path)}  ./{CONFIG}\n",
            encoding="utf-8",
        )
        require(
            invoke(overbroad_config, "--filename", "../secret.md").returncode == 2,
            "overbroad config filename was not refused",
        )
        require(
            access_rows(overbroad_config)[0]["outcome"] == "ACCESS_REFUSED",
            "overbroad-config refusal was not logged",
        )

    print(
        "synthetic exact-file helper tests passed: partial write-all/fsync, exact "
        "bytes, and two-phase logs accepted; absent/drifted/wrong/duplicate/"
        "malformed phase manifests, "
        "config/manifest membership and hash mismatch, target drift, wrong "
        "order, path/glob, required skip, config drift, helper drift, config "
        "after gate, and overbroad config rejected"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
