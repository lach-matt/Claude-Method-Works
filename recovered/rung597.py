"""rung597.py -- s62. Prediction sha bdc1e7052de80073.
R5 classify _ceff  |  R9 candidate truncation  |  R7 minimal grid floor.
usage: python3 pack61/rung597.py 5 | 9 Z | 7 Z
"""
import sys, os, json, time
import numpy as np
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
sys.path.insert(0, os.getcwd())
import t7b_hf
import nlchain as NC
import nlguard as NG
import hfc2 as H
from t7c_kernel import C0
H.CORR = False

BASE_CEFF = t7b_hf.HF._ceff
HITS = {"frac": 0, "default": 0}


def counting_ceff(self, a, Q):
    if self.frac and a in self.frac:
        HITS["frac"] += 1
    else:
        HITS["default"] += 1
    return BASE_CEFF(self, a, Q)


def r5():
    """three directions, Rung 6's standard, on the walk's own path."""
    t7b_hf.HF._ceff = counting_ceff
    cfg = NC.cfg_from_chain(18, NC.load())          # the Z=19 reference configuration
    cfg = [tuple(x) for x in cfg]

    print("PHASE 1  frac unset (the ruling path)")
    HITS.update(frac=0, default=0)
    g1 = NG.run_guarded(19, cfg, 'r5')
    E1 = g1['E']
    print(f"   E = {E1:.9f}   frac-branch calls = {HITS['frac']}   default calls = {HITS['default']}")

    print("PHASE 2  frac FORCED ON for the 3p shell (must execute AND move the answer)")
    HITS.update(frac=0, default=0)
    h = H.HFC(19, cfg, c=C0); h.frac = {(3, 1): (6.0, 0.5)}
    E2, _, it2, _ = h.run2()
    f2 = HITS['frac']
    print(f"   E = {E2:.9f}   frac-branch calls = {f2}   dE = {E2-E1:+.9f} Ha")

    print("PHASE 3  released (must return BIT-IDENTICAL to phase 1)")
    HITS.update(frac=0, default=0)
    g3 = NG.run_guarded(19, cfg, 'r5')
    E3 = g3['E']
    print(f"   E = {E3:.9f}   frac-branch calls = {HITS['frac']}   identical={E3==E1}")

    v = "PASS"
    if g1['E'] is None or HITS['frac'] != 0: v = "VOID"
    if f2 == 0: print("   *** VOID: forcing frac did not execute the branch"); v = "VOID"
    if abs(E2 - E1) < 1e-9: print("   *** VOID: forcing frac changed nothing (F59.3)"); v = "VOID"
    if E3 != E1: print("   *** FAIL: release not bit-identical"); v = "FAIL"
    print(f"R5-1: {v}")

    print("R5-2  the q=1 falsifier: _ceff(q=1) = 0 -> NO self-repulsion at Z=1")
    t7b_hf.HF._ceff = BASE_CEFF
    hz = H.HFC(1, [(1, 0, 1.0)], c=C0)
    print(f"   _ceff at q=1 returns {hz._ceff((1,0),{(1,0):1.0})}")
    E, _, it, eps = hz.run2()
    print(f"   Z=1  E = {E:.9f} Ha   hydrogenic -0.5   d = {E+0.5:+.9f} Ha = {(E+0.5)*1000:+.4f} mHa")
    ok = (E + 0.5) < 1e-3 and (E + 0.5) > -1e-3
    print(f"R5-2: {'PASS' if ok else 'FAIL'}  (SR must sit at or just below -0.5 by <1 mHa)")
    json.dump(dict(E1=E1, E2=E2, E3=E3, fraccalls_on=f2, Z1=E), open("../pack61/r5.json", "w"), indent=1)


def r9(Z):
    """extend the candidate space and show every added channel loses."""
    rows = NC.load()
    cfg = [tuple(x) for x in NC.cfg_from_chain(Z - 1, rows)]
    d = {(n, l): k for n, l, k in cfg}
    N = max(n for n, l, k in cfg)
    inside = set(NC.candidates(cfg))
    extra = []
    for n in range(1, N + 3):
        for l in range(0, min(n - 1, 5) + 1):
            if d.get((n, l), 0) < NC.CAP(l) - 1e-9 and (n, l) not in inside:
                extra.append((n, l))
    print(f"R9 Z={Z}  in-space {len(inside)}  EXCLUDED-BY-TRUNCATION {len(extra)}: "
          + " ".join(f"{n}{'spdfg h'[l]}" for n, l in extra))
    g = NG.run_guarded(Z, cfg, 'ref')
    Eref = g['E']
    win = rows[Z]['ent']; Dwin = rows[Z]['D_ent']
    out = {}
    for c in extra:
        t0 = time.time()
        gg = NG.run_guarded(Z, NC.add(cfg, c), NC.tagof(c))
        D = round(gg['E'] - Eref, 5) if gg['conv'] else None
        out[NC.tagof(c)] = D
        gap = None if D is None else round(D - Dwin, 5)
        print(f"   {NC.tagof(c):>3}  D={D}  gap above winner {win}({Dwin}) = {gap} Ha  {int(time.time()-t0)}s")
    live = {k: v for k, v in out.items() if v is not None}
    if live:
        worst = min(live, key=lambda k: live[k])
        print(f"R9 Z={Z}: closest excluded channel {worst} at {live[worst]}, "
              f"gap {round(live[worst]-Dwin,5)} Ha above the winner. "
              f"{'PASS' if live[worst]-Dwin > 0.05 else 'FAIL'}")
    json.dump(out, open(f"../pack61/r9_{Z}.json", "w"), indent=1)


def r7(Z):
    """minimal floor: npts 4000 -> 3000 on the ruling path, one row."""
    rows = NC.load()
    cfg = [tuple(x) for x in NC.cfg_from_chain(Z - 1, rows)]
    res = {}
    for npts in (4000, 3000):
        Eref, _, _, _ = H.HFC(Z, cfg, c=C0, npts=npts).run2()
        D = {}
        for c in NC.candidates(cfg):
            try:
                E, _, _, _ = H.HFC(Z, [tuple(x) for x in NC.add(cfg, c)], c=C0, npts=npts).run2()
                D[NC.tagof(c)] = E - Eref
            except Exception as e:
                D[NC.tagof(c)] = None
        res[npts] = D
        live = {k: v for k, v in D.items() if v is not None}
        print(f"   npts={npts}  entrant {min(live,key=lambda k:live[k])}  "
              + " ".join(f"{k}={v:.5f}" for k, v in sorted(live.items(), key=lambda x: x[1])[:3]))
    common = [k for k in res[4000] if res[4000][k] is not None and res[3000].get(k) is not None]
    dmax = max(abs(res[4000][k] - res[3000][k]) for k in common)
    e4 = min(common, key=lambda k: res[4000][k]); e3 = min(common, key=lambda k: res[3000][k])
    print(f"R7 Z={Z}: max|dD| over {len(common)} channels = {dmax*1000:.4f} mHa "
          f"(tightest margin in the chain 32.33 mHa). entrant {e4} -> {e3} "
          f"{'UNCHANGED' if e4==e3 else 'CHANGED'}")
    json.dump({str(k): v for k, v in res.items()}, open(f"../pack61/r7_{Z}.json", "w"), indent=1)


if __name__ == "__main__":
    a = sys.argv[1]
    if a == "5": r5()
    elif a == "9": r9(int(sys.argv[2]))
    elif a == "7": r7(int(sys.argv[2]))
