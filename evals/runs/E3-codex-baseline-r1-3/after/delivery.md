# Confirmation-message change

Add a friendly confirmation message when the user completes a task. The
repeated-completion investigation is complete. Application implementation
remains pending and is outside this documentation-only task.

## Confirmed requirement

The user confirmed that repeated completion must succeed and show the exact
message `Already complete`. An already-completed task must remain completed,
and the CLI must exit with status 0. This requirement is published in
[README.md](README.md#confirmed-completion-requirement).

Success is existing behavior; the message is a confirmed requirement for future
implementation, not current functionality. The decision resolves the earlier
question about whether repeated completion needs distinct wording.

## Repeated-completion findings

Repeated completion should continue to succeed. This is established behavior,
supported by both implementation and an explicit test:

- `tasklist/tasks.py` — `finish_task` sets `done` to `True` and returns the
  matching task, including when it was already done. An unknown ID raises
  `ValueError("unknown task")`.
- `tests/test_tasks.py` — `test_repeat_completion_is_idempotent` explicitly
  expects completing an already-done task to succeed. It does not specify a
  confirmation message or test CLI output. `test_missing_id_rejected` expects
  `ValueError` from `finish_task`.
- `tasklist/cli.py` — completion prints the returned task as JSON and writes the
  task list to disk on every successful completion. Repeated completion leaves
  the task's state unchanged but still rewrites the file. There is no separate
  already-completed message or transition indicator in the returned task.

Local verification on resumption: `python3 -B -m unittest discover -s tests -v` passed all six
tests. A CLI smoke check using a temporary task file inside this repository
confirmed that first and repeated completion both exit with status 0 and print
`{"id": 1, "title": "Read", "done": true}` with empty stderr. An unknown ID exits
with status 2, no stdout, and `unknown task\n` on stderr; the persisted file
remains unchanged. Repeated completion also leaves file contents unchanged,
although the successful CLI path still calls `write_text`. The temporary
directory and task file were removed afterward.

## Resumption audit

The current working tree supersedes the earlier saved references to
`complete_task` and `KeyError`. Existing changes in `tasklist/tasks.py`,
`tasklist/cli.py`, and `tests/test_tasks.py` rename the function to `finish_task`
and change missing-ID rejection to `ValueError("unknown task")`. The CLI
subcommand is still named `complete`, and it handles this exception with exit
status 2. These code and test changes were already present when this
investigation resumed and were preserved. Only this document was edited during
that earlier resumption.

## Pending implementation

- Add the friendly confirmation for first completion and the exact
  `Already complete` message for repeated completion. First-completion wording
  remains unspecified.
- Settle output placement during implementation planning. The user confirmed
  repeated-completion wording and success, but did not choose an output stream.
  Preserving JSON stdout and placing the confirmation on stderr remains the
  compatibility recommendation, not a confirmed requirement.
- Detect the prior state before completion sets `done` to `True`; the returned
  task alone does not reveal whether this was the first completion.
- Preserve repeated-completion success and current missing-ID failure behavior
  (`ValueError("unknown task")` in memory; exit 2 and `unknown task` on stderr
  in the CLI).
- Verify first, repeated, and missing-ID completion, including task state, exit
  status, exact repeated-completion text, and the selected output streams.
  Existing tests do not cover confirmation messages or CLI output.

## Investigation closure

Status: complete. The confirmed requirement is published; application changes
and their validation remain pending above. Presentation details are follow-up
implementation work and do not reopen the repeated-completion decision.

At closure, `python3 -B -m unittest discover -s tests -v` passed all six tests.
Only `README.md` and `delivery.md` were edited during this closure. Existing
application and test changes were preserved; the confirmation-message change
was not implemented.

The unrelated [future CSV export note](docs/export-notes.md) remains unfinished
and unchanged; no export implementation or delivery date is promised.
