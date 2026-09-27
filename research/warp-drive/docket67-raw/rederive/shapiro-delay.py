#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation for key 'shapiro-delay'.

External result: Shapiro (1964) time delay, as restated in Will, Living Rev.
Rel. 17 (2014) 4, arXiv:1403.7377 eq. (62) (round trip):
    dt = 2(1+gamma) M ln[ (r_E + x_E.n)(r_e - x_e.n) / d^2 ]
and in LVC+Fermi+INTEGRAL, ApJL 848 L13 (2017), arXiv:1710.05834 eq. (3):
    dt_S = -(1+gamma)/c^3 * int U(r(l)) dl      (linear in the potential)

Tree uses (G = c = 1, gamma = 1 built into the linearised metric
ds^2 = -(1+2Phi)dt^2 + (1-2Phi)dx^2):
    composite.py:284-287   2 M ln[(x1+r1)/(x0+r0)]     one way, Phi = -M/r
    concentric.py:86-90    shell delay / core advance ~ (L/R_s)/(2 ln(L/a))

Checks
  S1 sympy: null coordinate speed dt/dx in the linearised metric = 1 - 2Phi + 2Phi^2 + O(Phi^3)
  S2 sympy: int 2M/sqrt(x^2+b^2) dx over [x0,x1] == 2M ln[(x1+r1)/(x0+r0)]  (exact)
  S3 sympy: one-way tree form == half of Will eq.(62) at gamma = 1 on the straight line
  S4 numeric: the Cassini datum gamma-1 = (2.1 +- 2.3)e-5 moves the delay by ~1e-5 relative
  S5 numeric: concentric design ratio -- exact first-order Shapiro for the tree's own
     potential at b = 1, a = 0.02, R_s = 200, L = 300, against the owner's ln(L/a) form
  S6 numeric: M_ADM = 0 -> first-order Shapiro integral converges with baseline
  S7 numeric: O(Phi^2) metric term's share of composite's symmetric residue
  T  (--tree) run the tree's own composite.survey / concentric.survey read-only
     (no bytecode written) and compare with S2/S5.
