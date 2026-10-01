Updated [task-completion knowledge](docs/task-completion.md) for the existing `finish_task` rename and `ValueError("unknown task")` behavior. Repeated completion still succeeds.

All six existing tests passed; documentation links and `git diff --check` passed. Application code and tests were untouched.

Investigation remains partial: the [saved record](docs/work/investigation/repeated-completion.md) retains the pending choice between a shared confirmation and a distinct “already complete” message. Implementation remains in [delivery.md](delivery.md).