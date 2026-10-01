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

Completing an already completed task must succeed, leave it complete, and show the exact message “Already complete”. This is the confirmed requirement for the pending confirmation-message change; the current CLI still prints task JSON without this message. First completion should show a friendly confirmation, with its wording and how confirmations coexist with JSON output still to be settled during implementation. The investigation is complete; implementation and verification work remain in [delivery.md](delivery.md).
