# Evaluation results

Implementation and evaluation were authorized on 2026-10-01. **Codex: all selected same-host cases pass after repairs. Claude Code: behavioral validation blocked by missing authentication.** Cross-host continuation and Claude comparisons are not complete, so V1 is not fully validated for both hosts.

## Package and structural checks

The installed Codex skill-creator initialized both skills; its `quick_validate.py` passed for each. Plugin-creator generated the Codex package and marketplace; its `validate_plugin.py` passed. Claude Code's manifest validator passed. The validators required PyYAML, installed in a temporary virtual environment. The plugin itself has no runtime dependencies.

Local install and changed-version update were exercised in both hosts: original `0.1.0` and repaired `0.1.1` (Codex adds its creator-generated build suffix). Codex reruns read the repaired installed-cache paths. Claude's CLI reports the installed 0.1.1 inventory, but no Claude model executed the skills. Lifecycle evidence is in [lifecycle records](../../evals/runs/lifecycle/). The [installation guide](../installation.md) covers install, update, invocation, and removal.

Both temporary plugin installations and their `sdlc-skills` marketplace registrations were removed after evaluation. [Removal evidence](../../evals/runs/lifecycle/removal.json) records all four successful commands and matching before/after hashes for every fixture file outside Git metadata. Generated knowledge and unfinished records were preserved. The repository's marketplace files remain available for installation.

Both evaluated packages are retained outside runtime resources: [original ZIP](../../evals/packages/repository-knowledge-0.1.0.zip) and [repaired ZIP](../../evals/packages/repository-knowledge-0.1.1.zip). Each contains nine plugin files; fixtures, expected answers, and reports are excluded.

## Method and scope

The [plan](plan.md) and [expected facts](../../evals/expected/outcomes.md) preceded behavioral execution. Expectations SHA256: `f248e94b97cc187366cf399c917ca90c31a5d5a5b849a890a5442d595f37f39b`. The [fixture preflight](../../evals/runs/preflight/fixtures.json) verifies six passing base tests and the deliberately failing conflict/unavailable-check variants.

Codex CLI 0.158.0-alpha.2.1 used configured model `gpt-6-astra` with `high` reasoning. The CLI does not report the resolved runtime model identifier, so that field is marked unavailable. Claude Code 2.1.285 initialized with `claude-opus-5-5`, then rejected the request as unauthenticated before inference. [Environment evidence](../../evals/runs/preflight/environment.json), [successful Codex discovery](../../evals/runs/preflight/codex-discovery.jsonl), and [Claude attempt](../../evals/runs/E1-claude-plugin-r1-1/output.jsonl) preserve these distinctions.

Each executing session received a fresh isolated fixture and the ordinary task, with only the invocation wrapper differing for plugin/baseline. Expected answers were outside its workspace and context. Codex workspace-write still permits broader reads; this was not an OS-enforced unreadable grader directory. Visible command/file-change traces were reviewed for contamination and writes outside the fixture. No expectation-file access was observed. User configuration and the discovered unrelated skills were disabled for Codex, identically across conditions.

The primary Codex agent reviewed actual generated prose, behavior/reference accuracy, command results, ID identity, record lifecycle, and before/after diffs. It also authored the plugin, so this is not a blinded independent human study. Executing sessions did not grade themselves. The inspection helper checks preservation and relative file links; it does not judge wording or headings. Raw inputs, outputs, snapshots, hashes, usage, and individual review judgments are retained for inspection.

Original 0.1.0 runs hashed the source package before and after each run; [preflight](../../evals/runs/preflight/installed-package.json) confirmed that source and installed bytes matched. Those runs did not separately hash the installed cache after every session. The repaired 0.1.1 runner hashes the actual installed Codex cache before and after each plugin run. No changes to the checked package files were observed; visible write traces were also reviewed.

## Required outcomes

