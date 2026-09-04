"""kpoison78.py -- s78 ITEM 3. LEVER TEST ON THE EIGENINDEX. F54.2's exact shape.
The eigenindex in t7c_hfsr.solve_one is implicit: the bracket is seeded from
eigen_sr(Vf, l, n, ...) and the bisection then hunts a zero of log(nrm). n is passed
POSITIONALLY, so a default patch would be DEAD. This wraps the MODULE-LEVEL NAME.
VERDICT rc=0 lever LIVE, rc=4 lever DEAD (never called, or output unmoved).
usage: python3 pack78/kpoison78.py <Z> <delta>
"""
import sys, os, json, time
import numpy as np
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
sys.path.insert(0, os.getcwd())
import t7c_hfsr as HS
import nlchain as NC
import hfc2 as H
from t7c_kernel import C0
H.CORR = False
L="spdfg"
Z = int(sys.argv[1]); DELTA = int(sys.argv[2])
rows = NC.load(); cfg = [tuple(x) for x in NC.cfg_from_chain(Z-1, rows)]

ORIG = HS.eigen_sr
CALLS = [0]
def clean(*a, **k):
    CALLS[0] += 1
    return ORIG(*a, **k)
def poisoned(Vf, l, n, *a, **k):
    CALLS[0] += 1
    return ORIG(Vf, l, n + DELTA, *a, **k)

def run(tag, fn):
    HS.eigen_sr = fn; CALLS[0] = 0
    t0 = time.time()
    try:
        E, Ec, it, eps = H.HFC(Z, cfg, c=C0).run2()
        r = dict(tag=tag, E=float(E), it=it, calls=CALLS[0], err=None)
        print(f"  {tag:<10s} E = {E:.9f} Ha   it={it}  eigen_sr calls={CALLS[0]}  {time.time()-t0:.0f}s")
    except Exception as e:
        r = dict(tag=tag, E=None, it=None, calls=CALLS[0],
                 err=f"{type(e).__name__}: {e}")
        print(f"  {tag:<10s} RAISED {r['err']}   eigen_sr calls={CALLS[0]}  {time.time()-t0:.0f}s")
    return r

print(f"EIGENINDEX LEVER TEST -- Z={Z}, poison n -> n{DELTA:+d}")
a = run("clean", clean)
b = run(f"poison{DELTA:+d}", poisoned)

verdict = "LIVE"
if b["calls"] == 0:
    print("  *** DEAD: the wrapper was NEVER CALLED. The lever does not reach the solver.")
    verdict = "DEAD"
elif a["E"] is not None and b["E"] is not None and abs(a["E"] - b["E"]) <= 1e-6:
    print(f"  *** DEAD: converged energy unmoved, |dE| = {abs(a['E']-b['E']):.3e} Ha <= 1e-6.")
    verdict = "DEAD"
elif a["E"] is not None and b["E"] is not None:
    print(f"  LEVER MOVES THE ENERGY: dE = {b['E']-a['E']:+.9f} Ha")
elif b["E"] is None and a["E"] is not None:
    print("  LEVER MOVES THE OUTPUT: the poisoned run does not reach a converged answer.")
print(f"LEVER: {verdict}")
json.dump(dict(Z=Z, delta=DELTA, verdict=verdict, clean=a, poisoned=b),
          open(f"../pack78/kpoison78_{Z}_{DELTA:+d}.json","w"), indent=1)
sys.exit(0 if verdict == "LIVE" else 4)