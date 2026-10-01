# Task completion

The local task-list CLI lets a person mark a task complete by numeric ID. The [README](../README.md) describes the command and local JSON storage. The [delivery request](../delivery.md) calls for a friendly confirmation message; that message has not been implemented.

## Current behavior

These findings describe the inspected implementation. Confirmed requirements for the pending change appear below. Successful CLI results assume the JSON file can be read and written.

| ID | Condition or trigger | Behavior | Code and tests |
| --- | --- | --- | --- |
| completion-first | Complete an existing unfinished task | Sets `done` to `True` and returns the task. The CLI persists the task list, prints the returned task as JSON, and exits successfully. | [tasks.py](../tasklist/tasks.py), `finish_task`; [cli.py](../tasklist/cli.py), `main`; [test_tasks.py](../tests/test_tasks.py), `TaskTests.test_complete_marks_done` checks the return value and in-memory mutation. CLI persistence and output are established by code inspection, not this test. |
| completion-repeat | Complete an existing task whose `done` is already `True` | Succeeds and leaves `done` true. The CLI still writes the task list and prints the same task JSON; it has no special repeated-completion message. | [tasks.py](../tasklist/tasks.py), `finish_task`; [cli.py](../tasklist/cli.py), `main`; [test_tasks.py](../tests/test_tasks.py), `TaskTests.test_repeat_completion_is_idempotent` starts with an already-completed task and checks that the returned `done` is true. It does not exercise the CLI or assert wording. |
| completion-missing | Complete an ID absent from the task list | The core function raises `ValueError("unknown task")`. The CLI catches it, exits with status 2, and writes `unknown task` followed by a newline to stderr before reaching the file-write or success-output steps. | [tasks.py](../tasklist/tasks.py), `finish_task`; [cli.py](../tasklist/cli.py), `main`; [test_tasks.py](../tests/test_tasks.py), `TaskTests.test_missing_id_rejected` checks the core `ValueError` type, not its message or the CLI behavior. |

For example, completing task 1 titled `Read` prints `{"id": 1, "title": "Read", "done": true}` on both first and repeated completion. There is no friendly confirmation text in either case today.

## Confirmed requirement

For `completion-repeat`, completing an already-completed task must succeed, leave it complete, and show the distinct message `Already complete`. The user confirmed the success policy and this wording on 2026-10-01. Current code satisfies the success policy but does not display the required message; the existing repeat test establishes only the returned completion state.

The original request for a friendly confirmation on first completion also remains in scope. Its exact wording was not specified by this decision. Implementation and verification remain pending in the [delivery task](../delivery.md); the repeated-completion investigation is complete.

## Implementation route and change implications

`main` parses `complete <task_id>`, loads the JSON list (or uses an empty list if the file does not exist), and calls `finish_task`. That function finds the matching ID, unconditionally assigns `done = True`, and returns the same task object. It does not report whether this invocation changed the task's state. The CLI then writes the list and prints the result with `json.dumps`.

The required distinct repeat message needs the task's state before mutation, or an explicit indication of whether completion changed it; the returned `done` value alone cannot distinguish the cases. The implementation approach remains delivery work.

## Evidence and limits

On resumption on 2026-10-01, `python3 -B -m unittest discover -s tests -v` passed all six existing tests against the current working tree. No existing test covers CLI exit status, persistence, output, or confirmation wording; those current CLI findings come from inspecting `main`.

The inspected working tree differs from commit `d5148499135549644556c204300f3b3827898a30`: the completion function was renamed from `complete_task` to `finish_task`, the CLI and tests now call it, and missing IDs raise `ValueError("unknown task")` instead of `KeyError(task_id)`. The missing-ID test now expects `ValueError`. These application and test edits were already present on resumption; this investigation only updates documentation. The behavior IDs above remain unchanged.

The passing checks establish current core behavior only; they do not verify the pending confirmation messages. The confirmed repeat requirement above comes from the user's decision, not from those checks.
