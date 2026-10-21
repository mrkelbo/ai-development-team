# Engineering and architecture standards

## Start with the application profile

Define app type, supported OS/browser, language/framework, repo layout, company model, connectivity/offline expectations, data store, installer/hosting, rollback capability, versions, tests, source control and observability. A Python web app is a web app with Python-specific runtime/build/migration/worker needs—not a new agent team.

## Design rules

- Domain logic belongs in the trusted core; UI and admin invoke contract-defined operations; persistence behind repositories. When local desktop monolith, these can be module boundaries in one executable rather than network services.
- Reject unnecessary microservices. Change only impacted components **where the actual build/deployment boundary permits**. A desktop package may need rebuilding the executable to ship a UI fix.
- Keep secrets out of repositories. Use dependency lockfiles, linters/formatters, relevant test automation, explicit configuration validation and a well-documented local development path.
- Avoid hidden mutable globals, hard-coded company filtering in UI, circular module dependencies, public breaking changes without transition, and unknown-version dependencies.
- Document ADRs for material irreversible decisions; run version compatibility checks before changing contracts.

## Operational diagnostics

Structured contextual logs without PII/secrets, actionable errors, health checks where applicable, task/job tracing and a runbook for common failures. No speculative hot changes to production.
