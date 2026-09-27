#!/usr/bin/env python3
"""
DOCKET 67, pass S, 31/36 -- le-2026-eq17-dec-margin.

Re-derive, from the Lanczos/Israel junction and NOT from Le's text (which could
not be read in this stage), the static surface dominant-energy margin of a thin
shell with Minkowski inside and Schwarzschild (mass m) outside:

    8 pi R (sigma_0 - p_0) = -(5s-1)(s-1)/(2s),   s = sqrt(1 - x), x = 2m/R

and the window "surface dec iff x < 24/25".  Then check the two things the tree
leans on: (a) the static margin carries no beta^2 (the 'decoupling'), and
(b) what that decoupling does NOT cover -- the margin off equilibrium.

Checks:
  C1  extrinsic curvature of r = R (static) from the Lie derivative of the metric
  C2  sigma_0, p_0 from the Lanczos equations; match wall.py statics()
  C3  8 pi R (sigma_0 - p_0) == -(5s-1)(s-1)/(2s) identically
  C4  roots in s: {1/5, 1}; x = 24/25 at s = 1/5
  C5  z3: for 0 < s < 1, margin > 0  <=>  s > 1/5  (and p_0 > 0 throughout)
  C6  dynamic junction (Rdot != 0): conservation law identity; sigma, p at the
      static point reduce to C2 for every beta^2
  C7  off-equilibrium margin: d(sigma - p)/dR at R_0 = (1 - beta^2) sigma'(R_0)
      -- depends on beta^2 (the named hypothesis 'static equilibrium')
  C8  numeric: wall.py dec_margin_scaled vs dec_margin_le at the five x the
      tree uses, and vs this file's closed form (wall.py imported read-only)
"""
import sys, math, importlib.util
sys.dont_write_bytecode = True
import sympy as sp

ok = True
def rep(label, good, detail=""):
    global ok
    ok &= bool(good)
    print("  %-64s %s %s" % (label, "ok" if good else "FAIL", detail))

m, R, r, t = sp.symbols("m R r t", positive=True)
s = sp.symbols("s", positive=True)

# ---- C1: static extrinsic curvature via K_ab = (1/2) L_n g_ab ---------------
def K_static(f):
    # metric -f dt^2 + dr^2/f + r^2 dOmega^2; unit normal n = sqrt(f) d_r
    nr = sp.sqrt(f)
    g_tt, g_thth = -f, r**2
    K_tt = sp.Rational(1, 2) * nr * sp.diff(g_tt, r)
    K_thth = sp.Rational(1, 2) * nr * sp.diff(g_thth, r)
    # proper-time frame on the static worldline: K^tau_tau = g^tt K_tt
    Ktau = sp.simplify((1 / g_tt) * K_tt)
    Kth = sp.simplify(K_thth / g_thth)
    return Ktau.subs(r, R), Kth.subs(r, R)

f_in, f_out = sp.Integer(1) + 0 * r, 1 - 2 * m / r
Ktau_in, Kth_in = K_static(f_in)
Ktau_out, Kth_out = K_static(f_out)
print("C1 extrinsic curvature (static)")
rep("K^th_th(in) = 1/R", sp.simplify(Kth_in - 1 / R) == 0)
rep("K^th_th(out) = sqrt(1-2m/R)/R", sp.simplify(Kth_out - sp.sqrt(1 - 2 * m / R) / R) == 0)
rep("K^tau_tau(in) = 0", sp.simplify(Ktau_in) == 0)
rep("K^tau_tau(out) = m/(R^2 sqrt(1-2m/R))",
    sp.simplify(Ktau_out - m / (R**2 * sp.sqrt(1 - 2 * m / R))) == 0)

# ---- C2: Lanczos -----------------------------------------------------------
sigma0 = sp.simplify(-(Kth_out - Kth_in) / (4 * sp.pi))
p0 = sp.simplify(((Ktau_out - Ktau_in) + (Kth_out - Kth_in)) / (8 * sp.pi))
# express in s: m = (1 - s^2) R / 2
sub = {m: (1 - s**2) * R / 2}
sig_s = sp.simplify(sigma0.subs(sub).subs(sp.sqrt(s**2), s))
p_s = sp.simplify(p0.subs(sub).subs(sp.sqrt(s**2), s))
sig_s = sp.simplify(sp.powsimp(sig_s, force=True))
p_s = sp.simplify(sp.powsimp(p_s, force=True))
print("\nC2 Lanczos surface stress")
rep("sigma_0 = (1-s)/(4 pi R)", sp.simplify(sig_s - (1 - s) / (4 * sp.pi * R)) == 0, str(sig_s))
rep("p_0 = (1-s)^2/(16 pi R s)", sp.simplify(p_s - (1 - s)**2 / (16 * sp.pi * R * s)) == 0, str(p_s))

# ---- C3: Eq (17) as the tree prints it -------------------------------------
margin = sp.simplify(8 * sp.pi * R * (sig_s - p_s))
le17 = -(5 * s - 1) * (s - 1) / (2 * s)
print("\nC3 the closed form")
rep("8 pi R (sigma_0 - p_0) - [-(5s-1)(s-1)/(2s)] == 0", sp.simplify(margin - le17) == 0,
    "margin = %s" % sp.factor(margin))

