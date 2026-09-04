#!/usr/bin/env python3
"""em3.py -- the electromagnetic image of Λ, on what Λ actually supplies.

Λ's coordinates give a source (n, ℓ, k, 2S) and a target (e, f, g, 2S′, v, 2J_c,
2K, 2J). There is NO SOURCE J. So the electromagnetic quantities available are
exactly two:

    Δℓ = f − ℓ        available at Λ₈
    ΔS = 2S′ − 2S     available at Λ₉

|ΔJ| is not available at any level of the tower, which is why the multipole is
determined by Δℓ and parity alone:

    Δℓ = 0 → M1     Δℓ = 1 → E1     Δℓ = 2 → E2     Δℓ = 3 → E3

the lowest multipole whose parity matches. Type alternates with Δℓ, so μ is a
function of |Δℓ| and nothing else.

THE PROBLEM THAT MAKES THIS INTERESTING. Δℓ is a DIFFERENCE, and §18.2 excludes
differences as axes because they are non-monotone in the cell order — that is
exactly why ν = e − δ was refused. So an index on Δℓ should be open, and the
question is whether the multipole ordering repairs it the way Janet's block
order repairs the periodic table.
"""
import itertools, sys
from collections import Counter, defaultdict
from zeno import State, step
from method_tower import base

GMAX = 6
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

def mu_of(dl):
    """the lowest multipole carrying |Δℓ| = dl, as μ = 2(γ−1)+τ"""
    for g in range(max(dl, 1), GMAX + 1):
        for t in (0, 1):
            if (dl % 2) == ((g + t) % 2):
                return 2 * (g - 1) + t
    return None
NAME = lambda m: f"{'M' if m % 2 else 'E'}{m // 2 + 1}"

def cells(caps, coord):
    L8 = base(caps); L9 = [c + (s,) for c in L8 for s in range(0, c[6] + 1)]
    im = Counter()
    for c in L9:
        n, l, k, q, e, f, g_, S2, S2p = c
        dl = abs(f - l); ds = abs(S2p - S2)
        if coord == "raw":            key = (dl, ds)
        elif coord == "mu":           key = (mu_of(dl), ds)
        elif coord == "mu+dS-capped": key = (mu_of(dl), min(ds, 2))
        im[key] += 1
    return im, len(L9)

def run():
    out = {}
    for caps in [(3,3,1,3,1),(3,3,2,3,2),(4,4,2,6,2),(4,4,3,6,3),(5,5,3,10,3)]:
        row = {}
        for coord in ("raw", "mu"):
            im, n = cells(caps, coord); o = set(im)
            row[coord] = (n, len(o), len(R(list(o), 2)), E(list(o), 2), im)
        out[caps] = row
    return out

with State("em3") as st:
    OUT = step(st, "the image at five cap settings", run, budget=300)

print(f"  {'caps':<20}{'Λ₉':>9}   {'coordinate':<14}{'cells':>7}{'|ℛ|':>6}{'E':>5}")
for caps, row in OUT.items():
    for coord in ("raw", "mu"):
        n, nc, nr, e, _ = row[coord]
        lbl = "(|Δℓ|, ΔS)" if coord == "raw" else "(μ, ΔS)"
        print(f"  {str(caps):<20}{n:>9,}   {lbl:<14}{nc:>7}{nr:>6}{e:>5}")
    print()

caps = (3,3,1,3,1)
im = OUT[caps]["mu"][4]; o = set(im)
print(f"  THE IMAGE AT THE BOOK'S CAPS, on (μ, ΔS)")
for c in sorted(o):
    print(f"    {NAME(c[0]):<3} ΔS={c[1]}   {im[c]:>6,} cells")
print(f"    total {sum(im.values()):,}")
gap = sorted(R(list(o), 2) - o)
print(f"\n  ADMITTED AND ABSENT: {len(gap)}")
for c in gap:
    print(f"    {NAME(c[0]):<3} ΔS={c[1]}")
