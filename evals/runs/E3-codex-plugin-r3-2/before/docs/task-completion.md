# Task completion

The local task-list CLI lets a user mark a task done by its numeric ID. Run `python3 -m tasklist.cli --file tasks.json complete 1` from the repository root to complete task 1 in that file. The [confirmation-message delivery request](../delivery.md) asks for friendly feedback; that change has not been implemented.

## Current behavior

| ID | Condition or trigger | Behavior | Code and tests |
| --- | --- | --- | --- |
| completion-1 | Complete an existing unfinished task | Set `done` to `True` and return the matching task. | [tasks.py](../tasklist/tasks.py), `complete_task`; [test_tasks.py](../tests/test_tasks.py), `test_complete_marks_done` checks the returned and stored done flags. |
| completion-2 | Complete an already-done task | Succeed and leave `done` as `True`. Repeating completion has the same effect on task state (idempotence). | [tasks.py](../tasklist/tasks.py), `complete_task` does not branch on the prior done flag; [test_tasks.py](../tests/test_tasks.py), `test_repeat_completion_is_idempotent` checks that an already-done task can be completed and returns a true done flag. |
| completion-3 | CLI completion succeeds, including a repeat | Rewrite the JSON file, print the returned task as JSON, and exit successfully. There is no friendly confirmation or special repeat message. | [cli.py](../tasklist/cli.py), `main` loads tasks, calls `complete_task`, writes the file, and prints JSON. No existing CLI/output unit test; local CLI verification below. |
| completion-4 | No task matches the ID | Raise `KeyError`; the CLI exits with code 2 and writes the error to stderr before any file write. | [tasks.py](../tasklist/tasks.py), `complete_task`; [cli.py](../tasklist/cli.py), `main`; [test_tasks.py](../tests/test_tasks.py), `test_missing_id_rejected` checks the core exception. |

The core completion function returns the task after setting its done flag. Its return value does not distinguish first completion from a repeat. If delivery adopts distinct feedback, it will need to determine the previous state before mutation or otherwise expose whether a transition occurred.

## Evidence and requirement boundary

[delivery.md](../delivery.md) confirms the request for a friendly confirmation and requires investigation before implementation. It does not specify repeat success, special repeat wording, or how the message should coexist with JSON output. The implementation and repeat unit test establish current behavior, not product acceptance of keeping it. Those decisions remain in the [unfinished investigation](work/investigation/repeated-completion.md).

On 2026-10-01, `python3 -m unittest discover -s tests -v` passed all six existing tests. A local CLI check using a temporary JSON file inside the repository added `Read`, completed ID 1 twice, then attempted ID 9. Both completions exited 0 and printed `{"id": 1, "title": "Read", "done": true}`; saved task content stayed the same after the repeat. ID 9 exited 2 with stderr `9` and left the saved content unchanged. The temporary file was removed. This verifies current behavior only; the suite has no confirmation-message assertions.
