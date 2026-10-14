#!/usr/bin/env python3
r"""DOCKET 67 -- re-derivation for key fewster-teo-5.6-spectral-gap-bound.

Independent of research/warp-drive/fewsterteo.py's code (it re-implements
everything in sympy + mpmath at 30 dps; it imports NOTHING from the tree except
-- in part F only, read-only, bytecode writing disabled -- achievable.py's
demand, to recompute the tree's own witness gap).

  A. H^3 (radius a) heat kernel: sympy verifies it solves the heat equation;
     its coincidence limit is the flat one times exp(-t/a^2), so the local
     spectral density of -Laplacian on H^3 is sqrt(lam - 1/a^2)/(4 pi^2),
     the flat density shifted by the gap 1/a^2.
  B. From that density, the Fewster-Eveson counting INT_{omega<=u} omega dN
     gives (u^4/8pi^2) Q_3(u/C) with C = 1/a, and Q_3 closed form = the
     tree's; so a massless minimally coupled field on R x H^3 has exactly the
     flat MASSIVE (m = 1/a) bound -- the structure the tree's ratio() encodes.
  C. Parseval + clamping: INT_0^oo u^4|ghat|^2 du = pi INT (g'')^2 = pi mu^4,
     and (1/16pi^3) of it = mu^4/(16 pi^2).
  D. ratio(C) re-measured at 30 dps (mpmath) against every fixture the tree pins.
  E. inf spec = 0 on any slice containing arbitrarily large (nearly) flat balls:
     Rayleigh quotient of a scaled bump ~ const/R^2 (sympy).
  F. the witness gap C = b/a_c recomputed from achievable.py's demand.
"""
import math
import os
import sys

import mpmath as mp
import sympy as sp

OK = True


def rep(label, good, detail=""):
    global OK
    OK &= bool(good)
    print("  [%s] %s %s" % ("ok" if good else "XX", label, detail))


# ---------------------------------------------------------------- A
print("A. H^3 heat kernel and local spectral density")
t, a, rho, lam = sp.symbols('t a rho lambda', positive=True)
K = (4 * sp.pi * t) ** sp.Rational(-3, 2) * (rho / a) / sp.sinh(rho / a) \
    * sp.exp(-t / a ** 2 - rho ** 2 / (4 * t))
lapK = sp.diff(K, rho, 2) + (2 / a) * sp.cosh(rho / a) / sp.sinh(rho / a) * sp.diff(K, rho)
res = sp.simplify((sp.diff(K, t) - lapK) / K)
rep("H^3 kernel solves dK/dt = Lap_H3 K (radial)", res == 0, "residual/K = %s" % res)
K0 = sp.limit(K, rho, 0)
rep("coincidence limit = (4 pi t)^(-3/2) exp(-t/a^2)",
    sp.simplify(K0 - (4 * sp.pi * t) ** sp.Rational(-3, 2) * sp.exp(-t / a ** 2)) == 0, str(K0))
C = sp.Symbol('C', positive=True)
dens = sp.sqrt(lam - C ** 2) / (4 * sp.pi ** 2)
lap_tr = sp.integrate(dens * sp.exp(-t * lam), (lam, C ** 2, sp.oo))
rep("density sqrt(lam - C^2)/(4 pi^2) Laplace-transforms to that limit (C = 1/a)",
    sp.simplify(lap_tr - (4 * sp.pi * t) ** sp.Rational(-3, 2) * sp.exp(-t * C ** 2)) == 0,
    str(sp.simplify(lap_tr)))

# F&T (5.4) sum rule SUM |Pi Y|^2 = q^2/(2 pi^2) with (5.2) U = (2 w a^3)^(-1/2) Pi Y, w^2 = (q^2+1)/a^2:
# per unit proper volume the density in k = q/a is k^2/(2 pi^2) dk, lam = k^2 + 1/a^2 -> sqrt(lam - 1/a^2)/(4 pi^2) dlam
q_ = sp.Symbol('q', positive=True)
dens_54 = (q_ ** 2 / (2 * sp.pi ** 2)) / a ** 3            # per dq, per unit proper volume
lam_q = (q_ ** 2 + 1) / a ** 2
dens_from_54 = sp.simplify(dens_54 / sp.diff(lam_q, q_))     # per dlam
rep("F&T (5.4)+(5.2) sum rule gives the heat-kernel density sqrt(lam - 1/a^2)/(4 pi^2)",
    sp.simplify(dens_from_54 - dens.subs(C, 1 / a).subs(lam, lam_q)) == 0, str(dens_from_54))

