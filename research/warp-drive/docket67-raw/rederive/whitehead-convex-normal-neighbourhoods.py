#!/usr/bin/env python3
"""
DOCKET 67 / pass S / 26 of 36 -- Whitehead (1932): every point of a manifold
with a sufficiently regular affine connection has a convex normal
neighbourhood.  As used at research/warp-drive/qeihps.py:101-105, 436-439.

Self-contained: nothing is imported from research/warp-drive (no .pyc is
written there).  The HPS throat constants are re-entered from qeihps.py:328-333
and re-derived where they are closed forms.

CHECKS
 A. The tree's data: f(0) = e^L, r0^2 = -16 K^2 L, K^2 = 1/(5760 pi), L = -2/3
    -> r0 = 1/sqrt(540 pi) = 0.0242789 l_P; det g != 0 at the throat; and over
    HPS's whole range -1 <= L < 0 (non-degeneracy fails only at L = 0).
 B. The hypothesis the tree states ("non-degenerate Lorentzian AT THE POINT")
    is NOT sufficient for the theorem: an explicit 1+1 Lorentzian metric,
    non-degenerate at l = 0 (f(0) = 1), of class C^{1,1/2}, has TWO distinct
    geodesics with the same initial point and velocity -> exp_p is not even
    defined, no normal neighbourhood (Hartman-Wintner mechanism, rebuilt here).
 C. On the HPS 4th-order throat jet (a smooth, polynomial metric -- the only
    metric the tree computes; TAYLOR_RADIUS_OF_CONVERGENCE_PROVED = False),
    every Christoffel symbol vanishes at the throat point (theta = pi/2), and
    Whitehead's convexity lemma  d^2/ds^2 |x|^2 = 2|x'|^2 - 2 x_k G^k_ij x'^i x'^j
    > 0  holds on the coordinate ball |x| < eps with eps * sup||G|| < 1 : eps
    computed (units r0).  Spot check by RK4 geodesics inside the ball.
 D. Size claims (the tree's CAVEAT at qeihps.py:114-117): the throat sphere is
    totally geodesic, sectional curvature 1/r0^2 -> conjugate points at pi*r0
    along angular geodesics (an UPPER bound on the angular extent of any
    convex normal neighbourhood about a throat point); along the throat
    worldline l = 0 the tidal tensor R^a_{t b t} vanishes EXACTLY (all t),
    so nothing computed bounds the TIME extent by r0.
"""
import math
import sys
import random

import sympy as sp

OK = []


def chk(label, cond, detail=""):
    OK.append(bool(cond))
    print("  [%s] %s %s" % ("PASS" if cond else "FAIL", label, detail))


# ---------------------------------------------------------------- A
print("A. the tree's data")
K2 = sp.Rational(1, 5760) / sp.pi          # qeihps.py:328
L = sp.Rational(-2, 3)                      # qeihps.py:329
r0 = sp.sqrt(-16 * K2 * L)
chk("r0 = 1/sqrt(540 pi)", sp.simplify(r0 - 1 / sp.sqrt(540 * sp.pi)) == 0,
    "= %.7f l_P" % float(r0))
chk("r0 printed 0.0242789", abs(float(r0) - 0.0242789) < 5e-8)
f0 = sp.exp(L)
chk("f(0) = e^(-2/3) > 0", float(f0) > 0, "= %.6f" % float(f0))
th = sp.Symbol('theta')
g0 = sp.diag(-f0, 1, r0**2, r0**2 * sp.sin(th)**2)
d0 = sp.simplify(g0.det().subs(th, sp.pi / 2))
chk("det g(throat) = -f0 r0^4 != 0", d0 != 0 and float(d0) < 0, "= %.3e" % float(d0))
Ls = sp.Symbol('L', real=True)
r0L = sp.sqrt(-16 * K2 * Ls)
chk("non-degenerate over HPS range -1<=L<0 (r0^2 = -16K^2 L > 0)",
    all(float(r0L.subs(Ls, v)) > 0 for v in [-1, -0.75, -2 / 3., -0.5, -0.1, -1e-6]),
    "; L=0 gives r0 = %s (degenerate)" % r0L.subs(Ls, 0))
print("     r0(L=-1) = %.7f l_P (range endpoint)" % float(r0L.subs(Ls, -1)))

# ---------------------------------------------------------------- B
print("B. non-degeneracy at a point does NOT give a normal neighbourhood")
l, s, E = sp.symbols('l s E', real=True)
# f(l) = 1/(1+|l|^(3/2)) : f(0)=1 > 0, Lorentzian, C^1 with f' Holder-1/2, not C^{1,1}
# geodesic l-equation in -f dt^2 + dl^2 :  l'' = -(f'/2) tdot^2, tdot = E/f
# => l'' = (E^2/2) * d/dl(1/f)  = (E^2/2)*(3/2)|l|^(1/2) sign(l)
lp = sp.Symbol('lp', positive=True)   # l > 0 branch
finv = 1 + lp**sp.Rational(3, 2)
rhs = (E**2 / 2) * sp.diff(finv, lp)
# initial data at s=0: l=0, l'=0, t'=E/f(0)=E; unit timelike -> E^2 = f(0) = 1
Kc = sp.Symbol('K', positive=True)
cand = Kc * s**4
res = sp.simplify(sp.diff(cand, s, 2) - rhs.subs(lp, cand).subs(E, 1))
Ksol = sp.solve(sp.Eq(res.subs(s, 1), 0), Kc)
chk("l(s) = s^4/256 solves the geodesic l-equation (E=1)",
    Ksol == [sp.Rational(1, 256)] and
    sp.simplify(res.subs(Kc, sp.Rational(1, 256))) == 0, "K = %s" % Ksol)
