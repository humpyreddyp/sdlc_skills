# Task completion: current behavior

This document describes the checked-in implementation, not planned features.
The application is a local, single-user CLI with in-memory core functions and
JSON persistence. It has no web service or multi-user database.

## Data and core operations

Tasks are dictionaries with `id`, `title`, and `done` fields, stored in a list.
[tasklist/tasks.py](../tasklist/tasks.py) contains all three core operations:

- `add_task(tasks, title)` strips surrounding whitespace and rejects an empty
  result with `ValueError("title must not be blank")`. It assigns the current
  maximum ID plus one (starting at 1), appends a task with `done=False`, and
  returns that same dictionary.
- `list_tasks(tasks)` returns a new list of shallow dictionary copies, in the
  existing order. It includes both open and completed tasks.
- `complete_task(tasks, task_id)` finds the first task whose ID equals
  `task_id`, sets its `done` field to `True` in place, and returns that same
  dictionary. Its ID, title, and list position are unchanged. Completing an
  already completed task succeeds again. If no ID matches, it raises
  `KeyError(task_id)` without changing the list.

The core functions do not read or write files. They assume the supplied task
data has the expected structure; there is no general schema validation. The
CLI converts completion IDs to integers, while the core uses direct equality.

## CLI completion and persistence

[tasklist/cli.py](../tasklist/cli.py), in `main()`, defines `add`, `list`, and
`complete` subcommands. Put the global `--file` option before the subcommand:

```sh
python3 -m tasklist.cli --file ./example-tasks.json complete 1
```

Use an existing task file containing ID 1 for this example, or first add a task
to a disposable file. Without `--file`, the CLI uses `tasks.json` in the current
working directory.

1. The CLI loads the whole JSON file, or starts with an empty list if it does
   not exist.
2. `complete` calls `complete_task` with the parsed integer ID.
3. On success, it rewrites the whole task list as JSON with a trailing newline,
   then prints the completed task as JSON to standard output. Repeated
   completion also rewrites the file. For example, a task titled `Read` with
   ID 1 produces `{"id": 1, "title": "Read", "done": true}`.
4. A missing ID is caught as `KeyError`: the CLI exits with status 2 and writes
   the error text to standard error. It neither saves the file nor prints a
   successful result. A nonexistent file therefore remains absent after a
   failed completion.

`add` also saves after success; `list` only prints its result and does not save.
Malformed integer arguments are rejected by `argparse`. JSON loading happens
outside the operation error handler, and file writes happen after it: malformed
JSON and file I/O failures are not converted into the handled task-error path.
Writes are direct, with no atomic replacement or concurrency protection.

## Code and test map

All current tests are methods of `TaskTests` in
[tests/test_tasks.py](../tests/test_tasks.py).

| Behavior | Implementation | Existing test |
| --- | --- | --- |
| Trim title and assign initial ID | `add_task` | `test_add_trims_and_assigns_id` |
| Reject blank title | `add_task` | `test_blank_title_rejected` |
| Return copies when listing | `list_tasks` | `test_list_returns_copies` |
| Mark a task done and mutate its dictionary | `complete_task` | `test_complete_marks_done` |
| Allow repeated completion | `complete_task` | `test_repeat_completion_is_idempotent` |
| Reject a missing ID | `complete_task` | `test_missing_id_rejected` |

These are in-memory unit tests. There are no existing tests for CLI parsing,
exit codes, output, JSON persistence, or file errors. The missing-ID test uses
an empty list; the suite does not verify selection among multiple tasks or
unchanged neighboring tasks. CLI behavior above was established by reading
the implementation, not by an automated CLI check.

## Local check result

On 2026-10-01, from the repository root, using Python 3.14.2:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Result: **6 tests passed**, exit status **0**. This verifies the existing suite
in that environment; other Python versions were not checked. No additional
lint, type-check, build, or CI configuration is present in the repository.

CSV export remains unimplemented. See the preserved
[future export note](export-notes.md) for the proposal.
