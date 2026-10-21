---
name: agent-status
description: "Review agent responsibilities, uncovered work, blockers, requirement traceability and documentation/test completeness in an active development project."
---
# Team and change status audit

Ask Coordinator to inspect existing backlog/work orders, architecture/requirements, agent handoffs, QA verdicts, release docs, and untracked TODOs.

Build a compact matrix: task/change ID; accountable agent; reviewer; state; blocked dependency; files/contracts touched; test evidence; docs updated; next action. Specifically flag ownerless tasks, duplicate ownership, implied tenant permissions, unplanned schema changes, untested populated-data upgrades and releases called complete without real test evidence.

The Coordinator MUST assign each ownerless item to the closest qualified agent, or own triage with explicit next step; don't silently drop it. Separate blocked, deferred by user and rejected scope.
