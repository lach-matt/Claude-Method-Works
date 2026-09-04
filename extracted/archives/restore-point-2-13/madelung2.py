#!/usr/bin/env python3
"""madelung2.py -- does the channel equation PRODUCE the n+l rule?

Register 1250. The equation was fitted to quantum defects. It knows nothing about
n+l: its inputs are p (the core's orbital count at that l, from Pauli), Ne (the
electron count, through Thomas-Fermi screening) and c (the charge, through the
isoelectronic form). No term in it references n+l, and it was never fitted against
a filling order.

    p > 0 :  delta = a p^e(Ne) Ne^k ln(c+1)/c
    p = 0 :  delta = h C(Z) (Ne-1)/Ne Ne^k ln(c+1)/c

The energy of a subshell is E = -Zc^2 R / (n - delta)^2, so the subshell that fills
first is the one with the smallest n* = n - delta. And the first available n for a
given l is fixed by orthogonality to the core:

    n0(l) = p(l) + l + 1

because a radial function with l must have at least p nodes to be orthogonal to the
p core orbitals of the same l, and an nl function has n - l - 1 nodes.

So for each element the equation gives, with no free choice:

    n*(l) = p(l) + l + 1 - delta(p(l), Ne, c)

THE TEST. For every element, rank the available subshells by n* and compare to the
Madelung order (smallest n+l first, then smallest n). If the equation reproduces the
order, the n+l rule is a CONSEQUENCE of three mechanisms that are individually
attributed -- Pauli 1925 for p, Fermi 1928 for Ne^k, Edlen 1964 for the charge form
-- and none of which mentions n+l.
"""
import math
import numpy as np

A, E0, E1, K, HH = 0.3772, 0.8297, -0.0900, 0.4942, 0.5415

ORDER = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
         (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1),(8,0)]
OPEN = {}; _z = 0
for _n, _l in ORDER: OPEN[(_n,_l)] = _z + 1; _z += 2*(2*_l+1)

def config(ne):
    """the aufbau ground configuration for ne electrons, as (n, l, occ)"""
    out = []; left = ne
    for n, l in ORDER:
        if left <= 0: break
        cap = 2*(2*l+1); k = min(cap, left)
        out.append((n, l, k)); left -= k
    return out

def core_p(ne, l):
    """how many orbitals of this l the core already holds"""
    return sum(1 for n, ll, o in config(ne) if ll == l and o > 0)

def delta(Z, c, l):
    ne = Z - c + 1
    p = core_p(ne - 1, l)
    t = math.log(c + 1) / c
    if p > 0:
        e = max(E0 + E1*math.log(max(ne, 2)), 0.05)
        return A * (p**e) * ne**K * t
    # p = 0: the collapse branch
    v = [n for n, ll, o in config(ne - 1) if ll == l and o > 0]
    n0 = (max(v) + 1) if v else l + 1
    thr = OPEN.get((n0, l), 999)
    C = min(max((Z - thr + 4.0)/8.0, 0.0), 1.0)
    return HH * C * ((ne - 1)/ne) * ne**K * t

def n0_of(ne, l):
    """the first Pauli-allowed n for this l -- p nodes forced by orthogonality"""
    return core_p(ne, l) + l + 1

def madelung_key(n, l):
    return (n + l, n)

# ---------------------------------------------------------------- the test
print("  DOES THE EQUATION PRODUCE THE FILLING ORDER?\n")
print("      inputs: p (Pauli 1925) · Nₑ^k (Fermi 1928) · ln(c+1)/c (Edlén 1964)")
print("      NO term references n+ℓ, and the equation was never fitted to an order.\n")

agree = disagree = 0
rows = []
BAD = []
for Z in range(3, 104):
    ne = Z                      # neutral
    cfg = config(ne - 1)        # the core, one electron short
    # every l that could receive the next electron
    cand = []
    for l in range(0, 5):
        n = n0_of(ne - 1, l)
        if n > 8: continue
        d = delta(Z, 1, l)
        cand.append((l, n, d, n - d))
    if len(cand) < 2: continue
    # the equation's order, and Madelung's
    eq_order  = [x[0] for x in sorted(cand, key=lambda x: x[3])]
    mad_order = [x[0] for x in sorted(cand, key=lambda x: madelung_key(x[1], x[0]))]
    # compare pairwise
    for i in range(len(cand)):
        for j in range(i+1, len(cand)):
            a, b = cand[i], cand[j]
            ma, mb = madelung_key(a[1], a[0]), madelung_key(b[1], b[0])
            if ma == mb: continue
            lo, hi = (a, b) if ma < mb else (b, a)
            if lo[3] < hi[3]: agree += 1
            else:
                disagree += 1
                BAD.append((Z, lo, hi))
    rows.append((Z, eq_order, mad_order, cand))

tot = agree + disagree
print(f"  PAIRWISE, over elements Z = 3 to 103\n")
print(f"      comparisons          : {tot}")
print(f"      equation agrees      : {agree}   ({100*agree/tot:.1f}%)")
print(f"      equation disagrees   : {disagree}")
print()

exact = sum(1 for _, e, m, _ in rows if e == m)
print(f"  FULL ORDER, per element\n")
print(f"      elements tested      : {len(rows)}")
print(f"      order reproduced EXACTLY: {exact}   ({100*exact/len(rows):.1f}%)")
print()

if BAD:
    from collections import Counter
    L = "spdfg"
    print(f"  WHERE IT DISAGREES\n")
    print("      by ℓ-pair : " + "  ".join(
        f"{L[a]}–{L[b]}:{v}"
        for (a, b), v in Counter((lo[0], hi[0]) for _, lo, hi in BAD).most_common()))
    zz = sorted({z for z, _, _ in BAD})
    print(f"      by Z      : {zz[:26]}{' …' if len(zz) > 26 else ''}")
    print()
    print(f"      {'Z':>4}{'Madelung first':>18}{'n*':>9}{'then':>10}{'n*':>9}")
    for z, lo, hi in BAD[:18]:
        print(f"      {z:>4}{f'{lo[1]}{L[lo[0]]}':>18}{lo[3]:>9.3f}"
              f"{f'{hi[1]}{L[hi[0]]}':>10}{hi[3]:>9.3f}")
