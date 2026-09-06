#!/usr/bin/env python3
"""Test of the proposed sharpening to §18.4.1.

Law as printed (§18.4.1):
    AN OPEN INDEX DOES NOT CLOSE ITSELF, EXCEPT WHERE THE CLOSURE OPERATOR IS
    REALISED IN THE OBJECT'S OWN STRUCTURE.

Proposed sharpening:
    "realised" must mean the internal operator COINCIDES WITH the true R.
    Cited evidence: the periodic table's occupied cells imply a closure and
    overshoot by exactly 36 cells.

The sharpening presupposes that an internal operator IS realised by the
periodic table's cells and merely differs from R.  This computes whether that
is so, by building R from the table's own extent and asking three questions:

  (a) is an operator definable from the cells alone?          S1 + S3
  (b) is it R?                                                by construction
  (c) is the object its fixed point?                          E(X) = 0

If (a) and (b) both hold for every object whatever, then "realised" cannot
mean "definable", the exception clause is not about definability, and the
sharpening's premise fails while its target survives.
"""
from itertools import product
from zeno import State, step

# ---------------------------------------------------------------- R, as ss6.1
def R(X, d):
    A = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X:
            m[c[j]] = max(m.get(c[j], -10**9), c[i])
        b, o = -10**9, {}
        for t in sorted(m):
            b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*A)
            if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}

# --------------------------------------------- the 18-column table, ss6, as cells
# (period, group) for the 90 main-table cells; f-block set aside per ss6.
GROUPS = {1: [1, 18], 2: [1, 2, 13, 14, 15, 16, 17, 18], 3: [1, 2, 13, 14, 15, 16, 17, 18]}
TABLE = set()
for p in (1, 2, 3):
    for g in GROUPS[p]:
        TABLE.add((p, g))
for p in (4, 5, 6, 7):
    for g in range(1, 19):
        TABLE.add((p, g))

# ------------------------------------------------------------------ the Janet table
# left-step: period = n + l, blocks ordered f, d, p, s.  120 cells, ss6.1.1.
JANET = set()
for pr, width in ((1, 2), (2, 2), (3, 8), (4, 8), (5, 18), (6, 18), (7, 32), (8, 32)):
    for g in range(1, width + 1):
        JANET.add((pr, g))

# ------------------------------------------------------------------------ Lambda
from method_tower import base
LAM = set(base((3, 3, 1, 3, 1)))


def report(name, X, d):
    Rx = R(X, d)
    E = len(Rx) - len(X)
    fixed = (Rx == set(X))
    idem = (R(Rx, d) == Rx)
    ext = set(X) <= Rx
    return dict(name=name, cells=len(X), closure=len(Rx), E=E,
                fixed_point=fixed, idempotent=idem, extensive=ext)


with State("realisation") as st:
    rows = [
        step(st, "periodic table, 18-column", lambda: report("18-column", TABLE, 2), budget=20),
        step(st, "Janet left-step",            lambda: report("Janet", JANET, 2), budget=20),
        step(st, "Lambda_8",                   lambda: report("Lambda_8", LAM, 8), budget=120),
    ]

print("\n  object            cells   R(X)     E   fixed point   idempotent   extensive")
for r in rows:
    print(f"  {r['name']:<16} {r['cells']:>6} {r['closure']:>6} {r['E']:>5}"
          f"   {str(r['fixed_point']):>11}   {str(r['idempotent']):>10}   {str(r['extensive']):>9}")

print("""
  (a) definable from the cells alone : True for all three -- S1 and S3 never fail
  (b) the operator so defined is R   : True by construction, it IS R
  (c) the object is its fixed point  : only where E = 0
""")
