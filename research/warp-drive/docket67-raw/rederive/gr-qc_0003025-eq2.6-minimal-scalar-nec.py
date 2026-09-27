#!/usr/bin/env python3
"""DOCKET 67 audit: Barcelo-Visser gr-qc/0003025 eq. (2.6), xi = 0 case.
T_mn k^m k^n = (k.grad phi)^2 >= 0 for a classical, canonical, minimally
coupled scalar with ANY potential V, on ANY metric.

Checks (sympy + z3); each prints PASS/FAIL and the script exits 1 on a FAIL.
 A  general symbolic metric: T_kk - (k.dphi)^2 == -(g_kk)(X/2 + V) identically,
    so the potential drops out exactly when g_kk = 0 (k null).  No flat-metric
    restriction (the tree's own machine check is flat, higgs.py:325).
 A2 an explicit curved rational Lorentzian metric with an exactly-null k
    (radicals): T_kk == (k.dphi)^2 exactly, for symbolic V.
 B  T_mn derived by METRIC VARIATION of sqrt(-g) P(X,phi), 4D, symbolic inverse
    metric: T_mn = P_X d_m phi d_n phi + g_mn P, hence T_kk = P_X (k.dphi)^2.
    Canonical P = X - V gives BV; phantom P = -X - V and any k-essence with
    P_X < 0 give T_kk < 0 -- the named hypothesis 'canonical' is load-bearing.
 C  z3: for null k != 0 and w.k = 0 in Minkowski, w.w >= 0.  Hence the gauge
    field T_kk = F_{k a} F_k^a >= 0, and the gauged doublet T_kk = 2|k.DH|^2 +
    gauge >= 0: the tree's 'one real field' reduction loses nothing.
 C2 multi-field: T_kk = G_ab u^a u^b, >= 0 for all u iff G is PSD (z3 counter
    example for an indefinite G).
 D  the source's xi-general eq. (2.6) from its eq. (2.3) on a straight null
    line: numerator = phi'^2 - xi (phi^2)''.  And the adjacent PROSE case
    statements (which extremum type violates) are evaluated against eq. (2.6):
    recorded as a DISCREPANCY of the arXiv v2 text, not part of the xi = 0
    result, not repaired, not to be quoted against the journal version unread.
 E  the vev: rho = V_min < 0 (V(0)=0 convention), rho + p = 0: WEC violated,
    NEC saturated -- 'negative energy' and 'NEC violation' are different things.
"""
import sys, itertools
import sympy as sp

