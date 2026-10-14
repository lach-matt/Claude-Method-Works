#!/usr/bin/env python3
"""
DOCKET 67 re-derivation for key boyer-casimir-real-mirror-sign.

What the tree uses (ledger.py:1546-1552, 2130-2133; specthm.py:1244-1245; built in tolman.py:1459-1527):
  "The sign INVERTS for any real mirror at a_c = 0.480 x skin depth, materials-independent";
  "m(r) > 0 near the wall for every real mirror".
Built from: ideal interior near-wall p_r = -A hbar c/(a^2 eps^2), A = 1/(60 pi^2)  (Deutsch-Candelas via Milton 1005.0031 eq.58,
Saharian 0708.1187 eq.14.21), and a RECONSTRUCTED plasma-sphere p_r = +K/(a eps^2), K = (sqrt2/128pi) omega_p (Sopova-Ford
quant-ph/0504143 eq.15, transverse T_xx), compared at the SAME eps (tolman.py V17, crossover_coefficient()).

Checks (stdlib + sympy + scipy + mpmath + z3):
  C1 sympy: conservation p_r' + 2(p_r - p_t)/r = 0 turns p_t = K/eps^3 into p_r = +K/(a eps^2) INSIDE, -K/(a eps^2) OUTSIDE;
            the same step on the ideal interior u reproduces the tree's p_r = -1/(60 pi^2 a^2 eps^2); log terms are excluded.
  C2 exact arithmetic: K_SF/A_EM = 60 sqrt2 pi/128; a_c/lambdabar_p = 0.4801687020.
  C3 sign of the near-wall material coefficient: I = INT (eps(i z)-1)/(eps(i z)+1) dz > 0 for plasma (closed form), Drude,
     Drude + Lorentz (ILLUSTRATIVE parameters); z3: eps > 1 => integrand in (0,1).
  C4 planar regime test on the EXACT one-interface plasma-model integrals: the ideal asymptote 3/(16 pi^2 z^4) of <E^2> is reached
     only for omega_p z >> 1, the plasma asymptote sqrt2 omega_p/(32 pi z^3) only for omega_p z << 1; at the point where the two
     asymptotes are EQUATED (omega_p z* = 6/(sqrt2 pi)) neither is accurate.  U has ideal coefficient 0 and plasma coefficient > 0.
  C5 Boyer total, perfectly conducting sphere: E a = 3/64 + (1/2pi) SUM_l [(2l+1) J_l + 3pi/32], J_l = INT_0^inf ln(1 - lambda_l^2) dx,
     lambda_l = (x I_nu K_nu)', nu = l+1/2; target +0.04618 (Milton 1005.0031 Table 1 / eq.117, citing Boyer 1968).
  C6 data: gold a_c at omega_p = 9.0 eV (tree) vs 8.38 / 6.82 eV (measured films, 0801.1384 Table II); compactness chi at
     eps = lambdabar_p (where the ideal band begins).
Exit 0 iff every check passes.
"""
import math, sys
import sympy as sp
import mpmath as mp
from scipy import integrate, special

FAIL = []
def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    if not ok:
        FAIL.append(name)

