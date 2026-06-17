#!/usr/bin/env python3
import os

ROOT = os.path.join(os.path.dirname(__file__), '..')

old1 = '/philly-tango-fest-teachers/'
old2 = '/philly-tango-fest-teachers'
new = '/teachers/'

changed_files = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    # skip node_modules, .git, and assets binary dirs
    if '.git' in dirpath or 'node_modules' in dirpath:
        continue
    for fname in filenames:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(dirpath, fname)
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                s = f.read()
        except Exception:
            continue
        ns = s.replace(old1, new).replace(old2, new.rstrip('/'))
        if ns != s:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(ns)
            changed_files.append(os.path.relpath(fpath, ROOT))

print('Updated files:')
for p in changed_files:
    print(p)
