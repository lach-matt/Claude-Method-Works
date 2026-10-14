#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation of Kuo & Ford gr-qc/9304008 v1, eqs (3.40)-(3.45), Casimir section III.C.
Independent of research/warp-drive/fluctuation.py (nothing imported from the tree).

KF v1 text layer (d67/src/casmag/all/gr-qc_9304008v1.txt, md5 f1a6628604751cf61b2a4bd411b00153, lines 2015-2160):
  (3.40) <:T00^2:>_C = <:T00:>_C^2 + (1/2)[<:phidot^2:>^2 + <:(phi_x)^2:>^2 + <:(phi_y)^2:>^2 + <:(phi_z)^2:>^2]
  (3.41) <:phidot^2:>_C^2 = (1/2)(rho + p1 + p2 + p3)^2
  (3.42) <:(phi_x)^2:>_C^2 = (1/2)(rho + p1 - p2 - p3)^2
  (3.43) Delta' = (<:T00^2:> - rho^2)/rho^2 = (1/8)[(rho+xi1+xi2+xi3)^2 + (rho+xi1-xi2-xi3)^2
                                                   + (rho-xi1+xi2-xi3)^2 + (rho-xi1-xi2+xi3)^2],  xi_i = p_i/rho
  (3.45) Delta' >= 1/2, Delta >= 1/3; periodic z: xi = (-1,-1,3), Delta' = 6, Delta = 6/7.
