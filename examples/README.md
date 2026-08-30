# Constructed Companion Examples

<!-- markdownlint-disable MD013 -->

**Collection ID:** DATA-EX-NBX-001
**Collection version:** 1.0.0
**Status:** Transparent constructed example; not an experiment result
**Domain:** Fictional Northbridge Exchange partner-renewal review
**Terms:** [Working internal companion terms](../TERMS.md)

## Disclosure and evidence boundary

Northbridge Exchange, its roles, records, quantities, conditions, decisions,
and outcomes are fictional scenario material. The records demonstrate how the
five working templates can refer to one another. They do not describe John
Briggs's experience, a customer, an employer, an executed control, or an
observed business result.

No DATA-X005 or DATA-X006 run occurred. No practitioner used these records. No
detector, reconstruction, workflow, model, release process, or control was
executed. A scenario value labeled `SCENARIO` is an authored test condition,
not a measurement. A completed example does not establish correctness,
completeness, usability, detection, safety, legal sufficiency, productivity,
cost reduction, or beneficial outcome.

## Integrated record set

| Record ID | Version | File | Decision represented | Scenario state |
| --- | --- | --- | --- | --- |
| NBX-DPC-001 | 1.0.0 | [Data-Product Contract](northbridge-data-product-contract-v1.md) | Promise for the quarterly renewal product | Conditionally approved |
| NBX-SAR-001 | 1.0.0 | [Semantic-Authority Record](northbridge-semantic-authority-record-v1.md) | Meaning and authority for `on_time_for_renewal` | Conditionally approved; one translation unresolved |
| NBX-QES-001 | 1.0.0 | [Quality-Evidence Scorecard](northbridge-quality-evidence-scorecard-v1.md) | Fitness of the product for partner-level renewal | Scenario stop because a cohort condition fails |
| NBX-PVR-001 | 1.0.0 | [Provenance Requirements](northbridge-provenance-requirements-v1.md) | Reconstruction chain for a renewal score and its population context | Insufficient for product-level use; eligible-partner population link deliberately missing |
| NBX-ADR-001 | 1.0.0 | [AI-Data Readiness Assessment](northbridge-ai-data-readiness-assessment-v1.md) | Data fitness for human-reviewed renewal support | Deferred while QES and PVR stops remain; release gate separate |

The records deliberately preserve partial and negative states. They are not a
happy-path claim that completing five forms creates trust. The cross-record
links make a conflicting decision visible: NBX-ADR-001 cannot pass while the
named product is stopped by NBX-QES-001 and its complete eligible-partner
population cannot be reconstructed under NBX-PVR-001.

The [One-Screen Handoff Miniature](one-screen-handoff-miniature-v1.md) is a
separate constructed format example for a compact decision transfer. It is not
part of `DATA-RV-PILOT-001`, is never a scored-route input, and carries no
freeze or usability result.

## How to read the sequence

1. Start with NBX-DPC-001 to see the bounded information promise and excluded
   uses.
2. Use NBX-SAR-001 to see why one `on_time` field cannot carry three meanings.
3. Inspect NBX-QES-001 for the scenario's aggregate-green, cohort-red condition
   and stop action.
4. Inspect NBX-PVR-001 for the deliberately broken eligible-partner population
   link and the distinct retained settled-obligation denominator.
5. Finish with NBX-ADR-001. It defers the named data-fitness decision and leaves
   the separate system release gate unresolved.

## Stable-fixture convention

These files use UTF-8 text, LF line endings, explicit record IDs, semantic
versions, stable scenario identifiers, and no generated timestamps. Do not
replace `SCENARIO` labels with claimed observations. Before any authorized run,
copy the exact files and their pinned governed-template bytes into the
controlled evidence package, calculate SHA-256 digests, record the tool and
command used, and preserve those frozen bytes.

The [experiment register](https://github.com/bmozi/architecting-data-platforms-in-the-age-of-ai/blob/main/EXPERIMENT-REGISTER.md) remains authoritative
for DATA-X005 and DATA-X006. These examples do not change its `unrun` state.
