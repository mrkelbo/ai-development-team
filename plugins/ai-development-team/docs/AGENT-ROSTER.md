# Agent team — roles, ownership and defaults

| Agent | Primary ownership | Review partners |
|---|---|---|
| coordinator | Requirements, work assignment, orphan pickup, acceptance | All relevant specialists |
| architect | Architecture, contracts, compatibility | Security, Data, Integration |
| security | Identity, platform/company access, tenant security | Architect, QA |
| data | Schema, persistence, integrity and migrations | Architect, Security, QA |
| business-logic | Domain rules, workflows, core services | Architect, Data, Security |
| frontend | End-user interfaces, desktop/web UX, reports | Business Logic, QA |
| admin-console | Platform/company operator UI and management workflows | Security, Business Logic, QA |
| platform-ops | Environments, installers, containers, backups, monitoring | Data, Integration, Security |
| integration-release | Assemble/build releases, versioning and deployment package | Platform/Ops, QA, Architect |
| qa-testing | Independent requirement/regression/security-adjacent/upgrade verification | All relevant owners |

One accountable owner per work item. Cross-agent contributors are permitted. The Coordinator catches uncovered responsibilities and assigns the closest qualified agent, or owns triage until one is found. No one owns generic “do everything” coding by default.