Tree's claim (fluctuation.py:47-48, 150, 456-459): (3.41),(3.42) print 1/2 where 1/4 holds; the 1/8 of (3.43)
is right, so the 1/2 is typographical.
"""
import itertools, sys
import sympy as sp

ok = True
def chk(name, got, want):
    global ok
    good = (got == want)
    ok &= good
    print(("PASS " if good else "FAIL ") + name + "   got=" + str(got) + "  want=" + str(want))

# ---------------------------------------------------------------- 1. operator identities, minimal coupling
# T_mn = d_m phi d_n phi - (1/2) eta_mn (d phi)^2, checked in BOTH signature conventions (physical rho, p_i).
d0, d1, d2, d3 = sp.symbols('d0 d1 d2 d3', real=True)
d = [d0, d1, d2, d3]
for sig, eta in (("(-,+,+,+)", sp.diag(-1, 1, 1, 1)), ("(+,-,-,-)", sp.diag(1, -1, -1, -1))):
    dphi2 = sum(eta[m, m] * d[m]**2 for m in range(4))       # eta^{mn} d_m d_n (eta diagonal, self-inverse)
    T = lambda m, n: d[m] * d[n] - sp.Rational(1, 2) * eta[m, n] * dphi2
    rho = T(0, 0)
    p = [T(i, i) for i in (1, 2, 3)]                         # p_i = T_ii (lower spatial indices, both signs agree)
    chk("identity %s: phidot^2 = (rho+p1+p2+p3)/2" % sig, sp.expand(d0**2 - (rho + sum(p)) / 2), 0)
    chk("identity %s: phi_x^2 = (rho+p1-p2-p3)/2" % sig, sp.expand(d1**2 - (rho + p[0] - p[1] - p[2]) / 2), 0)
    chk("identity %s: T00 = (1/2) sum_A d_A^2" % sig, sp.expand(rho - sum(x**2 for x in d) / 2), 0)
# Normal ordering is linear, so the same identities hold for <:...:> in ANY state (minimal coupling).
# Hence <:phidot^2:>^2 = (1/4)(rho+sum p)^2 EXACTLY -- the coefficient is 1/4.

# ---------------------------------------------------------------- 2. Casimir image sum, periodic z, from scratch
t, x, y, z, tp, xp, yp, zp = sp.symbols('t x y z tp xp yp zp', real=True)
L = sp.symbols('L', positive=True)
n = sp.symbols('n', integer=True, nonzero=True)
X, XP = [t, x, y, z], [tp, xp, yp, zp]
sigma_n = -(t - tp)**2 + (x - xp)**2 + (y - yp)**2 + (z - zp + n * L)**2   # KF (3.30)-(3.31)
Gn = 1 / (4 * sp.pi**2 * sigma_n)                                              # KF (3.29)
coinc = {tp: t, xp: x, yp: y, zp: z}
Gmat = sp.zeros(4, 4)
for A in range(4):
    for B in range(4):
        term = sp.simplify(sp.diff(Gn, X[A], XP[B]).subs(coinc))              # <:d_A phi d_B phi:> term n
        # sum over n != 0 of c/n^4: term is c(L)/n^4 exactly -> 2 zeta(4) c
        c = sp.simplify(term * n**4)
        assert not c.has(n), (A, B, c)
        Gmat[A, B] = sp.simplify(2 * sp.zeta(4) * c)
print("G_AB = <:d_A phi d_B phi:>_C =", Gmat)
chk("Casimir G off-diagonal zero", all(Gmat[A, B] == 0 for A in range(4) for B in range(4) if A != B), True)
rhoC = sp.simplify(sum(Gmat[A, A] for A in range(4)) / 2)
# p_i = G_ii + (G00 - sum_j G_jj)/2 (from T_ii = d_i^2 + (phidot^2 - |grad|^2)/2)
pC = [sp.simplify(Gmat[i, i] + (Gmat[0, 0] - sum(Gmat[j, j] for j in (1, 2, 3))) / 2) for i in (1, 2, 3)]
chk("KF (3.33) rho = -pi^2/(90 L^4)", sp.simplify(rhoC + sp.pi**2 / (90 * L**4)), 0)
xi = [sp.simplify(pi_ / rhoC) for pi_ in pC]
chk("KF (3.32) xi = (-1,-1,3)", xi, [-1, -1, 3])

# ---------------------------------------------------------------- 3. (3.41)/(3.42) with 1/2 vs 1/4
s41 = rhoC + sum(pC)
s42 = rhoC + pC[0] - pC[1] - pC[2]
chk("(3.41) printed 1/2 holds on the Casimir G", sp.simplify(Gmat[0, 0]**2 - s41**2 / 2) == 0, False)
chk("(3.41) with 1/4 holds on the Casimir G", sp.simplify(Gmat[0, 0]**2 - s41**2 / 4), 0)
chk("(3.42) printed 1/2 holds on the Casimir G", sp.simplify(Gmat[1, 1]**2 - s42**2 / 2) == 0, False)
chk("(3.42) with 1/4 holds on the Casimir G", sp.simplify(Gmat[1, 1]**2 - s42**2 / 4), 0)
print("   ratio printed/true for (3.41):", sp.simplify((s41**2 / 2) / Gmat[0, 0]**2))

# ---------------------------------------------------------------- 4. (3.40) Wick coefficient, Isserlis, general 4x4
g = sp.Matrix(4, 4, lambda a, b: sp.Symbol('g%d%d' % (min(a, b), max(a, b))))
def isserlis4(a, b, c, e):
    return g[a, b] * g[c, e] + g[a, c] * g[b, e] + g[a, e] * g[b, c]
T00sq = sum(sp.Rational(1, 4) * isserlis4(A, A, B, B) for A in range(4) for B in range(4))
rho_g = sum(g[A, A] for A in range(4)) / 2
chk("(3.40) <:T00^2:> = rho^2 + (1/2) sum_AB G_AB^2 (zero-mean quasifree)",
    sp.expand(T00sq - rho_g**2 - sp.Rational(1, 2) * sum(g[A, B]**2 for A in range(4) for B in range(4))), 0)
chk("  and it reduces to KF's diagonal-only (3.40) when G is diagonal (Casimir periodic: yes, see 2)",
    all(Gmat[A, B] == 0 for A in range(4) for B in range(4) if A != B), True)

# ---------------------------------------------------------------- 5. propagation: which coefficient does (3.43) carry?
cc = sp.symbols('c', positive=True)
x1, x2, x3 = sp.symbols('xi1 xi2 xi3', real=True)
signs = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
quad = sum((1 + s1 * x1 + s2 * x2 + s3 * x3)**2 for s1, s2, s3 in signs)
# (3.40) with <:(d_A phi)^2:>^2 = c (...)^2  ->  Delta' = (1/2) c sum (...)^2 / rho^2 = (c/2) quad
coef343 = cc / 2
chk("(3.43) coefficient implied by c=1/4", coef343.subs(cc, sp.Rational(1, 4)), sp.Rational(1, 8))
chk("(3.43) coefficient implied by printed c=1/2", coef343.subs(cc, sp.Rational(1, 2)), sp.Rational(1, 4))
chk("so the printed 1/8 is the c=1/4 value", sp.solve(sp.Eq(coef343, sp.Rational(1, 8)), cc), [sp.Rational(1, 4)])
chk("Hadamard sum: quad = 4(1+|xi|^2)", sp.expand(quad - 4 * (1 + x1**2 + x2**2 + x3**2)), 0)
Dp = sp.Rational(1, 8) * quad
chk("Delta'(xi=0) = 1/2  [KF min]", Dp.subs({x1: 0, x2: 0, x3: 0}), sp.Rational(1, 2))
chk("Delta'(-1,-1,3) = 6  [KF]", Dp.subs({x1: -1, x2: -1, x3: 3}), 6)
chk("Delta = 6/7  [KF (3.44)]", sp.Rational(6) / 7, sp.Rational(6, 1) / (1 + 6))
DpWrong = sp.Rational(1, 4) * quad
print("   with the printed 1/2 carried through: min Delta' =", DpWrong.subs({x1: 0, x2: 0, x3: 0}),
      ", periodic Delta' =", DpWrong.subs({x1: -1, x2: -1, x3: 3}), "(KF print 1/2 and 6: not what 1/2 gives)")
chk("printed 1/2 carried through contradicts KF's own 1/2 and 6",
    (DpWrong.subs({x1: 0, x2: 0, x3: 0}), DpWrong.subs({x1: -1, x2: -1, x3: 3})) != (sp.Rational(1, 2), 6), True)
# Direct Delta' from the image-sum G, Wick:
DpDirect = sp.simplify(sp.Rational(1, 2) * sum(Gmat[A, B]**2 for A in range(4) for B in range(4)) / rhoC**2)
chk("Delta' from image-sum G + Wick = 6 (independent of (3.41)-(3.43))", DpDirect, 6)

# ---------------------------------------------------------------- 6. (3.43)'s leading 'rho' (a separate item)
r = sp.symbols('r', positive=True)
quad_rho = sum((r + s1 * x1 + s2 * x2 + s3 * x3)**2 for s1, s2, s3 in signs)
lit = sp.Rational(1, 8) * quad_rho
chk("(3.43) as printed (leading rho) equals the true Delta' identically", sp.expand(lit - Dp) == 0, False)
chk("  ... it does only at rho = 1 (units-dependent), so the printed leading rho must read 1",
    sp.expand((lit - Dp).subs(r, 1)), 0)

# ---------------------------------------------------------------- 7. z3: min of (1/8)quad is 1/2, unique at xi=0
try:
    import z3
    a, b, c3 = z3.Reals('a b c')
    q = sum((1 + s1 * a + s2 * b + s3 * c3)**2 for s1, s2, s3 in signs) / 8
    s = z3.Solver(); s.add(q < z3.RealVal('1/2'))
    chk("z3: no xi with Delta' < 1/2", str(s.check()), "unsat")
    s = z3.Solver(); s.add(q == z3.RealVal('1/2'), z3.Or(a != 0, b != 0, c3 != 0))
    chk("z3: Delta' = 1/2 only at xi = 0", str(s.check()), "unsat")
    s = z3.Solver(); s.add(q < z3.RealVal('3/4'))
    chk("VACUITY GUARD: a stronger bound (Delta' >= 3/4) is refuted", str(s.check()), "sat")
except ImportError:
    print("z3 not installed; sympy check in 5 already proves min via quad = 4(1+|xi|^2)")

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
