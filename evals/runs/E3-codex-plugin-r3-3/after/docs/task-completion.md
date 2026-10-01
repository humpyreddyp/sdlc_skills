# Task completion

The local task-list CLI lets a user mark a task done by its numeric ID. Run `python3 -m tasklist.cli --file tasks.json complete 1` from the repository root to complete task 1 in that file. The [confirmation-message delivery request](../delivery.md) asks for friendly feedback; that change has not been implemented.

## Current behavior

| ID | Condition or trigger | Behavior | Code and tests |
| --- | --- | --- | --- |
| completion-1 | Complete an existing unfinished task | Set `done` to `True` and return the matching task. | [tasks.py](../tasklist/tasks.py), `finish_task`; [test_tasks.py](../tests/test_tasks.py), `test_complete_marks_done` checks the returned and stored done flags. |
| completion-2 | Complete an already-done task | Succeed and leave `done` as `True`. Repeating completion has the same effect on task state (idempotence). | [tasks.py](../tasklist/tasks.py), `finish_task` does not branch on the prior done flag; [test_tasks.py](../tests/test_tasks.py), `test_repeat_completion_is_idempotent` checks that an already-done task can be completed and returns a true done flag. |
| completion-3 | CLI completion succeeds, including a repeat | Rewrite the JSON file, print the returned task as JSON on stdout, and exit successfully. There is no friendly confirmation or special repeat message. | [cli.py](../tasklist/cli.py), `main` loads tasks, calls `finish_task`, writes the file, and prints JSON. No existing CLI/output unit test; local CLI verification below. |
| completion-4 | No task matches the ID | Raise `ValueError("unknown task")`; the CLI exits with code 2, writes `unknown task` to stderr, emits no stdout, and does not write the file. | [tasks.py](../tasklist/tasks.py), `finish_task`; [cli.py](../tasklist/cli.py), `main`; [test_tasks.py](../tests/test_tasks.py), `test_missing_id_rejected` checks the core exception type, but not its message. |

The core completion function returns the task after setting its done flag. Its return value does not distinguish first completion from a repeat. To implement the confirmed distinct feedback, delivery will need to determine the previous state before mutation or otherwise expose whether a transition occurred.

## Confirmed requirement and delivery boundary

The user confirmed on 2026-10-01: repeated completion should succeed and show `Already complete`. For `completion-2`, this confirms success with the task remaining done. For `completion-3`, this requires distinct repeat feedback that the current CLI does not yet provide. The existing repeat test checks the done flag, not the required message.

The repeated-completion investigation is complete. [delivery.md](../delivery.md) retains the original friendly-confirmation request, acceptance criteria, pending implementation and verification, and the still-unspecified relationship between friendly feedback and JSON output. Neither stdout versus stderr nor first-completion wording was confirmed by this decision. These delivery details do not change the confirmed repeat behavior; no application change was made as part of this investigation.

## Verification context

On resumption on 2026-10-01, the inspected working tree at base revision `9520c642f6eaa9004cdafac26f16238042ce754c` already contained uncommitted changes renaming `complete_task` to `finish_task` and changing the missing-ID exception from `KeyError` to `ValueError("unknown task")`, with corresponding CLI and test updates. The behavior table reflects those working-tree sources, not just the committed revision. Those pre-existing application and test changes were preserved.

`python3 -B -m unittest discover -s tests -v` passed all six existing tests on resumption. A local CLI check using a temporary JSON file inside the repository added `Read`, completed ID 1 twice, then attempted ID 9. Both completions exited 0, printed `{"id": 1, "title": "Read", "done": true}` on stdout, and emitted no stderr; saved task content stayed the same after the repeat. ID 9 exited 2 with stderr `unknown task`, emitted no stdout, and left the saved content unchanged. The temporary directory was removed. This verifies current behavior only; the suite has no confirmation-message assertions.
