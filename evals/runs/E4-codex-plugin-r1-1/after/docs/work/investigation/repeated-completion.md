# Repeated completion: pending message decision

Status: partial; paused for a user decision, to be answered next session.

Scope: investigate whether repeated completion should succeed and whether it should display a special message within the original [confirmation-message delivery task](../../../delivery.md). Do not implement application changes under this investigation.

## Progress and decision

[Published completion findings](../../task-completion.md) record the implementation, explicit repeat test, CLI behavior, and successful six-test run. Repeated completion success is the evidence-backed baseline; no change to success semantics is needed for the message request. A special message is not specified by available evidence.

Open question for the user: keeping repeated completion successful, should it show the same friendly confirmation as a first completion, or a distinct message such as “Task 1 is already complete”?

- Same confirmation: use a common success message for both cases; no previous-state distinction is needed for wording.
- Distinct confirmation: detect whether the task was already complete and select repeat-specific wording while retaining success.

The example text is a proposal, not a confirmed requirement. There is no user answer yet. Message implementation and coverage remain pending in the delivery task.

## Resume

1. Read this record, the linked findings, and `delivery.md`; inspect Git status and relevant diffs, then recheck affected conclusions against `tasklist/tasks.py`, `tasklist/cli.py`, and `tests/test_tasks.py`.
2. Incorporate the user's message choice into the delivery requirements and the completion explanation, clearly separating the chosen requirement from current implementation. If the answer leaves a necessary decision unresolved, keep it here.
3. Leave implementation and message coverage with `delivery.md`. Once the question is resolved and all remaining work has a durable home there, remove this record and update incoming links in `delivery.md` and `docs/task-completion.md`.

Source context: inspected HEAD `334cd3b134b10291818f46f26cda5c689193d400`; the working tree was clean at investigation start. This session modifies only documentation: navigation in `README.md`, findings and continuity links in `delivery.md`, and new `docs/task-completion.md` and this record. No source or test modifications, commits, network services, or subagents were used. `docs/export-notes.md` remains unrelated future work and is unchanged.
