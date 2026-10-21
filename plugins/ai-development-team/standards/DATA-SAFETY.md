# Data protection and migration standard

## Production rules

- Routine feature deployment **never requires reset, drop, truncation, bulk delete or re-seeding** of existing production data.
- Treat existing production databases, user documents, attachments, config and local desktop stores as durable assets. Use a migration framework appropriate to the selected stack.
- Each migration: unique immutable ID; preconditions; lock/performance estimate; transaction/error handling; idempotency where relevant; backfill verification; rollout order; recovery and restore plan.
- Prefer expand → backfill → coexist → switch consumers → contract after a measured compatibility window.
- Never edit a migration already applied to a shared environment. Never assume undoing a schema change restores deleted data; plan roll-forward.
- Validate upgrades using sanitized populated copies with integrity comparisons, company isolation checks, historical business invariants and realistic schema versions.
- Test and document restore, including files and secrets/config dependencies; backup existence alone is insufficient.
- Build repositories/data-access interfaces that encapsulate persistence semantics; never expose a generic caller-controlled SQL endpoint.

## Dangerous operations require an approved change

Drop/truncate; broad deletion; mass rewrite; disabling constraints; exporting live private data; changing storage encryption; irreversible transformation; pruning backups; overwriting a desktop data file. Agent instructions alone cannot protect production: isolate credentials, use permission policy, code reviews, CI gates and human authorization.
