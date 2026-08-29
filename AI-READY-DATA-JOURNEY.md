# The AI-Ready Data Journey

“AI-ready” is not a permanent property of a database. Data is ready only when
named information is demonstrably fit to influence one named AI use under
known conditions.

A data platform is the people, rules, and machinery that turn records into
maintained information products for named uses—not merely the place data is
stored.

## Why this comes first

APIs give automation a governed way to ask or act. Events declare what
happened. Workflows preserve responsibility. Agents decide and act within
delegated boundaries. All of them can move bad, stale, misunderstood, or
unauthorized information faster. Before adding intelligence to the path, make
the information promise visible.

## The seven readiness questions

### 1. Ready for what?

Name one task: retrieve a current policy passage, predict a maintenance need,
summarize a case, evaluate a model, or recommend a next action. “Use our data
with AI” is not a testable use.

**Produce:** a named use, affected person or decision, consequence, and
abstention condition.

### 2. What does the information mean?

Define the business term, grain, time boundary, inclusions, exclusions, and
version. Resolve who has authority to change that meaning.

**Produce:** a [Semantic-Authority Record](semantic-authority-record.md).

### 3. Is it fit for this use?

Examine coverage, freshness, accuracy, completeness, representativeness,
known gaps, and the cost of being wrong. Different uses require different
evidence.

**Produce:** a [Quality-Evidence Scorecard](quality-evidence-scorecard.md) with
stop-trust rules, not a generic quality percentage.

### 4. Can we trace and reproduce it?

Record sources, versions, transformations, labels, chunks, embeddings, indexes,
corrections, and deletion propagation. A plausible answer without a defensible
information path is not ready for consequential use.

**Produce:** [Provenance Requirements](provenance-requirements.md).

### 5. May it be used this way?

Check purpose, classification, consent or contract, tenant and subject
boundaries, entitlements, retention, and prohibited derived uses. Access to a
record does not automatically authorize every AI use.

**Produce:** explicit permitted and prohibited uses in the
[Data-Product Contract](data-product-contract.md).

### 6. Can it remain ready?

Assign an owner, service expectation, correction path, version policy,
monitoring, incident response, and retirement rule. A one-time cleanup creates
a snapshot; it does not create a maintained information product.

**Produce:** operating ownership, refresh evidence, drift and staleness signals,
and a stop-trust path.

### 7. Who decides and what remains separate?

Decide **approve**, **conditionally approve**, **defer**, or **reject** for the
named data use. Keep model, tool, workflow, agent-authority, and release gates
separate.

**Produce:** a completed
[AI-Data Readiness Assessment](ai-data-readiness-assessment.md) with conditions,
unknowns, and reconsideration triggers.

## The readiness ladder

| Level | What is true | What is not yet justified |
| --- | --- | --- |
| 0 — Available | Records can be accessed. | Meaning, fitness, rights, and trust. |
| 1 — Understandable | Meaning, grain, time, owner, and limits are stated. | Fitness for an AI use. |
| 2 — Fit for one use | Required quality, coverage, and rights are evidenced for a named use. | Readiness for other uses. |
| 3 — Traceable | Sources, versions, transformations, and result influence can be reconstructed. | Ongoing readiness. |
| 4 — Operable | Monitoring, correction, abstention, incidents, and reassessment have owners. | Permission for an agent to act. |
| 5 — Decision-ready | The bounded data-fitness gate is approved with evidence and conditions. | Model, action, or production-release approval. |

This is a reasoning ladder, not an organizational maturity score. A team may
reject a use at any level and make the best architectural decision available.

## Monday-morning first pass

Choose one answer, recommendation, or action your organization wants AI to
produce. In ten minutes, complete the six lines at the top of the
[AI-Data Readiness Assessment](ai-data-readiness-assessment.md). Circle every
word that different teams could define differently. Those circles are your
first semantic backlog.

## Outside-team comprehension test

Give the result to someone outside the data and AI teams. Ask: What may this
data influence? When must the system decline? Who owns the meaning? What use is
still prohibited? If the summary is only “the data is clean,” the readiness
case is not yet understandable.
