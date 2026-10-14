#!/usr/bin/env python3
r"""
DOCKET 67 -- re-derivation of Kuo & Ford, gr-qc/9304008 v1, Eqs. (3.40)-(3.45):
    Delta' >= 1/2, Delta >= 1/3 (Casimir-vacuum fluctuations), and the periodic-z
    values Delta' = 6, Delta = 6/7 (xi = (-1,-1,3)).
Independent of research/warp-drive/fluctuation.py (nothing imported from the tree).

Checks
  A  Wick/Isserlis: <:T00^2:> = rho^2 + (1/2) sum_AB G_AB^2 for a zero-mean quasifree
     state, G_AB = <:d_A phi d_B phi:>, massless minimally coupled, flat.  KF's (3.40)
     second line keeps only the DIAGONAL squares.
  B  (3.41)/(3.42) in terms of rho, p_i  (coefficient 1/4 vs printed 1/2), and (3.43):
     with '1' in place of the printed 'rho' inside the brackets, (3.43) is exact;
     read literally (rho inside) it is not.
  C  sum over the 4 sign patterns of (1 + s.xi)^2 = 4 (1 + |xi|^2)  =>  Delta' = (1+|xi|^2)/2,
     minimum 1/2 at xi = 0; Delta = Delta'/(1+Delta') monotone  =>  Delta >= 1/3.
  D  Casimir periodic z, image sum: G diagonal, rho = -pi^2/(90 L^4), xi = (-1,-1,3),
     Delta' = 6, Delta = 6/7.
  E  z3: 4 sum G_AB^2 >= (tr G)^2 for EVERY real symmetric 4x4 G (no PSD, no diagonality);
     vacuity guard: 3 sum G^2 >= (tr G)^2 is refuted.  The diagonal-only (3.40) is not an
     identity when G has off-diagonal entries (counterexample), but the bound holds a fortiori.
  F  hypothesis-necessity guard: with mass m > 0 (T00 gains m^2 phi^2/2) the floor is NOT 1/2.
  G  the |.| in KF (3.2) is inert on this class (numerator = (1/2) sum G^2 >= 0).
Exit 0 and 'ALL CHECKS PASS' iff every check agrees with the source as recorded.
"""
import sys
import itertools
import sympy as sp
import z3

fails = []


def chk(label, ok):
    print("  [%s] %s" % ("ok" if ok else "XX", label))
    if not ok:
        fails.append(label)


# ---------------------------------------------------------------- A  Wick
G = sp.Matrix(4, 4, lambda i, j: sp.Symbol('g%d%d' % (min(i, j), max(i, j))))


def isserlis4(a, b, c, d):
    return G[a, b] * G[c, d] + G[a, c] * G[b, d] + G[a, d] * G[b, c]


# T00 = (1/2) sum_A (d_A phi)^2 (massless minimal coupling, flat); normal-ordered moments of a
# zero-mean quasifree state factorise over pairings of <:d_A phi d_B phi:> = G_AB.
T2 = sp.Rational(1, 4) * sum(isserlis4(A, A, B, B) for A in range(4) for B in range(4))
rho = sp.Rational(1, 2) * G.trace()
closed = rho**2 + sp.Rational(1, 2) * sum(G[A, B]**2 for A in range(4) for B in range(4))
chk("A1 <:T00^2:> = rho^2 + (1/2) sum_AB G_AB^2 (general symmetric G)", sp.expand(T2 - closed) == 0)
kf340 = rho**2 + sp.Rational(1, 2) * sum(G[A, A]**2 for A in range(4))
offdiag = sp.expand(T2 - kf340)
chk("A2 KF (3.40) second line = diagonal part; remainder = (1/2) sum_{A!=B} G_AB^2 >= 0",
    sp.expand(offdiag - sp.Rational(1, 2) * sum(G[A, B]**2 for A in range(4) for B in range(4) if A != B)) == 0)

# ---------------------------------------------------------------- B  (3.41)-(3.43)
r, p1, p2, p3 = sp.symbols('rho p1 p2 p3')
g0, g1, g2, g3 = sp.symbols('G0 G1 G2 G3')        # diagonal G
# minimal coupling: T_ij = d_i phi d_j phi - (1/2) eta_ij (d phi)^2, (d phi)^2 = -G0 + G1+G2+G3
sq = -g0 + g1 + g2 + g3
eqs = [sp.Eq(r, (g0 + g1 + g2 + g3) / 2),
       sp.Eq(p1, g1 - sq / 2), sp.Eq(p2, g2 - sq / 2), sp.Eq(p3, g3 - sq / 2)]
