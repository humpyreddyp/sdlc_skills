#!/usr/bin/env python3
"""Summarize recorded human-readable reviews and host telemetry, without grading."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
runs = root / 'evals/runs'


def stages(case, condition, repeat):
    count = 3 if case == 'E3' else 2 if case == 'E5' else 1
    return [f'{case}-codex-{condition}-r{repeat}-{n}' for n in range(1, count + 1)]


def status(names):
    verdicts = []
    for name in names:
        p = runs / name / 'review.json'
        verdicts.append(json.loads(p.read_text())['status'] if p.exists() else 'pending')
    return 'fail' if 'fail' in verdicts else 'blocked' if 'blocked' in verdicts else 'pending' if 'pending' in verdicts else 'pass'


def metrics(names):
    seconds = input_tokens = output_tokens = cached = 0
    for name in names:
        p = runs / name / 'metadata.json'
        if not p.exists():
            return 'pending'
        d = json.loads(p.read_text())
        seconds += d['elapsed_seconds']
        if not isinstance(d['usage'], list):
            return 'unavailable — host usage absent'
        for u in d['usage']:
            input_tokens += u.get('input_tokens', 0)
            output_tokens += u.get('output_tokens', 0)
            cached += u.get('cached_input_tokens', 0)
    return f'{seconds:.1f}s; {input_tokens:,} / {output_tokens:,} / {cached:,}'


selected = {
    'E1 — no knowledge': stages('E1', 'plugin', 1) + stages('E1', 'plugin', 2),
    'E2a — established documentation': stages('E2a', 'plugin', 1),
    'E2b — partial guidance': stages('E2b', 'plugin', 1),
    'E3 — fresh-session continuation': stages('E3', 'plugin', 3) + stages('E3', 'plugin', 4),
    'E4 — gap during delivery': stages('E4', 'plugin', 2),
    'E5 — maintenance and repeat': stages('E5', 'plugin', 1) + stages('E5', 'plugin', 2),
    'E6a — conflicting evidence': stages('E6a', 'plugin', 2),
    'E6b — unavailable check': stages('E6b', 'plugin', 1)}
all_pass = all(status(names) == 'pass' for names in selected.values())
rows = []
for label, names in selected.items():
    links = ', '.join(f'[{n}](../../evals/runs/{n}/review.json)' for n in names)
    rows.append(f'| {label} | {status(names)} | Blocked by authentication; not behaviorally validated | {links} |')

text = f'''# Evaluation results

Implementation and evaluation were authorized on 2026-10-01. **Codex: {'all selected same-host cases pass after repairs' if all_pass else 'review and repair reruns in progress'}. Claude Code: behavioral validation blocked by missing authentication.** Cross-host continuation and Claude comparisons are not complete, so V1 is not fully validated for both hosts.

## Package and structural checks

The installed Codex skill-creator initialized both skills; its `quick_validate.py` passed for each. Plugin-creator generated the Codex package and marketplace; its `validate_plugin.py` passed. Claude Code's manifest validator passed. The validators required PyYAML, installed in a temporary virtual environment. The plugin itself has no runtime dependencies.

Local install and changed-version update were exercised in both hosts: original `0.1.0` and repaired `0.1.1` (Codex adds its creator-generated build suffix). Codex reruns read the repaired installed-cache paths. Claude's CLI reports the installed 0.1.1 inventory, but no Claude model executed the skills. Lifecycle evidence is in [lifecycle records](../../evals/runs/lifecycle/). The [installation guide](../installation.md) covers install, update, invocation, and removal.

Both temporary plugin installations and their `sdlc-skills` marketplace registrations were removed after evaluation. [Removal evidence](../../evals/runs/lifecycle/removal.json) records all four successful commands and matching before/after hashes for every fixture file outside Git metadata. Generated knowledge and unfinished records were preserved. The repository's marketplace files remain available for installation.

Both evaluated packages are retained outside runtime resources: [original ZIP](../../evals/packages/repository-knowledge-0.1.0.zip) and [repaired ZIP](../../evals/packages/repository-knowledge-0.1.1.zip). Each contains nine plugin files; fixtures, expected answers, and reports are excluded.

## Method and scope

The [plan](plan.md) and [expected facts](../../evals/expected/outcomes.md) preceded behavioral execution. Expectations SHA256: `{hashlib.sha256((root / 'evals/expected/outcomes.md').read_bytes()).hexdigest()}`. The [fixture preflight](../../evals/runs/preflight/fixtures.json) verifies six passing base tests and the deliberately failing conflict/unavailable-check variants.

Codex CLI 0.158.0-alpha.2.1 used configured model `gpt-6-astra` with `high` reasoning. The CLI does not report the resolved runtime model identifier, so that field is marked unavailable. Claude Code 2.1.285 initialized with `claude-opus-5-5`, then rejected the request as unauthenticated before inference. [Environment evidence](../../evals/runs/preflight/environment.json), [successful Codex discovery](../../evals/runs/preflight/codex-discovery.jsonl), and [Claude attempt](../../evals/runs/E1-claude-plugin-r1-1/output.jsonl) preserve these distinctions.

Each executing session received a fresh isolated fixture and the ordinary task, with only the invocation wrapper differing for plugin/baseline. Expected answers were outside its workspace and context. Codex workspace-write still permits broader reads; this was not an OS-enforced unreadable grader directory. Visible command/file-change traces were reviewed for contamination and writes outside the fixture. No expectation-file access was observed. User configuration and the discovered unrelated skills were disabled for Codex, identically across conditions.

The primary Codex agent reviewed actual generated prose, behavior/reference accuracy, command results, ID identity, record lifecycle, and before/after diffs. It also authored the plugin, so this is not a blinded independent human study. Executing sessions did not grade themselves. The inspection helper checks preservation and relative file links; it does not judge wording or headings. Raw inputs, outputs, snapshots, hashes, usage, and individual review judgments are retained for inspection.

Original 0.1.0 runs hashed the source package before and after each run; [preflight](../../evals/runs/preflight/installed-package.json) confirmed that source and installed bytes matched. Those runs did not separately hash the installed cache after every session. The repaired 0.1.1 runner hashes the actual installed Codex cache before and after each plugin run. No changes to the checked package files were observed; visible write traces were also reviewed.

## Required outcomes

| Case | Codex selected runs | Claude Code | Review evidence |
| --- | --- | --- | --- |
''' + '\n'.join(rows) + '''

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
'''
for case in ['E1', 'E3', 'E5']:
    for repeat in [1, 2]:
        plugin_repeat = repeat + 2 if case == 'E3' else repeat
        pnames = stages(case, 'plugin', plugin_repeat)
        bnames = stages(case, 'baseline', repeat)
        text += f'| {case} / {repeat} | {status(pnames)}; {metrics(pnames)} | {status(bnames)}; {metrics(bnames)} |\n'
text += '''
Both preparation baselines produced useful accurate prose but omitted stable behavior IDs. Continuation baselines noticed changed sources and preserved work, but kept most resolved understanding in the delivery work document instead of publishing capability knowledge with stable IDs. Both maintenance baselines made further redundant documentation changes on the unchanged second invocation. The plugin's maintenance repeats made no file changes. These are failures against this plugin's acceptance criteria, not a claim that baseline output was generally unusable.

The data does not establish a general speed or token-saving benefit. The plugin's value in these fixtures is the required knowledge structure, uncertainty handling after repair, and stable maintenance. Repeated source-read counts are unavailable as a reliable metric; command counts and exact repeated-command counts are saved only as review signals. Account-wide cost and this supervising conversation's token usage are unavailable; per-run host token usage is recorded. Claude's rejected request reports zero inference tokens and no model execution.

Across 37 Codex sessions and one rejected Claude attempt, recorded totals are 4,057,974 input tokens (including 3,249,024 cached-input tokens), 85,223 output tokens, and 3,406.4 summed session seconds. These include original failures, baselines, and repair reruns; they exclude the supervising conversation and discovery preflights. See [session totals](../../evals/runs/lifecycle/session-totals.json).

## Complete run ledger

Each directory contains exact `input.txt`, `output.jsonl`, `stderr.txt`, `before/`, `after/`, `metadata.json`, and a separate `review.json`. Reviews include failures and their evidence. This ledger lists individual sessions; a multistep case requires all selected sessions to pass.

| Run | Review | Seconds | Input / output tokens |
| --- | --- | --- | --- |
'''
for p in sorted(runs.glob('*/metadata.json')):
    d = json.loads(p.read_text())
    review = p.parent / 'review.json'
    verdict = json.loads(review.read_text())['status'] if review.exists() else 'pending'
    usage = d['usage']
    tokens = 'unavailable'
    if isinstance(usage, list):
        tokens = f"{sum(u.get('input_tokens', 0) for u in usage):,} / {sum(u.get('output_tokens', 0) for u in usage):,}"
    name = p.parent.name
    text += f'| [{name}](../../evals/runs/{name}/metadata.json) | [{verdict}](../../evals/runs/{name}/review.json) | {d["elapsed_seconds"]:.1f} | {tokens} |\n'
text += '''
## Remaining limitation and continuation

Claude Code is available as a checksum-verified temporary executable at `/private/tmp/repository-knowledge-tools/claude`, but its recorded authentication state is `none`. Sign in through `claude auth login` (or that executable's absolute path) without pasting credentials into chat. Then run the full Claude matrix, both cross-host directions, and the two-repeat Claude comparisons from the unchanged plan. Resolve any newly demonstrated failures and rerun affected cases before claiming two-host behavioral validation.

No plugin release, Git push, or source Page edit was performed. Installation/update tests are reversible host configuration operations; removal and target-repository preservation are recorded in lifecycle evidence. The local deliverable is ready for review, while full two-host acceptance remains incomplete.
'''
(root / 'docs/evals/results.md').write_text(text)
print('Rendered results; all selected Codex cases pass:', all_pass)
