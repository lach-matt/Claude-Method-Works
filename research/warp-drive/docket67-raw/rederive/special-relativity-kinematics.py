#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key special-relativity-kinematics.

Owner under audit: research/warp-drive/arrival.py (read-only here; imported by path, never edited).
Checks, each printed PASS/FAIL/RECORD:
  A. Minkowski line element -> proper time of an inertial worldline: tau = D/(beta*gamma*c)   (sympy, exact)
  B. Boost preserves the interval; gamma(beta)=1/sqrt(1-beta^2) is the boost's time coefficient (sympy)
  C. Identity sqrt((1+b)/(1-b)) == gamma(1+b) on 0<=b<1 (sympy + z3 nlsat)
  D. (gamma-1) m c^2 -> m v^2/2 as beta -> 0 (sympy series)
  E. Numbers in arrival.py: gamma(0.866), sqrt(3)/2, trip and shipboard times, LY constant
  F. Constant-beta figure is a strict FLOOR on proper time for any trip whose peak speed is beta
     (monotonicity of beta*gamma, sympy) and its size at finite acceleration (hyperbolic motion, exact)
  G. Flat-spacetime hypothesis: size of the gravitational term dropped (weak-field, order of magnitude)
  H. Distance sensitivity: d(ln tau)/d(ln D) = 1 exactly (so any distance revision moves times 1:1)
  I. Prose-vs-code in rests_on_it sites of arrival.py report (RECORD only -- discrepancies, not errors in SR)
