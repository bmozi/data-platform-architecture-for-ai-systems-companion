# Failure Lab: The Green Pipeline and the Wrong Decision

**Status:** Constructed exercise; prepared and unrun. It is not evidence of a
real failure, control effectiveness, or practitioner usability.

## Scenario

An executive dashboard and an AI assistant both report “on-time delivery.” The
pipeline is green. Sales defines on-time as the promised calendar day;
operations uses business days and excludes customer holds; finance counts the
invoice date. A corrected shipment event reached the warehouse but not the
embedding index. The assistant cites an older policy that the user is allowed
to read but not authorized to apply to this account.

## Attractive shortcut

Tune the prompt, add more documents, and publish a single enterprise metric.

## Find the hidden decisions

1. Which definition is authoritative for the named use?
2. What is the grain and time boundary of each claim?
3. Which source, correction, transformation, chunk, and index version shaped
   the answer?
4. Does access imply permission for this purpose?
5. Which mismatch forces abstention rather than a plausible answer?
6. Who owns correction propagation and the decision to restore trust?

## Produce

- a [Semantic-Authority Record](semantic-authority-record.md) for “on time”;
- one stop-trust rule in the
  [Quality-Evidence Scorecard](quality-evidence-scorecard.md);
- correction and index-version requirements in
  [Provenance Requirements](provenance-requirements.md);
- a bounded [AI-Data Readiness Assessment](ai-data-readiness-assessment.md).

## Evidence that would change the design

Test contradictory definitions, late corrections, stale indexes, unauthorized
purpose, missing cohorts, and absent citations. Record whether the system
abstains, whether the output can be reconstructed, and what remains unknown.

## Outside-team test

Ask someone outside data engineering: “What does on-time mean here, and when
must we stop trusting the answer?” If the artifact cannot support the answer,
the data is available but not decision-ready.
