# Repeated completion: pending message decision

Status: partial; paused for the user's answer next session. Scope is the repeated-completion question within the [confirmation-message delivery request](../../../delivery.md). Keep the original friendly-confirmation request and its implementation work there.

## Established progress

[Task completion behavior](../../task-completion.md) publishes the inspected implementation, existing test coverage, and passing six-test check. Repeated completion succeeds today and has explicit core test coverage. Preserve that success behavior for this message change unless the user explicitly requests a contract change. No evidence settles whether its friendly message should differ.

## Open decision

Should successful repeated completion use the same friendly confirmation as first completion, or a distinct message such as `Task 1 is already complete`? The example is proposed wording only.

- Same confirmation: keep a uniform success message; no need to distinguish prior completion state for wording.
- Distinct confirmation: still succeed, but communicate that no completion-state change was needed. Delivery must distinguish the prior state before `complete_task` sets `done=True`, or otherwise carry that distinction to the message logic; the current return value alone does not distinguish the two cases.

This is a product wording decision, not a missing dependency or failing check. The user requested a pause after necessary questions and will answer next session.

## Resume and remaining work

1. Read this record, the capability page, and delivery request. Check Git status and relevant diffs, then recheck affected evidence before using the user's answer.
2. Incorporate the decision into the capability page and delivery request as a confirmed requirement. Keep current behavior separate from pending implementation.
3. Leave application implementation and any needed core/CLI tests with `delivery.md`. This session authorizes documentation and existing local checks only, and prohibits application/test edits, commits, network services, subagents, and inspection outside this repository and installed skill resources.
4. Once the decision is published and remaining implementation work is captured in delivery, remove this record and update its incoming links in the capability page and delivery request.

## Source context

Investigated on 2026-10-01 at HEAD `f7d89cfa5f8fba386f4c948527e90fed04d2da18`. The working tree was clean at the start. Session changes are documentation only: navigation in `README.md`, progress in `delivery.md`, new `docs/task-completion.md`, and this record. `docs/export-notes.md` remains unchanged.

Relevant sources: [CLI `main`](../../../tasklist/cli.py), [core `complete_task`](../../../tasklist/tasks.py), and [tests](../../../tests/test_tasks.py), especially `test_complete_marks_done`, `test_repeat_completion_is_idempotent`, and `test_missing_id_rejected`. No CLI tests or approved repeat-specific wording were found in the repository.
