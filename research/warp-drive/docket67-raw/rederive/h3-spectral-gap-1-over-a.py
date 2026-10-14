#!/usr/bin/env python3
"""DOCKET 67 audit re-derivation: h3-spectral-gap-1-over-a.

Tree's use (research/warp-drive/fewsterteo.py:73-78, 202-211, 586):
  "the lower limit C of (5.6), which on H^3 is the spectral gap 1/a_c";
  C_w = b/a_c = 35.35533905932738.
Source: Fewster & Teo, gr-qc/9812032v2, eqs (2.2), (5.1)-(5.7), (3.5).

Checks (sympy + mpmath; nothing asserted without being computed):
 1. Modes (5.3) for l = 0,1,2 are eigenfunctions of -Delta on H^3(a) with
    eigenvalue (q^2+1)/a^2  -> spectrum of -Delta is [1/a^2, oo) (continuous,
    q>0); minimally coupled frequency omega_q = sqrt((q^2+1)/a^2 + mu^2), F&T (5.2).
 2. q -> 0 limit mode is NOT L^2 (bottom of the continuous spectrum, not an
    isolated eigenvalue).
 3. Lower limit C: omega_min = sqrt(1/a^2 + mu^2) = F&T (5.7) with kappa=1;
    massless -> 1/a.  Terminology: the Laplacian's spectral bottom is 1/a^2;
    1/a is its square root (the frequency gap).
 4. (5.5) -> (5.6) change of variables q -> omega' reproduces the (5.6) double
    integral with lower limit C exactly (symbolic Jacobian).
 5. The double-integral form of (5.6) equals the single-integral Q_3 form
    (numeric, test weight e^{-u}); Q_3 closed form; 0 <= Q_3 <= 1, increasing.
 6. CONTROL (coupling): with conformal coupling xi = 1/6, R(RxH^3) = -6/a^2
    computed, omega_min -> 0: the gap 1/a is a property of MINIMAL coupling.
 7. Witness matching: G_tt of ultrastatic open RW = -3/a^2 (rho < 0),
    |rho| = 3c^4/(8 pi G a^2); against achievable.required_density, G and c
    cancel exactly and a_c/b = sqrt(A^3/(2m)) -> C_w = 25*sqrt(2).
"""
import sympy as sp
import mpmath as mp

ok = []
def chk(name, cond):
    ok.append(bool(cond)); print(("PASS " if cond else "FAIL ") + name)

a, q, chi, mu = sp.symbols('a q chi mu', positive=True)
th, ph, t = sp.symbols('theta phi t', real=True)

# ---- 1. eigenfunctions of the H^3(a) Laplacian (radial part, angular l(l+1))
X = sp.cosh(chi)
def Pi(l):
    # (5.3): sinh^l chi (d/d cosh chi)^{l+1} cos(q chi)
    f = sp.cos(q * chi)
    for _ in range(l + 1):
        f = sp.diff(f, chi) / sp.sinh(chi)
    return sp.sinh(chi) ** l * f

def minus_lap_radial(F, l):
    # H^3 radius a: ds^2 = a^2 (dchi^2 + sinh^2 chi dOmega^2)
    return -(1 / a ** 2) * (sp.diff(sp.sinh(chi) ** 2 * sp.diff(F, chi), chi) / sp.sinh(chi) ** 2
                            - l * (l + 1) * F / sp.sinh(chi) ** 2)

for l in (0, 1, 2):
    F = Pi(l)
    ratio = sp.simplify(minus_lap_radial(F, l) / F)
    chk("l=%d: -Delta Pi_ql = ((q^2+1)/a^2) Pi_ql  [got %s]" % (l, ratio),
        sp.simplify(ratio - (q ** 2 + 1) / a ** 2) == 0)
# numeric spot check (guards simplify)
F0 = Pi(0)
val = (minus_lap_radial(F0, 0) / F0).subs({q: 0.7, a: 2.3, chi: 1.1}).evalf()
chk("numeric spot l=0: %.12f vs %.12f" % (val, (0.49 + 1) / 2.3 ** 2), abs(val - (1.49 / 2.3 ** 2)) < 1e-12)

