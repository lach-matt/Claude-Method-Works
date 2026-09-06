"""f461_diag.py -- F46.1: WHY IS D_6p(Z=54) POSITIVE?
Reproduces the sealed value from the sealed reference configuration and reads
what nlchain.jsonl does not store: the iteration count and the converged eps.
Hypothesis under test: run2 breaks only on dmax<tol and RETURNS ANYWAY at maxit,
so a non-converged SCF yields a total energy with no error raised.
Comparison decides: 6p is run beside 6s and 5d on the same reference.
"""
import os, sys, json, time
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
import hfc2 as H
from t7c_kernel import C0
H.CORR = False

rows = {d['Z']: d for d in map(json.loads, open('nlchain.jsonl'))}
Z = int(sys.argv[1]) if len(sys.argv) > 1 else 54

def parse(s):
    import re
    return [(int(a), 'spdfg'.index(b), int(c)) for a, b, c in
            re.findall(r'(\d)([spdfg])(\d+)', s)]

cfg = parse(rows[Z]['ref_cfg'])
print(f"Z={Z}  ref_cfg electrons = {sum(k for _,_,k in cfg)}")

t = time.time()
Eref, _, itref, epsref = H.HFC(Z, [tuple(x) for x in cfg], c=C0).run2()
print(f"REF   E={Eref:.6f}  it={itref}  ({int(time.time()-t)}s)   "
      f"{'NOT CONVERGED (hit maxit)' if itref >= 100 else 'converged'}")

def add(cfg, c):
    d = {(n, l): k for n, l, k in cfg}
    d[c] = d.get(c, 0) + 1
    return [(n, l, k) for (n, l), k in sorted(d.items())]

for tag, c in [('6s', (6, 0)), ('5d', (5, 2)), ('6p', (6, 1))]:
    t = time.time()
    try:
        E, _, it, eps = H.HFC(Z, [tuple(x) for x in add(cfg, c)], c=C0).run2()
        flag = 'NOT CONVERGED (hit maxit)' if it >= 100 else 'converged'
        print(f"{tag}    D={E-Eref:+.5f}  it={it:>3}  eps={eps[c]:+.6f}  "
              f"({int(time.time()-t)}s)  {flag}")
    except Exception as e:
        print(f"{tag}    RAISED {type(e).__name__}: {str(e)[:80]}")
