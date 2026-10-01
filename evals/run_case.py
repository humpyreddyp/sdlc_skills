#!/usr/bin/env python3
"""Run real host sessions on isolated fixtures; never automatically grade prose."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / 'evals/fixtures/tasklist'
PLUGIN = ROOT / 'plugins/repository-knowledge'
WORK = Path('/private/tmp/repository-knowledge-evals')
DISABLED_SKILLS = ['belhaven-study-companion', 'bootstrap-context', 'compass',
                   'course-companion-orchestrator']
BOUNDARY = ('Work only in this repository and the installed skill resources, if any. '
            'Do not inspect other projects or evaluation materials. Do not use subagents, '
            'network services, commit, or change application code or tests. '
            'You may edit repository documentation and run existing local checks. ')
PREPARE = ('Prepare this repository for Codex and Claude Code to work on task completion. '
           'Explain current behavior, point me to relevant code and tests, '
           'and report whether the existing checks run.')
GAP = ('As part of the confirmation-message change in delivery.md, investigate repeated '
       'completion: should it succeed, and should it display a special message? '
       'Investigate available evidence and preserve the unfinished work if a decision '
       'is needed. Pause after asking necessary questions; I will answer next session.')
PROMPTS = {
    'E1': PREPARE, 'E2a': PREPARE, 'E2b': PREPARE,
    'E3': GAP, 'E4': GAP,
    'E5': 'Update the published knowledge to reflect the current uncommitted code and test change.',
    'E6a': 'Investigate the intended and current rule for completing an already completed task. Publish what is supported and identify any decision needed.',
    'E6b': 'Assess readiness for task-completion work and publish useful repository guidance for Codex and Claude Code. Verify the documented checks where possible.'}


def write(root, path, text):
    p = root / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)


def digest_tree(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob('*')) if p.is_file() and
            not any(x in p.parts for x in ['.git', '__pycache__']) and p.suffix != '.pyc'}


def snapshot(source, target):
    shutil.copytree(source, target, ignore=shutil.ignore_patterns('.git', '__pycache__', '*.pyc'))


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], text=True)


def docs(repo, wrong=False, navigation=True):
    repeat = 'raises ValueError and rejects the operation' if wrong else 'succeeds and keeps done true'
    write(repo, 'docs/completion.md', f'''# Task completion

One person can mark a local task complete by numeric ID. The CLI persists successful changes to JSON; the core function works on an in-memory list.

| ID | Condition | Behavior | Code and tests |
| --- | --- | --- | --- |
| COMP-01 | Existing not-done ID | Marks the task done and returns it | [complete_task](../tasklist/tasks.py); [test_complete_marks_done](../tests/test_tasks.py) checks the returned and stored flag |
| COMP-02 | Missing ID | Raises KeyError | [complete_task](../tasklist/tasks.py); [test_missing_id_rejected](../tests/test_tasks.py) checks a missing ID |
| COMP-03 | Already done ID | {repeat} | [complete_task](../tasklist/tasks.py); [test_repeat_completion_is_idempotent](../tests/test_tasks.py) checks repeated completion |

The CLI calls complete_task, reports errors with exit status 2, and writes the JSON file after success. Core tests do not test CLI persistence. See [working instructions](../README.md) for setup and checks.
''')
    if navigation:
        write(repo, 'docs/index.md', '# Knowledge\n\nA local task list lets one person add, list, and complete tasks. Read [completion](completion.md) and [setup and checks](../README.md).\n')
        for name in ['AGENTS.md', 'CLAUDE.md']:
            write(repo, name, '# Repository instructions\n\nRead [knowledge](docs/index.md) for task completion. Never use live customer data in examples.\n')


def setup(repo, case):
    shutil.copytree(FIXTURE, repo, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    if case in ['E2a', 'E2b', 'E5']:
        docs(repo, wrong=case == 'E2a', navigation=case != 'E2b')
    if case in ['E3', 'E4']:
        write(repo, 'delivery.md', '# Confirmation-message change\n\nAdd a friendly confirmation message when the user completes a task. Investigate repeated completion before implementing the message. Application implementation remains pending.\n')
    if case == 'E6a':
        write(repo, 'requirements.md', '# Confirmed requirement\n\nA repeated completion must be rejected with ValueError. This requirement was confirmed by the product owner; current compliance has not been verified.\n')
        p = repo / 'tests/test_tasks.py'
        p.write_text(p.read_text().replace('self.assertTrue(complete_task(tasks, 1)["done"])\n\n    def test_missing', 'with self.assertRaises(ValueError):\n            complete_task(tasks, 1)\n\n    def test_missing'))
    if case == 'E6b':
        p = repo / 'README.md'
        p.write_text(p.read_text().replace('python3 -m unittest discover -s tests -v', 'python3 tools/verify.py') + '\nThe verification wrapper requires the separately provided repository_eval_missing_dependency module; it is not vendored here.\n')
        write(repo, 'tools/verify.py', 'import repository_eval_missing_dependency\nrepository_eval_missing_dependency.verify()\n')
    git(repo, 'init', '-q')
    git(repo, 'add', '.')
    git(repo, '-c', 'user.name=Fixture Evaluator', '-c', 'user.email=evaluator@example.invalid',
        'commit', '-qm', 'Frozen fixture input')
    if case == 'E5':
        mutate(repo, 'E5')


def mutate(repo, case):
    for filename in ['tasklist/tasks.py', 'tasklist/cli.py', 'tests/test_tasks.py']:
        p = repo / filename
        p.write_text(p.read_text().replace('complete_task', 'finish_task'))
    if case == 'E3':
        p = repo / 'tasklist/tasks.py'
        p.write_text(p.read_text().replace('raise KeyError(task_id)', 'raise ValueError("unknown task")'))
        p = repo / 'tests/test_tasks.py'
        p.write_text(p.read_text().replace('with self.assertRaises(KeyError)', 'with self.assertRaises(ValueError)'))
    elif case == 'E5':
        p = repo / 'tasklist/tasks.py'
        p.write_text(p.read_text().replace('            task["done"] = True', '            if task["done"]:\n                raise ValueError("already complete")\n            task["done"] = True'))
        p = repo / 'tests/test_tasks.py'
        p.write_text(p.read_text().replace('test_repeat_completion_is_idempotent', 'test_repeat_completion_rejected').replace('self.assertTrue(finish_task(tasks, 1)["done"])\n\n    def test_missing', 'with self.assertRaises(ValueError):\n            finish_task(tasks, 1)\n\n    def test_missing'))


def command(host, repo, plugin, output, skill):
    if host == 'codex':
        skill_config = 'skills={bundled={enabled=false},config=[' + ','.join(
            '{name=' + json.dumps(n) + ',enabled=false}' for n in DISABLED_SKILLS) + ']}'
        plugins = 'plugins={"repository-knowledge@sdlc-skills"={enabled=' + ('true' if plugin else 'false') + '}}'
        return ['codex', 'exec', '--ignore-user-config', '--ephemeral', '--json',
                '--disable', 'apps', '--disable', 'browser_use', '--disable', 'multi_agent',
                '-c', skill_config, '-c', plugins, '-c', 'model="gpt-6-astra"',
                '-c', 'model_reasoning_effort="high"', '-c', 'approval_policy="never"',
                '-s', 'workspace-write', '-C', str(repo), '-o', str(output / 'final.md'), '-']
    executable = os.environ.get('REPOSITORY_KNOWLEDGE_CLAUDE', '/private/tmp/repository-knowledge-tools/claude')
    cmd = [executable, '-p', '--output-format', 'stream-json', '--verbose',
           '--setting-sources', 'project', '--strict-mcp-config', '--no-session-persistence',
           '--permission-mode', 'acceptEdits', '--allowedTools', 'Read,Edit,Write,Glob,Grep,Bash(python3 *),Bash(git *),Bash(rg *),Bash(cat *),Bash(ls *)']
    if plugin:
        cmd += ['--plugin-dir', str(PLUGIN)]
    return cmd


def execute(host, repo, plugin, out, prompt, skill, timeout):
    out.mkdir(parents=True)
    wrapper = ''
    if plugin:
        wrapper = (f'Use $repository-knowledge:{skill}. ' if host == 'codex'
                   else f'Use /repository-knowledge:{skill}. ')
    text = wrapper + BOUNDARY + '\n\n' + prompt
    (out / 'input.txt').write_text(text + '\n')
    snapshot(repo, out / 'before')
    before = digest_tree(repo)
    package_root = PLUGIN
    if host == 'codex' and plugin:
        version = json.loads((PLUGIN / '.codex-plugin/plugin.json').read_text())['version']
        package_root = Path.home() / '.codex/plugins/cache/sdlc-skills/repository-knowledge' / version
        if not package_root.is_dir():
            raise RuntimeError('Install the current Codex package before evaluation')
    package_before = digest_tree(package_root)
    cmd = command(host, repo, plugin, out, skill)
    start = datetime.now(timezone.utc).isoformat()
    monotonic = time.monotonic()
    state = 'exited'
    with (out / 'output.jsonl').open('w') as stdout, (out / 'stderr.txt').open('w') as stderr:
        proc = subprocess.Popen(cmd, cwd=repo, stdin=subprocess.PIPE, stdout=stdout, stderr=stderr, start_new_session=True, text=True)
        try:
            proc.communicate(text, timeout=timeout)
        except subprocess.TimeoutExpired:
            import signal
            os.killpg(proc.pid, signal.SIGTERM)
            proc.wait(timeout=15)
            state = 'timeout'
    elapsed = time.monotonic() - monotonic
    snapshot(repo, out / 'after')
    (out / 'working.diff').write_text(git(repo, 'diff', '--no-ext-diff'))
    events = []
    for line in (out / 'output.jsonl').read_text().splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    usage = [e['usage'] for e in events if e.get('type') == 'turn.completed']
    if host == 'claude':
        usage = [e.get('usage') for e in events if e.get('type') == 'result']
    summary = {
        'host': host, 'command': cmd, 'plugin': plugin, 'skill': skill,
        'host_version': subprocess.run([cmd[0], '--version'], capture_output=True, text=True).stdout.strip() or 'unavailable — version command returned no stdout',
        'plugin_version': json.loads((PLUGIN / ('.codex-plugin' if host == 'codex' else '.claude-plugin') / 'plugin.json').read_text())['version'] if plugin else None,
        'model_requested': 'gpt-6-astra' if host == 'codex' else 'host default',
        'model_reported': next((e.get('model') for e in events if e.get('type') == 'system' and e.get('subtype') == 'init'), 'unavailable — Codex JSONL does not report resolved runtime model'),
        'reasoning': 'high' if host == 'codex' else 'host default',
        'started_at': start, 'finished_at': datetime.now(timezone.utc).isoformat(),
        'elapsed_seconds': round(elapsed, 3), 'exit_code': proc.returncode, 'execution': state,
        'usage': usage or 'unavailable — no host usage event',
        'before_hashes': before, 'after_hashes': digest_tree(repo),
        'plugin_root': str(package_root), 'plugin_hashes': package_before, 'plugin_unchanged': package_before == digest_tree(package_root),
        'judgment': 'pending artifact and behavior review',
        'isolation': 'fresh ephemeral session; unrelated Codex skills disabled; workspace-write permits broader reads, restricted by identical task boundary; no expected answers supplied'}
    (out / 'metadata.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps({'run': out.name, 'exit': proc.returncode, 'seconds': elapsed, 'usage': usage}), flush=True)
    return proc.returncode == 0 and state == 'exited'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('case', choices=PROMPTS)
    parser.add_argument('--host', choices=['codex', 'claude'], default='codex')
    parser.add_argument('--destination-host', choices=['codex', 'claude'], help='E3 only: use this host for fresh-session continuation')
    parser.add_argument('--baseline', action='store_true')
    parser.add_argument('--repeat', type=int, default=1)
    parser.add_argument('--timeout', type=int, default=600)
    args = parser.parse_args()
    if args.destination_host and args.case != 'E3':
        parser.error('--destination-host is only valid for E3')
    destination_host = args.destination_host or args.host
    host_label = args.host if destination_host == args.host else args.host + '-to-' + destination_host
    condition = 'baseline' if args.baseline else 'plugin'
    name = f'{args.case}-{host_label}-{condition}-r{args.repeat}'
    repo = WORK / name
    if repo.exists() or (ROOT / 'evals/runs' / (name + '-1')).exists():
        raise SystemExit('Run already exists; select a new repeat number to preserve evidence.')
    setup(repo, args.case)
    outroot = ROOT / 'evals/runs'
    skill = 'knowledge-maintain' if args.case == 'E5' else 'knowledge-discover'
    if not execute(args.host, repo, not args.baseline, outroot / (name + '-1'), PROMPTS[args.case], skill, args.timeout):
        return
    if args.case == 'E5':
        execute(args.host, repo, not args.baseline, outroot / (name + '-2'), PROMPTS['E5'], skill, args.timeout)
    if args.case == 'E3':
        mutate(repo, 'E3')
        if execute(destination_host, repo, not args.baseline, outroot / (name + '-2'), 'Continue the saved task-completion investigation.', skill, args.timeout):
            execute(destination_host, repo, not args.baseline, outroot / (name + '-3'), 'Continue the investigation. My decision: repeated completion should succeed and show “Already complete”. Publish the confirmed requirement, preserve pending implementation work in delivery.md, and finish the investigation. Do not implement the application change.', skill, args.timeout)


if __name__ == '__main__':
    main()