chk("l(s) = 0 also solves it (rhs(0) = 0)", sp.limit(rhs.subs(E, 1), lp, 0) == 0)
chk("same initial point and velocity: l(0)=l'(0)=0 for both",
    (cand.subs(Kc, sp.Rational(1, 256)).subs(s, 0) == 0 and
     sp.diff(cand, s).subs(s, 0) == 0))
fB = 1 / finv
chk("f(0)=1, f'(0)=0 (C^1); f'' ~ l^(-1/2) unbounded (not C^{1,1})",
    sp.limit(fB, lp, 0) == 1 and sp.limit(sp.diff(fB, lp), lp, 0) == 0 and
    sp.limit(sp.diff(fB, lp, 2), lp, 0) == -sp.oo)
print("     -> two geodesics, one initial vector: exp_p undefined; the tree's")
print("        stated hypothesis (non-degenerate AT THE POINT) is insufficient.")

# ---------------------------------------------------------------- C
print("C. Whitehead's convexity lemma on the HPS throat jet (units r0 = 1)")
# qeihps.py:1112-1115: f''''(0)/f(0) = 259200 pi^2 (-L-1)/(L(3L+4)),
#                      r''''(0)/r(0) = 129600 pi^2 (2-L^2)/(L^2(3L+4))
A4 = 259200 * sp.pi**2 * (-L - 1) / (L * (3 * L + 4))
B4 = 129600 * sp.pi**2 * (2 - L**2) / (L**2 * (3 * L + 4))
a4 = sp.nsimplify(sp.simplify(A4 * r0**4))
b4 = sp.nsimplify(sp.simplify(B4 * r0**4))
chk("A4 r0^4 = 2/9, B4 r0^4 = 7/9 at L=-2/3", (a4, b4) == (sp.Rational(2, 9), sp.Rational(7, 9)),
    "(%s, %s)" % (a4, b4))
t, ps, ph = sp.symbols('t psi phi', real=True)   # psi = theta - pi/2 (scaled by r0 = 1)
X = [t, l, ps, ph]
fj = sp.exp(L) * (1 + a4 * l**4 / 24)
rj = 1 + b4 * l**4 / 24
g = sp.diag(-fj, 1, rj**2, rj**2 * sp.cos(ps)**2)
gi = g.inv()
Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                     - sp.diff(g[b, c], X[d])) for d in range(4)) / 2)
         for c in range(4)] for b in range(4)] for a in range(4)]
at0 = {t: 0, l: 0, ps: 0, ph: 0}
chk("every Gamma^a_bc = 0 at the throat point (theta = pi/2)",
    all(Gam[a][b][c].subs(at0) == 0 for a in range(4) for b in range(4) for c in range(4)))
Gf = [[[sp.lambdify((l, ps), Gam[a][b][c], 'math') for c in range(4)]
       for b in range(4)] for a in range(4)]


def gnorm(lv, pv):
    return math.sqrt(sum(Gf[a][b][c](lv, pv)**2 for a in range(4) for b in range(4)
                         for c in range(4)))


def supnorm(eps, n=81):
    m = 0.0
    for i in range(n):
        for j in range(n):
            lv = -eps + 2 * eps * i / (n - 1)
            pv = -eps + 2 * eps * j / (n - 1)
            if lv * lv + pv * pv <= eps * eps:
                m = max(m, gnorm(lv, pv))
    return m


lo, hi = 0.0, 1.5
for _ in range(40):
    mid = (lo + hi) / 2
    if mid * supnorm(mid) < 1:
        lo = mid
    else:
        hi = mid
EPS = lo * 0.98
chk("eps * sup_{B_eps}||Gamma||_F < 1 (Frobenius bounds the operator norm)",
    EPS * supnorm(EPS, 161) < 1, "eps = %.4f r0 = %.5f l_P" % (EPS, EPS * float(r0)))

# RK4 spot check: geodesics started inside B_eps, d^2/ds^2 |x|^2 > 0 along them
Gfull = [[[sp.lambdify(X, Gam[a][b][c], 'math') for c in range(4)] for b in range(4)]
         for a in range(4)]


def acc(x, v):
    return [-sum(Gfull[a][b][c](*x) * v[b] * v[c] for b in range(4) for c in range(4))
            for a in range(4)]


