# Task completion

One person can mark a local task complete by numeric ID. The CLI persists successful changes to JSON; the core function works on an in-memory list.

This page reflects the current uncommitted code and test change: the core function is now `finish_task`, and completing an already done task is rejected. The CLI command remains `complete`.

| ID | Condition | Behavior | Code and tests |
| --- | --- | --- | --- |
| COMP-01 | Existing not-done ID | Marks the task done and returns it | [finish_task](../tasklist/tasks.py); [test_complete_marks_done](../tests/test_tasks.py) checks the returned and stored flag |
| COMP-02 | Missing ID | Raises `KeyError(task_id)` | [finish_task](../tasklist/tasks.py); [test_missing_id_rejected](../tests/test_tasks.py) checks that a missing ID raises `KeyError` |
| COMP-03 | Already done ID | Raises `ValueError("already complete")` before changing the task | [finish_task](../tasklist/tasks.py); [test_repeat_completion_rejected](../tests/test_tasks.py) checks that an already done task raises `ValueError`; it does not assert the message or unchanged state |

The [`main` function in the CLI](../tasklist/cli.py) calls `finish_task` for `complete`, writes the JSON file after success, and prints the returned task as JSON. It catches `ValueError` and `KeyError`, reports the error on standard error, and exits with status 2 before writing the file. For repeated completion, the error is `already complete` and the file is left unchanged. These CLI behaviors are supported by code inspection; the core tests do not test CLI persistence or error output. See [working instructions](../README.md) for setup and checks.

Local verification of the current working tree: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` passed all six tests, including the three completion tests above.
