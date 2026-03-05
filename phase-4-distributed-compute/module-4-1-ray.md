# Module 4.1: Ray Core Concepts

Estimated time

- 2 to 3 days

Purpose

- Build a working mental model of Ray tasks, actors, and the object store.

Learning goals

- Understand task graphs, actors, and scheduling.
- Understand object store memory behavior and spillover.
- Understand fault tolerance and recovery behavior.

Core topics

- Ray head and worker nodes.
- Resource annotations and placement groups.
- Backpressure and autoscaling.
- Ray Data basics.

Exercises

- Run a local Ray cluster and create tasks and actors.
- Create a workload that stresses the object store.
- Kill a worker and observe recovery.
- Map Ray resource requests to Kubernetes resources.

Deliverables

- A Ray architecture summary with failure scenarios.
- A checklist for diagnosing slow or stuck Ray jobs.
- A minimal Ray job template with metrics hooks.

Mastery checks

- You can explain when to use tasks vs actors.
- You can trace where large objects live and how they move.
- You can predict how Ray will scale under load.

## Resources

- [ ] [Ray Core walkthrough](https://docs.ray.io/en/latest/ray-core/walkthrough.html) — Official introduction to tasks, actors, and objects.
- [ ] [Starting Ray](https://docs.ray.io/en/latest/ray-core/starting-ray.html) — Practical guidance on initializing Ray locally and on clusters.
