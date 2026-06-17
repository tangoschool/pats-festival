#!/usr/bin/env python3
import os

ROOT = os.path.join(os.path.dirname(__file__), '..')

old = 'https://drive.google.com/file/d/19lrZBaO0DbpmR9MdziF2zYufpltoQfGl/view?usp=drive_link'
new = '/complete-schedule/'

changed = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    if '.git' in dirpath or 'node_modules' in dirpath:
        continue
    for fname in filenames:
        if not fname.endswith('.html'):
            continue
        path = os.path.join(dirpath, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                s = f.read()
        except Exception:
            continue
        if old in s:
            ns = s.replace(old, new)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(ns)
            changed.append(os.path.relpath(path, ROOT))

print('Updated files:')
for p in changed:
    print(p)
