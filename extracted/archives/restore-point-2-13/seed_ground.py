#!/usr/bin/env python3
"""seed_ground.py -- the seed's structure against the control group.

Registers 585-593 established the seed at 7. This session found more: four cells
are NECESSARY (zero alternatives, 12-23 uniquely covered elements each) and the
remaining three admit 519 completing triples over 66 distinct cells.

Nothing is a result until it survives the control group: the real atomic numbers.
This checks the four forced cells and the 66 free ones against the ground-state
configurations of all 118 elements.

  A cell (n, l, k, q, e, f, g, 2S) is REALISABLE if some element holds at least
  k electrons in subshell (n, l) and can accommodate g in subshell (e, f).

COMMITTED BEFORE COMPUTING (§2.13)
  The four forced cells will be realisable — they carry the extreme envelope
  steps, and extremes in Λ come from real subshell capacities. The 66 free cells
  will be realisable at a LOWER rate, because freedom lives where the physics
  does not bind.
"""
import itertools, sys
from collections import Counter
from zeno import State, step
import importlib.util as _iu, sys as _sys
_sp=_iu.spec_from_file_location("_cl","close_L118.py"); _m=_iu.module_from_spec(_sp)
_old=_sys.exit; _sys.exit=lambda *a: None
try: _sp.loader.exec_module(_m)
except Exception: pass
_sys.exit=_old
ELEMENTS, LMAP = _m.C, _m.L

CAP = lambda l: 4 * l + 2

def occupancy():
    """(n, l) -> the largest k any real element holds there"""
    best = {}
    for Z, (sym, sh) in ELEMENTS.items():
        for (n, sub, k) in sh:
            l = LMAP[sub]
            key = (n, l)
            if k > best.get(key, 0): best[key] = k
    return best

def realisable(cell, occ):
    n, l, k, q, e, f, g, S = cell
    # the source must exist and hold at least k
    if occ.get((n, l), 0) < k: return False
    # the target subshell must exist in some element and admit g
    if (e, f) not in occ: return False
    if g > CAP(f): return False
    # the transfer cannot exceed what is held, nor what the target takes
    if q > k or g > q: return False
    return True

FORCED = [(1,0,2,2,3,1,2,2), (2,1,3,3,1,0,0,3),
          (2,1,3,3,2,1,3,0), (3,1,1,0,3,1,0,0)]

def run():
    occ = occupancy()
    out = {"subshells seen in real elements": len(occ)}
    out["forced realisable"] = sum(1 for c in FORCED if realisable(c, occ))
    out["forced total"] = len(FORCED)
    # rebuild the 66 free cells
    from method_tower import base
    X = [tuple(c) for c in base((3,3,1,3,1))]
    A = [sorted({c[i] for c in X}) for i in range(8)]
    el, wit = [], {}
    for i in range(8):
        for j in range(8):
            if i == j: continue
            m = {}
            for c in X: m[c[j]] = max(m.get(c[j], -99), c[i])
            run_ = -99
            for v in sorted(m):
                if m[v] > run_:
                    run_ = m[v]; k_ = ("s", i, j, v, run_); el.append(k_)
                    wit[k_] = frozenset(c for c in X if c[j] == v and c[i] == run_)
    for i in range(8):
        for v in A[i]:
            k_ = ("a", i, v); el.append(k_); wit[k_] = frozenset(c for c in X if c[i] == v)
    cov = {c: {e for e in el if c in wit[e]} for c in X}
    F = set()
    for c in FORCED: F |= cov[c]
    rem = set(el) - F
    cands = [c for c in X if cov[c] & rem]
    trip = [t for t in itertools.combinations(cands, 3) if rem <= (cov[t[0]] | cov[t[1]] | cov[t[2]])]
    free = sorted({c for t in trip for c in t})
    out["completing triples"] = len(trip)
    out["free cells"] = len(free)
    out["free realisable"] = sum(1 for c in free if realisable(c, occ))
    # and the whole lattice, for the baseline rate
    out["lambda cells"] = len(X)
    out["lambda realisable"] = sum(1 for c in X if realisable(c, occ))
    return out, occ

with State("seed_ground") as st:
    R, occ = step(st, "ground the seed in the control group", run, budget=900)

print(f"  CONTROL GROUP: {len(ELEMENTS)} elements, "
      f"{R['subshells seen in real elements']} distinct subshells occupied\n")
print(f"  {'set':<24}{'cells':>7}{'realisable':>12}{'rate':>8}")
for lbl, a, b in (("the four FORCED", R['forced realisable'], R['forced total']),
                  ("the 66 FREE", R['free realisable'], R['free cells']),
                  ("all of Λ₈", R['lambda realisable'], R['lambda cells'])):
    print(f"  {lbl:<24}{b:>7}{a:>12}{100*a/b:>7.0f}%")
print(f"\n  completing triples: {R['completing triples']}")
