#!/usr/bin/env python3
"""continuity.py -- §H.0. Run at session open, BEFORE gates, and again before any fault is
registered against chain state. Answers one question: is state I do not remember producing
CONTINUOUS with the sealed prefix? Never quarantines; prints what to reproduce.
usage: python3 continuity.py [sealed_copy]      default ../pack48/nlchain.jsonl
"""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
LIVE = 'nlchain.jsonl'
SEAL = sys.argv[1] if len(sys.argv) > 1 else '../pack48/nlchain.jsonl'
L = {json.loads(l)['Z']: json.loads(l) for l in open(LIVE)}
S = {json.loads(l)['Z']: json.loads(l) for l in open(SEAL)}
lz, sz = sorted(L), sorted(S)
print(f"  live  {len(lz)} rows Z={lz[0]}..{lz[-1]}")
print(f"  seal  {len(sz)} rows Z={sz[0]}..{sz[-1]}")
bad = 0
for Z in sz:                                    # the sealed prefix must be untouched
    if json.dumps(L.get(Z), sort_keys=True) != json.dumps(S[Z], sort_keys=True):
        print(f"  PREFIX ALTERED at Z={Z}  <-- this IS a fault"); bad += 1
extra = [Z for Z in lz if Z not in S]
if not extra:
    print("  no rows beyond the seal.")
else:
    import nlchain as NC
    print(f"  {len(extra)} row(s) beyond the seal: {extra}")
    for Z in extra:                              # continuity, not memory, decides
        want = NC.cfg_from_chain(Z - 1, L)
        got = L[Z]['ref_cfg']
        s = ''.join(f"{n}{'spdfg'[l]}{k}" for n, l, k in want)
        ok = (s == got)
        print(f"    Z={Z} ent={L[Z]['ent']} rung={L[Z]['rungs']} prov={L[Z]['prov']} "
              f"ref_cfg {'CONTINUOUS' if ok else 'BREAK'}")
        bad += 0 if ok else 1
    print(f"  REPRODUCE ONE ROW TO SETTLE IT:  Z={extra[0]}  (~100 s). Do not recompute the block.")
print(f"\nCONTINUITY: {'CLEAN' if not bad else f'{bad} REAL FAULT(S)'}")
sys.exit(1 if bad else 0)