Preparation complete for Codex and Claude Code. Both host instructions now point to shared documentation.

- [Task completion](/private/tmp/repository-knowledge-evals/E2a-codex-plugin-r1/docs/completion.md) explains behavior and links to code and tests. Corrected the stale claim: repeated completion succeeds. Missing IDs raise `KeyError`; successful CLI completion persists JSON.
- [Readiness results](/private/tmp/repository-knowledge-evals/E2a-codex-plugin-r1/README.md#verification-and-readiness): all **6 existing tests passed** on Python 3.14.2. Documentation links and whitespace checks passed.
- Coverage gap: existing tests cover core functions; CLI persistence and error handling were inspected but not executed.

Only documentation changed. The future export note was preserved. No application code, tests, or commits changed.