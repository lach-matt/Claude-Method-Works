#!/usr/bin/env python3
"""The Method 1.6 densities.py -- reconstructed from §12.11.1's stated definition.

The file named in the manifest was never supplied. This is rebuilt from the
DEFINITION the book prints, not from the figures it must reproduce:

  "For each axis, over every cell of the stage below that the lattice admits,
   count the values of the new coordinate that exact vector coupling realises
   and divide by the values the admissible bound allows."

and the three exact sets §12.11.1 says the column cannot be reproduced without:

  axis 9   the spin set of f^g by microstate enumeration
  axis 10  the terms genuinely NEW at occupancy v -- terms(f^v) less
           terms(f^(v-2)) as multisets -- conjoined with the parity congruence
           and the conjugation ceiling
  axis 11  the J values of terms of l^k carrying the CELL'S OWN multiplicity 2S,
           not of all terms of l^k
"""
import sys
from collections import Counter
from functools import lru_cache
from method_tower import base, terms, exact_2S, exact_2J, max2J, phihat

CAPS = (3, 3, 1, 3, 1)
NMAX, EMAX, LMAX, KMAX, FMAX = CAPS

@lru_cache(maxsize=None)
def new_at_v(f, v):
    """terms genuinely new at occupancy v: terms(f^v) less terms(f^(v-2))"""
    a = Counter(terms(f, v))
    b = Counter(terms(f, v - 2)) if v >= 2 else Counter()
    return a - b

@lru_cache(maxsize=None)
def exact_2J_at_2S(l, k, S2):
    """the J values of terms of l^k carrying multiplicity 2S -- axis 11's set"""
    js = set()
    for s2, L2 in terms(l, k):
        if s2 != S2: continue
        for j2 in range(abs(L2 - s2), L2 + s2 + 1, 2): js.add(j2)
    return tuple(sorted(js))

def densities():
    L8 = base(CAPS)
    ph = {k: phihat(k, LMAX) for k in range(0, KMAX + 1)}
    d = {}

    # axis 9 : 2S' <= g. exact = spin set of f^g
    adm = ex = 0
    for c in L8:
        f, g = c[5], c[6]
        adm += g + 1
        ex  += len(exact_2S(f, g))
    d["9"] = ex / adm

    # axis 9' : + 2S' <= 2f+1
    adm = ex = 0
    for c in L8:
        f, g = c[5], c[6]
        adm += min(g, 2 * f + 1) + 1
        ex  += len([s for s in exact_2S(f, g) if s <= 2 * f + 1])
    d["9'"] = ex / adm

    # axis 10 : 2S' <= v <= g, v ≡ g (mod 2), and the conjugation ceiling
    adm = ex = 0
    for c in L8:
        f, g = c[5], c[6]
        for S2 in range(0, g + 1):
            adm += max(0, g - S2 + 1)
            if S2 in exact_2S(f, g):
                ceil = min(g, 4 * f + 2 - g)
                ex += len([v for v in range(S2, ceil + 1, 2)
                           if any(s == S2 for s, _ in new_at_v(f, v))])
    d["10"] = ex / adm

    # axis 11 : 2J_c <= phihat(k), exact = J of terms of l^k at the cell's own 2S
    adm = ex = 0
    for c in L8:
        l, k, S2 = c[1], c[2], c[7]
        adm += ph[k] + 1
        ex  += len(exact_2J_at_2S(l, k, S2))
    d["11"] = ex / adm

    # axis 12 : 2K <= 2J_c + 2f_max ; exact triangle |2Jc-2f| .. 2Jc+2f step 2.
    # TWO THINGS THE DEFINITION REQUIRES AND A LOOSE READING DROPS:
    #  (i)  the sum runs over the STAGE BELOW, which for axis 12 is Λ₁₁, so the
    #       cells are Λ₁₀'s weighted by their own 2S' and v fibres -- not Λ₈'s
    #  (ii) J_c's realisability is axis 11's price, 17.0%. filtering on it here
    #       charges one envelope twice, and §12.11.3's dichotomy says each
    #       coupling axis pays once. over Λ₈ with the filter: 12.7%. without it:
    #       30.8%. over Λ₁₀ without it: 31.4%.
    L9  = [c + (s,) for c in L8 for s in range(0, c[6] + 1)]
    L10 = [c + (v,) for c in L9 for v in range(c[8], c[6] + 1)]
    adm = ex = 0
    for c in L10:
        l, k, f = c[1], c[2], c[5]
        for j2 in range(0, ph[k] + 1):
            adm += j2 + 2 * FMAX + 1
            ex  += len(range(abs(j2 - 2 * f), j2 + 2 * f + 1, 2))
    d["12"] = ex / adm

    # axis 13 : |2J - 2K| <= 1 admits up to 3 values (>= 0); exact is a doublet
    # everywhere except the K = 0 singlet
    adm = ex = 0
    for c in L8:
        l, k, f = c[1], c[2], c[5]
        for j2 in range(0, ph[k] + 1):
            for K in range(0, j2 + 2 * FMAX + 1):
                adm += len([J for J in range(max(0, K - 1), K + 2)])
                ex  += 1 if K == 0 else 2
    d["13"] = ex / adm
    return d

STATED = {"9": 63.7, "9'": 67.5, "10": 44.7, "11": 17.0, "12": 31.4, "13": 64.4}
if __name__ == "__main__":
    d = densities()
    print(f"  {'axis':<6}{'recomputed':>12}{'stated':>10}   verdict")
    bad = 0
    for a in ("9", "9'", "10", "11", "12", "13"):
        v = 100 * d[a]
        ok = abs(v - STATED[a]) < 0.05
        bad += not ok
        print(f"  {a:<6}{v:>11.1f}%{STATED[a]:>9.1f}%   {'reproduces' if ok else 'DIFFERS'}")
    print(f"\n  {6-bad} of 6 reproduce")
    sys.exit(bad)
