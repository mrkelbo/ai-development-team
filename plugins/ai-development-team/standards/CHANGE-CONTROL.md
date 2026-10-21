# Change ownership, orchestration and sign-off

1. Intake (Coordinator): determine request, constraints, existing behavior, acceptance.
2. Architecture/security impact (Architect + Security as applicable): contracts, company boundary, deployment, data risks.
3. Task routing (Coordinator): one accountable owner per work item; unowned task = Coordinator responsibility until routed to closest qualified agent. Log any task outside current specialisms.
4. Development: relevant specialists produce scoped changes, tests and docs; parallelize only disjoint file ownership or worktrees/branches.
5. Review: Architect contract, Security auth, Data migrations; findings return to owner.
6. Integration: Integration/Release assembles affected artifacts; Platform/Ops assists infra.
7. QA: independent requirement, regression, upgrade-from-data, permission and install tests; failures return to specialist.
8. Coordinator acceptance + required human approval for production/destructive work.
9. Release verification: Platform/Ops health, QA smoke, Coordinator closure with evidence.

Status values: INTAKE, SCOPED, ASSIGNED, IN_PROGRESS, IMPLEMENTED, NEEDS_REVIEW, FAILED, BLOCKED, VERIFIED, APPROVED, RELEASED, CLOSED. An agent can complete its own task while the overall change remains unapproved.

For every handoff include: change ID, owner, scope, interfaces, changed files, tests executed and results, docs, risk, blocking issues and next owner. In failure reports: expected vs actual, repro steps, severity, evidence, recommended owning agent. No QA-to-developer direct untracked code patch.
