---
name: implement-change
description: "Coordinate an incremental feature, defect fix or refactor across the appropriate specialists without unnecessary redeployment or data loss."
---
# Implement a scoped change

1. Have Coordinator inspect current project and identify whether the request is a bug, enhancement, workflow change, admin feature, deployment matter, cross-cutting refactor or investigation.
2. Write/change an appropriately sized work order: change ID, existing behavior, expected outcome, measurable acceptance criteria, non-goals, known interfaces/data, risk tier, environments, authorization boundaries.
3. **Actually delegate using the Agent tool when available, and capture specialist results** rather than role-playing reviews or writing an assignment list. Ask Architect for contracts/impact when module boundaries change; Security for identity/company/secret changes; Data for schema/migrations; route implementation to domain owner(s). Avoid concurrent writes to the same files; use ordered dependencies or worktrees where feasible.
4. Each owner modifies assigned modules only; updates relevant tests and docs; returns a structured handoff, including remaining risk and untested cases. New work outside scope returns to Coordinator for assignment; Coordinator explicitly owns every gap.
5. Have Integration/Release assemble the **affected** deliverables; QA independently test requirements, regression and populated-database upgrade/permissions if applicable.
6. Mark every required specialist NOT_RUN until a corresponding agent has actually returned evidence. If unavailable, mark the gate BLOCKED/NEEDS_REVIEW, never PASS.
7. Failed check → structured defect → nearest accountable owner → fix → review → QA rerun. No silent QA code patch.
8. Coordinator verifies acceptance and reports changed/unmodified modules, deployment need, unresolved risks, approval prerequisites, and status. Never equate local build success with production deployment.

If only one simple module is affected, keep this lightweight; do not manufacture nine ceremonial meetings.
