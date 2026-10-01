# Task completion

The local task-list CLI lets a person mark an existing task done by its numeric ID.
The [README](../README.md) describes this journey. The
[delivery request](../delivery.md) asks for a friendly confirmation message;
that message is pending implementation.

## Current behavior

These are implementation findings and existing test expectations, not a new
decision about message wording.

| ID | Condition or trigger | Behavior | Code and tests |
| --- | --- | --- | --- |
| COMPLETE-01 | Complete an existing unfinished task | Set `done` to `True` and return the task. The CLI writes the task list to its JSON file and prints the returned task as JSON. | [tasks.py](../tasklist/tasks.py), `finish_task`; [cli.py](../tasklist/cli.py), `main`. [test_tasks.py](../tests/test_tasks.py), `test_complete_marks_done`, checks the returned and stored `done` flags; it does not exercise the CLI. |
| COMPLETE-02 | Complete an already completed task | Succeed and leave `done` true. The core takes the same path as first completion; the CLI rewrites the file and prints the task as JSON, with no special message. | [tasks.py](../tasklist/tasks.py), `finish_task`; [cli.py](../tasklist/cli.py), `main`. [test_tasks.py](../tests/test_tasks.py), `test_repeat_completion_is_idempotent`, starts with `done=True` and checks the returned flag remains true without an exception. It does not check output, file writes, or two successive CLI calls. |
| COMPLETE-03 | Complete an ID absent from the task list | The core raises `ValueError("unknown task")`. The CLI exits with status 2 and writes `unknown task` followed by a newline to stderr before writing the file or printing a result. | [tasks.py](../tasklist/tasks.py), `finish_task`; [cli.py](../tasklist/cli.py), `main`. [test_tasks.py](../tests/test_tasks.py), `test_missing_id_rejected`, checks the core exception type only, not its text or CLI handling. |

The CLI parses `complete <task_id>`, loads the selected JSON file (or starts with
an empty list if it does not exist), then calls `finish_task`. That function
matches the ID, assigns `done=True`, and returns the same task object. It does not
return whether the task was already done. Distinct repeat wording would therefore
need a way to retain or expose the previous state before that assignment.

Repeated completion should remain successful for the confirmation-message change:
the implementation and explicitly named repeat test support that baseline, and
the delivery request does not ask to change it. There is no confirmed requirement
for distinct repeat wording or exact message text. The
[open decision](work/investigation/repeated-completion.md) belongs to the existing
delivery task. Rejecting repeated completion would change the current tested
behavior; adding a special success message would change presentation while keeping
completion successful.

## Verification

On resumption on 2026-10-01, `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`
passed all six existing tests against the working tree based on revision
`b11001160c88cae89ace01ee791bdc9041f0986a`. Pre-existing uncommitted changes in
`tasklist/tasks.py`, `tasklist/cli.py`, and `tests/test_tasks.py` rename
`complete_task` to `finish_task` and replace the missing-ID `KeyError` with
`ValueError("unknown task")`, updating the caller and test expectations. These
findings describe that working tree; this investigation did not edit application
code or tests. The suite exercises the in-memory operations only. CLI output,
exit status, and persistence above were established by source inspection, not an
executed CLI test. No friendly-message behavior has been implemented or tested.
