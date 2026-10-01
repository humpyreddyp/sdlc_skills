# Repository knowledge plugin evaluation plan

**Status: execution authorized by the user on 2026-10-01.** This pre-run plan remains the evaluation baseline. Actual runs and limitations are recorded in [results](results.md).

Baseline: [V1 design](../design/repository-readiness-and-knowledge-management-v1.md), derived from the [V1 Source Page](https://chatgpt.com/space/page_c2ad846136688191ab39d7d8b916036c), the [AI SDLC Source Page](https://chatgpt.com/space/page_bf0e0412a6448191882216af183595bc), and the user's repository handoff. Plan saved 2026-10-01.

## Purpose and decision rule

Establish whether the actual packaged Knowledge Discover and Knowledge Maintain skills produce useful, evidence-backed artifacts and preserve the user's request in **both Codex and Claude Code**. Structural validation is necessary but insufficient. Grade behavior, artifact usefulness, evidence, and scope; do not require exact prose, headings, filenames, or table wording where repository conventions support an equivalent result.

A required case passes only when all of its material expected outcomes are supported by the recorded run and artifacts. Record each outcome as pass or fail with evidence. Record a case that cannot execute as blocked, with its missing prerequisite, rather than a pass. An evaluator-injected unavailable check can still yield a passing case if the agent handles it correctly; a missing evaluation host cannot.

Claim two-host validation only when every required case has passed in each host, both cross-host continuation directions have passed, and demonstrated failures have been repaired and retested. Report comparison results even if the plugin offers no improvement. A limited sample establishes observed outcomes, not a general performance guarantee.

## Fixture and separation

Use the [small task-list preparation example](../../README.md#proposed-small-preparation-example) as the common fixture. Implement it only in the authorized implementation phase, with local standard-library checks and no live service dependency. Use isolated repository copies for every case and repeat. Freeze and identify each input snapshot before running the agent.

The evaluator prepares variants for missing guidance, partial navigation, established documentation with a relevant error, an unresolved investigation, changed behavior, conflicting evidence, and an unavailable check. Include an unrelated document and unrelated instruction content to test preservation. Application mutations for a scenario are made by the evaluator between sessions; they are not authorized application work for the skills.

Proposed evaluation storage, outside the installable plugin root:

- `evals/fixtures/`: immutable input snapshots or reproducible fixture definitions.
- `evals/expected/`: evaluator-only expected facts, affected areas, preserved content, and grading criteria.
- `evals/runs/<run-id>/`: exact input prompt, environment metadata, execution output, artifact snapshots/diff, measurements, and judgment.
- `docs/evals/`: this plan and readable reports linking to retained evidence.

These paths are a plan, not a request to create scaffolding now. Do not reference expected answers or reports from ordinary skill resources. The executing host receives only an isolated fixture, its task prompt, necessary ordinary repository context, and the tested plugin for plugin runs. Keep the evaluator's files outside its accessible workspace where the host permits; do not grant it the plugin development repository as ambient context. Record any isolation limitation and do not treat a contaminated run as a clean evaluation.

Finalize the expected facts and acceptable outcomes before the first run of a fixture version. Expectations should cite actual fixture code and tests once implemented. They must never be reconstructed from the executing agent's output. The conceptual outcomes below are already fixed; precise symbols and fixture assertions are bound before execution.

## Required cases and expected outcomes

Run every case below in each host with the plugin. Each variant receives a fresh fixture copy unless the case explicitly requires a continuation or repeated maintenance run.

| ID and case | Starting state and input | Expected outcomes | Evidence to inspect |
| --- | --- | --- | --- |
| E1 — Preparation without knowledge | Code, tests, and minimal setup README; no agent guidance or knowledge index. Ask to prepare for task completion in both hosts. | Creates useful short host instructions and navigation; explains product purpose and completion behavior with stable IDs and inspected code/test references; runs available relevant checks and states results and limits; publishes directly without requiring Maintain; writes only in the target repository. | Navigate from both entry points to behavior and sources; compare prose to inspected fixture facts and actual command output; inspect all new files and plugin-directory changes. |
| E2a — Preparation with existing documentation | Existing capability page, a stable behavior ID, a relevant inaccurate statement, valid setup instructions, and unrelated prose. Ask to prepare completion work. | Reuses suitable pages and IDs, corrects the relevant error using evidence, connects missing links, and preserves unrelated content. Avoids creating a second competing explanation. | Before/after diff, source evidence for correction, resolved links, preserved unrelated text and IDs. |
| E2b — Partial guidance | Useful existing explanations and setup instructions, but missing navigation or one host entry point. Same preparation request. | Adds the missing routes and relevant gaps without rewriting or duplicating useful documentation. Handles partial preparation without requiring the user to build the structure. | Document reuse, entry-point navigation, changed-file scope, absence of empty pages. |
| E3 — Fresh-session resumption | Discover begins an investigation with a real unresolved question and saves necessary context; evaluator changes a relevant source and test between sessions, including an uncommitted-change variant. A fresh session receives only “Continue the saved task-completion investigation,” the repository artifacts, and the plugin. | Reads saved context and linked knowledge, detects relevant changes, rechecks affected conclusions, and continues the next unresolved action without a routine recap or complete restart. Incorporates a supplied resolution into published knowledge. Removes the completed record only after preserving remaining delivery work and fixing incoming links. | Separate session IDs, artifacts carried between sessions, source/diff reads, changed conclusions, resolved questions, final record deletion and retained delivery link. |
| E4 — Investigation during delivery | A saved request asks for a completion-behavior change; two related questions about current rules arise. Ask Discover to investigate these gaps as part of that request, without implementing application changes. | Preserves the original request; inspects relevant evidence before asking; groups necessary questions with findings and consequences; continues independent investigation; publishes supported findings immediately; saves only necessary unresolved context and links remaining work to its existing owner. | Original task remains recoverable; tool/output trace, grouped questions, published explanations, minimal record, no unauthorized application edits or answer/transcript archive. |
| E5 — Maintenance after a change | Published behavior table and references; evaluator changes one behavior and renames a relevant function/test while another behavior remains unchanged. Ask Maintain to reflect the change, then invoke it again with no further changes. | Updates affected explanations and references across linked pages; preserves IDs for behaviors retaining identity and never reassigns an old ID to an unrelated behavior; distinguishes a working change from release; preserves unrelated content. The repeated run reports no necessary update and causes no unnecessary document churn. | Before/after source and document diffs, reference resolution, ID identity review, second-run diff and completion report. |
| E6a — Conflicting evidence | A confirmed requirement, implementation, and existing test disagree about completing an already completed task. Ask to investigate the rule. | Describes each source's actual claim and the conflict; distinguishes inspected code, test intent, executed test result, and confirmed intent. Asks only the decision needed to resolve intended behavior. Publishes supported findings without inventing intent or silently changing requirements. | Conflict explanation and references, questions, actual check results, appropriate open record and status. |
| E6b — Unavailable checks | A documented verification command cannot run because the evaluator removes a required test tool or denies a fixture-only prerequisite. Ask to assess readiness. | Records the command attempted or the specific prerequisite preventing an attempt; reports checks not run and limits on conclusions; does not claim a pass, install dependencies, fix application code, or overstate readiness. Completes supported documentation and identifies remaining action. | Command/output trace, prerequisite evidence, readiness report, scoped diff, distinction between completed assessment and a ready environment. |

For E6b, choose the missing prerequisite before execution and document it in the evaluator's expectations. Do not simulate a failure merely by telling the executing agent that a command failed.

## Continuation matrix

E3 must exercise four fresh-session paths: Codex → Codex, Claude Code → Claude Code, Codex → Claude Code, and Claude Code → Codex. The destination receives the source session's actual generated repository artifacts, not an evaluator-written substitute summary or the prior conversation. Transfer published knowledge, unfinished records, and any relevant working changes faithfully.

For each path, stop at a meaningful unresolved question, save progress, make the predeclared relevant change, and resume. Use a consistent evaluator-provided answer when the agent reaches the unresolved decision. Do not reveal hidden expected answers or suspected failures. Verify that resolved human input becomes published understanding without a separate default answer archive, and that record cleanup does not lose remaining work.

## Comparable runs without the plugin

Use E1 (preparation), E3 (same-host fresh-session resumption), and E5 (maintenance and a repeated invocation) as representative comparisons in each host. Run at least two independent plugin/no-plugin pairs for each of these case/host combinations; increase repetitions only when variability or a failure needs clarification. Alternate which condition runs first.

Within a pair, hold the host version, exact model and reasoning settings, fixture starting snapshot, substantive user request, permission profile, available tools, time/token limits, and evaluator responses constant. Use fresh sessions and isolated profiles or equivalent host controls so the baseline has no tested plugin, injected skill instructions, previous plugin outputs, or hidden expectations. Other skills and user-level instructions must be matched and recorded; disable interfering discovery where supported and report unavoidable contamination.

For plugin runs, the invocation wrapper may explicitly select the intended skill. For baseline runs, remove only the plugin invocation wrapper while retaining the same substantive task. Do not paste the skill's workflow into the baseline prompt. E3 baseline must create and resume its own saved artifacts; inability to preserve context is an observed result, not grounds for giving it the plugin's record.

Compare outcome passes/failures, unsupported claims, omissions, unnecessary edits, evidence quality, navigation usability, and resumption quality. Measure elapsed time, input/output tokens, cached tokens, and repeated source reads when observable. Show paired raw results and ranges; do not hide failures behind an aggregate average. Explain differences in configuration or cache visibility that limit comparability. Do not compare raw cross-host timing as though the models and tool runtimes were identical.

## Execution and inspection method

1. After implementation authorization, verify both host runtimes and model access; record versions and available telemetry. Build skills using the required creators and validate both skills, the Codex package, and the Claude manifest. Structural passes are reported separately from behavioral results.
2. Prepare and freeze fixtures, ordinary prompts, evaluator responses, and expected outcomes. Run the fixture's own checks to establish its true starting state; retain that output only with evaluator evidence.
3. Load the actual package in an isolated host environment and confirm skill availability. Capture plugin identity/version and content hash. Snapshot the plugin installation before each run to detect accidental writes there.
4. Execute each case with its assigned isolation and limits. Save host-emitted outputs, visible tool/command activity, and generated files. Record start/end timestamps and interruptions. Do not supply private grading criteria to the executing session.
5. Inspect all resulting documents against the frozen expectations and actual sources. Follow links, inspect named symbols/tests, review IDs and diffs, and check that the requested scope remains identifiable. Review evidence as an evaluator, not by asking the executing agent to grade itself.
6. For failures, retain the original result, identify the demonstrated cause, and make a narrow fix. Rerun affected cases in each host whose shared instructions or resources changed; rerun a paired baseline if comparison inputs changed. Preserve result history and link the fix to its reruns.
7. Report per-host results, both cross-host directions, paired comparisons, untested cases, remaining failures, and limits on any validation claim. Do not release or push solely because evaluations pass; follow the user's authorized delivery scope.

Package lifecycle checks after authorization must also cover install, update/version pickup in a fresh session, invocation of both skills, and removal in each host. Verify removal leaves the investigated repositories' generated knowledge and investigation records intact. Record exact verified instructions for the eventual installation and usage guide.

## Reporting method

Each run record must include:

| Field | Required value |
| --- | --- |
| Identity | Run ID, case/variant, repeat number, plugin or baseline, predecessor/destination run IDs for continuation |
| Host and model | Product/surface, executable/app version, reported model identifier, reasoning setting, OS/runtime, relevant permission/tool configuration |
| Plugin | Version/revision and content hash; loaded skills, invocation form, or evidence that the tested plugin was absent |
| Inputs | Exact prompts and supplied follow-ups, fixture snapshot/hash, relevant Git state including uncommitted changes, allowed tools and limits |
| Outputs | Host output/log references, commands and exit results, generated document snapshot, before/after diff, final completion status |
| Judgment | Expected-outcome-by-outcome pass/fail, evidence locations, overall pass/fail/blocked, failure explanation, reviewer identity/method |
| Time | Start/end timestamps, total elapsed time; separate host execution, human wait, and environment setup where measurable |
| Usage | Input/output/cached tokens and provider-reported total where available; telemetry source and scope |
| Repair | Related implementation fix, affected cases, rerun IDs, final disposition while retaining original failure |
| Limitations | Missing measurements, access restrictions, untested paths, timeouts, contamination, and comparison differences |

Record unavailable values explicitly as `unavailable — <reason>`, never zero or an estimate presented as telemetry. If a host reports only combined token usage, retain that value and mark the unavailable breakdown. A host's unreported model version is likewise unavailable; do not infer it from a brand name. Capture visible execution artifacts, not hidden model reasoning.

The readable report should contain a per-case/per-host result matrix, a continuation matrix, paired comparison results, links to outputs and artifacts, and a concise account of failures, fixes, reruns, and outstanding limitations. Distinguish plugin defects from evaluation infrastructure failures, and mark interrupted/time-limited runs explicitly.

## Prerequisites recorded before implementation

- **Execution authorization:** pending the user's go-ahead. This is the explicit phase boundary from the handoff; do not scaffold, implement, install, run model evaluations, release, or push now.
- **Required creators:** both installed skills were read and their `quick_validate.py` and `validate_plugin.py` scripts located. They are available; validators have not been run because no skills or package exist yet.
- **Source access:** both design Pages were successfully read through Pages tools. No source-content blocker remains, and source Pages were not edited.
- **Codex runtime:** an executable was found on PATH. Host version, authenticated execution, model identity, usage reporting, and clean-profile controls remain to be verified before evaluation.
- **Claude Code runtime:** `claude` was not found on the current shell's PATH. This does not prove it is absent elsewhere; locate an existing usable runtime or resolve installation/access after authorization. Claude Code evaluations and two-host validation cannot be claimed until real runs succeed.
- **Git remote:** the local repository has no configured remote. This does not block saving or reviewing these documents; no remote action is part of this phase.

The prerequisite list above records the design-phase state. No behavioral outcome or host-validation pass is claimed by this plan; use the results report for current evidence.
