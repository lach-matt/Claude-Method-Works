#!/usr/bin/env python3
r"""
DOCKET 67, key static-open-rw-einstein-density.

Re-derives, from the metric alone (no Friedmann equation typed in), the
Einstein-equation source of the static open Robertson-Walker spacetime
    ds^2 = -c^2 dt^2 + a^2 [ dchi^2 + sinh^2 chi dOmega^2 ]      (R x H^3_a)
with G_ab = (8 pi G / c^4) T_ab, and checks every use fewsterteo.py makes of it:
  (1) energy density eps = -T^t_t = -3 c^4/(8 pi G a^2)  -> |eps| = 3c^4/(8piG a^2)
  (2) pressure p = +c^4/(8 pi G a^2) = -eps/3 (isotropic perfect fluid)
  (3) the same from the r-chart a^2[dr^2/(1+r^2) + r^2 dOmega^2]
  (4) controls: k = +1 static (Einstein static, no Lambda) flips both signs,
      k = 0 gives zero -- the computation can return something else
  (5) Friedmann cross-check H = 0, k = -1 (standard form, as restated in the
      sibling audit frw-metric-k-minus1-and-k0: Baumann eq.110-111)
  (6) Misner-Sharp mass m(R) = -c^2 R^3/(2 G a^2): m(0) = 0, m < 0,
      = (4pi/3)(eps/c^2) R^3
  (7) NEC: T_ab k^a k^b < 0 for every null k (eps + p < 0)
  (8) matching to achievable.required_density(b): C = b/a_c = sqrt(2 (m/b)/(a/b)^3)
      exactly -- G and c cancel; C = sqrt(1250) = 35.35533905932738 at the tree's
      window; compared with fewsterteo.witness_gap() imported READ-ONLY
      (no bytecode written into research/)
  (9) adjacent (not this key's claim, used by the same line): the bottom of the
      Laplace spectrum on H^3_a is 1/a^2, so the gap in units c/b is b/a_c.
Exit 0 iff every check passes.
"""
import sys, math
import sympy as sp

sys.dont_write_bytecode = True
FAILS = []


def check(label, ok):
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        FAILS.append(label)


