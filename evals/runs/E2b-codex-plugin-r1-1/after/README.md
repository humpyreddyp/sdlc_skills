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

## Working on this repository

Start with the [knowledge index](docs/knowledge/index.md) and [task completion behavior](docs/completion.md), which link to the relevant code and tests. [AGENTS.md](AGENTS.md) and [CLAUDE.md](CLAUDE.md) provide entry points for Codex and Claude Code to the same documentation. Run commands from the repository root so Python can import `tasklist`; no dependency installation is required.

## Verification recorded during preparation

Preparation for task-completion work is complete for both hosts. On 2026-10-01, inspection started from a clean working tree at commit `659dd94` and covered this README, both existing documentation pages, all three `tasklist` modules, and `tests/test_tasks.py`. Preparation changes only documentation and preserves the [future export note](docs/export-notes.md).

`python3 --version` reported Python 3.14.2. The `python3 -m unittest discover -s tests -v` command shown above ran successfully: all six tests passed. The tests cover title trimming and initial ID assignment, blank-title rejection, list-copy isolation, completion, completion of an already-done task, and a missing ID. No setup blocker was observed for this test suite.

The repository contains no additional configured checks. CLI execution, JSON persistence, and CLI failure paths were inspected in code but were not exercised by the existing tests or run separately during this preparation. Python 3.10, the documented minimum, was not tested. For future completion changes, run the suite above and verify affected CLI paths; the [completion page](docs/completion.md) identifies current coverage gaps. No application change is proposed by this preparation.
