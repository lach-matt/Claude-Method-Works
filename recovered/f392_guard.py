#!/usr/bin/env python3
"""f392_guard.py -- AUDIT, not a measurement. Produces no new number.
Session 41. M's ruling: F39.2 is repaired only if it furthers n+l.

F39.2 mechanism (s40): solve_one computes tgt=n-l-1 and never uses it; the bracket
is a bare log-norm bracket. The node check is one level up (hfc2.py:55) and RAISES.
nlchain.step catches it, sets D=None, and DROPS the channel from `ok` before
win=min(ok,...). So a node-failed channel cannot win -- it vanishes.

THE ONLY WAY F39.2 CAN TOUCH AN n+l RESULT is if a DROPPED channel could have
outranked the winner. Guard: a step is UNSAFE iff nfail>0 and some dropped channel
has n+l <= n+l(winner). Then and only then does repair become load-bearing.
"""
import json, sys

def nl(tag):
    return int(tag[0]) + 'spdfg'.index(tag[1])

rows = [json.loads(l) for l in open('nlchain.jsonl') if l.strip()]
rows = [r for r in rows if r.get('mode')]
unsafe = []
drops  = 0
for r in rows:
    if not r.get('nfail'): continue
    drops += 1
    wnl = nl(r['ent'])
    bad = [k for k in r['fail'] if nl(k) <= wnl]
    tag = 'UNSAFE' if bad else 'safe'
    if bad: unsafe.append((r['Z'], bad))
    print(f"  Z={r['Z']:>3} ent={r['ent']} n+l={wnl}  dropped={list(r['fail'])} "
          f"n+l={[nl(k) for k in r['fail']]}  -> {tag}")
print()
print(f"  steps scored           : {len(rows)}")
print(f"  steps with a drop      : {drops}")
print(f"  steps UNSAFE for n+l   : {len(unsafe)}")
print(f"  F39.2 REPAIR REQUIRED  : {'YES ' + str(unsafe) if unsafe else 'NO'}")
sys.exit(1 if unsafe else 0)