# Repeated completion: awaiting product decisions

## Scope and progress

Investigate whether repeated completion should succeed and display a special message as part of the [confirmation-message change](../../../delivery.md). The user requested a pause after necessary questions and will answer next session. Work is limited to this repository and installed skill resources: no subagents, network services, commits, or application/test edits. Documentation edits and existing local checks are allowed.

The evidence investigation is complete; product intent remains unresolved. Read [task completion](../../task-completion.md) for current behavior, code/test references, and actual verification results. No application implementation has been performed. Preserve the unrelated [future export note](../../export-notes.md).

## Decisions awaiting the user

1. Should completing an already-complete task continue to succeed, or should it be rejected? Keeping success preserves the current CLI exit status and core repeat behavior. Rejection changes the operation's contract and requires changing the repeat test and defining the CLI error behavior.
2. Should repeated completion display a special message, such as `Task 1 is already complete.`, or use the ordinary completion confirmation? A distinct message requires detecting the previous state; ordinary wording does not distinguish a new completion from a repeat. If rejection is chosen, the repeat text should describe that error.

Proposal, not an accepted requirement: preserve successful repeated completion and use the distinct already-complete message. Repeating the command still achieves the requested state, while the text accurately describes that no new completion occurred. Existing code/tests support the compatibility argument but cannot settle the product decision.

## Source context and resumption

Inspected at revision `cf0709365aa93fe5895dd547fad4a04536cc5af6`; the working tree was clean before this investigation. Relevant sources are `tasklist/tasks.py` (`complete_task`), `tasklist/cli.py` (`main`), `tests/test_tasks.py` (completion, repeat, and missing-ID tests), `README.md`, and `delivery.md`.

Uncommitted documentation changes from this investigation: navigation in `README.md`, decision/ownership links in `delivery.md`, the published `docs/task-completion.md`, and this record. Application code and tests are unchanged. The existing suite passed all 6 tests, and the local CLI smoke check is recorded in the published page.

Next session, read this record and the published page, inspect Git status and relevant diffs, and recheck affected sources before incorporating the user's answers. Publish confirmed decisions with attribution to the user's answer, update the delivery task with the resulting implementation and validation requirements, and leave implementation with that task. Once these questions are resolved and all remaining work has a home in `delivery.md`, remove this record and update its incoming links. Do not treat the proposed behavior as accepted in the absence of an answer.
