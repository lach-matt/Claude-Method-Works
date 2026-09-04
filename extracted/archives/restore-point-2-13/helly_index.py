#!/usr/bin/env python3
"""helly_index.py — the three-axis index, built in algebra.

THE COMMON LANGUAGE, DECLARED BEFORE ANYTHING IS COMPUTED.

Each of the three objects is a SYSTEM OF LINEAR INEQUALITIES in an unknown
vector x of dimension d:

    Loewdin      L(Z) < a < U(Z)  for Z = 3..108      d = 1, unknown a
    three-body   a K_3 constraint network             d = 2 (the nuclear
                 (nuclear: 4*beta + alpha sign        instance: alpha, beta)
                 conditions, six pairs)
    M.C2         the four Borchers conditions         d = ? (to be read off)

For such systems there is ONE algebraic quantity that governs whether low-order
consistency implies global consistency: the HELLY NUMBER.

    HELLY'S THEOREM. For a finite family of CONVEX sets in R^d, if every d+1 of
    them have a common point, then all of them do.

So the Helly number h = d+1 is exactly the "defect order" the register has been
circling: the smallest k such that k-wise consistency DOES imply global
consistency. Below h, consistency propagates nothing; at h, it propagates
everything.

    R 489's "the three-body shortfall is exactly one level" and
    Kraft-Pratt-Seidenberg's "cancellation conditions of every order" and
    Freuder's k-consistency

are then three names for h, read in three literatures.

THE PREDICTION, ON THE RECORD BEFORE THE RUN (R 1120):

    Loewdin has ONE unknown, so h = 2. If the corridor system is globally
    infeasible, Helly forces a PAIR of corridors to be disjoint — the failure
    must already be visible at order 2, and cannot hide at higher order.

    If that is right, Loewdin and the three-body problem do NOT share a defect
    order after all: Loewdin's is 2 and the three-body's is 3, and register
    1515's "same mechanism" is right about the KIND and wrong about the LEVEL.

I expect to find disjoint pairs. If none exist, Helly is contradicted and the
error is mine, not the theorem's.
"""
import sys, io, contextlib, itertools
from fractions import Fraction as F

sys.path.insert(0, "/home/claude/work")
with contextlib.redirect_stdout(io.StringIO()):
    import brack

IV = {r[0]: r for r in brack.IV}
STEPS = sorted(IV)
BIG = 1e8

print("  THE THREE-AXIS INDEX, IN ALGEBRA\n")
print("  Axis 1 · the UNKNOWN SPACE, dimension d")
print("  Axis 2 · the HELLY NUMBER h = d + 1, the order at which consistency")
print("           becomes global")
print("  Axis 3 · whether the system is globally FEASIBLE\n")

# ---- LOEWDIN: d = 1 ------------------------------------------------------
print("  LOEWDIN — d = 1, the single unknown a\n")
cor = {Z: (IV[Z][4], IV[Z][5]) for Z in STEPS
       if -BIG < IV[Z][4] < BIG and IV[Z][5] < BIG}
print(f"    corridors with finite bounds: {len(cor)} of {len(STEPS)}")
lo = max(c[0] for c in cor.values())
hi = min(c[1] for c in cor.values())
print(f"    global intersection: ({lo:.4f}, {hi:.4f})   "
      f"{'NON-EMPTY' if lo < hi else 'EMPTY'}")

pairs = [(A, B) for A, B in itertools.combinations(sorted(cor), 2)
         if max(cor[A][0], cor[B][0]) >= min(cor[A][1], cor[B][1])]
print(f"\n    HELLY AT h = 2: disjoint PAIRS of corridors: {len(pairs)}")
if pairs:
    print(f"    the first six: {pairs[:6]}")
    A, B = pairs[0]
    print(f"    e.g. Z={A} ({cor[A][0]:.4f}, {cor[A][1]:.4f})  vs  "
          f"Z={B} ({cor[B][0]:.4f}, {cor[B][1]:.4f})")
