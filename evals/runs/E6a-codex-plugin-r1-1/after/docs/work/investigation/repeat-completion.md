# Repeated completion follow-up

Request: investigate the intended and current rule for completing an already completed task, publish supported findings, and identify any decision needed. The investigation is complete; application changes and test changes were explicitly excluded.

The [published explanation](../../task-completion.md) records the confirmed rejection requirement, implementation mismatch, misleading test name, CLI consequences, and executed check. The requirement remains authoritative; no product clarification is needed to establish it.

Remaining delivery work requires a separately authorized implementation task; no delivery owner or issue is recorded in the repository. Implement the required `ValueError` for an already completed task, choose exception wording (currently unspecified), and align the misleading test name with its assertion. Rerun the existing suite and verify the CLI error path. Retaining successful repeated completion would require an explicit product-owner revision of [requirements.md](../../../requirements.md), not an inference from current code or the test name.

Recheck sources: `tasklist/tasks.py` (`complete_task`), `tasklist/cli.py` (`main`), and `tests/test_tasks.py` (`TaskTests.test_repeat_completion_is_idempotent`). The investigation began at revision `fdeae91` with a clean working tree. Its only resulting changes are documentation: README navigation, requirement compliance status, the completion explanation, and this record. No application fix has been made.
