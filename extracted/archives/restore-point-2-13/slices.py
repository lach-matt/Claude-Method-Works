#!/usr/bin/env python3
"""slices.py -- the spectra index in three-axis slices, each read in every language.

Register 1176. Everything so far has read Lambda_spectra whole: E on the entire object,
one number per language. That is a linear reading of a four-coordinate body, and it
cannot see an edge — an edge is where a slice changes character, and a whole-object
number averages every slice together.

A SLICE fixes one coordinate and keeps the other three. Three coordinates is the minimum
for an index (register 1173: at two, pairwise consistency and the cell coincide and every
language agrees for no reason), so a four-coordinate index has exactly four families of
three-axis slice:

    fix Z         → (charge, l, mult)   one element, all its ions
    fix charge    → (Z, l, mult)        one ionisation stage across the table
    fix l         → (Z, charge, mult)   one orbital, every species
    fix mult      → (Z, charge, l)      one term type, every species

Each slice is a genuine index in its own right, and the cypher analysis applies to it
unchanged. What the analysis returns for a slice is what that slice's ALGEBRA is: E in
each language, the agreements, the density. Sweeping the fixed coordinate then traces
how the algebra changes — and where it changes abruptly is an edge.

WHAT WOULD CONFIRM AN EDGE. A slice whose E, agreement pattern or algebraic density
differs sharply from its neighbours in the sweep. WHAT WOULD REFUTE ONE. A smooth sweep,
which would say the index has no internal structure along that axis and the whole-object
reading was adequate.
"""
import itertools, math, json, re, statistics as st
from itertools import product
from collections import defaultdict
from zeno import State, step

P = (1<<61) - 1

# ---------------------------------------------------------------- the operators
def op_order(X, d):
    X = set(X)
    if not X: return set()
    vals = [sorted({c[i] for c in X}) for i in range(d)]
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
    X = set(X)
    if not X: return set()
    vals = [sorted({c[i] for c in X}) for i in range(d)]
    combos = list(itertools.combinations(range(d), order))
    M = set()
    for c in X:
        for idxs in combos: M.add((idxs, tuple(c[i] for i in idxs)))
    return {x for x in product(*vals)
            if all((idxs, tuple(x[i] for i in idxs)) in M for idxs in combos)}

def _uh(pts):
    Q = sorted(set(pts)); H = []
    for p in Q:
        while len(H) >= 2 and (H[-1][1]-H[-2][1])*(p[0]-H[-1][0]) <= (p[1]-H[-1][1])*(H[-1][0]-H[-2][0]):
            H.pop()
        H.append(p)
    return [((y2-y1)/(x2-x1), y1-((y2-y1)/(x2-x1))*x1)
            for (x1,y1),(x2,y2) in zip(H, H[1:]) if x2 != x1]

def op_geometry(X, d):
    X = set(X)
    if not X: return set()
    vals = [sorted({c[i] for c in X}) for i in range(d)]
    HP = {(i,j): _uh([(c[j], c[i]) for c in X]) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*vals)
            if all(x[i] <= a*x[j]+b+1e-9 for (i,j), segs in HP.items() for a, b in segs)}

def _rank_gf(rows, nc, p=P):
    M = [r[:] for r in rows]; r = 0
    for c in range(nc):
        piv = None
        for i in range(r, len(M)):
            if M[i][c] % p: piv = i; break
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], p-2, p); M[r] = [(v*inv) % p for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p:
                f = M[i][c]; M[i] = [(a-f*b) % p for a, b in zip(M[i], M[r])]
        r += 1
        if r == len(M): break
    return r

def op_algebra(X, d, maxmon=260):
    """the ideal's density: rank of the evaluation matrix over the monomials it spans"""
    X = sorted(X)
    if len(X) < 2: return float("nan")
    mons = [()]
    for deg in range(1, 9):
        mons += list(itertools.combinations_with_replacement(range(d), deg))
        if len(mons) > maxmon: break
    rows = []
    for pt in X:
        row = []
        for mm in mons:
            v = 1
            for i in mm: v = (v*pt[i]) % P
            row.append(v)
        rows.append(row)
    return _rank_gf(rows, len(mons))/len(mons)

# ---------------------------------------------------------------- the index
def load():
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
    return H, {v: k for k, v in ZN.items()}

def slice_report(X):
    """the cypher analysis on one slice, which is a three-coordinate index"""
    d = 3
    if len(X) < 4: return None
    amb = 1
    for i in range(d): amb *= len({c[i] for c in X})
    if amb > 60000: return None
    o = op_order(X, d); s = op_statistics(X, d, 2); g = op_geometry(X, d)
    a = op_algebra(X, d)
    return dict(n=len(X), amb=amb, Eo=len(o)-len(X), Es=len(s)-len(X), Eg=len(g)-len(X),
                alg=a, agree=(o == s == g), os=len(o ^ s), og=len(o ^ g))

def run():
    H, INV = load()
    out = {}
    for axis, keep, name in ((0, (1,2,3), "fix Z      → (charge, ℓ, mult)"),
                             (1, (0,2,3), "fix charge → (Z, ℓ, mult)"),
                             (2, (0,1,3), "fix ℓ      → (Z, charge, mult)"),
                             (3, (0,1,2), "fix mult   → (Z, charge, ℓ)")):
        rows = []
        for v in sorted({c[axis] for c in H}):
            S = {tuple(c[i] for i in keep) for c in H if c[axis] == v}
            r = slice_report(S)
            if r: rows.append((v, r))
        out[name] = rows
    return out, INV

with State("slices") as s:
    OUT, INV = step(s, "slice on four axes and read each in every language", run, budget=1500)

print("  THE SPECTRA INDEX IN THREE-AXIS SLICES\n")
print("  Each slice fixes one coordinate and keeps three — the minimum for an index.")
print("  The cypher analysis then applies unchanged, and sweeping the fixed value")
print("  traces how the slice's algebra changes. An abrupt change is an EDGE.\n")
for name, rows in OUT.items():
    if not rows: continue
    print(f"  {name}\n")
    print(f"      {'value':>7}{'cells':>7}{'ambient':>9}{'E ord':>8}{'E stat':>8}"
          f"{'E geom':>8}{'algebra':>9}{'  agree'}")
    for v, r in rows:
        lab = str(v)
        if "fix Z" in name: lab = INV.get(v, str(v))
        if "fix ℓ" in name: lab = "spdfghik"[v]
        print(f"      {lab:>7}{r['n']:>7}{r['amb']:>9,}{r['Eo']:>8,}{r['Es']:>8,}"
              f"{r['Eg']:>8,}{r['alg']:>9.3f}{'  yes' if r['agree'] else '  no':>7}")
    print()