# ---------------------------------------------------------------- C1
a, eps, K, B, P2, C3 = sp.symbols("a epsilon K B P2 C3", positive=True)
Bs = sp.Symbol("B")
# interior r = a - eps : d/dr = -d/deps
pt = K / eps**3 + P2 / eps**2
pr = Bs / eps**2
cons_in = sp.limit(sp.simplify((-sp.diff(pr, eps) + 2 * (pr - pt) / (a - eps)) * eps**3), eps, 0)
sol_in = sp.solve(cons_in, Bs)
check("C1a interior: p_t = K/eps^3 => p_r = +K/(a eps^2)", sol_in == [K / a], str(sol_in))
# exterior r = a + eps : d/dr = +d/deps
cons_out = sp.limit(sp.simplify((sp.diff(pr, eps) + 2 * (pr - pt) / (a + eps)) * eps**3), eps, 0)
sol_out = sp.solve(cons_out, Bs)
check("C1b exterior: p_r = -K/(a eps^2) (opposite sign outside)", sol_out == [-K / a], str(sol_out))
# ideal interior: u = -1/(30 pi^2 a eps^3), traceless -u + p_r + 2 p_t = 0, p_r = O(eps^-2) => p_t ~ u/2
u_id = -1 / (30 * sp.pi**2 * a * eps**3)
Kid = sp.simplify((u_id / 2) * eps**3)
check("C1c ideal interior reproduces tree p_r = -1/(60 pi^2 a^2 eps^2)", sp.simplify(Kid / a + 1 / (60 * sp.pi**2 * a**2)) == 0)
# log term excluded: p_r = L ln(eps)/eps^2 leaves an uncancelled ln(eps)/eps^3
L = sp.Symbol("L")
prL = L * sp.log(eps) / eps**2
exprL = sp.expand(-sp.diff(prL, eps) * eps**3)
check("C1d a log term in p_r would leave 2L ln(eps)/eps^3 uncancelled => L = 0",
      sp.simplify(exprL.coeff(sp.log(eps)) - 2 * L) == 0)
# plasma tracelessness consistency: u = p_r + 2 p_t ~ 2K/eps^3 = planar U = 2 T_xx
check("C1e traceless: leading u = 2K/eps^3 (Sopova-Ford U = 2 T_xx)", sp.limit((Bs / eps**2 + 2 * pt).subs(Bs, K / a) * eps**3, eps, 0) == 2 * K)

# ---------------------------------------------------------------- C2
K_SF = sp.sqrt(2) / (128 * sp.pi)
A_EM = 1 / (60 * sp.pi**2)
coef = sp.nsimplify(K_SF / A_EM)
check("C2a K_SF/A_EM = 60 sqrt2 pi/128 exactly", sp.simplify(coef - 60 * sp.sqrt(2) * sp.pi / 128) == 0, "%.10f" % float(coef))
ac = float(1 / coef)
check("C2b a_c / lambdabar_p = 0.4801687020", abs(ac - 0.4801687020) < 1e-10, "%.10f" % ac)

# ---------------------------------------------------------------- C3
wp = 1.0
I_plasma = integrate.quad(lambda z: (wp**2 / z**2) / (2 + wp**2 / z**2), 0, math.inf)[0]
check("C3a plasma I = pi omega_p/(2 sqrt2), K = I/(32 pi^2) = sqrt2 omega_p/(128 pi)",
      abs(I_plasma - math.pi / (2 * math.sqrt(2))) < 1e-9 and abs(I_plasma / (32 * math.pi**2) - math.sqrt(2) / (128 * math.pi)) < 1e-12,
      "I = %.10f" % I_plasma)
def I_of(epsfun):
    return integrate.quad(lambda z: (epsfun(z) - 1) / (epsfun(z) + 1), 0, math.inf, limit=400)[0]
# units eV; gold-like Drude 9.0 eV / 35 meV; ILLUSTRATIVE Lorentz interband term (not a fit to any sample)
drude = lambda z: 1 + 81.0 / (z * (z + 0.035))
lor = lambda z: drude(z) + 30.0 / (9.0 + z * z + 1.0 * z)
I_d, I_dl = I_of(drude), I_of(lor)
I_p9 = math.pi * 9.0 / (2 * math.sqrt(2))
check("C3b Drude (9.0 eV, 35 meV): I > 0, shift vs plasma", I_d > 0, "I/I_plasma - 1 = %+.4f %%" % (100 * (I_d / I_p9 - 1)))
check("C3c Drude + ILLUSTRATIVE Lorentz: I > 0 (sign kept, magnitude moves)", I_dl > 0,
      "I/I_plasma - 1 = %+.4f %%  => a_c/lambdabar_p would be %.4f, not 0.4802" % (100 * (I_dl / I_p9 - 1), ac * I_p9 / I_dl))
