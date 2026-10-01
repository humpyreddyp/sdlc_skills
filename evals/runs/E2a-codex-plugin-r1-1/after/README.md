# Local task list

A command-line task list for one person, stored in a local JSON file. Add a task, list tasks, and complete a task by its numeric ID. Python 3.10 or later is required; there are no third-party dependencies.

Run from this directory:

```sh
python3 -m tasklist.cli --file /tmp/example-tasks.json add 'Review a document'
python3 -m tasklist.cli --file /tmp/example-tasks.json list
python3 -m tasklist.cli --file /tmp/example-tasks.json complete 1
python3 -m unittest discover -s tests -v
```

The core functions also work in memory. Persistence is provided by the CLI; this is not a web service or a multi-user database.

## Verification and readiness

Run the commands above from the repository root with Python 3.10 or later. No third-party dependency installation is needed. Use synthetic tasks and a disposable JSON file for examples; never use live customer data. Start with the [knowledge index](docs/index.md) and [task completion](docs/completion.md) for behavior and links to the implementation and individual tests. Codex and Claude Code enter through [AGENTS.md](AGENTS.md) and [CLAUDE.md](CLAUDE.md), respectively, and share this documentation.

Preparation assessed on 2026-10-01 at revision `3f95211`, starting from a clean working tree. Inspected the root instructions, existing documentation, both implementation modules, package initializer, and the sole test module. Documentation now describes the current completion behavior; application code and tests were not changed.

| Command executed | Result |
| --- | --- |
| `python3 --version` | Python 3.14.2 |
| `python3 -m unittest discover -s tests -v` | Passed all 6 tests |
| `git diff --check` | Passed; no whitespace errors |

Preparation for both hosts is complete, with no observed setup blocker for the existing suite. The CLI examples above were not executed during this assessment. The suite covers in-memory operations only; CLI persistence and error behavior remain unverified by execution. Python 3.10 compatibility was not exercised. Future CLI changes need verification of persisted JSON, output, and exit status; see the [completion coverage limits](docs/completion.md#verification-limits). No dependency installation, network access, or application fixes were needed for this assessment.
