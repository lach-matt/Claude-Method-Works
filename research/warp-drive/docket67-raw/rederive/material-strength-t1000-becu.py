#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key material-strength-t1000-becu.

Audits warpfolder.py:222-227 (MATERIALS, status ORDER) and what rests on it,
ROTOR_IS_WITHIN_MATERIAL_LIMITS = False (warpfolder.py:247, selftest 564-570),
through burst_speed_m_s = sqrt(sigma/rho) (warpfolder.py:328-330).

Imports nothing from the tree; restates the tree's numbers as data.
Values labelled SNIPPET came from a WebSearch summary of the maker's sheet
(the sheets themselves were egress-blocked and alphaXiv's quota was exhausted);
they are NOT READ at source.  Values labelled ORDER are memory-order inputs
used only for sensitivity, never as findings.
"""
import math
import sympy as sp

FAIL = 0
def check(name, ok, detail=""):
    global FAIL
    print(("PASS " if ok else "FAIL ") + name + (("  -- " + detail) if detail else ""))
    if not ok:
        FAIL += 1

c = 299792458.0
# ---- the tree's own inputs (warpfolder.py:218-219, 224-227)
D, RPM = 1.8, 85000.0
TREE = {"T1000": (6.4e9, 1800.0), "BeCu": (1.4e9, 8250.0)}

# ---- (1) tip speed
v = math.pi * D * RPM / 60.0
check("R1 tip speed pi*D*N/60 = 8011.06 m/s", abs(v - 8011.06) / 8011.06 < 1e-6, "%.4f" % v)
check("R1b v/c = 2.672e-5 (not relativistic)", abs(v / c - 2.672e-5) / 2.672e-5 < 1e-3, "%.4e" % (v / c))

# ---- (2) thin rotating ring: hoop stress sigma = rho v^2, derived symbolically
rho, w, R, A, th = sp.symbols("rho omega R A theta", positive=True)
# element of a ring of cross-section A subtending d(theta): centripetal force
# rho*A*R*dth*omega^2*R is supplied by two hoop forces T at angle dth/2 each:
# 2 T sin(dth/2) ~ T dth.  T = sigma A.
sig = sp.symbols("sigma", positive=True)
eq = sp.Eq(sig * A * th, rho * A * R * th * w**2 * R)
sol = sp.solve(eq, sig)[0]
check("R2 thin ring: sigma = rho (omega R)^2", sp.simplify(sol - rho * (w * R)**2) == 0, str(sol))
# => burst tip speed of a ring v_b = sqrt(sigma/rho), independent of R

# ---- (3) uniform isotropic disc, plane stress (Lame): solve and find the max stress
r, nu, E_ = sp.symbols("r nu E", positive=True)
u = sp.Function("u")
# Navier displacement equation for a rotating disc in plane stress:
# u'' + u'/r - u/r^2 = -(1-nu^2) rho omega^2 r / E
ode = sp.Eq(u(r).diff(r, 2) + u(r).diff(r) / r - u(r) / r**2, -(1 - nu**2) * rho * w**2 * r / E_)
gen = sp.dsolve(ode).rhs
C1, C2 = sorted(gen.free_symbols - {r, nu, rho, w, E_}, key=str)
us = gen.subs(C1 if gen.coeff(1/r) == 0 else C2, 0)
# regular at r=0: drop the 1/r term
us = sp.expand(gen)
cs = [s for s in us.free_symbols if s.name.startswith("C")]
for s in cs:
    if sp.simplify(us.coeff(s) - 1 / r) == 0:
        us = us.subs(s, 0)
cfree = [s for s in us.free_symbols if s.name.startswith("C")][0]
er, et = us.diff(r), us / r
sr = E_ / (1 - nu**2) * (er + nu * et)
st = E_ / (1 - nu**2) * (et + nu * er)
cval = sp.solve(sp.Eq(sr.subs(r, R), 0), cfree)[0]
sr, st = sp.simplify(sr.subs(cfree, cval)), sp.simplify(st.subs(cfree, cval))
centre = sp.simplify(sp.limit(st, r, 0))
check("R3 uniform disc: sigma_theta(0)=sigma_r(0)=(3+nu)/8 rho omega^2 R^2",
      sp.simplify(centre - (3 + nu) / 8 * rho * w**2 * R**2) == 0, str(centre))
check("R3b uniform disc: sigma_theta(R) = (1-nu)/4 rho omega^2 R^2",
      sp.simplify(st.subs(r, R) - (1 - nu) / 4 * rho * w**2 * R**2) == 0)
# max over r of sigma_theta is at the centre: d sigma_theta/dr <= 0
dst = sp.simplify(st.diff(r))
check("R3c sigma_theta decreasing in r (max at centre)",
      sp.simplify(dst + (1 + 3 * nu) / 4 * rho * w**2 * r) == 0, str(dst))
disc_factor = lambda n: math.sqrt(8.0 / (3.0 + n))
print("     uniform-disc tip-speed ceiling = sqrt(8/(3+nu)) sqrt(sigma/rho): nu=0.3 -> %.4f, nu=0 -> %.4f, nu=0.5 -> %.4f"
      % (disc_factor(0.3), disc_factor(0.0), disc_factor(0.5)))

# ---- (4) Stodola constant-stress disc: h(r) = h0 exp(-rho omega^2 r^2/(2 sigma))
h0 = sp.symbols("h0", positive=True)
h = h0 * sp.exp(-rho * w**2 * r**2 / (2 * sig))
# radial equilibrium of a variable-thickness disc: d(h r s_r)/dr - h s_t + h rho omega^2 r^2 = 0
resid = sp.simplify(sp.diff(h * r * sig, r) - h * sig + h * rho * w**2 * r**2)
check("R4 Stodola disc satisfies equilibrium with s_r = s_t = sigma", resid == 0, str(resid))
# taper needed to reach tip speed v:  h(R)/h0 = exp(-(v/v_b)^2 / 2)

# ---- (5) the tree's factors, and the rounding sensitivity
def vb(s, d): return math.sqrt(s / d)
tree_over = [round(v / vb(*TREE[k]), 1) for k in ("T1000", "BeCu")]
check("R5 tree's factors reproduce [4.2, 19.4]", tree_over == [4.2, 19.4],
      "unrounded %.4f, %.4f" % (v / vb(*TREE["T1000"]), v / vb(*TREE["BeCu"])))

# SNIPPET values (WebSearch summary of Toray T1000G data sheet; C17200 peak-aged)
SNIP = {"T1000G sheet (SNIPPET)": (6.37e9, 1800.0),
        "C17200 peak-aged 1357 MPa (SNIPPET, PMC9000027)": (1.357e9, 8250.0),
        "C17200 '>1380 MPa' (SNIPPET)": (1.38e9, 8250.0)}
for k, (s, d) in SNIP.items():
    print("     %-50s v_b = %7.1f m/s   v/v_b = %.4f -> printed %.1f" % (k, vb(s, d), v / vb(s, d), round(v / vb(s, d), 1)))
t_snip = round(v / vb(6.37e9, 1800.0), 1)
check("R5b with the sheet's 6,370 MPa the T1000 factor prints 4.3, not 4.2 (rounding discrepancy, not a refutation)",
      t_snip == 4.3, "%.4f" % (v / vb(6.37e9, 1800.0)))
# density band for BeCu, ORDER: 8.25-8.36 g/cm^3 (SNIPPET gave 8.30 before aging, 8.36 for TD02)
lo = v / vb(1.60e9, 8250.0); hi = v / vb(1.14e9, 8360.0)
print("     BeCu factor over sigma in [1.14,1.60] GPa, rho in [8250,8360]: %.2f .. %.2f" % (lo, hi))

# ---- (6) how far would the data have to move to reverse the conclusion?
need = v**2
for k, (s, d) in TREE.items():
    print("     %-6s sigma/rho = %.3e J/kg ; ring needs %.3e (x%.1f) ; uniform disc (nu=0.3) needs x%.1f"
          % (k, s / d, need, need / (s / d), need / (s / d) / disc_factor(0.3)**2))
check("R6 T1000: specific strength must rise >= 18.0x for a ring, >= 7.4x for a uniform disc (nu=0.3)",
      need / (6.4e9 / 1800) > 18.0 and need / (6.4e9 / 1800) / disc_factor(0.3)**2 > 7.4)
check("R6b BeCu: >= 378x for a ring, >= 156x for a uniform disc (nu=0.3)",
      need / (1.4e9 / 8250) > 378 and need / (1.4e9 / 8250) / disc_factor(0.3)**2 > 155)

# ---- (7) the only geometric escape: the Stodola taper
for k, (s, d) in TREE.items():
    x = (v / vb(s, d))**2 / 2
    print("     %-6s Stodola taper h(R)/h0 = exp(-%.2f) = %.3e" % (k, x, math.exp(-x)))
x_becu = (v / vb(*TREE["BeCu"]))**2 / 2
# BeCu is isotropic, so the Stodola escape is formally open; it needs taper exp(-189)
# i.e. for h(R) >= one atomic spacing (2.5e-10 m, ORDER) the hub would be thicker than
check("R7 BeCu Stodola escape needs a hub > 1e70 m thick for an atom-thick rim",
      2.5e-10 * math.exp(x_becu) > 1e70, "%.2e m" % (2.5e-10 * math.exp(x_becu)))
x_t = (v / vb(*TREE["T1000"]))**2 / 2
check("R7b T1000 treated (counterfactually) as ISOTROPIC at fibre strength: Stodola taper exp(-9.02)=1.2e-4 -- not excluded by the formula alone",
      1e-4 < math.exp(-x_t) < 2e-4, "%.3e" % math.exp(-x_t))

# ---- (8) laminate, rule of mixtures (ORDER inputs: Vf=0.6, resin 1200 kg/m^3), fibre-direction upper bound
Vf, rres = 0.6, 1200.0
sl, rl = Vf * 6.4e9, Vf * 1800 + (1 - Vf) * rres
print("     UD laminate (ORDER) sigma/rho = %.3e vs fibre %.3e -> ring factor %.2f"
      % (sl / rl, 6.4e9 / 1800, v / vb(sl, rl)))
check("R8 laminate is weaker per mass than the bare fibre, so the fibre figure favours the rotor",
      sl / rl < 6.4e9 / 1800)

print()
print("FAILURES:", FAIL)
raise SystemExit(1 if FAIL else 0)
