#!/usr/bin/env python3
"""spectra_closure.py -- E on the compendium itself.

Register 785. The question "what prevents closure of the Spectra Compendium" has a
definite answer in this book's own terms: apply the recovery operator to the set of
channels and read E.

The operator, from §6.1 and Appendix A:
    Â_i(X)   = the alphabet of coordinate i — every value it takes in X
    φ̂_ij(v)  = max{ x_i : x ∈ X, x_j ≤ v }  — the monotone upper envelope
    ℛ(X)     = { x ∈ ∏_i Â_i(X) : x_i ≤ φ̂_ij(x_j) ∀ i≠j }
    E(X)     = |ℛ(X)| − |X|

E(X) = 0 means the table is exactly what its own coordinates and envelopes generate:
nothing is missing that the structure implies. E(X) > 0 counts the cells the operator
recovers that the table does not contain — and by the reading of register 553 those
are PREDICTIONS, not defects: channels the structure says should exist.

Coordinates chosen: the ones a channel is actually indexed by.
"""
import re, itertools, sys
from collections import defaultdict
from zeno import State, step

ZNUM = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"Ne":10,"Na":11,
        "Mg":12,"Al":13,"Si":14,"P":15,"Ar":18,"K":19,"Ca":20,"Sc":21,"Ti":22,
        "Zn":30,"Ga":31,"Cd":48,"Ba":56,"Hg":80,"Bi":83}
LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}

def load():
    rows = [l.rstrip("\n").split("\t") for l in open("SPECTRA-DATA.tsv", encoding="utf-8")][1:]
    X = set()
    for r in rows:
        m = re.search(r"n([spdfghik])\b", r[1])
        if not m: continue
        try: z = int(r[9])
        except Exception: continue
        el = re.match(r"([A-Z][a-z]?)", r[0].strip())
        if not el or el.group(1) not in ZNUM: continue
        # (Z, charge, l) — the element, its ionisation stage, and the orbital.
        # The n-RANGE is deliberately excluded: it records how much of a series was
        # measured, not which series it is. Including it made the operator generate
        # every interval and E blew up to 7,892 (register 785).
        X.add((ZNUM[el.group(1)], z, LM[m.group(1)]))
    return X

def R(X):
    d = len(next(iter(X)))
    A = [sorted({x[i] for x in X}) for i in range(d)]
    # the monotone upper envelope on every ordered pair of coordinates
    phi = {}
    for i in range(d):
        for j in range(d):
            if i == j: continue
            f = {}
            for v in A[j]:
                c = [x[i] for x in X if x[j] <= v]
                f[v] = max(c) if c else None
            phi[(i, j)] = f
    out = set()
    for cand in itertools.product(*A):
        ok = True
        for i in range(d):
            for j in range(d):
                if i == j: continue
                b = phi[(i, j)][cand[j]]
                if b is None or cand[i] > b: ok = False; break
            if not ok: break
        if ok: out.add(cand)
    return out

def run():
    X = load()
    Rx = R(X)
    missing = sorted(Rx - X)
    return X, Rx, missing

with State("spectra_closure") as s:
    X, Rx, missing = step(s, "apply the recovery operator to the compendium", run, budget=900)

print(f"  |X|      {len(X):>6}   distinct (Z, charge, l) cells in the compendium")
print(f"  |R(X)|   {len(Rx):>6}")
print(f"  E(X)     {len(Rx)-len(X):>6}")
print()
if not missing:
    print("  E(X) = 0 — the compendium is CLOSED on these coordinates.")
else:
    print(f"  {len(missing)} cells the operator recovers that the table does not hold.")
    print(f"  These are what the structure says should exist and does not.\n")
    INV={v:k for k,v in ZNUM.items()}
    print(f"  {'element':>8}{'charge':>8}{'l':>4}")
    for c in missing[:25]:
        print(f"  {INV.get(c[0],c[0]):>8}{c[1]:>8}{'spdfghik'[c[2]]:>4}")
    if len(missing) > 25: print(f"  ... and {len(missing)-25} more")