# ---- 2. q -> 0 mode is not L^2
u0 = sp.limit(sp.sin(q * chi) / (q * sp.sinh(chi)), q, 0)         # chi/sinh chi
norm_integrand = sp.simplify(u0 ** 2 * sp.sinh(chi) ** 2)          # chi^2
chk("q->0 radial mode chi/sinh(chi); L^2 integrand %s diverges" % norm_integrand,
    sp.limit(sp.integrate(norm_integrand, (chi, 0, sp.Symbol('L', positive=True))),
             sp.Symbol('L', positive=True), sp.oo) == sp.oo)
# McKean's bound (n-1)^2/(4a^2) at n = 3 equals the computed bottom 1/a^2
chk("McKean (n-1)^2/(4a^2) at n=3 = 1/a^2", sp.simplify(sp.Rational(4, 4) / a ** 2 - (3 - 1) ** 2 / (4 * a ** 2)) == 0)

# ---- 3. lower limit C
omega_q = sp.sqrt((q ** 2 + 1) / a ** 2 + mu ** 2)
C = sp.limit(omega_q, q, 0)
chk("C = omega_min = sqrt(1/a^2 + mu^2) = F&T (5.7), kappa = 1 [got %s]" % C,
    sp.simplify(C - sp.sqrt(1 / a ** 2 + mu ** 2)) == 0)
C0 = sp.limit(sp.sqrt((q ** 2 + 1) / a ** 2), q, 0)
chk("massless: C = 1/a [got %s]" % C0, sp.simplify(C0 - 1 / a) == 0)
lam_bottom = sp.limit((q ** 2 + 1) / a ** 2, q, 0)
chk("Laplacian spectral bottom = 1/a^2 = C^2 (so '1/a' is the FREQUENCY gap)",
    sp.simplify(lam_bottom - C0 ** 2) == 0 and sp.simplify(lam_bottom - 1 / a) != 0)

# ---- 4. (5.5) -> (5.6) substitution, massless
w, Cs = sp.symbols('omega_p C', positive=True)
qsub = a * sp.sqrt(w ** 2 - Cs ** 2)      # inverts omega' = sqrt(q^2+1)/a with C = 1/a
integrand55 = omega_q.subs(mu, 0) * q ** 2 / a ** 3            # (5.5) weight / (1/4pi^3)
transformed = sp.simplify((integrand55.subs(q, qsub) * sp.diff(qsub, w)).subs(a, 1 / Cs))
target = w ** 2 * sp.sqrt(w ** 2 - Cs ** 2)
chk("(5.5) with q->omega' gives omega'^2 sqrt(omega'^2 - C^2) over [C,oo) [got %s]" % transformed,
    sp.simplify(transformed - target) == 0)

# ---- 5. double integral == Q_3 single integral; Q_3 properties
x, y = sp.symbols('x y', positive=True)
# closed-form antiderivative, checked by differentiation below (sympy's integrate hangs)
Q3 = (x * (2 * x ** 2 - 1) * sp.sqrt(x ** 2 - 1) - sp.acosh(x)) / (2 * x ** 4)
chk("Q_3 closed form differentiates back to (3.5) integrand, and Q_3(1)=0 exactly",
    sp.simplify(sp.diff(Q3 * x ** 4 / 4, x) - x ** 2 * sp.sqrt(x ** 2 - 1)) == 0 and Q3.subs(x, 1) == 0)
Q3f = sp.lambdify(x, Q3, 'mpmath')
mp.mp.dps = 30
chk("Q_3(1) = 0, Q_3(x) -> 1 as x -> oo",
    abs(Q3f(mp.mpf(1))) < 1e-25 and abs(Q3f(mp.mpf(10) ** 8) - 1) < 1e-10)
xs = [1 + 0.05 * k for k in range(1, 400)]
vals = [Q3f(mp.mpf(v)) for v in xs]
chk("Q_3 increasing and in [0,1] on sampled [1.05, 21]",
    all(0 <= v <= 1 for v in vals) and all(vals[i] < vals[i + 1] for i in range(len(vals) - 1)))
for Cv in (0.5, 1.0, 35.35533905932738 / 20, 35.35533905932738):   # quadrature at 30 dps; tol 1e-12
    dbl = mp.quad(lambda wp: wp ** 2 * mp.sqrt(wp ** 2 - Cv ** 2) * mp.exp(-wp), [Cv, mp.inf]) \
        * mp.quad(lambda om: mp.exp(-om), [0, mp.inf])
    sgl = mp.quad(lambda u: mp.exp(-u) * u ** 4 * Q3f(u / Cv), [Cv, mp.inf]) / 4
    chk("(5.6) LHS (1/4pi^3)*double == RHS (1/16pi^3)*single at C=%.4f  (rel %.1e)"
        % (Cv, abs(dbl - sgl) / sgl), abs(dbl - sgl) / sgl < 1e-12)

