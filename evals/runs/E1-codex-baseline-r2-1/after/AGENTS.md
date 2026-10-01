# Repository guidance

This repository is a single-user Python task-list CLI backed by a local JSON
file. Use Python 3.10 or later from the repository root; no third-party
dependencies or installation step are required.

Read [README.md](README.md) for usage and
[docs/task-completion.md](docs/task-completion.md) for the current completion
contract, code map, test coverage, and recorded check result. Claude Code should
also start with this guidance via [CLAUDE.md](CLAUDE.md).

## Where to work

- `tasklist/tasks.py`: in-memory operations, including `complete_task`.
- `tasklist/cli.py`: argument parsing, JSON loading/saving, output, and CLI errors.
- `tests/test_tasks.py`: six standard-library unit tests for in-memory operations.
- `docs/export-notes.md`: future CSV proposal; preserve it. Export is not implemented.

## Working conventions

Keep changes scoped to the requested task. Preserve completion's in-place
mutation, repeat-completion behavior, and missing-ID error unless a requested
change explicitly alters that contract. Keep persistence in the CLI and core
operations usable in memory. Do not infer unimplemented features from planning
notes.

For documentation-only work, leave application code and tests unchanged. Use an
explicit disposable `--file` path for manual CLI exercises; the default
`tasks.json` belongs to the caller's current directory. Put `--file` before the
subcommand.

## Validation

Run the existing suite from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Use explicit discovery with `-s tests`. There is no configured formatter, linter,
type checker, build step, or CI workflow in this repository. Report the command,
test count, outcome, and any unverified behavior. The unit suite does not exercise
CLI persistence or process exit behavior. Check documentation patches with
`git diff --check` and inspect `git status --short` before handing work back.
