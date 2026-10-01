Investigation is partial and paused for your decision. Repeated completion currently succeeds and prints the same JSON; the existing repeat test passes. That establishes current behavior, not intended policy.

Should repeated completion:

1. **Succeed with a special message** such as “Task 1 was already complete.” — my recommendation.
2. **Succeed with the ordinary confirmation.**
3. **Fail as an error.**

Findings are in [task completion](docs/task-completion.md); unfinished context is saved in the [investigation record](docs/work/investigation/repeated-completion.md), linked from [delivery.md](delivery.md).

All six existing tests passed; documentation links and diff checks passed. Only documentation changed.