# coupling: Ricci scalar of the static open RW spacetime R x H^3(a), computed from the metric
ch, th, ph, tt = sp.symbols('chi theta phi t', positive=True)
X = [tt, ch, th, ph]
gm = sp.diag(-1, a ** 2, a ** 2 * sp.sinh(ch) ** 2, a ** 2 * sp.sinh(ch) ** 2 * sp.sin(th) ** 2)
gi = gm.inv()
Gam = [[[sum(gi[i, l] * (sp.diff(gm[l, j], X[k]) + sp.diff(gm[l, k], X[j]) - sp.diff(gm[j, k], X[l]))
             for l in range(4)) / 2 for k in range(4)] for j in range(4)] for i in range(4)]
Ric = sp.zeros(4)
for j in range(4):
    for k in range(4):
        Ric[j, k] = sp.simplify(sum(sp.diff(Gam[i][j][k], X[i]) - sp.diff(Gam[i][j][i], X[k])
                                    + sum(Gam[i][i][l] * Gam[l][j][k] - Gam[i][k][l] * Gam[l][j][i]
                                          for l in range(4)) for i in range(4)))
Rs = sp.simplify(sum(gi[j, k] * Ric[j, k] for j in range(4) for k in range(4)))
rep("Ricci scalar of R x H^3(a) = -6/a^2 (computed)", sp.simplify(Rs + 6 / a ** 2) == 0, str(Rs))
xi = sp.Symbol('xi')
gap2 = sp.simplify(1 / a ** 2 + xi * Rs)
rep("gap^2 = 1/a^2 + xi R: minimal (xi = 0) -> 1/a^2; conformal (xi = 1/6) -> 0",
    gap2.subs(xi, 0) == 1 / a ** 2 and sp.simplify(gap2.subs(xi, sp.Rational(1, 6))) == 0, str(gap2))

# ---------------------------------------------------------------- B
print("B. Fewster-Eveson counting with the H^3 density -> Q_3(u/C)")
w, u, y, x = sp.symbols('omega u y x', positive=True)
# dN = dens(lam) dlam, lam = omega^2 -> dens * 2 omega domega
# count(u) = INT_C^u dens(w^2) 2w * w dw; symbolic integrand, numeric integral.
integrand = sp.simplify(dens.subs(lam, w ** 2) * 2 * w * w)
rep("H^3 count integrand = w^2 sqrt(w^2 - C^2)/(2 pi^2)",
    sp.simplify(integrand - w ** 2 * sp.sqrt(w ** 2 - C ** 2) / (2 * sp.pi ** 2)) == 0, str(integrand))
flat = sp.integrate(w ** 3 / (2 * sp.pi ** 2), (w, 0, u))
rep("flat count = u^4/(8 pi^2)", sp.simplify(flat - u ** 4 / (8 * sp.pi ** 2)) == 0, str(flat))
Q3_tree = (x * (2 * x ** 2 - 1) * sp.sqrt(x ** 2 - 1) - sp.acosh(x)) / (2 * x ** 4)
anti = (y * (2 * y ** 2 - 1) * sp.sqrt(y ** 2 - 1) - sp.acosh(y)) / 8
rep("d/dy[(y(2y^2-1)sqrt(y^2-1) - acosh y)/8] = y^2 sqrt(y^2-1); = 0 at y = 1",
    sp.simplify(sp.diff(anti, y) - y ** 2 * sp.sqrt(y ** 2 - 1)) == 0
    and sp.simplify(anti.subs(y, 1)) == 0)
