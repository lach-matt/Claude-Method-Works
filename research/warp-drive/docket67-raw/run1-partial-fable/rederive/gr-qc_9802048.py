#!/usr/bin/env python3
"""DOCKET 67, item 18 -- re-derivation of Hochberg & Visser gr-qc/9802048
(PRL 81, 746), 'The null energy condition in dynamic wormholes'.

Three checks.  Nothing here is quoted as a finding about the paper beyond what
each check literally establishes.

  CHECK A  (z3, general)  The Raychaudhuri sign lemma, eq. (7) of the paper:
           theta = 0, dtheta/du >= 0, twist = 0, shear^2 >= 0
           ==>  R_ab l^a l^b <= 0.     (paper's result (2), weak form)
           And its strict form: dtheta/du > 0  ==>  R_ab l^a l^b < 0.
           Also: dtheta/du >= 0 alone does NOT give the strict inequality
           (z3 exhibits the boundary model), which is exactly why the paper
           needs eq. (9)-(12) -- the 'at or near' subtlety.

  CHECK B  (sympy, general)  The fundamental-theorem-of-calculus step, eqs.
           (9)-(10): if A is C^2, A'(0) = 0 and A(e0) > A(0) for some e0 != 0,
           then A'' > 0 on some open interval between 0 and e0.  Shown by the
           double-integral identity  A(e0) - A(0) = int_0^e0 (e0 - s) A''(s) ds,
           and a numeric instance.

  CHECK C  (sympy, concrete)  A spherically symmetric DYNAMIC wormhole
              ds^2 = -dt^2 + a(t)^2 [ dl^2 + (b^2 + l^2) dOmega^2 ]
           (Ellis-Bronnikov profile with a scale factor; Kar-Sahdev shape).
           Affinely parametrised radial null geodesics k_pm, their expansions
           theta_pm computed as div(k), the two throats theta_pm = 0 located,
           and R_ab k^a k^b at the throat computed TWICE -- from the Ricci
           tensor of the metric and from the Raychaudhuri equation -- and
           compared.  Then the sign of R_kk at and near each throat is
           evaluated for concrete a(t).  This verifies results (1)-(3) of the
           paper in the spherical case, where the transverse average of (4)
           is the integrand itself (uniform on the sphere), so (4) reduces
           to (3).  The non-symmetric (4) is NOT re-derived here: its proof
           lives in gr-qc/9802046 and rests on the averaged flare-out
           condition, which needs an integral over a non-uniform surface.

Exit 0 if every check agrees with the paper; exit 1 otherwise.
"""
import sys
import sympy as sp

results = []

# ------------------------------------------------------------------ CHECK A
try:
    import z3
    th, dth, sig2, om2, Rll = z3.Reals("theta dtheta sigma2 omega2 Rll")
    # Raychaudhuri, paper eq. (1):  dtheta/du = -theta^2/2 - sigma^2 + omega^2 - R_ll
    ray = dth == -th * th / 2 - sig2 + om2 - Rll
    hyp_weak = z3.And(ray, th == 0, dth >= 0, om2 == 0, sig2 >= 0)
    hyp_strict = z3.And(ray, th == 0, dth > 0, om2 == 0, sig2 >= 0)

    s = z3.Solver(); s.add(hyp_weak, z3.Not(Rll <= 0))
    a1 = s.check() == z3.unsat          # eq. (7) holds
    s = z3.Solver(); s.add(hyp_strict, z3.Not(Rll < 0))
    a2 = s.check() == z3.unsat          # strict version holds
    s = z3.Solver(); s.add(hyp_weak, z3.Not(Rll < 0))
    a3 = s.check() == z3.sat            # weak hyp does NOT give strict: model exists
    model = s.model() if a3 else None
    # vacuity guard: the hypotheses are satisfiable at all
    s = z3.Solver(); s.add(hyp_strict); a4 = s.check() == z3.sat
    # twist matters: with omega^2 > 0 allowed the lemma FAILS (paper needs omega = 0)
    s = z3.Solver(); s.add(ray, th == 0, dth >= 0, sig2 >= 0, om2 >= 0, z3.Not(Rll <= 0))
    a5 = s.check() == z3.sat
    ok = a1 and a2 and a3 and a4 and a5
    results.append(("A: eq.(7) R_ll<=0 from weak flare-out", a1))
    results.append(("A: strict R_ll<0 from strict flare-out", a2))
    results.append(("A: weak flare-out alone leaves R_ll=0 open (boundary model %s)" % model, a3))
    results.append(("A: hypotheses non-vacuous", a4))
    results.append(("A: omega=0 hypothesis is load-bearing (lemma fails if twist allowed)", a5))
