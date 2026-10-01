# Confirmation-message change

Add a friendly confirmation message when the user completes a task. Investigate repeated completion before implementing the message. Application implementation remains pending.

Investigation is complete. Current behavior and the user's confirmed requirement
for repeated completion are published in
[task completion](docs/task-completion.md#confirmed-requirement).
Implementation remains owned by this delivery task and is pending.

The rechecked working tree uses `finish_task` and rejects missing IDs with
`ValueError("unknown task")`; these existing application and test changes do not
implement the friendly message. The existing six core tests passed on 2026-10-01,
but do not cover CLI output or persistence.

Remaining delivery work:

- Retain or expose the completion state before `finish_task` assigns `done=True`
  so the CLI can distinguish first and repeated completion.
- Implement the friendly first-completion confirmation and the confirmed repeat
  message. First-completion wording is not specified by the repeat decision.
- Verify first and repeated completion output, successful exit status, and
  persisted `done=True`, including two successive CLI completion calls. Preserve
  missing-ID rejection and the existing core behavior.

Application and test changes are outside this investigation's authorized scope;
no confirmation-message implementation or new tests were added.
