# Confirmation-message change

Add a friendly confirmation message when the user completes a task. Investigate repeated completion before implementing the message. Application implementation remains pending.

The repeated-completion investigation is complete. [Task completion](docs/task-completion.md) publishes current behavior, verification, and the user's 2026-10-01 confirmed requirement: repeated completion succeeds and shows `Already complete`. The current CLI succeeds but prints only JSON, so the feedback change remains pending.

## Acceptance criteria

- Completing an unfinished task marks it done and provides friendly confirmation, as requested originally.
- Completing an already-done task succeeds (CLI exit code 0), keeps it done, and shows `Already complete` as distinct repeat feedback.

## Pending delivery work

- Settle how friendly feedback coexists with the current JSON output. Retaining JSON on stdout and sending feedback to stderr remains a proposal, not an accepted requirement. First-completion wording is also unspecified; the earlier suggestion `Task 1 completed.` is only a proposal.
- Implement feedback with awareness of the task's state before `finish_task` mutates it; its current return value does not distinguish first completion from a repeat. Relevant code and test routes are in the capability page.
- Verify first completion and repeated completion, including message text, exit status, saved state, and the chosen stdout/stderr contract. Add appropriate CLI/output coverage during implementation; the six existing unit tests do not assert confirmation messages.
- Verify missing-ID handling still exits 2 with `unknown task` on stderr, no stdout, and no file write.

This document owns the remaining application and test work. Investigation closure does not mean the confirmation change has been implemented or verified. The documentation-only investigation preserved the pre-existing application/test edits described in the capability page.
