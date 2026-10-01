Investigation complete. Published [findings](docs/task-completion.md) and [follow-up work](docs/work/investigation/repeat-completion.md).

- Intended: repeated completion must raise `ValueError`.
- Current: it succeeds; the CLI rewrites the file and prints success.
- Tests: five passed, one failed confirming the mismatch. The misleadingly named “idempotent” test actually asserts rejection.
- Decision: the rejection rule is already confirmed. Error wording remains unspecified; retaining successful repeats would require changing the requirement.

Documentation links and whitespace checks passed. Only documentation changed; no commits were made.