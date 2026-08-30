#!/usr/bin/env python3
"""Positive and negative subprocess tests for the synthetic exact-file helper."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SOURCE_HELPER = (
    ROOT
    / "testing/ai-ready-data-reader-value-v1/facilitator-only/07-synthetic-exact-file-access.py"
)
HELPER = "DATA-SYNTHETIC-EXACT-FILE-ACCESS-v1.py"
CONFIG = "DATA-SYNTHETIC-EXACT-FILE-ACCESS-CONFIG-v1.json"
MANIFEST = "DATA-SYNTHETIC-EXACT-FILE-ACCESS-SHA256SUMS-v1.txt"
ACCESS_LOG = "DATA-SYNTHETIC-EXACT-FILE-ACCESS-LOG-v1.jsonl"


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
    for filename, content, optional in members:
        target = inputs / filename
        target.write_bytes(content)
        ordered.append(
            {
                "filename": filename,
                "sha256": (hash_overrides or {}).get(filename, sha256(target)),
                "optional": optional,
            }
        )
    config = {
        "schema_version": 1,
        "packet_id": "DATA-RV-PILOT-001",
        "packet_version": "1.2.6",
        "attempt_id": "DATA-SYN-TEST-001",
        "actor_code": actor,
        "stage": "A" if actor.startswith("DATA-A") else "B",
        "phase_id": phase_id,
        "input_root": str(inputs.resolve()),
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


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="data-exact-file-helper-") as directory:
        root = Path(directory)

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

        wrong_hash = make_phase(
            root,
            "wrong-hash",
            "DATA-A-SYN-HASH",
            [("input.md", b"real bytes\n", False)],
            {"input.md": "0" * 64},
        )
        hash_result = invoke(wrong_hash, "--filename", "input.md")
        require(hash_result.returncode == 2, "target hash drift was not refused")
        require(access_rows(wrong_hash)[0]["outcome"] == "ACCESS_REFUSED", "hash refusal not logged")

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
        "synthetic exact-file helper tests passed: exact bytes and two-phase "
        "logs accepted; wrong order, path/glob, hash, required skip, config "
        "drift, helper drift, config after gate, and overbroad config rejected"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
