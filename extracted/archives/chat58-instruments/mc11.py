"""MC-11 — §10.4 closed-form void count.  Verify the tree factorisation and the
two closed-form leaves against direct enumeration.  Coordinates in tuple order
(n,l,k,q,e,f,g,S2) = positions 0..7 (matches lam8.py and the book's hi_7/lo_7, hi_6/lo_6).
"""
import random, itertools, sys
sys.path.insert(0, '.')
from lam8 import L8

CAP = (3, 3, 1, 3, 1)   # (capn, cape, capl, capk, capf)

def lattice(capn, cape, capl, capk, capf):
    out = []
    for n in range(1, capn + 1):
        for l in range(0, min(capl, n - 1) + 1):
            for k in range(1, min(capk, 4 * l + 2) + 1):
                for q in range(0, k + 1):
                    for e in range(1, cape + 1):
                        for f in range(0, min(capf, e - 1) + 1):
                            for g in range(0, min(4 * f + 2, q) + 1):
                                for S2 in range(0, k + 1):
                                    out.append((n, l, k, q, e, f, g, S2))
    return out

import numpy as np
_C = None
def direct(box_lo, box_hi, cells):
    """|box ∩ Λ| by brute enumeration of the lattice (vectorised, still exhaustive)."""
    global _C
    if _C is None or _C[1] is not cells: _C = (np.array(cells), cells)
    lo = np.array(box_lo); hi = np.array(box_hi)
    return int(((_C[0] >= lo) & (_C[0] <= hi)).all(1).sum())

def leaf_S2(lo, hi, k):
    return max(0, min(hi[7], k) - lo[7] + 1)

def leaf_g(lo, hi, q, f):
    return max(0, min(hi[6], q, 2 * (2 * f + 1)) - lo[6] + 1)

def factorised(lo, hi):
    """The book's §10.4 formula: sum over the six interior coordinates of the
    product of the edge indicators times the two closed-form leaf counts.
    Interior coordinates range over their box interval only (the box is the
    universe; Λ's own caps are already inside the box for any box [x∧y,x∨y])."""
    tot = 0
    for n in range(lo[0], hi[0] + 1):
        for l in range(lo[1], hi[1] + 1):
            if not (l <= n - 1): continue
            for k in range(lo[2], hi[2] + 1):
                if not (1 <= k <= 2 * (2 * l + 1)): continue
                for q in range(lo[3], hi[3] + 1):
                    if not (q <= k): continue
                    for e in range(lo[4], hi[4] + 1):
                        for f in range(lo[5], hi[5] + 1):
                            if not (f <= e - 1): continue
                            tot += leaf_S2(lo, hi, k) * leaf_g(lo, hi, q, f)
    return tot

def meet_join(x, y):
    return tuple(min(a, b) for a, b in zip(x, y)), tuple(max(a, b) for a, b in zip(x, y))

if __name__ == '__main__':
    cells = L8()
    assert len(cells) == 976 and lattice(*CAP) == cells
    random.seed(1106)
    # (1) eight random intervals [x∧y, x∨y] — the book's check, reproduced
    print("== eight random intervals ==")
    for t in range(8):
        x, y = random.sample(cells, 2)
        lo, hi = meet_join(x, y)
        d, fct = direct(lo, hi, cells), factorised(lo, hi)
        boxsize = 1
        for i in range(8): boxsize *= hi[i] - lo[i] + 1
        print(f"  lo={lo} hi={hi}  direct={d} factorised={fct} box={boxsize} void={boxsize-d}  {'OK' if d==fct else 'FAIL'}")
    # (2) exhaust: every unordered pair + every singleton
    print("== exhaustive over all pairs ==")
    from collections import Counter
    boxes = Counter()
    for i in range(len(cells)):
        for j in range(i, len(cells)):
            boxes[meet_join(cells[i], cells[j])] += 1
    npairs = sum(boxes.values()); print("  pairs+singletons", npairs, " distinct boxes", len(boxes), flush=True)
    fails = 0; nonempty_void_pairs = 0; done = 0
    for (lo, hi), mult in boxes.items():
        d, fct = direct(lo, hi, cells), factorised(lo, hi)
        if d != fct: fails += 1
        boxsize = 1
        for t in range(8): boxsize *= hi[t] - lo[t] + 1
        if boxsize - d > 0: nonempty_void_pairs += mult
        done += 1
        if done % 20000 == 0: print("   boxes done", done, "fails", fails, flush=True)
    print(f"  distinct boxes tested {len(boxes)} covering {npairs} pairs (475,800 + 976 = {475800+976}); factorised≠direct: {fails}")
    print(f"  pairs whose box has void>0: {nonempty_void_pairs}; void-free fraction (pairs+singletons): {(npairs-nonempty_void_pairs)/npairs:.4f}")
