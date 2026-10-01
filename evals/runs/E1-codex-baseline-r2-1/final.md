Added [AGENTS.md](/private/tmp/repository-knowledge-evals/E1-codex-baseline-r2/AGENTS.md), [CLAUDE.md](/private/tmp/repository-knowledge-evals/E1-codex-baseline-r2/CLAUDE.md), and a shared [task-completion guide](/private/tmp/repository-knowledge-evals/E1-codex-baseline-r2/docs/task-completion.md), linked from README.

Completion updates the matching task in place, succeeds when repeated, and raises `KeyError` for missing IDs. Relevant files:

- [Core operations](/private/tmp/repository-knowledge-evals/E1-codex-baseline-r2/tasklist/tasks.py:18)
- [CLI and JSON persistence](/private/tmp/repository-knowledge-evals/E1-codex-baseline-r2/tasklist/cli.py:8)
- [Existing tests](/private/tmp/repository-knowledge-evals/E1-codex-baseline-r2/tests/test_tasks.py:21)

All **6 tests passed** using unittest discovery on Python 3.14.2. `git diff --check` passed. CLI persistence and exit behavior lack automated coverage; no CLI smoke test was run.

Only documentation changed. Application code, tests, and the future export note remain unchanged. No commits were made.