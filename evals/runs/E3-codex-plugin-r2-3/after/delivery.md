# Confirmation-message change

Add a friendly confirmation message when the user completes a task. Investigate repeated completion before implementing the message. Application implementation remains pending.

Investigation is complete. The [confirmed requirement, COMPLETE-05](docs/task-completion.md#confirmed-requirement-and-delivery-boundary) records the user's decision on repeated completion. That page distinguishes current JSON output from the required message and documents the existing test coverage. Application implementation remains pending under this delivery request.

Remaining delivery work:

- Implement friendly confirmation for first completion and the confirmed repeated-completion message, preserving successful repeated completion. First-completion wording has not been specified.
- Distinguish the task's prior completion state before `finish_task` sets `done=True`, or carry that distinction to the CLI message logic. The current returned task alone cannot distinguish first from repeated completion.
- Add CLI coverage for first and repeated completion, including successful exit, the required repeated-completion wording, and persisted completion state. Preserve core idempotency and missing-ID behavior; run the existing suite and new tests.
- Update the capability page's current-behavior and verification evidence after implementation. The six existing in-memory tests passed on 2026-10-01, but do not verify CLI output or persistence.

Continue from the existing uncommitted `finish_task` rename and `ValueError("unknown task")` missing-ID change documented in the capability page. Investigation closure made documentation changes only; it did not implement or test the new message.
