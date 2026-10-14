#!/usr/bin/env python3
"""DOCKET 67, key 1208.5399-sec1.3 -- Fewster, Lectures on QEIs, Sec. 1.3 (p.13-14):
a priori bound T00 >= -C/(2l)^4 on a static trajectory at distance l from the nearer
Casimir plate, and the massless minimally coupled scalar (Dirichlet) Casimir density
'ranges between 3-7% of the bound as z varies in [-L/2, L/2]'.

Re-derived here, independently of the tree (the tree's own function is called only in
section F, read-only, to compare):
  A. C = mu_1^4/(16 pi^2), cos mu cosh mu = 1 (clamped d^4/dt^4); Fewster's 'C ~ 3.17'
     and '-0.20/l^4'.
  B. The density: <phi^2> from the Dirichlet image sum (closed form, sympy), the
     minimal-minus-conformal term (1/6) d_z^2 <phi^2>, compared with Fewster's second
     term; the conformal constant by zeta-regularised mode sum (1440 vs printed 1140).
  C. The ratio R(z) = rho(z) / (C/(2l)^4), l = L/2 - |z|, both constants: range,
     monotonicity, closed-form plate limit 16/mu_1^4.
  D. The window: for a constant density every tau <= 2l is admissible and the bound
     -C/tau^4 is tightest at tau = 2l, so 2l is the best the causal argument allows.
  E. What 'saturation' would need of a SHARP constant: C_sharp = R_max * C.
  F. The owner's reproduction figures (achievable.py:210 '6.8% at the midpoint, 3.4%
     and 3.2% off it'; bounds.py casimir_fraction_of_bound), located in z.
  G. Illustration outside the source, CONDITIONAL on a named, unread hypothesis: the
     perfect-conductor EM density -pi^2/(720 L^4) against the scalar a priori bound.
Exit 0 iff every check passes.
"""
import sys, importlib.util, os
import sympy as sp
import mpmath as mp

mp.mp.dps = 40
FAIL = []
def check(name, ok, extra=""):
    print(("PASS " if ok else "FAIL ") + name + ((" " + extra) if extra else ""))
    if not ok:
        FAIL.append(name)

# ---------------- A. the constant ----------------
k = sp.symbols('k', positive=True)
t = sp.symbols('t', real=True)
# general solution of y'''' = k^4 y on [0,1], clamped both ends: determinant
a1, a2, a3, a4 = sp.symbols('a1:5')
y = a1*sp.cos(k*t) + a2*sp.sin(k*t) + a3*sp.cosh(k*t) + a4*sp.sinh(k*t)
eqs = [y.subs(t, 0), sp.diff(y, t).subs(t, 0), y.subs(t, 1), sp.diff(y, t).subs(t, 1)]
M = sp.Matrix([[sp.diff(e, v) for v in (a1, a2, a3, a4)] for e in eqs])
det = sp.simplify(sp.expand_trig(M.det()))
check("A1 clamped determinant = 2k^2 (1 - cos k cosh k)",
      sp.simplify(det - 2*k**2*(1 - sp.cos(k)*sp.cosh(k))) == 0, str(det))
mu1 = mp.findroot(lambda m: mp.cos(m)*mp.cosh(m) - 1, 4.73)
# no root in (0, mu1): cos k cosh k - 1 < 0 on (0, 4.7)
grid_ok = all(mp.cos(x)*mp.cosh(x) - 1 < 0 for x in mp.linspace(0.01, 4.72, 2000))
check("A2 first positive root mu_1 = 4.7300407448627040260", abs(mu1 - mp.mpf('4.7300407448627040260')) < 1e-18 and grid_ok,
      mp.nstr(mu1, 20))
C = mu1**4/(16*mp.pi**2)
check("A3 C = mu_1^4/(16 pi^2) = 3.1698579383, Fewster's 'C ~ 3.17'", abs(C - mp.mpf('3.17')) < 5e-3, mp.nstr(C, 12))
check("A4 C/16 = 0.19812, Fewster's '-0.20/l^4'", abs(C/16 - mp.mpf('0.20')) < 5e-3, mp.nstr(C/16, 8))

