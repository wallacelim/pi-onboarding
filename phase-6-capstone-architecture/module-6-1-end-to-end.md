# Module 6.1: End-to-End Stack Rebuild

Estimated time

- 3 to 5 days

Purpose

- Rebuild the ML infra stack end-to-end to prove functional understanding.

Learning goals

- Integrate Terraform, GKE, Flux, Helm, OTEL, ClickHouse, Grafana, and Anyscale.
- Validate metric flow from a Ray job to dashboards.

Core topics

- End-to-end system wiring and dependencies.
- Metrics validation and instrumentation checks.
- Operational ownership and recovery steps.

Exercises

- Provision GKE with Terraform.
- Install Flux and reconcile manifests.
- Deploy ClickHouse, OTEL collector, and Grafana.
- Deploy Anyscale operator and run a Ray job.
- Verify metrics flow into ClickHouse and appear in Grafana.

Deliverables

- A build plan with step-by-step verification checks.
- A validation checklist for metrics and dashboards.
- A final system diagram with resolved endpoints.

Mastery checks

- You can explain each dependency in the stack and why it exists.
- You can debug missing metrics anywhere in the pipeline.
- You can reproduce the stack from scratch reliably.
