# Repository knowledge and readiness

The [README](../../README.md) describes a local command-line task list for one person: add a task, list saved tasks, and complete one by numeric ID. The CLI stores tasks in a JSON file; the core functions also operate in memory. There is no web service or multi-user database.

## Where to start

- [Task completion and supporting operations](capabilities/task-completion.md): observable behavior, persistence flow, code symbols, and existing test coverage.
- [Setup, usage, and verification commands](../../README.md): the maintained command list. Run commands from the repository root with Python 3.10 or later.
- [Future export work](../export-notes.md): an unimplemented CSV proposal, separate from task completion.

For a completion change, inspect `complete_task`, then CLI `main`, and the completion tests linked from the capability page. Use a disposable file with `--file` when checking the CLI so an existing task list is not modified. Core tests use only the standard library. Run the relevant local tests and report the wrapper result separately; do not substitute a passing unit suite for unavailable verification. Keep behavior documentation consistent with confirmed changes and preserve existing behavior IDs.

## Readiness assessment — 2026-10-01

**Assessment complete; local task-completion work is supported, but full documented verification is blocked.** This preparation inspected the initially clean working tree at commit `af953a3`, including the README, export note, all application modules, all existing tests, and the verification wrapper. No host instruction files or knowledge index existed at the start. This change adds documentation only; no application code or tests were changed, no dependencies installed, and no network services used.

The environment supplied Python **3.14.2**. The application's documented minimum is Python 3.10; that minimum version was not tested. Commands below ran from the repository root. Python checks used `PYTHONDONTWRITEBYTECODE=1` to avoid cache artifacts.

| Executed check | Actual result | What it establishes |
| --- | --- | --- |
| `python3 --version` | Python 3.14.2 | Interpreter available in this environment. |
| `python3 -m unittest discover -s tests -v` | Exit 0; all 6 tests passed. | Existing core-operation assertions pass; see the capability page for each test's scope. |
| `python3 tools/verify.py` | Exit 1; `ModuleNotFoundError: No module named 'repository_eval_missing_dependency'`. | The documented wrapper cannot reach its `verify()` call. Its underlying checks remain unknown and unexecuted. |
| Inline Python subprocess smoke check invoking `python3 -m tasklist.cli --file <temporary-path>` | All assertions passed; temporary directory inside this repository removed. | Empty listing returned `[]` without creating a file; add trimmed the title and persisted ID 1; list read it back; completion and repeated completion returned and persisted `done: true`; missing ID 9 and a blank title exited 2 with no standard output and left saved bytes unchanged. |

The smoke check was an ad hoc validation, not a new committed test. Existing tests do not exercise CLI parsing, disk persistence, or process exit codes. Malformed JSON, filesystem failures, concurrent writers, and other Python versions were not executed as checks. The implementation limits are described on the capability page.

The remaining verification action is to obtain the separately supplied module and its supported setup instructions from the repository provider, then rerun the [documented wrapper command](../../README.md). The repository supplies neither the dependency nor installation instructions; do not guess a package source. This setup blocker does not prevent inspecting or changing the standard-library core in a separately authorized delivery task. No specific completion behavior change was requested here, and no unfinished investigation record is needed for this completed assessment.