mp.mp.dps = 30
Cn = mp.mpf('0.37')
for xv in ('1.5', '2', '7', '40'):
    xm = mp.mpf(xv)
    cnt = mp.quad(lambda ww: ww ** 2 * mp.sqrt(ww ** 2 - Cn ** 2) / (2 * mp.pi ** 2), [Cn, xm * Cn])
    fl = (xm * Cn) ** 4 / (8 * mp.pi ** 2)
    v2 = mp.mpf(str(sp.N(Q3_tree.subs(x, sp.Rational(xv)), 35)))
    rep("x = %s: numeric H^3 count / flat count = tree's Q_3 closed form" % xv,
        abs(cnt / fl - v2) < mp.mpf(10) ** -20, mp.nstr(cnt / fl, 15))
rep("Q_3(x) -> 1 as x -> oo", sp.limit(Q3_tree, x, sp.oo) == 1)
Q3_log = Q3_tree.subs(sp.acosh(x), sp.log(x + sp.sqrt(x ** 2 - 1)))
lim2 = sp.limit(x ** 2 * (1 - Q3_log), x, sp.oo)
rep("x^2 (1 - Q_3(x)) -> 1 (so 1 - Q_3(u/C) ~ C^2/u^2: the tail used in D)", lim2 == 1, str(lim2))

# ---------------------------------------------------------------- C, D
print("C/D. sampler, Parseval, ratio(C) at 30 dps")
mp.mp.dps = 30
MU = mp.findroot(lambda m: mp.cos(m) * mp.cosh(m) - 1, mp.mpf('4.73'))
SG = (mp.cosh(MU) - mp.cos(MU)) / (mp.sinh(MU) - mp.sin(MU))


def g(tt):
    return mp.cosh(MU * tt) - mp.cos(MU * tt) - SG * (mp.sinh(MU * tt) - mp.sin(MU * tt))


def g2(tt):
    return MU ** 2 * (mp.cosh(MU * tt) + mp.cos(MU * tt) - SG * (mp.sinh(MU * tt) + mp.sin(MU * tt)))


NRM = mp.quad(lambda tt: g(tt) ** 2, [0, 0.5, 1])
I2 = mp.quad(lambda tt: g2(tt) ** 2, [0, 0.5, 1])
rep("INT g^2 = 1 (clamped mode)", abs(NRM - 1) < mp.mpf(10) ** -25, mp.nstr(NRM, 20))
rep("INT (g'')^2 = mu^4 INT g^2", abs(I2 / NRM - MU ** 4) < mp.mpf(10) ** -20, mp.nstr(I2 / NRM, 20))
# FT(g'') via the four exponentials of g'' (written out here, not imported)
EX = [(MU, (1 - SG) / 2), (-MU, (1 + SG) / 2), (1j * MU, (1 + 1j * SG) / 2 * -1 * -1),
      (-1j * MU, (1 - 1j * SG) / 2)]
# check the exponential form reproduces g'' before trusting it
def g2_exp(tt):
    s = mp.mpc(0)
    for ak, ck in EX:
        s += ck * ak ** 2 / MU ** 2 * mp.exp(ak * tt)
    return (MU ** 2 * s).real
# g'' / mu^2 = cosh + cos - sg(sinh + sin):  coefficients of e^{+mu t}, e^{-mu t}, e^{i mu t}, e^{-i mu t}
EX = [(MU, (1 - SG) / 2), (-MU, (1 + SG) / 2), (1j * MU, (1 + 1j * SG) / 2), (-1j * MU, (1 - 1j * SG) / 2)]


def g2_exp(tt):
    s = mp.mpc(0)
    for ak, ck in EX:
        s += ck * mp.exp(ak * tt)
    return (MU ** 2 * s).real


rep("exponential form of g'' matches direct g''",
    max(abs(g2_exp(tt) - g2(tt)) for tt in (0, 0.3, 0.77, 1)) < mp.mpf(10) ** -24)


def F2(uu):
    """|INT_0^1 g''(t) e^{-i u t} dt|^2 / INT g^2."""
    s = mp.mpc(0)
    for ak, ck in EX:
        z = ak - 1j * uu
        s += ck * (mp.exp(z) - 1) / z
    s *= MU ** 2
    return (s.real ** 2 + s.imag ** 2) / NRM


# spot check against direct quadrature of the transform
for uu in (mp.mpf('0.7'), mp.mpf(13), mp.mpf(101)):
    d = mp.quad(lambda tt: g2(tt) * mp.exp(-1j * uu * tt), mp.linspace(0, 1, 12))
    rep("FT(g'') closed form = quadrature at u = %s" % uu,
        abs((d.real ** 2 + d.imag ** 2) / NRM - F2(uu)) < mp.mpf(10) ** -20)