sol = sp.solve(eqs, [g0, g1, g2, g3], dict=True)[0]
chk("B1 <:phidot^2:> = (rho+p1+p2+p3)/2, so its square has 1/4 (KF (3.41) prints 1/2)",
    sp.simplify(sol[g0] - (r + p1 + p2 + p3) / 2) == 0)
chk("B2 <:phi_x^2:> = (rho+p1-p2-p3)/2, square 1/4 (KF (3.42) prints 1/2)",
    sp.simplify(sol[g1] - (r + p1 - p2 - p3) / 2) == 0)
Dp = sp.simplify((sp.Rational(1, 2) * sum(sol[x]**2 for x in (g0, g1, g2, g3))) / r**2)
x1, x2, x3 = sp.symbols('xi1 xi2 xi3')
Dp_xi = sp.simplify(Dp.subs({p1: x1 * r, p2: x2 * r, p3: x3 * r}))
signs = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
kf343_one = sp.Rational(1, 8) * sum((1 + a * x1 + b * x2 + c * x3)**2 for a, b, c in signs)
kf343_lit = sp.Rational(1, 8) * sum((r + a * x1 + b * x2 + c * x3)**2 for a, b, c in signs)
chk("B3 (3.43) with '1' for the printed 'rho' in the brackets is EXACT", sp.simplify(Dp_xi - kf343_one) == 0)
chk("B4 (3.43) read literally (rho inside the brackets) is NOT an identity",
    sp.simplify(Dp_xi - kf343_lit) != 0)
chk("B5   ... and literal (3.43) at xi=0 is rho^2/2, not the 1/2 KF state as its minimum",
    sp.simplify(kf343_lit.subs({x1: 0, x2: 0, x3: 0}) - r**2 / 2) == 0)
chk("B6 the 1/8 of (3.43) is consistent with 1/4 in (3.41)-(3.42), not 1/2",
    sp.simplify(sp.Rational(1, 2) * sp.Rational(1, 4) * 4 - sp.Rational(1, 8) * 4) == 0)

# ---------------------------------------------------------------- C  the minimum
S = sp.expand(sum((1 + a * x1 + b * x2 + c * x3)**2 for a, b, c in signs))
chk("C1 sum_4 (1 + s.xi)^2 = 4 (1 + |xi|^2)  (Hadamard sign patterns)",
    sp.expand(S - 4 * (1 + x1**2 + x2**2 + x3**2)) == 0)
chk("C2 Delta' = (1+|xi|^2)/2 >= 1/2, equality iff xi = 0",
    sp.simplify(kf343_one - (1 + x1**2 + x2**2 + x3**2) / 2) == 0)
d = sp.Symbol('d', positive=True)
f = d / (1 + d)
chk("C3 Delta = Delta'/(1+Delta') strictly increasing, value 1/3 at Delta' = 1/2",
    sp.simplify(sp.diff(f, d) - 1 / (1 + d)**2) == 0 and f.subs(d, sp.Rational(1, 2)) == sp.Rational(1, 3))
D_ = sp.Symbol('D')
chk("C4 (3.44) inverse pair consistent: D/(1-D) and D'/(1+D') invert",
    sp.simplify((D_ / (1 - D_)) / (1 + D_ / (1 - D_)) - D_) == 0)

# ---------------------------------------------------------------- D  Casimir, periodic z
L = sp.Symbol('L', positive=True)
n = sp.Symbol('n', integer=True, positive=True)
t, xx, yy, zz, tp, xp, yp, zp = sp.symbols('t x y z tp xp yp zp', real=True)
X, XP = (t, xx, yy, zz), (tp, xp, yp, zp)
Gc = sp.zeros(4, 4)
for sgn in (1, -1):                    # images n and -n, n >= 1 (n = 0 is the Minkowski term)
    sig = -(t - tp)**2 + (xx - xp)**2 + (yy - yp)**2 + (zz - zp + sgn * n * L)**2
    Gn = 1 / (4 * sp.pi**2 * sig)      # KF (3.29)
    for A in range(4):
        for B in range(4):
            e = sp.diff(Gn, X[A], XP[B])
            e = e.subs({tp: t, xp: xx, yp: yy, zp: zz})
            e = sp.simplify(e)
            Gc[A, B] += sp.summation(e, (n, 1, sp.oo))
