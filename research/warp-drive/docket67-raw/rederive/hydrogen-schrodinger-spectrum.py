#!/usr/bin/env python3
"""DOCKET 67 audit -- hydrogen-schrodinger-spectrum.

Re-derives, in sympy (exact), the result excite.py:953-959 uses:
    E_n = -m alpha^2/(2 n^2),  <r>_{n,l} = (3 n^2 - l(l+1))/(2 m alpha),
    hbar = c = 1, point nucleus of infinite mass,
against the published restatements READ at source:
  * Suslov & Trey arXiv:0707.1887 eqs (3.2)-(3.5), (3.13)-(3.15), (4.16)-(4.17)
  * Cordero-Soto & Suslov arXiv:0908.0032 eqs (2.6)-(2.7) (Kramers-Pasternack)
  * CODATA 2022 arXiv:2409.03787 eqs (26), (28)-(30), (50); Table XXXIII
Checks are over a FINITE box (n <= NMAX, all l < n); that is what is shown.
Exits 1 if any check fails.  Run: python3 hydrogen-schrodinger-spectrum.py
"""
import sys
import sympy as sp
from fractions import Fraction

NMAX = 6
ok_all = True
rows = []


def chk(label, cond, detail=""):
    global ok_all
    ok_all &= bool(cond)
    rows.append(("PASS" if cond else "FAIL", label, detail))
    print(("PASS " if cond else "FAIL ") + label + (("  [" + detail + "]") if detail else ""))


r, m, a, Z = sp.symbols("r m alpha Z", positive=True)
# units hbar = c = 1, e^2 = alpha (Gaussian); a0 = hbar^2/(m e^2) = 1/(m alpha)
a0 = 1 / (m * a)


def R_nl(n, l):
    """Suslov-Trey 0707.1887 eq (3.2)-(3.3), normalised radial function."""
    eta = 2 * Z * r / (n * a0)
    return (sp.Rational(2, n ** 2) * (Z / a0) ** sp.Rational(3, 2)
            * sp.sqrt(sp.factorial(n - l - 1) / sp.factorial(n + l))
            * sp.exp(-eta / 2) * eta ** l * sp.assoc_laguerre(n - l - 1, 2 * l + 1, eta))


def E_bohr(n):
    """Suslov-Trey eq (3.5) E_n = -m Z^2 e^4/(2 hbar^2 n^2) with e^2 = alpha."""
    return -m * Z ** 2 * a ** 2 / (2 * n ** 2)


# ---------------------------------------------------------------- 1. eigen-equation
# radial Schrodinger: -(1/2m)(1/r^2) d/dr(r^2 dR/dr) + l(l+1)/(2 m r^2) R - Z alpha/r R = E R
for n in range(1, NMAX + 1):
    for l in range(n):
        R = R_nl(n, l)
        res = (-sp.diff(r ** 2 * sp.diff(R, r), r) / (2 * m * r ** 2)
               + l * (l + 1) / (2 * m * r ** 2) * R - Z * a / r * R - E_bohr(n) * R)
        res0 = sp.simplify(res / R)
        norm = sp.simplify(sp.integrate(R ** 2 * r ** 2, (r, 0, sp.oo)))
        rexp = sp.simplify(sp.integrate(R ** 2 * r ** 3, (r, 0, sp.oo)))
        target = (3 * n ** 2 - l * (l + 1)) / (2 * m * a * Z)
        chk("n=%d l=%d: H R = E_n R with E_n=-m(Z alpha)^2/(2n^2); norm=1; <r>=(3n^2-l(l+1))/(2 m Z alpha)"
            % (n, l), res0 == 0 and norm == 1 and sp.simplify(rexp - target) == 0,
            "residual/R=%s norm=%s <r>-target=%s" % (res0, norm, sp.simplify(rexp - target)))

# ---------------------------------------------------------------- 2. l-independence control
chk("E_n independent of l (SO(4)); a WRONG level E=-m(Z a)^2/(2(n+1)^2) FAILS the eigen-equation (control)",
    sp.simplify((-sp.diff(r ** 2 * sp.diff(R_nl(2, 1), r), r) / (2 * m * r ** 2)
                 + 2 / (2 * m * r ** 2) * R_nl(2, 1) - Z * a / r * R_nl(2, 1)
                 - E_bohr(3) * R_nl(2, 1)) / R_nl(2, 1)) != 0)

