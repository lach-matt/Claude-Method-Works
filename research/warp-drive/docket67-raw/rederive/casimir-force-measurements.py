#!/usr/bin/env python3
"""DOCKET 67 audit -- casimir-force-measurements.

Re-derives / machine-checks what is finite or closed-form in the tree's use of
the measured Casimir force (Lamoreaux 1997; Mohideen-Roy 1998; Bressi 2002) and
the ideal-plate energy E/A = -pi^2 hbar c/(720 d^3), as used at
research/warp-drive/tolman.py:1317-1322, 2539-2540, 2855-2900 and
candidates.py:73-74.  Read-only with respect to the tree.

Checks
  A. sympy: E/A from the zeta-regularised mode sum; F/A = -d(E/A)/dd = -3 u0;
     Brown-Maclay tensor traceless; isotropic average (-u0,-u0/3,-u0/3);
     the factor 9; m(R) at d = 10 nm, R = 1 mm against tolman's -2.019814e-21 kg.
  B. numbers the three papers state, recomputed: Bressi K_C = pi h c/480 and the
     measured (1.22 +- 0.18)e-27 N m^2; Lamoreaux erratum radius shift 11.3->12.5 cm.
  C. Lifshitz (zero-T, plasma model, identical half-spaces) energy per area
     against the ideal formula, eta(d) = E_real/E_ideal, for gold (9.0 eV, the
     tree's own HBAR_OMEGA_P_GOLD_EV) at the tree's d = 10 nm and across the
     measured ranges.  Cross-checked: eta -> 1 at large d; nonretarded limit.
  D. Sopova & Ford (quant-ph/0204125) eq. (50): the LOCAL energy density at the
     centre of the gap between plasma-model half-spaces, as a function of
     omega_p a; check the perfect-conductor limit -pi^2/720 and the paper's
     sign change near omega_p a ~ 99; evaluate at the tree's d = 10 nm (gold).
"""
import math
import sympy as sp
from scipy import integrate

out = {}

# ---------------------------------------------------------------- A. sympy
d, hbar, c, n, R = sp.symbols('d hbar c n R', positive=True)
# zeta-regularised: E/A = -(pi^2/(6 d^3)) hbar c * zeta(-3)*... use the standard
# closed form E/A = -(hbar c pi^2/(3 d^3)) * (1/(2pi)^4) * INT x^3/(e^x-1) dx
x = sp.symbols('x', positive=True)
I3 = sp.gamma(4) * sp.zeta(4)          # Bose integral INT x^3/(e^x-1) = Gamma(4) zeta(4)
# sympy cannot close the integral itself; the Bose identity is checked numerically:
_I3num = float(sp.Integral(x**3 / (sp.exp(x) - 1), (x, 0, sp.oo)).evalf(30))
out['A0_bose_integral_numeric_vs_pi4_over_15'] = (_I3num, float(sp.pi**4 / 15))
assert abs(_I3num - float(sp.pi**4 / 15)) < 1e-12
EA = -hbar * c * sp.pi**2 / (3 * d**3) / (2 * sp.pi)**4 * I3       # Bordag et al. (2.36)
EA_ideal = -sp.pi**2 * hbar * c / (720 * d**3)
out['A1_EA_matches_720'] = sp.simplify(EA - EA_ideal) == 0
u0 = sp.pi**2 * hbar * c / (720 * d**4)
FA = -sp.diff(EA_ideal, d)                                           # force per area
out['A2_FA_equals_minus_3u0'] = sp.simplify(FA - (-3 * u0)) == 0     # attractive
out['A2b_FA_equals_pi2_over_240'] = sp.simplify(FA + sp.pi**2 * hbar * c / (240 * d**4)) == 0
rho, pn, pt = -u0, -3 * u0, +u0
out['A3_traceless'] = sp.simplify(-rho + pn + 2 * pt) == 0
p_iso = sp.simplify((pn + 2 * pt) / 3)
out['A4_isotropic_p'] = sp.simplify(p_iso + u0 / 3) == 0
m_quad = -4 * sp.pi * R**3 * u0 / (3 * c**2)
m_raw = 4 * sp.pi * R**3 * pn / c**2
out['A5_factor_9'] = sp.simplify(m_raw / m_quad) == 9
HBAR, C = 1.054571817e-34, 2.99792458e8
u0n = math.pi**2 * HBAR * C / (720 * 1e-8**4)
mn = -4 * math.pi * 1e-3**3 * u0n / (3 * C * C)
out['A6_u0_at_10nm_J_per_m3'] = u0n
out['A6_m_at_10nm_R1mm_kg'] = mn
out['A6_matches_tolman'] = abs(mn / -2.019814e-21 - 1) < 1e-4

# ------------------------------------------------ B. the papers' own numbers
h = 2 * math.pi * HBAR
KC_theory = math.pi * h * C / 480
out['B1_KC_theory_Nm2'] = KC_theory               # Bressi: 1.3e-27
out['B1_KC_equals_pi2hbarc_240'] = abs(KC_theory / (math.pi**2 * HBAR * C / 240) - 1) < 1e-12
out['B2_Bressi_KC_measured'] = (1.22e-27, 0.18e-27)
out['B2_pull_sigma'] = (1.22e-27 - KC_theory) / 0.18e-27
out['B2_Bressi_alt_fit'] = (1.24e-27, 0.10e-27, (1.24e-27 - KC_theory) / 0.10e-27)
out['B3_Lamoreaux_radius_shift'] = 12.5 / 11.3 - 1      # +10.6 % per Bordag et al. p.209
# Mohideen-Roy: rms 1.6 pN with corrections (1 % at closest), 6.3 pN ideal (5 %)
out['B4_MR_ideal_vs_corrected_rms_pN'] = (6.3, 1.6)

