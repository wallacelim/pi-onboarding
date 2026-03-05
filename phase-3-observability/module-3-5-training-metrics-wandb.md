# Module 3.5: Training Metrics and W&B Integration

Estimated time

- 1 to 2 days

Purpose

- Understand existing training metrics practices and design a better OTEL-based path.

Learning goals

- Understand W&B metric export cadence and limitations.
- Design an OTEL-based replacement with per-step granularity.
- Propose a developer-friendly metrics wrapper for researchers.

Core topics

- W&B metric semantics and export flow.
- OTEL mapping for training metrics.
- Sampling, throttling, and storage cost tradeoffs.

Exercises

- Compare W&B export frequency to training step requirements.
- Design a metrics wrapper API with sensible defaults.
- Propose a migration path that avoids breaking existing workflows.

Deliverables

- A training metrics taxonomy and schema.
- A proposal for W&B and OTEL coexistence or replacement.
- A metrics ingestion budget with sampling strategy.

Mastery checks

- You can explain how to get per-step visibility without destabilizing training.
- You can defend the cost and performance tradeoffs of your proposal.
- You can show how researchers would instrument metrics with minimal friction.

## Resources

- [ ] [W&B Models Quickstart](https://docs.wandb.ai/models/quickstart) — First run with an end-to-end ML experiment.
- [ ] [Get Started with W&B Models](https://docs.wandb.ai/models/models_quickstart) — Guided walkthrough of the Models workflow.
