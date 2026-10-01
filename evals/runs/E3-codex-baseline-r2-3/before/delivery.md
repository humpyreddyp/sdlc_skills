# Confirmation-message change

Add a friendly confirmation message when the user completes a task. Investigate repeated completion before implementing the message. Application implementation remains pending.

Repeated completion should continue to succeed. In [finish_task](tasklist/tasks.py), an existing task is marked done and returned even if it was already done. The explicit [test_repeat_completion_is_idempotent test](tests/test_tasks.py) requires success for an already completed task. This supports preserving the existing success behavior; it does not establish a requirement for special wording.

On resuming the investigation, the current working tree differs from the saved notes: the function is now named `finish_task`, the CLI and tests use that name, and a missing ID raises `ValueError("unknown task")` instead of `KeyError(task_id)`. The current `test_missing_id_rejected` checks for `ValueError`; it does not assert the error text. These application and test changes were already present when this investigation resumed.

The [CLI](tasklist/cli.py) currently prints the returned task as JSON and rewrites the task file on both first and repeated completion. Neither the function result nor the CLI output distinguishes those cases. Idempotence here concerns the resulting task state, not avoiding file writes. There is no friendly confirmation or special repeated-completion message yet, and the existing tests cover core behavior, not CLI wording.

Source inspection shows that a missing ID reaches the CLI's error handler, which exits with status 2 and writes `unknown task` followed by a newline to stderr. This happens before file writing and JSON output, so the missing-ID path does not rewrite the task file or print a success result. This CLI behavior has not been exercised by the existing unit tests.

Open decision for the next session: should repeated completion use the same friendly confirmation as first completion, or a distinct message such as “Task 1 was already complete”? Recommendation: use the same confirmation unless a distinct message is desired; preserve successful repeated completion either way. This recommendation is not an approved wording decision.

Status: investigation refreshed against the current working tree; implementation remains pending. This continuation is restricted to investigation, documentation, and existing local checks. The wording decision remains open. When implementation is authorized and wording is settled, resume the CLI message work, decide how the message should coexist with its existing JSON output, and verify first completion, repeated completion, and missing-ID behavior. A distinct message would require knowing whether the task was already done before completion; the returned done flag alone cannot distinguish the cases.

Validation: reran `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`; all six existing tests passed. No application code or tests were changed during this continuation; their pre-existing working-tree changes were preserved. The unrelated unfinished [CSV export note](docs/export-notes.md) remains unchanged; export is still unimplemented with no promised delivery date.
