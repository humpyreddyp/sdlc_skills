# Confirmation-message change

Add a friendly confirmation message when the user completes a task. Investigate repeated completion before implementing the message. Application implementation remains pending.

Investigation findings are published in [task completion](docs/task-completion.md).
Repeated completion succeeds today and has explicit core test coverage; retain
that behavior as the baseline for this message change. Whether it needs distinct
wording remains a product decision. The [unfinished investigation](docs/work/investigation/repeated-completion.md)
records the decision and next actions. Implementation remains owned by this delivery task.

The rechecked working tree uses `finish_task` and rejects missing IDs with
`ValueError("unknown task")`; these existing application and test changes do not
implement the friendly message. Delivery still needs to choose repeat wording,
implement confirmation output, and verify first and repeated completion output
while preserving successful repeated completion. The existing six core tests
pass, but do not cover CLI output or persistence.
