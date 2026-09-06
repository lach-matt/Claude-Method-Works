#!/usr/bin/env python3
"""The violation index V — does it close itself?

Coordinates: eight law-classes that can break. A profile is a subset of them.
Implications are taken from the retrieved literature only; each is labelled.
"""
import sys
sys.path.insert(0, "/home/claude/method")
from itertools import product, combinations
from zeno import State, step

LAWS = ["T", "H", "L", "U", "N", "C", "E", "D"]
GLOSS = {"T": "chronology (no CTCs)", "H": "global hyperbolicity",
         "L": "linearity of evolution", "U": "unitarity",
         "N": "no-cloning", "C": "no superluminal signalling",
         "E": "null energy condition", "D": "no perfect discrimination"}
IX = {l: i for i, l in enumerate(LAWS)}

# breaking the first forces breaking the second
IMP = [("T", "H", "Friedman+ 1990, Cauchy problem in spacetimes with CTCs"),
       ("T", "L", "Deutsch 1991 / Bacon 2003, globally nonlinear evolution"),
       ("T", "U", "DeJonghe+ 0908.2655, pure -> mixed, unitarity lost"),
       ("T", "N", "Brun+, exact cloning in D-CTC model"),
       ("T", "D", "Brun+ PRL 102.210402, perfect distinguishability"),
       ("T", "E", "chronology violation in 3+1 requires exotic matter"),
       ("D", "N", "perfect discrimination yields cloning"),
       ("N", "C", "cloning yields superluminal signalling"),
       ("L", "C", "Gisin 1990 / Polchinski 1991, nonlinearity signals")]

def close(S):
    S = set(S); grew = True
    while grew:
        grew = False
        for a, b, _ in IMP:
            if a in S and b not in S:
                S.add(b); grew = True
    return frozenset(S)

def vec(S):
    return tuple(1 if l in S else 0 for l in LAWS)

def RR(X, d):
    """the running-maxima envelope closure used by audit 1 (RR in audits.py)"""
    vals = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -99), c[i])
        b, o = -99, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*vals)
            if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}

with State("violations", reset=True) as st:
    allsets = step(st, "enumerate the box", lambda: 2 ** len(LAWS), budget=5)
    closed = step(st, "implication-closed profiles",
                  lambda: sorted({close(c) for r in range(len(LAWS) + 1)
                                  for c in combinations(LAWS, r)}, key=lambda s: (len(s), sorted(s))),
                  budget=30)
    closed = [frozenset(c) for c in closed]
    X = {vec(c) for c in closed}
    print(f"\n  box            2^8 = {allsets}")
    print(f"  closed profiles      {len(X)}")
    print(f"  density              {100*len(X)/allsets:.2f}%")

    # is the family a lattice under union/intersection?
    Sx = set(X)
    jf = sum(1 for a, b in combinations(X, 2)
             if tuple(max(p, q) for p, q in zip(a, b)) not in Sx)
    mf = sum(1 for a, b in combinations(X, 2)
             if tuple(min(p, q) for p, q in zip(a, b)) not in Sx)
    print(f"  join failures        {jf}")
    print(f"  meet failures        {mf}")

    # THE TEST: does the index realise its own closure operator?
    R = RR(X, len(LAWS))
    E = len(R) - len(X)
    print(f"\n  |R(V)|               {len(R)}")
    print(f"  |V|                  {len(X)}")
    print(f"  E(V)                 {E}")

    if E:
        extra = sorted(R - Sx)
        print(f"\n  the {E} cells the envelope admits but the implications forbid:")
        for x in extra[:40]:
            broken = "".join(LAWS[i] for i, v in enumerate(x) if v)
            missing = [f"{a}->{b}" for a, b, _ in IMP
                       if x[IX[a]] and not x[IX[b]]]
            print(f"    {{{broken or '-'}}}   violates: {', '.join(sorted(set(missing)))}")

    # minimal profiles: what is the cheapest admissible break?
    print("\n  minimal non-empty closed profiles (the cheapest addresses):")
    mins = [c for c in closed if c and not any(d < c and d for d in closed)]
    for c in sorted(mins, key=lambda s: (len(s), sorted(s))):
        print(f"    {{{''.join(sorted(c))}}}  = {', '.join(GLOSS[l] for l in sorted(c))}")
