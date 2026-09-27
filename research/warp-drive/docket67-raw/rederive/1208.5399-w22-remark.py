#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Fewster 1208.5399 p.10 remark -- bound (3)
   INT <T00>_w g(t)^2 dt >= -(1/16 pi^2) INT |g''|^2 dt
'remains valid if one take g to be an element of the Sobolev space W^{2,2}(R)'
('In four-dimensions'), as noise.py H4 uses it for the clamped sampler.

What is checked (finite / closed form), each with a CONTROL that must fail:
 A  (sympy) the clamped mode g = cosh - cos - s(sinh - sin): g(0)=g'(0)=0 and g(1)=0
    identically; g'(1)(sinh mu - sin mu)/mu = 2(cos mu cosh mu - 1) identically, so the
    exact mode vanishes with g' at both ends iff cos mu cosh mu = 1.
 B  (mpmath) the zero extension G of g is in W^{2,2}(R): the weak 2nd derivative is
    g''chi_[0,1] (boundary terms vanish), g'' bounded (max 2 mu^2 at the ends), and
    g''(0) != 0 so G is NOT C^2 / NOT W^{3,2}: the minimiser is exactly the case the
    W^{2,2} remark is needed for, if (4) is read as attained.  CONTROL: a non-root mu.
 C  C = mu_1^4/(16 pi^2) vs Fewster's printed 'C ~ 3.17'.
 D  Fourier side: RHS of (1) at m = 0 equals RHS of (3) for G (Parseval), and converges
    (|G^|^2 u^4 ~ u^-2).  CONTROL: a discontinuous (box) g gives a divergent RHS,
    Fewster's 'does not apply to g with lower regularity'.
 E  density: C0^oo mollifications g_eps -> G in W^{2,2}; their Rayleigh quotients
    -> mu^4 and are >= mu^4/(1+2eps)^4 (clamped eigenvalue on the longer support);
    LHS INT rho g_eps^2 -> INT rho G^2 for a smooth bounded rho.  So (3) passes to the
    compactly supported W^{2,2} limit: the remark re-derives FOR COMPACT SUPPORT.
 F  noise.py's 1e-25 boundary residual is arithmetic (it scales with working
    precision), not a jump in the exact object.
