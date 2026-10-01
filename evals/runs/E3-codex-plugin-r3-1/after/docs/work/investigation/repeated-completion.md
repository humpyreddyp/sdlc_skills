# Repeated completion: pending product decisions

Status: partial; evidence investigation complete, awaiting the user's next-session answers. Scope is repeated completion within the [confirmation-message change](../../../delivery.md), which remains the owner of implementation work. The user requested documentation-only investigation, no application/test changes, no commits, network services, other-project inspection, or subagents, and a pause after necessary questions.

Read [published task-completion findings](../../task-completion.md) for current behavior, source/test routes, and actual checks. No available requirement settles whether repeat success should remain or receive special feedback.

## Decisions to ask together

1. Should completing an already-done task keep succeeding, or become an error? Proposal: keep success, preserving current behavior and the existing repeat test. Choosing an error changes the CLI success contract and requires revising the repeat test and defining error feedback.
2. If repeats succeed, should they use the ordinary confirmation or a distinct message such as `Task 1 is already complete.`? Proposal: use distinct feedback so the user can tell that no state transition occurred. This is not a confirmed requirement. Ordinary confirmation needs no distinction in the returned result; special feedback needs awareness of the previous done flag. If repeats become errors, this choice instead concerns error wording.
3. Should friendly feedback replace the completion JSON on stdout, or go to stderr while JSON remains on stdout? Proposal: retain JSON on stdout and send friendly feedback to stderr to preserve the current output format. Replacement changes observable output. Exact wording can follow the chosen behavior; suggested first-completion copy is `Task 1 completed.`

## Resume and handoff

- Baseline inspected: `9520c642f6eaa9004cdafac26f16238042ce754c`; the working tree was clean at investigation start. This session adds `docs/task-completion.md` and this record, and adds navigation to `README.md` and `delivery.md`. Application code and tests are unchanged; unrelated `docs/export-notes.md` is preserved.
- On resumption, read this record, the linked findings and delivery request; inspect Git status/diffs and recheck affected sources (`tasklist/tasks.py`, `tasklist/cli.py`, `tests/test_tasks.py`). Continue with the user's answers rather than restarting discovery.
- Incorporate confirmed choices into the capability explanation and delivery acceptance criteria. Keep any unanswered decisions here. Remaining application implementation and appropriate test updates belong to `delivery.md`; this investigation does not authorize them.
- When all decisions are resolved and delivery contains remaining implementation work, remove this record and update incoming links. No separate answer archive is needed.
