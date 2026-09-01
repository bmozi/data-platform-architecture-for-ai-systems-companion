# Stage A Initial Workbook

- Artifact: `DATA-A-INITIAL-WORKBOOK-v1`, `INITIAL COMPLETE`
- Attempt: `DATA-SYN-20260830-007`
- Completion: 2026-08-30T14:05:00-0600 MDT
- Actor: synthetic reader

## Recognition

- The support agent needs a current, building-scoped draft response for a resident reporting no heat.
- Harbor Grove has records, but the index mixes policy v2 and v3, loses effective-date metadata, and permits cross-building retrieval.
- Residents could receive obsolete escalation instructions or have restricted HG-11 notes exposed; agents and policy owners could also be misled.
- Fit information could reduce lookup time while keeping the trained agent responsible for the answer.

## Readiness journey

| Question | Bounded answer | Evidence | Unknown/stop trigger |
| --- | --- | --- | --- |
| Ready for what? | Non-authoritative draft for trained HG-03/HG-04 agents | Scenario and approved purpose | Any request to act or decide emergency status |
| Meaning/authority? | Current no-heat procedure; policy owner owns meaning | v3 approval and scope facts | Unresolved `resolved` semantics; owner change without review |
| Fit? | Not yet | Mixed versions and missing index fields | v2 retrieval, stale freshness, missing required passage |
| Traceable? | Not yet | Source system has version/scope, index does not | Citation lacks ID/version/effective date |
| Permitted/access? | Current policy for named use only | Purpose record | Any resident note, HG-11 data, or all-building service account |
| Remain ready? | Not demonstrated | No correction propagation owner | No indexed correction SLA or monitoring |
| Decision/gates? | Defer; model/action/release separate | Bounded scope | Reconsider only after conditions are evidenced |

## Initial decision

`DEFER` the pilot. The artifact makes the use and consequences concrete, but
does not yet establish fit, traceability, entitlement, or operability.
