# Harbor Grove Scenario: Is This Information Ready for This AI Use?

**Packet:** DATA-RV-PILOT-001 version 1.1.1
**Status:** Fictional, prepared, and unrun

Harbor Grove Housing operates eighteen fictional apartment buildings. Resident
support agents answer questions about urgent maintenance, including loss of
heat. Leadership wants an AI assistant that can draft a response while the
agent speaks with the resident.

The request is:

> Put our policies and work-order history into a vector database so the AI can
> answer maintenance questions. We already have the data, so can we launch a
> pilot next month?

The named use for this review is narrower:

> Draft a non-authoritative response for a trained Harbor Grove support agent
> handling a no-heat question from a resident in buildings HG-03 or HG-04. The
> draft must cite the current approved policy and state when the agent must use
> the existing emergency escalation process. The agent reviews the source and
> remains responsible for the response. The AI may not create or close a work
> order, contact a vendor, determine legal rights, or decide whether an
> emergency actually exists.

## Known facts

1. Policy owners approved **Heat Response Policy v3**, effective October 1.
   Version 2 remains in a shared drive for historical reference.
2. The retrieval index was built September 10 and contains chunks from both
   versions. It does not retain effective date in every chunk and has no rule
   that prefers the current approved version.
3. The source system can identify policy ID, version, approval owner, effective
   interval, and building scope. The index record currently retains document
   ID but not all of those fields.
4. Policies for HG-03 and HG-04 use the same current no-heat procedure. Policies
   for five other buildings are still under review and are outside the named
   pilot.
5. The support application knows the resident's building. The proposed AI
   service account can retrieve policy and work-order data for all eighteen
   buildings.
6. The approved purpose record allows current maintenance policy to support an
   agent-reviewed draft. It does not authorize use of resident notes, payment
   history, disability information, vendor commentary, or historical work-
   order narratives.
7. The work-order field `resolved` has three meanings: a vendor marks the visit
   complete, support means the resident confirmed service, and finance means
   no further invoice is expected. No role owns a shared definition.
8. The named use does not require `resolved` or work-order history. A project
   sponsor still wants to include them because “more context should help.”
9. A policy correction reaches the source repository immediately. No owner,
   deadline, or test ensures the correction reaches chunks and the retrieval
   index.
10. No retrieval evaluation has tested obsolete, contradictory, restricted,
    missing-building, or unanswerable questions.
11. No model, interface, entitlement, citation, usability, security, release,
    or outcome test has run.
12. The release owner and the owner of the separate model/tool authority gate
    have not been assigned.

## Stage A task

1. Explain what “AI-ready data” should mean for this exact use without using a
   universal readiness badge.
2. Use the AI-Ready Data Journey and complete the first pass plus relevant
   portions of the AI-Data Readiness Assessment.
3. Decide whether the named policy information is ready, conditionally ready,
   not yet ready, or not permitted for this use.
4. Keep source data, derived chunks/indexes, model behavior, agent review,
   action authority, and release as distinct decisions.
5. State what must cause abstention or stop trust.
6. After the live update, complete and freeze the one-screen practitioner
   handoff without estimating savings or inventing an owner or date.

The facilitator will provide one live update after the first artifact is
frozen.

## Boundary

You are not being asked to select a platform, approve the model or release,
interpret law, or design the entire enterprise data estate. “Unknown,”
“disputed,” “not permitted,” and “stop” are valid results.
