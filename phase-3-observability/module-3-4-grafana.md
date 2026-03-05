# Module 3.4: Grafana for SQL Metrics

Estimated time

- 1 day

Purpose

- Build clear and actionable dashboards on top of ClickHouse.

Learning goals

- Configure ClickHouse as a data source.
- Use SQL panels and variables effectively.
- Create alerting rules and provisioning configs.

Core topics

- Dashboard organization and naming conventions.
- Variables for job ids, clusters, and runs.
- Alerts and thresholds for training reliability.
- Provisioning dashboards as code.

Exercises

- Connect Grafana to ClickHouse.
- Build dashboards for memory usage and training histograms.
- Export dashboards as code and re-import them.

Deliverables

- A dashboard spec with required panels and queries.
- A provisioning example for dashboards.
- An alerting checklist for training failures.

Mastery checks

- You can design a dashboard that answers "what ran out of memory" quickly.
- You can explain how a panel query maps to the schema.
- You can create variables that make dashboards reusable.

## Resources

- [ ] [Grafana Getting Started](https://grafana.com/docs/grafana/latest/fundamentals/getting-started/) — Core concepts and first dashboard workflow.
- [ ] [Build your first dashboard](https://grafana.com/docs/grafana/latest/fundamentals/getting-started/build-first-dashboard/) — Step-by-step dashboard creation reference.
- [ ] [Grafana provisioning docs](https://grafana.com/docs/grafana/latest/administration/provisioning/) — Dashboards as code for GitOps workflows.
- [ ] [Grafana ClickHouse data source plugin](https://grafana.com/grafana/plugins/grafana-clickhouse-datasource/) — Official ClickHouse data source for Grafana.
