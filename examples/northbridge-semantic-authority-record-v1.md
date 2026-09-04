# Northbridge Semantic-Authority Record — Constructed Example

<!-- markdownlint-disable MD013 -->

**Record ID:** NBX-SAR-001
**Record version:** 1.0.0
**Template:** [Semantic-Authority Record](../semantic-authority-record.md)
**Template source version:** Illustrative template bytes reviewed 2026-08-29<br>
**Template source SHA-256:** `6a9bf8c05722fcd56a0f61d266dae3cd1f2fd624474b3d3c4dad471f9f6cd11b`
**Status:** `SCENARIO — conditionally approved; translation unresolved`
**Term, field, measure, or concept:** `on_time_for_renewal`
**Effective interval:** SCENARIO-Q3 renewal cycle
**Decision owner:** NBX-ROLE-PARTNER-OPS for contractual meaning; NBX-ROLE-RENEWAL for acceptance in the renewal use

> **Constructed-example disclosure:** This record contains fictional roles,
> rules, decisions, and examples. It is not evidence, legal interpretation, an
> account of John Briggs's work, or proof that the authority allocation works.

## 1. Meaning in context

- **Plain-language definition:** A contractual delivery obligation is on time
  when its qualifying completion event falls inside the window established by
  the partner contract effective for that obligation, after only the approved
  exception and grace rules for that version are applied.
- **Business question answered:** Under the fictional SCENARIO-Q3 rule, which
  settled obligations count toward a partner's renewal evidence?
- **Unit of observation or grain:** One settled contractual delivery
  obligation, not a scan, package, order, partner-day, or buyer promise.
- **Population, inclusion, and exclusion:** Include obligations attached to an
  eligible partner-contract relationship at the review cutoff. Exclude
  unresolved identities, open obligations, and buyer-requested changes only
  when the effective contract rule authorizes that exclusion.
- **Time basis and timezone:** Event time interpreted in the contractual
  location timezone; effective contract and identity versions selected at the
  obligation's declared start event; reporting cutoff fixed for SCENARIO-Q3.
- **Calculation, classification, or interpretation rule:** Compare the qualifying completion
  event with the effective contractual window; apply only versioned exceptions;
  preserve `unknown` when a required event, identity, or rule is unresolved.
- **Examples that qualify:** `SCENARIO EXAMPLE` — an obligation completing
  before the effective contract deadline; an obligation inside an authorized
  grace period.
- **Near-misses or counterexamples:** `SCENARIO EXAMPLE` — arrival inside the
  buyer promise but outside the partner contract; a late scan corrected after
  the settlement cutoff; an obligation silently attached to today's partner
  identity instead of its historical relationship.

## 2. Authority

| Decision | Accountable authority | Required contributors | Evidence or policy basis | Escalation path |
| --- | --- | --- | --- | --- |
| Define contractual meaning | NBX-ROLE-PARTNER-OPS | NBX-ROLE-CONTRACT-CUSTODY, NBX-ROLE-SERVICE-OPS | Effective fictional contract rule NBX-POL-CONTRACT-17 | NBX-ROLE-COMMERCIAL-GOVERNANCE |
| Change meaning | NBX-ROLE-PARTNER-OPS | Renewal, contract custody, affected consumers | Versioned change proposal and impact review | NBX-ROLE-COMMERCIAL-GOVERNANCE |
| Approve translation | Authority for the receiving use | Source authority and product owner | Translation table, loss statement, negative cases | Cross-domain design review |
| Resolve dispute | NBX-ROLE-COMMERCIAL-GOVERNANCE | All authorities whose meanings conflict | Competing definitions and consequence statement | Defer the affected use if unresolved |
| Retire definition | NBX-ROLE-PARTNER-OPS | NBX-ROLE-RENEWAL, NBX-ROLE-PRODUCT | Consumer inventory and migration record | Stop publication for unmigrated use |

Technical custody belongs to NBX-ROLE-PRODUCT. Platform operation belongs to
NBX-ROLE-RELIABILITY. Neither role may redefine the contractual measure by
changing code or metadata.

## 3. Scope and competing meanings

| Context or domain | Definition/version | Legitimate use | Incompatible use | Translation required |
| --- | --- | --- | --- | --- |
| Buyer promise | NBX-MEAN-BUYER-02 | Customer reporting and service recovery | Partner contractual accountability | Yes; buyer clock and change rules do not transfer |
| Partner contract | NBX-MEAN-CONTRACT-17 | Contract management and renewal evidence | Live dispatch priority without operations context | Source meaning for this record |
| Service operations | NBX-MEAN-SERVICE-06 | Intervention while work is active | Retrospective renewal comparison | Yes; mutable operational state must settle first |
| Renewal analysis | NBX-SAR-001 | Versioned SCENARIO-Q3 retrospective review | Public ranking or autonomous action | Yes; binds contract meaning to cutoff and population |

- **Shared invariant, if any:** Source observations, event identities, clocks, and
  effective versions must remain inspectable even when interpretations differ.
- **Meaning that must not be forced into a canonical form:** Buyer-promise,
  contractual, and live-service meanings remain legitimate and separate.
- **Loss introduced by translation:** A single renewal boolean discards the
  buyer-facing promise, evolving service state, source uncertainty, and some
  exception detail. Consumers needing those facts must use the source views.

## 4. Change and evidence

- **Versioning rule:** Patch corrects wording without changing classification;
  minor adds compatible examples or mappings; major changes population,
  clock, qualifying event, exception, or use.
- **Backdating or correction rule:** Never silently apply today's definition to
  a prior review. Record the original and corrected classification, effective
  versions, reason, and consumer notification.
- **Consumers requiring notice:** NBX-ROLE-RENEWAL, NBX-ROLE-PRODUCT, and any
  authorized downstream review holding NBX-PERF-3.2.1.
- **Recalculation or migration required:** Any change to the contractual window,
  qualifying event, approved exception, identity translation, or cutoff.
- **Tests or reconciliations:** `PLANNED/UNRUN` examples at boundary times,
  buyer-change exception cases, missing-event cases, and historical identity
  mappings. No result is claimed.
- **Evidence retained:** Definition versions, role decisions, dissent,
  translation mappings, scenario examples, product impact, and stopped uses.
- **Unknowns and dissent:** The acquisition-era source encoded a predecessor
  relationship without a complete effective-time translation. The renewal
  classification for that subset remains `unknown`.
- **Trigger for reconsideration:** Resolved predecessor mapping, contract-rule
  change, a new consumer use, recurring unknowns, or disagreement about the
  qualifying event.

**Decision:** `SCENARIO — conditionally approved for the declared renewal
context; disputed acquisition-era translation remains unresolved.`
**Approver and date:** Fictional NBX-ROLE-PARTNER-OPS and NBX-ROLE-RENEWAL;
scenario interval SCENARIO-Q3, not a real date or approval.

## Cross-record effects

- NBX-DPC-001 binds the information promise to this semantic version.
- NBX-QES-001 treats unresolved acquisition-era translation as a cohort stop,
  not as a default `false` classification.
- NBX-PVR-001 requires this version and translation record in the chain.
- NBX-ADR-001 cannot expand the definition or resolve the dispute through a
  model-generated explanation.
