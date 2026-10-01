# Confirmation-message change

Add a friendly confirmation message when the user completes a task. Investigate repeated completion before implementing the message. Application implementation remains pending.

Current behavior and verification are documented in [task completion](docs/task-completion.md). Repeated completion currently succeeds and prints the same JSON as first completion; this is evidence of existing behavior, not a confirmed requirement to retain it.

Before implementation, resolve whether repeated completion should remain successful and whether it should display a special message. The [unfinished investigation](docs/work/investigation/repeated-completion.md) preserves the decisions, proposal, and resumption steps. This delivery task remains the owner of the confirmation-message implementation and its tests once those decisions are answered.
