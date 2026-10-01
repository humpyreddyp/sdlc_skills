# Task completion

One person can mark a local task complete by numeric ID. The CLI persists successful changes to JSON; the core function works on an in-memory list.

| ID | Condition | Behavior | Code and tests |
| --- | --- | --- | --- |
| COMP-01 | Existing not-done ID | Marks the task done and returns it | [complete_task](../tasklist/tasks.py); [test_complete_marks_done](../tests/test_tasks.py) checks the returned and stored flag |
| COMP-02 | Missing ID | Raises KeyError | [complete_task](../tasklist/tasks.py); [test_missing_id_rejected](../tests/test_tasks.py) checks a missing ID |
| COMP-03 | Already done ID | raises ValueError and rejects the operation | [complete_task](../tasklist/tasks.py); [test_repeat_completion_is_idempotent](../tests/test_tasks.py) checks repeated completion |

The CLI calls complete_task, reports errors with exit status 2, and writes the JSON file after success. Core tests do not test CLI persistence. See [working instructions](../README.md) for setup and checks.
