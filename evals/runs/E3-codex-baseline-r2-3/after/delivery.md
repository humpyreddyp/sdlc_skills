# Confirmation-message change

Add a friendly confirmation message when the user completes a task. Investigation is complete. Application implementation remains pending and is not authorized in this continuation.

Confirmed user decision: repeated completion must succeed, leave the task complete, and show the exact message “Already complete”. This requirement is published in the [README](README.md#confirmed-completion-requirement). In [finish_task](tasklist/tasks.py), an existing task is marked done and returned even if it was already done. The explicit [test_repeat_completion_is_idempotent test](tests/test_tasks.py) requires success for an already completed task. The message requirement comes from the user's decision; the existing test establishes only successful repeated completion.

On resuming the investigation, the current working tree differs from the saved notes: the function is now named `finish_task`, the CLI and tests use that name, and a missing ID raises `ValueError("unknown task")` instead of `KeyError(task_id)`. The current `test_missing_id_rejected` checks for `ValueError`; it does not assert the error text. These application and test changes were already present when this investigation resumed.

The [CLI](tasklist/cli.py) currently prints the returned task as JSON and rewrites the task file on both first and repeated completion. Neither the function result nor the CLI output distinguishes those cases. Idempotence here concerns the resulting task state, not avoiding file writes. There is no friendly confirmation or special repeated-completion message yet, and the existing tests cover core behavior, not CLI wording.

Source inspection shows that a missing ID reaches the CLI's error handler, which exits with status 2 and writes `unknown task` followed by a newline to stderr. This happens before file writing and JSON output, so the missing-ID path does not rewrite the task file or print a success result. This CLI behavior has not been exercised by the existing unit tests.

The repeated-completion wording decision is closed. “Already complete” supersedes the earlier recommendation to use the same confirmation for both cases. First-completion wording and how confirmations should coexist with existing JSON output remain implementation details to settle; they do not reopen the confirmed repeated-completion requirement.

Status: investigation finished against the current working tree; implementation remains pending. This continuation is restricted to investigation, documentation, and existing local checks. Resume the following work when implementation is authorized:

- Determine whether the task was already done before completion; the returned done flag alone cannot distinguish first and repeated completion.
- Add the friendly first-completion confirmation and the exact repeated-completion message “Already complete”, preserving successful repeated completion and the completed task state. Settle first-completion wording and how messages coexist with JSON output.
- Verify first completion, successful repeated completion with the exact message, and missing-ID behavior. Preserve the missing-ID error path without a success confirmation. Existing core tests do not verify CLI messages; CLI verification remains pending.

Validation: reran `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`; all six existing tests passed. No application code or tests were changed during this continuation; their pre-existing working-tree changes were preserved. The unrelated unfinished [CSV export note](docs/export-notes.md) remains unchanged; export is still unimplemented with no promised delivery date.
