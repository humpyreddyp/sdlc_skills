# Local task list

A command-line task list for one person, stored in a local JSON file. Add a task, list tasks, and complete a task by its numeric ID. Python 3.10 or later is required; the application and unit tests have no third-party dependencies.

Run from this directory:

```sh
python3 -m tasklist.cli --file /tmp/example-tasks.json add 'Review a document'
python3 -m tasklist.cli --file /tmp/example-tasks.json list
python3 -m tasklist.cli --file /tmp/example-tasks.json complete 1
python3 -m unittest discover -s tests -v
python3 tools/verify.py
```

The core functions also work in memory. Persistence is provided by the CLI; this is not a web service or a multi-user database.

Use a fresh JSON path for the example if you expect the new task to have ID 1. Put `--file` before the subcommand; omitting it uses `tasks.json` in the current working directory. Commands print JSON to standard output.

The verification wrapper requires the separately provided `repository_eval_missing_dependency` module; it is not vendored here. Its installation source and setup procedure are not documented in this repository. Running the unit tests directly does not replace this wrapper.

Start with the [repository knowledge and readiness assessment](docs/knowledge/index.md) for task-completion work. See [task behavior and implementation](docs/knowledge/capabilities/task-completion.md) and the separate [future export note](docs/export-notes.md).
