---
name: start-project
description: "Kick off a new desktop, web, Python web, hybrid, mobile or other application with profile and ten-agent work allocation."
---
# Start a project with the development team

Follow shared standards and favor concise discovery over speculative stacks.

1. Ask the Coordinator to establish goal, users, problem, acceptance MVP, constraints and what is explicitly out-of-scope. Do not infer a proprietary product clone's undocumented functionality.
2. Inspect repo/current files if any; identify greenfield vs existing-data update. If existing, protect compatibility.
3. Define project profile: desktop/web/Python web/mobile/hybrid, OS/browser, languages/framework choice or shortlist, single vs multiple company deployment, mandatory company identity, platform/company role model, auth approach, local/cloud/offline behavior, database, deployment packaging, test/lint tools and documentation location.
4. Route architecture to Architect, company/security rules to Security, storage to Data, UI to Frontend/Admin as appropriate, operations to Platform/Ops. Tasks without clear owner remain Coordinator-owned and are assigned to nearest competent specialist.
5. Create `CLAUDE.md` and `docs/project-profile.yaml` from templates in this plugin, adapted to real requirements and existing conventions. If the plugin templates cannot be reached, reproduce their fields in concise markdown/YAML.
6. Create a minimally coupled module map, requirement/backlog, initial acceptance criteria, ADRs, initial risk register and early test plan. Do not start ten agents for no reason.
7. Tell the user the recommended profile and alternative(s) with tradeoffs, exact unknowns and next implementable tasks.

Deliver: project overview, environment/profile, role/tenant approach, module boundary, MVP and first change IDs, chosen owner/reviewer, expected tests and docs.
