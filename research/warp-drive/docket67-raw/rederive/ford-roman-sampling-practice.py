#!/usr/bin/env python3
"""DOCKET 67 -- ford-roman-sampling-practice.
Re-derives (i) the tree's 3989 l_P (achievable.py:119-121, not computed in that
file's code), (ii) the 'four decades' wording, (iii) Ford & Roman gr-qc/9510071's
own f-examples (eqs 51, 69, 88, Sec.5), (iv) Pfenning-Ford's alpha = 1/10 example,
(v) how far the tree's 'geometric scale' (core radius a) sits from F&R's scale
(minimum local proper radius of curvature r_m) in the tree's own core geometry.
Read-only against research/: achievable.py is imported with bytecode writing off.
Exit 0 iff every check passes."""
import sys, math, importlib.util
sys.dont_write_bytecode = True
import sympy as sp

OK = True
def chk(label, got, want, rtol):
    global OK
    good = abs(got - want) <= rtol * abs(want)
    OK &= good
    print("  %-66s got %-14.6g want %-12.6g %s" % (label, got, want, "ok" if good else "FAIL"))

spec = importlib.util.spec_from_file_location(
    "achievable", "/home/user/Claude-Method-Works/research/warp-drive/achievable.py")
A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
LP = A.L_PLANCK

print("(1) the tree's printed crossing, from its own code")
a0 = A.crossing_radius() * A.A_OVER_B
chk("achievable crossing core a (l_P), sampling length = a, no coefficient", a0 / LP, 4.0933, 1e-4)

print("(2) symbolic crossing with sampling length f*a and coefficient kappa")
hb, c, G, a, f, kap, K = sp.symbols('hbar c G a f kappa K', positive=True)
b = a / sp.Rational(1, 50)                       # a = 0.02 b
eq = sp.Eq(kap * hb * c / (f * a) ** 4, K * c ** 4 / (G * b ** 2))
sol = [s for s in sp.solve(eq, a) if s.is_positive is not False][0]
print("   a_cross =", sp.simplify(sol))
ratio = sp.simplify(sol / sol.subs({f: 1, kap: 1}))
print("   a_cross(f,kappa)/a_cross(1,1) =", ratio)
assert sp.simplify(ratio - sp.sqrt(kap) / f ** 2) == 0
kFR = sp.Rational(3, 32) / sp.pi ** 2
a_FR_f1 = float(a0 / LP * sp.sqrt(kFR))
a_FR_f001 = float(a0 / LP * sp.sqrt(kFR) / sp.Rational(1, 100) ** 2)
a_FR_f01 = float(a0 / LP * sp.sqrt(kFR) / sp.Rational(1, 10) ** 2)
chk("F&R coefficient, f = 1   (l_P)", a_FR_f1, 0.39894, 1e-3)
chk("F&R coefficient, f = 0.1 (l_P)  [F&R Sec.4.5 / P-F alpha]", a_FR_f01, 39.894, 1e-3)
chk("F&R coefficient, f = 0.01 (l_P) -- the tree's 3989", a_FR_f001, 3989.4, 1e-3)
# direct numeric root: solve ford_roman_allow(0.01*a/c) = required_density(a/0.02)
lo, hi = 1e-34, 1e-28
g = lambda x: A.ford_roman_allow(0.01 * x / A.C_SI) - A.required_density(x / A.A_OVER_B)
for _ in range(300):
    mid = math.sqrt(lo * hi)
    if g(lo) * g(mid) <= 0: hi = mid
    else: lo = mid
chk("numeric root ford_roman_allow(0.01 a/c) = required_density(a/0.02) (l_P)", mid / LP, 3989.4, 1e-3)

print("(3) 'four decades away' -- from which baseline?")
d_from_printed = math.log10(a_FR_f001 / (a0 / LP))
d_from_FRf1 = math.log10(a_FR_f001 / a_FR_f1)
chk("decades from the printed 4.0933 l_P", d_from_printed, 2.989, 1e-3)
chk("decades from F&R-coefficient f = 1 crossing 0.399 l_P", d_from_FRf1, 4.0, 1e-9)
print("   -> 'four decades' is the f^-2 move alone; from the 4.09 the adjacent sentence")
print("      prints, the move is 2.99 decades (coefficient sqrt(3/32pi^2) = %.5f absorbs one)."
      % float(sp.sqrt(kFR)))

