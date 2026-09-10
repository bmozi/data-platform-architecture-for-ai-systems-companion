# AI Answer Acceptance Pack

**Use boundary:** Illustrative field tool; practitioner validation unrun.
**Use with:** [Data Meaning, Provenance, and Permitted-Use Contract](data-meaning-provenance-and-permitted-use-contract.md) and [AI-Data Readiness Assessment](ai-data-readiness-assessment.md).
**Does not authorize:** a model, agent, API, workflow, business action, or release.

Use this pack when a person can ask an AI system a consequential question about
organizational information. It turns “the agent can answer it” into a
reviewable decision: which question is in scope, what the terms mean, which
evidence may support the answer, when the system must abstain, and who owns a
separate action decision.

This is not a generic prompt-writing worksheet. A polished response can still
be semantically wrong, stale, out of scope, or impermissibly derived.

## Ten-minute first pass

1. Name the one question, affected person, and decision it may inform.
2. Mark the answer as descriptive, advisory, or action-triggering. Action
   authority belongs in a separate record.
3. List the approved measures, terms, population, and effective-time boundary.
4. Name the sources and citations an answer must carry.
5. State the no-answer conditions and escalation owner.

If the request says “tell me everything,” “use all data,” or “take the best
action,” stop and narrow the question before configuring the system.

## Acceptance record

| Field | Decision or evidence | Owner | Revalidation trigger |
| --- | --- | --- | --- |
| Question, affected party, and decision | | | |
| Answer role: descriptive, advisory, or action-triggering | | | |
| Approved measures, terms, and business-language synonyms | | | |
| Excluded meanings, measures, and misleading synonyms | | | |
| Population, grain, cohort, geography, and effective-time boundary | | | |
| Approved semantic model, data product, and version | | | |
| Required source, transformation, and retrieval evidence | | | |
| Freshness, quality, coverage, and uncertainty conditions | | | |
| Entitlement, purpose, and permitted inference boundary | | | |
| Response format, citations, and uncertainty statement | | | |
| Required abstention or escalation condition | | | |
| Separate human, agent, workflow, API, or release authority | | | |

## Test prompts and review evidence

Write acceptance tests before calling the configuration complete. Keep the
test question, permitted evidence set, expected answer boundary, and reviewer
decision together. The “expected answer” may be a refusal or escalation.

| Test ID | Prompt or condition | Permitted evidence | Expected boundary | Result and reviewer evidence |
| --- | --- | --- | --- | --- |
| Known answer | | | Answer with cited evidence and declared limits | |
| Ambiguous term | | | Ask a clarifying question or name the chosen definition | |
| Stale source | | | Abstain or state the freshness limitation | |
| Restricted attribute | | | Refuse or route to an entitled process | |
| Conflicting evidence | | | Surface the conflict; do not silently choose | |
| Action request | | | Return information only and name the separate authority | |
| Out-of-scope request | | | Decline or route to the correct product | |

## What AI may generate

AI may propose question variants, candidate synonyms, draft explanations,
retrieval queries, test prompts, and citations for review. Treat these as
unapproved suggestions. A generated SQL query, DAX expression, source list, or
confidence statement is not proof that the meaning, evidence, or permission is
correct.

## What AI must not decide

AI must not silently choose between contested business meanings; expand its own
data scope; use a restricted attribute because it seems predictive; convert an
answer into a credit, employment, pricing, access, or other consequential
action; or waive an abstention condition. Those are accountable authority
decisions owned outside this pack.

## Completion check

A reviewer should be able to answer all of these without reading source code:

- What exact question is allowed?
- Which definition, population, and time boundary make the answer meaningful?
- Which evidence must accompany the answer, and what may not be used?
- When must the system say “I do not know” or escalate?
- Who owns the separate decision if someone wants to act on the answer?

If any answer is “the agent will figure it out,” the acceptance record is not
complete.

## Evidence boundary

This proposed pack is a design aid, not evidence that an AI system gives
correct answers, protects rights, reduces review burden, or improves decisions.
Before any such claim, freeze versioned fixtures and test prompts; include
negative, stale, restricted, contradictory, and out-of-scope cases; retain
reviewer outcomes and misses; and record the task, versions, expected outcomes, and remaining limits.
