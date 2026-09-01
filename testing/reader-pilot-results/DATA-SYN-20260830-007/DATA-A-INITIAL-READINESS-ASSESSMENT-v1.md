# Stage A Initial Readiness Assessment

- Artifact: `DATA-A-INITIAL-READINESS-ASSESSMENT-v1`, `INITIAL COMPLETE`
- Attempt: `DATA-SYN-20260830-007`
- Completion: 2026-08-30T14:08:00-0600 MDT

Named use: draft a non-authoritative no-heat response for a trained support
agent serving HG-03 or HG-04. The agent reviews the current approved policy;
the assistant may not send messages, create or close work orders, contact a
vendor, determine legal rights, or decide whether an emergency exists.

Decision: `DEFER`.

Required before reconsideration: rebuild the index with policy ID, version,
approval owner, effective interval, and building scope; exclude HG-11 and all
unauthorized resident/work-order fields at retrieval and output; enforce
current-v3 selection; emit version/effective-date citations; define correction
propagation and freshness monitoring; assign meaning, privacy/incident, and
index-operation owners; add abstention tests for stale, missing, conflicting,
or out-of-scope evidence. Model evaluation, action authority, and production
release remain separate gates.

Evidence classes: scenario facts are `CONSTRUCTED`; this assessment is
`SYNTHETIC OBSERVED`; no production or human claim follows.
