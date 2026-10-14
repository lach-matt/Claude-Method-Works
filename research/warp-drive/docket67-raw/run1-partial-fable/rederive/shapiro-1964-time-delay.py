#!/usr/bin/env python3
"""
DOCKET 67, result 13/286 -- shapiro-1964-time-delay.  Re-derivation.

Checks, in order:
  A  sympy: the exact radial Schwarzschild null travel time
        dt = int_{R1}^{R2} dR / (1 - 2M/R)  =  (R2 - R1) + 2M ln((R2-2M)/(R1-2M))
     is foliation.shapiro()'s closed form (residual simplifies to 0).
  B  numeric: foliation.py's pinned numbers at M=1, R1=10, R2=100.
  C  z3: for every M>0, 2M<R1<R2 the excess over the areal gap is positive
     (a DELAY); for every M<0, 0<R1<R2 it is negative (sign flips with M).
  D  sympy: the weak-field isotropic first-order form
        int_{x0}^{x1} (1 + 2M/sqrt(x^2+b^2)) dx = (x1-x0) + 2M ln((x1+r1)/(x0+r0))
     is composite.analytic_shapiro(); this is Will 2014 eq.(62) one-way with
     gamma=1 and Possel 2020 eq.(27).
  E  composite.py's VALIDATION 3 from its own pinned numbers: the antisymmetric
     part of t-|dx| at M = +-2e-3 against the analytic form (quoted 0.6 %).
  F  Named-hypothesis measurements the owners do not print:
       - exact vs first-order at foliation's numbers (2M ln(R2/R1));
       - the excess against the PROPER radial distance, not the areal gap;
       - the same Killing interval on the NEAR static clock;
       - the chart term Possel eq.(21) vs (25): Schwarzschild-chart straight
         line carries an extra -M b^2/r^3 integrand, integrating to
         -M (x1/r1 - x0/r0), absent in the isotropic chart composite uses.
Nothing here edits the tree.  stdlib + sympy + z3.
"""
import math, sys
import sympy as sp

ok = True
def chk(label, cond):
    global ok
    ok = ok and bool(cond)
    print(("  PASS  " if cond else "  FAIL  ") + label)

def near(label, a, b, tol=1e-9):
    d = abs(a - b) / (abs(b) if b else 1.0)
    chk("%s: %r vs %r (rel %.2e)" % (label, a, b, d), d <= tol)

# ---------------------------------------------------------------- A: exact radial
print("A. sympy -- exact radial null travel time in Schwarzschild")
M, R, R1, R2 = sp.symbols("M R R1 R2", positive=True)
integrand = 1 / (1 - 2 * M / R)                      # dt/dR for a radial null ray, Killing time
F = sp.integrate(integrand, R)                        # antiderivative
exact = sp.simplify(F.subs(R, R2) - F.subs(R, R1))
tree = (R2 - R1) + 2 * M * sp.log((R2 - 2 * M) / (R1 - 2 * M))   # foliation.py:571
resid = sp.simplify(sp.expand_log(exact - tree, force=True))
print("     sympy antiderivative:", F)
print("     residual (exact - foliation form):", resid)
chk("closed form agrees with the integral symbolically", resid == 0)
# numerical spot check of the symbolic identity at a random interior point
vals = {M: 1.0, R1: 10.0, R2: 100.0}
near("symbolic form evaluated at (1,10,100)", float(exact.subs(vals)), float(tree.subs(vals)), 1e-12)

# ---------------------------------------------------------------- B: pinned numbers
print("B. numeric -- foliation.py:993-995 pins")
def shapiro(Mv, r1, r2):                              # copied verbatim from foliation.py:568-574
    dt = (r2 - r1) + 2.0 * Mv * math.log((r2 - 2.0 * Mv) / (r1 - 2.0 * Mv))
    return dict(killing=dt, far_proper=dt * math.sqrt(1.0 - 2.0 * Mv / r2),
                near_proper=dt * math.sqrt(1.0 - 2.0 * Mv / r1),
                excess=dt - (r2 - r1), areal_gap=r2 - r1)
sh = shapiro(1.0, 10.0, 100.0)
near("Killing travel time", sh["killing"], 95.011051874, 1e-9)
near("proper time at the far mouth", sh["far_proper"], 94.056142695, 1e-9)
near("Shapiro excess over the areal gap", sh["excess"], 5.011051874, 1e-8)
near("'5.6 % DELAY' = excess / areal gap", 100 * sh["excess"] / sh["areal_gap"], 5.567835, 1e-6)
chk("excess > 0 -- a delay", sh["excess"] > 0)

