Added [AGENTS.md](AGENTS.md) and [CLAUDE.md](CLAUDE.md) with shared repository guidance, plus a [completion reference](docs/task-completion.md) linked from README.

Completion marks the matching task done, succeeds on repeats, and rejects missing IDs. The reference maps behavior to code and tests and explains CLI persistence.

Validation: all **6 tests pass** on Python 3.14.2; documentation links and whitespace checks pass. Existing tests cover core functions, not CLI behavior.

Application code, tests, and the export note remain unchanged. No commits were made.