A2 = (g2(0) ** 2 + g2(1) ** 2) / NRM          # |FT g''|^2 -> A2/u^2 on average
B2 = 2 * g2(0) * g2(1) / NRM                  # ... minus B2 cos(u)/u^2


def tail0(U):
    """INT_U^oo (A2 - B2 cos u)/u^2 du, exact in Si: the large-u form of |FT g''|^2
    (the 1/u^3 cross term has no non-oscillating part; residual O(U^-3))."""
    cos_int = mp.cos(U) / U - (mp.pi / 2 - mp.si(U))
    return A2 / U - B2 * cos_int
UMAX = mp.mpf(2000)


def integ(f, lo, hi, step=2 * mp.pi):
    n = int(mp.ceil((hi - lo) / step))
    pts = [lo + (hi - lo) * k / n for k in range(n + 1)]
    return mp.quad(f, pts)


def Q3n(xx):
    if xx <= 1:
        return mp.mpf(0)
    return (xx * (2 * xx ** 2 - 1) * mp.sqrt(xx ** 2 - 1) - mp.acosh(xx)) / (2 * xx ** 4)


mp.mp.dps = 20
PAR = integ(F2, 0, UMAX) + tail0(UMAX)
rep("Parseval: INT_0^oo |FT g''|^2 = pi mu^4 (quad to 2000 + exact Si tail)",
    abs(PAR / (mp.pi * MU ** 4) - 1) < 1e-8, "rel %s" % mp.nstr(PAR / (mp.pi * MU ** 4) - 1, 3))
rep("(1/16 pi^3) pi mu^4 = mu^4/(16 pi^2) = C_F",
    abs(mp.pi * MU ** 4 / (16 * mp.pi ** 3) - MU ** 4 / (16 * mp.pi ** 2)) < 1e-18,
    mp.nstr(MU ** 4 / (16 * mp.pi ** 2), 15))


def ratio(Cv):
    """massive-flat(m = C)/massless-flat bound, same sampler: the H^3 (5.6) ratio."""
    Cv = mp.mpf(Cv)
    d = integ(F2, 0, Cv) if Cv > 0 else mp.mpf(0)
    # 1 - Q3(u/C) ~ C^2/u^2: tail beyond UMAX ~ C^2 A2/(3 U^3)
    d += integ(lambda uu: F2(uu) * (1 - Q3n(uu / Cv)), Cv, UMAX) + Cv ** 2 * A2 / (3 * UMAX ** 3)
    return 1 - d / (mp.pi * MU ** 4)


def ratio_direct(Cv):
    """second route: the numerator INT_C^oo |FT g''|^2 Q_3(u/C) directly."""
    Cv = mp.mpf(Cv)
    n = integ(lambda uu: F2(uu) * Q3n(uu / Cv), Cv, UMAX) + tail0(UMAX) - Cv ** 2 * A2 / (3 * UMAX ** 3)
    return n / (mp.pi * MU ** 4)


FIX = [(35.35533905932738, 0.0453939, 1e-5), (20.0, 0.0807201, 1e-5), (10.0, 0.165631, 1e-5),
       (5.0, 0.469090, 1e-5), (1.0, 0.974321, 1e-5), (0.1, 0.999753886523, 1e-11),
       (0.01, 0.999997542191, 1e-11)]
results = {}
for Cv, want, tol in FIX:
    r = ratio(Cv)
    results[Cv] = r
    rel = abs(r - want) / want
    rep("ratio(C = %g) = %s  (tree %s)" % (Cv, mp.nstr(r, 13), want), rel <= tol, "rel %.2e" % float(rel))
rd = ratio_direct(35.35533905932738)
rep("second route (numerator directly) agrees at the witness",
    abs(rd - results[35.35533905932738]) < 1e-7, mp.nstr(rd, 12))
rw = results[35.35533905932738]
rep("witness orders -log10(ratio) = 1.343002", abs(-mp.log10(rw) - 1.343002) < 2e-6,
    mp.nstr(-mp.log10(rw), 10))
