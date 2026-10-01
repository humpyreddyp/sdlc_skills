# Task completion

One person can mark a local task complete by numeric ID. The CLI persists successful changes to JSON; the core function works on an in-memory list.

This page reflects the current uncommitted code and test change: the core function is renamed from `complete_task` to `finish_task`, and repeated completion is rejected. The CLI command remains `complete`. COMP-03 retains its identity for the already-done case, replacing the previous successful repeat behavior.

| ID | Condition | Behavior | Code and tests |
| --- | --- | --- | --- |
| COMP-01 | Existing not-done ID | Marks the task done and returns it | [finish_task](../tasklist/tasks.py); [test_complete_marks_done](../tests/test_tasks.py) checks the returned and stored flag |
| COMP-02 | Missing ID | Raises `KeyError(task_id)` | [finish_task](../tasklist/tasks.py); [test_missing_id_rejected](../tests/test_tasks.py) checks a missing ID raises `KeyError` |
| COMP-03 | Already done ID | Raises `ValueError("already complete")` before mutation; the task stays done | [finish_task](../tasklist/tasks.py) establishes the message and unchanged state; [test_repeat_completion_rejected](../tests/test_tasks.py) checks that an already-done task raises `ValueError` |

The [CLI main function](../tasklist/cli.py) loads the JSON task list and calls `finish_task` for `complete`. On success, it writes the updated list to the JSON file and prints the returned task as JSON. It catches `ValueError` and `KeyError`, reports the error, and exits with status 2 before writing the file. Repeating completion therefore reports `already complete` and leaves the file unchanged.

Verification: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` passed all six tests against the current working tree. These core tests do not check the exact repeat-error message, unchanged state after rejection, or CLI persistence; those details above come from inspected implementation. See [working instructions](../README.md) for setup and checks.