print("(4) Ford & Roman gr-qc/9510071's own f-examples, re-derived (Planck units)")
r0, ff = sp.symbols('r0 f', positive=True)
cc = sp.Rational(3, 32) / sp.pi ** 2
# Sec.4.1: Phi = 0, b = r0^2/r; rho at throat = -1/(8 pi r0^2); tau0 = f r0 ; eq (50)
rmax = sp.solve(sp.Eq(1 / (8 * sp.pi * r0 ** 2), cc / (ff * r0) ** 4), r0)[0]
print("   eq(51) r0 <~", sp.simplify(rmax), " (printed: l_p/(2 f^2))")
coef51 = float(sp.sqrt(3 / (4 * sp.pi)))
chk("eq(51) coefficient sqrt(3/4pi) vs printed 1/2", coef51, 0.5, 0.03)
chk("eq(51) at f = 0.01: r0 (l_p)  [printed '~10^4 l_p']", coef51 / 0.01 ** 2, 4886.0, 1e-3)
# eq (69): a0 <~ (r0/(8 f^4 l_p))^(1/3) l_p ; r0 = 1 m, f = 0.01, printed 10^14 l_p
a69 = (1.0 / LP / (8 * 0.01 ** 4)) ** (1 / 3)
chk("eq(69) r0 = 1 m, f = 0.01: a0 (l_p)  [printed 10^14]", math.log10(a69), 13.96, 2e-3)
# eq (88): r0 >~ f^2 s^2, f = 0.1, s = 1e23 l_p -> 1e44 l_p ~ 0.01 AU
r88 = 0.1 ** 2 * (1e23) ** 2
chk("eq(88) f = 0.1, s = 1e23 l_p: r0 (l_p)", r88, 1e44, 1e-9)
chk("        in AU  [printed '~0.01 A.U.']", r88 * LP / 1.495978707e11, 0.0108, 1e-2)
# Sec.5: r0 <~ l_p/f^2 at f = 0.01 -> 10^4
chk("Sec.5 r0 <~ l_p/f^2 at f = 0.01 (l_p)", 1 / 0.01 ** 2, 1e4, 1e-12)

print("(5) Pfenning-Ford gr-qc/9702026 eq.(22)-(23): Delta <= (3/4)sqrt(3/pi) v_b/alpha^2")
chk("alpha = 1/10 (their example) -> Delta/(v_b l_P)  [printed '10^2']",
    0.75 * math.sqrt(3 / math.pi) / 0.1 ** 2, 73.29, 1e-3)
print("   P-F's sampling fraction is a TENTH, not a hundredth.")

print("(6) the tree's 'geometric scale' a vs F&R's r_m, in the tree's own core")
comp = A.M_OVER_B / A.A_OVER_B             # G m /(c^2 a) = 0.25
# uniform ball interior: 8 pi G rho/c^2 = 6 G m/(c^2 a^3); tidal (Newtonian) Gm/(c^2 a^3)
rc_ricci = 1 / math.sqrt(6 * comp)          # in units of a
rc_tidal = 1 / math.sqrt(comp)
chk("G m/(c^2 a)", comp, 0.25, 1e-12)
chk("r_c from 8 pi G rho/c^2, units of a", rc_ricci, 0.8165, 1e-3)
chk("r_c from tidal G m/(c^2 a^3), units of a", rc_tidal, 2.0, 1e-12)
lo_c, hi_c = a_FR_f001 / rc_ricci ** 2, a_FR_f001 / rc_tidal ** 2
print("   crossing with tau0 = 0.01 r_c instead of 0.01 a: %.0f .. %.0f l_P (vs 3989)" % (hi_c, lo_c))
print("   -> the substitution a -> r_m moves the figure by < 1 decade; order unchanged.")

print("\nRESULT:", "ALL CHECKS PASS" if OK else "FAILURES")
sys.exit(0 if OK else 1)
