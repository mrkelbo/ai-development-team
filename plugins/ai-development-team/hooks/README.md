# Hooks reserved for environment-specific enforcement

`hooks.json` contains no active hooks in this initial release. This is intentional: Windows/Linux, local/remote, and shell runtimes need real smoke testing before packaging any command-interception hook that fires across **every enabled project**. Establish production permission/credential separation and appropriate deny rules before enabling actions that might affect live resources. See `docs/SAFETY-AND-LIMITATIONS.md`.
