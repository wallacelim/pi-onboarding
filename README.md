# ML Infrastructure Spinup Guide

This guide is designed for an engineer ramping up to expert-level ML infrastructure competence, with a strong focus on observability, GKE GitOps, and Ray/Anyscale.

Important constraint

- This guide is lab-first: you will stand up a reference stack from scratch and use it as the learning substrate.
- Every module produces reusable artifacts.

How to use this guide

- Work phase-by-phase from top to bottom.
- Each module has concrete deliverables and mastery checks.
- Prefer hands-on learning and failure-first experiments.
- Treat each deliverable as a reusable artifact you can bring into the role.

Ordering rationale

- Learn Kubernetes mechanics first so every later step has a concrete substrate.
- Learn Terraform/GCP next so you can provision GKE and understand the control plane you will own.
- Add GitOps workflows once you can reason about Kubernetes objects and cluster lifecycle.
- Build observability next because it is the highest-leverage ownership area and requires a working cluster.
- Then learn distributed compute (Ray/Anyscale) which plugs into the same cluster and observability stack.
- Finish with control-plane edges, reliability playbooks, and the end-to-end capstone.

Syllabus

- [Phase 1: Kubernetes and IaC Foundations](phase-1-foundations/README.md)
- [Phase 2: GitOps and Cluster Management](phase-2-gitops/README.md)
- [Phase 3: Observability Mastery](phase-3-observability/README.md)
- [Phase 4: Distributed Compute](phase-4-distributed-compute/README.md)
- [Phase 5: Control-Plane Edges](phase-5-control-plane-edges/README.md)
- [Phase 6: Capstone and Architecture](phase-6-capstone-architecture/README.md)

End state

- You can build and operate an ML infra stack end-to-end in a lab environment.
- You can debug training observability issues involving OTEL, ClickHouse, and Grafana.
- You can own Flux-based GitOps workflows and the Terraform GKE control plane.
- You can propose coherent infrastructure architecture improvements.
