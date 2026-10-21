# Risk-proportionate QA and release gates

| Risk tier | Examples | Minimum review / verification |
| --- | --- | --- |
| LOW | Visual copy, non-structural styling | Local build/lint, targeted UI check, docs note when relevant |
| MEDIUM | UI flows, internal API additions, feature rules | Unit/integration tests, contract compatibility, relevant role tests, independent QA |
| HIGH | Auth, multi-company access, billing, migrations, exports, workers | Architect/Security/Data review as applicable; negative role tests; populated-data upgrade regression; QA and release dry-run |
| CRITICAL | Destructive data/keys, live production permission changes, irreversible migrations | Explicit human approval, backup and restore validation, operator runbook, planned staged rollout, monitoring, manual final authorization |

Always refuse to report PASS for checks not run. Document limitations honestly. Security/QA are not substituted by a model's assertion that code looks good.
