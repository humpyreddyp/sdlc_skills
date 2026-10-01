Repeated completion currently succeeds and prints the same JSON as first completion. The existing repeat test supports that behavior; no requirement settles whether it should remain or receive special feedback.

Saved [findings](docs/task-completion.md) and [unfinished decisions](docs/work/investigation/repeated-completion.md), linked from [delivery.md](delivery.md). All six tests, local CLI checks, documentation links, and whitespace checks passed. Only documentation changed.

For next session:

1. Should repeats keep succeeding or become errors? I recommend keeping success.
2. If successful, should repeats show the ordinary confirmation or “Task 1 is already complete”? I recommend distinct feedback.
3. Should friendly messages replace stdout JSON or appear on stderr while preserving JSON? I recommend preserving JSON.

Investigation is partial pending these decisions. Pausing as requested.