| Case | Codex selected runs | Claude Code | Review evidence |
| --- | --- | --- | --- |
| E1 — no knowledge | pass | Blocked by authentication; not behaviorally validated | [E1-codex-plugin-r1-1](../../evals/runs/E1-codex-plugin-r1-1/review.json), [E1-codex-plugin-r2-1](../../evals/runs/E1-codex-plugin-r2-1/review.json) |
| E2a — established documentation | pass | Blocked by authentication; not behaviorally validated | [E2a-codex-plugin-r1-1](../../evals/runs/E2a-codex-plugin-r1-1/review.json) |
| E2b — partial guidance | pass | Blocked by authentication; not behaviorally validated | [E2b-codex-plugin-r1-1](../../evals/runs/E2b-codex-plugin-r1-1/review.json) |
| E3 — fresh-session continuation | pass | Blocked by authentication; not behaviorally validated | [E3-codex-plugin-r3-1](../../evals/runs/E3-codex-plugin-r3-1/review.json), [E3-codex-plugin-r3-2](../../evals/runs/E3-codex-plugin-r3-2/review.json), [E3-codex-plugin-r3-3](../../evals/runs/E3-codex-plugin-r3-3/review.json), [E3-codex-plugin-r4-1](../../evals/runs/E3-codex-plugin-r4-1/review.json), [E3-codex-plugin-r4-2](../../evals/runs/E3-codex-plugin-r4-2/review.json), [E3-codex-plugin-r4-3](../../evals/runs/E3-codex-plugin-r4-3/review.json) |
| E4 — gap during delivery | pass | Blocked by authentication; not behaviorally validated | [E4-codex-plugin-r2-1](../../evals/runs/E4-codex-plugin-r2-1/review.json) |
| E5 — maintenance and repeat | pass | Blocked by authentication; not behaviorally validated | [E5-codex-plugin-r1-1](../../evals/runs/E5-codex-plugin-r1-1/review.json), [E5-codex-plugin-r1-2](../../evals/runs/E5-codex-plugin-r1-2/review.json), [E5-codex-plugin-r2-1](../../evals/runs/E5-codex-plugin-r2-1/review.json), [E5-codex-plugin-r2-2](../../evals/runs/E5-codex-plugin-r2-2/review.json) |
| E6a — conflicting evidence | pass | Blocked by authentication; not behaviorally validated | [E6a-codex-plugin-r2-1](../../evals/runs/E6a-codex-plugin-r2-1/review.json) |
| E6b — unavailable check | pass | Blocked by authentication; not behaviorally validated | [E6b-codex-plugin-r1-1](../../evals/runs/E6b-codex-plugin-r1-1/review.json) |

The selected cases use 0.1.1 for affected investigation/continuity reruns, and 0.1.0 for preparation, document reuse, maintenance, and unavailable checks whose behavior was unaffected by the narrow repair. Original failures remain in the run ledger below.

| Continuation direction | Result |
| --- | --- |
| Codex → Codex | See E3; two repaired sequences, each with three fresh sessions |
| Codex → Claude Code | Blocked by Claude authentication; not run |
| Claude Code → Codex | Blocked because no authenticated Claude source run can be created; not run |
| Claude Code → Claude Code | Blocked by Claude authentication; not run |

The runner supports `--host codex --destination-host claude` and the reverse. Destination sessions use the actual source repository and its Git working state, without the source conversation. Cross-host support is a required remaining evaluation, not inferred from shared Markdown.

## Demonstrated failures and repairs

1. **Premature product decision:** E4 and the original E3 starts treated successful repeat behavior in code/tests as sufficient to settle an explicitly open intent question. Discover now preserves that question, labels recommendations as proposals, and groups related choices. E4 was rerun and two new E3 sequences exercise publication, changed-source rechecks, explicit resolution, and cleanup.
2. **Completed investigation retained for implementation:** Original E6a correctly explained the requirement/code/test conflict, but kept a completed investigation merely as a home for application follow-up. Continuity now routes pending implementation to a delivery document and closes the investigation. E6a was rerun; E3 closure also exercises the same lifecycle rule.

No fixture expectations were weakened after observing results. Claude reruns are blocked by authentication. There is no claim that structural validation proves behavior in that host.

## Comparable plugin/no-plugin runs

Two independent pairs were run for preparation, continuation, and maintenance. E3 compares repaired plugin repeats 3/4 with the original unchanged baseline repeats 1/2; ordinary prompts, fixture content, model/settings and expected responses remain the same. Git commit timestamps/IDs differ across otherwise identical fixture copies. The original plugin E3 repetitions remain recorded as failures and are not substituted away in the ledger.

