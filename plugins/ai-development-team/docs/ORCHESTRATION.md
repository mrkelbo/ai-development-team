# Coordinator operating procedure

**This is a procedural design implemented through prompts/skills and Claude Code's subagent delegation. It is not a continuously running scheduler, centralized service, or a guarantee that a particular subagent will be invoked without a delegation instruction.**

## Invocation

Use `claude --agent ai-development-team:coordinator` to launch the plugin's Coordinator as the main session, or mention `@ai-development-team:coordinator` in a regular session and select it from the agent picker. From any Claude session, `/ai-development-team:implement-change` provides a reusable workflow. Slash skills execute as task instructions; agent names execute in separate contexts.

## Core loop

1. Coordinator scopes request and inspects existing code and `CLAUDE.md`.
2. Coordinator records impact and selected specialists with one accountable owner per work item. Orphan task → nearest qualified owner; genuinely unknown → Coordinator triage with reviewer and user escalation if needed.
3. Architect plans interface impact; Security/Data review relevant boundaries.
4. Specialists change disjoint modules or work sequentially when contracts aren't finalized. Each updates relevant tests and docs.
5. Integration assembles. QA independently verifies. Failed acceptance → defect to accountable specialist and review/retest.
6. Coordinator accepts when required evidence passes. Production actions still require authorized person and appropriate environment controls.

## Verified execution, not roleplay

The intended operating mode is the Coordinator started **as the main Claude Code agent** with `--agent`. It has the `Agent` tool to invoke real named subagents. An assignment list is not evidence of invocation. Track specialist statuses **PLANNED / RUNNING / COMPLETED / FAILED / NOT_RUN**; quote actual test commands/results or mark NOT_TESTED. A Coordinator-generated QA checklist is not an independent QA verdict. If the `Agent` tool or a named agent cannot be loaded, disclose the missing review rather than declaring it complete. A project may optionally integrate CI and branch-protection gates; this plugin does not install them in target repositories.

The Coordinator retains ownership of all orphan work, chooses the closest specialist and returns any scope-boundary work to that specialist. User-authorized scope, not agent availability, determines when work may be closed.

### Skill-loading compatibility

Specialists request preloading of `ai-development-team:core-standards`. This is supported by the current subagent frontmatter schema but should be behavior-tested for the installed Claude Code version. **When the Coordinator is run as the main session with `--agent`, skill preloading may not run**; the key constraints are therefore also included in each agent's own operating contract and the Coordinator may invoke `/ai-development-team:core-standards` manually. Verify with an actual session rather than relying on YAML syntax alone.

## Choosing the team

- A pure UI styling change: usually Frontend + targeted QA, no Data migration.
- A new field in a populated system: Architect, Data, Business Logic, Frontend/Admin as affected, QA, Integration.
- New cross-company tech support permission: Security, Architect, Business Logic, Admin Console, QA; Data if schema changes.
- Install/backup problem: Platform/Ops, Data for data safety, QA for restore evidence.

## Technical limitations

Subagents do not automatically share one continuous context with the main conversation. Pass requirement IDs, existing decisions and concrete file references with each delegation. Delegations may be sequential or parallel; parallel file modifications need worktrees/branches and deliberate merge resolution. Plugins alone do not establish CI, production permissions, persistent orchestration, or access to cloud Claude sessions.
