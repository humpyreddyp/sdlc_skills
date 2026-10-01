# Working instructions and readiness

## Starting work

Use the [knowledge index](index.md) to find the relevant capability. For completion changes, read the [task completion behavior map](capabilities/task-completion.md), then follow its references to `main`, `complete_task`, and the named tests. Distinguish implemented behavior from intended changes and from behavior actually covered by tests. Update the affected explanation and retain its behavior IDs when a change is made.

The [README](../../README.md) is the authoritative setup and command source: Python 3.10 or later, no third-party dependencies, and execution from the repository root. There is no dependency installation step. Its example CLI commands write the selected JSON file; choose a disposable file when trying them. Its unittest discovery command is the existing verification entry point. No other check configuration or test suite is present in the inspected repository files.

## Preparation assessment — 2026-10-01

**Complete for the requested scope:** Codex and Claude Code have short entry points into shared knowledge; task completion is explained with code and test references; the existing suite runs in this environment. This assesses readiness to work on completion, not readiness of an unspecified future change.

Inspection started with a clean working tree at commit `24eb47b`. Sources inspected were [README](../../README.md), [the export note](../export-notes.md), [CLI](../../tasklist/cli.py), [core operations](../../tasklist/tasks.py), [package initializer](../../tasklist/__init__.py), and [tests](../../tests/test_tasks.py). Preparation changes are documentation only. The export proposal remains unchanged.

| Command actually executed | Result |
| --- | --- |
| `python3 --version` | Passed: Python 3.14.2. |
| `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` | Passed: all 6 tests, exit status 0. The environment variable suppresses bytecode creation; the test command is the README runner. |
| `python --version` | Could not run: `python` is not installed as a command, exit status 127. The documented `python3` command is available. |

There is no setup blocker for the existing suite. Python 3.10 itself was not tested. The suite covers in-memory functions only; no CLI smoke commands or persistence checks were run. The [behavior map](capabilities/task-completion.md) identifies the specific coverage gaps. A future CLI or persistence change will need validation of those affected paths before its behavior can be reported as tested.

No installation, application or test edits, network access, or commits were performed. No remaining investigation or required user decision blocks this preparation.