Metric cells show **elapsed time; input / output / cached-input tokens**, as reported by the host. Input includes cached input; do not add the cached column again. E3 totals all three sessions; E5 totals both invocations. Times include tool work and host latency, exclude fixture setup, and are summed session durations rather than total parallel wall time. Cache differences and variable concurrent load limit performance conclusions.

| Case / pair | Plugin outcome and metrics | Baseline outcome and metrics |
| --- | --- | --- |
| E1 / 1 | pass; 111.3s; 104,490 / 3,293 / 94,080 | fail; 116.8s; 89,275 / 2,742 / 66,944 |
| E1 / 2 | pass; 120.9s; 106,996 / 3,478 / 75,648 | fail; 116.3s; 117,021 / 3,217 / 82,560 |
| E3 / 1 | pass; 339.3s; 399,464 / 8,952 / 352,000 | fail; 227.4s; 291,511 / 5,343 / 238,464 |
| E3 / 2 | pass; 325.0s; 387,978 / 7,842 / 303,360 | fail; 170.7s; 253,891 / 3,986 / 217,728 |
| E5 / 1 | pass; 125.2s; 209,381 / 2,524 / 167,040 | fail; 108.7s; 150,005 / 2,015 / 100,480 |
| E5 / 2 | pass; 107.8s; 190,522 / 2,386 / 154,624 | fail; 96.2s; 165,312 / 1,796 / 123,008 |

Both preparation baselines produced useful accurate prose but omitted stable behavior IDs. Continuation baselines noticed changed sources and preserved work, but kept most resolved understanding in the delivery work document instead of publishing capability knowledge with stable IDs. Both maintenance baselines made further redundant documentation changes on the unchanged second invocation. The plugin's maintenance repeats made no file changes. These are failures against this plugin's acceptance criteria, not a claim that baseline output was generally unusable.

The data does not establish a general speed or token-saving benefit. The plugin's value in these fixtures is the required knowledge structure, uncertainty handling after repair, and stable maintenance. Repeated source-read counts are unavailable as a reliable metric; command counts and exact repeated-command counts are saved only as review signals. Account-wide cost and this supervising conversation's token usage are unavailable; per-run host token usage is recorded. Claude's rejected request reports zero inference tokens and no model execution.

Across 37 Codex sessions and one rejected Claude attempt, recorded totals are 4,057,974 input tokens (including 3,249,024 cached-input tokens), 85,223 output tokens, and 3,406.4 summed session seconds. These include original failures, baselines, and repair reruns; they exclude the supervising conversation and discovery preflights. See [session totals](../../evals/runs/lifecycle/session-totals.json).

## Complete run ledger

Each directory contains exact `input.txt`, `output.jsonl`, `stderr.txt`, `before/`, `after/`, `metadata.json`, and a separate `review.json`. Reviews include failures and their evidence. This ledger lists individual sessions; a multistep case requires all selected sessions to pass.

