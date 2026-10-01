# Task completion

The local task list lets a person mark a task complete by numeric ID. The [README](../README.md) describes the CLI and local JSON storage. The [delivery request](../delivery.md) calls for a friendly confirmation message; that message is not implemented.

## Current behavior

| ID | Condition or trigger | Behavior | Code and tests |
| --- | --- | --- | --- |
| COMPLETE-01 | Complete an existing unfinished task | Set `done` to `True` and return the task. | [tasks.py](../tasklist/tasks.py), `finish_task`; [test_tasks.py](../tests/test_tasks.py), `test_complete_marks_done` checks both the returned task and stored in-memory state. |
| COMPLETE-02 | Complete an existing task whose `done` is already `True` | Succeed and return the task with `done=True`. Completion is idempotent: repeating it leaves the completion state unchanged. | [tasks.py](../tasklist/tasks.py), `finish_task` has no rejection or separate branch for completed tasks; [test_tasks.py](../tests/test_tasks.py), `test_repeat_completion_is_idempotent` starts with a completed task and checks that the returned task is still done. |
| COMPLETE-03 | Complete an ID absent from the list | The core raises `ValueError("unknown task")`; the CLI writes `unknown task` followed by a newline to stderr and exits with status 2 before writing the file. | [tasks.py](../tasklist/tasks.py), `finish_task`; [cli.py](../tasklist/cli.py), `main`; [test_tasks.py](../tests/test_tasks.py), `test_missing_id_rejected` checks the core exception type only, not its message or CLI behavior. |
| COMPLETE-04 | A CLI completion call returns successfully | Write the task list to the JSON file and print the returned task as JSON, for both first and repeated completion. There is no friendly confirmation or special repeated-completion message. | [cli.py](../tasklist/cli.py), `main`, calls `finish_task`, writes for non-list commands, then prints `json.dumps(result)`. No existing test exercises CLI output or persistence. |

For a task with ID 1 and title `Read`, either successful completion path prints `{"id": 1, "title": "Read", "done": true}`. This follows from the inspected CLI; it was not verified by a CLI execution. Repeated completion still writes the file, even though the completion state is unchanged.

## Confirmed requirement and delivery boundary

The user confirmed on 2026-10-01 that repeated completion should succeed and show “Already complete”. This resolves the investigation's product decision. The existing success behavior in COMPLETE-02 must be preserved; the distinct message is required but not implemented.

| ID | Condition or trigger | Required behavior | Source and implementation status |
| --- | --- | --- | --- |
| COMPLETE-05 | The CLI completes a task that was already complete | Succeed, leave the task complete, and show `Already complete`. | User decision on 2026-10-01. [cli.py](../tasklist/cli.py), `main`, still prints JSON as described in COMPLETE-04; [test_tasks.py](../tests/test_tasks.py), `test_repeat_completion_is_idempotent`, checks core success only. No existing test checks this message. |

The investigation is complete. The original friendly-confirmation change and required implementation and test work remain pending in the [delivery request](../delivery.md). The user's decision specifies repeated-completion wording; it does not specify first-completion wording.

## Evidence

On resumption on 2026-10-01, the working tree already contained changes to [tasks.py](../tasklist/tasks.py), [cli.py](../tasklist/cli.py), and [test_tasks.py](../tests/test_tasks.py): `complete_task` was renamed to `finish_task`, its CLI caller and tests were updated, and missing IDs now raise `ValueError("unknown task")` instead of `KeyError(task_id)`. The table describes this working tree, not just HEAD `f7d89cfa5f8fba386f4c948527e90fed04d2da18`.

After rechecking those changes for investigation closure, `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` passed all six existing tests on 2026-10-01. These tests exercise in-memory operations, including an already completed task; they do not establish CLI message behavior. This resumption changed documentation only; the pre-existing application and test edits were preserved.
