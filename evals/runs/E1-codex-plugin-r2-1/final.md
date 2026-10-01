Preparation is complete.

- Added [Codex instructions](AGENTS.md) and [Claude Code instructions](CLAUDE.md), linked to a shared [knowledge index](docs/knowledge/index.md).
- Documented [completion behavior with code and test references](docs/knowledge/capabilities/task-completion.md): completion marks a task done, repeating succeeds, and missing IDs produce an error.
- All **6 existing tests pass** on Python 3.14.2. They cover in-memory operations; CLI and persistence remain untested. See [readiness results](docs/knowledge/working.md).
- Documentation links and whitespace checks pass.

Only documentation changed. The export note was preserved; no application code, tests, or commits were changed.