"""
import math, importlib.util, sys
import sympy as sp

ok = True
def res(label, good, detail=""):
    global ok
    ok &= bool(good)
    print("  %-72s %s %s" % (label, "PASS" if good else "FAIL", detail))
def rec(label, detail):
    print("  %-72s RECORD %s" % (label, detail))

spec = importlib.util.spec_from_file_location(
    "arrival", "/home/user/Claude-Method-Works/research/warp-drive/arrival.py")
A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)

b, c, D, t, x, m, v, a, tau = sp.symbols('beta c D t x m v a tau', positive=True)
g = 1/sp.sqrt(1-b**2)

print("A. proper time of an inertial worldline from ds^2 = c^2 dt^2 - dx^2")
# worldline x = beta c t; dtau = sqrt(dt^2 - dx^2/c^2)
dtau_dt = sp.sqrt(1 - (sp.diff(b*c*t, t))**2/c**2)
T = D/(b*c)                                   # coordinate time to cover D
tau_exact = sp.simplify(dtau_dt*T)
res("tau = D/(beta*gamma*c)", sp.simplify(tau_exact - D/(b*g*c)) == 0, str(tau_exact))

print("B. Lorentz boost preserves the interval; time coefficient is gamma")
ct, X = sp.symbols('ct X', real=True)
ctp = g*(ct - b*X); Xp = g*(X - b*ct)
res("(ct')^2 - x'^2 == ct^2 - x^2", sp.simplify(ctp**2 - Xp**2 - (ct**2 - X**2)) == 0)
# clock at rest in primed frame: X = beta ct -> ct' = ct/gamma
res("moving clock: t' = t/gamma", sp.simplify(ctp.subs(X, b*ct) - ct/g) == 0)
# composition law (1+1D): gamma(b1 (+) b2) = g1 g2 (1 + b1 b2)
b1, b2 = sp.symbols('b1 b2', positive=True)
bc = (b1+b2)/(1+b1*b2)
gc = 1/sp.sqrt(1-bc**2)
res("gamma(b1+b2 relativistic) == g1 g2 (1+b1 b2)",
    sp.simplify(gc**2 - (1/(1-b1**2))*(1/(1-b2**2))*(1+b1*b2)**2) == 0)

print("C. photon-rocket identity used as a self-check at arrival.py:71-73")
lhs = sp.sqrt((1+b)/(1-b)); rhs = g*(1+b)
res("squares agree: (1+b)/(1-b) == gamma^2 (1+b)^2", sp.simplify(lhs**2 - rhs**2) == 0)
try:
    import z3
    B = z3.Real('B'); G = z3.Real('G'); L = z3.Real('L')
    s = z3.Solver()
    s.add(B >= 0, B < 1, G > 0, G*G*(1-B*B) == 1, L > 0, L*L*(1-B) == 1+B, L != G*(1+B))
    r = s.check()
    res("z3: no 0<=b<1 with sqrt((1+b)/(1-b)) != gamma(1+b)", r == z3.unsat, str(r))
except ImportError:
    rec("z3 not installed", "skipped")

print("D. kinetic energy (gamma-1)mc^2 used by magsail_distance (arrival.py:51)")
KE = (1/sp.sqrt(1-v**2/c**2) - 1)*m*c**2
ser = sp.series(KE, v, 0, 5).removeO()
res("(gamma-1)mc^2 = m v^2/2 + 3 m v^4/(8 c^2) + O(v^6)",
    sp.simplify(ser - (m*v**2/2 + 3*m*v**4/(8*c**2))) == 0)

print("E. numbers printed and pinned by arrival.py")
res("gamma(sqrt(3)/2) == 2 exactly", sp.simplify(g.subs(b, sp.sqrt(3)/2) - 2) == 0)
gv = A.gamma(0.866)
res("arrival.gamma(0.866) = 1.999824 (rel. err to 2: %.2e < tol 1e-3)" % (abs(gv-2)/2),
    abs(gv - 1.9998244) < 1e-6 and abs(gv-2)/2 < 1e-3, "%.7f" % gv)
res("trip 4.24 ly @0.866 = 4.89607 yr", abs(A.trip_time_ly(4.24, 0.866) - 4.24/0.866) < 1e-12)
pt = A.proper_time_ly(4.24, 0.866)
res("shipboard 4.24 ly @0.866 = 2.44825 yr (selftest pins 2.4487 at tol 1e-3)",
    abs(pt - 4.24*math.sqrt(1-0.866**2)/0.866) < 1e-12, "%.5f" % pt)
rec("selftest pin 2.4487 vs computed 2.44825", "rel diff %.1e (inside its stated tol 1e-3; pin was written for gamma=2 exactly: 4.24/(0.866*2)=%.5f)"
    % (abs(pt-2.4487)/2.4487, 4.24/(0.866*2)))
res("LY = Julian year * c = 9460730472580800 m (arrival.py uses 9.4607304726e15)",
    abs(365.25*86400*A.c - A.LY)/A.LY < 1e-10, "%.6e" % (365.25*86400*A.c))
res("c = 299792458 m/s exact (SI definition)", A.c == 299792458.0)

print("F. constant-beta idealisation: a floor on proper time, and its size at finite acceleration")
bg = b*g
res("d(beta*gamma)/d(beta) = gamma^3 > 0 on (0,1)  => dtau/dx = 1/(c beta gamma) decreasing in beta",
    sp.simplify(sp.diff(bg, b) - g**3) == 0)
rec("consequence", "for ANY speed profile with max beta_p over distance D: tau >= D/(c beta_p gamma_p); "
    "equality only if |v| = beta_p c everywhere (instantaneous boosts). Same for Earth time t >= D/(beta_p c).")
# hyperbolic motion at proper acceleration a from rest to beta_p (units c=1, ly, yr)
g0 = 9.80665; cc = A.c; yr = 365.25*86400
a_ly = g0*yr**2/A.LY               # 1 g in ly/yr^2 (c = 1 ly/yr)
bp = 0.866; gp = 1/math.sqrt(1-bp*bp); w = math.atanh(bp)
tau_acc = w/a_ly; t_acc = gp*bp/a_ly; x_acc = (gp-1)/a_ly
Dly = 4.24
x_cruise = Dly - 2*x_acc
tau_1g = 2*tau_acc + x_cruise/(bp*gp); t_1g = 2*t_acc + x_cruise/bp
res("1 g ramp distance to 0.866c = (gamma-1)c^2/a = %.3f ly (< D/2, profile feasible)" % x_acc, x_acc < Dly/2)
rec("4.24 ly, peak 0.866c, 1 g accel + 1 g brake",
    "shipboard %.3f yr vs constant-beta %.3f yr (+%.0f%%); Earth %.3f vs %.3f yr (+%.0f%%)"
    % (tau_1g, pt, 100*(tau_1g/pt-1), t_1g, Dly/bp, 100*(t_1g/(Dly/bp)-1)))
res("finite-acceleration shipboard time exceeds the constant-beta figure", tau_1g > pt)
# the shell at 0.0476c: same test
bs = 0.0476; gs = 1/math.sqrt(1-bs*bs)
xs = (gs-1)/a_ly; tau_s = 2*math.atanh(bs)/a_ly + (Dly-2*xs)/(bs*gs)
rec("same at 0.0476c, 1 g", "shipboard %.4f vs %.4f yr (+%.3f%%) -- negligible at low beta"
    % (tau_s, A.proper_time_ly(Dly, bs), 100*(tau_s/A.proper_time_ly(Dly, bs)-1)))

print("G. flat-spacetime hypothesis: size of the dropped gravitational term (weak field, GM/(r c^2))")
GM_sun = 1.32712440018e20   # value as recalled (IAU nominal); NOT READ in this run -- order of magnitude only
phi_1au = GM_sun/(A.AU*cc**2)
rec("GM_sun/(1 AU c^2)", "%.2e  (vs tree tolerance 1e-3 and vs gamma-1 = 1.1e-3 at 0.0476c)" % phi_1au)
rr = phi_1au/(gs-1)
res("dropped term / (gamma-1) at 0.0476c = %.1e  (< 1e-4)" % rr, rr < 1e-4)
rec("scope", "cruise only; near a compact deflector (the arrival network's nodes) GM/(r c^2) is O(0.1) and the flat hypothesis fails there -- the tree does not apply gamma there")

print("H. sensitivity to the one astronomical datum (distance 4.24 ly)")
res("tau and t are linear in D: d ln tau / d ln D = 1",
    sp.simplify(sp.diff(sp.log(D/(b*g*c)), D)*D - 1) == 0)
rec("any revision dD/D moves both times by the same dD/D", "ratio shipboard/Earth = 1/gamma independent of D")

print("I. prose vs code at rests_on_it sites of arrival.py report (RECORD, not SR findings)")
d_1000km = A.magsail_distance(1e6, 0.0476, 1e12)/A.AU
d_087 = A.magsail_distance(1e6, 0.866, 1e12)/A.LY
rec("arrival.py:150-151 prose '810 AU' (1000 km sail, 1000 t, 0.048c)", "code prints %.0f AU" % d_1000km)
rec("arrival.py:152 prose '2.6 ly' (same sail from 0.87c)", "code prints %.3f ly" % d_087)
r_speed = 0.866/0.0476
f1 = A.photon_mass_ratio(0.866)-1; f0 = A.photon_mass_ratio(0.0476)-1
rec("arrival.py:137 prose '18x the speed for 76x the fuel ratio'",
    "speed ratio %.1f; fuel-per-tonne ratio %.1f; M0/M1 ratio %.2f; ln(M0/M1) ratio %.1f -- 76 not reproduced by these"
    % (r_speed, f1/f0, A.photon_mass_ratio(0.866)/A.photon_mass_ratio(0.0476),
       math.log(A.photon_mass_ratio(0.866))/math.log(A.photon_mass_ratio(0.0476))))
res("the gamma values in all three sites are the SR values (discrepancies are not in gamma)",
    abs(A.gamma(0.0476) - 1/math.sqrt(1-0.0476**2)) < 1e-15)

print("\nOVERALL %s" % ("PASS" if ok else "FAIL"))
sys.exit(0 if ok else 1)