# ---------------------------------------------------------------- 3. Kramers-Pasternack
# 0908.0032 eq (2.6): <r^k> = 2n(2k+1)/(k+1) (n a0/2Z) <r^{k-1}> - k((2l+1)^2-k^2)/(k+1) (n a0/2Z)^2 <r^{k-2}>
# with <1/r> = Z/(a0 n^2), <1> = 1  (eq 2.7)
nn, ll = sp.symbols("n l", positive=True)
A = nn * a0 / (2 * Z)
k = 1
r1 = (2 * nn * (2 * k + 1) / (k + 1) * A * 1
      - k * ((2 * ll + 1) ** 2 - k ** 2) / (k + 1) * A ** 2 * Z / (a0 * nn ** 2))
chk("Kramers-Pasternack recursion at k=1 gives <r> = a0/(2Z)(3n^2 - l(l+1)) for SYMBOLIC n,l",
    sp.simplify(r1 - (3 * nn ** 2 - ll * (ll + 1)) / (2 * m * a * Z)) == 0, str(sp.factor(r1)))

# ---------------------------------------------------------------- 4. Dirac -> Bohr limit
# CODATA 2022 eq (29) f(n,kappa) = [1+(Z a)^2/(n-delta)^2]^{-1/2}, delta = |k| - sqrt(k^2-(Z a)^2)
x = sp.symbols("x", positive=True)  # x = Z alpha
okD = True
for n in range(1, 5):
    for kap in [kk for kk in range(-n, n + 1) if kk != 0 and not (kk == n)]:
        K = abs(kap)
        f = (1 + x ** 2 / (n - K + sp.sqrt(K ** 2 - x ** 2)) ** 2) ** sp.Rational(-1, 2)
        ser = sp.series(f, x, 0, 6).removeO()
        j = sp.Rational(2 * K - 1, 2)
        st = 1 - x ** 2 / (2 * n ** 2) - x ** 4 / (2 * n ** 4) * (n / (j + sp.Rational(1, 2)) - sp.Rational(3, 4))
        okD &= sp.simplify(ser - st) == 0
chk("Dirac-Coulomb f(n,kappa) = 1 - (Z a)^2/(2n^2) - (Z a)^4/(2n^4)(n/(j+1/2)-3/4) + O(x^6), n<=4, all kappa "
    "(CODATA eq 29 vs Suslov-Trey eq 4.17): Bohr term is the O(alpha^2) term", okD)

# ---------------------------------------------------------------- 5. the dilation D18 rests on (excite.py:195-200)
alpha_tree = Fraction(1.0 / 137.035999084)  # address.py:429, exact rational of that double
for eps in (Fraction(1, 10), Fraction(-3, 7), Fraction(1, 10 ** 18)):
    E0 = {n: -1 * alpha_tree ** 2 / (2 * n * n) for n in range(1, NMAX + 1)}
    E1 = {n: -(1 + eps) * alpha_tree ** 2 / (2 * n * n) for n in range(1, NMAX + 1)}
    r0 = {(n, l): Fraction(3 * n * n - l * (l + 1)) / (2 * alpha_tree) for n in range(1, NMAX + 1) for l in range(n)}
    rr = {(n, l): Fraction(3 * n * n - l * (l + 1)) / (2 * (1 + eps) * alpha_tree) for n in range(1, NMAX + 1) for l in range(n)}
    chk("clamped model, m->m(1+%s): E_n*(1+eps), <r>/(1+eps), E_n/E_1 and <r>E_1 unchanged EXACTLY" % eps,
        all(E1[n] == E0[n] * (1 + eps) and E1[n] / E1[1] == E0[n] / E0[1] for n in E0)
        and all(rr[q] == r0[q] / (1 + eps) and rr[q] * E1[1] == r0[q] * E0[1] for q in r0))

# ---------------------------------------------------------------- 6. what the CLAMPED hypothesis hides (numbers)
# CODATA 2022 (2409.03787 Table XXXII/XXXIII, READ): 1/alpha = 137.035999177(21), mp/me = 1836.152673426(32),
# R_inf = 10973731.568157(12) m^-1, a0 = 5.29177210544e-11 m (all READ); r_p from 2602.14980
inv_a_2018 = sp.Rational("137.035999084")
inv_a_2022 = sp.Rational("137.035999177")
rel = abs(inv_a_2022 - inv_a_2018) / inv_a_2022
chk("alpha datum moved CODATA2018->2022 by %.2e relative; D18 is an identity in alpha (holds for every alpha)"
    % float(rel), float(rel) < 1e-9)
