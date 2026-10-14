#!/usr/bin/env python3
"""DOCKET 67 audit: Le App. K worked burn, delta_eta/lambda = 2.0.
Source READ: arXiv:2606.22531v2 (30 Jun 2026) text cached from an earlier alphaXiv
tool result at scratchpad/d67/src/casmag/all/2606.22531v3.txt (its own header line
reads 'arXiv:2606.22531v2 [gr-qc] 30 Jun 2026'), p.45 (App. K paragraph) and p.28.
Checks, none of which writes under research/.  Geometric units G=c=1, R=1."""
import sys, math, importlib.util
sys.dont_write_bytecode = True
import sympy as sp

ok = True
def chk(label, got, want, tol=0.0):
    global ok
    good = abs(float(got) - float(want)) <= tol if tol else got == want
    ok &= bool(good)
    print("  %-66s %-18s %-14s %s" % (label, got if not isinstance(got, float) else "%.10g" % got,
                                       want if not isinstance(want, float) else "%.10g" % want,
                                       "ok" if good else "FAIL"))

print("C1  Le's printed parameters (p.45): x*=0.3, lambda_max=0.12, rapidity gain 0.24, ~51%")
de, lm, x = sp.Rational(24, 100), sp.Rational(12, 100), sp.Rational(3, 10)
chk("delta_eta/lambda_max exact", de / lm, sp.Integer(2))
chk("float 0.24/0.12 (the tree's sf)", 0.24 / 0.12, 2.0, 1e-15)
rad = 1 - sp.exp(-3 * de)
chk("radiated fraction 1-e^{-0.72} (Le: 'approx 51%')", float(rad), 0.5132477440, 1e-9)
chk("  rounds to 51%", round(float(rad) * 100), 51)
chk("lambda_max < Prop.5 ceiling (1-x)/2 = 0.35", bool(lm < (1 - x) / 2), True)
chk("x + 2 lambda_max = 0.54 < 4/5 (operative window)", bool(x + 2 * lm < sp.Rational(4, 5)), True)

print("\nC2  the sin^2 profile of App. K: a(u) = a_max sin^2(pi u/T)")
u, T, a = sp.symbols("u T a_max", positive=True)
I = sp.integrate(a * sp.sin(sp.pi * u / T) ** 2, (u, 0, T))
chk("INT a du = a_max T/2 (sympy)", sp.simplify(I - a * T / 2), sp.Integer(0))
Tburn = sp.solve(sp.Eq(a * T / 2, de), T)[0].subs(a, lm)   # R = 1
chk("full burn duration T in units R (retarded time u)", Tburn, sp.Integer(4))
chk("constant-a reading tau = delta_eta/a_max (the tree's) ", de / lm, sp.Integer(2))
# duration over which a >= a_max/2: sin^2 >= 1/2 on the middle half of the burn
chk("time with a >= a_max/2 (FWHM) in units R", Tburn / 2, sp.Integer(2))
chk("mean acceleration over the burn / a_max", sp.integrate(sp.sin(sp.pi*u/T)**2,(u,0,T))/T, sp.Rational(1,2))

print("\nC3  budget along the profile: m' = -3 m a integrates to e^{-3 eta}")
m = sp.Function("m")
sol = sp.dsolve(sp.Eq(m(u).diff(u), -3 * m(u) * a * sp.sin(sp.pi * u / T) ** 2), m(u), ics={m(0): 1})
mf = sp.simplify(sol.rhs.subs(u, T))
chk("m_f/m_0 == e^{-3 a_max T/2} (sympy dsolve)", sp.simplify(mf - sp.exp(-3 * a * T / 2)), sp.Integer(0))

print("\nC4  the tree's own numbers, imported read-only (no bytecode written)")
spec = importlib.util.spec_from_file_location(
    "wall", "/home/user/Claude-Method-Works/research/warp-drive/wall.py")
wall = importlib.util.module_from_spec(spec); spec.loader.exec_module(wall)
W = wall.omega_scaled(0.3, 0.5)
lew = wall.adiabatic_margin(0.24, 1.0, 1.0, 0.3, 0.5) * wall.lam(1.0, 1.0) / 0.12
print("      W(0.3, 0.5) = %.10f   (V''R^2 = %.10f)" % (W, wall.Vpp(0.3, 0.5)))
chk("wall.py:575 lew == 2 W", lew, 2.0 * W, 1e-12)
chk("wall.py:64 'adiabatic by only 2.4'", round(lew, 1), 2.4)
chk("wall.py:698 hardcoded sf=2.0 == 0.24/0.12", 2.0, 0.24 / 0.12, 1e-15)
chk("wall.py:576 lew < 5", lew < 5.0, True)
lew_profile = float(Tburn) * W
print("      with the App. K profile's full duration T = 4 R: margin = 4 W = %.6f" % lew_profile)
chk("  still < 5 on the full duration (the tree's < 5 survives, narrowly)", lew_profile < 5.0, True)
chk("  margin on full duration", lew_profile, 4.0 * W, 1e-12)
shortfall_profile = float(Tburn)
chk("marginal-wall shortfall on full duration (tau_efold = R): 4, not 2", shortfall_profile, 4.0, 1e-15)

print("\nC5  what an O(1) coefficient in tau_efold does to 'fails by 2.0'")
# Le p.28: tau_efold = sqrt(2/|V''|), 'of order a light-crossing time'.  The tree
# sets tau_efold = R.  Write tau_efold = k R.  The burn outruns iff tau_burn <= k R.
for lbl, tb in (("constant-a reading tau_burn = 2R", 2.0), ("full sin^2 duration 4R", 4.0)):
    kflip = tb
    Vflip = 2.0 / kflip ** 2
    print("      %-36s flips to PASS iff k >= %.1f, i.e. |V''|R^2 <= %.4f" % (lbl, kflip, Vflip))
chk("verdict is coefficient-dependent: k = 2 flips the tree's reading", 2.0 / 2.0 <= 1.0, True)
chk("  k = 1 (the tree's choice) fails it", 2.0 / 1.0 <= 1.0, False)

print("\nC6  proper-time vs retarded-time factor at the static anchor x = 0.3")
s = math.sqrt(1 - 0.3)
print("      sqrt(1-x) = %.6f : a static shell's proper time per unit u (Schwarzschild anchor)" % s)
chk("the O(1) clock factor is < 1 and > 0.8 -- it does not flip a factor-2 miss by itself",
    0.8 < s < 1.0, True)

print("\n  REDERIVE %s" % ("OK" if ok else "FAILED"))
sys.exit(0 if ok else 1)
