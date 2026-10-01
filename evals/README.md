# Behavioral evaluation evidence

Read [the plan](../docs/evals/plan.md) and [results](../docs/evals/results.md). This directory is excluded from the plugin ZIP and is not linked by either skill.

- `fixtures/tasklist/` is the raw application fixture.
- `expected/outcomes.md` contains evaluator-only expected facts defined before execution.
- `run_case.py` creates an isolated Git repository under `/private/tmp/repository-knowledge-evals/`, supplies only the ordinary request and optional plugin invocation, and captures actual host output and before/after artifacts.
- `run_codex_matrix.py` runs the remaining planned Codex cases and repetitions without overwriting existing evidence.
- `runs/` stores exact inputs, JSONL outputs, errors, artifact snapshots, source hashes, telemetry, and separately authored review judgments.

Example: `python3 evals/run_case.py E5 --host codex --repeat 3`. Add `--baseline` for the matched run without the plugin. For cross-host E3, use `--host codex --destination-host claude` or the reverse; the destination receives the same actual repository and Git working state in a fresh session. Existing run IDs are never overwritten; use a new repeat number for repair trials. For Claude, provide an authenticated `claude` executable through `REPOSITORY_KNOWLEDGE_CLAUDE` or the temporary path documented in the runner. It uses normal host permissions, not an approval bypass.

Codex needs the package installed as `repository-knowledge@sdlc-skills`. Its runs ignore normal user configuration, disable the four discovered unrelated user skills, and explicitly enable or disable this plugin per condition. Claude uses `--plugin-dir` for the plugin condition and project settings only. Review discovery before using this runner on another machine: the unrelated-skill list is environment-specific, and new globally discovered skills must be accounted for.

Expected answers and reports are not copied into the execution workspace. The Codex workspace-write sandbox permits reads outside that workspace, so this is context isolation, not an OS-enforced unreadable grader directory. The common task boundary prohibits reading other projects/evaluation material. Inspect command traces for contamination and discard contaminated runs. Do not claim stronger isolation than observed.

The runner records evidence, not a verdict. Review artifacts and behavior against frozen expectations; then save `review.json` beside the run. A successful process exit alone is never a passing evaluation. Host authentication failures are blocked runs even if the host emits a success-shaped result envelope.
