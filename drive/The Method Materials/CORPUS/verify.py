#!/usr/bin/env python3
"""Verify a checkout of method/members/ against MEMBER-INDEX.tsv.

No network, no bundle needed. Exit 0 iff every member is present and byte-identical.

    python3 method/verify.py          # from the repository root
    python3 verify.py                 # from method/
"""
import hashlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(HERE, 'MEMBER-INDEX.tsv')
MEM = os.path.join(HERE, 'members')

want = {}
with open(IDX, encoding='utf-8') as f:
    head = next(f).rstrip('\n').split('\t')
    assert head[:5] == ['member', 'bundle', 'ext', 'bytes', 'md5'], head
    for line in f:
        r = line.rstrip('\n').split('\t')
        want[r[0]] = (r[1], int(r[3]), r[4])

have = set(os.listdir(MEM)) if os.path.isdir(MEM) else set()
missing = sorted(set(want) - have)
extra = sorted(have - set(want))
altered = []
for name, (bundle, size, md5) in sorted(want.items()):
    p = os.path.join(MEM, name)
    if not os.path.exists(p):
        continue
    b = open(p, 'rb').read()
    if len(b) != size or hashlib.md5(b).hexdigest() != md5:
        altered.append((name, bundle, size, len(b), md5, hashlib.md5(b).hexdigest()))

print(f'indexed {len(want)} members, found {len(have)} files')
for n in missing:
    print(f'MISSING  {n}')
for n in extra:
    print(f'EXTRA    {n}')
for n, bundle, ws, hs, wm, hm in altered:
    print(f'ALTERED  {n}  [{bundle}]  bytes {ws} -> {hs}  md5 {wm} -> {hm}')

bad = len(missing) + len(extra) + len(altered)
print('VERIFY OK' if bad == 0 else f'VERIFY FAIL: {bad} problem(s)')
sys.exit(0 if bad == 0 else 1)