except ImportError:
    results.append(("A: z3 not available", False))

# ------------------------------------------------------------------ CHECK B
e, s_ = sp.symbols("epsilon s", real=True)
A = sp.Function("A")
# identity: A(e) - A(0) - e A'(0) = int_0^e (e - s) A''(s) ds   (Taylor with integral remainder)
# check it on a generic polynomial of degree 6
c = sp.symbols("c0:7")
Apoly = sum(ci * e**i for i, ci in enumerate(c))
lhs = Apoly.subs(e, e) - Apoly.subs(e, 0) - e * sp.diff(Apoly, e).subs(e, 0)
rhs = sp.integrate((e - s_) * sp.diff(Apoly, e, 2).subs(e, s_), (s_, 0, e))
b1 = sp.simplify(lhs - rhs) == 0
# consequence: with A'(0)=0 and A(e0)>A(0), the kernel (e0 - s) is > 0 on (0,e0),
# so A'' must be > 0 somewhere on (0,e0); by continuity, on an open interval.
# Numeric instance: A(e) = e^4 (A'(0)=0, A''(0)=0 -- the degenerate case the
# paper's eq.(9) is designed to handle):  A'' = 12 e^2 > 0 on (0, e0) \ {0}.
Ainst = e**4
b2 = sp.diff(Ainst, e).subs(e, 0) == 0 and sp.diff(Ainst, e, 2).subs(e, 0) == 0 \
     and all(sp.diff(Ainst, e, 2).subs(e, v) > 0 for v in [sp.Rational(1, 10), sp.Rational(1, 2), 1])
# and the open set of eq.(12) need not contain e=0 itself: here it does not.
results.append(("B: Taylor-remainder identity behind eqs.(9)-(10)", b1))
results.append(("B: degenerate throat A=e^4: A''>0 on punctured interval only", b2))

# ------------------------------------------------------------------ CHECK C
t, l, th_, ph = sp.symbols("t l theta phi", real=True)
b = sp.symbols("b", positive=True)
a = sp.Function("a")(t)
r2 = b**2 + l**2
coords = [t, l, th_, ph]
g = sp.diag(-1, a**2, a**2 * r2, a**2 * r2 * sp.sin(th_)**2)
ginv = g.inv()
n = 4