# --------------------------------------- C. Lifshitz plasma-model eta(d)
# units: hbar = c = omega_p = 1; lengths in units of delta = c/omega_p
def EA_lifshitz(D):
    """E/A in units hbar omega_p^3 / c^2, zero T, plasma model eps = 1 + 1/xi^2.
    E/A = (1/4pi^2) INT_0^inf dq q INT_0^q dxi [ln(1-rTE^2 e^{-2qD}) + ln(1-rTM^2 e^{-2qD})]
    (k dk = q dq)."""
    def inner(q):
        def f(xi):
            if xi == 0.0:
                xi = 1e-300
            k2 = q * q - xi * xi
            kap = math.sqrt(k2 + xi * xi + 1.0)
            eps = 1.0 + 1.0 / (xi * xi)
            rte = (q - kap) / (q + kap)
            rtm = (eps * q - kap) / (eps * q + kap)
            e = math.exp(-2 * q * D)
            return math.log1p(-rte * rte * e) + math.log1p(-rtm * rtm * e)
        v, _ = integrate.quad(f, 0.0, q, limit=200)
        return q * v
    qmax = 60.0 / D
    pts = [0.0, 1.0 / D, 5.0 / D, 20.0 / D, qmax]
    tot = 0.0
    for a_, b_ in zip(pts[:-1], pts[1:]):
        v, _ = integrate.quad(inner, a_, b_, limit=200)
        tot += v
    return tot / (4 * math.pi**2)

def EA_ideal_units(D):
    return -math.pi**2 / (720 * D**3)

QE = 1.602176634e-19
def delta_gold(eV=9.0):
    return C / (eV * QE / HBAR)

dg = delta_gold()
out['C0_gold_skin_depth_nm'] = dg * 1e9
out['C0_gold_lambda_p_nm'] = 2 * math.pi * dg * 1e9
eta = {}
for dnm in (10.0, 62.0, 100.0, 120.0, 500.0, 600.0, 1000.0, 3000.0, 6000.0):
    D = dnm * 1e-9 / dg
    eta[dnm] = EA_lifshitz(D) / EA_ideal_units(D)
out['C1_eta_gold_plasma'] = eta
# nonretarded check at small D: E/A -> -(1/(16 pi^2 D^2)) INT_0^inf dxi Li3(r(xi)^2),
# r = 1/(1+2 xi^2)  (eps-1)/(eps+1) with eps = 1+1/xi^2
import mpmath
nr_int = mpmath.quad(lambda xi: mpmath.polylog(3, (1 / (1 + 2 * xi**2))**2), [0, mpmath.inf])
D10 = 1e-8 / dg
Dsmall = 1e-3
nr_small = -float(nr_int) / (16 * math.pi**2 * Dsmall**2)
out['C2_nonretarded_check_ratio_at_D=1e-3'] = EA_lifshitz(Dsmall) / nr_small
out['C3_nonretarded_over_lifshitz_at_10nm'] = (-float(nr_int) / (16 * math.pi**2 * D10**2)) / EA_lifshitz(D10)

# ----------------------------- D. Sopova-Ford eq. (50) at the gap centre
def U_centre_a4(wpa):
    """a^4 U(z=a/2), Sopova-Ford quant-ph/0204125 eq. (50), omega_p a = wpa.
    Units a = 1, so omega_p = wpa.  r, r' from eqs. (34a,b), t = cos theta."""
    wp = wpa
    def f(t, u):
        s = math.sqrt(u * u + wp * wp)
        r = (u - s) / (u + s)
        rp = (u * u * t * t + wp * wp - u * t * t * s) / (u * u * t * t + wp * wp + u * t * t * s)
        e2 = math.exp(-2 * u)
        first = t * t * (r * r * e2 / (r * r * e2 - 1) + rp * rp * e2 / (rp * rp * e2 - 1))
        second = (1 - t * t) * (r / (1 - r * r * e2) + rp / (1 - rp * rp * e2)) * math.exp(-u)
        return u**3 * (first + second)
    tot = 0.0
    for a_, b_ in ((0, 2), (2, 10), (10, 40), (40, 120)):
        v, _ = integrate.dblquad(f, a_, b_, 0.0, 1.0, epsabs=1e-12, epsrel=1e-9)
        tot += v
    return tot / (2 * math.pi**2)

out['D0_perfect_limit'] = -math.pi**2 / 720
sf = {}
for wpa in (D10, 1.0, 10.0, 50.0, 90.0, 99.0, 110.0, 200.0, 1e4):
    sf[round(wpa, 4)] = U_centre_a4(wpa)
out['D1_U_centre_a4'] = sf
out['D2_sign_at_gold_10nm'] = 'POSITIVE' if sf[round(D10, 4)] > 0 else 'NEGATIVE'
out['D3_gold_distance_where_centre_turns_negative_um'] = 99 * dg * 1e6

for k, v in out.items():
    print(k, '=', v)

assert out['A1_EA_matches_720'] and out['A2_FA_equals_minus_3u0'] and out['A3_traceless']
assert out['A4_isotropic_p'] and out['A5_factor_9'] and out['A6_matches_tolman']
assert out['B1_KC_equals_pi2hbarc_240']
assert eta[6000.0] > 0.95 and eta[10.0] < 0.5
assert abs(out['C2_nonretarded_check_ratio_at_D=1e-3'] - 1) < 0.02
assert abs(sf[1e4] / out['D0_perfect_limit'] - 1) < 0.05
print('ALL ASSERTIONS PASS')