# ---------------- B. the density ----------------
z, L, u = sp.symbols('z L u', real=True)
Lp = sp.symbols('L', positive=True)
# <phi^2>_ren = (1/4pi^2)[ sum_{n!=0} 1/(2nL)^2  -  sum_n 1/((2n+1)L - 2z)^2 ]
#   sum_{n!=0} 1/(4 n^2 L^2) = pi^2/(12 L^2) ;  sum_n 1/(n + 1/2 - z/L)^2 = pi^2/cos^2(pi z/L)
n = sp.symbols('n', integer=True, positive=True)
S1 = 2*sp.summation(1/(4*n**2*Lp**2), (n, 1, sp.oo))
check("B1 sum_{n!=0} 1/(2nL)^2 = pi^2/(12 L^2)", sp.simplify(S1 - sp.pi**2/(12*Lp**2)) == 0)
# numerically confirm the reflection-image sum identity at a sample point
zz, LL = mp.mpf('0.137'), mp.mpf(1)
S2num = mp.nsum(lambda m: 1/((2*m + 1)*LL - 2*zz)**2, [-mp.inf, mp.inf])
check("B2 sum_n 1/((2n+1)L-2z)^2 = pi^2/(4 L^2 cos^2(pi z/L)) (numeric, z=0.137L)",
      abs(S2num - mp.pi**2/(4*LL**2*mp.cos(mp.pi*zz/LL)**2)) < 1e-25)
phi2 = (sp.pi**2/(12*Lp**2) - sp.pi**2/(4*Lp**2*sp.cos(sp.pi*z/Lp)**2))/(4*sp.pi**2)
check("B3 <phi^2> = (1/(48 L^2)) (1 - 3/cos^2(pi z/L))",
      sp.simplify(phi2 - (1 - 3/sp.cos(sp.pi*z/Lp)**2)/(48*Lp**2)) == 0)
# T00(xi) = T00(1/6) - (xi - 1/6) d_z^2 <phi^2>  for a static, z-dependent <phi^2>, signature (-+++)
second = sp.Rational(1, 6)*sp.diff(phi2, z, 2)   # xi = 0
fewster2 = -(sp.pi**2/(48*Lp**4))*(3 - 2*sp.cos(sp.pi*z/Lp)**2)/sp.cos(sp.pi*z/Lp)**4
check("B4 (1/6) d_z^2 <phi^2> equals Fewster's second term exactly",
      sp.simplify(second - fewster2) == 0)
# conformal constant: E/A = (1/2) sum_n INT d^2k/(2pi)^2 sqrt(k^2 + (n pi/L)^2), dim-reg INT = -a^3/(6 pi)
EA = sp.Rational(1, 2)*(-(sp.pi/Lp)**3/(6*sp.pi))*sp.zeta(-3)
check("B5 zeta mode sum: E/A = -pi^2/(1440 L^3)", sp.simplify(EA + sp.pi**2/(1440*Lp**3)) == 0, str(sp.simplify(EA)))
check("B6 conformal density constant is 1440; Fewster's text layer prints 1140 (DISCREPANCY, recorded)", 1440 != 1140)

# ---------------- C. the ratio ----------------
def rho(zL, const):
    c = mp.cos(mp.pi*zL)
    return -mp.pi**2/const - (mp.pi**2/48)*(3 - 2*c**2)/c**4
def R(zL, const):
    ell = mp.mpf(1)/2 - abs(zL)
    return rho(zL, const)/(-C/(2*ell)**4)
for const in (1140, 1440):
    zs = [mp.mpf(i)/2000 for i in range(0, 1000)]
    vals = [R(x, const) for x in zs]
    mono = all(vals[i] > vals[i+1] for i in range(len(vals)-1))
    lim = R(mp.mpf('0.5') - mp.mpf('1e-12'), const)
    check("C1.%d R decreasing in |z| from midpoint to plate" % const, mono)
    check("C2.%d plate limit -> 16/mu_1^4 = %s" % (const, mp.nstr(16/mu1**4, 8)), abs(lim - 16/mu1**4) < 1e-9)
    check("C3.%d range [%.4f%%, %.4f%%] lies inside Fewster's '3-7%%'" % (const, 100*float(16/mu1**4), 100*float(vals[0])),
          mp.mpf('0.03') <= 16/mu1**4 and vals[0] <= mp.mpf('0.07'))
Rmid1140, Rmid1440 = R(0, 1140), R(0, 1440)
print("     midpoint: %.5f%% (1140)  %.5f%% (1440);  plate limit %.5f%% (both)" %
      (100*float(Rmid1140), 100*float(Rmid1440), 100*float(16/mu1**4)))
# plate limit closed form, symbolic: near the plate the second term ~ 1/(16 pi^2 l^4), bound ~ mu^4/(256 pi^2 l^4)
l_ = sp.symbols('l', positive=True); mus = sp.symbols('mu', positive=True)
check("C4 closed form: [1/(16 pi^2 l^4)] / [mu^4/(16 pi^2 (2l)^4)] = 16/mu^4",
      sp.simplify((1/(16*sp.pi**2*l_**4))/(mus**4/(16*sp.pi**2*(2*l_)**4)) - 16/mus**4) == 0)
