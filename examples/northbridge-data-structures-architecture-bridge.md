# Northbridge Data-Structures Architecture Bridge

**Status:** Constructed teaching example; `PLANNED/UNRUN`

**Disclosure:** Northbridge Exchange, its warehouse, records, quantities,
workload, and outcomes are fictional composite teaching material. They are not
production measurements or John Briggs project history.

## Operational structures are not analytical meaning

Northbridge's hash index can answer “what quantity does the current inventory
view contain?” A list can hold an event batch. Pandas can aggregate shipments by
warehouse, and a sorted index can expose reorder ranges. None of these choices
settles what “available,” “fulfilled,” “on time,” or “utilization” means.

The analytical record needs source, transformation, semantic owner, time
boundary, freshness, permitted use, and quality evidence. An operational index
may be rebuilt from durable records; a report must still identify which version
and definition produced its answer.

## Plain-language model: the working counter and the health record

An operational index is like a counter arranged for the next order. An
analytical product is more like a health record: it must preserve where the
observations came from, when they were valid, how they were interpreted, and
which decisions they are fit to support. Copying the counter into a dataframe
does not create trustworthy history.

```text
operational records + durable events -> governed, versioned transformation
                                     -> data product -> report or AI input
```

A Pandas-style group-by can calculate utilization quickly. The architecture
must still govern the numerator, denominator, exclusions, null handling,
event-time window, late arrivals, and freshness. An overnight aggregate should
not become the transactional source for live reservations merely because it is
easy to query.

| Representation | Meaning question |
| --- | --- |
| Hash index | Is this current state authoritative, or only a rebuildable projection? |
| Event list/batch | Which occurrences and time boundaries are included? |
| Pandas aggregate | Which definition, cohort, null rule, and freshness window apply? |
| Sorted capacity view | Which capacity and location semantics justify the range? |

## Transfer artifact: metric meaning and permitted-use card

| Decision | Your answer |
| --- | --- |
| Metric and decision it supports | |
| Operational sources and durable events | |
| Numerator, denominator, exclusions, and null rule | |
| Event-time and freshness boundary | |
| Transformation and dataset version | |
| Semantic owner and correction path | |
| Permitted and prohibited uses | |

## AI-amplified transfer to other systems

AI tools can generate candidate structures, implementation code, tests, and
diagrams for many domains. The architect supplies the governing decisions the
generated machinery must preserve.

| Transfer case | AI can accelerate | Decision the structure cannot settle |
| --- | --- | --- |
| Search-engine indexing | Crawlers, inverted indexes, ranking code, query tests | Content authority, freshness, deletion, ranking policy, and evidence |
| Social-media platforms | Social graphs, feeds, queues, moderation classifiers | Consent, identity, amplification limits, appeal, and causal responsibility |
| Blockchain systems | Transaction parsing, Merkle proofs, graph analysis, contract tests | Signing authority, finality assumptions, off-chain governance, and reversal limits |
| Recommendation systems | Feature pipelines, candidate retrieval, ranking, evaluation | Permitted inputs, objective, fairness, explanation, and user control |
| Online food delivery | Route graphs, order queues, dispatch heaps, ETA models | Order and payment authority, worker custody, retry safety, refunds, and recovery |

The lesson is not that AI removes architecture work. It moves practitioners up
a level: generated machinery arrives sooner, so meaning, authority, failure,
and evidence must become explicit sooner.

> **Why we did not choose every structure**
>
> Autocomplete systems help predict partial search terms, but they are not
> needed for core inventory and order operations. Huffman coding compresses
> data, but it does not establish meaning, freshness, provenance, utilization,
> or fitness for use. Choose a structure because the problem requires it.