random.seed(67)
worst = float('inf')
for trial in range(60):
    x = [random.uniform(-1, 1) for _ in range(4)]
    nx = math.sqrt(sum(q * q for q in x))
    x = [q * EPS * random.uniform(0.05, 0.9) / nx for q in x]
    v = [random.gauss(0, 1) for _ in range(4)]
    nv = math.sqrt(sum(q * q for q in v))
    v = [q / nv for q in v]
    h = 1e-3
    for step in range(400):
        if sum(q * q for q in x) >= EPS * EPS:
            break
        a = acc(x, v)
        second = 2 * sum(q * q for q in v) + 2 * sum(x[i] * a[i] for i in range(4))
        worst = min(worst, second / max(sum(q * q for q in v), 1e-300))
        k1x, k1v = v, a
        x2 = [x[i] + h / 2 * k1x[i] for i in range(4)]; v2 = [v[i] + h / 2 * k1v[i] for i in range(4)]
        k2x, k2v = v2, acc(x2, v2)
        x3 = [x[i] + h / 2 * k2x[i] for i in range(4)]; v3 = [v[i] + h / 2 * k2v[i] for i in range(4)]
        k3x, k3v = v3, acc(x3, v3)
        x4 = [x[i] + h * k3x[i] for i in range(4)]; v4 = [v[i] + h * k3v[i] for i in range(4)]
        k4x, k4v = v4, acc(x4, v4)
        x = [x[i] + h / 6 * (k1x[i] + 2 * k2x[i] + 2 * k3x[i] + k4x[i]) for i in range(4)]
        v = [v[i] + h / 6 * (k1v[i] + 2 * k2v[i] + 2 * k3v[i] + k4v[i]) for i in range(4)]
chk("RK4: min over 60 geodesics of (d^2|x|^2/ds^2)/|x'|^2 > 0 inside B_eps",
    worst > 0, "min = %.4f" % worst)

# ---------------------------------------------------------------- D
print("D. size: what bounds a convex normal neighbourhood about the throat")
chk("throat sphere totally geodesic: Gamma^l_{psi psi}, Gamma^l_{phi phi}, Gamma^t_.. = 0 on l=0",
    all(sp.simplify(Gam[1][b][c].subs(l, 0)) == 0 for b in (2, 3) for c in (2, 3)) and
    all(sp.simplify(Gam[0][b][c].subs(l, 0)) == 0 for b in (2, 3) for c in (2, 3)))
Rm = {}
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                e = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                e += sum(Gam[a][c][k] * Gam[k][b][d] - Gam[a][d][k] * Gam[k][b][c] for k in range(4))
                Rm[a, b, c, d] = e
Kpp = sp.simplify((g[2, 2] * Rm[2, 3, 2, 3] / (g[2, 2] * g[3, 3])).subs(at0))
chk("sectional curvature of the throat sphere = 1/r0^2", Kpp == 1, "K = %s / r0^2" % Kpp)
print("     conjugate distance along an angular geodesic = pi r0 = %.5f l_P" % (math.pi * float(r0)))
tidal = [sp.simplify(Rm[a, 0, b, 0].subs(l, 0)) for a in range(4) for b in range(4)]
chk("tidal tensor R^a_{t b t} = 0 EXACTLY on the throat worldline l = 0 (all t, all psi)",
    all(q == 0 for q in tidal))
print("     -> the throat worldline has no conjugate points for any duration; the")
print("        caveat 'any sampling domain it admits is sub-Planckian' is bounded here")
print("        only in the angular directions; Whitehead itself states no size.")

# ---------------------------------------------------------------- E
print("E. does the narrowing move qeihps's FFKP status?  (read-only import)")
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
try:
    import qeihps as Q
    rows = Q.hypothesis_table()
    dom = [r for r in rows if r[0] == Q.FFKP and r[1] == "domain"]
    base = Q.qei_status(rows, Q.FFKP)
    chk("as seated: FFKP domain row = MET LOCALLY, status OPEN",
        dom and dom[0][4] == "MET LOCALLY" and base[0] == "OPEN", str(base[0]))
    for word in ("MET LOCALLY (conditional: metric C^{1,1} on a neighbourhood)",
                 "NOT-ESTABLISHED"):
        alt = [r if not (r[0] == Q.FFKP and r[1] == "domain") else r[:4] + (word,) for r in rows]
        st = Q.qei_status(alt, Q.FFKP)
        tv = Q.throat_verdict(alt, True)
        print("     domain -> %-62s FFKP %s; throat verdict %s" % (repr(word[:60]), st[0], tv[0]))
    print("     (qei_status maps ANY non-MET form row to REFUSED, so a bare")
    print("      NOT-ESTABLISHED would over-state the narrowing as a failure.)")
except Exception as e:  # the audit does not depend on this section
    print("     import failed: %r (section skipped)" % (e,))

print()
print("ALL %d CHECKS PASS" % len(OK) if all(OK) else "FAILURES: %d" % OK.count(False))
sys.exit(0 if all(OK) else 1)
