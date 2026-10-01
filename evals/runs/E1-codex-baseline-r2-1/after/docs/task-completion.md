# Task completion: current behavior

This describes the implementation in the repository, not a proposed feature.
The application stores tasks as dictionaries with `id`, `title`, and `done`.
`add_task` trims titles, rejects blank titles with `ValueError`, assigns one more
than the largest existing ID (starting at 1), appends the task, and returns it.
`list_tasks` returns shallow copies of the task dictionaries in their existing
order, including completed tasks.

## Completing a task in memory

[`complete_task(tasks, task_id)` in tasklist/tasks.py](../tasklist/tasks.py)
scans the list and updates the first task whose `id` equals `task_id`:

- Sets `done` to `True` on the original dictionary and returns that dictionary.
- Leaves its ID and title unchanged and keeps the task in the list.
- Repeating completion succeeds and leaves `done` as `True`.
- Raises `KeyError(task_id)` when no matching task exists, without modifying the list.

The function performs no disk I/O. It does not validate the list's schema or
enforce ID uniqueness; CLI argument parsing supplies an integer task ID.

## CLI and persistence

[`main()` in tasklist/cli.py](../tasklist/cli.py) accepts `add`, `list`, and
`complete`. Run from the repository root; `--file` goes before the subcommand.
For example, using a disposable file in an existing directory:

```sh
python3 -m tasklist.cli --file ./example-tasks.json add 'Review a document'
python3 -m tasklist.cli --file ./example-tasks.json complete 1
python3 -m tasklist.cli --file ./example-tasks.json list
```

If the file is absent before running this sequence, the `add` command creates
task 1, and the subsequent `complete` command prints
`{"id": 1, "title": "Review a document", "done": true}` followed by a newline.
The file contains the full JSON task array, also followed by a newline.

Each invocation loads the selected JSON file, or starts with an empty list if
it does not exist. Without `--file`, the path is `tasks.json` relative to the
current working directory. Successful `add` and `complete` operations rewrite
the whole file before printing their result as JSON. Repeated completion also
rewrites it. `list` prints the array without writing a file.

A missing ID is caught as `KeyError`: the CLI exits with status 2, writes the
error text to stderr (for ID 9, `9` followed by a newline), and does not save or
print a result. Completing against an absent file therefore fails without
creating that file. Blank-title `ValueError` is handled by the same error path.
An invalid integer argument is rejected by argparse before loading tasks.

JSON loading and file writes are outside the operation error handler. Invalid
JSON and filesystem failures are not converted to the friendly operation error.
There is no schema validation, locking, or atomic file replacement. These are
implementation boundaries, not behavior verified by the current unit suite.

## Code and test map

| Behavior | Implementation | Existing test in [tests/test_tasks.py](../tests/test_tasks.py) |
| --- | --- | --- |
| Trim title and assign initial ID | `tasks.py:add_task` | `test_add_trims_and_assigns_id` |
| Reject blank title | `tasks.py:add_task` | `test_blank_title_rejected` |
| Return copied task dictionaries | `tasks.py:list_tasks` | `test_list_returns_copies` |
| Set completion flag on result and input | `tasks.py:complete_task` | `test_complete_marks_done` |
| Allow repeated completion | `tasks.py:complete_task` | `test_repeat_completion_is_idempotent` |
| Reject absent ID | `tasks.py:complete_task` | `test_missing_id_rejected` |
| Parse ID, load/save JSON, emit output and exit status | `cli.py:main` | No CLI tests |

The suite does not directly assert returned-object identity, unchanged ID/title,
selection among multiple tasks, the missing-ID exception payload, or disk and
process behavior. Use these gaps to scope validation if a future task changes
completion; do not treat the passing unit suite as CLI integration coverage.

## Recorded validation

On 2026-10-01, from the repository root with Python 3.14.2:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Result: all 6 tests passed; exit status 0. The environment variable only prevents
bytecode cache writes. Python 3.10 is the documented minimum, but was not tested
in this run. No CLI smoke test was run. There are no additional configured local
checks or CI workflows in the repository.

CSV export remains unimplemented. Preserve the separate
[future export note](export-notes.md); it makes no delivery promise.