def einstein_mixed(g, X):
    n = len(X)
    ginv = sp.simplify(g.inv())
    Gam = [[[sp.simplify(sum(ginv[i, l] * (sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j])
                                            - sp.diff(g[j, k], X[l])) for l in range(n)) / 2)
             for k in range(n)] for j in range(n)] for i in range(n)]
    Ric = sp.zeros(n, n)
    for j in range(n):
        for k in range(n):
            Ric[j, k] = sp.simplify(sum(sp.diff(Gam[i][j][k], X[i]) - sp.diff(Gam[i][j][i], X[k])
                                        + sum(Gam[i][i][l] * Gam[l][j][k] - Gam[i][k][l] * Gam[l][j][i]
                                              for l in range(n)) for i in range(n)))
    R = sp.simplify(sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    Gdn = sp.simplify(Ric - R * g / 2)
    return sp.simplify(ginv * Gdn), Gdn, ginv


t, chi, th, ph, r = sp.symbols('t chi theta phi r', real=True)
c, G, a = sp.symbols('c G a', positive=True)
kappa = 8 * sp.pi * G / c**4

results = {}
for name, S in (("k=-1", sp.sinh(chi)), ("k=0", chi), ("k=+1", sp.sin(chi))):
    g = sp.diag(-c**2, a**2, a**2 * S**2, a**2 * S**2 * sp.sin(th)**2)
    Gmix, Gdn, ginv = einstein_mixed(g, [t, chi, th, ph])
    Tmix = sp.simplify(Gmix / kappa)
    eps = sp.simplify(-Tmix[0, 0])
    ps = [sp.simplify(Tmix[i, i]) for i in (1, 2, 3)]
    offdiag = all(sp.simplify(Tmix[i, j]) == 0 for i in range(4) for j in range(4) if i != j)
    results[name] = (eps, ps, offdiag, Gdn, g)
    print(name, " eps =", eps, "  p =", ps)

eps, ps, offd, Gdn, g = results["k=-1"]
check("(1) k=-1 energy density = -3 c^4/(8 pi G a^2)",
      sp.simplify(eps + 3 * c**4 / (8 * sp.pi * G * a**2)) == 0)
check("(1) |eps| equals the tree's 3 c^4/(8 pi G a_c^2)",
      sp.simplify(sp.Abs(eps) - 3 * c**4 / (8 * sp.pi * G * a**2)) == 0)
check("(2) isotropic pressure p = +c^4/(8 pi G a^2) = -eps/3, T diagonal",
      offd and all(sp.simplify(p - c**4 / (8 * sp.pi * G * a**2)) == 0 for p in ps)
      and sp.simplify(ps[0] + eps / 3) == 0)

# (3) r-chart
g_r = sp.diag(-c**2, a**2 / (1 + r**2), a**2 * r**2, a**2 * r**2 * sp.sin(th)**2)
Gm_r, _, _ = einstein_mixed(g_r, [t, r, th, ph])
check("(3) r-chart gives the same eps and p",
      sp.simplify(-Gm_r[0, 0] / kappa - eps) == 0 and sp.simplify(Gm_r[1, 1] / kappa - ps[0]) == 0)

# (4) controls
e1, p1, _, _, _ = results["k=+1"]
e0, p0, _, _, _ = results["k=0"]
check("(4) control k=+1: eps = +3c^4/(8piG a^2), p = -c^4/(8piG a^2) (sign flips)",
      sp.simplify(e1 - 3 * c**4 / (8 * sp.pi * G * a**2)) == 0
      and sp.simplify(p1[0] + c**4 / (8 * sp.pi * G * a**2)) == 0)
check("(4) control k=0: eps = p = 0", sp.simplify(e0) == 0 and all(sp.simplify(x) == 0 for x in p0))

# (5) Friedmann, standard form: H^2 = 8piG rho/3 - k c^2/a^2 ; addot/a = -(4piG/3)(rho + 3p/c^2)
rho_m, pp = sp.symbols('rho_m p')
sol_rho = sp.solve(sp.Eq(0, 8 * sp.pi * G * rho_m / 3 - (-1) * c**2 / a**2), rho_m)[0]
sol_p = sp.solve(sp.Eq(0, -(4 * sp.pi * G / 3) * (sol_rho + 3 * pp / c**2)), pp)[0]
check("(5) Friedmann H=0,k=-1 gives rho c^2 = eps and p equal",
      sp.simplify(sol_rho * c**2 - eps) == 0 and sp.simplify(sol_p - ps[0]) == 0)

# (6) Misner-Sharp: 1 - 2 G m/(c^2 R) = g^{ab} d_a R d_b R, R = a sinh chi (static)
Rarea = a * sp.sinh(chi)
grad2 = sp.simplify(g.inv()[1, 1] * sp.diff(Rarea, chi)**2)   # = cosh^2 chi
Rs = sp.symbols('R', positive=True)
m_expr = sp.simplify((1 - grad2) * c**2 * Rarea / (2 * G))
m_R = sp.simplify(m_expr.subs(chi, sp.asinh(Rs / a)))
check("(6) m(R) = -c^2 R^3/(2 G a^2)", sp.simplify(m_R + c**2 * Rs**3 / (2 * G * a**2)) == 0)
check("(6) m(R) = (4pi/3)(eps/c^2) R^3, m(0) = 0, m < 0 for R > 0",
      sp.simplify(m_R - sp.Rational(4, 3) * sp.pi * eps / c**2 * Rs**3) == 0
      and sp.limit(m_R, Rs, 0) == 0 and (m_R.subs({Rs: 1, a: 1, c: 1, G: 1}) < 0))

# (7) NEC on a general null vector k = (1/c, n^i/a) with |n|=1 in an orthonormal-ish chart
Tdn = sp.simplify(Gdn / kappa)
n1, n2, n3 = sp.symbols('n1 n2 n3', real=True)
kvec = sp.Matrix([1 / c, n1 / a, n2 / (a * sp.sinh(chi)), n3 / (a * sp.sinh(chi) * sp.sin(th))])
null = sp.simplify((kvec.T * g * kvec)[0].subs(n3**2, 1 - n1**2 - n2**2))
TK = sp.simplify((kvec.T * Tdn * kvec)[0])
TK = sp.simplify(TK.subs(n3**2, 1 - n1**2 - n2**2))
print("    T_ab k^a k^b =", TK)
check("(7) k null and T_ab k^a k^b = eps + p = -2 c^4/(8 pi G a^2) < 0 for every null direction (k^t = 1/c)",
      null == 0 and sp.simplify(TK + 2 * c**4 / (8 * sp.pi * G * a**2)) == 0 and sp.simplify(TK - (eps + ps[0])) == 0)

# (8) matching to achievable.required_density
mb, ab, b = sp.symbols('m_b a_b b', positive=True)
M = mb * b * c**2 / G
V = sp.Rational(4, 3) * sp.pi * (ab * b)**3
rho_req = M * c**2 / V
a_c = sp.sqrt(3 * c**4 / (8 * sp.pi * G * rho_req))
C_sym = sp.simplify(b / a_c)
check("(8) C = b/a_c = sqrt(2 (m/b)/(a/b)^3): G, c and b cancel",
      sp.simplify(C_sym - sp.sqrt(2 * mb / ab**3)) == 0 and not C_sym.has(G) and not C_sym.has(c))
C_num = float(C_sym.subs({mb: sp.Rational(5, 1000), ab: sp.Rational(2, 100)}))
check("(8) C = sqrt(1250) = %.14f at m/b = 5e-3, a/b = 0.02" % C_num,
      abs(C_num - math.sqrt(1250)) < 1e-12)

sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
try:
    import achievable, fewsterteo
    tree_C = fewsterteo.witness_gap()
    check("(8) tree's fewsterteo.witness_gap() = %.14f agrees to 1e-12" % tree_C,
          abs(tree_C - C_num) < 1e-12 * C_num)
    # G sensitivity: CODATA 2022 G is identical; even a +-1e-3 change moves C by roundoff only
    for Gv in (6.67430e-11, 6.67430e-11 * (1 + 1e-3), 6.67554e-11):
        Mv = achievable.M_OVER_B * 1.0 * achievable.C_SI**2 / Gv
        Vv = 4.0 / 3.0 * math.pi * achievable.A_OVER_B**3
        rv = Mv * achievable.C_SI**2 / Vv
        acv = math.sqrt(3 * achievable.C_SI**4 / (8 * math.pi * Gv * rv))
        check("(8) G = %.5e -> C = %.12f (G-independent)" % (Gv, 1 / acv),
              abs(1 / acv - C_num) < 1e-9)
    print("    a_c at b = 1 m: %.10f m ; |eps| = %.6e Pa" % (1 / tree_C, achievable.required_density(1.0)))
except Exception as e:  # pragma: no cover
    check("(8) import of tree (read-only) failed: %r" % (e,), False)

# (9) bottom of spectrum of -Laplacian on H^3_a: f_k = sin(k chi)/sinh chi, eigenvalue (1+k^2)/a^2
k = sp.symbols('k', positive=True)
f = sp.sin(k * chi) / sp.sinh(chi)
lap = sp.diff(sp.sinh(chi)**2 * sp.diff(f, chi), chi) / (a**2 * sp.sinh(chi)**2)
check("(9) -Lap f_k = (1+k^2)/a^2 f_k (radial), inf over k>0 -> 1/a^2 = gap^2",
      sp.simplify(-lap - (1 + k**2) / a**2 * f) == 0)

print("\n%d FAIL(S)" % len(FAILS) if FAILS else "\nALL PASS")
sys.exit(1 if FAILS else 0)