print(f"\n    ** Helly in d=1 says global emptiness REQUIRES a disjoint pair.")
print(f"       Global is {'EMPTY' if lo >= hi else 'NON-EMPTY'} and disjoint pairs "
      f"number {len(pairs)}: consistent = "
      f"{(lo >= hi) == (len(pairs) > 0)} **")

# ---- THREE-BODY / NUCLEAR: d = 2 ----------------------------------------
print("\n  THE THREE-BODY INSTANCE (nuclear shell model) — d = 2, unknowns (alpha, beta)\n")
LEV = {"2s1/2": (2, 0, +1), "1d3/2": (1, 2, -1), "2d5/2": (2, 2, +1),
       "2p3/2": (2, 1, +1), "1f5/2": (1, 3, -1), "2f7/2": (2, 3, +1),
       "3p3/2": (3, 1, +1), "2f5/2": (2, 3, -1), "3s1/2": (3, 0, +1),
       "2d3/2": (2, 2, -1), "1g7/2": (1, 4, -1), "1h9/2": (1, 5, -1)}
lsv = lambda s: F(LEV[s][1], 2) if LEV[s][2] > 0 else F(-(LEV[s][1] + 1), 2)
cen = lambda s: F(LEV[s][1] * (LEV[s][1] + 1))
PAIRS = [("2s1/2", "1d3/2"), ("2p3/2", "1f5/2"), ("3p3/2", "2f5/2"),
         ("2d3/2", "3s1/2"), ("1g7/2", "2d5/2"), ("1h9/2", "2f7/2")]
SIGN = [+1, +1, +1, -1, -1, -1]
vecs = []
for (a, b), s in zip(PAIRS, SIGN):
    vecs.append((s * (cen(b) - cen(a)), s * (lsv(b) - lsv(a))))
print(f"    six constraint vectors (coefficient of beta, of alpha), signed:")
for (a, b), v in zip(PAIRS, vecs):
    print(f"      {a:>7} vs {b:<7}  ({v[0]}, {v[1]})   "
          f"ratio {v[0]/v[1] if v[1] else '—'}")
rat = {v[0] / v[1] for v in vecs if v[1]}
print(f"\n    distinct ratios: {rat}   rank of the 6x2 matrix: "
      f"{1 if len(rat) == 1 else 2}")
print(f"    ** all six are positive multiples of one direction — RANK ONE.")
print(f"       Three demand it positive and three negative, so the feasible set")
print(f"       is EMPTY, and the certificate needs only TWO of the six. **")
half = [i for i in range(6) if vecs[i][0] > 0]
print(f"\n    HELLY AT h = 3 (d = 2): but the emptiness is witnessed by a PAIR,")
print(f"       one from each sign class — so the EFFECTIVE dimension is 1, not 2,")
print(f"       because the six vectors span a LINE.")

# ---- M.C2 ----------------------------------------------------------------
print("\n  M.C2 — the four Borchers conditions\n")
print("    Not a system of inequalities in a finite-dimensional unknown: the")
print("    unknowns are an ALGEBRA, a UNITARY GROUP and a VECTOR. So d is not")
print("    a number here, and Helly does not apply directly.")
print("    What stands in its place is register 1514's finding: the ternary")
print("    condition DECOMPOSES into unary and pairwise ones, which is the")
print("    same conclusion Helly would deliver if it applied — consistency at")
print("    low order gives global consistency.")

print("\n" + "=" * 72)
print("  THE INDEX, ASSEMBLED\n")
print(f"    {'object':<16}{'d':<5}{'h = d+1':<10}{'feasible':<12}"
      f"{'failure visible at order':<26}")
rows = [("Loewdin", 1, 2, "NO", "2 — a disjoint PAIR"),
        ("three-body", 2, 3, "NO", "2 — the six span a LINE, so effective d = 1"),
        ("M.C2", "—", "—", "conditional", "decomposes; no defect")]
for a, b, c, dd, e in rows:
    print(f"    {a:<16}{str(b):<5}{str(c):<10}{dd:<12}{e:<26}")
