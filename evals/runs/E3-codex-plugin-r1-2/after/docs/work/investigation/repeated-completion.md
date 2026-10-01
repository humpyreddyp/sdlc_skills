# Repeated completion: pending message decision

Status: partial; current-source recheck complete, message decision awaiting the user.

## Scope and progress

The original [confirmation-message request](../../../delivery.md) remains the
owner of application implementation. This investigation asks whether repeated
completion should succeed and whether it should display a special message.
The user authorized documentation and existing local checks only, with no
application or test changes, commits, network services, or subagents.

Supported conclusions, corrected source routes, test limits, and the six-test
passing result from the resumed check on 2026-10-01 are published in
[task completion](../../task-completion.md). Repeated success is
the existing tested baseline. Only the message decision remains unresolved;
the repository provides no distinct-repeat wording requirement.

## Decision needed

For an already completed task, should the CLI use the same friendly confirmation
as first completion, or a distinct successful message such as “Task 1 is already
complete”? Both choices preserve success. The second requires detecting the
previous completion state. Suggested wording is a proposal, not an accepted
requirement. The user may supply preferred text with the choice.

## Resume next session

1. Read this record, the linked completion page, and the delivery task. Inspect
   Git status and relevant diffs before rechecking affected conclusions.
2. Incorporate the user's message decision into the completion page and delivery
   task. If the answer leaves a necessary decision unresolved, update this record.
3. Keep implementation pending in `delivery.md`; this investigation does not
   authorize application or test edits. Delivery will need verification of first
   and repeated completion output while preserving successful repeated completion.
4. Once the decision is published and delivery contains the remaining work,
   remove this record and update its incoming links in `delivery.md` and
   `docs/task-completion.md`.

## Source context

Investigated revision: `b11001160c88cae89ace01ee791bdc9041f0986a`.
At resumption, the working tree already contained modified `README.md` and
`delivery.md`, untracked `docs/task-completion.md` and this record, and
uncommitted changes to `tasklist/cli.py`, `tasklist/tasks.py`, and
`tests/test_tasks.py`. The application/test diff renames `complete_task` to
`finish_task` in the implementation, CLI, and tests, and changes missing-ID
rejection from `KeyError(task_id)` to `ValueError("unknown task")` with a matching
test expectation. The current published findings include those changes;
application code and tests were not edited during this resumption.
Recheck `tasklist/cli.py` (`main`), `tasklist/tasks.py` (`finish_task`), and
`tests/test_tasks.py` (`test_complete_marks_done`,
`test_repeat_completion_is_idempotent`, `test_missing_id_rejected`) if sources
change. `docs/export-notes.md` is unrelated and remains intact.
