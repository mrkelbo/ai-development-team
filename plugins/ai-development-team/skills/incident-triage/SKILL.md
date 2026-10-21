---
name: incident-triage
description: "Investigate an application failure, deployment incident or regression by assigning the proper specialist and preserving evidence."
---
# Diagnose an incident or regression

1. Coordinator captures symptom, environment, version, scope of affected users/companies, timing, business impact and what changed. Avoid assuming root cause from one error log.
2. Platform/Ops gathers read-only health/logs/config evidence; QA obtains safe reproduction; Architect traces boundary; Security handles possible breach; Data handles integrity/recovery; Business Logic/Frontend/Admin own code defects in their modules.
3. Start with non-destructive diagnosis. Do not run live migrations, delete caches indiscriminately, reset databases or expose secrets. Distinguish mitigation from corrective fix.
4. Assign an accountable owner; every uncovered task is Coordinator-owned until reassigned. Record hypotheses, evidence, excluded causes, reproduction and severity.
5. Prepare minimal fix or safe mitigation, targeted tests plus regression, deployment plan and monitoring checks. Follow approval boundaries for production.
6. Update root-cause/runbook/docs and incident handoff, including unresolved uncertainties and company/tenant exposure assessment when appropriate.
