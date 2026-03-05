# Module 1.1: GKE and Kubernetes Mechanics

Estimated time

- 2 days

Purpose

- Understand Kubernetes as a system, not just YAML.

Prerequisites

- A local cluster (kind or minikube) or a GKE cluster created via the quickstart.

Learning goals

- Understand workload primitives and their reconciliation behavior.
- Understand scheduling, resource requests, limits, taints, and node pools.
- Understand where logs live and how failures surface.

Core topics

- Pods, Deployments, StatefulSets, Jobs, DaemonSets, Services.
- ConfigMaps, Secrets, RBAC, CRDs, and controllers.
- Scheduling, autoscaling, and failure recovery.
- GKE specifics and node pools.
- K9s as a rapid operational interface.

Exercises

- Deploy a simple workload and scale it.
- Kill pods manually and observe reconciliation.
- Delete a node and observe rescheduling.
- Create an OOM scenario and observe failure signals.
- Use K9s to navigate resources and events.

Deliverables

- A reference sheet for K8s objects and when to use them.
- A short writeup explaining the reconciliation loop and scheduling path.
- A failure checklist for common K8s failure modes.

Mastery checks

- You can explain why a pod is Pending or CrashLooping.
- You can identify when to use a Deployment vs StatefulSet.
- You can trace a request from Service to pod.

## Resources

- [x] [Hello Minikube](https://kubernetes.io/docs/tutorials/hello-minikube/) — Run a sample app on a local cluster with `minikube`.
- [x] [Learn Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) — Guided walkthrough of core Kubernetes concepts and workflows.
- [x] [Quickstart: Create a cluster and deploy a workload](https://cloud.google.com/kubernetes-engine/docs/quickstarts/create-cluster) — Fastest path to a real GKE cluster and a sample workload.
- [x] [Quickstart: Deploy an app to a GKE cluster](https://cloud.google.com/kubernetes-engine/docs/deploy-app-cluster) — Deploy and expose a containerized web app.

## Further reading

- [GKE Learn](https://cloud.google.com/kubernetes-engine/docs/learn) — Curated next steps for production readiness and operations.
- [Kubernetes Tutorials](https://kubernetes.io/docs/tutorials/) — Official guided tutorials (including Kubernetes Basics and Hello Minikube) for core concepts and workflows.