try:
    import z3
    e = z3.Real("e"); s = z3.Solver()
    s.add(e > 1, z3.Not(z3.And((e - 1) / (e + 1) > 0, (e - 1) / (e + 1) < 1)))
    r = s.check()
    s2 = z3.Solver(); s2.add(e > 1); vac = s2.check()
    check("C3d z3: eps(i zeta) > 1 => 0 < (eps-1)/(eps+1) < 1 (guard: premise satisfiable)", r == z3.unsat and vac == z3.sat, "%s / guard %s" % (r, vac))
except ImportError:
    check("C3d z3 available", False)

# ---------------------------------------------------------------- C4
def planar(z, which):
    """Exact one-interface plasma-model renormalised <E^2> or U at distance z (omega_p = 1), Lorentz-Heaviside, hbar=c=1.
    <E^2> = (1/2pi^2) INT dzeta dk (k/2kappa) e^{-2 kappa z} [(2k^2+zeta^2) r_TM - zeta^2 r_TE];  U = (1/2pi^2) INT (k^3/kappa) e^{..}(r_TM + r_TE)/2 * ...
    computed in polar coordinates zeta = kappa cos th, k = kappa sin th, t = kappa z."""
    def inner(th, t):
        kap = t / z
        ze, k = kap * math.cos(th), kap * math.sin(th)
        if ze == 0.0:
            return 0.0
        ep = 1.0 + 1.0 / ze**2
        km = math.sqrt(k * k + ep * ze * ze)
        rte = (kap - km) / (kap + km)
        rtm = (ep * kap - km) / (ep * kap + km)
        if which == "E2":
            br = (2 * k * k + ze * ze) * rtm - ze * ze * rte
        else:  # U = (E2 + B2)/2, bracket 2k^2(rTM + rTE)/2
            br = k * k * (rtm + rte)
        return (k / (2 * kap)) * math.exp(-2 * t) * br * kap / z   # dk dzeta = kappa dkappa dth, dkappa = dt/z
    val = integrate.dblquad(inner, 0, 60, 0, math.pi / 2, epsabs=0, epsrel=1e-9)[0]
    return val / (2 * math.pi**2)

ideal_E2 = lambda z: 3 / (16 * math.pi**2 * z**4)
plas_E2 = lambda z: math.sqrt(2) / (32 * math.pi * z**3)
plas_U = lambda z: math.sqrt(2) / (64 * math.pi * z**3)
rows = []
for z in (1e-3, 1e-2, 1e-1, 1.0, 10.0, 100.0, 1000.0):
    E2 = planar(z, "E2")
    rows.append((z, E2 / ideal_E2(z), E2 / plas_E2(z)))
    print("      omega_p z = %-7g  <E^2>/ideal = %.6f   <E^2>/plasma-asymptote = %.6f" % rows[-1])
check("C4a <E^2> -> ideal 3/(16pi^2 z^4) only for omega_p z >> 1", abs(rows[-1][1] - 1) < 2e-3 and rows[0][1] < 2e-2,
      "ratio %.5f at 1000, %.5f at 1e-3" % (rows[-1][1], rows[0][1]))
check("C4b <E^2> -> plasma sqrt2 omega_p/(32 pi z^3) only for omega_p z << 1", abs(rows[0][2] - 1) < 5e-3 and rows[-1][2] < 0.01,
      "ratio %.5f at 1e-3, %.5f at 1000" % (rows[0][2], rows[-1][2]))
add = 1 + ideal_E2(1e-3) / plas_E2(1e-3)
check("C4e the ideal term does NOT coexist near the wall: an ADDITIVE ideal term would make exact/plasma = %.1f at omega_p z = 1e-3" % add,
      abs(rows[0][2] - 1) < 5e-3 and add > 1000, "measured %.5f -- the ideal 1/z^4 term is replaced, not out-competed" % rows[0][2])
zs = 6 / (math.sqrt(2) * math.pi)
E2s = planar(zs, "E2")
check("C4c at the asymptote-equality point omega_p z* = 6/(sqrt2 pi) = %.4f neither asymptote holds" % zs,
      abs(E2s / ideal_E2(zs) - 1) > 0.2, "exact/ideal = %.4f, exact/plasma = %.4f" % (E2s / ideal_E2(zs), E2s / plas_E2(zs)))