def christoffel(g, ginv):
    G = [[[0] * n for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                G[i][j][k] = sp.simplify(sum(ginv[i, m] * (sp.diff(g[m, j], coords[k]) + sp.diff(g[m, k], coords[j]) - sp.diff(g[j, k], coords[m])) for m in range(n)) / 2)
    return G

G = christoffel(g, ginv)

def ricci(G):
    R = sp.zeros(n)
    for i in range(n):
        for j in range(n):
            R[i, j] = sp.simplify(sum(sp.diff(G[k][i][j], coords[k]) - sp.diff(G[k][i][k], coords[j]) + sum(G[k][k][m] * G[m][i][j] - G[k][j][m] * G[m][i][k] for m in range(n)) for k in range(n)))
    return R

Ric = ricci(G)
sqrtg = sp.sqrt(-g.det())

def divergence(k):
    return sp.simplify(sum(sp.diff(sqrtg * k[i], coords[i]) for i in range(n)) / sqrtg)

def geodesic_residual(k):
    # k^b nabla_b k^a  (should vanish for affine geodesic)
    res = []
    for i in range(n):
        v = sum(k[j] * sp.diff(k[i], coords[j]) for j in range(n)) + sum(G[i][j][m] * k[j] * k[m] for j in range(n) for m in range(n))
        res.append(sp.simplify(v))
    return res

checks_c = []
for sgn in (+1, -1):
    # radial null geodesic, affine:  k = (1/a) d_t + sgn (1/a^2) d_l
    k = [1 / a, sgn / a**2, 0, 0]
    null = sp.simplify(sum(g[i, j] * k[i] * k[j] for i in range(n) for j in range(n))) == 0
    geo = all(x == 0 for x in geodesic_residual(k))
    theta = divergence(k)
    # expected: theta = (2/R) dR/dlambda, R = a sqrt(b^2+l^2)
    Rarea = a * sp.sqrt(r2)
    dR = sum(k[i] * sp.diff(Rarea, coords[i]) for i in range(n))
    theta_expected = sp.simplify(2 * dR / Rarea)
    th_ok = sp.simplify(theta - theta_expected) == 0
    # throat: theta = 0  <=>  adot * sqrt(r2) + sgn * l / sqrt(r2) = 0  <=>  l = -sgn * adot * r2 ... solve
    adot = sp.diff(a, t)
    throat_eq = sp.simplify(theta * a * Rarea)      # proportional to adot*r2 + sgn*l  (times factors)
    # Raychaudhuri check: dtheta/dlambda = -theta^2/2 - sigma^2 - R_kk, sigma = 0 for radial spherical congruence
    dtheta = sp.simplify(sum(k[i] * sp.diff(theta, coords[i]) for i in range(n)))
    Rkk = sp.simplify(sum(Ric[i, j] * k[i] * k[j] for i in range(n) for j in range(n)))
    ray_res = sp.simplify(dtheta + theta**2 / 2 + Rkk)
    ray_ok = ray_res == 0
    checks_c.append((sgn, null, geo, th_ok, ray_ok, theta, Rkk, dtheta))
    results.append(("C(%+d): k null, affine geodesic, theta = (2/R)dR/dlambda" % sgn, null and geo and th_ok))
    results.append(("C(%+d): Raychaudhuri (shear 0, twist 0) holds against Ricci of the metric" % sgn, ray_ok))

# Concrete scale factors and throat locations.  b = 1 throughout, evaluated at t = 1.
#   expanding   a = 1 + t/4   (adot = 1/4 > 0, slow enough that marginal surfaces exist)
#   contracting a = 1 - t/4   (adot = -1/4 < 0)
#   static      a = 1
#   fast        a = 1 + t^2   (adot = 2 at t=1: 2*adot*b > 1, so NO marginal surface exists --
#               the paper's 'temporary suspension eradicates the throat' case, gr-qc/9802046 s6)
# A marginal surface (theta = 0) is a THROAT only if dtheta/dlambda >= 0 (paper eq. (5)); the
# other root is an apparent-horizon-type surface the paper explicitly excludes.
concrete_ok = True
notes = []
def along_ray(expr, aexpr, sgn, l0, dt):
    """evaluate expr at the point reached from (t=1, l=l0) by moving dt along the radial null
    ray dl/dt = sgn / a(t), exactly."""
    Lint = sp.integrate(1 / aexpr, (t, 1, 1 + dt))
    return sp.simplify(expr.subs({b: 1}).subs({l: l0 + sgn * Lint, t: 1 + dt}))
for aexpr, label, expect_throats in [(1 + t / 4, "expanding a=1+t/4", 1), (1 - t / 4, "contracting a=1-t/4", 1),
                                     (sp.Integer(1) + 0 * t, "static a=1", 1), (1 + t**2, "fast a=1+t^2", 0)]:
    for sgn, null, geo, th_ok, ray_ok, theta, Rkk, dtheta in checks_c:
        thc = theta.subs(a, aexpr).doit()
        Rc = Rkk.subs(a, aexpr).doit()
        dthc = dtheta.subs(a, aexpr).doit()
        thc1 = sp.simplify(thc.subs({t: 1, b: 1}))
        marg = [s0 for s0 in sp.solve(sp.Eq(thc1, 0), l) if s0.is_real]
        adot1 = sp.diff(aexpr, t).subs(t, 1)
        throats = []
        for s0 in marg:
            Rth = sp.simplify(Rc.subs({t: 1, b: 1, l: s0}))
            dth1 = sp.simplify(dthc.subs({t: 1, b: 1, l: s0}))
            if dth1 >= 0:
                throats.append(s0)
                weak = bool(Rth <= 0)
                strict = bool(Rth < 0) and bool(dth1 > 0)
                # open interval ALONG THE NULL RAY through the throat (paper eq. (12)-(13)): sample
                # at affine displacements both sides, exactly on the ray
                nb = [along_ray(Rc, aexpr, sgn, s0, d) for d in (sp.Rational(-1, 20), sp.Rational(1, 20))]
                nbhd = all(bool(v < 0) for v in nb)
                side = "l<0" if s0 < 0 else ("l>0" if s0 > 0 else "l=0")
                expect_side = "l=0" if adot1 == 0 else ("l<0" if (sgn * adot1 > 0) else "l>0")
                side_ok = side == expect_side
                notes.append("%s sgn=%+d THROAT l=%s (%.4f) R_kk=%.4f dtheta=%.4f weak=%s strict=%s open-nbhd-on-ray=%s side=%s(expected %s)"
                             % (label, sgn, s0, float(s0), float(Rth), float(dth1), weak, strict, nbhd, side, expect_side))
                concrete_ok = concrete_ok and weak and strict and nbhd and side_ok
            else:
                notes.append("%s sgn=%+d marginal-but-NOT-throat l=%s (%.4f): dtheta=%.4f<0, R_kk=%.4f (NEC holds there; paper excludes such surfaces)"
                             % (label, sgn, s0, float(s0), float(dth1), float(Rth)))
                concrete_ok = concrete_ok and bool(Rth > 0)
        if len(throats) != expect_throats:
            notes.append("%s sgn=%+d: %d throats found, expected %d: %s" % (label, sgn, len(throats), expect_throats, throats))
            concrete_ok = False
        if expect_throats == 0:
            # no throat: report the NEC at the centre and how far a ray gets (comoving) -- for information only
            Rc0 = sp.simplify(Rc.subs({t: 1, b: 1, l: 0}))
            reach = sp.integrate(1 / aexpr, (t, 1, sp.oo))
            notes.append("%s sgn=%+d: no throat; R_kk at centre = %.4f; a ray from t=1 covers comoving distance %s = %.4f only (never traverses)"
                         % (label, sgn, float(Rc0), reach, float(reach)))
# two throats of the dynamic cases are displaced to OPPOSITE sides and coalesce at l=0 when static: checked via side_ok above
results.append(("C: every throat (theta=0, dtheta>=0) has R_kk<0 there and on an open interval along its null ray; the two dynamic throats sit on opposite sides of the centre (expanding: before it, contracting: after it) and coalesce at l=0 when static; the fast case has no throat at all", concrete_ok))

# ------------------------------------------------------------------ CHECK D
# (closed form)  In  ds^2 = -dt^2 + a^2[dl^2 + (b^2+l^2) dOmega^2]  an H&V marginal surface
# for k_pm exists iff  adot (b^2 + l^2) = -/+ l  has a real root, i.e. iff |adot| <= 1/(2b)
# (the maximum of |l|/(b^2+l^2) is 1/(2b) at |l| = b).  Tomikawa-Izumi-Shiromizu
# arXiv:1503.01926 eq. (62)-(63) give the window in which the dynamical Ellis wormhole
# satisfies the DOMINANT energy condition under THEIR (hybrid) throat definition:
# adot^2 b^2 >= 2/3 and adot^2 < 1/b^2.  Is that window disjoint from the H&V-throat range?
# If so, the DEC-satisfying 'cosmological wormhole' has NO H&V throat, so the H&V theorem is
# silent there rather than contradicted -- and the Discussion's 'if one ever succeeds in
# passing through ... there must be NEC violations' rests on the throat definition.
ad, bb, ll = sp.symbols("adot b l", positive=True)
ratio = ll / (bb**2 + ll**2)
crit = sp.solve(sp.diff(ratio, ll), ll)
maxratio = sp.simplify(ratio.subs(ll, crit[0]))
d1 = (crit == [bb]) and (maxratio == 1 / (2 * bb))
# H&V range: adot^2 b^2 <= 1/4 ; TIS DEC window: adot^2 b^2 >= 2/3.  Disjoint iff 1/4 < 2/3.
d2 = sp.Rational(1, 4) < sp.Rational(2, 3)
# and z3: no (adot, b) satisfies both
try:
    import z3
    x = z3.Real("adot_b_sq")
    s = z3.Solver(); s.add(x >= 0, x <= z3.RealVal("1/4"), x >= z3.RealVal("2/3"))
    d3 = s.check() == z3.unsat
except ImportError:
    d3 = False
results.append(("D: H&V marginal surface exists iff |adot| b <= 1/2 (max of |l|/(b^2+l^2) is 1/(2b) at |l|=b)", d1))
results.append(("D: Tomikawa et al. DEC window adot^2 b^2 >= 2/3 is DISJOINT from the H&V-throat range adot^2 b^2 <= 1/4 (sympy)", d2))
results.append(("D: ... and z3 confirms no adot^2 b^2 lies in both", d3))

# ------------------------------------------------------------------ report
print("gr-qc/9802048 re-derivation")
allok = True
for label, ok in results:
    print("  [%s] %s" % ("OK " if ok else "BAD", label))
    allok = allok and ok
print("  C notes:")
for nline in notes:
    print("    " + nline)
print("VERDICT:", "agrees with source on every check" if allok else "DISAGREEMENT -- read the BAD rows")
sys.exit(0 if allok else 1)
