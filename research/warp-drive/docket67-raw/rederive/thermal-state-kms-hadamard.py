#!/usr/bin/env python3
r"""
DOCKET 67 -- re-derivation for key 'thermal-state-kms-hadamard'.

The tree (noise.py:111-114) uses: THERMAL RADIATION of the free (massless) scalar
in 3+1 Minkowski, at inverse temperature beta w.r.t. an inertial time translation,
is a zero-mean Gaussian (quasifree), KMS and Hadamard state, with normal-ordered
phidot kernel
    g(u) = -(1/2pi^2) d^3/du^3 [ (pi/2beta) coth(pi u/beta) - 1/(2u) ],
    g(0) = pi^2/(30 beta^4),  g -> -3/(2 pi^2 u^4),
    ||g^2||_1 = 180 (zeta6 - zeta7)/(pi^3 beta^7).

What is checked here (beta = 1 unless stated; every check prints PASS/FAIL):
  K1  KMS: per-mode detailed balance (1+n) e^{-beta w} = n, and the resulting
      strip identity W+(t - i beta) = W+(-t) for the Planck two-point function,
      symbolically (sympy).
  K2  Quasifree/Gaussian: the Gibbs state of ONE oscillator (the Planck state is a
      product of these over modes) has <x>=<x^3>=0 and <x^4> = 3<x^2>^2
      (truncated Fock space, numeric) -- Wick's theorem at fourth order.
  K3  The closed-form kernel: the mode integral (1/2pi^2) INT k^3 n(k) cos(ku) dk
      equals the coth expression at several u (mpmath quadrature), g(0), the u^-4
      tail, and ||g^2||_1 by quadrature against 180(zeta6-zeta7)/pi^3.
  K4  Hadamard (elementary form, Minkowski): W_beta - W_0 is smooth.
      (a) closed form (1/(8 pi beta r))[coth(pi(r-t)/beta)+coth(pi(r+t)/beta)]
          - 1/(4 pi^2 (r^2 - t^2)) has a regular Taylor expansion at (t,r) -> 0
          along arbitrary rays and no pole on the light cone r = |t| (sympy);
      (b) every derivative of the integral representation
          (1/2pi^2) INT k n(k) [sin kr/(kr)] cos(kt) dk is dominated by the moment
          INT k^(1+j) n(k) dk = Gamma(j+2) zeta(j+2) < oo  (all j) -> C^infinity;
      (c) coincidence value <:phi^2:>_beta = 1/(12 beta^2) from both forms.
  K5  CONTROLS THAT CAN FAIL (vacuity guards):
      (a) in 1+1 dimensions the massless thermal difference INT dk n(k)/k diverges
          at k -> 0 (the '3+1' hypothesis is load-bearing);
      (b) a deliberately wrong kernel (coth replaced by tanh) fails K3;
      (c) the Boltzmann (classical) factor e^{-beta w} in place of n fails K1.
  K6  Zero mean is a CHOICE, not forced by KMS for m = 0: a constant classical shift
      c (a time-independent solution of the massless wave equation) adds c^2 to
      the two-point function; the constant satisfies the KMS strip identity
      trivially, and the truncated (connected) function is unchanged.  This is a
      two-point-level demonstration, not a full classification.
"""
import sys
import sympy as sp
import mpmath as mp

mp.mp.dps = 30
ok_all = True


def chk(name, cond, detail=""):
    global ok_all
    ok_all &= bool(cond)
    print("%s  %s  %s" % ("PASS" if cond else "FAIL", name, detail))


# ---------------------------------------------------------------- K1  KMS
b, w, t = sp.symbols('beta omega t', positive=True)
n = 1 / (sp.exp(b * w) - 1)
chk("K1a detailed balance (1+n) e^{-beta w} == n",
    sp.simplify((1 + n) * sp.exp(-b * w) - n) == 0)
tt = sp.symbols('tt', real=True)
Wp = lambda T: (1 + n) * sp.exp(-sp.I * w * T) + n * sp.exp(sp.I * w * T)  # per-mode W+(t)
chk("K1b per-mode strip identity W+(t - i beta) == W+(-t)",
    sp.simplify(sp.expand(Wp(tt - sp.I * b) - Wp(-tt))) == 0)
nB = sp.exp(-b * w)                                    # control K5c
WpB = lambda T: (1 + nB) * sp.exp(-sp.I * w * T) + nB * sp.exp(sp.I * w * T)
chk("K5c CONTROL: Boltzmann factor fails the KMS identity (must be nonzero)",
    sp.simplify(sp.expand(WpB(tt - sp.I * b) - WpB(-tt))) != 0)