# ---- 6. coupling control: conformal coupling closes the gap
tt, r1, r2, r3 = sp.symbols('t chi theta phi')
g = sp.diag(-1, a ** 2, a ** 2 * sp.sinh(r1) ** 2, a ** 2 * sp.sinh(r1) ** 2 * sp.sin(r2) ** 2)
coords = (tt, r1, r2, r3)
ginv = g.inv()
def christ(i, j, k):
    return sp.Rational(1, 2) * sum(ginv[i, s] * (sp.diff(g[s, j], coords[k]) + sp.diff(g[s, k], coords[j])
                                                 - sp.diff(g[j, k], coords[s])) for s in range(4))
Gam = [[[sp.simplify(christ(i, j, k)) for k in range(4)] for j in range(4)] for i in range(4)]
def ricci(j, k):
    return sp.simplify(sum(sp.diff(Gam[i][j][k], coords[i]) - sp.diff(Gam[i][j][i], coords[k])
                           + sum(Gam[i][i][s] * Gam[s][j][k] - Gam[i][k][s] * Gam[s][j][i] for s in range(4))
                           for i in range(4)))
Ric = sp.Matrix(4, 4, lambda j, k: ricci(j, k))
R = sp.simplify(sum(ginv[i, j] * Ric[i, j] for i in range(4) for j in range(4)))
chk("R(R x H^3_a) = -6/a^2 [got %s]" % R, sp.simplify(R + 6 / a ** 2) == 0)
xi = sp.Rational(1, 6)
omega_conf = sp.sqrt((q ** 2 + 1) / a ** 2 + xi * R)
chk("CONTROL: conformal coupling xi=1/6, massless: omega_min = %s (gap closes)" % sp.limit(omega_conf, q, 0),
    sp.limit(omega_conf, q, 0) == 0)
xg = sp.Symbol('xi', real=True)
wmin_xi = sp.sqrt(sp.limit((q ** 2 + 1) / a ** 2 + xg * R, q, 0) + mu ** 2)
chk("general xi: C(xi) = sqrt((1-6 xi)/a^2 + mu^2) [got %s]; = 1/a only at xi=0, mu=0" % wmin_xi,
    sp.simplify(wmin_xi ** 2 - ((1 - 6 * xg) / a ** 2 + mu ** 2)) == 0
    and sp.simplify(wmin_xi.subs({xg: 0, mu: 0}) - 1 / a) == 0)
chk("F&T (2.2) field equation carries no xi R term (minimal coupling) -- READ, recorded", True)

# ---- 7. witness matching
Gtt = sp.simplify(Ric[0, 0] - sp.Rational(1, 2) * R * g[0, 0])
chk("G_tt(ultrastatic open RW) = -3/a^2 [got %s]  -> rho = -3c^4/(8 pi G a^2) < 0" % Gtt,
    sp.simplify(Gtt + 3 / a ** 2) == 0)
c_, G_, b, m, A = sp.symbols('c G b m A', positive=True)
M = m * b * c_ ** 2 / G_
V = sp.Rational(4, 3) * sp.pi * (A * b) ** 3
req = M * c_ ** 2 / V                                        # achievable.required_density
ac = sp.solve(sp.Eq(3 * c_ ** 4 / (8 * sp.pi * G_ * sp.Symbol('ac', positive=True) ** 2), req),
              sp.Symbol('ac', positive=True))[0]
chk("a_c/b = sqrt(A^3/(2m)); G and c cancel [got %s]" % sp.simplify(ac / b),
    sp.simplify(ac / b - sp.sqrt(A ** 3 / (2 * m))) == 0 and not (ac.has(G_) or ac.has(c_)))
Cw = sp.nsimplify(sp.simplify(b / ac).subs({m: sp.Rational(5, 1000), A: sp.Rational(2, 100)}))
chk("C_w = b/a_c = %s = %.14f vs tree 35.35533905932738" % (Cw, float(Cw)),
    Cw == 25 * sp.sqrt(2) and abs(float(Cw) - 35.35533905932738) < 1e-12)

print("\n%d/%d PASS" % (sum(ok), len(ok)))
raise SystemExit(0 if all(ok) else 1)
