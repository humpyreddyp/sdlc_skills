# Task completion

Completing a task records that an item in the local task list is done. Users select a numeric ID with `python3 -m tasklist.cli --file PATH complete ID`; callers can also use the in-memory `complete_task(tasks, task_id)` function. The CLI supplies JSON persistence, as described in the [README](../README.md).

## Intended rule and current behavior

The [confirmed product requirement](../requirements.md) requires `ValueError` when completing an already completed task. The implementation currently accepts that request. This is a compliance gap, not an unresolved choice of product intent.

| ID | Condition or trigger | Current behavior | Code and tests |
| --- | --- | --- | --- |
| COMPLETE-001 | A matching task has `done: false` | Sets `done` to `true`, mutates the input task, and returns that task. | [tasks.py](../tasklist/tasks.py), `complete_task`; [test_tasks.py](../tests/test_tasks.py), `TaskTests.test_complete_marks_done` checks the returned and stored flags. |
| COMPLETE-002 | A matching task already has `done: true` | Assigns `true` again and returns the task without raising. The confirmed requirement instead requires `ValueError`. | [tasks.py](../tasklist/tasks.py), `complete_task` has no check of the prior flag; [test_tasks.py](../tests/test_tasks.py), `TaskTests.test_repeat_completion_is_idempotent` asserts `ValueError` and fails. |
| COMPLETE-003 | No task matches the ID | Raises `KeyError(task_id)`. | [tasks.py](../tasklist/tasks.py), `complete_task`; [test_tasks.py](../tests/test_tasks.py), `TaskTests.test_missing_id_rejected` checks this with an empty list and ID 9. |

The name `test_repeat_completion_is_idempotent` is misleading: its body explicitly expects rejection. It does not establish a requirement for successful repeated completion. Current repeated completion leaves the `done` value unchanged, but that alone does not satisfy the required exception.

## CLI flow and consequences

In [cli.py](../tasklist/cli.py), `main` parses the numeric ID, reads the selected JSON file (or starts with an empty list), and calls `complete_task`. On a successful return it writes the task list to the file and prints the returned task as JSON. Consequently, the current repeated-completion path rewrites the file and prints success even though the task was already done.

`main` catches `ValueError` and `KeyError`, prints the exception text to standard error, and exits with status 2 before writing the file or printing a success result. If `complete_task` is corrected to raise the required `ValueError`, that existing handler provides the CLI rejection path. Neither the requirement nor the repeat-completion test specifies the exception message. These CLI conclusions come from source inspection; the existing suite tests the core functions, not CLI execution.

## Verification and remaining work

On 2026-10-01, using Python 3.14.2, ran the README's existing suite with bytecode generation disabled:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Six tests ran: five passed and `test_repeat_completion_is_idempotent` failed with `AssertionError: ValueError not raised`. This directly confirms noncompliance for an existing task whose `done` value is `True`. Application code and tests were not changed.

No further product decision is needed to establish the rejection rule. Follow-up delivery must implement that rule; any proposal to retain successful repeats would require an explicit revision of the confirmed requirement. Exception wording remains unspecified. See the [follow-up record](work/investigation/repeat-completion.md) for the work left outside this documentation investigation.