lead = sp.limit(fewster2.subs(z, Lp/2 - l_)*l_**4, l_, 0)
check("C5 leading plate behaviour of Fewster's second term is -1/(16 pi^2 l^4)", sp.simplify(lead + 1/(16*sp.pi**2)) == 0, str(lead))

# ---------------- D. the window ----------------
# For a density constant in time, Eq.(4) with any tau <= 2l gives rho >= -C/tau^4; -C/tau^4 increases with tau.
taus = [mp.mpf(i)/10 for i in range(1, 21)]
check("D1 -C/tau^4 is increasing in tau, so tau = 2l is the tightest the causal window admits",
      all(-C/taus[i]**4 < -C/taus[i+1]**4 for i in range(len(taus)-1)))

# ---------------- E. saturation against a sharp constant ----------------
# Eq.(3) is 'known not to be optimal' (Fewster p.10). A sharp constant C_s <= C would raise R by C/C_s.
# Saturation at the midpoint would need C_s = R_mid * C.
for const, Rm in ((1140, Rmid1140), (1440, Rmid1440)):
    print("     E.%d saturation at midpoint would need C_sharp = %.5f  (= C / %.3f)" % (const, float(Rm*C), float(1/Rm)))
check("E1 the ratio to a sharper valid bound is >= the ratio to this one (C_s <= C => R C/C_s >= R)", True)

# ---------------- F. owner's figures ----------------
def solve_z(target, const):
    lo, hi = mp.mpf(0), mp.mpf('0.5') - mp.mpf('1e-30')   # R decreasing: R(lo) > target > R(hi)
    for _ in range(200):
        mid = (lo + hi)/2
        if R(mid, const) > target: lo = mid
        else: hi = mid
    return (lo + hi)/2
for const in (1140, 1440):
    z34 = solve_z(mp.mpf('0.034'), const)
    z32 = solve_z(mp.mpf('0.032'), const)
    print("     F.%d R = 3.4%% at z/L = %.4f;  R = 3.2%% at z/L = %.4f;  R(0.2) = %.4f%%, R(0.4) = %.4f%%" %
          (const, float(z34), float(z32), 100*float(R(mp.mpf('0.2'), const)), 100*float(R(mp.mpf('0.4'), const))))
check("F1 '6.8% at the midpoint' is the 1140 value rounded (6.76%); 1440 gives 6.70% -> '6.7%'",
      round(100*float(Rmid1140), 1) == 6.8 and round(100*float(Rmid1440), 1) == 6.7)
check("F2 '3.2% off it' matches z/L = 0.4 (3.20% on 1140)", round(100*float(R(mp.mpf('0.4'), 1140)), 1) == 3.2)
# tree's function, read-only
sys.dont_write_bytecode = True
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, TREE)
try:
    spec = importlib.util.spec_from_file_location("bounds_ro", os.path.join(TREE, "bounds.py"))
    b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
    tv = {x: b.casimir_fraction_of_bound(x) for x in (0.0, 0.2, 0.4)}
    print("     tree bounds.casimir_fraction_of_bound: " + ", ".join("z/L=%.1f -> %.5f%%" % (x, 100*v) for x, v in tv.items()))
    check("F3 tree's function reproduces the 1140 ratio at z/L = 0, 0.2, 0.4 (to 1e-10)",
          all(abs(tv[x] - float(R(mp.mpf(str(x)), 1140))) < 1e-10 for x in tv))
    check("F4 achievable.py's '3.4%%' is the tree's z/L=0.2 value %.3f%% rounded (1140); on 1440 it would round to 3.3%%" % (100*tv[0.2]),
          round(100*tv[0.2], 1) == 3.4 and round(100*float(R(mp.mpf('0.2'), 1440)), 1) == 3.3)
except Exception as e:
    check("F3 import of bounds.py (read-only)", False, repr(e))

# ---------------- G. EM, conditional ----------------
# Perfect-conductor EM density (Brown-Maclay) -pi^2/(720 L^4), uniform. Hypothesis H_EM (NAMED, NOT READ):
# the EM field's a priori bound is at least as weak as the scalar one (|C_EM| >= C); commonly C_EM = 2C (two polarisations).
Rem_mid = (mp.pi**2/720)/C
print("     G  EM uniform density at midpoint: %.4f%% of the SCALAR a priori bound; %.4f%% if C_EM = 2C; -> 0 at the plates"
      % (100*float(Rem_mid), 50*float(Rem_mid)))
check("G1 under H_EM the ideal-plate EM ratio is below the scalar's minimum 16/mu_1^4 everywhere", Rem_mid < 16/mu1**4)

print()
print("%d FAIL" % len(FAIL))
sys.exit(1 if FAIL else 0)
