#!/usr/bin/env python3
"""diff_quotient.py — does Diff(S) reduce a(y) from a function to a class?

REGISTER 1487 found the coupling: diff(S) is the one non-ultralocal factor of the
extended corner symmetry algebra, and Diff(S) x SL(2,R)^S carries a(y) to
a(phi(y)). The inference to test is that the physical content of a(y) is its
DIFFEOMORPHISM CLASS rather than the function, which would correct R 1485's
"underdetermined by a whole function's worth" downward.

SPACE, DECLARED BEFORE THE RUN. The corner S is a compact surface; take S^1 as
the tractable case and a(y) a smooth positive function on it. The group acting is
Diff(S^1), and the question is what invariants of a survive the action

        (phi . a)(y) = a(phi^{-1}(y)).

A quantity is PHYSICAL iff it is Diff-invariant. The test is: enumerate the
invariants, and ask whether they determine a up to the action. Nothing here is
chosen after seeing an answer -- the invariants are the standard ones for a
scalar under diffeomorphism.

AND THE HONEST NULL, CHECKED FIRST. If a is a SCALAR, the orbit of a generic a
under Diff(S^1) is large and the quotient is small -- which is the hoped-for
reduction. But if a is a DENSITY or carries a weight, the transformation law
picks up a Jacobian and the invariants differ. THE WEIGHT MATTERS AND IS NOT
MINE TO CHOOSE: a(y) came from l -> a(y) l, a rescaling of a vector field, so
its weight must be read off that, not assumed.
"""
import math

print("  STEP 0 · WHAT WEIGHT DOES a(y) CARRY? Read off, not assumed.\n")
print("    a(y) enters as  ℓ → a(y) ℓ  — a rescaling of the null generator.")
print("    ℓ is a VECTOR FIELD along the generators, transverse to the cut.")
print("    Under a diffeomorphism φ of the CUT, the point y moves but ℓ's")
print("    direction is not tangent to the cut, so a is carried as a SCALAR:")
print("        (φ · a)(y) = a(φ⁻¹(y))")
print("    No Jacobian, because a is a ratio of two vectors in the SAME")
print("    transverse direction, and that ratio is diffeomorphism-independent.")
print("    ** a IS A SCALAR. That is the branch we are on. **\n")

print("  STEP 1 · THE INVARIANTS OF A SCALAR UNDER Diff(S¹)\n")
for l in [
 "For a smooth function a on a compact 1-manifold, the complete invariants",
 "of the Diff-action are the LEVEL-SET STRUCTURE: the ordered list of",
 "critical values and the topology of the level sets between them — the",
 "REEB GRAPH of a. Two Morse functions on S¹ are Diff-related iff their",
 "Reeb graphs agree with matching critical values.",
 "",
 "So the quotient is NOT a point, and it is NOT a function space either.",
 "It is a finite tree decorated with real numbers.",
]:
    print(f"      {l}")

print("\n  STEP 2 · HOW MUCH FREEDOM IS THAT? Count it against the alternatives.\n")
rows = [
 ("an arbitrary positive function a(y)", "infinite-dimensional", "R 1485's reading"),
 ("a smooth positive function", "infinite-dimensional", "R 1486's gain"),
 ("modulo Diff(S¹), a with k critical points",
  "k real numbers + a finite tree", "FINITE-DIMENSIONAL per stratum"),
 ("modulo Diff(S¹), a monotone or constant", "1 or 2 real numbers", "the generic low strata"),
]
print(f"    {'object':<44}{'freedom':<34}note")
for a, b, c in rows:
    print(f"    {a:<44}{b:<34}{c}")

print("\n  ** SO THE REDUCTION IS REAL AND IT IS LARGE: from an infinite-dimensional")
print("     function space to a FINITE-DIMENSIONAL space on each stratum, indexed")
print("     by the number of critical points. R 1485 was too pessimistic. **\n")

print("  STEP 3 · BUT CHECK WHAT IT DOES NOT DO, BEFORE CLAIMING ANYTHING.\n")
for l in [
 "It does not make a(y) UNIQUE. The quotient is finite-dimensional, not a",
 "point: a constant a is one real number and remains unfixed, which is",
 "exactly R 1022's 'canonical scaling of the affine parameter' still",
 "missing. The reduction takes the problem from a function's worth of",
 "freedom to a NUMBER's worth — it does not remove it.",
 "",
 "And it holds only if Diff(S) is a GAUGE symmetry of the corner data. If",
 "the diffeomorphisms are PHYSICAL — carrying non-vanishing Noether charge,",
 "which is precisely what the corner literature says makes them corner",
 "symmetries at all — then one must NOT quotient by them, and a(y) keeps",
 "its full freedom.",
 "",
 "THAT IS THE FORK, AND IT IS NOT MINE TO DECIDE HERE: gauge or physical.",
 "The corner literature's whole point is that these become PHYSICAL at a",
 "corner. If so, this reduction is not available and R 1485 stands.",
]:
    print(f"      {l}")
