#!/usr/bin/env python3
"""corner_sudoku.py — are a(y) and b(y) a sudoku, and does that mean search?

REGISTER 1484 named the unknowns: on a null hypersurface the residual freedom is
l -> a(y) l, acting on the affine parameter as u -> u/a(y) + b(y). Two functions
on the (d-2)-dimensional cut, doubled across the two corners.

THE QUESTION. The person's reading is that these sit in two constraint families
at once — affine and transverse — which is the sudoku shape rather than a sum. If
so, the closure operator is the wrong instrument, because sudoku_index.py showed
a sudoku has E = maximal and redundancy 0: nothing propagates, and search is
required.

SPACE, DECLARED BEFORE THE RUN (R 1383 q2, and the fault this session already
committed once in anec_null.py). The admissible set is discretisations of (a, b)
on a cut of N points, with a > 0 and b real, under exactly the constraints the
register records and NO others:

    C1  a(y) > 0 everywhere          l is future-directed; a rescaling, not a flip
    C2  the group law                composing two rescalings composes their a
                                     multiplicatively and their b affinely
    C3  Theta = 0 is INVARIANT       R 1020: theta_ab -> a(y) theta_ab, so the
                                     non-expansion condition places NO constraint
                                     on a(y) at all
    C4  cut-to-cut identification    R 1021: Theta = 0 identifies cuts
                                     ISOMETRICALLY, which constrains the map
                                     between cuts and NOT the scaling along them

WHAT WOULD REFUTE THE SUDOKU READING. If the constraints decouple — if a(y) at
one point is unconstrained by a(y') at another — then this is not a sudoku but a
product, and there is nothing to search. That is the honest null and it is
checked first.
"""
import itertools

print("  THE CONSTRAINTS THE REGISTER ACTUALLY RECORDS, AS A SYSTEM\n")
rows = [
    ("C1", "a(y) > 0", "an open half-line at each point", "POINTWISE"),
    ("C2", "group law under composition", "closure of the rescaling group", "POINTWISE"),
    ("C3", "Theta = 0", "INVARIANT under a(y) — R 1020", "NO CONSTRAINT"),
    ("C4", "cuts identified isometrically", "a map BETWEEN cuts — R 1021", "NOT ON a(y)"),
]
print(f"    {'':4}{'constraint':<34}{'what it is':<40}acts on a(y) how")
for a, b, c, d in rows:
    print(f"    {a:<4}{b:<34}{c:<40}{d}")

print("\n  THE NULL, CHECKED FIRST: DO THE CONSTRAINTS COUPLE POINTS OF THE CUT?\n")
print("    C1 is a condition at each y separately.")
print("    C2 is a condition on the group, satisfied by any positive a(y).")
print("    C3 places no condition on a(y) at all — that is register 1020's result.")
print("    C4 conditions the identification BETWEEN cuts, not a(y) along one.\n")
print("    ** NOT ONE OF THE FOUR RELATES a(y) TO a(y'). **\n")
print("    So on the constraints the register holds, the system DECOUPLES")
print("    completely across the cut. It is a PRODUCT of open half-lines,")
print("    one per point — not a sudoku, and not a constraint network at all.\n")

print("  WHAT THAT MEANS, STATED PLAINLY\n")
for l in [
 "The sudoku reading is REFUTED on the present constraints — not because the",
 "shape is wrong in principle, but because there are no cross-point constraints",
 "for it to be a shape OF. A sudoku's difficulty is that rows, columns and boxes",
 "each tie distant cells together. Here nothing ties y to y'.",
 "",
 "And that is the same result as R 1020 read at the level of the whole cut",
 "rather than at a point: non-expansion does not merely fail to fix a(y) HERE,",
 "it fails to relate a(y) to a(y') ANYWHERE. The freedom is not underdetermined",
 "by one parameter — it is underdetermined by a whole function's worth.",
 "",
 "So M.C2 does not need SEARCH. It needs a CONSTRAINT — one additional relation",
 "coupling the cut to itself — and the register has been describing its absence",
 "for four hundred entries without naming it as an absence of coupling.",
]:
    print(f"    {l}")

print("\n  AND THAT IS A DIFFERENT QUEUE ITEM FROM THE ONE WE HAD.\n")
print("    was : is M.C2 sudoku-shaped, needing search rather than propagation?")
print("    is  : WHAT COUPLES a(y) TO a(y')? Nothing in the NEH definition does.")
print("          Candidates the register already holds, none yet tested:")
print("            · the corner modes' own doubling across the two corners")
print("            · the crossed-product structure C&F use to recover HSMI")
print("            · a global condition — completeness, maximality, the bracket")
