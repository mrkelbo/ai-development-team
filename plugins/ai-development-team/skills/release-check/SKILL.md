---
name: release-check
description: "Prepare and gate a safe application release, including populated-data migrations, supported deployment mechanisms and honest signoff."
---
# Release readiness procedure

Do not auto-deploy. Treat package preparation, QA approval, Coordinator acceptance and actual production action as four distinct states.

- Establish exact change IDs, target app profile, installed/target versions, affected build units, deploy method, customer/company scope, authorized environment and data migrations.
- Integration/Release verifies dependency/contract compatibility, builds/releases only necessary units, locks versions and assembles release manifest/release notes.
- Data supplies schema upgrade plan, populated-data test and integrity evidence where applicable. Security reviews changed auth/tenant effects. Platform/Ops supplies health, backup+restore readiness, staged deployment and operator instructions.
- QA runs acceptance, regression, permissions and upgrade tests and documents commands/results. A missing test is NOT_TESTED, not PASS.
- Coordinator checks required gates and records explicit human approval for production, destructive work or special access. Missing approvals BLOCK release.
- Supply roll-forward/rollback handling (including when database rollback is unsafe), smoke tests, telemetry and stop criteria. Track post-deployment verification and close only when observed.

Return a release checklist with PASS / FAIL / BLOCKED / NOT_TESTED per required gate and precise evidence paths.
