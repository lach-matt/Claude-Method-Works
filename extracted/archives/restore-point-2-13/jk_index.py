#!/usr/bin/env python3
"""jk_index.py — does the three-axis rebuild CLOSE?

M's reading of Argon: three defects in one slot name three axes to look for,
and reading the labels confirms it. `2[3/2]* J=2` carries

    core   the parent ion's J     which ion state the electron orbits
    K      J_core (x) l           how the core's momentum couples to the orbit
    J      K (x) s                where the electron's own spin lands

and the s-channel proves J is a real axis rather than a label: at FIXED K = 3/2,
J = 1 gives 2.1778 and J = 2 gives 2.1978, a split of 0.0200.

WHY THIS MIGHT SUCCEED WHERE THE PARENT AXIS FAILED (R 1599). The parent term
count is a FIBRE — 1 or 3 or 16 or 119 depending on the species, so the product
admits 119 parents for species that have one. K and J are different in kind:
their ranges follow from ANGULAR MOMENTUM COUPLING, a fixed rule,

    K  runs |J_core - l| .. J_core + l
    J  runs K - 1/2 .. K + 1/2

so the range depends on (J_core, l) and NOT on the species. Whether that is
enough to close is the question, and register 1581 is the standing warning:
a determined axis need not close.

THE DOMAIN. This is tested where it is needed — the hole-plus-electron species
the keyability bound refuses. Their core is a p^5 hole, so J_core is 1/2 or 3/2
for every one of them, which is what makes the ranges uniform.
"""
import itertools, collections

INF = 10 ** 9


def clos(X, d):
    X = list(X)
    A = [sorted({c[i] for c in X}) for i in range(d)]
    ph = {}
    for a in range(d):
        for b in range(d):
            if a == b:
                continue
            m = {}
            for c in X:
                m[c[b]] = max(m.get(c[b], -INF), c[a])
            z = -INF
            o = {}
            for t in sorted(m):
                z = max(z, m[t])
                o[t] = z
            ph[(a, b)] = o
    return sum(1 for x in itertools.product(*A)
               if all(x[a] <= ph[(a, b)][x[b]]
                      for a in range(d) for b in range(d) if a != b))


def halves(lo, hi):
    """the ladder lo, lo+1, .., hi in half-integer units, as doubled integers."""
    return list(range(int(round(2 * lo)), int(round(2 * hi)) + 1, 2))


# ---- the jK cells, built from the coupling rule and nothing else ----------
# J_core doubled: 1 means 1/2, 3 means 3/2. A p^5 hole carries both.
CELLS = []
for jc in (1, 3):                       # 2*J_core
    for l in range(5):                  # s p d f g
        for K2 in halves(abs(jc / 2 - l), jc / 2 + l):
            for J2 in (K2 - 1, K2 + 1):
                if J2 >= 0:
                    CELLS.append((jc, l, K2, J2))

print(f"  jK cells from the coupling rule alone : {len(CELLS)}")
print(f"  distinct (J_core, l)                  : {len({(a,b) for a,b,_,_ in CELLS})}")
rng = collections.Counter()
for jc in (1, 3):
    for l in range(5):
        rng[len(halves(abs(jc / 2 - l), jc / 2 + l))] += 1
print(f"  K-range sizes across (J_core, l)      : {dict(sorted(rng.items()))}")
print(f"    (the parent axis had 1, 3, 16, 119 — R 1599)\n")

print("  DOES IT CLOSE?\n")
print(f"    {'coordinate set':<30}{'d':>3}{'cells':>8}{'|R(X)|':>10}{'E':>8}")
for lab, proj, d in (
        ("(l)", lambda t: (t[1],), 1),
        ("(J_core, l)", lambda t: (t[0], t[1]), 2),
        ("(J_core, l, K)", lambda t: (t[0], t[1], t[2]), 3),
        ("(J_core, l, K, J)", lambda t: t, 4)):
    X = {proj(t) for t in CELLS}
    n = clos(X, d)
    print(f"    {lab:<30}{d:>3}{len(X):>8,}{n:>10,}{n-len(X):>8,}")
