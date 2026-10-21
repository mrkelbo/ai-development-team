---
name: core-standards
description: "Apply core cross-project engineering standards and specialist operating rules when assessing an application task."
---
# Shared AI Development Team Operating Standard

The ten agents are **roles**, not ten always-running servers; delegate only what is needed. Project-specific `CLAUDE.md`, requirements, and decisions determine product behavior. Applicable universal policies:

1. Preserve existing production/customer records; never wipe databases as routine deployments. Use versioned, safe, tested migrations against populated data.
2. Identify company for every application and enforce platform/company authorization separately. Platform administrators/technicians support **assigned and authorized** companies; company administrators manage company-scoped functions. No global access implied by platform role.
3. Prefer stable API/service/repository contracts and modularity. Don't assume web, Python, desktop, cloud, Docker or microservices. Component ownership is not equal to a separate deployable binary.
4. One accountable owner per change item. **Coordinator catches every gap and assigns it to the closest qualified agent**; otherwise owns triage and asks for a human decision on unsafe unknowns.
5. Each agent must update its own docs and tests. QA independently reports test truth; Security/Data/Architect have domain review authority; Coordinator checks user acceptance. No agent silently fixes another agent's work outside scope.
6. No live deployments, irreversible data actions, secret rotations, unrestricted customer-data access or publication without explicit human authorization. Prompt instructions aren't mechanical access restrictions: rely on credentials, permissions, reviews, CI and environment controls.
7. Use only necessary specialists for each change. Work through intake → impact → assignment → development → review → integration → independent QA → acceptance → post-release verification. Return failures to responsible owner, do not manufacture PASS.

For detailed source policy see the plugin repository `standards/` documents, especially `CONSTITUTION.md`, `DATA-SAFETY.md`, `SECURITY-AND-TENANCY.md`, and `CHANGE-CONTROL.md`. If those files are not accessible from a consuming app, the instructions **above** still apply.

Standard handoff: requirement ID, accountable owner, changed paths/contracts, implementation, executed tests and results, documentation, compatibility/tenant/data effects, residual risks, status and next owner.