# ---------------------------------------------------------------- K2  Gaussian
import numpy as np
N = 700
for bw in (0.3, 1.0, 3.0):
    kk_ = np.arange(N)
    probs = np.exp(-bw * kk_)
    probs /= probs.sum()
    X = np.diag(np.sqrt(kk_[1:] / 2.0), 1) + np.diag(np.sqrt(kk_[1:] / 2.0), -1)
    X2 = X @ X
    X3 = X2 @ X
    X4 = X2 @ X2
    M = N - 8          # states near the truncation edge carry weight < e^{-0.3*692}
    ex = lambda A: float(np.sum(probs[:M] * np.diag(A)[:M]))
    m1, m2, m3, m4 = ex(X), ex(X2), ex(X3), ex(X4)
    nb = 1.0 / np.expm1(bw)
    chk("K2 beta*w=%.1f  <x>=<x^3>=0, <x^2>=n+1/2, <x^4>=3<x^2>^2" % bw,
        abs(m1) < 1e-14 and abs(m3) < 1e-14 and abs(m2 / (nb + 0.5) - 1) < 1e-12
        and abs(m4 / (3 * m2 ** 2) - 1) < 1e-12,
        "<x^2>=%.12g  <x^4>/(3<x^2>^2)=%.15g" % (m2, m4 / (3 * m2 ** 2)))

# ---------------------------------------------------------------- K3  kernel
u = sp.symbols('u', positive=True)
bracket = (sp.pi / 2) * sp.coth(sp.pi * u) - 1 / (2 * u)
g_sym = -sp.diff(bracket, u, 3) / (2 * sp.pi ** 2)
g0 = sp.limit(g_sym, u, 0)
chk("K3a g(0) == pi^2/30 (beta=1)", sp.simplify(g0 - sp.pi ** 2 / 30) == 0, str(g0))
tail = sp.limit(g_sym * u ** 4, u, sp.oo)
chk("K3b u^4 g(u) -> -3/(2 pi^2)", sp.simplify(tail + 3 / (2 * sp.pi ** 2)) == 0, str(tail))
g_num = sp.lambdify(u, g_sym, 'mpmath')


def g_mode(uu):
    f = lambda k: k ** 3 / (mp.e ** k - 1) * mp.cos(k * uu)
    return mp.quadosc(f, [0, mp.inf], omega=uu) / (2 * mp.pi ** 2) if uu > 0 else \
        mp.quad(lambda k: k ** 3 / (mp.e ** k - 1), [0, mp.inf]) / (2 * mp.pi ** 2)


worst = 0
for uu in (mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf(1), mp.mpf(2), mp.mpf(5)):
    a, c = g_mode(uu), g_num(uu)
    worst = max(worst, abs(a - c) / abs(c))
chk("K3c mode integral == coth closed form at u in {0.1,0.5,1,2,5}", worst < 1e-15,
    "worst rel err %s" % mp.nstr(worst, 3))
g_ser = sp.lambdify(u, sp.series(g_sym, u, 0, 12).removeO(), 'mpmath')
g_safe = lambda x: g_ser(x) if x < mp.mpf('0.05') else g_num(x)
g2 = 2 * mp.quad(lambda x: g_safe(x) ** 2, [0, mp.mpf('0.05'), 1, 5, 20, mp.inf])
g2_closed = 180 * (mp.zeta(6) - mp.zeta(7)) / mp.pi ** 3
chk("K3d ||g^2||_1 (full line) == 180(zeta6-zeta7)/pi^3", abs(g2 / g2_closed - 1) < 1e-10,
    "quad %s closed %s" % (mp.nstr(g2, 15), mp.nstr(g2_closed, 15)))
# Parseval route, exact in sympy
k = sp.symbols('k', positive=True)
j = sp.symbols('j', integer=True, positive=True)
# INT k^6/(e^k-1)^2 dk = sum_{m>=2} (m-1) 6!/m^7 = 720 (zeta6 - zeta7)
S = sp.summation((j - 1) * sp.factorial(6) / j ** 7, (j, 2, sp.oo))
chk("K3e INT k^6/(e^k-1)^2 = 720(zeta6-zeta7) (series, sympy)",
    sp.simplify(S - 720 * (sp.zeta(6) - sp.zeta(7))) == 0, str(sp.nsimplify(S)))
