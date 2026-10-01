#!/usr/bin/env python3
"""Build a deterministic local plugin archive, excluding development/evaluation files."""
from pathlib import Path
import hashlib
import json
import zipfile

root = Path(__file__).resolve().parents[1]
plugin = root / 'plugins/repository-knowledge'
version = json.loads((plugin / '.claude-plugin/plugin.json').read_text())['version']
destination = root / 'dist' / f'repository-knowledge-{version}.zip'
destination.parent.mkdir(exist_ok=True)
allowed = {'.codex-plugin', '.claude-plugin', 'skills', 'references'}
files = [p for p in sorted(plugin.rglob('*')) if p.is_file()]
for p in files:
    relative = p.relative_to(plugin)
    if p.is_symlink() or relative.parts[0] not in allowed:
        raise SystemExit(f'Unexpected packaged file: {relative}')
with zipfile.ZipFile(destination, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
    for p in files:
        name = 'repository-knowledge/' + p.relative_to(plugin).as_posix()
        info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, p.read_bytes())
with zipfile.ZipFile(destination) as archive:
    assert archive.testzip() is None
    assert len(archive.namelist()) == len(files)
    for p in files:
        assert archive.read('repository-knowledge/' + p.relative_to(plugin).as_posix()) == p.read_bytes()
print(destination)
print('SHA256', hashlib.sha256(destination.read_bytes()).hexdigest())
print(f'{len(files)} files; no evaluation artifacts')