fails = []
def chk(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    if not ok:
        fails.append(label)

# ---------------------------------------------------------------- A
g = sp.Matrix(4, 4, lambda i, j: sp.Symbol('g%d%d' % (min(i, j), max(i, j))))
dphi = sp.symbols('d0:4')
k = sp.symbols('k0:4')
X, V = sp.symbols('X V')   # X = g^{ab} d_a phi d_b phi (any value), V arbitrary
T = sp.Matrix(4, 4, lambda m, n: dphi[m]*dphi[n] - g[m, n]*(X/2 + V))
Tkk = sum(T[m, n]*k[m]*k[n] for m in range(4) for n in range(4))
kdphi = sum(k[m]*dphi[m] for m in range(4))
gkk = sum(g[m, n]*k[m]*k[n] for m in range(4) for n in range(4))
chk("A  T_kk - (k.dphi)^2 + g_kk (X/2+V) == 0 identically, symbolic metric",
    sp.expand(Tkk - kdphi**2 + gkk*(X/2 + V)) == 0)
chk("A  dT_kk/dV == -g_kk  (V enters ONLY through g_kk, zero for null k)",
    sp.expand(sp.diff(Tkk, V) + gkk) == 0)

# ---------------------------------------------------------------- A2
gnum = sp.Matrix([[-3, sp.Rational(1, 2), 0, sp.Rational(1, 3)],
                  [sp.Rational(1, 2), 2, sp.Rational(1, 5), 0],
                  [0, sp.Rational(1, 5), sp.Rational(3, 2), sp.Rational(1, 7)],
                  [sp.Rational(1, 3), 0, sp.Rational(1, 7), 1]])
ev = [sp.re(sp.N(e)) for e in gnum.eigenvals(multiple=True)]
chk("A2 metric is Lorentzian (one negative eigenvalue)", sum(1 for e in ev if e < 0) == 1)
k0 = sp.Symbol('k0')
ks = [k0, 1, 2, -1]
sol = [s for s in sp.solve(sp.expand(sum(gnum[m, n]*ks[m]*ks[n] for m in range(4) for n in range(4))), k0) if s.is_real]
kk = [sol[0], 1, 2, -1]
ginv = gnum.inv()
dp = [sp.Rational(3, 2), -2, sp.Rational(5, 7), 4]
Xn = sum(ginv[a, b]*dp[a]*dp[b] for a in range(4) for b in range(4))
Tn = sp.Matrix(4, 4, lambda m, n: dp[m]*dp[n] - gnum[m, n]*(Xn/2 + V))
Tkkn = sum(Tn[m, n]*kk[m]*kk[n] for m in range(4) for n in range(4))
chk("A2 k exactly null on the curved metric", sp.simplify(sum(gnum[m, n]*kk[m]*kk[n] for m in range(4) for n in range(4))) == 0)
chk("A2 T_kk == (k.dphi)^2 exactly, V symbolic, curved metric",
    sp.simplify(Tkkn - sum(kk[m]*dp[m] for m in range(4))**2) == 0)

# ---------------------------------------------------------------- B
gi = sp.Matrix(4, 4, lambda i, j: sp.Symbol('h%d%d' % (min(i, j), max(i, j))))  # g^{mn}
phi = sp.Symbol('phi')
P = sp.Function('P')
Xs = -sp.Rational(1, 2)*sum(gi[a, b]*dphi[a]*dphi[b] for a in range(4) for b in range(4))
# sqrt(-g) with g = det(g_mn) = 1/det(g^mn): d sqrt(-g)/d g^{mn} = -1/2 sqrt(-g) g_mn (Jacobi),
# verified here symbolically rather than assumed:
detgi = gi.det()
sqrtmg = sp.sqrt(-1/detgi)
lower = gi.inv()          # g_mn
ok_jacobi = True
for (m, n) in [(0, 0), (0, 1), (2, 3)]:
    hmn = gi[m, n]
    lhs = sp.diff(sqrtmg, hmn)
    mult = 1 if m == n else 2   # symmetric symbol appears twice off-diagonal
    rhs = -sp.Rational(1, 2)*sqrtmg*lower[m, n]*mult
    ok_jacobi &= sp.simplify((lhs - rhs).subs({gi[i, j]: (sp.Integer(-1) if i == j == 0 else (1 if i == j else 0)) for i in range(4) for j in range(i, 4)})) == 0
chk("B  Jacobi d sqrt(-g)/d g^mn = -1/2 sqrt(-g) g_mn (at eta)", bool(ok_jacobi))
L = sqrtmg*P(Xs, phi)
eta_sub = {gi[i, j]: (sp.Integer(-1) if i == j == 0 else (1 if i == j else 0)) for i in range(4) for j in range(i, 4)}
ok_B = True
for (m, n) in itertools.product(range(4), repeat=2):
    if n < m:
        continue
    mult = 1 if m == n else 2
    Tmn = (-2/sqrtmg*sp.diff(L, gi[m, n])/mult)
    Tmn = sp.simplify(Tmn.subs(eta_sub).doit())
    etamn = -1 if m == n == 0 else (1 if m == n else 0)
    Xeta = Xs.subs(eta_sub)
    PX = sp.Subs(sp.Derivative(P(sp.Symbol('x'), phi), sp.Symbol('x')), sp.Symbol('x'), Xeta).doit()
    want = PX*dphi[m]*dphi[n] + etamn*P(Xeta, phi)
    ok_B &= sp.simplify(Tmn - want) == 0
chk("B  metric variation: T_mn = P_X d_m phi d_n phi + g_mn P (at eta, all 10 comps)", bool(ok_B))
# null contraction with a null k at eta: T_kk = P_X (k.dphi)^2
kn = (3, 1, 2, 2)   # -9+1+4+4 = 0
PXs = sp.Symbol('P_X'); Ps = sp.Symbol('P')
TkkP = sum((PXs*dphi[m]*dphi[n] + (-1 if m == n == 0 else (1 if m == n else 0))*Ps)*kn[m]*kn[n]
           for m in range(4) for n in range(4))
chk("B  T_kk = P_X (k.dphi)^2 for exactly null k",
    sp.expand(TkkP - PXs*sum(kn[m]*dphi[m] for m in range(4))**2) == 0)
chk("B  canonical P = x - V: P_X = 1 -> T_kk = (k.dphi)^2, BV eq. (2.6) at xi = 0", sp.diff(sp.Symbol("x") - V, sp.Symbol("x")) == 1)
# explicit counterexamples to dropping 'canonical'
subs1 = {dphi[0]: 1, dphi[1]: 0, dphi[2]: 0, dphi[3]: 0}
chk("B  phantom P = -X - V: T_kk = -(k.dphi)^2 = -9 < 0",
    sp.expand(TkkP.subs({PXs: -1, Ps: 0}).subs(subs1)) == -9)
xx = sp.Symbol('x')
Pk = xx - xx**2      # k-essence P(X) = X - X^2 : P_X = 1 - 2X < 0 for X > 1/2
Xval = sp.Rational(1, 2)*(3**2 - 0)  # X = -1/2 eta^{ab} d_a d_b with dphi = (3,0,0,0): +9/2
PXval = sp.diff(Pk, xx).subs(xx, Xval)
chk("B  k-essence P = X - X^2 at X = 9/2: P_X = -8, T_kk = -8 (k.dphi)^2 < 0 (classical, minimal coupling)",
    PXval == -8 and sp.expand(TkkP.subs({PXs: PXval, Ps: 0}).subs({dphi[0]: 3, dphi[1]: 0, dphi[2]: 0, dphi[3]: 0})) == -8*81)

# ---------------------------------------------------------------- C (z3)
try:
    import z3
    k0_, k1_, k2_, k3_, w0, w1, w2, w3 = z3.Reals('k0 k1 k2 k3 w0 w1 w2 w3')
    s = z3.Solver()
    s.add(-k0_*k0_ + k1_*k1_ + k2_*k2_ + k3_*k3_ == 0, k0_ != 0,
          -w0*k0_ + w1*k1_ + w2*k2_ + w3*k3_ == 0,
          -w0*w0 + w1*w1 + w2*w2 + w3*w3 < 0)
    r = s.check()
    chk("C  z3: null k != 0, w.k = 0  =>  w.w >= 0 (negation %s)" % r, r == z3.unsat)
    # C2 multi-field target metric
    a, b, c, u1, u2 = z3.Reals('a b c u1 u2')
    s2 = z3.Solver()
    s2.add(a >= 0, c >= 0, a*c - b*b >= 0, a*u1*u1 + 2*b*u1*u2 + c*u2*u2 < 0)
    r2 = s2.check()
    chk("C2 z3: PSD target metric G => G_ab u^a u^b >= 0 (negation %s)" % r2, r2 == z3.unsat)
    s3 = z3.Solver()
    s3.add(a == 1, c == 1, b == 2, a*u1*u1 + 2*b*u1*u2 + c*u2*u2 < 0)
    r3 = s3.check()
    chk("C2 z3: indefinite G (1,2;2,1) admits T_kk < 0 (%s)" % r3, r3 == z3.sat)
except ImportError:
    chk("C  z3 not installed", False)
# complex doublet with gauge covariant derivative: T_kk = 2 Re (k.DH)^dagger (k.DH) = 2|z|^2
z = sp.symbols('z1:5', real=True)
kDH = sp.Matrix([z[0] + sp.I*z[1], z[2] + sp.I*z[3]])
chk("C  doublet: 2 (k.DH)^dagger (k.DH) == 2 sum z_i^2 >= 0",
    sp.expand((2*(kDH.H*kDH))[0] - 2*sum(zi**2 for zi in z)) == 0)

# ---------------------------------------------------------------- D
lam, xi, kap = sp.symbols('lambda xi kappa')
f = sp.Function('f')
# flat, straight null line x^m = k^m lambda; phi along it = f(lambda)
num_23 = sp.diff(f(lam), lam)**2 - 2*xi*sp.diff(f(lam)*sp.diff(f(lam), lam), lam)
num_26 = sp.diff(f(lam), lam)**2 - xi*sp.diff(f(lam)**2, lam, 2)
chk("D  eq.(2.3) contracted with null k == eq.(2.6) numerator phi'^2 - xi (phi^2)''",
    sp.simplify(num_23 - num_26) == 0)
chk("D  xi = 0: eq.(2.6) -> phi'^2 >= 0 (BV: 'clearly satisfied by minimally coupled scalars')",
    sp.simplify(num_26.subs(xi, 0) - sp.diff(f(lam), lam)**2) == 0)
# PROSE case statements, evaluated at an extremum of phi^2 with phi != 0 (phi' = 0):
def nec_sign(xi_v, phi0, curv, kap_v=1):
    """phi = phi0 + curv*lam^2/2 near lam = 0; returns sign of eq.(2.6) at 0."""
    ff = phi0 + curv*lam**2/2
    val = ((sp.diff(ff, lam)**2 - xi_v*sp.diff(ff**2, lam, 2))/(kap_v - xi_v*ff**2)).subs(lam, 0)
    return sp.sign(val)
# local MIN of phi^2 (phi0 > 0, curv > 0) and local MAX (phi0 > 0, curv < 0)
cases = [
    ("xi<0", sp.Rational(-1, 10), sp.Rational(1, 2), "BV: any local MINIMUM of phi^2 violates"),
    ("xi>0, |phi|<(kappa/xi)^1/2", sp.Rational(1, 10), sp.Rational(1, 2), "BV: any local MAXIMUM violates"),
    ("xi>0, |phi|>(kappa/xi)^1/2", sp.Rational(1, 10), 5, "BV: any local MINIMUM violates"),
]
print("\n   D-prose: sign of eq.(2.6) at an extremum of phi^2 with phi != 0")
disc = 0
for name, xv, p0, bvsays in cases:
    smin = nec_sign(xv, p0, 1)
    smax = nec_sign(xv, p0, -1)
    violator = "MINIMUM" if smin < 0 else ("MAXIMUM" if smax < 0 else "neither")
    agree = (("MINIMUM" in bvsays) == (violator == "MINIMUM"))
    disc += (not agree)
    print("   %-28s at min: %+d  at max: %+d  -> eq.(2.6) says %s violates;  %s  [%s]"
          % (name, smin, smax, violator, bvsays, "agrees" if agree else "DISCREPANCY"))
print("   D-prose: %d of 3 prose case statements disagree with eq.(2.6) as printed "
      "(arXiv v2).  RECORDED, NOT REPAIRED; outside the xi = 0 result audited here." % disc)
DISCREPANCY_BV_PROSE_CASES = disc

# ---------------------------------------------------------------- E
m_h, v = sp.Rational(12513, 100), sp.Rational(24622, 100)   # tree's READ m_h; v ~ 246.22 GeV
Vmin = -m_h**2*v**2/8
rho, p = Vmin, -Vmin
chk("E  vev (V(0)=0 convention): rho = V_min = %.4e GeV^4 < 0 (WEC violated)" % float(Vmin), rho < 0)
chk("E  vev: rho + p == 0 exactly (NEC saturated, not violated)", rho + p == 0)

print()
print("RESULT: %d FAIL" % len(fails))
sys.exit(1 if fails else 0)
