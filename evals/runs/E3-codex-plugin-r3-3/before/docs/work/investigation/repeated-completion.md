# Repeated completion: pending product decisions

Status: partial; evidence rechecked on resumption on 2026-10-01, awaiting answers to the three product decisions below. Scope is repeated completion within the [confirmation-message change](../../../delivery.md), which remains the owner of implementation work. The current request permits repository documentation edits and existing local checks, with no application/test changes, commits, network services, other-project inspection, or subagents.

Read [published task-completion findings](../../task-completion.md) for current behavior, source/test routes, and actual checks. No available requirement settles whether repeat success should remain or receive special feedback.

## Decisions to ask together

1. Should completing an already-done task keep succeeding, or become an error? Proposal: keep success, preserving current behavior and the existing repeat test. Choosing an error changes the CLI success contract and requires revising the repeat test and defining error feedback.
2. If repeats succeed, should they use the ordinary confirmation or a distinct message such as `Task 1 is already complete.`? Proposal: use distinct feedback so the user can tell that no state transition occurred. This is not a confirmed requirement. Ordinary confirmation needs no distinction in the returned result; special feedback needs awareness of the previous done flag. If repeats become errors, this choice instead concerns error wording.
3. Should friendly feedback replace the completion JSON on stdout, or go to stderr while JSON remains on stdout? Proposal: retain JSON on stdout and send friendly feedback to stderr to preserve the current output format. Replacement changes observable output. Exact wording can follow the chosen behavior; suggested first-completion copy is `Task 1 completed.`

## Resume and handoff

- Base revision remains `9520c642f6eaa9004cdafac26f16238042ce754c`. On resumption, `README.md` and `delivery.md` had uncommitted navigation/handoff edits; `docs/task-completion.md` and this record were untracked. Application/test changes were also already present: `tasklist/tasks.py` renames `complete_task` to `finish_task` and raises `ValueError("unknown task")` for a missing ID, `tasklist/cli.py` calls the renamed function, and `tests/test_tasks.py` uses the new name and exception type. No staged changes were present.
- Rechecked those changes, corrected the published symbol/error references, and reran all six existing unit tests and local CLI checks successfully; details are in the published findings. This resumption edits documentation only and preserves the existing application/test changes and unrelated `docs/export-notes.md`.
- On resumption, read this record, the linked findings and delivery request; inspect Git status/diffs and recheck affected sources (`tasklist/tasks.py`, `tasklist/cli.py`, `tests/test_tasks.py`). Continue with the user's answers rather than restarting discovery.
- Incorporate confirmed choices into the capability explanation and delivery acceptance criteria. Keep any unanswered decisions here. Remaining application implementation and appropriate test updates belong to `delivery.md`; this investigation does not authorize them.
- When all decisions are resolved and delivery contains remaining implementation work, remove this record and update incoming links. No separate answer archive is needed.
