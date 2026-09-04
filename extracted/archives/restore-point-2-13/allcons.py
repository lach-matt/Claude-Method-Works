#!/usr/bin/env python3
"""allcons.py -- every constraint in the book, indexed.

§21.5.3 indexes Λ's thirteen. This indexes every constraint that DEFINES an index
anywhere in the work — the tower, the drawn objects, the book's own indexes of
itself, and the electromagnetic quotient.

COORDINATES, ordered so ℛ and ℛ₄ both apply
  parents   0 = one parent · 1 = two parents
  form      0 = a plain bound x ≤ y          1 = an affine bound x ≤ ay + b
            2 = a two-sided band |x−y| ≤ c   3 = a congruence or diagonal
  carried   0 = ℛ carries it (E = 0 on its own)      1 = ℛ₄ but not ℛ
            2 = neither operator carries it
  source    0 = physics · 1 = a drawing · 2 = this book's own record

COMMITTED BEFORE COMPUTING (§2.13)
  (a) the index is OPEN — a corpus that acquires constraints from four sources
      will not have covered the space
  (b) 'carried = 2' is rare: almost everything this book indexes is ℛ-carriable,
      which is why the method works at all
  (c) the congruences cluster at carried ≥ 1, since §14.5.5 shows the parity rule
      is exactly the case ℛ misses and ℛ₄ catches
"""
import itertools, sys
from collections import Counter
from zeno import State, step

# (name, where, parents, form, carried, source)
C = [
 # --- Λ's tower, §21.5.3 ---------------------------------------------------
 ("ℓ ≤ n−1",              "Λ₈", 0, 1, 0, 0),
 ("k ≤ 4ℓ+2",             "Λ₈", 0, 1, 0, 0),
 ("q ≤ k",                "Λ₈", 0, 0, 0, 0),
 ("f ≤ e−1",              "Λ₈", 0, 1, 0, 0),
 ("g ≤ 4f+2",             "Λ₈", 1, 1, 0, 0),
 ("g ≤ q",                "Λ₈", 1, 0, 0, 0),
 ("2S ≤ k",               "Λ₉", 0, 0, 0, 0),
 ("2S′ ≤ v ≤ g",          "Λ₁₀",1, 2, 0, 0),
 ("v ≡ g (mod 2)",        "Λ₁₀",0, 3, 1, 0),
 ("2J_c ≤ φ̂(k)",          "Λ₁₁",0, 1, 0, 0),
 ("|2J_c−2f| ≤ 2K",       "Λ₁₂",1, 2, 0, 0),
 ("|2J−2K| ≤ 1",          "Λ₁₃",0, 2, 0, 0),
 # --- the electromagnetic quotient, §12.11.8 -------------------------------
 ("Δℓ = f−ℓ",             "EM", 1, 0, 0, 0),
 ("ΔS = 0, a diagonal",   "EM", 1, 3, 0, 0),
 ("|Δℓ| = 1, parity",     "EM", 1, 3, 1, 0),
 # --- the drawn objects ----------------------------------------------------
 ("period × group",       "the periodic table", 0, 0, 2, 1),
 ("n+ℓ × position",       "Janet",              0, 0, 0, 1),
 ("month × day",          "the calendar",       0, 0, 2, 1),
 ("months by length",     "the calendar, relabelled", 0, 0, 0, 1),
 ("l ≥ w ≥ h",            "a box ordering",     0, 0, 0, 1),
 ("rank × file",          "a chessboard",       0, 0, 0, 1),
 # --- the book's own indexes ----------------------------------------------
 ("object < source < artefact < outside", "the audits",   0, 0, 1, 2),
 ("corroboration ≤ φ̂(repair)",            "the register", 0, 1, 0, 2),
 ("blocks · obstacle · cost · depends",   "Q",            0, 0, 0, 2),
 ("access ≥ referent",                    "the reference index", 0, 0, 0, 2),
 ("entered ≤ access",                     "the bibliography",    0, 0, 0, 2),
 ("trigger · object · failure · earned",  "the protocols", 0, 0, 0, 2),
 ("stage · parents · multiplier",         "the constraints", 0, 0, 1, 2),
]
AX = [["one parent", "two parents"],
      ["a plain bound", "an affine bound", "a two-sided band", "a congruence or diagonal"],
      ["ℛ carries it", "ℛ₄ but not ℛ", "neither operator"],
      ["physics", "a drawing", "this book's own record"]]

def envp(X, i, j, ui, uj):
    m = {}
    for c in X:
        k = c[j]; v = c[i]
        if k not in m: m[k] = [v, v]
        m[k][0] = min(m[k][0], v); m[k][1] = max(m[k][1], v)
    ks = sorted(m); out = {}; run = None
    for t in (ks if uj else list(reversed(ks))):
        v = m[t][1] if ui else m[t][0]
        run = v if run is None else (max(run, v) if ui else min(run, v))
        out[t] = run
    return out

ONE = [(True, True)]
FOUR = [(True, True), (True, False), (False, True), (False, False)]

def clos(X, d, corners):
    X = list(X); A = [sorted({c[i] for c in X}) for i in range(d)]
    cons = [(i, j, a, envp(X, i, j, a, b))
            for i in range(d) for j in range(d) if i != j for (a, b) in corners]
    out = set()
    for x in itertools.product(*A):
        ok = True
        for (i, j, a, e) in cons:
            bd = e.get(x[j])
            if bd is None or (a and x[i] > bd) or ((not a) and x[i] < bd): ok = False; break
        if ok: out.add(x)
    return out

def run():
    X = {c[2:] for c in C}
    box = 1
    for i in range(4): box *= len({c[i] for c in X})
    return X, box, clos(X, 4, ONE), clos(X, 4, FOUR)

with State("allcons") as st:
    X, box, R1, R4 = step(st, "index every constraint", run, budget=300)

print(f"  EVERY CONSTRAINT IN THE BOOK, INDEXED")
print(f"    constraints    {len(C)}   distinct cells {len(X)}   collisions {len(C)-len(X)}")
print(f"    box {box}   density {100*len(X)/box:.0f}%")
print(f"    E  under ℛ     {len(R1)-len(X):>4}")
print(f"    E₄ under ℛ₄    {len(R4)-len(X):>4}   orientation cost {len(R1)-len(R4)}")
print(f"\n  distribution:")
for k, ax in enumerate(AX):
    c = Counter(x[k] for x in [t[2:] for t in C])
    print(f"    {['parents','form','carried','source'][k]:<9}"
          + " · ".join(f"{ax[v]} {c[v]}" for v in sorted(c)))
print(f"\n  admitted by ℛ₄ and absent — constraint shapes the corpus does not have:")
for c in sorted(R4 - X):
    print(f"    {AX[0][c[0]]:<12} {AX[1][c[1]]:<24} {AX[2][c[2]]:<18} {AX[3][c[3]]}")
print(f"\n  the constraints no operator carries:")
for t in C:
    if t[4] == 2: print(f"    {t[0]:<26} in {t[1]}")
