# Task completion

The local task list lets a person mark a task complete by numeric ID, using `python3 -m tasklist.cli --file <path> complete <id>`. The CLI saves tasks to a local JSON file, as described in the [README](../README.md). The [delivery request](../delivery.md) calls for a friendly confirmation message; that message is not implemented.

## Current behavior

| ID | Condition or trigger | Behavior | Code and tests |
| --- | --- | --- | --- |
| completion-first | Complete an existing unfinished task | Sets `done` to `True` and returns the task. The CLI writes the tasks file, prints the returned task as JSON, and exits successfully. | [tasks.py](../tasklist/tasks.py), `complete_task`; [cli.py](../tasklist/cli.py), `main`; [test_tasks.py](../tests/test_tasks.py), `test_complete_marks_done` checks the returned and stored flags. CLI behavior was checked locally as described below. |
| completion-repeat | Complete an existing task whose `done` flag is already `True` | Succeeds and leaves the task complete. The CLI rewrites the tasks file and prints the same task JSON, with no special repeat message. | [tasks.py](../tasklist/tasks.py), `complete_task` has no prior-state branch; [cli.py](../tasklist/cli.py), `main`; [test_tasks.py](../tests/test_tasks.py), `test_repeat_completion_is_idempotent` checks that completing an already-complete task returns a true flag without raising. |
| completion-missing | Complete an ID absent from the task list | Raises `KeyError`. The CLI exits with status 2 and prints the error to stderr before writing the file or printing a result. | [tasks.py](../tasklist/tasks.py), `complete_task`; [cli.py](../tasklist/cli.py), `main`; [test_tasks.py](../tests/test_tasks.py), `test_missing_id_rejected` checks the exception. |

In `main`, the CLI loads the JSON list (or uses an empty list if the file is absent), then calls `complete_task`. The function mutates and returns the matching dictionary without reporting its previous completion state. The CLI writes the list and prints that dictionary. For a task titled `Read` with ID 1, both the first and repeated completion print `{"id": 1, "title": "Read", "done": true}`. A special repeat message would require distinguishing the prior state before it is overwritten, either in the CLI or through a revised core result.

## Requirements and limits

The friendly confirmation message is requested in [delivery.md](../delivery.md). Neither that request nor the README specifies whether repeated completion should remain successful or have different wording. The existing repeat test establishes current behavior, not product acceptance of preserving it. Both decisions remain open in the [investigation record](work/investigation/repeated-completion.md).

## Verification

On 2026-10-01, `python3 -m unittest discover -s tests -v` passed all 6 existing tests. These tests exercise the in-memory functions; they do not check CLI output, persistence, or future confirmation wording.

A local CLI smoke check used a temporary directory inside this repository and ran `add Read`, `complete 1`, `complete 1`, and `complete 9` against the same JSON file. Both valid completion calls exited 0 with identical task JSON on stdout, empty stderr, and stored `done: true`. The missing-ID call exited 2, printed `9` followed by a newline to stderr, produced no stdout, and left the stored task unchanged. The temporary directory was removed. This was a manual check, not a new automated test.