rcav = ratio(0.005)
rep("cavity C = 0.005 -> ratio rounds to 0.999999", round(float(rcav), 6) == 0.999999,
    mp.nstr(rcav, 12))
rep("monotone decreasing in C", all(results[a1] > results[a2] for a1, a2 in
                                     ((0.01, 0.1), (0.1, 1.0), (1.0, 5.0), (5.0, 10.0), (10.0, 20.0))))
# small-C law: 1 - ratio ~ k C^2 ; the tree does not state one -- recorded
for Cv in (0.1, 0.01):
    print("     (1 - ratio)/C^2 at C = %g: %s" % (Cv, mp.nstr((1 - results[Cv]) / Cv ** 2, 10)))

# F&T (5.6) change of variables: (1/4pi^3) INT_0^oo dw INT_C^oo dw' w'^2 sqrt(w'^2-C^2) |h(w+w')|^2
# = (1/16pi^3) INT_C^oo du |h(u)|^2 u^4 Q_3(u/C): inner INT_C^u w'^2 sqrt(w'^2 - C^2) dw' = u^4 Q_3(u/C)/4
uu_, CC_ = sp.symbols('u C', positive=True)
inner = CC_ ** 4 * anti.subs(y, uu_ / CC_)
rep("(5.6) LHS -> RHS: (1/4pi^3) * C^4 [antideriv](u/C) = u^4 Q_3(u/C)/(16 pi^3)",
    sp.simplify(inner / (4 * sp.pi ** 3) - uu_ ** 4 * Q3_tree.subs(x, uu_ / CC_) / (16 * sp.pi ** 3)) == 0)

# ---------------------------------------------------------------- G
print("G. F&T's OWN Einstein static universe (5.14), mu a = 1: gap C = 1/a, same sampler")
import numpy as np
from scipy.special import roots_legendre
xg, wg = roots_legendre(40)
MUf, SGf = float(MU), float(SG)
EXf = [(MUf, (1 - SGf) / 2), (-MUf, (1 + SGf) / 2), (1j * MUf, (1 + 1j * SGf) / 2), (-1j * MUf, (1 - 1j * SGf) / 2)]
NRMf = float(NRM)


def F2f(uv):
    s = np.zeros_like(uv, dtype=complex)
    for ak, ck in EXf:
        z = ak - 1j * uv
        s += ck * (np.exp(z) - 1) / z
    s *= MUf ** 2
    return (s.real ** 2 + s.imag ** 2) / NRMf


def seg_int(fun, lo, hi, width=0.5):
    n = max(1, int(np.ceil((hi - lo) / width)))
    edges = np.linspace(lo, hi, n + 1)
    h = 0.5 * (edges[1:] - edges[:-1])[:, None]
    m = 0.5 * (edges[1:] + edges[:-1])[:, None]
    uv = m + h * xg[None, :]
    return float(np.sum(h * wg[None, :] * fun(uv)))


def ratio_esu(Cv, U=2000.0):
    """(5.14) at mu a = 1 over the massless flat bound: INT_C^oo |FT g''|^2 C^4 (N+1)^2(N+2)^2/u^4 du / (pi mu^4),
    N(u) = floor(u/C - 1).  On [kC,(k+1)C), N + 1 = k.  Beyond U: weight -> (1 + C/u)^2 ~ 1 + 2C/u."""
    tot = 0.0
    kmax = int(U / Cv)
    for k in range(1, kmax + 1):
        lo, hi = k * Cv, min((k + 1) * Cv, U)
        if lo >= U:
            break
        wk = Cv ** 4 * k ** 2 * (k + 1) ** 2
        tot += seg_int(lambda uv: F2f(uv) * wk / uv ** 4, lo, hi)
    tot += float(A2) / U + float(A2) * Cv / U ** 2          # 1/u^2 (+ 2C/u^3) tail, averaged
    return tot / (np.pi * MUf ** 4)


def ratio_h3f(Cv, U=2000.0):
    def q3(xv):
        xv = np.maximum(xv, 1.0)
        return (xv * (2 * xv ** 2 - 1) * np.sqrt(xv ** 2 - 1) - np.arccosh(xv)) / (2 * xv ** 4)
    d = seg_int(F2f, 0, Cv) + seg_int(lambda uv: F2f(uv) * (1 - q3(uv / Cv)), Cv, U)
    return 1 - d / (np.pi * MUf ** 4)


