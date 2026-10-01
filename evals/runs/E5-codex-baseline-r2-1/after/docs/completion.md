# Task completion

One person can mark a local task complete by numeric ID. The CLI persists successful changes to JSON; the core function works on an in-memory list.

| ID | Condition | Behavior | Code and tests |
| --- | --- | --- | --- |
| COMP-01 | Existing not-done ID | Marks the task done and returns it | [finish_task](../tasklist/tasks.py); [test_complete_marks_done](../tests/test_tasks.py) checks the returned and stored flag |
| COMP-02 | Missing ID | Raises `KeyError(task_id)` | [finish_task](../tasklist/tasks.py); [test_missing_id_rejected](../tests/test_tasks.py) checks a missing ID |
| COMP-03 | Already done ID | Raises `ValueError("already complete")` and leaves the task unchanged | [finish_task](../tasklist/tasks.py); [test_repeat_completion_rejected](../tests/test_tasks.py) checks that repeated completion raises `ValueError` |

The CLI's `complete` command calls [finish_task](../tasklist/tasks.py). The [CLI](../tasklist/cli.py) reports errors with exit status 2 and writes the JSON file after successful completion. Repeated completion reports `already complete` and exits without writing the file. Core tests do not test CLI persistence; the repeated-completion test checks the exception type, but does not assert the message or unchanged task state. See [working instructions](../README.md) for setup and checks.