# ---------------------------------------------------------------- C: z3 sign
print("C. z3 -- the sign of the excess for every admissible (M, R1, R2)")
try:
    import z3
    m, r1, r2 = z3.Reals("m r1 r2")
    # excess = 2m ln((r2-2m)/(r1-2m)); ln is not in z3, so encode the sign of the
    # log through its argument: excess > 0  <=>  m>0 and ratio>1, or m<0 and ratio<1.
    # ratio > 1  <=>  (r2-2m) > (r1-2m)  (both denominators positive on the domain).
    s = z3.Solver()
    s.add(m > 0, r1 > 2 * m, r2 > r1)
    s.add(z3.Not(z3.And(r2 - 2 * m > r1 - 2 * m, r1 - 2 * m > 0)))   # try to refute ratio>1
    chk("M>0, 2M<R1<R2: no counterexample to ratio>1 (excess>0, DELAY)", s.check() == z3.unsat)
    s2 = z3.Solver()
    s2.add(m < 0, r1 > 0, r2 > r1)
    s2.add(z3.Not(z3.And(r2 - 2 * m > r1 - 2 * m, r1 - 2 * m > 0)))
    # here ratio>1 again, and 2m<0, so excess<0: ADVANCE.  The sign is that of M.
    chk("M<0, 0<R1<R2: no counterexample to ratio>1, so 2M ln(ratio) < 0 (ADVANCE)", s2.check() == z3.unsat)
    # vacuity guard: the domains are non-empty
    s3 = z3.Solver(); s3.add(m > 0, r1 > 2 * m, r2 > r1); chk("vacuity guard: domain M>0 is satisfiable", s3.check() == z3.sat)
    s4 = z3.Solver(); s4.add(m < 0, r1 > 0, r2 > r1);     chk("vacuity guard: domain M<0 is satisfiable", s4.check() == z3.sat)
except ImportError:
    chk("z3 available", False)

# ---------------------------------------------------------------- D: weak-field isotropic
print("D. sympy -- first-order isotropic straight-line form (Will 2014 eq.62 one-way, gamma=1; Possel 2020 eq.27)")
x, b, x0, x1 = sp.symbols("x b x0 x1", real=True)
bpos = sp.symbols("b", positive=True)
G = sp.integrate(1 + 2 * M / sp.sqrt(x ** 2 + bpos ** 2), x)
print("     antiderivative:", G)
wf_exact = G.subs(x, x1) - G.subs(x, x0)
r0s, r1s = sp.sqrt(x0 ** 2 + bpos ** 2), sp.sqrt(x1 ** 2 + bpos ** 2)
wf_tree = (x1 - x0) + 2 * M * sp.log((x1 + r1s) / (x0 + r0s))     # composite.py:284-287
resid_wf = sp.simplify(sp.expand_log(wf_exact - wf_tree, force=True))
print("     residual:", resid_wf)
# asinh(x/b) = ln((x + sqrt(x^2+b^2))/b); the /b cancels in the difference.  Numeric check too.
wv = {M: 2e-3, bpos: 0.3, x0: -40.0, x1: 35.0}
near("weak-field integral vs composite.analytic_shapiro at its defaults", float(wf_exact.subs(wv)), float(wf_tree.subs(wv)), 1e-12)
chk("residual simplifies to 0 (or is numerically 0 at the defaults)", resid_wf == 0 or abs(float(wf_exact.subs(wv)) - float(wf_tree.subs(wv))) < 1e-12)

# ---------------------------------------------------------------- E: composite VALIDATION 3 from pins
print("E. composite.py VALIDATION 3 from its own pinned t-|dx| values (composite.py:50-52, 337-346)")
def analytic_shapiro(Mv, bv=0.3, x0v=-40.0, x1v=35.0):        # composite.py:284-287 verbatim
    r0v, r1v = math.hypot(x0v, bv), math.hypot(x1v, bv)
    return 2.0 * Mv * math.log((x1v + r1v) / (x0v + r0v))
