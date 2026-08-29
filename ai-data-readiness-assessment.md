# AI-Data Readiness Assessment

Use this when a specific dataset, document collection, retrieval index, or
derived feature will influence one named AI use. The assessment helps a team
say “fit for this use,” “not yet,” or “not for this purpose” without pretending
that available data is universally AI-ready.

## Ten-minute first assessment

Complete these six lines before the full review:

1. **The AI use is:** name the exact task, not “use AI.”
2. **The person or decision affected is:**
3. **The information must mean and cover:**
4. **Its source, version, and permitted purpose are:**
5. **The system must abstain or stop when:**
6. **A separate authority or release decision is still owned by:**

### Miniature example

| First-pass line | Northbridge policy-retrieval answer |
| --- | --- |
| Named AI use | Retrieve current partner policy passages to help an analyst draft an exception explanation. |
| Affected person or decision | The analyst and partner receiving the explanation; the retrieval result does not approve a credit. |
| Required meaning and coverage | The current policy for the named partner, contract, exception type, and effective date, including superseding corrections. |
| Source, version, and purpose | Versioned policy records under the policy owner's authority, permitted for case investigation and explanation drafting. |
| Abstain or stop | No authoritative current policy, entitlement mismatch, unresolved version conflict, missing citation, or correction not propagated. |
| Separate gate | The accountable agent, workflow, capability, and release owners retain action and release authority. |

See the
[complete Northbridge AI-Data Readiness Assessment](examples/northbridge-ai-data-readiness-assessment-v1.md)
for the full application and its unresolved evidence.

## Plain-language vocabulary

- **Named use:** one specific task and consequence the information will support.
- **Fitness:** sufficient meaning, coverage, quality, freshness, rights, and
  evidence for that use—not for every possible use.
- **Provenance:** where the information came from and which versions and
  transformations shaped it.
- **Population:** the people, cases, records, periods, or conditions represented
  and omitted.
- **Temporal validity:** the period during which the information remains
  applicable.
- **Leakage or contamination:** information entering training or evaluation in
  a way that creates misleading performance or violates the intended boundary.
- **Abstention:** the system declines to answer or act when the evidence is not
  good enough.
- **Separate gate:** an authority, model, agent, workflow, tool, or release
  decision this data assessment cannot make.

**Status:** Working template
**Named AI use:**
**Decision or action supported:**
**System and release stage:**
**Assessment owner:**
**Separate release gate ID and accountable owner:**
**Separate model, agent, workflow, or tool-authority gate ID and accountable owner:**

This assessment decides readiness for one use. It cannot award a universal
“AI-ready” label to a platform or dataset.

> **Scope guard:** The outcome below approves, conditions, rejects, or defers
> only the named data's fitness for the named use. It does not approve the
> model, agent, workflow, tool authority, consequential action, or overall
> release. Record those decisions under their separate gate IDs and
> accountable owners. If no separate gate exists, this assessment cannot
> create one by implication.

## 1. Use boundary

- Users and affected parties:
- Model or retrieval role:
- Consequence and reversibility:
- Human review or escalation:
- Prohibited outputs or uses:
- Required abstention or stop conditions:

## 2. Meaning and fitness

| Required information | Meaning authority | Intended representation | Known ambiguity/bias/gap | Fitness evidence |
| --- | --- | --- | --- | --- |
| | | | | |

- Training, evaluation, retrieval, context, or monitoring role:
- Population and coverage limits:
- Temporal validity:

## 3. Provenance and reproducibility

- Source and version evidence:
- Transformation and feature lineage:
- Document, chunk, embedding, and index versions:
- Labels or annotations and authority:
- Ability to reconstruct a result:
- Correction and deletion propagation:

## 4. Rights, access, and purpose

- Classification and sensitivity:
- Approved collection and use purpose:
- Consent, contract, policy, or other authority:
- Tenant, subject, row, column, and document entitlements:
- Derived-data and model-output restrictions:
- Retention and deletion:

## 5. Quality and evaluation

| Risk or required behavior | Dataset/evaluation design | Threshold or acceptance rule | Result | What remains unknown |
| --- | --- | --- | --- | --- |
| | | | | |

- Slice/cohort coverage:
- Leakage and contamination checks:
- Staleness and drift monitoring:
- Retrieval attribution and citation checks:
- Adversarial and misuse tests:

## 6. Operational control

- Refresh and version policy:
- Stop-trust signals:
- Incident owner:
- Rollback, quarantine, or disabling path:
- Reassessment triggers:

## 7. Decision

**Outcome:** approve / conditionally approve / reject / defer
**Scope and conditions:**
**Rejected or unresolved uses:**
**Evidence required to expand scope:**
**Data-fitness approvers and authority:**
**Separate gates still required or unresolved:**

## Outside-team comprehension test

Give the six first-pass lines to someone outside the data or AI implementation
team. Ask them to name the approved use, one prohibited inference, one condition
that forces abstention, and the owner of the separate action or release gate.
If “the data is AI-ready” is their summary, the assessment is still too broad.
