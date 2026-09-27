#!/usr/bin/env python3
"""DOCKET 67 audit re-derivation: Hu & Verdaguer 0802.0658 Eq. (3.13) as noise.py uses it.

Eq. (3.13) is a DEFINITION (a Gaussian stochastic tensor with mean 0 and covariance N,
N = (1/2)<{t,t}> by Eq. (3.11)).  What is checkable here:
  A. the tree's number built on it: -ln P for P = Prob(xi(f) <= -D), xi(f) ~ N(0, SD_0^2),
     recomputed INDEPENDENTLY of noise.py (constants retyped from CODATA, mpmath erfc at
     60 digits), and its sensitivity to the only moved-able data (G, K_F);
  B. that the smeared covariance of Eq. (3.13) for rho = T_00 is the vacuum variance the
     tree uses: Var_0 = (1/(3360 pi^4)) INT w^7 |fhat|^2 reproduces K = 1/(70 pi^4)
     (Gaussian) and 3/(512 pi^4) (Lorentzian) exactly in sympy;
  C. the source's own caveat ("captures only partially the quantum nature ... since it
     assumes that cumulants of higher order are zero"): the exact vacuum third cumulant of a
     smeared Wick square is NONZERO (2D chiral T, Lorentzian sampler, exact sympy), so the
     true law is not Gaussian -- which the tree already says (H6 != surrogate).
  D. N(f,f) = <t(f)^2> >= 0 for a self-adjoint t(f): the positive semi-definiteness that makes
     (3.13) well defined, checked on B's closed forms (trivially >0) and on C's kappa_2.
Exit 1 on any failed check.
"""
import sys
import sympy as sp
import mpmath as mp

ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)

# ---------------------------------------------------------------- A
mp.mp.dps = 60
HBAR = mp.mpf('1.054571817e-34')        # exact (SI 2019)
C = mp.mpf(299792458)                   # exact
G_2018 = mp.mpf('6.67430e-11')          # CODATA 2018
G_2022 = mp.mpf('6.67430e-11')          # CODATA 2022 (unchanged, u = 1.5e-15)
KF = mp.mpf('19.80242121506098')        # noise.py fixture (tree's own measurement)
m_over_b, a_over_b, b = mp.mpf('5e-3'), mp.mpf('0.02'), mp.mpf(1)

def neg_lnP_log10(G=G_2018, K=KF):
    M = m_over_b * b * C**2 / G
    V = mp.mpf(4) / 3 * mp.pi * (a_over_b * b)**3
    D = M * C**2 / V
    tau = b / C
    sd = mp.sqrt(K) * HBAR / (C**3 * tau**4)
    z = D / sd
    P = mp.erfc(z / mp.sqrt(2)) / 2
    return D, sd, z, mp.log10(-mp.log(P))

D, sd, z, L = neg_lnP_log10()
print("A: D = %s Pa, SD_0 = %s Pa, log10 z = %s, log10(-ln P) = %s"
      % (mp.nstr(D, 8), mp.nstr(sd, 6), mp.nstr(mp.log10(z), 8), mp.nstr(L, 17)))
chk("A1 log10(-ln P) = 141.91579497495206 (noise.py) to 1e-9", abs(L - mp.mpf('141.91579497495206')) < 1e-9)
chk("A2 log10 z = 71.108 (noise.py text) to 1e-3", abs(mp.log10(z) - mp.mpf('71.108')) < 1e-3)
chk("A3 SD_0 = 1.4e-25 Pa (noise.py text) to 2 sig figs", abs(sd / mp.mpf('1.4e-25') - 1) < 0.036)
chk("A4 P below exp(-10^141)", L > 141)
chk("A5 P NOT below exp(-10^142) (the CORRECTED entry)", L < 142)
# sensitivity: G (CODATA 2022 identical), and the K_F margin to each threshold
L22 = neg_lnP_log10(G=G_2022)[3]
chk("A6 CODATA 2022 G leaves the exponent unchanged (|dL| < 1e-12)", abs(L22 - L) < 1e-12)
# G moved by 1e3 x its 2018 standard uncertainty (2.2e-5 rel x 1000 = 2.2%) -- still in (141,142)?
Lg = neg_lnP_log10(G=G_2018 * (1 + mp.mpf('0.022')))[3]
chk("A7 even a 2.2%% shift of G keeps the exponent in (141,142): %s" % mp.nstr(Lg, 8), 141 < Lg < 142)
# K_F factor that would carry the exponent to 142 or 141 (L = 2 log10 z + const; z ~ K^-1/2)
k142 = mp.mpf(10) ** (-(142 - L))        # K -> K * k gives dL = -log10 k
k141 = mp.mpf(10) ** (-(141 - L))
print("A: K_F would have to change by factor %s to reach 10^142, %s to reach 10^141"
      % (mp.nstr(k142, 6), mp.nstr(k141, 6)))
