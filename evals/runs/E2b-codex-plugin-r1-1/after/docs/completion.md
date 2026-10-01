# Task completion

One person can mark a local task complete by numeric ID. The CLI persists successful changes to JSON; the core function works on an in-memory list.

| ID | Condition | Behavior | Code and tests |
| --- | --- | --- | --- |
| COMP-01 | Existing not-done ID | Marks the task done and returns it | [complete_task](../tasklist/tasks.py); [test_complete_marks_done](../tests/test_tasks.py) checks the returned and stored flag |
| COMP-02 | Missing ID | Raises KeyError | [complete_task](../tasklist/tasks.py); [test_missing_id_rejected](../tests/test_tasks.py) checks a missing ID |
| COMP-03 | Already done ID | Succeeds and keeps done true | [complete_task](../tasklist/tasks.py); [TaskTests.test_repeat_completion_is_idempotent](../tests/test_tasks.py) calls completion on an already-done task and checks the returned flag |

## CLI flow and limits

In [tasklist/cli.py](../tasklist/cli.py), `main` parses `complete <task_id>` as an integer. `--file` selects the JSON file and defaults to `tasks.json` relative to the working directory. The CLI loads an existing file or starts with an empty list if the file is absent, then calls [complete_task](../tasklist/tasks.py). That function scans the list, mutates the first matching task, and returns the same dictionary. Completing a task keeps it in the list; `list_tasks` returns copies of all task dictionaries, including completed tasks.

| ID | Condition | Behavior | Code and tests |
| --- | --- | --- | --- |
| COMP-04 | CLI completion succeeds | Rewrites the task list as JSON with a trailing newline, then prints the completed task as JSON. Completing an already-done task also writes the file. | [main](../tasklist/cli.py); no existing CLI test |
| COMP-05 | CLI completion cannot find the ID, including when the file is absent | Catches the core `KeyError`, prints the error to stderr, and exits with status 2 before writing a file. | [main](../tasklist/cli.py); [TaskTests.test_missing_id_rejected](../tests/test_tasks.py) covers only the core exception |
| COMP-06 | CLI ID is not an integer | Argument parsing rejects it before loading the file. | [main](../tasklist/cli.py), `type=int`; no existing CLI test |

The CLI catches `ValueError` and `KeyError` from the selected core operation. JSON loading happens before that handler and file writing happens afterward, so malformed JSON and file I/O failures are not handled by that error path. There is no explicit validation of the loaded task schema. These limits are visible in `main`; the existing tests do not exercise them.

The three completion tests in [TaskTests](../tests/test_tasks.py) cover the returned and stored done flag, an already-done task, and a missing ID on an empty list. They do not cover CLI persistence or error output, selecting among multiple IDs, duplicate IDs, or the returned object's identity. [TaskTests.test_list_returns_copies](../tests/test_tasks.py) separately checks that changing a listed task's done flag does not mutate the original task.

See [working instructions and verification results](../README.md) for setup and checks, and the [knowledge index](knowledge/index.md) for repository navigation.
