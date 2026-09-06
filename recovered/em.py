#!/usr/bin/env python3
"""em.py -- the electromagnetic index, built inside Λ.

THE CLAIM UNDER TEST. The selection rules are not a foreign vocabulary. They are
monotone bounds in the MULTIPOLE RANK, and every quantity they bound is already a
function of Λ's own coordinates. If so the index is §16.4 form, it closes, and it
is CONTAINED in Λ rather than adjacent to it.

  γ    multipole rank            1 dipole < 2 quadrupole < 3 octupole
  τ    type                      0 electric < 1 magnetic
  |Δℓ| orbital change            f − ℓ, from Λ's own ℓ and f
  |ΔJ| total angular change      in 2J units, from Λ's own 2S and 2S′
  ΔS   spin change               0 or not, from Λ's own 2S and 2S′

  THE RULES, as bounds:
    |Δℓ| ≤ γ                 monotone in γ            ONE PARENT
    |ΔJ| ≤ 2γ                monotone in γ            ONE PARENT
    parity change = (−1)^γ for Eγ, (−1)^(γ+1) for Mγ  — a CONGRUENCE on γ+τ
    ΔS = 0 in LS coupling                             a cut, not a bound

Committed before computing: the first two are §16.4 form and will close; the
parity rule is a congruence and §12.11.2 lists congruence as an excluded form, so
if the index closes it must be because parity is DETERMINED rather than imposed.
"""
import itertools, sys
from collections import Counter, defaultdict
from zeno import State, step
from method_tower import base

def R(X, d):
    A = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -10**9), c[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in itertools.product(*A)
            if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}
E = lambda X, d: len(R(X, d)) - len(X)

GMAX = 3
def build_free():
    """the EM index on its own coordinates, before Λ is consulted"""
    cells = []
    for g in range(1, GMAX + 1):
        for t in (0, 1):
            for dl in range(0, g + 1):                 # |Δl| <= γ
                for dj in range(0, 2 * g + 1):         # |ΔJ| <= 2γ, in 2J units
                    for ds in (0, 1):                  # ΔS = 0 allowed; ≠0 is the M-type leak
                        # parity: Eγ changes parity by (-1)^γ, Mγ by (-1)^(γ+1).
                        # Δl carries the parity change, so the rule DETERMINES the
                        # admissible Δl parity rather than constraining a free axis.
                        if (dl % 2) != ((g + t) % 2): continue
                        cells.append((g, t, dl, dj, ds))
    return cells

def build_in_lambda():
    """every Λ₉ cell, mapped to its EM coordinates"""
    L8 = base((3, 3, 1, 3, 1))
    L9 = [c + (s,) for c in L8 for s in range(0, c[6] + 1)]
    out, hist = [], Counter()
    for c in L9:
        n, l, k, q, e, f, g_, S2, S2p = c
        dl = abs(f - l); dj = abs(S2p - S2); ds = 0 if S2p == S2 else 1
        # the lowest multipole that can carry it
        gam = max(dl, (dj + 1) // 2, 1)
        if gam > GMAX:
            hist["beyond octupole"] += 1; continue
        tau = (dl - gam) % 2                       # parity fixes the type
        out.append((gam, tau, dl, dj, ds))
        hist[f"γ={gam} {'M' if tau else 'E'}"] += 1
    return out, hist, len(L9)

def run():
    F = build_free(); IN, hist, n9 = build_in_lambda()
    return F, set(IN), hist, n9

with State("em") as st:
    F, INS, hist, n9 = step(st, "build both readings", run, budget=300)

box = GMAX * 2 * (GMAX + 1) * (2 * GMAX + 1) * 2
print(f"  THE FREE INDEX -- the rules on their own coordinates")
print(f"    cells        {len(F)}")
print(f"    ambient box  {box}")
print(f"    density      {100*len(F)/box:.1f}%")
print(f"    |ℛ(X)|       {len(R(F,5))}")
print(f"    E(EM)        {E(F,5)}")

print(f"\n  THE INDEX INSIDE Λ -- every Λ₉ cell mapped to its EM coordinates")
print(f"    Λ₉ cells mapped            {n9:,}")
print(f"    distinct EM cells occupied {len(INS)} of {len(F)} admissible")
print(f"    E over what Λ occupies     {E(list(INS),5)}")
print(f"\n    {'multipole':<18}{'Λ₉ cells':>10}")
for k, v in sorted(hist.items()):
    print(f"    {k:<18}{v:>10,}")

print(f"""
  AND THE DECIDING QUESTION: is the EM index a SUBLATTICE of Λ, or a quotient?
  Every EM coordinate is a function of Λ's coordinates -- Δl of (l,f), ΔJ of
  (2S,2S'), γ and τ of those. A function of the coordinates is not a new axis;
  it is a MAP. So the EM index is the image of Λ₉ under that map, and closure of
  the image is a different statement from closure of Λ.""")
sys.exit(0)
