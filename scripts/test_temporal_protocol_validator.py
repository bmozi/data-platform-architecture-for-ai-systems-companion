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


def mutate_live_update_member_omission(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["revision_phase_input"]["required_members"].remove(
        "DATA-A-LIVE-UPDATE-v1.md"
    )
    write_protocol(repo, protocol)


def mutate_live_update_rename(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["revision_phase_input"]["immutable_participant_input"][
        "filename"
    ] = "DATA-A-LIVE-UPDATE-renamed-v1.md"
    write_protocol(repo, protocol)


def mutate_live_update_unbound(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["revision_phase_input"]["opens_release"] = "stage_a_handoff"
    write_protocol(repo, protocol)


def mutate_route_live_update_omission(repo: Path) -> None:
    update_critical_document(
        repo,
        "participant/00-packet-route.md",
        lambda content: content.replace(
            "`DATA-A-LIVE-UPDATE-v1.md`", "the live-update file"
        ),
    )


def mutate_live_update_wording_drift(repo: Path) -> None:
    protocol = load_protocol(repo)
    relative = protocol["revision_phase_input"]["immutable_participant_input"][
        "path"
    ]
    packet_dir = protocol_path(repo).parent
    target = packet_dir / relative
    original = target.read_text(encoding="utf-8")
    updated = original.replace("Policy v2 above v3", "Policy v3 above v2", 1)
    if updated == original:
        raise AssertionError("live-update wording mutation did not change input")
    target.write_text(updated, encoding="utf-8")
    refresh_packet_checksum(repo, target)
    updated_hash = sha256(target)
    protocol["revision_phase_input"]["immutable_participant_input"][
        "sha256"
    ] = updated_hash
    for item in protocol["critical_documents"]:
        if item["path"] == relative:
            item["sha256"] = updated_hash
            break
    else:
        raise AssertionError("live-update critical document not found")
    write_protocol(repo, protocol)


def mutate_optional_branch_weakening(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["revision_phase_input"]["conditional_members"][0][
        "required_when_prior_release_artifact_included"
    ] = False
    write_protocol(repo, protocol)


def mutate_entry_branch_omission(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol.pop("entry_branch")
    write_protocol(repo, protocol)


def mutate_branch_mixing(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["entry_branch"]["mixed_branch_forbidden"] = False
    write_protocol(repo, protocol)


def mutate_synthetic_human_consent_claim(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["entry_branch"]["synthetic"]["human_consent_claim_forbidden"] = False
    write_protocol(repo, protocol)


def mutate_synthetic_human_result_claim(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["entry_branch"]["synthetic"]["human_result_claim_forbidden"] = False
    write_protocol(repo, protocol)


def remove_route_boundary(event: str) -> Callable[[Path], None]:
    def mutation(repo: Path) -> None:
        protocol = load_protocol(repo)
        protocol["route_closure"]["required_boundary_sequence"].remove(event)
        write_protocol(repo, protocol)

    return mutation


def mutate_debrief_gate_omission(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["route_closure"].pop("debrief_phase_input")
    write_protocol(repo, protocol)


def mutate_debrief_unverified(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["route_closure"]["debrief_phase_input"][
        "verified_before_open"
    ] = False
    write_protocol(repo, protocol)


def mutate_results_omission(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol.pop("run_results")
    write_protocol(repo, protocol)


def mutate_premature_log_close(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["run_results"]["completed_before_log_close"] = False
    write_protocol(repo, protocol)


def mutate_predicted_future_log_hash(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["run_results"]["predicted_final_closed_log_hash_forbidden"] = False
    write_protocol(repo, protocol)


def mutate_missing_closeout(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol.pop("external_closeout")
    write_protocol(repo, protocol)


def mutate_favorable_layout_without_proof(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["handoff_layout_proof"]["favorable_claim_requires_passed_proof"] = False
    write_protocol(repo, protocol)


def mutate_future_stage_end_in_scored_workbook(repo: Path) -> None:
    update_critical_document(
        repo,
        "participant/03-practitioner-workbook.md",
        lambda content: content
        + "\n- Required future route fact: `STAGE_A_ENDED`\n",
    )


def mutate_synthetic_helper_absent(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol.pop("synthetic_exact_file_access")
    write_protocol(repo, protocol)


def mutate_synthetic_helper_after_start(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["synthetic_exact_file_access"]["helper_selected_before_event"] = (
        "STAGE_A_STARTED"
    )
    write_protocol(repo, protocol)


def mutate_synthetic_helper_overbroad(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["synthetic_exact_file_access"][
        "helper_grants_general_terminal_or_shell"
    ] = True
    write_protocol(repo, protocol)


def mutate_ad_hoc_message_delivery(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["synthetic_exact_file_access"][
        "ad_hoc_message_delivery_allowed"
    ] = True
    write_protocol(repo, protocol)


def mutate_future_or_dummy_hashes(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["synthetic_exact_file_access"][
        "future_or_dummy_hashes_forbidden"
    ] = False
    write_protocol(repo, protocol)


def mutate_config_after_phase_gate(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["synthetic_exact_file_access"]["config_created_before_event"] = (
        "CURRENT_PHASE_GATE_CLOSED"
    )
    write_protocol(repo, protocol)


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
        (
            "live-update-member-omission",
            mutate_live_update_member_omission,
            "revision input omits or changes required manifest members",
        ),
        (
            "live-update-rename",
            mutate_live_update_rename,
            "immutable live-update filename must be DATA-A-LIVE-UPDATE-v1.md",
        ),
        (
            "live-update-unbound",
            mutate_live_update_unbound,
            "revision phase input must open stage_a_revised",
        ),
        (
            "route-live-update-omission",
            mutate_route_live_update_omission,
            "participant/00-packet-route.md lacks exact identity: DATA-A-LIVE-UPDATE-v1.md",
        ),
        (
            "live-update-wording-drift",
            mutate_live_update_wording_drift,
            "immutable live-update input differs from canonical facilitator wording",
        ),
        (
            "optional-branch-weakening",
            mutate_optional_branch_weakening,
            "optional initial contract membership semantics weakened",
        ),
        (
            "entry-branch-omission",
            mutate_entry_branch_omission,
            "entry branch must preserve exact mutually exclusive",
        ),
        (
            "entry-branch-mixing",
            mutate_branch_mixing,
            "entry branch must preserve exact mutually exclusive",
        ),
        (
            "synthetic-human-consent-claim",
            mutate_synthetic_human_consent_claim,
            "entry branch must preserve exact mutually exclusive",
        ),
        (
            "synthetic-human-result-claim",
            mutate_synthetic_human_result_claim,
            "entry branch must preserve exact mutually exclusive",
        ),
        (
            "missing-stage-a-start",
            remove_route_boundary("STAGE_A_STARTED"),
            "full-route closure boundaries",
        ),
        (
            "missing-stage-a-context-gate",
            remove_route_boundary("STAGE_A_CONTEXT_GATE_OPENED"),
            "full-route closure boundaries",
        ),
        (
            "missing-layout-proof-boundary",
            remove_route_boundary("HANDOFF_LAYOUT_PROOF_COMPLETED"),
            "full-route closure boundaries",
        ),
        (
            "missing-stage-a-material-feedback",
            remove_route_boundary("STAGE_A_MATERIAL_FEEDBACK_COMPLETED"),
            "full-route closure boundaries",
        ),
        (
            "missing-stage-a-end",
            remove_route_boundary("STAGE_A_ENDED"),
            "full-route closure boundaries",
        ),
        (
            "missing-stage-b-start",
            remove_route_boundary("STAGE_B_STARTED"),
            "full-route closure boundaries",
        ),
        (
            "missing-stage-b-context-gate",
            remove_route_boundary("STAGE_B_CONTEXT_GATE_OPENED"),
            "full-route closure boundaries",
        ),
        (
            "missing-stage-b-scoring-end",
            remove_route_boundary("STAGE_B_SCORING_ENDED"),
            "full-route closure boundaries",
        ),
        (
            "missing-section-6-completion",
            remove_route_boundary("STAGE_B_SECTION_6_DEBRIEF_COMPLETED"),
            "full-route closure boundaries",
        ),
        (
            "missing-section-6-open",
            remove_route_boundary("STAGE_B_SECTION_6_DEBRIEF_OPENED"),
            "full-route closure boundaries",
        ),
        (
            "missing-stage-b-end",
            remove_route_boundary("STAGE_B_ENDED"),
            "full-route closure boundaries",
        ),
        (
            "missing-run-results-boundary",
            remove_route_boundary("RUN_RESULTS_COMPLETED"),
            "full-route closure boundaries",
        ),
        (
            "debrief-gate-omission",
            mutate_debrief_gate_omission,
            "full-route closure boundaries",
        ),
        (
            "debrief-unverified",
            mutate_debrief_unverified,
            "full-route closure boundaries",
        ),
        (
            "run-results-omission",
            mutate_results_omission,
            "immutable run-results identity",
        ),
        (
            "premature-log-close",
            mutate_premature_log_close,
            "immutable run-results identity",
        ),
        (
            "predicted-future-log-hash",
            mutate_predicted_future_log_hash,
            "immutable run-results identity",
        ),
        (
            "missing-external-closeout",
            mutate_missing_closeout,
            "later external closeout identity",
        ),
        (
            "favorable-layout-without-proof",
            mutate_favorable_layout_without_proof,
            "one-page US Letter handoff proof contract",
        ),
        (
            "future-stage-end-in-scored-workbook",
            mutate_future_stage_end_in_scored_workbook,
            "requires future stage-end fact inside governed/scored source",
        ),
        (
            "synthetic-helper-absent",
            mutate_synthetic_helper_absent,
            "synthetic exact-file access must preserve",
        ),
        (
            "synthetic-helper-after-start",
            mutate_synthetic_helper_after_start,
            "synthetic exact-file access must preserve",
        ),
        (
            "synthetic-helper-overbroad",
            mutate_synthetic_helper_overbroad,
            "synthetic exact-file access must preserve",
        ),
        (
            "ad-hoc-message-delivery",
            mutate_ad_hoc_message_delivery,
            "synthetic exact-file access must preserve",
        ),
        (
            "future-or-dummy-config-hashes",
            mutate_future_or_dummy_hashes,
            "synthetic exact-file access must preserve",
        ),
        (
            "config-after-phase-gate",
            mutate_config_after_phase_gate,
            "synthetic exact-file access must preserve",
        ),
    ]
    for name, mutation, expected in repo_cases:
        assert_repo_rejected(name, mutation, expected)

    print(
        "temporal protocol mutation tests passed: full positive control and "
        "semantic baseline accepted; 46 adversarial mutations rejected"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
