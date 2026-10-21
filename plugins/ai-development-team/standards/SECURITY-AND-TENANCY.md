# Security, identity, tenancy and access standard

## Universal distinction

- **Platform administrator:** approved control-plane authority, not blanket read access to all tenant records.
- **Platform technician:** assigned-company support access, least-privileged, auditable and revocable.
- **Platform user:** platform identity with permissions expressly assigned, no implicit admin privileges.
- **Company administrator:** administration of their company's delegated functions only.
- **Company personnel:** project-specific company membership, role and resource grants.
- The same individual can hold different memberships in different companies. Company identification is mandatory even for dedicated installations.

## Enforcement

Resolve identity, active company, memberships, explicit support assignments, permission grants and resource ownership on the trusted side; do not trust headers or frontend-provided company identifiers without verifying. Validate at authorization decisions for API routes, repositories, object storage, report exports, jobs, caches, search, events and audit views. Avoid resource existence leakage. Use least-privilege database/service identities, secret managers, safe session handling and audited privilege changes.

## Project-dependent choices

Identity provider, local email/password vs OAuth/OIDC/SSO, shared vs separate databases, role vocabulary, support approval workflow, enterprise policies and retention requirements. Never hardcode these choices in the reusable agent team.

## Required test cases

Cross-company object access; assigned vs unassigned platform technician; scoped platform admin operations; company-admin attempt to change other tenants; access after role revocation; company switch; export/report/worker and cache isolation; audit records and sensitive data redaction.
