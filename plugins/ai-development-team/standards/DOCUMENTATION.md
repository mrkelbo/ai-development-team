# Documentation ownership standard

Documentation is part of every assignment and must be maintained by the author of each change. Do not delegate documentation to an imaginary Documentation Agent. Prefer plain text in the application's existing version-controlled `docs/` tree.

| Agent | Required owned records |
| --- | --- |
| Coordinator | Requirements, ownership/backlog, accepted decisions, acceptance reports |
| Architect | ADRs, interface contracts, module/dependency maps |
| Security | Roles, permissions, scopes, threat model and audit flows |
| Data | Schema/data dictionary, migrations, integrity/restore notes |
| Business Logic | Domain behavior, state transitions, service interfaces, job behavior |
| Frontend | Design conventions, screens/routes, accessibility, interaction states |
| Admin Console | Management capabilities, authorization matrices and operator procedures |
| Platform/Ops | Setup, configuration, build/install, monitoring, backup and recovery |
| Integration/Release | Release manifest, deployment order, rollback and release notes |
| QA | Test plan/results, coverage, defects and verification evidence |

Maintain **what changed, why, where, how to operate/test/restore, and what remains unresolved**. Avoid duplicating secrets or generated binaries. If a change leaves docs untouched, explicitly explain why; do not mark a changed contract complete without updated docs.