# consistency of the exponent law: -lnP = z^2/2 + ln(z sqrt(2 pi)) + O(1/z^2)
mills = mp.log10(z**2 / 2 + mp.log(z * mp.sqrt(2 * mp.pi)))
chk("A8 Mills asymptotic form agrees with erfc to 1e-40", abs(mills - L) < mp.mpf('1e-40'))

# ---------------------------------------------------------------- B
w, tau = sp.symbols('w tau', positive=True)
var = lambda fhat: sp.integrate(w**7 * fhat**2, (w, 0, sp.oo)) / (3360 * sp.pi**4)
Kg = sp.simplify(var(sp.exp(-w**2 * tau**2 / 4)) * tau**8)   # Gaussian f, fhat(0)=1
Kl = sp.simplify(var(sp.exp(-w * tau)) * tau**8)             # Lorentzian f
print("B: K_Gauss =", Kg, " K_Lorentz =", Kl)
chk("B1 Gaussian K = 1/(70 pi^4)", sp.simplify(Kg - 1 / (70 * sp.pi**4)) == 0)
chk("B2 Lorentzian K = 3/(512 pi^4)", sp.simplify(Kl - sp.Rational(3, 512) / sp.pi**4) == 0)
chk("D1 both smeared noise-kernel variances positive", Kg > 0 and Kl > 0)

# ---------------------------------------------------------------- C
# 2D chiral: W(u) = <d phi(u) d phi(0)> = (1/4pi) INT_0^oo w e^{-iwu} dw;  A = INT f :(d phi)^2:
# kappa2 = 2 INT f1 f2 W12^2 ;  kappa3 = 8 INT f1 f2 f3 W12 W13 W23 (operator order 1,2,3)
# Lorentzian fhat(k) = e^{-tau|k|}.  t1 -> fhat(a+b), t2 -> fhat(a-c), t3 -> fhat(b+c)
a, bb, c = sp.symbols('a b c', positive=True)
k2 = sp.Rational(2) / (4 * sp.pi)**2 * sp.integrate(a * bb * sp.exp(-2 * tau * (a + bb)), (a, 0, sp.oo), (bb, 0, sp.oo))
base = a * bb * c * sp.exp(-tau * (a + bb)) * sp.exp(-tau * (bb + c))
I1 = sp.integrate(base * sp.exp(-tau * (a - c)), (a, c, sp.oo), (c, 0, sp.oo), (bb, 0, sp.oo))   # a > c
I2 = sp.integrate(base * sp.exp(-tau * (c - a)), (c, a, sp.oo), (a, 0, sp.oo), (bb, 0, sp.oo))   # c > a
k3 = sp.simplify(sp.Rational(8) / (4 * sp.pi)**3 * (I1 + I2))
k2 = sp.simplify(k2)
skew = sp.simplify(k3 / k2**sp.Rational(3, 2))
print("C: kappa2 =", k2, " kappa3 =", k3, " skewness =", skew, "=", sp.N(skew, 12))
chk("C1 kappa2 = 1/(128 pi^2 tau^4) > 0", sp.simplify(k2 - 1 / (128 * sp.pi**2 * tau**4)) == 0)
chk("C2 kappa3 != 0: the vacuum law of a smeared Wick square is NOT Gaussian", sp.simplify(k3) != 0)
chk("C3 skewness > 0 (the heavy tail is on the POSITIVE side)", sp.N(skew) > 0)
# if the law is a shifted Gamma (shape alpha), skew = 2/sqrt(alpha): report the implied alpha
alpha = sp.simplify(4 / skew**2)
print("C: implied Gamma shape alpha = 4/skew^2 =", alpha, "=", sp.N(alpha, 12))
# planted-error control: dropping the |a-c| factor must change kappa3
k3bad = sp.simplify(sp.Rational(8) / (4 * sp.pi)**3 * sp.integrate(base, (a, 0, sp.oo), (bb, 0, sp.oo), (c, 0, sp.oo)))
chk("C4 CONTROL: a planted error (drop fhat(a-c)) changes kappa3", sp.simplify(k3bad - k3) != 0)

