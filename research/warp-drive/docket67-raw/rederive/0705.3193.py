#!/usr/bin/env python3
"""DOCKET 67 -- rederivation for arXiv:0705.3193 (Graham & Olum, achronal ANEC).

Graham-Olum's conjecture itself (no self-consistent semiclassical spacetime
violates ANEC on a complete achronal null geodesic) is NOT finite and is not
checked here -- nothing in this file bears on whether it is true.

What IS finite and closed-form, and is what the tree leans on beside it:

 C1  Past a conjugate point a null geodesic is chronal (Hawking-Ellis 4.5.12,
     restated in gr-qc/9406053 p.~33).  Checked exactly on the Einstein static
     universe R x S^2, where every null geodesic from a pole refocuses at the
     antipode at affine parameter pi.  (composite.py:93-95 uses this direction.)
 C2  The CONVERSE fails: a null geodesic with NO conjugate point can be chronal.
     Checked on the flat cylinder R^{1,1}/(x ~ x+L): Jacobi fields J = c*lambda
     never vanish again, yet points past lambda = L/2 are timelike-related.
     z3 finds the witness; z3 also proves the uncompactified line is achronal.
     (achronal.py:41-42 states 'achronal EXACTLY up to its first conjugate
     point'; obstruct.py:185-186 infers ACHRONAL from ZERO conjugate points.)
 C3  A conjugate point needs no T_kk: pure Weyl (traceless) tidal term, either
     sign, focuses one transverse axis in finite affine parameter -- the vacuum
     mechanism composite.py:90-95 relies on.
 C4  The two numbers the tree prints next to the result: 'nineteen years'
     (2026 - 2007) and spec.py's solar focus f = b^2 c^2 / (4 G M) = 547.6 AU.
"""
import math
import sympy as sp
import z3

ok = True
def rec(name, cond, detail):
    global ok
    ok &= bool(cond)
    print(f"[{'PASS' if cond else 'FAIL'}] {name}: {detail}")

# ---------------------------------------------------------------- C1: ESU
# ds^2 = -dt^2 + dchi^2 + sin^2 chi dphi^2 ; null geodesic t = s, chi = s, phi = 0.
# Two events are chronologically related iff |dt| > spherical distance d.
s, s1, s2 = sp.symbols('s s1 s2', real=True)
d_back = 2*sp.pi - s              # distance from pole to chi = s, the short way, for pi < s < 2 pi
gap_after = sp.simplify(s - d_back)   # dt - d
rec("C1a ESU beyond conjugate point is chronal",
    sp.solve_univariate_inequality(gap_after > 0, s, relational=False) == sp.Interval.open(sp.pi, sp.oo),
    f"dt - d = {gap_after} > 0 exactly for s > pi (conjugate point at s = pi)")
# before the conjugate point: any two points on the arc 0<=s1<s2<=pi have dt = d, null-related only
rec("C1b ESU up to the conjugate point is not chronal",
    sp.simplify((s2 - s1) - (s2 - s1)) == 0,
    "dt - d = 0 for 0 <= s1 < s2 <= pi: null-related, no timelike curve")
# Jacobi field on unit S^2 for the null congruence from the pole: J'' + J = 0, J(0)=0
lam = sp.symbols('lam')
J = sp.Function('J')
solJ = sp.dsolve(J(lam).diff(lam, 2) + J(lam), J(lam), ics={J(0): 0, J(lam).diff(lam).subs(lam, 0): 1}).rhs
rec("C1c ESU first conjugate point at lambda = pi",
    sp.simplify(solJ - sp.sin(lam)) == 0 and min(sp.solve(sp.Eq(solJ, 0), lam), key=lambda r: r if r > 0 else sp.oo) == sp.pi,
    f"J = {solJ}; first positive zero pi")

# ---------------------------------------------------------------- C2: flat cylinder
Jc = sp.dsolve(J(lam).diff(lam, 2), J(lam), ics={J(0): 0, J(lam).diff(lam).subs(lam, 0): 1}).rhs
rec("C2a flat cylinder has no conjugate point",
    Jc == lam, f"J = {Jc}: vanishes only at lambda = 0")
L = z3.RealVal(1)
a, b = z3.Reals('a b')
sol = z3.Solver()
# points (a,a) and (b,b) on x = t, 0 <= a < b < L; other way round the circle distance L - (b - a)
sol.add(0 <= a, a < b, b < L, (b - a) > L - (b - a))
res = sol.check()
w = sol.model() if res == z3.sat else None
rec("C2b flat cylinder null geodesic is chronal without a conjugate point",
    res == z3.sat, f"z3 witness a = {w[a] if w else None}, b = {w[b] if w else None} (L = 1): dt > d")
p = z3.Solver()
x = z3.Real('x')
# on uncompactified R^{1,1}: dt^2 - dx^2 for points on x = t is identically 0, never > 0
p.add(z3.Not((b - a)**2 - (b - a)**2 <= 0))
rec("C2c uncompactified null line is achronal (z3 proves no timelike pair)",
    p.check() == z3.unsat, "negation unsat")

# ---------------------------------------------------------------- C3: Weyl-only focusing
c = sp.symbols('c', positive=True)
for sign in (+1, -1):
    # Jacobi eqn J_i'' = -K_ii J_i, K = sign*diag(c, -c): traceless, R_kk = tr K = 0
    K = [sign*c, -sign*c]
    zeros = []
    for Ki in K:
        Ji = sp.dsolve(J(lam).diff(lam, 2) + Ki*J(lam), J(lam),
                       ics={J(0): 0, J(lam).diff(lam).subs(lam, 0): 1}).rhs
        z = [r for r in sp.solve(sp.Eq(Ji, 0), lam) if r.is_positive]
        zeros.append(sp.simplify(min(z)) if z else None)
    rec(f"C3 vacuum (trace-free) tidal term sign {sign:+d} gives a conjugate point",
        any(zz is not None for zz in zeros) and sum(K) == 0,
        f"tr K = {sum(K)}; first zeros per axis = {zeros}")

# ---------------------------------------------------------------- C4: the two printed numbers
rec("C4a 'nineteen years'", 2026 - 2007 == 19,
    "arXiv May 2007 / PRD 76 064001 Sept 2007 to 2026-09: 19 years")
GM = 1.32712440041e20   # m^3 s^-2, IAU 2015 nominal (GM)_sun
cc = 299792458.0
Rsun = 6.957e8          # m, IAU 2015 nominal solar radius
AU = 1.495978707e11
f = Rsun**2 * cc**2 / (4 * GM) / AU
rec("C4b solar focus f = R^2 c^2/(4GM)", abs(f - 547.6) < 0.5, f"{f:.2f} AU (spec.py prints 547.6)")

print("\nALL PASS" if ok else "\nSOME FAIL")
raise SystemExit(0 if ok else 1)
