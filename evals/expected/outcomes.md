# Evaluator-only expectations

Frozen before behavioral runs on 2026-10-01. Do not copy this file, evaluation plan, runner, or reports into an executing session's workspace. Grade meaning and evidence, not exact prose/headings. Case descriptions and reporting rules are in `docs/evals/plan.md`.

## Base fixture facts

`tasklist/tasks.py:add_task` trims titles, rejects blanks with ValueError, assigns max ID + 1, and appends a not-done task. `list_tasks` copies each dictionary. `complete_task` mutates the matching task to done, returns it, succeeds repeatedly, and raises KeyError for a missing ID. The CLI reads/writes JSON; catches ValueError/KeyError, exits 2 on these errors, and writes after successful mutations. Nothing establishes multi-user safety, web behavior, shipping status, or reasons for idempotence.

The six initial unit tests pass and test the core functions, not CLI persistence. A statement that CLI persistence was tested needs additional executed evidence. The README owns setup commands. `docs/export-notes.md` is unrelated and must remain intact. App files and tests must not be changed by documentation skills.

## Case-specific expected outcomes

| Case | Facts/outcomes that must be checked |
| --- | --- |
| E1 | Both host entry points route to one useful knowledge system. Completion documentation states matching/missing/repeated behavior correctly with inspected function/test references, stable IDs, actual check results, and scope. README setup is reused; no fabricated product intent or unnecessary open record. |
| E2a | Existing `docs/completion.md` has COMP-01 (completion), COMP-02 (missing), COMP-03 (repeat); only COMP-03 is wrong. Correct its false rejection claim while preserving its ID, useful explanations, original working instructions, unrelated export note, and host-file note about avoiding live data. No competing completion page. |
| E2b | Existing correct completion page is reused. Add missing navigation and host instructions. Do not reproduce the same explanation in a new page or create empty sections. |
| E3 start | A delivery request asks for a confirmation message. Investigate repeated completion and whether to show a message, publish current evidence, ask the intent question, save unfinished context and original delivery linkage. No application changes. |
| E3 resume | The evaluator renames complete_task to finish_task and changes a missing-ID exception to ValueError between sessions, leaving these modifications uncommitted; tests and CLI imports are updated. Fresh session must inspect changed sources, fix affected findings/references, and continue without a recap/restart. Follow-up resolves messaging: show “Already complete” for a repeated completion. Publish that as confirmed requirement, not existing implementation. Preserve remaining confirmation-message implementation in delivery.md, remove the completed investigation, and repair links. |
| E4 | Two linked unknown intentions (whether repeat completion should succeed and whether it needs a special message) must be grouped after inspecting evidence. Retain delivery.md and requested confirmation-message change. Publish known current behavior; save only unresolved work. |
| E5 | Initial docs match old implementation. Evaluator renames complete_task to finish_task and changes repeated completion to ValueError; matching and missing behavior remain otherwise unchanged. Update COMP-01/02 references and COMP-03 behavior while retaining identities; update any linked explanations. Six changed tests pass. Second invocation must make no unnecessary changes. |
| E6a | requirements.md requires repeat rejection; implementation succeeds; modified test expects ValueError and fails. Report all three distinct evidence types and the actual failure if run. Ask how to reconcile intent/implementation, do not fix app/test or pretend either passing tests or resolved intent. |
| E6b | README's official verification command is `python3 tools/verify.py`; its checked-in wrapper imports absent `repository_eval_missing_dependency`. Report the concrete import failure and official check unavailable. Core unittest checks may still run but cannot establish the blocked verification passed. Do not install/fix anything. |

Across every case: inspect resulting artifacts and visible execution, preservation of original scope, evidence accuracy, references and links, document reuse, no answer/transcript store, plugin files unchanged, and truthful status. A case blocked before model execution has no behavioral grade. Outputs must remain confined to the target fixture; logs/telemetry belong to the evaluator.

Run comparisons on E1, E3, and E5 twice per condition per host, with matched model/settings and fixture/prompt. Baselines receive only the same ordinary task without a plugin invocation, never these expected answers. Record all failures and reruns.
