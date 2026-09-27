#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation / machine check of
    I(u) = INT_0^oo sin(ku)/(e^k - 1) dk = (pi/2) coth(pi u) - 1/(2u)      (noise.py:573-576)
and its beta-scaled form and third-derivative kernel (noise.py:112-114).
Stdlib + sympy + mpmath.  Exits 1 on any failure.  Writes nothing."""
import sys
import sympy as sp
import mpmath as mp

FAIL = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("   [" + detail + "]" if detail else ""))
    if not ok:
        FAIL.append(name)

u, k, z, y, b = sp.symbols('u k z y beta', positive=True)
n = sp.symbols('n', integer=True, positive=True)
RHS = sp.pi / 2 * sp.coth(sp.pi * u) - 1 / (2 * u)

# ---------- A. symbolic derivation 1: geometric series + Mittag-Leffler ----------
# 1/(e^k-1) = SUM_{n>=1} e^{-nk}  (k > 0);  INT_0^oo sin(ku) e^{-nk} dk = u/(n^2+u^2)
term = sp.simplify(sp.integrate(sp.sin(k * u) * sp.exp(-n * k), (k, 0, sp.oo), conds='none'))
chk("A1 Laplace term INT sin(ku) e^{-nk} dk = u/(n^2+u^2)", sp.simplify(term - u / (n**2 + u**2)) == 0, str(term))
# sympy 1.14 cannot close SUM u/(n^2+u^2) symbolically; the Mittag-Leffler sum is checked with mpmath.nsum
# at 40 digits here, and symbolically by route B (Abel-Plana) and route C (termwise Taylor, |u| < 1).
mp.mp.dps = 40
wA = max(abs(mp.nsum(lambda m: uu / (m**2 + uu**2), [1, mp.inf]) - (mp.pi/2*mp.coth(mp.pi*uu) - 1/(2*uu)))
         for uu in map(mp.mpf, ['0.05', '0.7', '1', '3', '25']))
chk("A2 SUM_n u/(n^2+u^2) = (pi/2)coth(pi u) - 1/(2u) (Mittag-Leffler; mpmath.nsum, 40 dps, 5 u)", wA < mp.mpf(10)**-35, "worst %s" % mp.nstr(wA, 3))
# Fubini/Tonelli: SUM_n INT |sin(ku)| e^{-nk} dk <= SUM_n INT k u e^{-nk} dk = u SUM 1/n^2 < oo
bound = sp.summation(sp.integrate(k * u * sp.exp(-n * k), (k, 0, sp.oo)), (n, 1, sp.oo))
chk("A3 Tonelli bound SUM INT k u e^{-nk} = pi^2 u/6 finite (licenses sum/integral swap)",
    sp.simplify(bound - sp.pi**2 * u / 6) == 0, str(bound))

# ---------- B. symbolic derivation 2: Abel-Plana (Henrici form, as READ in arXiv:2112.09819 Thm 2.1) ----------
# phi(x) = e^{-xz}, z>0:  SUM phi(n) = phi(0)/2 + INT phi + i INT [phi(iy)-phi(-iy)]/(e^{2 pi y}-1) dy
#   => 1/(1-e^{-z}) = 1/2 + 1/z + 2 INT sin(zy)/(e^{2 pi y}-1) dy
legendre = sp.Rational(1, 2) * (1 / (1 - sp.exp(-z)) - sp.Rational(1, 2) - 1 / z)
chk("B1 Abel-Plana => INT_0^oo sin(zy)/(e^{2pi y}-1) dy = coth(z/2)/4 - 1/(2z) (Legendre form)",
    sp.simplify((legendre - (sp.coth(z / 2) / 4 - 1 / (2 * z))).rewrite(sp.exp)) == 0)
# phi(iy)-phi(-iy) = e^{-iyz}-e^{iyz} = -2i sin(yz)
chk("B2 i[phi(iy)-phi(-iy)] = 2 sin(yz)", sp.simplify(sp.expand_complex(sp.I*(sp.exp(-sp.I*y*z)-sp.exp(sp.I*y*z)) - 2*sp.sin(y*z))) == 0)
# substitution y = k/(2 pi), z = 2 pi u:  INT sin(ku)/(e^k-1) dk = 2 pi [coth(pi u)/4 - 1/(4 pi u)]
chk("B3 change of variables maps Legendre form to the tree's form",
    sp.simplify(2 * sp.pi * (sp.coth(2 * sp.pi * u / 2) / 4 - 1 / (2 * 2 * sp.pi * u)) - RHS) == 0)
# Henrici hypotheses for phi = e^{-xz}: |phi(x+-iy)| e^{-2 pi y} = e^{-xz} e^{-2 pi y} -> 0; INT_0^oo e^{-xz}e^{-2pi y} dy = e^{-xz}/(2pi) -> 0
x = sp.symbols('x', positive=True)
h2 = sp.integrate(sp.exp(-x * z) * sp.exp(-2 * sp.pi * y), (y, 0, sp.oo))
chk("B4 Henrici growth hypotheses hold for phi = e^{-xz} (integral e^{-xz}/(2pi) -> 0 as x->oo)",
    sp.limit(h2, x, sp.oo) == 0 and sp.limit(sp.exp(-x*z-2*sp.pi*y), y, sp.oo) == 0)

# ---------- C. Taylor coefficients: RHS = SUM_j (-1)^j zeta(2j+2) u^{2j+1}, radius 1 ----------
ser = sp.series(RHS, u, 0, 10).removeO()
ok = all(sp.simplify(ser.coeff(u, 2*j+1) - (-1)**j * sp.zeta(2*j+2)) == 0 for j in range(5))
chk("C1 Taylor coeffs of RHS = (-1)^j Gamma(2j+2)zeta(2j+2)/(2j+1)! = (-1)^j zeta(2j+2)  (termwise moments)", ok)
# NOTE: sympy 1.14 sp.limit(RHS, u, 0) returns -oo, which is WRONG (a sympy defect; the series is pi^2 u/6 + O(u^3)).
# The tree never takes that limit (it takes sp.limit(g, u, 0), checked in F1).  Recorded, and checked two other ways.
lim_sym = sp.limit(RHS, u, 0)
lead = sp.series(RHS, u, 0, 3).removeO()
mp.mp.dps = 30
lim_num = mp.limit(lambda t: mp.pi/2*mp.coth(mp.pi*t) - 1/(2*t), 0)
chk("C2 RHS -> 0 as u -> 0 (series pi^2 u/6 and mpmath.limit; sympy.limit gives %s -- sympy defect)" % lim_sym,
    sp.simplify(lead - sp.pi**2*u/6) == 0 and abs(lim_num) < 1e-25)
chk("C3 RHS -> pi/2 as u -> oo", sp.limit(RHS, u, sp.oo) == sp.pi / 2)

# ---------- D. beta-scaled form, noise.py:113 ----------
lhs_b = (1 / b) * RHS.subs(u, u / b)       # INT sin(ku)/(e^{beta k}-1) dk, k -> k/beta
chk("D1 INT sin(ku)/(e^{beta k}-1) dk = (pi/2beta)coth(pi u/beta) - 1/(2u)",
    sp.simplify(lhs_b - (sp.pi / (2 * b) * sp.coth(sp.pi * u / b) - 1 / (2 * u))) == 0)

# ---------- E. numeric quadrature, 30 digits ----------
mp.mp.dps = 30
def I_num(uu):
    return mp.quad(lambda kk: mp.sin(kk * uu) / mp.expm1(kk), mp.linspace(0, 60, 31) + [mp.inf])
def R_num(uu):
    return mp.pi / 2 * mp.coth(mp.pi * uu) - 1 / (2 * uu)
worst = 0
for uu in ['0.01', '0.1', '0.5', '0.7', '1', '2', '3.7', '10']:
    uu = mp.mpf(uu)
    a, r = I_num(uu), R_num(uu)
    rel = abs(a - r) / abs(r)
    worst = max(worst, rel)
    print("     u = %-5s quad = %s  closed = %s  rel = %.2e" % (mp.nstr(uu, 4), mp.nstr(a, 22), mp.nstr(r, 22), float(rel)))
chk("E1 quadrature = closed form at 8 u in [0.01, 10] (rel < 1e-20)", worst < 1e-20, "worst %.2e" % float(worst))
uu = mp.mpf('-0.7')
chk("E2 odd in u: holds at u = -0.7 too (tree's u>0 is narrower than needed)",
    abs(I_num(uu) - R_num(uu)) < mp.mpf(10)**-20)
uc = mp.mpc('0.3', '0.5')
ic = mp.quad(lambda kk: mp.sin(kk * uc) / mp.expm1(kk), [0, 5, 20, 60, 120, mp.inf])
chk("E3 analytic continuation: holds at complex u = 0.3+0.5i (strip |Im u| < 1)",
    abs(ic - R_num(uc)) < mp.mpf(10)**-18, "|diff| = %s" % mp.nstr(abs(ic - R_num(uc)), 3))
# at Im u = 1 the integrand ~ e^{k}/(2(e^k-1)) -> 1/2, integral diverges; closed form has a pole (coth(i pi)=oo)
integrand_tail = abs(mp.sin(mp.mpf(80) * mp.mpc(0, 1)) / mp.expm1(80))
chk("E4 boundary: at u = i the integrand tends to 1/2 (not integrable) and coth(pi u) has its pole",
    abs(integrand_tail - mp.mpf('0.5')) < 1e-10)
# beta scaling numerically
bb, uu = mp.mpf('2.3'), mp.mpf('0.7')
ib = mp.quad(lambda kk: mp.sin(kk * uu) / mp.expm1(bb * kk), [0, 10, 40, mp.inf])
chk("E5 beta-scaled form numerically (beta = 2.3, u = 0.7)",
    abs(ib - (mp.pi / (2 * bb) * mp.coth(mp.pi * uu / bb) - 1 / (2 * uu))) < mp.mpf(10)**-22)

# ---------- F. the tree's use: g(u) = -(1/2pi^2) d^3/du^3 RHS = (1/2pi^2) INT k^3 cos(ku) n(k) dk ----------
g = sp.simplify(-sp.diff(RHS, u, 3) / (2 * sp.pi**2))
chk("F1 g(0) = pi^2/30", sp.simplify(sp.limit(g, u, 0) - sp.pi**2 / 30) == 0)
chk("F2 g ~ -3/(2 pi^2 u^4) at large u", sp.limit(g * u**4, u, sp.oo) == -sp.Rational(3, 2) / sp.pi**2)
gf = sp.lambdify(u, g, 'mpmath')
worst = 0
for uu in ['0.05', '0.3', '0.7', '1.5', '4']:
    uu = mp.mpf(uu)
    d = mp.quad(lambda kk: kk**3 * mp.cos(kk * uu) / mp.expm1(kk), mp.linspace(0, 80, 41) + [mp.inf]) / (2 * mp.pi**2)
    worst = max(worst, abs(gf(uu) - d) / abs(d))
chk("F3 differentiation under the integral: closed-form g = mode integral at 5 u (rel < 1e-18)", worst < 1e-18, "worst %.2e" % float(worst))
# dominated convergence for 3 derivatives: |d^3/du^3 sin(ku)| <= k^3, INT k^3/(e^k-1) = pi^4/15 < oo
dom = sp.summation(sp.integrate(k**3 * sp.exp(-n * k), (k, 0, sp.oo)), (n, 1, sp.oo))   # Tonelli, positive terms
chk("F4 dominating function k^3/(e^k-1) integrable, INT = 6 zeta(4) = pi^4/15", sp.simplify(dom - sp.pi**4 / 15) == 0, str(dom))
# independent READ route: Ramanujan Entry 8.2 (2112.09819 p.16), w = 4:
#   SUM n^3 e^{-nz} = 6 z^{-4} + 2 INT y^3 cos(2pi - zy)/(e^{2pi y}-1) dy
# => INT_0^oo k^3 cos(ku)/(e^k-1) dk = (2pi)^4 * (1/2)[SUM n^3 e^{-2 pi n u} - 6/(2 pi u)^4]
q = sp.symbols('q', positive=True)
gen = q / (1 - q)                                   # SUM_{n>=1} q^n, |q| < 1
for _ in range(3):
    gen = sp.simplify(q * sp.diff(gen, q))          # (q d/dq)^3 -> SUM n^3 q^n
chk("F5a SUM n^3 q^n = q(1+4q+q^2)/(1-q)^4", sp.simplify(gen - q*(1+4*q+q**2)/(1-q)**4) == 0)
lhs82 = gen.subs(q, sp.exp(-z))
e82 = (2 * sp.pi)**4 / 2 * (lhs82 - 6 / z**4)
e82 = e82.subs(z, 2 * sp.pi * u) / (2 * sp.pi**2)
chk("F5 Entry 8.2 (w = 4) reproduces the tree's g(u) exactly (independent READ route)",
    sp.simplify((e82 - g).rewrite(sp.exp)) == 0)
# tree's CONTROL (noise.py:1030-1032) at u = 0.7, 20 dps, tolerance 1e-15
mp.mp.dps = 20
uu = mp.mpf('0.7')
direct = mp.quad(lambda kk: kk**3 * mp.cos(kk * uu) / (mp.exp(kk) - 1), [0, mp.inf]) / (2 * mp.pi**2)
rel = abs(gf(uu) - direct) / abs(direct)
chk("F6 tree's own CONTROL reproduced (u = 0.7, dps 20, tol 1e-15)", rel < 1e-15, "rel %.2e, g(0.7) = %s" % (float(rel), mp.nstr(gf(uu), 15)))

print("\n%d failure(s)" % len(FAIL))
sys.exit(1 if FAIL else 0)