esu = {}
for Cv in (35.35533905932738, 5.0, 1.0, 0.1):
    re_, rh_ = ratio_esu(Cv), ratio_h3f(Cv)
    esu[Cv] = (re_, rh_)
    print("     C = %-9.5g  H^3 (5.6): %.7f   ESU (5.14): %.7f" % (Cv, rh_, re_))
rep("float H^3 ratio reproduces the 30-dps value at the witness",
    abs(esu[35.35533905932738][1] - float(results[35.35533905932738])) < 1e-6)
rep("SAME gap C, DIFFERENT bound: |ESU - H^3| > 1e-4 at every C tested",
    all(abs(a1 - b1) > 1e-4 for a1, b1 in esu.values()))
rep("ESU with gap C = 5 > 0 is LOOSER than flat (ratio > 1): a gap does not imply tightening",
    esu[5.0][0] > 1.0, "%.7f" % esu[5.0][0])
rep("... and at C = 1 (margin 6.7e-5 >> quadrature/tail error ~1e-6)", esu[1.0][0] > 1.00005,
    "%.7f" % esu[1.0][0])
# control: the ESU routine at a huge a (C -> 0) returns the flat bound
rep("CONTROL: ESU routine at C = 0.02 returns 1 to 1e-5", abs(ratio_esu(0.02) - 1) < 1e-5,
    "%.8f" % ratio_esu(0.02))

# ---------------------------------------------------------------- E
print("E. inf spec(-Lap) = 0 on a slice with arbitrarily large flat balls")
r_, R_ = sp.symbols('r R', positive=True)
phi = sp.cos(sp.pi * r_ / (2 * R_)) ** 2            # C^1 bump, support r <= R
num = sp.integrate(sp.diff(phi, r_) ** 2 * 4 * sp.pi * r_ ** 2, (r_, 0, R_))
den = sp.integrate(phi ** 2 * 4 * sp.pi * r_ ** 2, (r_, 0, R_))
rq = sp.simplify(num / den)
rep("Rayleigh quotient of the R-scaled bump = k/R^2 -> 0", sp.simplify(rq * R_ ** 2).is_constant()
    and sp.limit(rq, R_, sp.oo) == 0, "RQ = %s" % rq)

# ---------------------------------------------------------------- F
print("F. the tree's witness gap (tree data, read-only import)")
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
try:
    import achievable
    a_c = math.sqrt(3.0 * achievable.C_SI ** 4 / (8.0 * math.pi * achievable.G_SI
                                                   * achievable.required_density(1.0)))
    Cw = 1.0 / a_c
    rep("C = b/a_c = 35.35533905932738", abs(Cw - 35.35533905932738) < 1e-9, repr(Cw))
    print("     note: 35.35533905932738 = 25*sqrt(2) = %r" % (25 * math.sqrt(2)))
except Exception as exc:                                   # pragma: no cover
    rep("import achievable", False, repr(exc))

# the witness gap carries no measured datum: G and c cancel exactly
Gs, cs, bs, mb, ab = sp.symbols('G c b m_b a_b', positive=True)
rho_c2 = (mb * bs * cs ** 2 / Gs) * cs ** 2 / (sp.Rational(4, 3) * sp.pi * (ab * bs) ** 3)
ac = sp.sqrt(3 * cs ** 4 / (8 * sp.pi * Gs * rho_c2))
Csym = sp.simplify(bs / ac)
rep("C = b/a_c = sqrt(2 (M/b) / (a/b)^3): G, c and b cancel", Csym.free_symbols == {mb, ab},
    str(Csym))
try:
    rep("... = 25 sqrt(2) at achievable's M/b = %g, a/b = %g" % (achievable.M_OVER_B, achievable.A_OVER_B),
        abs(float(Csym.subs({mb: achievable.M_OVER_B, ab: achievable.A_OVER_B})) - 25 * math.sqrt(2)) < 1e-9)
except NameError:
    pass

print("\nREDERIVE %s" % ("OK" if OK else "FAILED"))
sys.exit(0 if OK else 1)
