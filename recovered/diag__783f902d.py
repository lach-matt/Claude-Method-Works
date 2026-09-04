"""diag.py -- SESSION 65, AFTER THE SCORE. DIAGNOSTIC, NOT A TEST.
Nothing here is scored against any prediction. It exists to say what the four p->d
failures have in common, so that a REFINEMENT can be filed as a fresh prediction
rather than fitted to the failure. Read-only, no solves."""
import json, os, statistics as st
rows = {json.loads(l)['Z']: json.loads(l) for l in open('../rt/nlchain.jsonl')}
T = lambda n, l: f"{n}{'spdfg'[l]}"
def ratio(D, n, l):
    a,b,c = T(n,l), T(n,l+1), T(n+1,l)
    if not (a in D and b in D and c in D): return None
    den = D[c]-D[a]
    return None if abs(den)<=1e-4 else (D[b]-D[a])/den
print("  every p->d measurement in the pool, by base n and Z")
for Z in sorted(rows):
    if Z<3: continue
    D = dict(rows[Z]['order'])
    for n in range(2,8):
        v = ratio(D,n,1)
        if v is not None: print(f"    Z={Z:>4}  base {n}p   a={v:7.4f}")
print("\n  the four blocks that failed need a(n,1) at:")
for n,Zo in ((3,21),(4,39),(5,57),(6,89)):
    D=dict(rows[Zo]['order'])
    print(f"    base {n}p at Z={Zo:>4}: {T(n,1)} in candidate list? "
          f"{T(n,1) in D}   (base is FULL at Zopen -- that is why T-B had no data)")
print("\n  same-l-pair measurements grouped by base n:")
by={}
for Z in sorted(rows):
    if Z<3: continue
    D=dict(rows[Z]['order'])
    for n in range(2,8):
        v=ratio(D,n,1)
        if v is not None: by.setdefault(n,[]).append((Z,v))
for n in sorted(by):
    v=[x[1] for x in by[n]]
    print(f"    base {n}p  n={len(v):>2}  median {st.median(v):7.4f}  "
          f"Z {min(x[0] for x in by[n])}-{max(x[0] for x in by[n])}")