Exit 1 on any FAIL.
"""
import sys
import sympy as sp
import mpmath as mp
import numpy as np

FAILS = []


def chk(name, ok):
    print(("PASS  " if ok else "FAIL  ") + name)
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------- A (sympy)
t, m = sp.symbols('t mu', positive=True)
s = (sp.cosh(m) - sp.cos(m)) / (sp.sinh(m) - sp.sin(m))
g = sp.cosh(m * t) - sp.cos(m * t) - s * (sp.sinh(m * t) - sp.sin(m * t))
gp = sp.diff(g, t)
chk("A1 g(0) = 0 identically", sp.simplify(g.subs(t, 0)) == 0)
chk("A2 g'(0) = 0 identically", sp.simplify(gp.subs(t, 0)) == 0)
chk("A3 g(1) = 0 identically (sigma's definition)", sp.simplify(g.subs(t, 1)) == 0)
expr = sp.simplify(sp.expand(gp.subs(t, 1) * (sp.sinh(m) - sp.sin(m)) / m
                             - 2 * (sp.cos(m) * sp.cosh(m) - 1)).rewrite(sp.exp))
chk("A4 g'(1)(sinh mu - sin mu)/mu = 2(cos mu cosh mu - 1) identically", expr == 0)
g2_0 = sp.simplify(sp.diff(g, t, 2).subs(t, 0))
chk("A5 g''(0) = 2 mu^2 (nonzero: G not C^2)", sp.simplify(g2_0 - 2 * m**2) == 0)

# A6-A7: the sampling function the operator actually carries is f = G^2.  Its derivatives
# of order 0..3 vanish at the ends and f''''(0) = 6 g''(0)^2 = 24 mu^4, so f^ ~ u^-5 and the
# vacuum two-particle norm of A_tau Omega ~ INT u^7 |f^(u)|^2 du converges (u^-3): with this
# W^{2,2} root the time-smeared operator is still densely defined (context for H3, which
# this audit does not grade).
f = g**2
chk("A6 f = G^2: f, f', f'', f''' vanish at t = 0", all(sp.simplify(sp.diff(f, t, k).subs(t, 0)) == 0 for k in range(4)))
chk("A7 f''''(0) = 6 g''(0)^2 = 24 mu^4 (jump in the 4th derivative only)",
    sp.simplify(sp.diff(f, t, 4).subs(t, 0) - 24 * m**4) == 0)

# ---------------------------------------------------------------- B (mpmath)
mp.mp.dps = 50
mu1 = mp.findroot(lambda x: mp.cos(x) * mp.cosh(x) - 1, mp.mpf('4.73'))


def mk(mu):
    sg = (mp.cosh(mu) - mp.cos(mu)) / (mp.sinh(mu) - mp.sin(mu))

    def gg(x, d=0):
        f = [lambda y: mp.cosh(mu * y) - mp.cos(mu * y) - sg * (mp.sinh(mu * y) - mp.sin(mu * y)),
             lambda y: mu * (mp.sinh(mu * y) + mp.sin(mu * y) - sg * (mp.cosh(mu * y) - mp.cos(mu * y))),
             lambda y: mu**2 * (mp.cosh(mu * y) + mp.cos(mu * y) - sg * (mp.sinh(mu * y) + mp.sin(mu * y))),
             lambda y: mu**3 * (mp.sinh(mu * y) - mp.sin(mu * y) - sg * (mp.cosh(mu * y) + mp.cos(mu * y)))]
        return f[d](x)
    return gg


G = mk(mu1)
phi = lambda x: mp.exp(-(x - mp.mpf('0.3'))**2) * (1 + x)       # smooth test fn, nonzero at 0, 1
phi2 = lambda x: mp.diff(phi, x, 2)
lhs = mp.quad(lambda x: G(x) * phi2(x), [0, 0.5, 1])            # <G, phi''> (G = 0 off [0,1])
rhs = mp.quad(lambda x: G(x, 2) * phi(x), [0, 0.5, 1])          # <g'' chi, phi>
resB = abs(lhs - rhs)
print("   weak-derivative residual |<G,phi''> - <g''chi,phi>| = %s" % mp.nstr(resB, 5))
chk("B1 weak 2nd derivative of G is g''chi_[0,1] (residual < 1e-40)", resB < mp.mpf('1e-40'))
Gc = mk(mp.mpf('4.8'))                                           # CONTROL: not a clamped root
resC = abs(mp.quad(lambda x: Gc(x) * phi2(x), [0, 0.5, 1]) - mp.quad(lambda x: Gc(x, 2) * phi(x), [0, 0.5, 1]))
print("   CONTROL mu = 4.8: residual = %s  (= |g'(1) phi(1)|, a delta in G'')" % mp.nstr(resC, 5))
chk("B2 CONTROL: non-root mu leaves a boundary delta (residual > 1e-3)", resC > mp.mpf('1e-3'))
sup2 = max(abs(G(mp.mpf(i) / 2000, 2)) for i in range(2001))
print("   max|g''| on 2001 pts = %s ; 2 mu^2 = %s" % (mp.nstr(sup2, 12), mp.nstr(2 * mu1**2, 12)))
chk("B3 sup|g''| = 2 mu^2 = 44.75 (attained at the ends), < 1e3", abs(sup2 - 2 * mu1**2) < mp.mpf('1e-30') and sup2 < 1000)
chk("B4 g'''(0) != 0 as well, and g''(0) != 0 => G'' has jumps: G in W^{2,2} \\ W^{3,2}",
    abs(G(0, 2)) > 1 and abs(G(0, 3)) > 1)

# ---------------------------------------------------------------- C
N = mp.quad(lambda x: G(x)**2, [0, 0.5, 1])
R = mp.quad(lambda x: G(x, 2)**2, [0, 0.5, 1]) / N
C = mu1**4 / (16 * mp.pi**2)
print("   mu_1 = %s ; Rayleigh = %s ; mu^4 = %s ; C = %s" % (mp.nstr(mu1, 15), mp.nstr(R, 15), mp.nstr(mu1**4, 15), mp.nstr(C, 10)))
chk("C1 Rayleigh quotient INT g''^2/INT g^2 = mu_1^4 (1e-40)", abs(R - mu1**4) < mp.mpf('1e-40') * mu1**4)
chk("C2 C = mu_1^4/(16 pi^2) rounds to Fewster's printed 3.17", mp.nint(C * 100) == 317)

# ---------------------------------------------------------------- D (Fourier side, double precision)
mu = float(mu1)
sg = (np.cosh(mu) - np.cos(mu)) / (np.sinh(mu) - np.sin(mu))
a = np.array([mu, -mu, 1j * mu, -1j * mu])
c = np.array([(1 - sg) / 2, (1 + sg) / 2, -(1 + 1j * sg) / 2, -(1 - 1j * sg) / 2])
Nf = float(N)


def Ghat(u):     # INT_0^1 g(t) e^{i u t} dt, exact for the exponential sum
    u = np.asarray(u, dtype=float)[..., None]
    z = a + 1j * u
    return np.sum(c * (np.exp(z) - 1) / z, axis=-1)


U = 4000.0
u = np.linspace(1e-9, U, 4_000_001)
f = np.abs(Ghat(u))**2 * u**4
# tail: integrate by parts thrice with g = g' = 0 at ends -> Ghat ~ (g''(1)e^{iu} - g''(0))/(i u)^3 * (-1)
g2_0f, g2_1f = 2 * mu**2, float(G(1, 2))
tail_coef = g2_0f**2 + g2_1f**2              # mean of |g''(1)e^{iu}-g''(0)|^2 over oscillation
Ifour = np.trapezoid(f, u) + tail_coef / U
rhs1 = Ifour / (16 * np.pi**3) / Nf
rhs3 = float(R) / (16 * np.pi**2)
print("   (1/16pi^3) INT_0^oo |G^|^2 u^4 / N = %.10f ; (1/16pi^2) INT g''^2 / N = %.10f" % (rhs1, rhs3))
chk("D1 RHS(1) at m=0 = RHS(3) for G (Parseval, rel 1e-6)", abs(rhs1 - rhs3) < 1e-6 * rhs3)
ratio_tail = np.mean(f[-200000:] * u[-200000:]**2) / tail_coef
chk("D2 |G^|^2 u^4 ~ u^-2 at large u (tail coefficient matches g''(0), g''(1) to 1e-2)", abs(ratio_tail - 1) < 1e-2)
# CONTROL: box on [0,1]: |hat|^2 = 4 sin^2(u/2)/u^2, times u^4 grows like u^2
box = lambda uu: 4 * np.sin(uu / 2)**2 / uu**2 * uu**4
I1 = np.trapezoid(box(np.linspace(1e-9, 1000, 1_000_001)), np.linspace(1e-9, 1000, 1_000_001))
I2 = np.trapezoid(box(np.linspace(1e-9, 2000, 2_000_001)), np.linspace(1e-9, 2000, 2_000_001))
print("   CONTROL box: partial RHS integral to U=1000: %.3e, to 2000: %.3e (ratio %.2f ~ 8 = U^3)" % (I1, I2, I2 / I1))
chk("D3 CONTROL: discontinuous g -> RHS diverges like U^3", 7.5 < I2 / I1 < 8.5)

# ---------------------------------------------------------------- E (density)
h = 1e-4
tt = np.arange(-0.3, 1.3 + h / 2, h)
inside = (tt >= 0) & (tt <= 1)
gv = np.where(inside, np.real(np.sum(c * np.exp(np.outer(tt, a)), axis=1)), 0.0)
g2v = np.where(inside, np.real(np.sum(c * a**2 * np.exp(np.outer(tt, a)), axis=1)), 0.0)
rho = np.cos(5 * tt) - 0.3 * tt           # a smooth bounded stand-in for a Hadamard <T00>(t)
L0 = np.trapezoid(rho * gv**2, tt)
prev = None
defs = []
for eps in (0.1, 0.03, 0.01, 0.003, 0.001):
    k = np.arange(-eps, eps + h / 2, h)
    eta = np.where(np.abs(k) < eps, np.exp(-1.0 / np.maximum(1e-300, 1 - (k / eps)**2)), 0.0)
    eta /= eta.sum()
    ge = np.convolve(gv, eta, mode='same')
    g2e = np.convolve(g2v, eta, mode='same')        # (G*eta)'' = G''*eta since G in W^{2,2}
    Re = np.trapezoid(g2e**2, tt) / np.trapezoid(ge**2, tt)
    Le = np.trapezoid(rho * ge**2, tt)
    low = mu**4 / (1 + 2 * eps)**4
    print("   eps=%g: Rayleigh(g_eps) = %.6f  (mu^4 = %.6f, floor mu^4/(1+2eps)^4 = %.6f); LHS %.6f vs %.6f"
          % (eps, Re, mu**4, low, Le, L0))
    chk("E eps=%g Rayleigh(g_eps) >= clamped floor on its longer support" % eps, Re >= low * (1 - 1e-6))
    prev = (Re, Le)
    defs.append((mu**4 - Re) / eps)
print("   deficit (mu^4 - Rayleigh)/eps = " + ", ".join("%.1f" % d for d in defs) + "  (O(eps): g'' jumps at the ends)")
chk("E4 Rayleigh(g_eps) -> mu^4 linearly in eps (deficit/eps constant to 10%, eps=0.03..0.001)",
    max(defs[1:]) / min(defs[1:]) < 1.10 and abs(prev[0] - mu**4) < 2e-3 * mu**4)
chk("E5 LHS INT rho g_eps^2 -> INT rho G^2 (eps=0.001, rel 1e-4)", abs(prev[1] - L0) < 1e-4 * abs(L0))

# E6: approximants in C0^oo((0,1)) itself (shrink about 1/2, then mollify): the infimum of
# Fewster's p.11 Rayleigh quotient over C0^oo((0,1)) is mu^4, approached FROM ABOVE and not
# attained -- so (4) needs only density, while using the minimiser G itself as the sampler
# (noise.py C1, K_F) is what needs the W^{2,2} remark.
Rin = []
for eps in (0.03, 0.01, 0.003, 0.001):
    sc = 1 + 2.2 * eps                               # support of shrunk G: [1/2 - 1/(2sc), 1/2 + 1/(2sc)]
    x = (tt - 0.5) * sc + 0.5
    ins = (x >= 0) & (x <= 1)
    gs = np.where(ins, np.real(np.sum(c * np.exp(np.outer(x, a)), axis=1)), 0.0)
    g2s = np.where(ins, np.real(np.sum(c * a**2 * np.exp(np.outer(x, a)), axis=1)), 0.0) * sc**2
    k = np.arange(-eps, eps + h / 2, h)
    eta = np.where(np.abs(k) < eps, np.exp(-1.0 / np.maximum(1e-300, 1 - (k / eps)**2)), 0.0)
    eta /= eta.sum()
    ge = np.convolve(gs, eta, mode='same'); g2e = np.convolve(g2s, eta, mode='same')
    supp = tt[np.abs(ge) > 0]
    Ri = np.trapezoid(g2e**2, tt) / np.trapezoid(ge**2, tt)
    Rin.append(Ri)
    print("   C0^oo((0,1)) approximant eps=%g: support [%.4f, %.4f], Rayleigh = %.6f (mu^4 = %.6f)"
          % (eps, supp.min(), supp.max(), Ri, mu**4))
    chk("E6 eps=%g support inside (0,1) and Rayleigh >= mu^4" % eps,
        supp.min() > 0 and supp.max() < 1 and Ri >= mu**4 * (1 - 1e-9))
chk("E7 C0^oo((0,1)) Rayleigh quotients decrease to mu^4 (eps=0.001, rel 1e-2)",
    Rin[0] > Rin[1] > Rin[2] > Rin[3] and abs(Rin[3] - mu**4) < 1e-2 * mu**4)

# ---------------------------------------------------------------- F (noise.py's residual)
res = []
for dps in (30, 50):
    mp.mp.dps = dps
    r = mp.findroot(lambda x: mp.cos(x) * mp.cosh(x) - 1, mp.mpf('4.73'))
    Gd = mk(r)
    bc = max(abs(v) for v in (Gd(0), Gd(0, 1), Gd(1), Gd(1, 1)))
    res.append(bc)
    print("   dps=%d: boundary residual %s" % (dps, mp.nstr(bc, 3)))
chk("F1 residual shrinks with precision (arithmetic, not a jump in the exact mode)",
    res[1] < res[0] * mp.mpf('1e-15'))

print("\n%d FAIL" % len(FAILS))
sys.exit(1 if FAILS else 0)
