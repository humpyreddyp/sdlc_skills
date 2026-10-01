# Confirmation-message change

Add a friendly confirmation message when the user completes a task. Investigate repeated completion before implementing the message. Application implementation remains pending.

## Repeated-completion findings

Repeated completion should continue to succeed. This is established behavior,
supported by both implementation and an explicit test:

- `tasklist/tasks.py` — `complete_task` sets `done` to `True` and returns the
  matching task, including when it was already done. An unknown ID raises
  `KeyError`.
- `tests/test_tasks.py` — `test_repeat_completion_is_idempotent` explicitly
  expects completing an already-done task to succeed. It does not specify a
  confirmation message or test CLI output.
- `tasklist/cli.py` — completion prints the returned task as JSON and writes the
  task list to disk on every successful completion. Repeated completion leaves
  the task's state unchanged but still rewrites the file. There is no separate
  already-completed message or transition indicator in the returned task.

Local verification: `python3 -B -m unittest discover -s tests -v` passed all six
tests. A CLI smoke check using a temporary task file inside this repository
confirmed that first and repeated completion both exit with status 0 and print
`{"id": 1, "title": "Read", "done": true}` with empty stderr. An unknown ID exits
with status 2 and no stdout. The temporary file was removed afterward.

## Pending decisions and resumption

No available documentation or test establishes whether repeated completion
should display a special message. Success semantics are supported by evidence;
message wording and presentation remain product decisions. Proposed wording
below is illustrative, not approved.

Questions for the next session:

1. Should repeated completion use the same confirmation as first completion
   (for example, `Task 1 is complete.`), or a distinct message such as
   `Task 1 was already complete.`?
2. Should the friendly confirmation accompany the existing JSON output on
   stderr, or replace the JSON output on stdout? Preserving JSON stdout is the
   recommended default for compatibility.

Status: investigation complete; confirmation-message implementation paused
pending these answers. No application code or tests were changed. On resumption,
resolve the questions before implementation. If distinct wording is chosen,
the implementation must distinguish the prior state before completion sets
`done` to `True`; the returned task alone does not reveal that distinction.
Preserve repeated-completion success and missing-ID failure behavior, then
verify first, repeated, and missing-ID completion and the chosen output streams.

The unrelated [future CSV export note](docs/export-notes.md) remains unfinished
and unchanged; no export implementation or delivery date is promised.