# C5: the 1D worldline structure of 4D :phi^2: is the same as 2D chiral (d phi)^2 up to scale:
# W_4D(u) = 1/(4 pi^2 (u - i0)^2) = (1/pi) x W_chiral.  Scale the cumulants by pi^-n and compare
# with FFR 1004.0179 Eq. (26) (READ): shifted Gamma alpha = 1/72, beta = 4 pi^2 tau^2/3,
# omega_0 = 1/(96 pi^2 tau^2).  Gamma cumulants: kappa2 = alpha/beta^2, kappa3 = 2 alpha/beta^3.
al, be = sp.Rational(1, 72), 4 * sp.pi**2 * tau**2 / 3
chk("C5 kappa2(4D :phi^2:, Lorentzian) = alpha/beta^2 of FFR Eq. (26)",
    sp.simplify(k2 / sp.pi**2 - al / be**2) == 0)
chk("C5b kappa3(4D :phi^2:, Lorentzian) = 2 alpha/beta^3 of FFR Eq. (26)",
    sp.simplify(k3 / sp.pi**3 - 2 * al / be**3) == 0)
chk("C5c implied lower bound alpha/beta = 1/(96 pi^2 tau^2) (FFR Eq. (26)/(27))",
    sp.simplify(al / be - 1 / (96 * sp.pi**2 * tau**2)) == 0)
# C6: FFR's printed 0.95 probability of a negative outcome: P(Y < omega_0), Y ~ Gamma(alpha, beta),
# beta omega_0 = alpha  =>  P = gammainc_regularised(alpha, 0, alpha)
mp.mp.dps = 30
Pneg = mp.gammainc(mp.mpf(1) / 72, 0, mp.mpf(1) / 72, regularized=True)
print("C6: Prob(negative outcome), true law (Gamma 1/72) = %s ; Gaussian surrogate = 0.5" % mp.nstr(Pneg, 8))
chk("C6 reproduces FFR 1004.0179 p.7 '0.95'", abs(Pneg - mp.mpf('0.95')) < 0.005)
# C7: mass the Gaussian surrogate puts BELOW the quantum law's hard floor -omega_0:
# omega_0/sigma = (alpha/beta)/(sqrt(alpha)/beta) = sqrt(alpha)
Pbelow = mp.erfc(mp.sqrt(mp.mpf(1) / 72) / mp.sqrt(2)) / 2
print("C7: Gaussian mass below the true floor (4D :phi^2:, Lorentzian) = %s (true law: 0)" % mp.nstr(Pbelow, 6))
chk("C7 the surrogate puts > 40 percent of its mass where the quantum law puts none", Pbelow > 0.4)
# C8: the tree's own object -- Fewster's sampler, rho: floor -C/tau^4 is at -(1/SD0_OVER_C) sigma
SD0_OVER_C = mp.sqrt(KF) / (mp.mpf('4.730040744862704')**4 / (16 * mp.pi**2))
Pbelow_rho = mp.erfc(1 / SD0_OVER_C / mp.sqrt(2)) / 2
print("C8: SD_0/(C/tau^4) = %s ; Gaussian mass below -C/tau^4 = %s (H6: 0, by C1)"
      % (mp.nstr(SD0_OVER_C, 8), mp.nstr(Pbelow_rho, 6)))
chk("C8 SD0_OVER_C = 1.4038456 (noise.py import value)", abs(SD0_OVER_C - mp.mpf('1.4038456089684255')) < 1e-6)
chk("C8b the surrogate puts > 20 percent of its mass below the QEI floor of the tree's own operator", Pbelow_rho > 0.2)

print("ALL PASS" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
