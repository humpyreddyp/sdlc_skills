# Task completion

The local task list lets a person mark a task done by its numeric ID using `complete <task_id>`. The [confirmed requirement](../requirements.md) says that completing an already completed task must raise `ValueError`. This rule is settled; the current implementation does not comply.

## Current behavior and evidence

These rows describe the inspected implementation, not acceptance of its behavior as the intended rule.

| ID | Condition or trigger | Current behavior | Code and tests |
| --- | --- | --- | --- |
| COMPLETE-001 | Complete an existing task whose `done` value is false | Set `done` to true and return the same task dictionary. | [tasks.py](../tasklist/tasks.py), `complete_task`; [test_tasks.py](../tests/test_tasks.py), `TaskTests.test_complete_marks_done` checks the returned and stored `done` values. |
| COMPLETE-002 | Complete an existing task whose `done` value is already true | Set `done` to true again and return the task without raising an error. This conflicts with the confirmed requirement. | [tasks.py](../tasklist/tasks.py), `complete_task` has no check for prior completion; [test_tasks.py](../tests/test_tasks.py), `TaskTests.test_repeat_completion_is_idempotent` actually expects `ValueError` and fails. Its name does not describe its assertion. |
| COMPLETE-003 | Complete an ID absent from the task list | Raise `KeyError(task_id)`. | [tasks.py](../tasklist/tasks.py), `complete_task`; [test_tasks.py](../tests/test_tasks.py), `TaskTests.test_missing_id_rejected` checks `KeyError`. |

The command-line path is [cli.py](../tasklist/cli.py), `main`: parse the integer ID, load the JSON file (or use an empty list if it does not exist), and call `complete_task`. After a successful completion, the CLI writes the list to the file and prints the returned task as JSON. Thus repeating `complete 1` on a completed task currently succeeds and rewrites the file even though the task's state stays the same.

The CLI already catches `ValueError` and `KeyError`, exits with status 2, and prints the error to standard error before reaching the file write. If the core function raises the required `ValueError`, this existing handler provides the rejection path. These CLI conclusions come from code inspection; the existing suite does not exercise the CLI.

## Verification

On 2026-10-01, ran the README's existing check with bytecode generation disabled:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Result: six tests ran, five passed, and `TaskTests.test_repeat_completion_is_idempotent` failed with `AssertionError: ValueError not raised`. The assertion agrees with the confirmed requirement; the implementation is the observed compliance gap. No application code or tests were changed during this investigation.

## Decision and follow-up

No further product decision is needed about whether repeated completion is allowed: the product owner has already confirmed rejection. Successful repeated completion is only the current behavior. Retaining it would require an explicit change to the confirmed requirement.

The requirement does not specify the exact error message. That wording remains an implementation choice, not a blocker to establishing the rule. Remaining work is recorded in the [completion compliance follow-up](work/task-completion.md).