g_bad = -sp.diff((sp.pi / 2) * sp.tanh(sp.pi * u) - 1 / (2 * u), u, 3) / (2 * sp.pi ** 2)
gb = sp.lambdify(u, g_bad, 'mpmath')
chk("K5b CONTROL: tanh kernel disagrees with the mode integral at u=1",
    abs(gb(mp.mpf(1)) - g_mode(mp.mpf(1))) / abs(g_mode(mp.mpf(1))) > 1e-3)

# ---------------------------------------------------------------- K4  Hadamard
r, tq, s = sp.symbols('r t s', real=True)
Wdiff = (sp.coth(sp.pi * (r - tq)) + sp.coth(sp.pi * (r + tq))) / (8 * sp.pi * r) \
    - 1 / (4 * sp.pi ** 2 * (r ** 2 - tq ** 2))
regular = True
for (aa, bb) in ((1, sp.Rational(1, 3)), (sp.Rational(1, 2), 1), (1, 0), (0, 1), (2, sp.Rational(7, 5))):
    ser = sp.series(Wdiff.subs({tq: aa * s, r: bb * s}) if bb != 0 else
                    sp.limit(Wdiff, r, 0).subs(tq, aa * s), s, 0, 4).removeO()
    ser = sp.simplify(ser)
    lead = sp.limit(ser, s, 0)
    regular &= (lead.is_finite is True) and sp.simplify(lead - sp.Rational(1, 12)) == 0
chk("K4a W_beta - W_0 regular at coincidence along 5 rays, value 1/12 = <:phi^2:>",
    regular)
# light cone r = t: residue of the difference vanishes
eps = sp.symbols('eps')
lc = sp.series(Wdiff.subs(tq, r - eps), eps, 0, 1).removeO()
chk("K4a' no pole on the light cone r=t (1/eps coefficient == 0)",
    sp.simplify(sp.expand(lc).coeff(eps, -1)) == 0)
# numeric agreement of closed form and integral representation off-diagonal
Wd = sp.lambdify((r, tq), Wdiff, 'mpmath')


def Wd_int(rr, t0):
    f = lambda kk: kk / (mp.e ** kk - 1) * mp.sin(kk * rr) / (kk * rr) * mp.cos(kk * t0)
    return mp.quad(f, [0, 5, 20, 60, mp.inf]) / (2 * mp.pi ** 2)


wst = 0
for (rr, t0) in ((0.3, 0.1), (1.0, 0.7), (2.0, 2.5), (0.5, 0.5000001)):
    wst = max(wst, abs(Wd(mp.mpf(rr), mp.mpf(t0)) - Wd_int(rr, t0)) / abs(Wd_int(rr, t0)))
chk("K4b' closed form == integral rep at 4 points incl. near light cone", wst < 1e-10,
    "worst %s" % mp.nstr(wst, 3))
moments = [mp.quad(lambda kk: kk ** (1 + jj) / (mp.e ** kk - 1), [0, mp.inf]) for jj in range(0, 9)]
closed_m = [mp.gamma(jj + 2) * mp.zeta(jj + 2) for jj in range(0, 9)]
chk("K4b all derivative-dominating moments finite: INT k^(1+j) n = Gamma(j+2)zeta(j+2), j=0..8",
    all(abs(a / c - 1) < 1e-20 for a, c in zip(moments, closed_m)))
phi2 = mp.quad(lambda kk: kk / (mp.e ** kk - 1), [0, mp.inf]) / (2 * mp.pi ** 2)
chk("K4c <:phi^2:>_beta from the mode integral == 1/12", abs(phi2 - mp.mpf(1) / 12) < 1e-25)

# ---------------------------------------------------------------- K5a  1+1 control
lo = [mp.quad(lambda kk: 1 / (kk * (mp.e ** kk - 1)), [cut, 1, mp.inf]) for cut in (1e-2, 1e-4, 1e-6)]
chk("K5a CONTROL: 1+1 massless INT n(k)/k dk diverges (grows ~1/cut)",
    lo[2] > 100 * lo[1] > 1e4 * lo[0] / 1e2, "at cut 1e-2,1e-4,1e-6: %s" % [mp.nstr(v, 6) for v in lo])

# ---------------------------------------------------------------- K6  zero mean is a choice
cc = sp.symbols('c', real=True)
F = cc ** 2                                  # constant added to W+(t) by the shift
chk("K6 constant shift: c^2 satisfies F(t - i beta) == F(-t); connected W unchanged",
    sp.simplify(F.subs(tt, tt - sp.I * b) - F.subs(tt, -tt)) == 0)

print("\nALL PASS" if ok_all else "\nSOME FAILED")
sys.exit(0 if ok_all else 1)
