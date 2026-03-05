# Module 3.2: OTEL Collector Pipelines

Estimated time

- 2 days

Purpose

- Build reliable OTEL collector pipelines for high-throughput metrics.

Learning goals

- Configure receivers, processors, and exporters.
- Understand batching and queueing in the collector.
- Deploy collectors in Kubernetes and debug them.

Core topics

- Pipeline configuration and component roles.
- Resource attributes and metric labels.
- Load testing and backpressure handling.
- Collector observability and troubleshooting.

Exercises

- Deploy an OTEL collector in a cluster.
- Configure a pipeline to export to ClickHouse.
- Stress test high-frequency metrics and observe collector behavior.
- Tune batching and queue sizes to stabilize throughput.

Deliverables

- A reference collector config for training metrics.
- Notes on pipeline bottlenecks and mitigation strategies.
- A troubleshooting checklist for collector issues.

Mastery checks

- You can pinpoint where metrics drop under load.
- You can tune collector settings for throughput and memory.
- You can explain how collector config choices affect latency.

## Resources

- [ ] [Collector overview](https://opentelemetry.io/docs/collector/) — Architecture, objectives, and component model.
- [ ] [Collector configuration](https://opentelemetry.io/docs/collector/configuration/) — Receivers, processors, exporters, and pipeline wiring.
- [ ] [Install the Collector with Kubernetes](https://opentelemetry.io/docs/collector/install/kubernetes/) — Reference DaemonSet + gateway deployment pattern.
- [ ] [OpenTelemetry Collector and Kubernetes](https://opentelemetry.io/docs/platforms/kubernetes/collector/) — Kubernetes-specific deployment and scaling guidance.

## Further reading

- [Collector component registry](https://opentelemetry.io/ecosystem/registry/?component=exporter&language=collector) — Explore available exporters and components.
