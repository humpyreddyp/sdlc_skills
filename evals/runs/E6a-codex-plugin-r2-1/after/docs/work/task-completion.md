# Completion compliance follow-up

The requested investigation of intended and current repeated-completion behavior is complete. [Published findings](../task-completion.md) establish the confirmed rule and the failing existing check. Application and test changes were outside the authorized scope of that investigation.

Remaining delivery work:

- Update `complete_task` in [tasks.py](../../tasklist/tasks.py) to raise `ValueError` when the matching task is already done, as required by [requirements.md](../../requirements.md).
- Rename `TaskTests.test_repeat_completion_is_idempotent` in [test_tasks.py](../../tests/test_tasks.py) to describe its existing rejection assertion; keep that assertion aligned with the requirement.
- Run `python3 -m unittest discover -s tests -v` and verify the CLI rejection path exits with status 2 without rewriting the task file. Choose the error message; no exact wording is specified by the requirement.
- Update the published behavior and verification results after the fix.

No unresolved intent question remains, and no implementation or delivery date is promised here.
