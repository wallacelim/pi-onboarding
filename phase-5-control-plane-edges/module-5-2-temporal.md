# Module 5.2: Temporal Workflows

Estimated time

- 1 day

Purpose

- Build intuition for workflow orchestration and failure handling.

Learning goals

- Understand workflows, activities, retries, and idempotency.
- Understand signals, timers, and async coordination.
- Design robust workflows for long-running ML jobs.

Core topics

- Workflow lifecycle and execution history.
- Activity retries and compensation.
- Workflow versioning and backward compatibility.

Exercises

- Design a workflow for data prep, training, and evaluation.
- Add failure handling and compensation steps.
- Draft an observability plan for the workflow.

Deliverables

- A workflow design doc for a training pipeline.
- A failure handling map for key activities.
- A list of workflow observability metrics.

Mastery checks

- You can explain how Temporal ensures durability.
- You can handle long-running tasks without losing progress.
- You can evolve a workflow without breaking existing runs.

## Resources

- [ ] [Python SDK Quickstart](https://docs.temporal.io/develop/python/set-up-your-local-python) — Local dev setup and first workflow.
- [ ] [Temporal Workflows](https://docs.temporal.io/workflows) — Core workflow concepts and lifecycle.
- [ ] [Temporal Activities](https://docs.temporal.io/activities) — Activity semantics, retries, and idempotency.
