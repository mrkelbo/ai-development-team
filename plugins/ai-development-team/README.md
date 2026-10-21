# AI Development Team — Claude Code Plugin

**Status:** Initial unpublished draft (review candidate)  
**Purpose:** One reusable ten-agent engineering team for multiple unrelated software projects.  
**Supports:** desktop, web, Python web, hybrid, mobile, CLI and other project profiles.

## What's included

Ten specialist agents in `agents/`; five workflows plus shared policy skill in `skills/`; detailed cross-project standards, templates, operator documentation, and an initially empty hooks configuration. Every agent must document its work. Coordinator assigns work not covered by existing specialties to the closest qualified agent.

## Test locally before GitHub

From the **marketplace repository root**:

```bash
python scripts/validate_package.py
claude plugin validate ./plugins/ai-development-team
claude plugin validate .
claude --plugin-dir ./plugins/ai-development-team
```

Start a Coordinator-driven session directly from an actual application project (use an **absolute path** to the plugin directory):

```bash
claude --plugin-dir /absolute/path/to/AI-Development-Team-Marketplace/plugins/ai-development-team --agent ai-development-team:coordinator
```

On Windows, replace with the actual Windows path. You may need to reload/restart Claude Code after plugin edits.

## Install from the local marketplace (user scope)

From the marketplace repository root:

```bash
claude plugin marketplace add .
claude plugin install ai-development-team@ai-team-marketplace --scope user
claude plugin list
```

Open Claude Code from **the application project's own folder**, not from the plugin folder, when working on that application. Invoke `claude --agent ai-development-team:coordinator` or use `@` agent picker.

## Publish to your own private GitHub repository

1. Initialize Git for **this entire marketplace folder** and create a private GitHub repository under your own chosen owner/repo name. No repository or account is preconfigured here.
2. Push tested changes. After validation, select the first official version, add it to the plugin manifest, and create a matching Git tag. Increment the manifest version for later released updates.
3. On other authorized computers, authenticate GitHub, then run:

```bash
claude plugin marketplace add YOUR_GITHUB_OWNER/YOUR_REPO
claude plugin install ai-development-team@ai-team-marketplace --scope user
```

4. Optionally enable marketplace auto-update in Claude Code's `/plugin` UI after you trust the release channel. New GitHub commits alone are not a promise of immediate update. The installed version changes as Claude Code refreshes/distributes the marketplace and plugin according to its settings.

## Useful commands inside Claude Code

- `/ai-development-team:start-project` — initialize a new application's plan and profile.
- `/ai-development-team:implement-change` — route one feature/fix through appropriate agents.
- `/ai-development-team:release-check` — prepare a verified release plan.
- `/ai-development-team:incident-triage` — diagnose a defect or production incident safely.
- `/ai-development-team:agent-status` — audit owners, blockers and unassigned work.
- `/ai-development-team:core-standards` — load shared cross-project rules on demand.

The Coordinator is a plugin-scoped agent (`ai-development-team:coordinator`), NOT a background daemon. Ask the main session to delegate; use the `--agent` switch to run it as your primary agent.

## Project configuration is separate

Copy `templates/project/CLAUDE.md.template` into **each application's** own `CLAUDE.md` and adapt it. Put a filled-out `project-profile.yaml` under that application's `docs/`. Do **not** hardcode project-specific languages, ports, passwords, data models or customer details into this global plugin.

## Important limitations

These files have been structurally validated in the authoring environment. Claude Code itself is not installed there, so native validation and behavior testing must occur on your computer. `hooks/hooks.json` is deliberately empty pending tested enforcement. No actual production permission boundary is created by a text prompt. See `docs/SAFETY-AND-LIMITATIONS.md`.

## Before publishing or enabling automatic updates

1. Run `python scripts/validate_package.py` from the repository root. GitHub Actions runs this check on pushes and PRs.
2. Run `claude plugin validate .` and `claude plugin validate ./plugins/ai-development-team` using your installed Claude Code.
3. Start from a **disposable test project**, launch `claude --agent ai-development-team:coordinator`, and work through `scripts/test_scenarios.md`. Verify the Coordinator **actually invokes** the required specialist agents rather than just describing what they would do.
4. Confirm the `core-standards` skill is available to specialist subagents and note any differences when launching the Coordinator with `--agent`.
5. Review the first agent-generated diff, exact tests and docs before granting broader automatic permissions or deploying anything. Keep production credentials out of the testing environment.

This remains a **review candidate**, not a certified production release. See `docs/PREPUBLICATION-REVIEW.md`.