Gc = Gc.applyfunc(sp.simplify)
chk("D1 Casimir G_AB = <:d_A phi d_B phi:> is diagonal", all(Gc[A, B] == 0 for A in range(4) for B in range(4) if A != B))
rc = sp.simplify(Gc.trace() / 2)
chk("D2 rho = -pi^2/(90 L^4)  [KF (3.33)]", sp.simplify(rc + sp.pi**2 / (90 * L**4)) == 0)
sqc = -Gc[0, 0] + Gc[1, 1] + Gc[2, 2] + Gc[3, 3]
pc = [sp.simplify(Gc[i, i] - sqc / 2) for i in (1, 2, 3)]
xic = [sp.simplify(p / rc) for p in pc]
chk("D3 xi = (-1, -1, 3)  [KF (3.32) diag[1,-1,-1,3]]", xic == [-1, -1, 3])
Dpc = sp.simplify(sp.Rational(1, 2) * sum(Gc[A, B]**2 for A in range(4) for B in range(4)) / rc**2)
chk("D4 Delta' = 6 (from G directly)", Dpc == 6)
chk("D5 Delta' = 6 (from (3.43) with xi)", kf343_one.subs({x1: -1, x2: -1, x3: 3}) == 6)
chk("D6 Delta = 6/7", sp.simplify(Dpc / (1 + Dpc)) == sp.Rational(6, 7))

# ---------------------------------------------------------------- E  z3, no diagonality
g = {(A, B): z3.Real('g%d%d' % (min(A, B), max(A, B))) for A in range(4) for B in range(4)}
tr = sum(g[A, A] for A in range(4))
ss = sum(g[A, B] * g[A, B] for A in range(4) for B in range(4))


def proved(hyps, goal):
    s = z3.Solver()
    s.add(*hyps)
    s.add(z3.Not(goal))
    return s.check() == z3.unsat


chk("E1 z3: 4 sum_AB G_AB^2 >= (tr G)^2 for every real symmetric G (=> Delta' >= 1/2 when rho != 0)",
    proved([], 4 * ss >= tr * tr))
chk("E2 z3: equality forces G = (tr/4) I", proved([4 * ss == tr * tr],
    z3.And([g[A, B] == (tr / 4 if A == B else 0) for A in range(4) for B in range(A, 4)])))
guard = z3.Solver()
guard.add(z3.Not(3 * ss >= tr * tr))
chk("E3 VACUITY GUARD: the stronger 3 sum G^2 >= (tr G)^2 is refuted (sat)", guard.check() == z3.sat)
cex = z3.Solver()
dsum = sum(g[A, A] * g[A, A] for A in range(4))
cex.add(ss != dsum)
chk("E4 z3: a G with off-diagonal entries exists, so KF's diagonal-only (3.40) is not general",
    cex.check() == z3.sat)
chk("E5 z3: but the diagonal part alone already obeys 4 sum G_AA^2 >= (tr G)^2 (bound holds a fortiori)",
    proved([], 4 * dsum >= tr * tr))

# ---------------------------------------------------------------- F  masslessness is load-bearing
h = [z3.Real('h%d' % i) for i in range(5)]     # diagonal 5x5 incl. m^2 <:phi^2:> slot, rho = tr/2
trh = sum(h)
ssh = sum(v * v for v in h)
s5 = z3.Solver()
s5.add(z3.Not(4 * ssh >= trh * trh))
chk("F1 massive (5 slots): 1/2 is NOT a floor (z3 sat for a violation)", s5.check() == z3.sat)
chk("F2 massive: the floor is Delta' >= 2/5 (5 sum >= tr^2 proved)", proved([], 5 * ssh >= trh * trh))

# ---------------------------------------------------------------- G  |.| in (3.2)
chk("G1 numerator <:T00^2:> - rho^2 = (1/2) sum G^2 is a sum of squares (|.| inert)",
    sp.expand(T2 - rho**2 - sp.Rational(1, 2) * sum(G[A, B]**2 for A in range(4) for B in range(4))) == 0)

print()
if fails:
    print("FAILED: %d -> %s" % (len(fails), fails))
    sys.exit(1)
print("ALL CHECKS PASS")
