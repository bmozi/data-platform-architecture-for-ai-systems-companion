# Decision-Fitness Practicum

**Use boundary:** Illustrative 90-minute exercise; practitioner testing unrun.
**Scenario:** Transparent fictional composite, Northbridge Exchange.
**Purpose:** Practice turning a plausible AI answer into a bounded,
decision-ready data product. This practicum does not demonstrate that the
method works in production or that participants learn it without testing.

## Outcome and prerequisites

By the end, a learner should be able to identify why one plausible AI answer
is unfit for a named decision and produce a first-pass:

- Data Meaning, Provenance, and Permitted-Use Contract;
- AI Answer Acceptance Pack; and
- decision receipt with a stop-trust condition and a separately owned action
  boundary.

Read the signature Contract and AI-Data Readiness Assessment first. Use a
timer, the three linked templates, and no real customer, employee, health, or
confidential data.

## Composite case: Northbridge Exchange

Northbridge Exchange is a fictional business-to-business marketplace. A
renewal-review lead asks a proposed AI assistant:

> “Which partners are underperforming and should receive intervention this
> week?”

The assistant produces a tidy ranked list. Its explanation combines a
month-to-date fulfillment field, a prior-week support-export field, and a
retrieved policy note. The list has three hidden problems:

1. **Meaning:** `underperforming` was interpreted as “late fulfillment,” but
   the renewal team normally considers eligible contractual obligations and
   documented exceptions.
2. **Freshness and population:** the support export is six days old and omits
   a recently onboarded partner cohort.
3. **Permitted use:** a restricted dispute-status attribute appears in the
   retrieval context. The information may help an entitled investigator, but it
   is not approved for broad renewal triage.

The list might still contain a useful lead. It is not yet an approved basis for
intervention. Northbridge, its data, roles, and consequences are fictional
teaching material—not a customer, observed incident, or measured outcome.

## 90-minute run sheet

| Time | Learner task | Deliverable |
| --- | --- | --- |
| 0–10 min | Mark what the answer claims, who could be affected, and whether “intervention” is descriptive, advisory, or action-triggering | One-sentence use boundary |
| 10–25 min | Separate the disputed meanings, population, and effective-time boundary | Three semantic/freshness gaps |
| 25–40 min | Complete the signature Contract’s decision card for the bounded review use | First-pass Contract |
| 40–55 min | Complete the AI Answer Acceptance Pack, including two answer tests and two no-answer tests | Acceptance record and test table |
| 55–70 min | Decide the cheapest defensible service level using the Decision Cost Envelope | Continue, narrow, defer, or do-not-build recommendation |
| 70–82 min | Enter open consequences in the Data Trust Operating Cadence ledger | Named owners and escalations |
| 82–90 min | Write a decision receipt and compare it with the annotated answer | Reviewable receipt and one remaining unknown |

## Exercises

### 1. Bound the question

Rewrite the request so it supports a human renewal-review decision without
authorizing the assistant to intervene. Name the people affected, the valid
time boundary, and one excluded use.

### 2. Expose the three failures

For each case problem, record the information that is missing, the owner who
must resolve it, and whether the result should continue, be conditioned, stop,
or remain unknown.

### 3. Write acceptance tests

Add four tests to the AI Answer Acceptance Pack:

- a known-answer request using current, permitted evidence;
- an ambiguous request using “underperforming”;
- a request made after the support export becomes stale; and
- a request that asks the assistant to directly contact or penalize a partner.

For each, state the expected answer boundary. A correct result can be an
abstention or escalation.

### 4. Choose a service level

Use the Decision Cost Envelope. Decide whether a daily, human-reviewed batch
is adequate or whether the scenario justifies a faster product. Also write a
specific condition under which work should pause rather than adding more data.

### 5. Produce a decision receipt

Complete this short form:

| Receipt field | Learner response |
| --- | --- |
| Named decision and human owner | |
| Allowed information use | |
| Meaning, population, and time boundary | |
| Required evidence and citations | |
| Prohibited inference or action | |
| Stop-trust condition | |
| Separate action authority | |
| Open evidence and next review | |

## Annotated answer example

The following is one defensible response, not the only acceptable one.

| Exercise | Example answer | Why it is stronger |
| --- | --- | --- |
| Bounded question | “Which currently eligible partners show documented fulfillment exceptions for the weekly human renewal-review queue?” The assistant may summarize evidence; it may not contact, penalize, or change terms for a partner. | It replaces an undefined judgment with a review use and separates information from action authority. |
| Meaning | Use the contractually eligible-obligation definition, with exception authority named in the Semantic-Authority Record. Do not equate all late events with poor performance. | It makes the semantic choice challengeable. |
| Freshness/population | The support export is excluded until refreshed and its cohort coverage and permitted use are verified. The answer must name its data-through time. | A source being present does not establish coverage or currentness. |
| Restricted attribute | Exclude dispute-status from renewal triage. Route a need for it to the permitted-use owner and entitled investigation process. | Predictive usefulness does not create a right to use data. |
| Stale-source test | Expected result: exclude stale advisory support context. Withhold the queue if mandatory eligibility, cohort, or settlement evidence fails; permit a narrower use only after its own checks pass. | A graceful no-answer is safer than a fabricated certainty. |
| Action request | Expected result: provide no action. State that outreach or term changes require the separately accountable renewal authority and its process. | The data/AI boundary cannot approve a business action. |
| Service level | Start with a daily human-reviewed queue if the decision can wait, a correction path exists, and the current eligible cohort and settlement evidence are verified. Pause if population, meaning, or settlement remains unresolved. | It ties platform burden to the decision rather than assuming real time is better. |

## Review questions

1. Why is a well-cited answer still unfit if it uses the wrong population?
2. Which condition makes this an action-triggering use rather than an advisory
   use?
3. What would change if an entitled dispute investigator, rather than the
   renewal-review lead, asked the question?
4. When is “do not build yet” more responsible than adding a new retrieval
   source?
5. Which unresolved consequence has a named owner at the end of your receipt?

## Facilitator and evidence boundary

Do not score a learner as competent merely because they filled every field.
Before a future authorized practitioner session, freeze the scenario, blank
template versions, task brief, expected routing criteria, and answer rubric;
then retain omissions, safe refusals, confusion, and negative results in the
[companion usability log](companion-usability-log.md). Record the scenario, tool versions, expected reasoning, and observed results. Until then, this is a
prepared exercise, not evidence of comprehension, transfer, usability, or
effectiveness.
