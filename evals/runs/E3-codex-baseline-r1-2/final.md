Updated [delivery.md](/private/tmp/repository-knowledge-evals/E3-codex-baseline-r1/delivery.md) to reflect current behavior: `finish_task` replaces `complete_task`, and missing IDs raise `ValueError("unknown task")`.

All six tests and CLI checks passed. Repeated completion still succeeds. Confirmation wording and output stream remain unresolved.

Only documentation was edited; existing code and test changes were preserved.