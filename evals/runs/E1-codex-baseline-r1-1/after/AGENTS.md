# Repository guidance

This is a single-user Python command-line task list backed by a local JSON file.
Python 3.10+ is required; there are no third-party dependencies or installation
steps. Run commands from the repository root.

## Start here

- Read [README.md](README.md) for usage.
- Read [docs/task-completion.md](docs/task-completion.md) for current completion
  behavior, code and test pointers, persistence boundaries, and check results.
- Core operations live in [tasklist/tasks.py](tasklist/tasks.py); argument parsing,
  file I/O, and CLI output live in [tasklist/cli.py](tasklist/cli.py).
- Existing tests are in [tests/test_tasks.py](tests/test_tasks.py).

## Working on tasks

Keep changes within the requested scope. Preserve the distinction between
in-memory operations and CLI persistence. For completion changes, review the
existing successful, repeated, and missing-ID cases before editing. Do not infer
CLI coverage from the core unit tests.

Use an explicitly chosen disposable JSON file for manual CLI checks; the default
`tasks.json` is relative to the working directory and may contain user data.
Preserve [docs/export-notes.md](docs/export-notes.md): CSV export is proposed,
not implemented or promised.

## Validation

Run the existing suite:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

No lint, type-check, build, or CI configuration is present. Report the command,
result, and any coverage limitations when handing off work. Update the behavior
documentation when an authorized implementation change alters it.
