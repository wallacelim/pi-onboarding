# Module 3.3: ClickHouse for Metrics

Estimated time

- 2 days

Purpose

- Understand how ClickHouse stores and serves high-volume metrics.

Learning goals

- Understand columnar storage and MergeTree engines.
- Design partitions, primary keys, and TTLs for metrics.
- Understand small-insert pitfalls and batching strategies.
- Understand the Postgres-on-ClickHouse compatibility layer.

Core topics

- MergeTree schema design.
- Materialized views for rollups.
- High-ingestion patterns and compaction.
- Query design for dashboards.

Exercises

- Install ClickHouse in a cluster or local environment.
- Create a metrics table and ingest millions of rows.
- Measure query latency under load.
- Experiment with partitioning and primary keys.

Deliverables

- A metrics schema for training metrics with clear keys and TTL.
- A query pack for common training observability questions.
- Notes on performance and ingestion tradeoffs.

Mastery checks

- You can explain why batching matters for ClickHouse.
- You can design a schema that supports fast time-range queries.
- You can reason about when to use materialized views.

## Resources

- [ ] [ClickHouse OSS quick start](https://clickhouse.com/docs/getting-started/quick-start/oss) — Local install, first table, and initial queries.
- [ ] [ClickHouse Cloud quick start](https://clickhouse.com/docs/getting-started/quick-start/cloud) — Managed service setup and first queries.
- [ ] [Choosing a Primary Key](https://clickhouse.com/docs/best-practices/choosing-a-primary-key) — Ordering key choices that drive query performance.
- [ ] [Use Materialized Views](https://clickhouse.com/docs/best-practices/use-materialized-views) — Rollups and pre-aggregation patterns.
- [ ] [ClickHouse Operator overview](https://clickhouse.com/docs/clickhouse-operator/overview) — Kubernetes deployment path for ClickHouse.
