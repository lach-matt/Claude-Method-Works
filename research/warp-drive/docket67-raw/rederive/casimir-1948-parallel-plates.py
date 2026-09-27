#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for casimir-1948-parallel-plates.

Checks, each against a formula READ at source (quant-ph/0106045 Bordag-Mohideen-
Mostepanenko 2001 review; quant-ph/0204125 Sopova-Ford 2002; quant-ph/0203002
Bressi et al. 2002).  Casimir 1948 itself (Proc. KNAW 51, 793) is NAMED-NOT-READ:
it is read via those restatements.

 A  sympy: zeta-regularised mode sum  -> E/A = -pi^2 hbar c/(720 a^3)
 B  sympy: Abel-Plana closed form (review eq 2.36) and force (2.37) -pi^2/(240 a^4)
 C  sympy: Brown-Maclay energy density = E/(A a); Sopova-Ford eqs (56)+(57) -> U = -pi^2/(720 a^4)
 D  tree's own numbers (candidates.py, achievable.py) from its constants
 E  data: tree constants vs scipy.constants; Bressi K_C vs pi h c/480
 F  numeric Lifshitz plasma model (review eqs 5.53, 4.26): real/ideal pressure and
    interaction-energy ratios at the tree's gaps; cross-check vs review eq 5.60
 G  numeric Sopova-Ford eq (50): midpoint energy density sign vs omega_p a;
    reproduce their a_c = 99/omega_p, then evaluate at the tree's gaps
 H  thermal correction (review eq 5.25) at 300 K