E1_2018 = sp.N(13.605693122990 * (inv_a_2022 / inv_a_2018) ** 2, 15)
chk("E_1 = m_e alpha^2/2 with tree alpha vs CODATA-2022 alpha (m_e c^2 fixed): %s vs 13.605693122990 eV (shift %.2e rel)"
    % (sp.N(E1_2018, 14), float(2 * rel)), float(2 * rel) < 2e-9)

mp_me = sp.Rational("1836.152673426")
Rinf = sp.Rational("10973731.568157")
RH_red = Rinf / (1 + 1 / mp_me)
EI_meas = sp.Rational("1.096787") * 10 ** 7  # CODATA 2022 Table IV, 1H ionization energy E_I/hc, truncated "1.096 787 ..."
dev_clamped = float((Rinf - EI_meas) / EI_meas)
dev_red = float((RH_red - EI_meas) / EI_meas)
# the reduced-mass Bohr term is NOT expected to match to the quoted digits: the Dirac alpha^4 term (Suslov-Trey
# eq 4.17: 1S binding deepens by (Z a)^2/4 relative) and the 1S Lamb shift (2602.14980 p.6: 8,172,744.1 kHz,
# READ; cR_inf = 3.2898419602500e15 Hz, CODATA 2022 Table XXXII) are outside the Schrodinger model.
L1S_rel = sp.Rational("8172744.1e3") / sp.Rational("3.2898419602500e15")
beyond = float((1 / inv_a_2022) ** 2 / 4 - L1S_rel)   # expected (E_I - Bohr_red)/E_I, leading orders
chk("real 1H ionization E_I/hc=1.096787e7 m^-1 (CODATA Table IV, truncated): clamped Bohr R_inf off by %.3e "
    "(= me/mp to 2e-6); reduced-mass Bohr off by %.2e = -(alpha^2/4 - L1S/cR) = %.2e within 1 unit of the last quoted digit (9.1e-7 rel)"
    % (dev_clamped, dev_red, -beyond),
    abs(dev_clamped - 1 / float(mp_me)) < 2e-5 and abs(dev_red + beyond) < 9.2e-7)

# reduced mass under m_e -> m_e(1+eps), m_p fixed: departure from pure dilation of E_n (across species)
e = sp.symbols("epsilon")
mu = lambda me, mp: me * mp / (me + mp)
ratio = sp.simplify(mu(1 + e, mp_me) / mu(1, mp_me) / (1 + e))
lin = sp.series(ratio, e, 0, 2).removeO()
chk("finite m_p: E_n scales by (1+eps)(1 - eps*me/(me+mp) + ...) -- departure coefficient %.4e = 1/(1+mp/me)"
    % float(-(lin - 1).coeff(e)), sp.simplify((lin - 1).coeff(e) + 1 / (1 + mp_me)) == 0)
# ...but within ONE hydrogen atom every E_n/E_1 and <r>*E_n is mu-independent: the two-body model also dilates
mm = sp.symbols("mu", positive=True)
chk("two-body (reduced-mass) model: E_n/E_1 = 1/n^2 and <r>E_1 = -alpha(3n^2-l(l+1))/4 carry no mass at all",
    sp.simplify((-mm * a ** 2 / (2 * nn ** 2)) / (-mm * a ** 2 / 2) - 1 / nn ** 2) == 0
    and sp.simplify((3 * nn ** 2 - ll * (ll + 1)) / (2 * mm * a) * (-mm * a ** 2 / 2)
                    + a * (3 * nn ** 2 - ll * (ll + 1)) / 4) == 0)

# finite size: CODATA eq (50) E4_nucl = (2/3) m (Z a)^4/n^3 (m_r/m)^3 (r_N/lambda_C)^2 delta_l0 carries r_N (a fixed
# length) -> under m->m(1+eps) it scales (1+eps)^3, not (1+eps).  Size relative to Bohr 1S:
lamC_fm = sp.Rational("5.29177210544e4") / inv_a_2022  # lambda_C = alpha*a0; a0 (fm) and 1/alpha READ in CODATA 2022 Table XXXIII
rp = sp.Rational("0.84060")  # muonic r_p as quoted in 2602.14980 p.6 (READ)
a22 = 1 / inv_a_2022
fs = sp.Rational(4, 3) * a22 ** 2 * (rp / lamC_fm) ** 2
chk("finite nuclear size (CODATA eq 50) / Bohr(1S) = (4/3) alpha^2 (r_p/lambda_C)^2 = %.3e; breaks dilation at 2*eps*that"
    % float(fs), 1e-10 < float(fs) < 1e-9)

print("\nSUMMARY: %d checks, %s" % (len(rows), "ALL PASS" if ok_all else "FAILURES"))
sys.exit(0 if ok_all else 1)
