# Confirmation-message change

Add a friendly confirmation message when the user completes a task. Investigate repeated completion before implementing the message. Application implementation remains pending.

The repeated-completion investigation is complete. Current behavior, supporting evidence, and the user's confirmed requirement are published in [task completion](docs/task-completion.md#confirmed-requirement). This delivery task retains ownership of the pending application change.

Remaining implementation and verification work:

- Add the friendly confirmation for first completion; choose its wording during delivery, since the repeat decision does not specify it.
- Distinguish first completion from repeated completion using the prior task state or an explicit result from `finish_task`. Preserve repeated success and display the confirmed repeat message documented above.
- Add CLI verification for first and repeated completion, including success status, persisted completion state, and confirmation output. Check the exact confirmed repeat wording and retain missing-ID error coverage.
- Run `python3 -B -m unittest discover -s tests -v` after implementation. All six existing tests passed during the investigation on 2026-10-01, but none covers CLI messages, exit status, or persistence.

The existing uncommitted application/test changes rename `complete_task` to `finish_task` and change missing-ID handling to `ValueError("unknown task")`; they do not implement the confirmation messages. This investigation made documentation changes only.