| Run | Review | Seconds | Input / output tokens |
| --- | --- | --- | --- |
| [E1-claude-plugin-r1-1](../../evals/runs/E1-claude-plugin-r1-1/metadata.json) | [blocked](../../evals/runs/E1-claude-plugin-r1-1/review.json) | 1.1 | 0 / 0 |
| [E1-codex-baseline-r1-1](../../evals/runs/E1-codex-baseline-r1-1/metadata.json) | [fail](../../evals/runs/E1-codex-baseline-r1-1/review.json) | 116.8 | 89,275 / 2,742 |
| [E1-codex-baseline-r2-1](../../evals/runs/E1-codex-baseline-r2-1/metadata.json) | [fail](../../evals/runs/E1-codex-baseline-r2-1/review.json) | 116.3 | 117,021 / 3,217 |
| [E1-codex-plugin-r1-1](../../evals/runs/E1-codex-plugin-r1-1/metadata.json) | [pass](../../evals/runs/E1-codex-plugin-r1-1/review.json) | 111.3 | 104,490 / 3,293 |
| [E1-codex-plugin-r2-1](../../evals/runs/E1-codex-plugin-r2-1/metadata.json) | [pass](../../evals/runs/E1-codex-plugin-r2-1/review.json) | 120.9 | 106,996 / 3,478 |
| [E2a-codex-plugin-r1-1](../../evals/runs/E2a-codex-plugin-r1-1/metadata.json) | [pass](../../evals/runs/E2a-codex-plugin-r1-1/review.json) | 139.1 | 130,473 / 3,546 |
| [E2b-codex-plugin-r1-1](../../evals/runs/E2b-codex-plugin-r1-1/metadata.json) | [pass](../../evals/runs/E2b-codex-plugin-r1-1/review.json) | 126.3 | 126,253 / 3,050 |
| [E3-codex-baseline-r1-1](../../evals/runs/E3-codex-baseline-r1-1/metadata.json) | [fail](../../evals/runs/E3-codex-baseline-r1-1/review.json) | 73.4 | 86,061 / 1,712 |
| [E3-codex-baseline-r1-2](../../evals/runs/E3-codex-baseline-r1-2/metadata.json) | [fail](../../evals/runs/E3-codex-baseline-r1-2/review.json) | 62.0 | 93,363 / 1,525 |
| [E3-codex-baseline-r1-3](../../evals/runs/E3-codex-baseline-r1-3/metadata.json) | [fail](../../evals/runs/E3-codex-baseline-r1-3/review.json) | 92.0 | 112,087 / 2,106 |
| [E3-codex-baseline-r2-1](../../evals/runs/E3-codex-baseline-r2-1/metadata.json) | [fail](../../evals/runs/E3-codex-baseline-r2-1/review.json) | 48.2 | 86,554 / 1,257 |
| [E3-codex-baseline-r2-2](../../evals/runs/E3-codex-baseline-r2-2/metadata.json) | [fail](../../evals/runs/E3-codex-baseline-r2-2/review.json) | 82.3 | 92,173 / 1,442 |
| [E3-codex-baseline-r2-3](../../evals/runs/E3-codex-baseline-r2-3/metadata.json) | [fail](../../evals/runs/E3-codex-baseline-r2-3/review.json) | 40.2 | 75,164 / 1,287 |
| [E3-codex-plugin-r1-1](../../evals/runs/E3-codex-plugin-r1-1/metadata.json) | [fail](../../evals/runs/E3-codex-plugin-r1-1/review.json) | 94.2 | 102,352 / 2,631 |
| [E3-codex-plugin-r1-2](../../evals/runs/E3-codex-plugin-r1-2/metadata.json) | [fail](../../evals/runs/E3-codex-plugin-r1-2/review.json) | 141.5 | 159,212 / 2,905 |
| [E3-codex-plugin-r1-3](../../evals/runs/E3-codex-plugin-r1-3/metadata.json) | [pass](../../evals/runs/E3-codex-plugin-r1-3/review.json) | 87.7 | 114,142 / 1,863 |
| [E3-codex-plugin-r2-1](../../evals/runs/E3-codex-plugin-r2-1/metadata.json) | [fail](../../evals/runs/E3-codex-plugin-r2-1/review.json) | 106.4 | 124,007 / 2,892 |
| [E3-codex-plugin-r2-2](../../evals/runs/E3-codex-plugin-r2-2/metadata.json) | [fail](../../evals/runs/E3-codex-plugin-r2-2/review.json) | 111.9 | 156,286 / 3,116 |
| [E3-codex-plugin-r2-3](../../evals/runs/E3-codex-plugin-r2-3/metadata.json) | [pass](../../evals/runs/E3-codex-plugin-r2-3/review.json) | 89.5 | 114,609 / 2,205 |
| [E3-codex-plugin-r3-1](../../evals/runs/E3-codex-plugin-r3-1/metadata.json) | [pass](../../evals/runs/E3-codex-plugin-r3-1/review.json) | 105.9 | 123,079 / 2,980 |
| [E3-codex-plugin-r3-2](../../evals/runs/E3-codex-plugin-r3-2/metadata.json) | [pass](../../evals/runs/E3-codex-plugin-r3-2/review.json) | 127.9 | 159,954 / 3,384 |
| [E3-codex-plugin-r3-3](../../evals/runs/E3-codex-plugin-r3-3/metadata.json) | [pass](../../evals/runs/E3-codex-plugin-r3-3/review.json) | 105.5 | 116,431 / 2,588 |
| [E3-codex-plugin-r4-1](../../evals/runs/E3-codex-plugin-r4-1/metadata.json) | [pass](../../evals/runs/E3-codex-plugin-r4-1/review.json) | 107.5 | 103,740 / 2,849 |
| [E3-codex-plugin-r4-2](../../evals/runs/E3-codex-plugin-r4-2/metadata.json) | [pass](../../evals/runs/E3-codex-plugin-r4-2/review.json) | 152.3 | 187,854 / 3,234 |
| [E3-codex-plugin-r4-3](../../evals/runs/E3-codex-plugin-r4-3/metadata.json) | [pass](../../evals/runs/E3-codex-plugin-r4-3/review.json) | 65.3 | 96,384 / 1,759 |
| [E4-codex-plugin-r1-1](../../evals/runs/E4-codex-plugin-r1-1/metadata.json) | [fail](../../evals/runs/E4-codex-plugin-r1-1/review.json) | 104.8 | 121,928 / 2,642 |
| [E4-codex-plugin-r2-1](../../evals/runs/E4-codex-plugin-r2-1/metadata.json) | [pass](../../evals/runs/E4-codex-plugin-r2-1/review.json) | 108.2 | 124,040 / 3,148 |
| [E5-codex-baseline-r1-1](../../evals/runs/E5-codex-baseline-r1-1/metadata.json) | [pass](../../evals/runs/E5-codex-baseline-r1-1/review.json) | 56.4 | 73,563 / 984 |
| [E5-codex-baseline-r1-2](../../evals/runs/E5-codex-baseline-r1-2/metadata.json) | [fail](../../evals/runs/E5-codex-baseline-r1-2/review.json) | 52.3 | 76,442 / 1,031 |
| [E5-codex-baseline-r2-1](../../evals/runs/E5-codex-baseline-r2-1/metadata.json) | [pass](../../evals/runs/E5-codex-baseline-r2-1/review.json) | 55.2 | 90,462 / 1,029 |
| [E5-codex-baseline-r2-2](../../evals/runs/E5-codex-baseline-r2-2/metadata.json) | [fail](../../evals/runs/E5-codex-baseline-r2-2/review.json) | 41.1 | 74,850 / 767 |
| [E5-codex-plugin-r1-1](../../evals/runs/E5-codex-plugin-r1-1/metadata.json) | [pass](../../evals/runs/E5-codex-plugin-r1-1/review.json) | 77.4 | 121,853 / 1,668 |
| [E5-codex-plugin-r1-2](../../evals/runs/E5-codex-plugin-r1-2/metadata.json) | [pass](../../evals/runs/E5-codex-plugin-r1-2/review.json) | 47.8 | 87,528 / 856 |
| [E5-codex-plugin-r2-1](../../evals/runs/E5-codex-plugin-r2-1/metadata.json) | [pass](../../evals/runs/E5-codex-plugin-r2-1/review.json) | 64.0 | 122,953 / 1,561 |
| [E5-codex-plugin-r2-2](../../evals/runs/E5-codex-plugin-r2-2/metadata.json) | [pass](../../evals/runs/E5-codex-plugin-r2-2/review.json) | 43.8 | 67,569 / 825 |
| [E6a-codex-plugin-r1-1](../../evals/runs/E6a-codex-plugin-r1-1/metadata.json) | [fail](../../evals/runs/E6a-codex-plugin-r1-1/review.json) | 97.2 | 104,881 / 2,574 |
| [E6a-codex-plugin-r2-1](../../evals/runs/E6a-codex-plugin-r2-1/metadata.json) | [pass](../../evals/runs/E6a-codex-plugin-r2-1/review.json) | 93.7 | 103,728 / 2,340 |
| [E6b-codex-plugin-r1-1](../../evals/runs/E6b-codex-plugin-r1-1/metadata.json) | [pass](../../evals/runs/E6b-codex-plugin-r1-1/review.json) | 139.2 | 110,217 / 4,737 |

## Remaining limitation and continuation

Claude Code is available as a checksum-verified temporary executable at `/private/tmp/repository-knowledge-tools/claude`, but its recorded authentication state is `none`. Sign in through `claude auth login` (or that executable's absolute path) without pasting credentials into chat. Then run the full Claude matrix, both cross-host directions, and the two-repeat Claude comparisons from the unchanged plan. Resolve any newly demonstrated failures and rerun affected cases before claiming two-host behavioral validation.

No plugin release, Git push, or source Page edit was performed. Installation/update tests are reversible host configuration operations; removal and target-repository preservation are recorded in lifecycle evidence. The local deliverable is ready for review, while full two-host acceptance remains incomplete.