"""
import math, sys
import sympy as sp

ok = True
def rec(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  [%s] %s %s" % ("ok" if cond else "FAIL", label, detail))

print("S1 null coordinate speed in the linearised metric")
Phi = sp.symbols('Phi', real=True)
v = sp.sqrt((1 - 2*Phi)/(1 + 2*Phi))
ser = sp.series(v, Phi, 0, 3).removeO()
rec("dt/dx = 1 - 2Phi + 2Phi^2 + O(Phi^3)", sp.simplify(ser - (1 - 2*Phi + 2*Phi**2)) == 0, str(ser))

print("S2 first-order integral along the straight line is the log form, exactly")
x, M, b = sp.symbols('x M b', positive=True)
x0, x1 = sp.symbols('x0 x1', real=True)
integrand = 2*M/sp.sqrt(x**2 + b**2)          # -2Phi with Phi = -M/r
F = sp.integrate(integrand, x)                  # 2M asinh(x/b)
lhs = F.subs(x, x1) - F.subs(x, x0)
r0, r1 = sp.sqrt(x0**2 + b**2), sp.sqrt(x1**2 + b**2)
rhs = 2*M*sp.log((x1 + r1)/(x0 + r0))
diff = sp.simplify(sp.expand_log(lhs.rewrite(sp.log) - rhs, force=True))
num_ok = all(abs(sp.N((lhs - rhs).subs({M: sp.Rational(2, 1000), b: sp.nsimplify(bb), x0: a0, x1: a1}), 50)) < 1e-40
             for bb, a0, a1 in ((0.3, -40, 35), (1.0, -150, 150), (0.01, 5, 90), (2.0, -900, -3)))
rec("int_{x0}^{x1} 2M/r dx == 2M ln[(x1+r1)/(x0+r0)]", diff == 0 or num_ok, "symbolic diff=%s numeric=%s" % (diff, num_ok))
rec("linear in M: sign of M reverses the first-order delay exactly",
    sp.simplify(rhs.subs(M, -M) + rhs) == 0)

print("S3 equivalence with Will (2014) eq. (62), gamma = 1, one way = half round trip")
# ray along +x, n = +x_hat; emitter at x0 (Will's 'Earth' leg reversed is symmetric)
g = sp.Integer(1)
will_rt = 2*(1 + g)*M*sp.log((r1 + x1)*(r0 - x0)/b**2)   # d = b on the unperturbed line
tree_ow = rhs
chk = sp.simplify(sp.expand_log(will_rt/2 - tree_ow, force=True))
# the residue sympy leaves is log(r0-x0)+log(r0+x0)-2log b = log((r0^2-x0^2)/b^2) = log 1:
chk = sp.simplify(sp.logcombine(chk.subs(sp.log(-x0 + r0) + sp.log(x0 + r0), sp.log(sp.expand((r0 - x0)*(r0 + x0)))), force=True))
# identity (r0 - x0)(r0 + x0) = b^2  ->  (r0 - x0)/b^2 = 1/(x0 + r0)
num3 = all(abs(sp.N((will_rt/2 - tree_ow).subs({M: 1, b: sp.nsimplify(bb), x0: a0, x1: a1}), 50)) < 1e-40
           for bb, a0, a1 in ((0.3, -40, 35), (1.0, -150, 150), (0.5, 3, 80)))
rec("half of eq.(62) == tree one-way form", chk == 0 or num3, "symbolic=%s numeric=%s" % (chk, num3))
print("     composite default: analytic_shapiro(2e-3) = %.6e" %
      float(tree_ow.subs({M: 2e-3, b: 0.3, x0: -40, x1: 35})))

print("S4 the datum: Cassini gamma - 1 = (2.1 +- 2.3)e-5 (Bertotti et al. 2003, via Will 2014 p.43)")
for gm1 in (2.1e-5, 2.1e-5 + 2*2.3e-5, 2.1e-5 - 2*2.3e-5):
    fac = (1 + (1 + gm1)) / 2.0
    print("     gamma-1 = %+.2e  ->  (1+gamma)/2 = %.7f  (relative shift %.1e)" % (gm1, fac, fac - 1))
rec("2-sigma envelope moves the delay by < 4e-5 relative, << composite's 1e-2 tolerance",
    abs((1 + 1 + 2.1e-5 + 4.6e-5) / 2 - 1) < 4e-5)

print("S5 concentric design ratio  shell delay / core advance  (b=1, a=0.02, R_s=200, L=300)")
bR, aC, Rs, L = 1.0, 0.02, 200.0, 300.0
core_adv = 2.0 * 2.0 * math.asinh((L/2) / math.sqrt(bR**2 + aC**2))   # per unit m, exact first order
shell_del = 2.0 * L / Rs                                                # per unit m (Phi = -m/R_s inside)
ratio_exact = shell_del / core_adv
ratio_owner = (L/Rs) / (2.0*math.log(L/aC))
ratio_b = (L/Rs) / (2.0*math.log(L/bR))
print("     exact first-order Shapiro ratio  = %.4f" % ratio_exact)
print("     owner's (L/R_s)/(2 ln(L/a))      = %.4f   (concentric.py:86-90, 325-326)" % ratio_owner)
print("     same form with ln(L/b)           = %.4f" % ratio_b)
rec("owner's number reproduces as written (0.0781)", abs(ratio_owner - 0.0781) < 1e-3)
rec("DISCREPANCY: exact first-order ratio is NOT under 10 % at the design point",
    ratio_exact > 0.1, "(%.1f %% vs owner's %.1f %%)" % (100*ratio_exact, 100*ratio_owner))
# sensitivity of core advance to a at fixed b = 1
for a in (0.02, 0.002, 0.2, 1.0):
    print("     a = %-6g  core advance / m = %.4f" % (a, 4.0*math.asinh((L/2)/math.sqrt(bR**2 + a**2))))
lin_pred = {m: -m*core_adv + m*shell_del for m in (1e-3, 3e-3)}
lin_owner = {m: -m*4.0*math.log(L/aC) + m*shell_del for m in (1e-3, 3e-3)}
for m, meas in ((1e-3, -1.921e-2), (3e-3, -5.404e-2)):
    print("     m=%.0e: measured (concentric.py:67-68) %+.4e | exact-Shapiro linear %+.4e | ln(L/a) linear %+.4e"
          % (m, meas, lin_pred[m], lin_owner[m]))
rec("measured small-m delay matches the ln(L/b)-governed first order within 5 %",
    abs(-1.921e-2/lin_pred[1e-3] - 1) < 0.05, "(ratio %.3f)" % (-1.921e-2/lin_pred[1e-3]))

print("S6 M_ADM = 0: first-order Shapiro integral converges with baseline")
def net_phi_int(X, m=1.0, b=1.0, a=0.02, Rs=200.0):
    # int_{-X}^{X} Phi dx with Phi = m/sqrt(r^2+a^2) - m/max(r,Rs), closed form
    core = 2*m*math.asinh(X/math.sqrt(b*b + a*a))
    xs = math.sqrt(Rs*Rs - b*b)
    if X <= xs:
        shell = 2*m*X/Rs
    else:
        shell = 2*m*xs/Rs + 2*m*(math.asinh(X/b) - math.asinh(xs/b))
    return core - shell
vals = [net_phi_int(X) for X in (1e3, 1e4, 1e5, 1e6)]
print("     int Phi dx at X = 1e3..1e6: " + ", ".join("%.7f" % v for v in vals))
rec("constant to 5 digits over three decades of baseline (1e3 -> 1e6)",
    abs(vals[-1] - vals[0]) / abs(vals[0]) < 1e-5, "(rel change %.1e)" % (abs(vals[-1]-vals[0])/abs(vals[0])))

print("S7 share of the O(Phi^2) metric term in composite's symmetric residue")
Mc, bc = 2e-3, 0.3
phi2 = 2*Mc*Mc*(math.atan(35/bc) - math.atan(-40/bc))/bc   # int 2 Phi^2 dx
sym = 0.5*(5.124e-2 + (-3.762e-2))
print("     int 2Phi^2 dx = %.3e ; symmetric residue (composite.py:52-53) = %.3e ; share %.1f %%"
      % (phi2, sym, 100*phi2/sym))
rec("the O(M^2) residue is dominated by ray bending, O(Phi^2) term is a minor part", phi2/sym < 0.05)

if "--tree" in sys.argv:
    print("T  tree code, read-only (sys.dont_write_bytecode)")
    sys.dont_write_bytecode = True
    sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
    import composite
    rp, rm = composite.survey(2e-3), composite.survey(-2e-3)
    anti = 0.5*(rp["delay"] - rm["delay"])
    an = composite.analytic_shapiro(2e-3)
    print("     composite: delay(+)=%+.4e delay(-)=%+.4e anti=%+.5e analytic=%+.5e ratio=%.4f"
          % (rp["delay"], rm["delay"], anti, an, anti/an))
    rec("composite VALIDATION 3 reproduces (|ratio-1| < 1e-2)", abs(anti/an - 1) < 1e-2)
    import concentric
    dp, dm = concentric.survey(1e-3)["delay"], concentric.survey(-1e-3)["delay"]
    anti_c = 0.5*(dp - dm)
    print("     concentric m=1e-3: delay(+)=%+.5e delay(-)=%+.5e anti=%+.5e ; exact-Shapiro linear %+.5e ; ln(L/a) linear %+.5e"
          % (dp, dm, anti_c, lin_pred[1e-3], lin_owner[1e-3]))
    rec("tree's own antisymmetric (linear) delay matches ln(L/b) first order within 2 %",
        abs(anti_c/lin_pred[1e-3] - 1) < 0.02, "(ratio %.4f)" % (anti_c/lin_pred[1e-3]))
    rec("and does NOT match the ln(L/a) form the design rule uses",
        abs(anti_c/lin_owner[1e-3] - 1) > 0.2, "(ratio %.4f)" % (anti_c/lin_owner[1e-3]))

print("\nRESULT %s" % ("ALL CHECKS AS RECORDED" if ok else "SOME CHECK FAILED"))
sys.exit(0 if ok else 1)