exits 0 when every PASS check passes.
"""
import math, sys
import sympy as sp
import numpy as np
from scipy import integrate, optimize
import scipy.constants as K

fails = 0
def chk(name, ok, detail=""):
    global fails
    print(("PASS " if ok else "FAIL ") + name + ("   " + detail if detail else ""))
    if not ok:
        fails += 1

# ---------------------------------------------------------------- A
print("A. zeta-regularised mode sum (units hbar = c = 1)")
a, s, m, n = sp.symbols('a s m n', positive=True)
# int d^2k/(2pi)^2 (k^2+m^2)^(-s) = m^(2-2s)/(4 pi (s-1)), continued to s = -1/2
k = sp.symbols('k', positive=True)
I_s = sp.integrate(k/(2*sp.pi) * (k**2 + m**2)**(-s), (k, 0, sp.oo), conds='none')
I_s = sp.simplify(I_s)
cont = sp.simplify(I_s.subs(s, sp.Rational(-1, 2)))
chk("transverse integral continued to s=-1/2 equals -m^3/(6 pi)",
    sp.simplify(cont + m**3/(6*sp.pi)) == 0, str(cont))
# E/A = (1/2) * 2 polarisations * sum_{n>=1} (-(n pi/a)^3/(6 pi)); n=0 mode is massless -> 0
E_area = sp.Rational(1, 2) * 2 * (-(sp.pi/a)**3/(6*sp.pi)) * sp.zeta(-3)
chk("E/A = -pi^2/(720 a^3)", sp.simplify(E_area + sp.pi**2/(720*a**3)) == 0, str(sp.simplify(E_area)))

# ---------------------------------------------------------------- B
print("B. Abel-Plana closed form and force")
x = sp.symbols('x', positive=True)
# expand 1/(e^x-1) = sum_n e^{-nx}; int x^3 e^{-nx} = 6/n^4 (sympy), then sum
nn = sp.symbols('nn', positive=True, integer=True)
term3 = sp.integrate(x**3*sp.exp(-nn*x), (x, 0, sp.oo))
bose3 = sp.summation(term3, (nn, 1, sp.oo))
import mpmath
chk("series value agrees with direct quadrature of int x^3/(e^x-1)",
    abs(float(bose3) - float(mpmath.quad(lambda t: t**3/mpmath.expm1(t), [0, mpmath.inf]))) < 1e-12)
chk("int x^3/(e^x-1) = pi^4/15", sp.simplify(bose3 - sp.pi**4/15) == 0)
E236 = -sp.pi**2/(3*a**3) * (1/(2*sp.pi)**4) * bose3
chk("review eq (2.36) -> -pi^2/(720 a^3)", sp.simplify(E236 + sp.pi**2/(720*a**3)) == 0)
F = -sp.diff(E236, a)
chk("force/area = -dE/da = -pi^2/(240 a^4) (review eq 2.37)", sp.simplify(F + sp.pi**2/(240*a**4)) == 0)
# Lifshitz ideal limit (4.26 -> 4.31): 2 int y^2 ln(1-e^-y) = -2 pi^4/45
y = sp.symbols('y', positive=True)
# ln(1-e^-y) = -sum_n e^{-ny}/n; int y^2 e^{-ny} = 2/n^3
term2 = sp.integrate(y**2*sp.exp(-nn*y), (y, 0, sp.oo))
Iln = -sp.summation(term2/nn, (nn, 1, sp.oo))
chk("series value agrees with direct quadrature of int y^2 ln(1-e^-y)",
    abs(float(Iln) - float(mpmath.quad(lambda t: t**2*mpmath.log(-mpmath.expm1(-t)), [0, mpmath.inf]))) < 1e-12)
chk("int y^2 ln(1-e^-y) = -pi^4/45", sp.simplify(Iln + sp.pi**4/45) == 0, str(sp.nsimplify(Iln)))
chk("Lifshitz energy ideal limit (1/(32 pi^2 a^3))(2 Iln) = -pi^2/(720 a^3)",
    sp.simplify(2*Iln/(32*sp.pi**2*a**3) + sp.pi**2/(720*a**3)) == 0)
chk("Lifshitz force ideal limit (1/(32 pi^2 a^4))(2 pi^4/15) = pi^2/(240 a^4)",
    sp.simplify(2*bose3/(32*sp.pi**2*a**4) - sp.pi**2/(240*a**4)) == 0)

# ---------------------------------------------------------------- C
print("C. local energy density for ideal plates")
rho_BM = E236 / a
chk("uniform T00 = (E/A)/a = -pi^2/(720 a^4) (Brown-Maclay, via Sopova-Ford eq 52)",
    sp.simplify(rho_BM + sp.pi**2/(720*a**4)) == 0)
z = sp.symbols('z', positive=True)
E2 = -sp.pi**2/(720*a**4) + sp.pi**2/(16*a**4)*(1+2*sp.cos(sp.pi*z/a)**2)/sp.sin(sp.pi*z/a)**4
B2 = -sp.pi**2/(720*a**4) - sp.pi**2/(16*a**4)*(1+2*sp.cos(sp.pi*z/a)**2)/sp.sin(sp.pi*z/a)**4
chk("Sopova-Ford (56)+(57): (E^2+B^2)/2 = -pi^2/(720 a^4), z-independent",
    sp.simplify((E2+B2)/2 + sp.pi**2/(720*a**4)) == 0)
chk("but <E^2> alone diverges at the plate (z -> 0)", sp.limit(E2, z, 0, '+') == sp.oo)
# trace of Brown-Maclay tensor diag(-1,1,1,-3)*pi^2/(720a^4) with T00 = -rho... check traceless
# (T^mu_mu = -T00 + T11 + T22 + T33 with rho=-pi^2/720a^4, p_perp = +pi^2/720a^4, p_z = -3 pi^2/720a^4)
r0 = sp.pi**2/(720*a**4)
chk("Brown-Maclay tensor traceless: rho=-r0, p_x=p_y=r0, p_z=-3r0 -> -rho+2p+pz ... ",
    sp.simplify(-(-r0) + r0 + r0 + (-3*r0) ) == 0)
chk("p_z = -3 r0 = -pi^2/(240 a^4) equals the attractive pressure", sp.simplify(-3*r0 + sp.pi**2/(240*a**4)) == 0)

# ---------------------------------------------------------------- D
print("D. the tree's numbers from its own constants")
HBAR, C, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
LAM = 9.982529174194637  # phase1.lam() as returned when candidates.py is imported
cas = lambda d: math.pi**2*HBAR*C/(720*d**4)
chk("casimir(1e-8) = 4.33375e4 J/m^3", abs(cas(1e-8)/4.33375e4 - 1) < 1e-5, "%.6e" % cas(1e-8))
chk("casimir(1e-9) = 4.33375e8 J/m^3", abs(cas(1e-9)/4.33375e8 - 1) < 1e-5, "%.6e" % cas(1e-9))
lP = math.sqrt(HBAR*G/C**3)
Rx = math.sqrt(math.pi**2*HBAR*C*G*LAM/(720*C**4))
chk("crossover = l_P pi sqrt(Lambda/720) = 0.369917 l_P", abs(Rx/lP - 0.369917) < 1e-6
    and abs(Rx/lP - math.pi*math.sqrt(LAM/720)) < 1e-12, "%.6f" % (Rx/lP))
chk("crossover in metres 5.978797e-36", abs(Rx/5.978797e-36 - 1) < 1e-6, "%.7e" % Rx)
chk("quantum_bound/casimir_density = 720/pi^2 = 72.951", abs(720/math.pi**2 - 72.951) < 1e-3, "%.4f" % (720/math.pi**2))
chk("corridor factor sqrt(720/pi^2) = 8.541", abs(math.sqrt(720/math.pi**2) - 8.541) < 1e-3)

# ---------------------------------------------------------------- E
print("E. data")
print("   scipy.constants:", K.__name__, "hbar =", K.hbar, " c =", K.c, " G =", K.G,
      " G unc =", K.physical_constants['Newtonian constant of gravitation'][2])
chk("tree HBAR vs SI-exact h/2pi: rel diff < 1e-9", abs(HBAR/K.hbar - 1) < 1e-9, "%.2e" % (HBAR/K.hbar - 1))
chk("tree C = exact c", C == K.c)
chk("tree G = scipy CODATA G", G == K.G)
KC_th = math.pi*K.h*K.c/480
chk("pi h c/480 = pi^2 hbar c/240 = 1.300e-27 N m^2", abs(KC_th - math.pi**2*K.hbar*K.c/240) < 1e-40, "%.4e" % KC_th)
KC_meas, KC_err = 1.22e-27, 0.18e-27
pull = (KC_meas - KC_th)/KC_err
chk("Bressi 2002 K_C = (1.22 +- 0.18)e-27 agrees within 1 sigma", abs(pull) < 1, "pull = %.2f sigma" % pull)

# ---------------------------------------------------------------- F
print("F. Lifshitz plasma model (review eqs 5.53, 4.26), real/ideal at the tree's gaps")
def ratios(a_m, lam_p_m):
    # substitution p = 1/t (dp/p^2 = dt); xi = c x t/(2a); eps = 1 + (omega_p/xi)^2
    wa = 4*math.pi*a_m/lam_p_m   # 2 a omega_p / c
    def refl(xv, t):
        eps_m1 = (wa/(xv*t))**2
        p = 1.0/t
        Kq = math.sqrt(p*p - 1.0 + 1.0 + eps_m1)
        eps = 1.0 + eps_m1
        rtm = (Kq - p*eps)/(Kq + p*eps)
        rte = (Kq - p)/(Kq + p)
        return rtm, rte
    def fF(t, xv):
        rtm, rte = refl(xv, t)
        ex = math.exp(xv)
        return xv**3*(rtm**2/(ex - rtm**2) + rte**2/(ex - rte**2))
    def fE(t, xv):
        rtm, rte = refl(xv, t)
        e = math.exp(-xv)
        return xv**2*(math.log1p(-rtm**2*e) + math.log1p(-rte**2*e))
    IF = integrate.dblquad(fF, 0, 60, 1e-12, 1, epsabs=1e-12, epsrel=1e-8)[0]
    IE = integrate.dblquad(fE, 0, 60, 1e-12, 1, epsabs=1e-12, epsrel=1e-8)[0]
    return IF/(2*math.pi**4/15), IE/(-2*math.pi**4/45)

LAM_AU, LAM_AL = 136e-9, 100e-9   # read: review p.220 (Au 136 nm, Al ~100 nm)
d0 = LAM_AU/(2*math.pi)
etaF_1um, etaE_1um = ratios(1e-6, LAM_AU)
pert = 1 - 16/3*(d0/1e-6) + 24*(d0/1e-6)**2 - 640/7*(1-math.pi**2/210)*(d0/1e-6)**3 \
       + 2800/9*(1-163*math.pi**2/7350)*(d0/1e-6)**4
chk("numeric plasma-model eta_F(Au, 1 um) matches review eq (5.60)", abs(etaF_1um - pert) < 2e-3,
    "numeric %.4f  vs  5.60 %.4f" % (etaF_1um, pert))
chk("review p.154 '10-20% at ~1 um': 1-eta_F(Au,1um) in [0.05,0.25]", 0.05 <= 1-etaF_1um <= 0.25,
    "%.3f" % (1-etaF_1um))
print("   gap        eta_F(Au)  eta_E(Au)  eta_F(Al)  eta_E(Al)   [real/ideal; plasma model, T=0]")
table = {}
for gap in (3e-6, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10):
    fa, ea = ratios(gap, LAM_AU)
    fl, el = ratios(gap, LAM_AL)
    table[gap] = (fa, ea, fl, el)
    print("   %-9.1e  %.4e %.4e %.4e %.4e" % (gap, fa, ea, fl, el))
chk("at 10 nm the ideal formula overstates the Au interaction energy (eta_E < 0.5)", table[1e-8][1] < 0.5,
    "eta_E = %.3f" % table[1e-8][1])
chk("at 0.1 nm (tree's 'atomic floor') eta_E(Au) < 0.05", table[1e-10][1] < 0.05, "eta_E = %.4f" % table[1e-10][1])
chk("small-gap scaling: eta_E(1nm)/eta_E(0.1nm) ~ 10 (non-retarded a^-3 regime)",
    8 < table[1e-9][1]/table[1e-10][1] < 12, "%.2f" % (table[1e-9][1]/table[1e-10][1]))
chk("every real/ideal ratio < 1: real plates give LESS |E|, never more",
    all(v < 1 for row in table.values() for v in row))
bad = K.hbar*K.c/K.e   # hbar c in eV m
print("   hbar omega_p: Au %.2f eV, Al %.2f eV (from lambda_p)" % (2*math.pi*bad/LAM_AU, 2*math.pi*bad/LAM_AL))

# ---------------------------------------------------------------- G
print("G. Sopova-Ford eq (50) midpoint energy density, collisionless plasma, hbar=c=1, omega_p = 1")
def U_mid_a4(wpa):
    # v = u a  ->  a^4 U = (1/2pi^2) int v^3 dv int dt [...] at u = v/a  (omega_p = 1)
    a_ = wpa
    def f(t, v):
        u = v/a_
        s_ = math.sqrt(u*u + 1.0)
        r = (u - s_)/(u + s_)
        num = u*u*t*t + 1.0 - u*t*t*s_
        den = u*u*t*t + 1.0 + u*t*t*s_
        rp = num/den
        e2 = math.exp(-2*v)
        first = t*t*(-(r*r*e2)/(1 - r*r*e2) - (rp*rp*e2)/(1 - rp*rp*e2))   # r^2/(r^2-e^{2ua})
        second = (1 - t*t)*(r/(1 - r*r*e2) + rp/(1 - rp*rp*e2))*math.exp(-v)
        return v**3*(first + second)
    val = integrate.dblquad(f, 1e-12, 80.0, 0, 1, epsabs=1e-13, epsrel=1e-9)[0]
    return val/(2*math.pi**2)
for w in (50, 99, 200, 2000):
    print("   omega_p a = %6d   a^4 U(mid) = %+.5f" % (w, U_mid_a4(w)))
chk("a^4 U(mid) -> -pi^2/720 = -0.01371 as omega_p a grows (Sopova-Ford eq 52)",
    abs(U_mid_a4(20000) + math.pi**2/720) < 1e-3, "%.5f at 2e4" % U_mid_a4(20000))
root = optimize.brentq(U_mid_a4, 30, 400, xtol=1e-3)
chk("sign change of U(mid) near omega_p a = 99 (Sopova-Ford eq 51)", 90 < root < 110, "root %.1f" % root)
ALw = 14.8/(K.hbar*K.c/K.e)   # omega_p/c for Al, 14.8 eV (Sopova-Ford eq 51), 1/m
print("   Al: a_c = root/(omega_p/c) = %.3f um  (paper: 1.3 um)" % (root/ALw*1e6))
chk("Al a_c ~ 1.3 um", 1.2e-6 < root/ALw < 1.45e-6)
for gap in (1e-8, 1e-9, 1e-10):
    w = ALw*gap
    um = U_mid_a4(w)
    print("   Al gap %.0e m: omega_p a = %.4f, a^4 U(mid) = %+.4e  (ideal -0.01371)" % (gap, w, um))
chk("at the tree's 10 nm gap (Al) the plasma-model midpoint energy density is POSITIVE",
    U_mid_a4(ALw*1e-8) > 0)

# ---------------------------------------------------------------- H
print("H. thermal correction, review eq (5.25), T = 300 K")
for gap in (1e-8, 1e-6, 3e-6):
    Teff = K.hbar*K.c/(2*gap*K.k)
    print("   gap %.0e m: T_eff = %.3e K, (1/3)(T/T_eff)^4 = %.3e" % (gap, Teff, (300/Teff)**4/3))
chk("thermal correction at 10 nm < 1e-9 (irrelevant to the tree's rows)",
    (300/(K.hbar*K.c/(2*1e-8*K.k)))**4/3 < 1e-9)

# ---------------------------------------------------------------- I
print("I. what the real-material ratios do to the tree's rows (direction only; plasma model, Au)")
for gap, tag in ((1e-8, "achievable 10 nm row"), (1e-10, "achievable 0.1 nm row")):
    eE = table[gap][1]
    print("   %s: eta_E = %.4g -> corridor b grows by 1/sqrt(eta_E) = %.2f" % (tag, eE, 1/math.sqrt(eE)))
eE1 = table[1e-9][1]
print("   candidates shortfall at R = d = 1 nm: 2.798e52 / eta_E = %.3e" % (2.798e52/eE1))
chk("real-plate correction can only ENLARGE the tree's shortfalls and corridors",
    all(table[g][1] < 1 for g in table))
# small-gap law rho_real ~ (eta_E/d) * pi^2 hbar c/(720 d^3): crossover with c^4/(G Lam R^2)
A_nr = table[1e-10][1]/1e-10 * math.pi**2*HBAR*C/720
R_nr = A_nr*G*LAM/C**4
print("   non-retarded-law crossover R = %.3e m = %.3e l_P (continuum model invalid there too)" % (R_nr, R_nr/lP))
chk("real-law crossover lies even deeper below l_P than the ideal 0.369917 l_P", R_nr/lP < 0.369917)

print("\n%s (%d failure%s)" % ("ALL PASS" if fails == 0 else "FAILURES", fails, "" if fails == 1 else "s"))
sys.exit(1 if fails else 0)
