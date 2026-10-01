# Task completion

One person can mark a local task complete by numeric ID. The CLI persists successful changes to JSON; the core function works on an in-memory list.

The core function is now `finish_task(tasks, task_id)`, replacing `complete_task`. In-memory callers must use the new name. Repeated completion now raises an error instead of succeeding with the task still marked done.

| ID | Condition | Behavior | Code and tests |
| --- | --- | --- | --- |
| COMP-01 | Existing not-done ID | Marks the task done and returns it | [finish_task](../tasklist/tasks.py); [test_complete_marks_done](../tests/test_tasks.py) checks the returned and stored flag |
| COMP-02 | Missing ID | Raises `KeyError(task_id)` | [finish_task](../tasklist/tasks.py); [test_missing_id_rejected](../tests/test_tasks.py) checks a missing ID |
| COMP-03 | Already done ID | Raises `ValueError("already complete")` without changing the task | [finish_task](../tasklist/tasks.py); [test_repeat_completion_rejected](../tests/test_tasks.py) checks that repeated completion raises `ValueError` |

The [CLI](../tasklist/cli.py) command remains `complete <task_id>` and calls `finish_task`. It reports missing-ID and already-complete errors with exit status 2, without writing the JSON file. Successful completion writes the updated tasks to JSON.

Core tests do not test CLI persistence or error handling. The repeated-completion test checks the exception type, but does not assert its message or that the task remains unchanged; those behaviors are established by the implementation. The missing-ID test likewise checks the exception type, without asserting its arguments. See [working instructions](../README.md) for setup and checks.
