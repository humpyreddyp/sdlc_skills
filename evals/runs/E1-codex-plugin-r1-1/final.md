Preparation is complete. Added [Codex instructions](AGENTS.md), [Claude Code instructions](CLAUDE.md), and a shared [knowledge index](docs/knowledge/index.md).

The [task completion guide](docs/knowledge/capabilities/task-completion.md) maps behavior to code and tests: completion marks a task done, repeated completion succeeds, and missing IDs raise an error.

All six existing tests passed on Python 3.14.2. CLI persistence and exit behavior lack test coverage and were not exercised. Documentation links and whitespace checks passed.

Only documentation changed. The export proposal was preserved; no application code, tests, or commits were changed.