U3 = planar(1e-3, "U")
U2 = planar(1e3, "U")
check("C4d U: plasma near-wall coefficient POSITIVE, ideal coefficient ZERO (replacement, not competition)",
      abs(U3 / plas_U(1e-3) - 1) < 5e-3 and U2 * (1e3)**4 < 0.05 * 3 / (16 * math.pi**2),
      "U/plasma = %.5f at 1e-3; z^4 U = %.3e at 1000 (ideal z^4<E^2> = %.3e)" % (U3 / plas_U(1e-3), U2 * 1e12, 3 / (16 * math.pi**2)))

# ---------------------------------------------------------------- C5  Boyer
mp.mp.dps = 30
def lam(l, x):
    nu = mp.mpf(l) + mp.mpf(1) / 2
    I, Kf = mp.besseli(nu, x), mp.besselk(nu, x)
    Im, Km = mp.besseli(nu - 1, x), mp.besselk(nu - 1, x)
    return I * Kf * (1 - 2 * nu) + x * (Im * Kf - I * Km)
def J(l):
    f = lambda x: mp.log(1 - lam(l, x)**2)
    return mp.quad(f, [0, 0.5, 2, 8, 30, mp.inf])
lmax = 40
terms = []
for l in range(1, lmax + 1):
    terms.append(float((2 * l + 1) * J(l) + 3 * mp.pi / 32))
# tail ~ c/nu^2 + d/nu^4 fitted on the last terms
nu = [l + 0.5 for l in range(1, lmax + 1)]
import numpy as np
X = np.array([[1 / n**2, 1 / n**4] for n in nu[-12:]]); Y = np.array(terms[-12:])
cfit = np.linalg.lstsq(X, Y, rcond=None)[0]
tail = sum(cfit[0] / (l + 0.5)**2 + cfit[1] / (l + 0.5)**4 for l in range(lmax + 1, 200000))
Ea = 3 / 64 + (sum(terms) + tail) / (2 * math.pi)
check("C5 Boyer E a = +0.04618 (repulsive), from 3/64 leading uniform term + convergent remainder", abs(Ea - 0.04618) < 5e-5,
      "E a = %.6f (3/64 = %.6f, remainder %.6f; l_max %d, fitted tail %.2e)" % (Ea, 3 / 64, Ea - 3 / 64, lmax, tail / (2 * math.pi)))

# ---------------------------------------------------------------- C6 data
HBAR, C, QE = 1.054571817e-34, 299792458.0, 1.602176634e-19
lP = 1.616255e-35
def lbar(eV): return C / (eV * QE / HBAR)
for eV, lab in ((9.0, "tree (Lambrecht-Reynaud estimate)"), (8.38, "film max, 0801.1384"), (6.82, "film min, 0801.1384")):
    print("      gold omega_p %.2f eV [%s]: lambdabar_p = %.4f nm, a_c = %.4f nm" % (eV, lab, lbar(eV) * 1e9, ac * lbar(eV) * 1e9))
check("C6a tree pins reproduced: gold 21.9252 / 10.5278 nm, Al 12.8972 / 6.19283 nm",
      abs(lbar(9.0) * 1e9 - 21.9252) < 1e-3 and abs(ac * lbar(9.0) * 1e9 - 10.5278) < 1e-3
      and abs(lbar(15.3) * 1e9 - 12.8972) < 1e-3 and abs(ac * lbar(15.3) * 1e9 - 6.19283) < 1e-4)
chi = (2 / (15 * math.pi)) * (lP / lbar(9.0))**2
check("C6b compactness where the ideal (m<0) band begins, eps = lambdabar_p(gold): chi << 1", chi < 1e-50, "chi = %.3e" % chi)

print()
print("ALL CHECKS PASS" if not FAIL else "FAILED: %s" % FAIL)
sys.exit(1 if FAIL else 0)
