# Module 3.1: OTEL Python SDK Deep Dive

Estimated time

- 3 to 4 days

Purpose

- Build expert-level intuition for OTEL metrics and the Python SDK internals.

Learning goals

- Understand counters, gauges, and histograms in OTEL.
- Understand cumulative vs delta and incremental gauges.
- Understand exporter behavior, batching, and context propagation.
- Understand performance, memory, and thread-safety implications in Python.

Core topics

- SDK initialization and lifecycle.
- Exporter concurrency and blocking behavior.
- Batching, flush cycles, and backpressure.
- GIL interactions and async behavior.
- Failure modes related to high-frequency instrumentation.

Exercises

- Write a Python training-like loop with high-frequency metrics.
- Compare OTLP gRPC vs HTTP exporters under load.
- Profile memory growth with frequent histogram updates.
- Simulate exporter backpressure and observe effects.

Deliverables

- A short report on SDK behavior under load.
- A hypothesis list for hangs and segfaults in training.
- A recommended default OTEL configuration for training jobs.

Mastery checks

- You can explain where blocking can occur in the SDK.
- You can explain how batching affects memory and latency.
- You can propose mitigations for segfaults and hangs.

## Resources

- [ ] [Getting Started (Python)](https://opentelemetry.io/docs/languages/python/getting-started/) — Quick setup for traces, metrics, and logs in Python.
- [ ] [Manual Instrumentation (Python)](https://opentelemetry.io/docs/languages/python/instrumentation/) — Core API/SDK usage for custom metrics.
- [ ] [Python Exporters](https://opentelemetry.io/docs/languages/python/exporters/) — Exporter setup and OTLP guidance.
- [ ] [OTLP Specification](https://opentelemetry.io/docs/specs/otlp/) — Protocol details for OTLP export.
- [ ] [Metrics API Spec](https://opentelemetry.io/docs/specs/otel/metrics/api/) — Instrument semantics and API contracts.