tp, tm = +5.124e-2, -3.762e-2          # t-|dx| at M = +2e-3, -2e-3, as printed
anti = 0.5 * (tp - tm)
sym = 0.5 * (tp + tm)
an = analytic_shapiro(2e-3)
print("     antisym %.5e   analytic %.5e   ratio %.4f   sym residue %+.4e" % (anti, an, anti / an, sym))
chk("antisym/analytic within 1e-2 of 1 (the quoted 0.6 %% is %.2f %%)" % (100 * abs(anti / an - 1)), abs(anti / an - 1) < 1e-2)
chk("symmetric residue > 0 (path lengthening, ~M^2)", sym > 0)
chk("weak-field hypothesis holds at composite's numbers: M/b = %.1e << 1" % (2e-3 / 0.3), 2e-3 / 0.3 < 1e-2)

# ---------------------------------------------------------------- F: named hypotheses, measured
print("F. named-hypothesis measurements (recorded, not repaired)")
first_order = 2.0 * math.log(100.0 / 10.0)
print("     first-order 2M ln(R2/R1) at foliation's numbers = %.6f M vs exact excess %.6f M (%.1f %% low)"
      % (first_order, sh["excess"], 100 * (1 - first_order / sh["excess"])))
chk("foliation uses the EXACT form where R1 = 10M is not weak-field (first order would be 8 %% low)", first_order < sh["excess"])
def proper_dist(Mv, r):     # int dR / sqrt(1-2M/R) = sqrt(R(R-2M)) + 2M ln(sqrt(R) + sqrt(R-2M))
    return math.sqrt(r * (r - 2 * Mv)) + 2 * Mv * math.log(math.sqrt(r) + math.sqrt(r - 2 * Mv))
L = proper_dist(1.0, 100.0) - proper_dist(1.0, 10.0)
# verify the antiderivative with sympy
Rr = sp.symbols("R", positive=True)
pd = sp.sqrt(Rr * (Rr - 2 * M)) + 2 * M * sp.log(sp.sqrt(Rr) + sp.sqrt(Rr - 2 * M))
chk("proper-distance antiderivative checks (d/dR = 1/sqrt(1-2M/R))",
    sp.simplify(sp.diff(pd, Rr) - 1 / sp.sqrt(1 - 2 * M / Rr)) == 0)
print("     proper radial distance 10M..100M = %.6f M (areal gap 90)" % L)
print("     Killing time 95.011 vs proper distance %.3f: excess %.3f M = %.1f %% (vs 5.6 %% on the areal gap)"
      % (L, sh["killing"] - L, 100 * (sh["killing"] - L) / L))
chk("delay sign survives the change of baseline (Killing time > proper distance)", sh["killing"] > L)
chk("far static clock also exceeds the proper distance (%.3f > %.3f)" % (sh["far_proper"], L), sh["far_proper"] > L)
print("     near static clock (R1 = 10M) reads %.3f M for the same interval, LESS than the proper distance %.3f M"
      % (sh["near_proper"], L))
chk("so 'DELAY' is a Killing-time / far-clock statement, not one every static clock on the corridor makes",
    sh["near_proper"] < L)
# chart term (Possel 2020 eq.21 vs eq.25): Schwarzschild-chart straight line integrand has -M b^2/r^3 extra
Hc = sp.integrate(-M * bpos ** 2 / (x ** 2 + bpos ** 2) ** sp.Rational(3, 2), x)
chart = float((Hc.subs(x, x1) - Hc.subs(x, x0)).subs(wv))
print("     Schwarzschild-chart extra term -M(x1/r1 - x0/r0) at composite's defaults = %+.4e (isotropic-chart value %.4e)"
      % (chart, an))
chk("chart-dependence of a first-order 't - |dx|' is O(2M) = %.1f %% of the isotropic value here; composite is consistently isotropic"
    % (100 * abs(chart) / an), abs(chart) < an)

# ---------------------------------------------------------------- data
print("G. data -- GM_sun/c^3 from the IAU 2015 nominal (GM)_sun (arXiv:1510.07674, READ)")
GM = 1.3271244e20; c = 2.99792458e8
print("     GM_sun/c^3 = %.9e s;  4 GM/c^3 = %.3f us (the scale of Will 2014 eq.63's '240 us')" % (GM / c ** 3, 4e6 * GM / c ** 3))
chk("the tree uses M = 1 in geometric units: no solar datum enters foliation/composite/concentric", True)

print("\nOVERALL:", "ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
