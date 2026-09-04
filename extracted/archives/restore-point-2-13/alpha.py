#!/usr/bin/env python3
"""alpha.py -- Lambda_alpha, the polarisability index.

Register 1165. The spectra index's constraint graph becomes a TREE when alpha_d is
carried as a species LABEL rather than as an edge between charge and delta_2 — and a
label must come from outside the thing it labels, which is why extracting alpha from the
same channels it then predicts left four testable points.

What alpha needs is not a table. A table has no coordinates, admits nothing, and cannot
say what it does not hold. Every other object in this book is an index, and alpha should
be one.

THE COORDINATES. alpha_d is the dipole polarisability of a CORE — an ion with Ne_core
electrons and nuclear charge Z. So the index is over cores, and the natural coordinates
are the ones that set a core's radial extent:

    Z            the nuclear charge
    Ne_core      the core's electron count
    n_out        the principal quantum number of its outermost occupied subshell
    l_out        that subshell's orbital angular momentum

n_out and l_out are DERIVED from Ne_core by aufbau, and by register 1143 a derived
coordinate earns its place only if its production is non-monotone. Both are: they cycle
with the shells. So all four are admitted and the test below measures what that buys.

THE VALUES. Three sources, graded as the spectra index grades its own:

    MEASURED     extracted from a high-l channel via Seaton, delta_0 = 3 alpha z^2 / K(l)
    PUBLISHED    from the literature, when a search finds one
    BOUNDED      alpha falls with charge along an isoelectronic sequence and rises with
                 Ne down a group; both are monotone and give one-sided bounds

E(Lambda_alpha) = |R(X)| - |X| is then the same quantity it is everywhere else, and it
says what the polarisability index admits and does not hold.
"""
import json, math, re, statistics as st
from itertools import product
from collections import defaultdict
from zeno import State, step

ORDER = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
         (4,3),(5,2),(6,1),(7,0)]
ZN = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,"Mg":12,
      "Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20,"Sc":21,"Ti":22,
      "Fe":26,"Zn":30,"Ga":31,"Ge":32,"Cd":48,"Ba":56,"Hg":80,"Bi":83}
INV = {v: k for k, v in ZN.items()}
ROM = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"IX":9,"XI":11,"XV":15,"XVI":16}
LM  = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}
RM  = {v: k for k, v in ROM.items()}

def config(ne):
    left, out = ne, []
    for n, l in ORDER:
        if left <= 0: break
        cap = 2*(2*l+1); occ = min(left, cap); out.append((n,l,occ)); left -= occ
    return out

def outer(ne):
    c = config(ne)
    return (c[-1][0], c[-1][1]) if c else (0, 0)

def kf(l): return l*(l+1)*(2*l-1)*(2*l+1)*(2*l+3)

# PUBLISHED values found by search during this session. Each carries its source; a value
# without one is not admitted, however plausible.
PUB = {
    (19,1): (5.49,  "K+ core, Peper et al. arXiv:1907.02776"),
    (11,1): (1.0015,"Na+ core, Freeman & Kleppner 1976"),
}

def measured_alpha():
    """alpha from every species holding a high-l channel, via Seaton's delta_0"""
    out = {}
    for nm, orb, term, Zc, d0, d2, r0, r1, n in json.load(open("RITZ.json")):
        if orb not in LM or LM[orb] < 4: continue
        if d0 <= 1e-4 or d0 >= 0.3: continue
        p = nm.split(); el = p[0]
        if el not in ZN: continue
        c = ROM.get(p[-1], 1) if len(p) > 1 else 1
        a = d0*kf(LM[orb])/(3.0*c*c)
        k = (ZN[el], c)
        if k not in out or r1 < out[k][1]: out[k] = (a, r1, LM[orb])
    return {k: v[0] for k, v in out.items()}

def RR(X, d):
    X = set(X)
    vals = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -99), c[i])
        b, o = -99, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i,j): env(i,j) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*vals)
            if all(x[i] <= phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i != j)}

def run():
    M = measured_alpha()
    held = {}
    for (Z, c), a in M.items():
        ne = Z - c            # the CORE's electron count
        n_out, l_out = outer(ne)
        held[(Z, ne, n_out, l_out)] = (a, "measured")
    for (Z, c), (a, src) in PUB.items():
        ne = Z - c
        n_out, l_out = outer(ne)
        held[(Z, ne, n_out, l_out)] = (a, "published")
    return M, held

with State("alpha") as s:
    M, held = step(s, "build the polarisability index", run, budget=600)

print("  Λ_α — THE POLARISABILITY INDEX\n")
print("  coordinates:  Z · Nₑ(core) · n_out · ℓ_out")
print("  the last two derived from Nₑ by aufbau, and both non-monotone in it,")
print("  so both earn a coordinate by register 1143.\n")
print(f"  {'core':<14}{'Z':>4}{'Nₑ':>5}{'n':>4}{'ℓ':>3}{'α (a₀³)':>11}{'  source'}")
for k, (a, src) in sorted(held.items(), key=lambda x: x[0][0]):
    Z, ne, n, l = k
    c = Z - ne
    print(f"  {INV.get(Z,Z)+' '+RM.get(c,str(c)):<14}{Z:>4}{ne:>5}{n:>4}{'spdfg'[l]:>3}"
          f"{a:>11.3f}  {src}")
print(f"\n  {len(held)} cores held\n")

X = set(held)
R = RR(X, 4)
print(f"  |X| = {len(X)}   |ℛ(X)| = {len(R)}   E(Λ_α) = {len(R)-len(X)}")
print(f"      {'CLOSED' if len(R)==len(X) else 'the operator admits '+str(len(R)-len(X))+' cores it does not hold'}")
