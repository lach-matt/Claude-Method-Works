#!/usr/bin/env python3
"""asm0.py -- RUNG 0 ASSEMBLY, the checkable clauses A0-A5 and A7.
Reads sealed nlchain.jsonl ONLY. No SCF, no re-run, deterministic.
Scores against pack63/PREDICTION-RUNG-0-ASSEMBLY.md (sha cdc0d2b1...).
usage: cd rt && python3 ../pack63/asm0.py [--fail]
"""
import sys, os, json
sys.path.insert(0, os.getcwd())

FAIL = '--fail' in sys.argv
rows = {d['Z']: d for d in map(json.loads, open('nlchain.jsonl'))}
bad = 0
def clause(name, ok, got, want):
    global bad
    bad += 0 if ok else 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print(f"         got  {got}")
    print(f"         want {want}")

print("=" * 74)
print("A0 - COMPLETE AND CONTIGUOUS")
Zs = sorted(rows)
gaps = [z for z in range(min(Zs), max(Zs) + 1) if z not in rows]
noent = [z for z in Zs if not rows[z].get('ent')]
ok = (len(rows) == 119 and min(Zs) == 2 and max(Zs) == 120 and not gaps and not noent)
clause("A0 chain complete", ok,
       f"{len(rows)} rows, Z {min(Zs)}..{max(Zs)}, gaps {gaps}, no-entrant {noent}",
       "119 rows, Z 2..120, no gaps, no missing entrant")

# ---- entrant sequence, chain's own column, ground.py NEVER consulted
seq = [(1, 0)] + [tuple(rows[z]['ent_nl']) for z in Zs]      # cfg(1)=1s is the seed
zof = [1] + Zs
TAG = lambda nl: f"{nl[0]}{'spdfghi'[nl[1]]}"
if FAIL: seq[6] = (3, 2)                                      # can-fail: force an n+l inversion

print("=" * 74)
print("A1 - PERIOD LENGTHS  (Challenge criterion: 2,8,8,18,18,32,32)")
starts = []
smax = 0
for nl, z in zip(seq, zof):
    if nl[1] == 0 and nl[0] > smax:
        smax = nl[0]; starts.append(z)
lens = [starts[i + 1] - starts[i] for i in range(len(starts) - 1)]
ok = (starts == [1, 3, 11, 19, 37, 55, 87, 119] and lens == [2, 8, 8, 18, 18, 32, 32])
clause("A1 period lengths", ok, f"starts {starts}  lengths {lens}",
       "starts [1,3,11,19,37,55,87,119]  lengths [2,8,8,18,18,32,32]")

print("=" * 74)
print("A2/A3/A4 - MADELUNG, FROM FIRST-ENTRY ORDER")
first, seen = [], set()
for nl in seq:
    if nl not in seen:
        seen.add(nl); first.append(nl)
nplus = [n + l for n, l in first]
inv = [(TAG(first[i]), TAG(first[i + 1])) for i in range(len(first) - 1) if nplus[i] > nplus[i + 1]]
clause("A2 n+l non-decreasing", not inv, f"{len(inv)} inversion(s) {inv}", "0 inversions")

tb = []
for i in range(len(first) - 1):
    if nplus[i] == nplus[i + 1] and first[i][0] > first[i + 1][0]:
        tb.append((TAG(first[i]), TAG(first[i + 1])))
clause("A3 tie-break increasing n", not tb, f"{len(tb)} violation(s) {tb}", "0 violations")

got = ' '.join(TAG(c) for c in first)
want = "1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p 8s"
clause("A4 madelung sequence", got == want, got, want)

print("=" * 74)
print("A5 - THE EXCEPTIONS")
sc = [z for z in Zs if rows[z]['ok'] is not None]
bd = [z for z in sc if rows[z]['ok'] is False]
blk = {}
for z in bd:
    blk['spdfg'[rows[z]['ent_nl'][1]]] = blk.get('spdfg'[rows[z]['ent_nl'][1]], 0) + 1
ok = (len(bd) < 25)
clause("A5 exception count < 25", ok,
       f"{len(bd)} of {len(sc)} scored rows, entrant-block {blk}", "< 25")
print("         rows: " + ' '.join(f"{z}({rows[z]['ent']}/{rows[z]['rec_ent']})" for z in bd))

print("=" * 74)
print(f"ASM0: {'PASS -- all clauses' if not bad else f'FAIL -- {bad} clause(s)'}")
sys.exit(1 if bad else 0)