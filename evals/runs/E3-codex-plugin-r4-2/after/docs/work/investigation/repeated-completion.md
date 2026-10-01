# Repeated completion: awaiting product decision

Scope: investigate whether completing an already-completed task should succeed and whether it should display a special message, as part of the [confirmation-message delivery task](../../../delivery.md). Evidence review has been refreshed on resumption; intent remains unresolved. The grouped decision below has been asked again; no answer has yet been received.

Read [published completion behavior](../../task-completion.md) first for current behavior, implementation routes, test coverage, and the six-test passing result. No repository evidence inspected establishes the intended repeat policy or message.

## Decision to ask together

Should repeated completion:

1. **Succeed with a distinct message (proposal):** keep successful repeated completion and say, for example, `Task 1 was already complete.` This preserves current success behavior and makes clear that the task was already done; implementation must distinguish the prior state.
2. **Succeed with the same confirmation:** preserve success and show the ordinary completion confirmation on repeats too; no repeat-specific wording is needed.
3. **Be rejected:** treat an already-completed task as an error; this changes current behavior and requires revisiting the existing repeat test and defining the rejection message/status during delivery.

Neither success nor special wording has been confirmed. The example text is a proposal, not approved copy. The user may specify another policy or wording.

## Resume next session

1. Read this record and the published page, then inspect Git status/diffs and recheck affected sources. HEAD remains `d5148499135549644556c204300f3b3827898a30`. On resumption, existing uncommitted changes in `tasklist/tasks.py`, `tasklist/cli.py`, and `tests/test_tasks.py` rename `complete_task` to `finish_task` and change missing-ID handling from `KeyError(task_id)` to `ValueError("unknown task")`, including the test expectation. Those changes have been inspected, published, and checked with all six existing tests passing on 2026-10-01; they do not resolve repeat intent. Documentation changes are in `README.md`, `delivery.md`, `docs/task-completion.md`, and this record. No application or test files were edited by this investigation.
2. Apply the user's answer to both the repeat success policy and message distinction. If the answer leaves either unresolved, keep that question open here. Incorporate confirmed intent into the published page, clearly separate from current implementation.
3. Record the resulting implementation and verification work in the existing delivery task. This investigation does not authorize changing application code or tests. Preserve `docs/export-notes.md`, which concerns unrelated future work.
4. When intent is resolved and remaining implementation work has its delivery home, remove this record and update its incoming links in the published page and delivery task. Pending implementation alone does not keep the investigation open.

Session constraints: work only in this repository and installed skill resources; no subagents, network services, commits, or application/test edits. Documentation edits and existing local checks are allowed.
