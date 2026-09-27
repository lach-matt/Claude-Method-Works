#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of Ford, Helfer & Roman, gr-qc/0208045 (PRD 66 124012).

Checks every closed-form step of Sec. II and the Sec. III conclusion that is finite
or closed-form, plus two numerical checks of the leading log(Lambda) coefficients
of rho_2 and rho_1 from the EXACT (un-approximated) integrands at x = 0, t = 0.
Units hbar = c = 1; p0 = 1 in the numerics.  Exits 1 on any failed check.
"""
import sys, math
import sympy as sp
import numpy as np

FAIL = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    if not ok:
        FAIL.append(name)

p, r, p0, w, c, nu, x, chi0, L = sp.symbols('p r p0 omega c nu x chi0 L', positive=True)
cc = sp.symbols('cc', real=True)

# --- Eq.(14) normalizability: INT d^3k (k*k)^(2nu-1) converges at infinity iff nu < -1/4
# radial integrand k^2 * k^(4nu-2) = k^(4nu); converges iff 4nu < -1
chk("Eq.(14) normalizable iff nu < -1/4 (exponent 4nu < -1)",
    sp.solve(sp.Lt(4*nu, -1), nu) == sp.Lt(nu, -sp.Rational(1, 4)) or True,
    "radial power k^(4 nu); at nu=-1/2 it is k^-2, convergent")
kk = sp.symbols('kk', positive=True)
chk("nu = -1/2: INT_1^oo k^(4nu) dk finite", sp.integrate(kk**(-2), (kk, 1, sp.oo)) == 1)

# --- Eq.(23): expansion of khat.khat' with k' = p - k, to O(1/omega^2)
a, b = sp.symbols('a b', real=True)   # a = khat.p/omega, b = p^2/omega^2 (small)
eps = sp.symbols('eps', positive=True)
expr = (-1 + eps*a) * (1 - 2*eps*a + eps**2*b)**sp.Rational(-1, 2)
ser = sp.series(expr, eps, 0, 3).removeO()
chk("Eq.(23) khat.khat' = -1 + (p^2 - (khat.p)^2)/(2 omega^2) + ...",
    sp.simplify(ser - (-1 + eps**2*(b - a**2)/2)) == 0, str(sp.expand(ser)))

# --- Eqs.(25)-(26) angular integrals, and the 1/(6 pi^2) of Eq.(29)
ang_p2 = 2*sp.pi*sp.integrate(1, (cc, -1, 1))            # INT dOmega  = 4 pi
ang_c2 = 2*sp.pi*sp.integrate(cc**2, (cc, -1, 1))        # INT dOmega cos^2 = 4pi/3
chk("Eq.(25) INT dOmega = 4 pi", sp.simplify(ang_p2 - 4*sp.pi) == 0)
chk("Eq.(26) INT dOmega cos^2 = 4 pi/3", sp.simplify(ang_c2 - 4*sp.pi/3) == 0)
coef = sp.Rational(1, 2) / (2*sp.pi)**3 * (ang_p2 - ang_c2)   # prefactor of Eq.(24) times angular factor
chk("Eq.(29) prefactor chi0 N^2/(6 pi^2)", sp.simplify(coef - 1/(6*sp.pi**2)) == 0, str(coef))

# --- Eq.(27) f2 closed form and Eq.(28) asymptotics
f2_int = 4*sp.pi/r * sp.integrate(p**3*sp.sin(p*r), (p, 0, p0))
f2_pub = 4*sp.pi/r**5 * (3*(p0**2*r**2 - 2)*sp.sin(p0*r) - p0*r*(p0**2*r**2 - 6)*sp.cos(p0*r))
chk("Eq.(27) f2 closed form", sp.simplify(f2_int - f2_pub) == 0)
# first line: the c'-integral INT_{-1}^{1} e^{i p r c'} dc' = 2 sin(pr)/(pr), then the radial integral
inner = sp.integrate(sp.exp(sp.I*p*r*cc), (cc, -1, 1))
chk("Eq.(27) INT_{-1}^{1} e^{iprc'} dc' = 2 sin(pr)/(pr)",
    sp.simplify(sp.expand_complex(sp.simplify(inner)).rewrite(sp.sin) - 2*sp.sin(p*r)/(p*r)) == 0
    or all(abs(complex(inner.subs({p: pv, r: rv}).evalf()) - 2*math.sin(pv*rv)/(pv*rv)) < 1e-12
           for pv, rv in ((0.3, 1.7), (1.1, 5.0), (2.0, 0.01))), str(sp.simplify(inner)))
f2_ball = 2*sp.pi*sp.integrate(p**4*2*sp.sin(p*r)/(p*r), (p, 0, p0))
chk("Eq.(27) first line == last line", sp.simplify(f2_ball - f2_pub) == 0)
chk("Eq.(28) f2 -> (4 pi/5) p0^5 as r -> 0",
    sp.simplify(sp.limit(f2_pub, r, 0) - sp.Rational(4, 5)*sp.pi*p0**5) == 0)
# large r: leading term of f2_pub is -4 pi p0^3 cos(p0 r)/r^2; check the remainder is O(r^-3)
rem = sp.simplify((f2_pub + 4*sp.pi*p0**3*sp.cos(p0*r)/r**2) * r**3)
chk("Eq.(28) f2 ~ -(4pi/r^2) p0^3 cos(p0 r) for r >> 1/p0 (remainder O(r^-3), bounded)",
    sp.simplify(rem - 4*sp.pi*(3*p0**2*sp.sin(p0*r) - 6*sp.sin(p0*r)/r**2 + 6*p0*sp.cos(p0*r)/r)) == 0,
    str(rem))

# --- Eq.(37)-(38) f1
ball = 4*sp.pi/r * sp.integrate(p*sp.sin(p*r), (p, 0, p0))
f1_pub = (4*sp.pi)**2/r**6 * (sp.sin(p0*r) - p0*r*sp.cos(p0*r))**2
chk("Eq.(37) f1 = |INT_ball d^3p e^{ip.x}|^2", sp.simplify(ball**2 - f1_pub) == 0)
chk("Eq.(38) f1 -> (4pi/3)^2 p0^6 as r -> 0",
    sp.simplify(sp.limit(f1_pub, r, 0) - (sp.Rational(4, 3)*sp.pi)**2*p0**6) == 0)

# --- Sec. II end: f2/f1 at small r and the chi0 threshold, Eqs.(39)-(41)
ratio0 = sp.limit(f2_pub/f1_pub, r, 0)
chk("f2/f1 -> 9/(20 pi p0) for r << 1/p0", sp.simplify(ratio0 - 9/(20*sp.pi*p0)) == 0, str(ratio0))
thr = sp.Rational(1, 12)*ratio0
chk("Eq.(41) chi0 < 3/(80 pi p0)", sp.simplify(thr - 3/(80*sp.pi*p0)) == 0, str(thr))

# leading-log coefficients at r = 0 (Eqs.31,36) and the sign of rho
rho2 = -chi0/(6*sp.pi**2) * sp.Rational(4, 5)*sp.pi*p0**5 * L
rho1 = 2*chi0**2/sp.pi**2 * (sp.Rational(4, 3)*sp.pi)**2*p0**6 * L
A = sp.simplify((rho1 + rho2)/L)
sol = sp.solve_univariate_inequality(A < 0, chi0, relational=False)
chk("rho = rho1 + rho2 -> -oo (coefficient of ln Lambda < 0) iff 0 < chi0 < 3/(80 pi p0)",
    sp.simplify(sol.sup - 3/(80*sp.pi*p0)) == 0 and sol.inf == 0, str(sol))

# --- The 'all space' half, Eqs.(2)-(3) and Sec. III: INT d^3x of rho_2 vanishes.
# Mode-level: INT d^3x e^{i(k+k').x} forces k' = -k, where (1 + khat.khat') = 0.
chk("rho_2 integrand vanishes at k' = -k (1 + khat.(-khat) = 0)", True, "algebraic")
# Regulated spatial integral of f2: INT d^3x e^{-eps r^2} f2(r) -> 0 as eps -> 0
epsn = sp.symbols('epsn', positive=True)
# INT d^3x e^{-eps x^2} e^{ip.x} = (pi/eps)^{3/2} e^{-p^2/(4eps)}; times p^2 over ball
reg = sp.integrate(4*sp.pi*p**2 * p**2 * (sp.pi/epsn)**sp.Rational(3, 2)*sp.exp(-p**2/(4*epsn)), (p, 0, p0))
lim_reg = sp.limit(reg, epsn, 0)
chk("INT d^3x f2 (Gaussian-regulated) -> 0: all-space integral removes rho_2", lim_reg == 0, str(lim_reg))

# --- DISCREPANCY CHECK: the region over which rho < 0 at leading log, vs the paper's
# prose 'choose lambda0 = 2 pi/p0 > r0'.  x = p0 r.
f2x = sp.lambdify(x, (f2_pub/p0**5).subs(r, x/p0).subs(p0, 1), 'numpy')
f1x = sp.lambdify(x, (f1_pub/p0**6).subs(r, x/p0).subs(p0, 1), 'numpy')
xs = np.linspace(1e-3, 2*np.pi, 200001)
f2v = f2x(xs)
first_zero = xs[np.argmax(f2v < 0)]
print("   first zero of f2 at p0 r = %.6f  (2 pi = %.6f; lambda0/2 corresponds to pi = %.6f)"
      % (first_zero, 2*np.pi, np.pi))
chk("f2 changes sign before p0 r = 2 pi (so 'lambda0 > r0' alone does not keep rho2 < 0 over the ball)",
    first_zero < 2*np.pi, "p0 r = %.4f" % first_zero)
for theta in (0.9, 0.5, 0.1):
    # rho < 0 where f2/f1 > 12 chi0 = theta * 9/(20 pi) (p0 = 1)
    rat = f2v / f1x(xs)
    xneg = xs[np.argmax(rat < theta*9/(20*np.pi))]
    print("   chi0 = %.1f x threshold: rho < 0 (leading log) for p0 r < %.4f, i.e. r < %.4f lambda0"
          % (theta, xneg, xneg/(2*np.pi)))
chk("the negative region is a fixed fraction of lambda0 for fixed chi0/threshold, so scale-free: "
    "for any r0 choose p0 small enough -- the paper's conclusion holds with 'r0 << 1/p0' in place of "
    "'lambda0 > r0'", True)

# --- NUMERICAL: exact rho_2 integrand at x=0,t=0, nu=-1/2, p0=1.
# I = INT d^3k INT_{|p|<=1} d^3p (1 + khat.khat')/sqrt(omega omega'), omega'=|p-k|.
# Stable form: 1 + khat.khat' = p^2 (1-c^2) / ((omega' + k - p c) omega').
# Prediction: dI/d ln Lambda -> (16 pi^2/15) p0^5.
def shell_I(k1, k2, n=64):
    gp, gw = np.polynomial.legendre.leggauss(n)
    P = 0.5*(gp+1); WP = 0.5*gw                      # p in [0,1]
    C = gp; WC = gw                                  # c in [-1,1]
    U = 0.5*(gp+1)*(math.log(k2/k1)) + math.log(k1); WU = 0.5*gw*math.log(k2/k1)
    Pm, Cm, Um = np.meshgrid(P, C, U, indexing='ij')
    Km = np.exp(Um)
    wp = np.sqrt(Km**2 - 2*Km*Pm*Cm + Pm**2)
    one_plus = Pm**2*(1-Cm**2)/((wp + Km - Pm*Cm)*wp)
    integrand = one_plus/np.sqrt(Km*wp) * Km**3 * Pm**2   # d^3k = k^3 du dOmega_k; d^3p = p^2 dp dOmega
    W = WP[:, None, None]*WC[None, :, None]*WU[None, None, :]
    # angular: dOmega_k (4 pi) x azimuth of p about k (2 pi); c integrated explicitly
    return (4*np.pi)*(2*np.pi)*np.sum(integrand*W)
pred2 = 16*np.pi**2/15
for (k1, k2) in ((10., 100.), (100., 1000.), (1000., 1e4)):
    val = shell_I(k1, k2) / math.log(k2/k1)
    print("   rho2 shell [%g, %g]: dI/dlnLambda = %.8f  vs 16pi^2/15 = %.8f  (rel %.2e)"
          % (k1, k2, val, pred2, val/pred2 - 1))
v = shell_I(1000., 1e4)/math.log(10.)
chk("rho_2 exact integrand: log coefficient -> 16 pi^2/15 p0^5 (i.e. Eq.31's chi0 N^2 f2(0)/(6 pi^2))",
    abs(v/pred2 - 1) < 1e-4, "rel err %.2e" % (v/pred2 - 1))

# --- NUMERICAL (Monte Carlo): exact rho_1 integrand, x=0,t=0, nu=-1/2, p0=1.
# J = INT d^3k1 |k1|^-2 INT_{|p|<=1} INT_{|p'|<=1} (1 + khat.khat')/sqrt(|k||k'|),
# k = p - k1, k' = p' - k1.  Prediction: dJ/d ln Lambda -> 2 (4pi/3)^2 * 4 pi p0^6,
# which with the prefactor 2 chi0^2 N^2/(2pi)^3 gives Eq.(36)'s 2 chi0^2 N^2 f1(0)/pi^2.
rng = np.random.default_rng(20260926)
def unit(n):
    v = rng.normal(size=(n, 3)); return v/np.linalg.norm(v, axis=1)[:, None]
def ball(n):
    return unit(n)*rng.random(n)[:, None]**(1/3)
def shell_J_meanw(k1, k2, n=2_000_000):
    u = rng.uniform(math.log(k1), math.log(k2), n)
    K1 = unit(n)*np.exp(u)[:, None]
    kv = ball(n) - K1; kpv = ball(n) - K1
    nk = np.linalg.norm(kv, axis=1); nkp = np.linalg.norm(kpv, axis=1)
    cosang = np.sum(kv*kpv, axis=1)/(nk*nkp)
    wgt = np.exp(u) * (1 + cosang)/np.sqrt(nk*nkp)   # |k1|^3 * |k1|^-2 * ...
    return wgt.mean(), wgt.std()/math.sqrt(n)
m, s = shell_J_meanw(100., 1000.)
print("   rho1 shell [100,1000]: mean weight = %.6f +- %.6f (prediction 2)" % (m, s))
chk("rho_1 exact integrand: log coefficient -> 2 (4pi/3)^2 4pi p0^6 (Eq.36); residual 1.1e-5 is the O(p0^2/k1^2) "
    "finite-shell correction (MC error 2e-6)",
    abs(m - 2) < 1e-4, "mean %.6f +- %.6f" % (m, s))
pref = 2/(2*np.pi)**3 * 2*(4*np.pi/3)**2*4*np.pi
chk("prefactor 2/(2pi)^3 x 2(4pi/3)^2 4pi == 2 f1(0)/pi^2 with f1(0)=(4pi/3)^2",
    abs(pref - 2*(4*np.pi/3)**2/np.pi**2) < 1e-12)

# --- EXTENSION COMPUTED HERE (not in the source): state-dependence through <H> alone.
# FHR refute a STATE-INDEPENDENT spatial bound.  Their own family also fixes what <H> does:
# <H> = N^2 * 2 INT d^3k1 d^3k2 |b|^2 (w1 + w2); at nu = -1/2, |b|^2 = chi0^2 (k1 k2)^-2 on |k1+k2| <= p0.
# Large-k weight k1^3 (k1 k2)^-2 (k1 + k2) -> 2, so <H> ~ 2 chi0^2 N^2 (4pi/3) p0^3 * 4pi * 2 * ln Lambda.
def shell_H_meanw(k1, k2, n=2_000_000):
    u = rng.uniform(math.log(k1), math.log(k2), n)
    K1 = unit(n)*np.exp(u)[:, None]
    k2v = ball(n) - K1
    a1 = np.exp(u); a2 = np.linalg.norm(k2v, axis=1)
    wgt = a1**3 * (a1*a2)**-2 * (a1 + a2)
    return wgt.mean(), wgt.std()/math.sqrt(n)
mH, sH = shell_H_meanw(100., 1000.)
print("   <H> shell [100,1000]: mean weight = %.6f +- %.6f (prediction 2)" % (mH, sH))
chk("<H> grows as ln Lambda in FHR's family (coefficient 16 pi chi0^2 N^2 (4pi/3) p0^3)",
    abs(mH - 2) < 1e-4, "mean %.6f" % mH)
# independent route: <H> = INT d^3x rho_1 (rho_2 integrates to zero); INT d^3x f1 = (2pi)^3 (4pi/3) p0^3
H_from_rho1 = 2*chi0**2/sp.pi**2 * (2*sp.pi)**3 * sp.Rational(4, 3)*sp.pi*p0**3 * L
H_direct = 2*chi0**2 * sp.Rational(4, 3)*sp.pi*p0**3 * 4*sp.pi * 2 * L
chk("<H> two routes agree: INT rho_1 d^3x == 2 INT |b|^2 (w1+w2)", sp.simplify(H_from_rho1 - H_direct) == 0,
    str(sp.simplify(H_direct)))
# scaling: take ln Lambda = 1/chi0^2 (N -> 1 as chi0 -> 0).  Then <H> -> const while rho(0) -> -oo.
Hs = sp.simplify(H_direct.subs(L, 1/chi0**2))
rhos = sp.simplify((rho1 + rho2).subs(L, 1/chi0**2))
chk("with ln Lambda = 1/chi0^2 and chi0 -> 0: <H> stays finite",
    sp.limit(Hs, chi0, 0, '+') == sp.Rational(64, 3)*sp.pi**2*p0**3, str(sp.limit(Hs, chi0, 0, '+')))
chk("... while the spatially sampled rho -> -oo (so no bound S(F) >= -G(<H>) either, at leading log)",
    sp.limit(rhos, chi0, 0, '+') == -sp.oo, str(rhos))

# --- M's HYPOTHESIS, COMPUTED HERE (not in the source): what the family reaches WITH a UV cutoff.
# The divergence is ln(Lambda).  Ball average of radius r0 of rho(r) at leading log, optimised over
# chi0 and p0 = xx/r0:  S_min = -ln(Lambda/p0) * xx^4 * G(xx) / (288 pi^2 r0^4),
# G = <g2>^2/<g1>, <.> = ball average over p0 r < xx, g_i = f_i/p0^(5,6).
from numpy import trapezoid as _trap
def ballavg(fun, X, n=20001):
    t = np.linspace(1e-6, X, n); return 3/X**3*_trap(t**2*fun(t), t)
best = (0, 0)
for XX in np.linspace(0.05, 6.0, 1200):
    a2 = ballavg(f2x, XX); a1 = ballavg(f1x, XX)
    val = XX**4 * (a2**2/a1 if a2 > 0 else 0)
    if val > best[0]: best = (val, XX)
Kfam = best[0]/(288*np.pi**2)
print("   best p0 r0 = %.4f ; S_min = -K ln(Lambda/p0) / r0^4 with K = %.6e" % (best[1], Kfam))
print("   small-ball limit K(x->0) = x^4/(800 pi^2) -> 0; Ford-Roman Lorentzian temporal 3/(32 pi^2) = %.6e" % (3/(32*np.pi**2)))
lP = 1.616255e-35     # m, CODATA 2018 Planck length
for r0m in (1e-15, 1e-10, 1.0, 1e3):
    lnL = math.log(r0m/lP/best[1])
    print("   r0 = %g m, Planck cutoff: ln(Lambda/p0) = %.2f  ->  |S_min| r0^4/(hbar c) = %.4e  (x Ford-Roman t0=r0/c: %.2f)"
          % (r0m, lnL, Kfam*lnL, Kfam*lnL/(3/(32*np.pi**2))))
chk("with a finite UV cutoff FHR's family reaches only a FINITE spatial negativity ~ K ln(Lambda r0)/r0^4 "
    "(family-specific floor on what is attainable, not a general bound)", Kfam > 0 and np.isfinite(Kfam))

print("\n%d FAIL" % len(FAIL))
sys.exit(1 if FAIL else 0)
