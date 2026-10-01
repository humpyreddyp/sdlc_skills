# Repository knowledge

This is a command-line task list for one person, backed by a local JSON file. The [README](../../README.md) establishes its purpose and setup: add a task, list tasks to find its numeric ID, then complete it. Core functions also operate on an in-memory list; the CLI handles persistence.

- [Task completion](capabilities/task-completion.md): current behavior, error handling, implementation flow, and specific test coverage.
- [README setup and commands](../../README.md): Python prerequisite, CLI examples, and the existing test command.
- [Future export work](../export-notes.md): preserved proposal; CSV export is not implemented.

## Working instructions

Run commands from the repository root. Python 3.10 or later is required, with no third-party dependencies or installation step documented. Use an explicit `--file` path for CLI experiments to avoid modifying an existing task list; the default is `tasks.json` in the current directory. The examples and verification command are maintained in the README.

For completion work, trace `main` in [tasklist/cli.py](../../tasklist/cli.py), `complete_task` in [tasklist/tasks.py](../../tasklist/tasks.py), and `TaskTests` in [tests/test_tasks.py](../../tests/test_tasks.py). Review the behavior table before proposing changes, run the existing suite after relevant changes, and update affected explanations. Keep proposed features distinct from current behavior. No application change was requested as part of this preparation.

## Preparation and verification

Preparation for Codex and Claude Code is complete for task completion. Inspected baseline: commit `6a63483`, initially clean working tree. Sources inspected: README, all three `tasklist` Python files, the existing test file, and the export note. Root host instructions now route both agents here. Only documentation was changed; there is no unfinished investigation requiring a separate record.

On 2026-10-01, local verification produced:

| Command | Observed result |
| --- | --- |
| `python3 --version` | Python 3.14.2, satisfying the documented minimum. |
| `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` | Exit 0; all six existing tests passed. The environment setting prevents bytecode files from being created. |

No setup blocker was encountered. The existing suite exercises in-memory operations only; CLI invocation, disk persistence, malformed files, and filesystem failures were not executed as checks. No additional test, lint, or CI configuration is present in the inspected repository. Future CLI changes need verification of those paths; passing this suite alone does not establish CLI correctness. No dependency installation, network access, commit, or application/test edit was performed.
