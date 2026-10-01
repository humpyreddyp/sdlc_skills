# Repository knowledge

The [Local task list](../../README.md) is a command-line tool for one person to add, list, and complete tasks stored in a local JSON file. A typical journey is to add a title, list tasks to find an ID, then complete that ID. The core functions also support in-memory use.

- [Task completion](../completion.md): current rules, CLI persistence and error handling, and links to the implementation and relevant tests. Start here for completion work.
- [Working instructions and verification results](../../README.md): Python prerequisites, usage, the existing check command, and what was verified during preparation.
- [Future export work](../export-notes.md): an existing proposal; CSV export is not implemented.

The implementation is small: [tasklist/tasks.py](../../tasklist/tasks.py) contains `add_task`, `list_tasks`, and `complete_task`; [tasklist/cli.py](../../tasklist/cli.py) contains the `main` entry point and JSON persistence. [tests/test_tasks.py](../../tests/test_tasks.py) contains the six `TaskTests` unit tests. Completion-specific behavior and evidence are maintained in the capability page above.