# ---- C4: roots -------------------------------------------------------------
roots = sp.solve(sp.numer(sp.together(margin)), s)
print("\nC4 roots")
rep("zeros of the margin in s are {1/5, 1}", set(roots) == {sp.Rational(1, 5), 1}, str(roots))
x_at = 1 - sp.Rational(1, 5)**2
rep("s = 1/5  <=>  x = 24/25", x_at == sp.Rational(24, 25), str(x_at))
rep("R at x = 24/25 is 25m/12 > 2m (outside the horizon)", sp.Rational(25, 12) > 2)

# ---- C5: z3 over the whole open interval ------------------------------------
print("\nC5 z3, quantified over every real s in (0,1)")
import z3
S = z3.Real("s")
num = -(5 * S - 1) * (S - 1)          # 2s * margin; 2s > 0 on the interval
pnum = (1 - S) * (1 - S)              # 16 pi R s * p_0
dom = z3.And(S > 0, S < 1)
def prove(claim, label):
    sol = z3.Solver()
    sol.add(z3.Not(z3.Implies(dom, claim)))
    res = sol.check()
    rep(label, res == z3.unsat, "(negation %s)" % res)
prove((num > 0) == (S > z3.RealVal("1/5")), "margin > 0  <=>  s > 1/5  on 0<s<1")
prove(pnum > 0, "p_0 > 0 on 0<s<1 (so |p_0| = p_0: the Type-I p>0 case is automatic)")
prove(z3.Implies(S > z3.RealVal("1/5"), (1 - S) > 0), "sigma_0 > 0 on the window")
# vacuity guard: the domain and the window are both inhabited
v = z3.Solver(); v.add(dom, S > z3.RealVal("1/5")); rep("vacuity guard: window inhabited", v.check() == z3.sat)
v = z3.Solver(); v.add(dom, S < z3.RealVal("1/5")); rep("vacuity guard: complement inhabited", v.check() == z3.sat)

# ---- C6: dynamic junction, conservation, static reduction -------------------
print("\nC6 dynamic junction (standard spherically symmetric thin-shell forms)")
Rt = sp.Function("R")(t)            # t here is proper time tau on the shell
Rd, Rdd = sp.diff(Rt, t), sp.diff(Rt, t, 2)
def Kdyn(f):
    fR = f.subs(r, Rt)
    fp = sp.diff(f, r).subs(r, Rt)
    root = sp.sqrt(fR + Rd**2)
    return (Rdd + fp / 2) / root, root / Rt
Kt_i, Kh_i = Kdyn(f_in)
Kt_o, Kh_o = Kdyn(f_out)
sig_d = -(Kh_o - Kh_i) / (4 * sp.pi)
p_d = ((Kt_o - Kt_i) + (Kh_o - Kh_i)) / (8 * sp.pi)
cons = sp.diff(sig_d * 4 * sp.pi * Rt**2, t) + p_d * sp.diff(4 * sp.pi * Rt**2, t)
rep("d(sigma A)/dtau + p dA/dtau == 0 (vacuum both sides)", sp.simplify(cons) == 0)
stat = {Rdd: 0}
sig_st = sp.simplify(sig_d.subs(stat).subs(Rd, 0).subs(Rt, R))
p_st = sp.simplify(p_d.subs(stat).subs(Rd, 0).subs(Rt, R))
rep("dynamic sigma at Rdot=Rddot=0 equals static sigma_0", sp.simplify(sig_st - sigma0) == 0)
rep("dynamic p at Rdot=Rddot=0 equals static p_0", sp.simplify(p_st - p0) == 0)
rep("no beta^2 symbol enters sigma_0 or p_0 (they are fixed by (m, R) alone)",
    not any(str(a).startswith("beta") for a in (sigma0 + p0).free_symbols))

# ---- C7: what the decoupling does not cover --------------------------------
print("\nC7 off equilibrium (the named hypothesis 'static equilibrium R = R_0')")
b2 = sp.symbols("beta2", real=True)
# conservation: dsigma/dR = -2 (sigma + p)/R ; EoS p = p0 + b2 (sigma - sigma0)
sigp_R0 = -2 * (sig_s + p_s) / R
dmargin_dR = (1 - b2) * sigp_R0
rep("d(sigma-p)/dR |_R0 = (1 - beta^2)(-2(sigma_0+p_0)/R_0) depends on beta^2",
    sp.diff(dmargin_dR, b2) != 0, "d/dbeta2 = %s" % sp.simplify(sp.diff(dmargin_dR, b2)))
rep("  ...and vanishes at beta^2 = 1 only (stiffest causal EoS)",
    sp.solve(sp.Eq(dmargin_dR, 0), b2) == [1])

# ---- C8: numeric, against wall.py read-only --------------------------------
print("\nC8 numeric against wall.py (imported read-only, no bytecode written)")
WALL = "/home/user/Claude-Method-Works/research/warp-drive/wall.py"
spec = importlib.util.spec_from_file_location("wall_ro", WALL)
wall = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wall)
fm = sp.lambdify(s, margin, "math")
for x in (0.1, 0.3, 0.5, 0.8, 24 / 25):
    ss = math.sqrt(1 - x)
    a, b, c = wall.dec_margin_scaled(x), wall.dec_margin_le(x), fm(ss)
    rep("x = %.4f  wall.scaled=%.15f  wall.le=%.15f  here=%.15f" % (x, a, b, c),
        abs(a - b) < 1e-12 and abs(a - c) < 1e-12)
rep("wall.X_THIN_SHELL == 24/25", wall.X_THIN_SHELL == 24 / 25)

print("\nRESULT:", "ALL CHECKS PASS" if ok else "A CHECK FAILED")
sys.exit(0 if ok else 1)
