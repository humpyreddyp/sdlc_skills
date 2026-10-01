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

## Confirmed completion requirement

Completing an already-completed task must succeed (CLI exit status 0), leave
the task completed, and show the exact message `Already complete`. This is the
confirmed product decision. Repeated completion already succeeds, but the
message is not implemented: the CLI currently prints the task as JSON for both
first and repeated completion.

The investigation is complete. Pending confirmation-message implementation,
presentation details, and validation are tracked in [delivery.md](delivery.md).
