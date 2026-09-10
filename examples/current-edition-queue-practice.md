# Derive and correct a supplied review queue

**Status:** Fictional Northbridge practice; execution and human learning unrun.
This repaired input set is separate from the failed stale/restricted ranking
in the [Decision-Fitness Practicum](../decision-fitness-practicum.md) and the
older quarterly-renewal examples. It does not validate either product.

Amara receives a daily queue for human renewal review. Contract operations
supplies `queue-rule-1`: include a partner when **more than 50%** of eligible
obligations were unfulfilled at settlement, with at least two eligible
obligations. Fewer than two means insufficient evidence. Approved exceptions
leave both numerator and denominator. This is a teaching policy, not a general
measure of partner merit.

## Calculate from these inputs

All obligations were due September 7, 2026 at 12:00 UTC; settlement is 18:00
that day. `roster-1` includes the complete two-partner cohort, including new
partner Cedar. `fulfillment-1` and `exceptions-1` were captured September 8 at
08:00 UTC. Completion times below are September 7; none means no completion
through capture time.

| ID | Partner | Completion UTC | Approved exception |
| --- | --- | --- | --- |
| H1 | Harborline | 17:00 | none |
| H2 | Harborline | 19:00 | none |
| H3 | Harborline | none | none |
| H4 | Harborline | none | exception-4: exclude |
| C1 | Cedar | 17:00 | none |
| C2 | Cedar | none | none |

Use `queue-calc-1` with only these permitted inputs. Exclude support exports,
retrieved policy guesses, and dispute status.

1. Record eligible and unfulfilled IDs, rates, and membership in `queue-v1`.
2. At 09:00 September 8, contract operations approves `exception-2` for H2,
   explicitly effective for the original obligation. Recalculate using
   `exceptions-2`; identify what Amara must be told.
3. Separately change H1 from 17:00 to 17:30 in `fulfillment-2`, without the
   H2 exception. Does the queue change? Does the evidence record change?
4. Explain the result if H2's exception is merely requested or disputed.

Carry the input versions, rule, settlement clock, calculation, consumer, and
correction into [Provenance Requirements](../provenance-requirements.md).
Record the review-only use and excluded action in the
[Meaning, Provenance, and Permitted-Use Contract](../data-meaning-provenance-and-permitted-use-contract.md).

## Check after trying

- Initially Harborline has eligible H1/H2/H3, unfulfilled H2/H3: 2/3 = 66.7%.
  Cedar has eligible C1/C2, unfulfilled C2: 1/2 = 50%. Only Harborline enters.
- The approved H2 correction leaves Harborline eligible H1/H3, unfulfilled H3:
  1/2 = 50%. `queue-v2` is empty. Link it to `queue-v1`, `exceptions-2`, and
  the approval; withdraw the active Harborline item and notify Amara to revisit
  any review already based on it. Preserve the prior receipt under its
  retention rule. An empty queue does not prove overall satisfactory performance.
- The separate H1 time correction leaves membership unchanged but needs a
  successor source/calculation receipt. H1 still completed before settlement.
- A requested or disputed exception is not an approved correction. Leave that
  decision with contract operations and expose the uncertainty to Amara.

This queue supports review. It authorizes no outreach, penalty, or renewal
change. Use the [AI Answer Acceptance Pack](../ai-answer-acceptance-pack.md)
to distinguish a supported answer from a prohibited action.
