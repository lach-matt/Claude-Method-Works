#!/usr/bin/env python3
"""rprop.py -- does R itself propagate values, if the defect is a COORDINATE?

Register 1089. The conjecture is that the Method's operator answers the propagation
problem for every index, not just the question of which cells exist.

R is a closure operator on CELLS. It recovers the largest set consistent with the
pairwise monotone envelopes. It says nothing about values — unless a value is made a
coordinate, in which case the envelopes constrain it exactly as they constrain anything
else.

THE EXPERIMENT. Take the spectra index on (Z, charge, l) and add a fourth coordinate:
the defect, discretised into bands. Run R on the 4-tuples. For each (Z, c, l) the set of
delta-bands appearing in R(X) is the operator's own statement about what delta can be.

If that reproduces the hand-written propagation, the propagation was reimplementing R.
If it is TIGHTER, the propagation was losing information. If it is LOOSER, the
propagation was claiming more than the operator licenses — which is what registers 1078
and 1084 found by a different route.

WHY THE DISCRETISATION MATTERS AND IS STATED. R works on a finite product of alphabets,
so delta must be binned. The bin width is a choice and the answer depends on it: too
coarse and every cell admits every band, too fine and R has no envelope to work with.
Three widths are run and reported so the dependence is visible rather than hidden.
"""
import re, itertools, math
from collections import defaultdict, Counter
from zeno import State, step

LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}
ZNUM = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,
        "Mg":12,"Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20,
        "Sc":21,"Ti":22,"Fe":26,"Zn":30,"Ga":31,"Ge":32,"Cd":48,"Ba":56,"Hg":80,"Bi":83}

def measured():
    out = {}
    for line in open("SPECTRA-DATA.tsv", encoding="utf-8").read().split("\n")[1:]:
        r = line.rstrip().split("\t")
        if len(r) < 11: continue
        m = re.search(r"n([spdfghik])\b", r[1])
        el = re.match(r"([A-Z][a-z]?)", r[0].strip())
        if not (m and el) or el.group(1) not in ZNUM: continue
        try:
            k = (ZNUM[el.group(1)], int(r[9]), LM[m.group(1)])
            out.setdefault(k, []).append(float(r[7]))
        except Exception: pass
    import statistics as st
    return {k: st.mean(v) for k, v in out.items()}

def RR(S, d):
    """the book's operator: the largest set consistent with every pairwise envelope"""
    S = set(S)
    if not S: return S
    A = [sorted({c[i] for c in S}) for i in range(d)]
    phi = {}
    for i in range(d):
        for j in range(d):
            if i == j: continue
            phi[(i,j)] = {}
            for v in A[j]:
                cand = [c[i] for c in S if c[j] <= v]
                phi[(i,j)][v] = max(cand) if cand else None
    return {c for c in itertools.product(*A)
            if all(phi[(i,j)][c[j]] is not None and c[i] <= phi[(i,j)][c[j]]
                   for i in range(d) for j in range(d) if i != j)}

def run():
    H = measured()
    res = []
    for width in (0.05, 0.10, 0.25):
        # delta is binned; the l coordinate is REVERSED so that all four coordinates
        # run the same way (delta falls as l rises, so -l rises with delta)
        X = {(Z, c, 7-l, int(round(d/width))) for (Z,c,l), d in H.items()}
        R = RR(X, 4)
        # for each (Z,c,l) in R, what band range does the operator admit?
        adm = defaultdict(list)
        for Z,c,ml,b in R: adm[(Z,c,7-ml)].append(b*width)
        widths = [max(v)-min(v) for v in adm.values() if len(v) > 1]
        exact  = sum(1 for v in adm.values() if len(v) == 1)
        res.append((width, len(X), len(R), len(adm), exact, widths))
    return res

with State("rprop") as s:
    res = step(s, "run R with the defect as a fourth coordinate", run, budget=1200)

import statistics as st
print("  R WITH THE DEFECT AS A COORDINATE\n")
print("  If the operator itself propagates values, the delta-bands it admits at each")
print("  (Z, charge, l) ARE the bound — computed by R, not by hand.\n")
print(f"  {'bin width':>10}{'|X|':>7}{'|R(X)|':>9}{'cells reached':>15}"
      f"{'pinned to one band':>20}{'median span':>13}")
for w, nx, nr, ncell, exact, widths in res:
    med = st.median(widths) if widths else 0.0
    print(f"  {w:>10.2f}{nx:>7}{nr:>9}{ncell:>15}{exact:>20}{med:>13.3f}")
print()
print("  'cells reached' counts (Z, charge, l) triples appearing anywhere in R(X).")
print("  The compendium holds 282 measured cells and its hand-written propagation")
print("  reaches 84 more with a two-sided bound.")
