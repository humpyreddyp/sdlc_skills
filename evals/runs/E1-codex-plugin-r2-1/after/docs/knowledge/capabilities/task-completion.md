# Task completion

Completion lets the person using the task list mark an existing task as done by its numeric ID, as described in the [README](../../../README.md). It keeps the task in the list. For example, completing `{"id": 1, "title": "Read", "done": false}` produces `{"id": 1, "title": "Read", "done": true}`. The same command can be repeated successfully.

## Current behavior

These rows describe inspected implementation. Named tests identify existing coverage; an uncovered row is not a verified CLI result.

| ID | Condition or trigger | Behavior | Code and tests |
| --- | --- | --- | --- |
| TC-001 | Complete an existing task ID | Find the first task with an equal ID, set `done` to `True` in the supplied list, and return that same task dictionary. Other fields remain unchanged. | [tasks.py](../../../tasklist/tasks.py), `complete_task`; [test_tasks.py](../../../tests/test_tasks.py), `TaskTests.test_complete_marks_done` checks returned and stored `done`. First-match selection, identity, and other-field preservation have no explicit assertions. |
| TC-002 | Complete a task already marked done | Succeed again with `done=True`; the in-memory state is idempotent. The CLI still writes the file on success. | [tasks.py](../../../tasklist/tasks.py), `complete_task`; `TaskTests.test_repeat_completion_is_idempotent` in [test_tasks.py](../../../tests/test_tasks.py) checks the returned flag for an already-complete task. File rewriting is implemented in [cli.py](../../../tasklist/cli.py), `main`, without an existing CLI test. |
| TC-003 | No task matches the requested ID | Core raises `KeyError(task_id)` without changing the list. CLI catches it, exits with status 2 and an error on stderr, and does not write the file or print a JSON result. | [tasks.py](../../../tasklist/tasks.py), `complete_task`; `TaskTests.test_missing_id_rejected` in [test_tasks.py](../../../tests/test_tasks.py) checks `KeyError` on an empty list. [cli.py](../../../tasklist/cli.py), `main`, implements the CLI error path; it is untested. |
| TC-004 | Invoke `complete` through the CLI | Require an integer `task_id`. Read the selected JSON file, defaulting to `tasks.json` relative to the working directory. A nonexistent file supplies an empty list, so completion fails as in TC-003 and does not create it. On success, write the entire list as JSON plus a newline, then print the completed task as JSON. | [cli.py](../../../tasklist/cli.py), `main`; no existing CLI or persistence tests. |
| TC-005 | List tasks after completing one | Include completed tasks with `done=True`; listing does not filter them out. Return a new list of shallow dictionary copies. CLI listing prints JSON without writing the file. | [tasks.py](../../../tasklist/tasks.py), `list_tasks`; `TaskTests.test_list_returns_copies` in [test_tasks.py](../../../tests/test_tasks.py) checks that changing a returned `done` field does not change the original. Completed-task inclusion and CLI behavior have no explicit tests. |

## Implementation route

Start at [cli.py](../../../tasklist/cli.py), `main`: `argparse` parses the command and file path, `json.loads` loads existing data, and the `complete` branch calls [tasks.py](../../../tasklist/tasks.py), `complete_task`. That function scans the list and mutates the matching dictionary. The CLI persists the list before printing the returned dictionary. Use the [README commands](../../../README.md) for the add/list/complete journey and the test runner.

The supporting `add_task` operation trims the title, rejects a blank title, assigns one more than the largest existing ID (1 for an empty list), and appends a task with `done=False`. In [test_tasks.py](../../../tests/test_tasks.py), `TaskTests.test_add_trims_and_assigns_id` covers trimming and the first ID; `TaskTests.test_blank_title_rejected` covers whitespace-only rejection. Allocation after existing IDs is implemented but not tested explicitly.

## Limits relevant to changes

The CLI trusts the loaded JSON structure; there is no explicit task schema validation. File reads and JSON decoding happen before its operation-error handler, and file writes happen afterward. Invalid JSON and file-access errors therefore do not use the handled completion-error path. Persistence uses a direct whole-file write with no locking or atomic replacement ([cli.py](../../../tasklist/cli.py), `main`). The [README](../../../README.md) scopes this to local, single-person use.

All existing tests exercise core functions in memory. They do not establish argument parsing, stdout/stderr, exit codes, on-disk persistence, or failure behavior for malformed files. See [readiness](../working.md) for the actual test execution result. No changed completion behavior is specified by this preparation request.
