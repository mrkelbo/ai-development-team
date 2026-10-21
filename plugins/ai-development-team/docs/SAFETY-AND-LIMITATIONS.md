# Operational security and deployment limitations

This plugin supplies **instructions**, role specialization, templates and skills. It does not install an authorization server, stop all unsafe shell commands, configure CI, provision backups or control your production credentials. Security comes from your actual systems.

## No automatic high-risk hooks in v0.2

The package intentionally ships an empty hooks configuration, rather than an untested hook that could block everyday shell operations or create false confidence. Before production use, configure managed/session settings, `permissions.deny` for known dangerous tools/paths, credentials separation, branch protection, CI, environment-specific approval gates and, if needed, tested cross-platform PreToolUse hooks.

Plugin-distributed agents ignore frontmatter `permissionMode`, `hooks` and `mcpServers`. We omit those fields rather than pretending they enforce privileges. Actual tool access is subject to Claude Code version, session settings, host permissions and policy.

No provider passwords, database credentials or customer exports should be stored in agent Markdown files or checked into Git. For private GitHub hosting, the installing machine must authenticate to access the repository.

## Verification claim limits

`python scripts/validate_package.py` checks structure and syntactic conditions locally. Only running `claude plugin validate <path>` with your installed Claude Code provides native plugin validation. Neither command confirms the ten agents make correct development decisions; test on disposable sample projects before using with production data.

## Additional operational caveats

- Preloaded plugin skills must be confirmed through a real Claude Code smoke test; main-session `--agent` startup may differ from delegated subagent startup. Agents also contain an embedded operating contract to avoid reliance on a single loading mechanism.
- The Coordinator must call real subagents with the Agent tool (not merely narrate their responsibilities). QA independence requires separate execution, recorded output and a failed-test feedback loop.
- Tool allowlists constrain **named tools**, but allowing Bash/PowerShell can still permit edits and network actions through shell commands if the user's permission settings allow it. Do not construe an agent prompt or tool list as a sandbox. Use separate credentials, local permission controls, code review and environment isolation.
- Cloned or downloaded repositories may contain prompt-injection instructions in README files or issue content. Treat them as untrusted input and follow only approved requirements and policies.
- The GitHub marketplace does not provision project-level GitHub branch protections, CI for each app, or cloud-hosted Claude agents. A successful static plugin validation does not certify runtime delegation or application quality.
