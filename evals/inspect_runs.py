#!/usr/bin/env python3
"""Collect review signals from artifacts; do not grade generated language."""
import json
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
signals = []
for run in sorted((root / 'evals/runs').iterdir()):
    metadata = run / 'metadata.json'
    if not metadata.exists():
        continue
    data = json.loads(metadata.read_text())
    before, after = data['before_hashes'], data['after_hashes']
    changed = sorted(k for k in before.keys() | after.keys() if before.get(k) != after.get(k))
    protected = [k for k in before if k.startswith(('tasklist/', 'tests/', 'tools/')) or k == 'docs/export-notes.md']
    preserved = all(before[k] == after.get(k) for k in protected)
    links = []
    for page in (run / 'after').rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', page.read_text()):
            target = target.split('#')[0]
            if not target or '://' in target or target.startswith('/'):
                continue
            if not (page.parent / target).exists():
                links.append({'page': str(page.relative_to(run / 'after')), 'target': target})
    commands = []
    for line in (run / 'output.jsonl').read_text().splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        item = event.get('item', {})
        if event.get('type') == 'item.completed' and item.get('type') == 'command_execution':
            commands.append({'command': item.get('command'), 'exit_code': item.get('exit_code')})
    record = {'run': run.name, 'changed_files': changed, 'protected_content_preserved': preserved,
              'broken_relative_file_links': links, 'command_count': len(commands),
              'exact_repeated_commands': len(commands) - len({c['command'] for c in commands}),
              'commands': commands, 'seconds': data['elapsed_seconds'], 'usage': data['usage']}
    (run / 'signals.json').write_text(json.dumps(record, indent=2) + '\n')
    signals.append({k: v for k, v in record.items() if k not in ['commands', 'usage']})
print(json.dumps(signals, indent=2))
