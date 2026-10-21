# Development notes (unpublished draft)

No public or tagged release has been created. This document tracks internal refinements before the first published release.

## Quality review — 2026-10-21

- Explicitly preload cross-project core standards where supported; provide fallback rules in agent definitions.
- Strengthen Coordinator delegation evidence and unassigned-task follow-through; prevent invented QA/security signoff.
- Improve QA reproducibility, tenant-scoped authorization review and handling of untrusted repository instructions.
- Add offline structural validation, CI and operator smoke-test scenarios.
- Leave dangerous hooks inactive and do not grant production privileges.

## Initial construction — 2026-10-21

- Define ten specialist agents, six reusable skills, shared engineering standards, templates and marketplace configuration.

**First official release:** choose a semantic version and Git tag only after native Claude Code validation and behavior tests pass.
