# Task completion

One person can mark a local task complete by numeric ID. The CLI persists successful changes to JSON; the core function works on an in-memory list.

| ID | Condition | Behavior | Code and tests |
| --- | --- | --- | --- |
| COMP-01 | Existing not-done ID | Sets `done` to `True` in the supplied list and returns that task | [tasks.py — complete_task](../tasklist/tasks.py); [TaskTests.test_complete_marks_done](../tests/test_tasks.py) checks the returned and stored flag |
| COMP-02 | Missing ID | Raises `KeyError(task_id)` without changing the list | [tasks.py — complete_task](../tasklist/tasks.py); [TaskTests.test_missing_id_rejected](../tests/test_tasks.py) checks the exception for an empty list, not preservation of a populated list |
| COMP-03 | Already done ID | Succeeds and returns the task with `done=True`; repeating completion leaves its state unchanged | [tasks.py — complete_task](../tasklist/tasks.py); [TaskTests.test_repeat_completion_is_idempotent](../tests/test_tasks.py) checks successful completion of an already-done task |
| COMP-04 | CLI completion succeeds | Writes the whole task list to the selected JSON file, then prints the completed task as JSON | [cli.py — main](../tasklist/cli.py); no existing CLI persistence test |
| COMP-05 | CLI completion cannot find the ID | Exits with status 2 and an error on stderr, before writing the file or printing a result | [cli.py — main](../tasklist/cli.py), handling `KeyError`; the core missing-ID test above does not check CLI status or file contents |

For example, completing task 1 twice returns the same task with `done=true` each time. The CLI writes the file on both successful calls.

## Implementation route

[cli.py — main](../tasklist/cli.py) parses `complete <task_id>` as an integer and selects `--file`, defaulting to `tasks.json` in the working directory. It loads an existing file with `json.loads`, or starts with an empty list if the file is absent. It passes that list and ID to [tasks.py — complete_task](../tasklist/tasks.py), which scans for the first matching ID, changes that dictionary, and returns it. The core function does no file I/O.

After a successful completion, `main` serializes the whole list with a trailing newline and prints the returned task as JSON. A missing file therefore leads to a missing-ID error on completion and is not created. The dispatch catches `ValueError` and `KeyError`; file loading, JSON parsing, and file writing are outside that handler. Do not assume every failure gets its controlled exit-status-2 message. These CLI paths are inspected behavior, not covered by the existing tests.

The same core module supplies the surrounding workflow: `add_task` trims titles, rejects blank titles, and assigns one greater than the largest existing ID (starting at 1); `list_tasks` returns shallow dictionary copies. In [tests/test_tasks.py](../tests/test_tasks.py), `TaskTests.test_add_trims_and_assigns_id` checks trimming and the first ID, `test_blank_title_rejected` checks rejection, and `test_list_returns_copies` checks that changing a returned `done` flag does not affect the original task. Larger-list ID allocation is not tested. The CLI's `list` command prints JSON without writing the file.

## Verification limits

The existing suite tests core operations only. It does not exercise argument parsing, CLI output or exit status, persistence across commands, invalid JSON, or file I/O failures. The implementation assumes task dictionaries have the expected keys; there is no explicit stored-data schema validation in the loader. See [working instructions and recorded check results](../README.md#verification-and-readiness) before changing completion or persistence.
