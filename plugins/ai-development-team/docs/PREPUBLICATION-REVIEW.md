# Pre-publication review — AI Development Team initial draft

## Decision

**Status: REVIEW CANDIDATE — approved for local sandbox testing, NOT production-certified.**

### Findings corrected during internal review

| Finding | Risk | Mitigation |
| --- | --- | --- |
| Shared policies were not explicitly preloaded into agent contexts | Agent might miss cross-project safety rules | Preload the `core-standards` skill; retain invariant rules in each definition as fallback |
| Named tool lists excluded Skill and relevant web tools | Missing workflow knowledge and external design research | Add Skill to agents and WebSearch/WebFetch to research-appropriate roles |
| Coordinator could describe delegation without invoking an agent | False claims of independently reviewed code | Require actual Agent tool dispatch and explicit PLANNED/NOT_RUN versus COMPLETED evidence |
| QA's evidence standards could be made more reproducible | Unverified releases | Add tested-version/command/results and before/after upgrade assertions |
| Untrusted repository content had no specific countermeasure | Prompt injection / workflow compromise | Add explicit untrusted-input rule to Security and shared constitution |
| Repository changes had no automated package test | Malformed plugin could be published | Add GitHub Actions offline validation job and stronger local validation checks |

### Known limitations and acceptance conditions

1. Claude Code is not installed in the authoring runtime, so the native `claude plugin validate`, installation flow, tool-list resolution, and live subagent execution **have not been verified here**.
2. Loading a preconfigured skill into a plugin subagent and into a main-session `--agent` may differ by CLI version. Confirm that actual constraints are visible and followed.
3. Tool lists are not a sandbox: shell access can write data and network calls depending on user permissions; use standard OS isolation and scoped credentials. The shipped hooks are intentionally inactive.
4. Manual evaluation scenarios must be run in a disposable repo: confirm Coordinator invokes specialist agents, QA doesn't modify implementation to force success, no tenant cross-access, no database reset and no unapproved deploys.
5. For a stable release, require native validator PASS, scenario results and project-specific environment security configuration. Add CI/branch protection to production *application* repositories separately.

## Recommendation

Upload this **initial draft** package to your private GitHub repository when convenient, but leave automatic updates disabled and do not label the plugin production-ready until the live smoke tests pass.
