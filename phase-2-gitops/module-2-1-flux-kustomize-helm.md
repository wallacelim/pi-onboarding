# Module 2.1: Flux, Kustomize, and Helm

Estimated time

- 1 to 2 days

Purpose

- Gain operational ownership of GitOps workflows and environment overlays.

Learning goals

- Understand Flux controllers and reconciliation behavior.
- Use Kustomize overlays for environment differentiation.
- Manage Helm releases via Flux.

Core topics

- Flux sources, Kustomizations, and HelmReleases.
- Drift detection and rollback patterns.
- Kustomize patches and overlays.
- Helm chart values and lifecycle.

Exercises

- Install Flux in a test cluster.
- Create a Git repo layout for dev and prod overlays.
- Deploy a service via Kustomize and observe reconciliation.
- Delete a resource manually and observe Flux correction.
- Manage a Helm release through Flux and update values.

Deliverables

- A GitOps repo layout with overlays and conventions.
- A reconciliation flow diagram showing Git to cluster.
- A quickstart runbook for Flux troubleshooting.

Mastery checks

- You can explain how Flux decides what to apply and when.
- You can design overlays without duplicating manifests.
- You can perform a safe rollback with Git history.

## Resources

- [ ] [Get Started with Flux](https://fluxcd.io/flux/get-started/) — Bootstrap Flux and deploy a sample app GitOps-style.
- [ ] [Flux Kustomization](https://fluxcd.io/flux/components/kustomize/kustomizations/) — How Flux reconciles Kustomize overlays.
- [ ] [Flux HelmRelease](https://fluxcd.io/flux/components/helm/helmreleases/) — Declarative Helm releases via Flux.
- [ ] [Declarative Management of Kubernetes Objects Using Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization) — Core Kustomize workflow with `kubectl`.
- [ ] [Helm Quickstart Guide](https://helm.sh/docs/v3/intro/quickstart) — Install Helm and ship a first chart.
