# Local task list

A command-line task list for one person, stored in a local JSON file. Add a task, list tasks, and complete a task by its numeric ID. Python 3.10 or later is required; there are no third-party dependencies.

Run from this directory:

```sh
python3 -m tasklist.cli --file /tmp/example-tasks.json add 'Review a document'
python3 -m tasklist.cli --file /tmp/example-tasks.json list
python3 -m tasklist.cli --file /tmp/example-tasks.json complete 1
python3 -m unittest discover -s tests -v
```

The core functions also work in memory. Persistence is provided by the CLI; this is not a web service or a multi-user database.

For agent working instructions, current behavior, code and test references, and local verification results, start with the [repository knowledge index](docs/knowledge/index.md). The [task completion guide](docs/knowledge/capabilities/task-completion.md) describes completion and its limits.
