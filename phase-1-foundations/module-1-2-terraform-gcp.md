# Module 1.2: Terraform and GCP Fundamentals

Estimated time

- 2 days

Purpose

- Gain deep intuition for infrastructure as code and GCP provisioning.

Prerequisites

- Basic Kubernetes concepts (pods, services, deployments) from Module 1.1.

Learning goals

- Understand Terraform providers, resources, modules, state, and plan vs apply.
- Understand how GCP APIs, VPCs, and GKE clusters are provisioned.
- Understand drift, idempotency, and state corruption risks.

Core topics

- Terraform workflow and remote state design.
- Dependency graph and implicit ordering.
- GCP APIs, IAM, VPCs, and GKE basics.

Exercises

- Create a fresh GCP project and enable required APIs.
- Write Terraform to create a VPC and a GKE cluster.
- Apply, then destroy, then recreate the cluster.
- Modify a node pool size and observe the plan and apply differences.
- Simulate a drift scenario and reconcile it with Terraform.

Deliverables

- A minimal Terraform module interface for GKE provisioning.
- Notes on state behavior and drift handling.
- A checklist for safe apply and destroy workflows.

Mastery checks

- You can explain what is stored in state and why it matters.
- You can predict the change set for common cluster modifications.
- You can recover from a drifted resource without manual guesswork.

## Resources

- [x] [Get Started with Google Cloud](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started) — HashiCorp’s step-by-step Terraform + GCP tutorial.
- [x] [Install and configure Terraform for Google Cloud](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) — GCP-specific install, auth, and environment setup.
- [x] [Quickstart: Create a VM instance using Terraform](https://cloud.google.com/docs/terraform/create-vm-instance) — First end-to-end resource creation on GCP.
- [x] [Quickstart: Create a GKE cluster and deploy a workload using Terraform](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/create-cluster-using-terraform) — Terraform flow that matches the GKE lab.
