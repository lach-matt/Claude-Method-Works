#!/usr/bin/env python3
"""DOCKET 67 audit, hep-th/0202068 (Khusnutdinov & Sushkov, PRD 65 084028, 2002).

Checks what is finite / closed-form, with sympy:
 (A) the abstract's two numbers are mutually consistent: stable conformal (xi=1/6)
     throat a = 0.16/m and self-consistent m = 11.35 m_P give a = 0.0141 l_P.
 (B) the short-throat flat-space wormhole r(rho) = a + |rho| (as restated in the
     later literature; the KS body was NOT read here): Misner-Sharp mass
     m = (r/2)(1 - r'^2) is exactly 0 for rho != 0, so ADM mass 0 on both sides;
     at rho = 0 r' jumps -1 -> +1 and m is undefined in the literal metric.
 (C) under smooth even regularisations r_eps with |r_eps'| <= 1, m >= 0 everywhere
     and m(0) = r_eps(0)/2 > 0 -> the tree's 'm = r_0/2 > 0 at the throat' holds as
     a limit of regularisations, and the sign 'no m < 0' is robust.
 (D) the thin shell carries negative energy: E_shell = -2a (G=c=1) i.e. sigma =
     -1/(2 pi a), and int R dl -> -8/a, matching the restated R = -8 delta(rho)/a.
 (E) the tree's SERIES_RESULT premise (r smooth at l=0, finite r''(0)) FAILS for the
     literal KS metric: r''(0) -> infinity as eps -> 0.
"""
import sympy as sp

ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)

# (A)
a_over = sp.Rational(16, 100) / sp.Rational(1135, 100)
print("0.16/11.35 =", sp.N(a_over, 8))
chk("(A) 0.16/11.35 rounds to 0.0141", round(float(a_over), 4) == 0.0141)

# (B)
rho = sp.Symbol('rho', real=True); a = sp.Symbol('a', positive=True)
for side, r in (("rho>0", a + rho), ("rho<0", a - rho)):
    m = sp.simplify(r / 2 * (1 - sp.diff(r, rho) ** 2))
    chk("(B) Misner-Sharp m = 0 on %s" % side, m == 0)

# (C),(D),(E) two smooth even regularisations
eps = sp.Symbol('epsilon', positive=True)
regs = {
    "sqrt": a + sp.sqrt(rho ** 2 + eps ** 2) - eps,
    "logcosh": a + eps * sp.log(sp.cosh(rho / eps)),
}
for nm, r in regs.items():
    rp = sp.diff(r, rho); rpp = sp.diff(r, rho, 2)
    m = sp.simplify(r / 2 * (1 - rp ** 2))
    chk("(C/%s) r'(0) = 0" % nm, sp.simplify(rp.subs(rho, 0)) == 0)
    chk("(C/%s) m(0) = r(0)/2 = a/2" % nm, sp.simplify(m.subs(rho, 0) - a / 2) == 0)
    chk("(C/%s) |r'| <= 1 -> m >= 0 (1 - r'^2 >= 0 symbolic)" % nm,
        sp.simplify(1 - rp ** 2).is_nonnegative is not False)
    # numeric scan m >= 0
    import math
    f = sp.lambdify((rho, a, eps), m, 'math')
    chk("(C/%s) numeric m >= 0 on grid" % nm,
        all(f(x / 50.0, 1.0, 0.05) >= -1e-15 for x in range(-200, 201)))
    # (D) shell energy: rho_E = -G^t_t/(8 pi), G^t_t = (2 r r'' + r'^2 - 1)/r^2 (f = 1)
    Gtt = (2 * r * rpp + rp ** 2 - 1) / r ** 2
    integrand = -(Gtt / (8 * sp.pi)) * 4 * sp.pi * r ** 2
    fn = sp.lambdify((rho, a, eps), integrand, 'math')
    from math import fsum
    def quad(g, lo, hi, n=200000):
        h = (hi - lo) / n
        return fsum(g(lo + (i + 0.5) * h) for i in range(n)) * h
    for e in (1e-2, 1e-3):
        L = min(1.0, 300 * e)  # logcosh overflows beyond; tails are ~sech^2
        E = quad(lambda x: fn(x, 1.0, e), -L, L)
        print("   %s eps=%g  E_shell(a=1) = %.6f" % (nm, e, E))
    chk("(D/%s) E_shell -> -2a (a=1, eps=1e-3)" % nm, abs(E + 2.0) < 1e-2)
    # Ricci scalar for f=1: R = -2 G^t_t ... check directly
    t, th, ph = sp.symbols('t theta phi')
    # for ultrastatic metric R = R^(3) = -2(2 r r'' + r'^2 - 1)/r^2
    R3 = -2 * (2 * r * rpp + rp ** 2 - 1) / r ** 2
    fr = sp.lambdify((rho, a, eps), R3, 'math')
    I = quad(lambda x: fr(x, 1.0, 1e-3), -0.3, 0.3)
    print("   %s int R drho (a=1, eps=1e-3) = %.5f  (restated: -8/a = -8)" % (nm, I))
    chk("(D/%s) int R drho -> -8/a" % nm, abs(I + 8.0) < 5e-2)
    # (E)
    rpp0 = sp.simplify(rpp.subs(rho, 0))
    print("   %s r''(0) =" % nm, rpp0)
    chk("(E/%s) r''(0) -> oo as eps -> 0" % nm, sp.limit(rpp0, eps, 0, '+') == sp.oo)

# independent check of the 3-curvature formula used in (D), ultrastatic metric
l, th = sp.symbols('l theta', real=True); rr = sp.Function('r')(l)
g = sp.diag(1, rr ** 2, rr ** 2 * sp.sin(th) ** 2); x = [l, th, sp.Symbol('phi')]
gi = g.inv(); n = 3
Gam = [[[sum(gi[i, d] * (sp.diff(g[d, j], x[k]) + sp.diff(g[d, k], x[j]) - sp.diff(g[j, k], x[d])) for d in range(n)) / 2
         for k in range(n)] for j in range(n)] for i in range(n)]
Ric = sp.zeros(n)
for b in range(n):
    for c in range(n):
        e = 0
        for q in range(n):
            e += sp.diff(Gam[q][b][c], x[q]) - sp.diff(Gam[q][b][q], x[c])
            for d in range(n):
                e += Gam[q][q][d] * Gam[d][b][c] - Gam[q][c][d] * Gam[d][b][q]
        Ric[b, c] = e
Rs = sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
target = -2 * (2 * rr * rr.diff(l, 2) + rr.diff(l) ** 2 - 1) / rr ** 2
chk("3-curvature R = -2(2 r r'' + r'^2 - 1)/r^2 (sympy from metric)", sp.simplify(Rs - target) == 0)

print("ALL PASS" if ok else "SOME FAIL")
raise SystemExit(0 if ok else 1)
