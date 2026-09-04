#!/usr/bin/env python3
"""cypher_audit.py -- the languages, run and compared, not asserted.

Register 1173. The comparison analysis found that the language cypher had never been
tested outside Lambda. A first attempt to test it failed because I implemented geometry
and information as `return x in R` — the order operator under two other names — and
reported three pairs holding when I had compared one operator with itself.

This runs the operators that exist and states plainly which do not.

THE CORRECTED STRUCTURE (register 1173). Logic is not a language. It is the mechanism by
which any language answers a binary question about a cell:

    LEVEL 0   binary       a cell is admitted or it is not
    LEVEL 1   a language   a coordinate system with a closure operator
    LEVEL 2   logic        binary -> (language) -> binary

A language earns its row when logic can operate on it and get a binary back. That is why
documentary has no row in the operator table: it returns a citation, not a binary.

THE OPERATORS

    order        R, the envelope closure. HAVE IT.
    statistics   max-entropy on the PAIRWISE marginals, reached by IPF. HAVE IT.
                 A cell is admitted iff every pair of its coordinates co-occurs in X.
                 First-order marginals are NOT the book's operator: on Lambda they admit
                 all 6,912 cells where the pairwise ones admit exactly 976.
    geometry     the monotone polyhedron. MISSING — needs vertex enumeration.
    algebra      the ideal and its Groebner basis. MISSING — needs Buchberger.
    information  description length, E_bits. PARTIAL — A.ebits exists for Lambda only.

WHAT A DISAGREEMENT MEANS. By P21 a property true in one language is true in all. So two
operators differing on one index is a fault in one of them, and the audit names the pair
without adjudicating — register 1171's discipline, because picking a winner is what
produced five failed corrections in a single session.
"""
import itertools, math
from itertools import product
from collections import defaultdict
from zeno import State, step

# ---------------------------------------------------------------- the operators
def op_order(X, d):
    """ORDER: R(X) = { x : x_i <= phi_ij(x_j) for all i != j }"""
    X = set(X); vals = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -10**9), c[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i,j): env(i,j) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*vals)
            if all(x[i] <= phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i != j)}

def op_statistics(X, d, order=2):
    """STATISTICS: the max-entropy closure on the marginals of the given order.

    IPF converges to the unique max-entropy distribution matching the marginals
    (Deming & Stephan 1940; Ireland & Kullback 1968; Csiszar 1975). Its support is
    every cell all of whose marginals are non-zero, which is what is computed here —
    the support, not the distribution, because the closure is a SET question.
    """
    X = set(X); vals = [sorted({c[i] for c in X}) for i in range(d)]
    combos = list(itertools.combinations(range(d), order))
    M = set()
    for c in X:
        for idxs in combos: M.add((idxs, tuple(c[i] for i in idxs)))
    return {x for x in product(*vals)
            if all((idxs, tuple(x[i] for i in idxs)) in M for idxs in combos)}

OPERATORS = [("order",      op_order,      True),
             ("statistics", op_statistics, True),
             ("geometry",   None,          False),
             ("algebra",    None,          False),
             ("information",None,          False),
             ("documentary",None,          False)]

# ---------------------------------------------------------------- the indexes
def indexes():
    out = {}
    from method_tower import base
    out["Λ"] = (set(base((3,3,1,3,1))), 8)
    out["the periodic table"] = ({(p,g) for p in range(1,8) for g in range(1,19)
                                  if not (p==1 and 2<=g<=17)}, 2)
    D = [31,29,31,30,31,30,31,31,30,31,30,31]
    out["the calendar"] = ({(m+1,d+1) for m in range(12) for d in range(D[m])}, 2)
    out["a box ordering"] = ({(a,b,c) for a in range(1,6) for b in range(1,6)
                              for c in range(1,6) if a>=b>=c}, 3)
    # the spectra index, as captured
    import re, statistics as st
    ZN = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,
          "Mg":12,"Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20,
          "Sc":21,"Ti":22,"Fe":26,"Zn":30,"Ga":31,"Ge":32,"Cd":48,"Ba":56,"Hg":80,"Bi":83}
    LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}
    SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹","0123456789")
    H = set()
    for line in open("SPECTRA-DATA.tsv", encoding="utf-8").read().split("\n")[1:]:
        r = line.rstrip().split("\t")
        if len(r) < 11: continue
        m = re.search(r"n([spdfghik])\b", r[1]); el = re.match(r"([A-Z][a-z]?)", r[0].strip())
        if not (m and el) or el.group(1) not in ZN: continue
        mu = re.search(r"(\d)[SPDFG]", r[1][m.end():].translate(SUP))
        try: H.add((ZN[el.group(1)], int(r[9]), LM[m.group(1)], int(mu.group(1)) if mu else 0))
        except Exception: pass
    out["Λ_spectra (measured)"] = (H, 4)
    return out

def run():
    IX = indexes()
    res = {}
    for nm, (X, d) in IX.items():
        amb = 1
        for i in range(d): amb *= len({c[i] for c in X})
        if amb > 400000: res[nm] = None; continue
        r = {}
        for lang, f, have in OPERATORS:
            if not have: continue
            r[lang] = f(X, d)
        res[nm] = (X, d, amb, r)
    return IX, res

with State("cypher_audit") as s:
    IX, RES = step(s, "run every operator on every index", run, budget=1500)

print("  THE CYPHER AUDIT\n")
print("      LEVEL 0  binary      a cell is admitted or it is not")
print("      LEVEL 1  a language  a coordinate system with a closure operator")
print("      LEVEL 2  logic       binary → (language) → binary\n")
print("  OPERATORS AVAILABLE\n")
for lang, f, have in OPERATORS:
    note = {"geometry":"needs vertex enumeration of the monotone polyhedron",
            "algebra":"needs Buchberger, or sympy.groebner",
            "information":"A.ebits exists for Λ only; needs extending",
            "documentary":"has no algorithm — returns a citation, not a binary"}.get(lang,"")
    print(f"      {lang:<14}{'RUNS' if have else 'MISSING':<9}{note}")
print()
print("  E BY LANGUAGE\n")
print(f"  {'index':<24}{'|X|':>7}{'ambient':>10}" + "".join(
      f"{l[:6]:>12}" for l,_,h in OPERATORS if h))
for nm, v in RES.items():
    if v is None:
        print(f"  {nm:<24}{'':>7}{'too large':>10}"); continue
    X, d, amb, r = v
    row = "".join(f"{len(r[l])-len(X):>12,}" for l,_,h in OPERATORS if h)
    print(f"  {nm:<24}{len(X):>7,}{amb:>10,}{row}")
print()
print("  AGREEMENT — cell by cell, between every pair that runs\n")
avail = [l for l,_,h in OPERATORS if h]
print(f"  {'index':<24}{'pair':<24}{'differ':>9}{'verdict':>10}")
bad = 0
for nm, v in RES.items():
    if v is None: continue
    X, d, amb, r = v
    for a, b in itertools.combinations(avail, 2):
        diff = len(r[a] ^ r[b])
        if diff: bad += 1
        print(f"  {nm:<24}{a+' / '+b:<24}{diff:>9,}{('AGREE' if not diff else 'DIFFER'):>10}")
print()
print(f"  {len(avail)} operators · {len([v for v in RES.values() if v])} indexes"
      f" · {bad} disagreements")
print()
print("  A disagreement is a fault in ONE of the two readings, and this audit does")
print("  not say which. Register 1171: naming the pair is the finding.")
