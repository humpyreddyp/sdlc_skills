#!/usr/bin/env python3
"""Run the planned Codex matrix; retain existing run IDs without overwriting them."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
cases = [('E2a', False, 1), ('E2b', False, 1), ('E4', False, 1),
         ('E6a', False, 1), ('E3', False, 1), ('E3', True, 1),
         ('E5', False, 1), ('E5', True, 1),
         ('E1', True, 2), ('E1', False, 2),
         ('E3', True, 2), ('E3', False, 2),
         ('E5', True, 2), ('E5', False, 2)]


def run(case):
    if (root / 'evals/.work/stop-matrix').exists():
        return 'Deferred after demonstrated failure; rerun after repair'
    name, baseline, repeat = case
    condition = 'baseline' if baseline else 'plugin'
    run_id = f'{name}-codex-{condition}-r{repeat}'
    if (root / 'evals/runs' / (run_id + '-1')).exists():
        return run_id + ': already exists; inspect rather than overwrite'
    command = [sys.executable, str(root / 'evals/run_case.py'), name, '--repeat', str(repeat)]
    if baseline:
        command.append('--baseline')
    result = subprocess.run(command, cwd=root, capture_output=True, text=True)
    return run_id + '\n' + result.stdout + result.stderr


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as pool:
        for future in as_completed([pool.submit(run, c) for c in cases]):
            print(future.result(), flush=True)
