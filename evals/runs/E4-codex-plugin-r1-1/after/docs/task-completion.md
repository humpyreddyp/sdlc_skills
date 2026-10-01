# Task completion

The local task list lets a person complete a task by numeric ID, using `python3 -m tasklist.cli --file <path> complete <id>` as described in the [README](../README.md). The [delivery request](../delivery.md) calls for a friendly confirmation message. That message is pending; current output is JSON.

## Current behavior

| ID | Condition or trigger | Behavior | Code and tests |
| --- | --- | --- | --- |
| COMPLETE-01 | Complete an existing unfinished task | Set `done` to `True` and return the matching task. | [tasks.py](../tasklist/tasks.py), `complete_task`; [test_tasks.py](../tests/test_tasks.py), `TaskTests.test_complete_marks_done`, checks returned and stored `done`. |
| COMPLETE-02 | Complete an already completed task | Succeed and leave `done` as `True`. Repeating completion is idempotent with respect to task state. | [tasks.py](../tasklist/tasks.py), `complete_task`; [test_tasks.py](../tests/test_tasks.py), `TaskTests.test_repeat_completion_is_idempotent`, supplies an already completed task and checks the returned `done` is true without an exception. |
| COMPLETE-03 | Complete an ID absent from the task list | Core raises `KeyError`; CLI exits with status 2 and an error message before saving or printing a result. | [tasks.py](../tasklist/tasks.py), `complete_task`; [cli.py](../tasklist/cli.py), `main`; [test_tasks.py](../tests/test_tasks.py), `TaskTests.test_missing_id_rejected`, checks the core exception only. |
| COMPLETE-04 | CLI completion succeeds, including a repeat | Write the task list to the JSON file and print the returned task as JSON. There is no distinct repeat message or friendly confirmation. | [cli.py](../tasklist/cli.py), `main`; no existing CLI output or persistence test. |

In `main`, the CLI reads the JSON file (or starts with an empty list if the file is absent), calls `complete_task`, saves successful mutations, and prints `json.dumps(result)`. `complete_task` searches for the ID, assigns `True` without checking the previous `done` value, and returns the same task object. Consequently, the CLI receives no indication of whether completion changed the state. A distinct repeat message would require detecting the previous state. Even a repeat rewrites the file; idempotent task state does not mean no file write.

## Evidence and delivery boundary

Successful repeated completion is supported by both implementation and an explicitly named test. Retaining success is the evidence-backed baseline for the confirmation-message change. Neither the [delivery request](../delivery.md) nor the inspected source and tests specify special repeat wording. They also do not establish a rationale for the original repeat behavior. The choice of a shared or distinct confirmation is a product decision, tracked in the [unfinished investigation](work/investigation/repeated-completion.md).

On 2026-10-01, `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` passed all six existing tests. These tests exercise the in-memory core; CLI output, exit status, and file-write statements above are based on source inspection, not executed CLI tests. No application code or tests were changed.
