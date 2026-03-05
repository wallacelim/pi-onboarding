# Module 5.1: Doppler Secrets Management

Estimated time

- 1 day

Purpose

- Standardize how services access secrets securely and consistently.

Learning goals

- Understand the secrets lifecycle from creation to rotation.
- Understand injection patterns for Kubernetes workloads.
- Identify common secret hygiene failures.

Core topics

- Secret scoping and environment separation.
- Runtime injection patterns and auditability.
- Rotation and revocation workflows.

Exercises

- Document a standard secrets template for a new microservice.
- Define a checklist for secret rotation and access review.
- Map secrets usage to deployment manifests.

Deliverables

- A secrets management checklist for new services.
- A template for secret naming and scoping.
- A short threat model for secret leakage.

Mastery checks

- You can audit a service for secret hygiene.
- You can explain how to rotate secrets with minimal downtime.
- You can explain how Doppler fits into GitOps workflows.

## Resources

- [ ] [Secrets](https://docs.doppler.com/docs/secrets) — Core concepts and how secrets behave in Doppler.
- [ ] [Secrets Setup Guide](https://docs.doppler.com/docs/secrets-setup-guide) — Create configs, add secrets, and wire environments.
- [ ] [Secrets Access Guide](https://docs.doppler.com/docs/accessing-secrets) — Injection, mounting, and access patterns.
- [ ] [Rotated Secrets](https://docs.doppler.com/docs/secrets-rotation) — Rotation workflows and options.
- [ ] [Doppler Kubernetes Operator](https://docs.doppler.com/docs/kubernetes-operator) — Sync secrets into clusters via the operator.
