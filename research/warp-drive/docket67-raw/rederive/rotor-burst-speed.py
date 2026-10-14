#!/usr/bin/env python3
"""DOCKET 67 -- rederivation of the classical rotor burst limit v = sqrt(sigma/rho)
as warpfolder.py:113-118, 328-330, 418-421, 566-570 uses it.

Plane-stress, linear-elastic, isotropic unless stated.  sympy for the closed forms,
float arithmetic for the tree's numbers.  Reads warpfolder.py (import only, no write).
Exit 0 iff every assertion holds."""
import math, sys, importlib.util
import sympy as sp

ok = True
def chk(label, cond):
    global ok
    print(("PASS  " if cond else "FAIL  ") + label)
    ok = ok and bool(cond)

r, R, a, w, rho, sig, nu, E, A, h0, v = sp.symbols('r R a omega rho sigma nu E A h0 v', positive=True)

# ---------------------------------------------------------------- 1. thin rim
# Ring element of angle dth, cross-section A, radius R: centripetal demand
# rho*A*R*dth * w^2 R is supplied by the two hoop forces T*dth.  T = sigma_h*A.
sig_h = sp.simplify(rho * A * R**2 * w**2 / A)          # T/A
chk("thin rim: sigma_h = rho v^2 (v = omega R)", sp.simplify(sig_h - rho*(w*R)**2) == 0)
vmax_rim = sp.sqrt(sig/rho)
chk("thin rim: v_max = sqrt(sigma/rho), no R in it", R not in vmax_rim.free_symbols)
# specific energy: E/m = v^2/2 -> K = 1/2 of sigma/rho
chk("thin rim: E/m at v_max = sigma/(2 rho)  (shape factor K = 1/2)",
    sp.simplify((vmax_rim**2/2) - sig/(2*rho)) == 0)

# ------------------------------------------------- 2. uniform-thickness disc
# Lame: u'' + u'/r - u/r^2 = -(1-nu^2) rho w^2 r / E
u = sp.Function('u')
C1, C2 = sp.symbols('C1 C2')
up = -(1 - nu**2) * rho * w**2 * r**3 / (8 * E)          # particular solution
chk("Lame particular solution satisfies the ODE",
    sp.simplify(sp.diff(up, r, 2) + sp.diff(up, r)/r - up/r**2 + (1-nu**2)*rho*w**2*r/E) == 0)
def stresses(uu):
    er, et = sp.diff(uu, r), uu/r
    sr = E/(1-nu**2)*(er + nu*et)
    st = E/(1-nu**2)*(et + nu*er)
    return sp.simplify(sr), sp.simplify(st)
# solid disc: u = C1 r + up, sigma_r(R)=0
uS = C1*r + up
srS, stS = stresses(uS)
c1 = sp.solve(sp.Eq(srS.subs(r, R), 0), C1)[0]
srS, stS = sp.simplify(srS.subs(C1, c1)), sp.simplify(stS.subs(C1, c1))
peak = sp.simplify(stS.subs(r, 0))
chk("solid disc: peak sigma = (3+nu)/8 rho w^2 R^2 at the centre (sigma_r = sigma_theta there)",
    sp.simplify(peak - (3+nu)/8*rho*w**2*R**2) == 0 and sp.simplify(srS.subs(r, 0) - peak) == 0)
chk("solid disc: sigma_theta decreases outward (d/dr < 0)",
    sp.simplify(sp.diff(stS, r) + (1+3*nu)/4*rho*w**2*r) == 0)
vS = sp.sqrt(8*sig/((3+nu)*rho))
fS = sp.simplify(vS/vmax_rim)
print("      solid-disc v_max / sqrt(sigma/rho) =", fS, "=", [round(float(fS.subs(nu, x)), 4) for x in (0.0, 0.25, 0.3, 0.35, 0.5)])
chk("solid disc: v_max is also radius-independent", R not in vS.free_symbols)
# disc with a bore a -> 0: sigma_theta(a) -> (3+nu)/4 rho w^2 R^2
uH = C1*r + C2/r + up
srH, stH = stresses(uH)
sol = sp.solve([srH.subs(r, a), srH.subs(r, R)], [C1, C2], dict=True)[0]
stH = sp.simplify(stH.subs(sol))
bore = sp.limit(stH.subs(r, a), a, 0)
chk("bored disc, a->0: bore hoop stress -> (3+nu)/4 rho w^2 R^2 (the stress-concentration factor 2)",
    sp.simplify(bore - (3+nu)/4*rho*w**2*R**2) == 0)
fH = sp.sqrt(4/(3+nu))
print("      pinhole-bore v_max / sqrt(sigma/rho) =", [round(float(fH.subs(nu, x)), 4) for x in (0.25, 0.3, 0.35)])
# thin ring limit a -> R recovers rho v^2
chk("bored disc, a->R: bore hoop stress -> rho w^2 R^2 (thin rim recovered)",
    sp.simplify(sp.limit(stH.subs(r, a), a, R) - rho*w**2*R**2) == 0)

# ---------------------------------------------- 3. constant-stress (Stodola) disc
# Equilibrium with variable thickness h(r):  d(h r s_r)/dr - h s_t + rho w^2 r^2 h = 0
hS = h0*sp.exp(-rho*w**2*r**2/(2*sig))
eq = sp.diff(hS*r*sig, r) - hS*sig + rho*w**2*r**2*hS
chk("Stodola: h = h0 exp(-rho w^2 r^2 / 2 sigma) with s_r = s_t = sigma satisfies equilibrium for EVERY omega",
    sp.simplify(eq) == 0)
eps = (1-nu)*sig/E
uu = eps*r
chk("Stodola: compatibility holds (e_r = e_theta = (1-nu) sigma/E, u = e r)",
    sp.simplify(sp.diff(uu, r) - eps) == 0 and sp.simplify(uu/r - eps) == 0)
# Truncate at R with a thin rim of section A. Rim hoop strain must match disc edge:
# sigma_rim = (1-nu) sigma <= sigma.  Rim balance: sigma_rim A = rho A v^2 - sigma h_R R
hR = hS.subs(r, R)
Asol = sp.solve(sp.Eq((1-nu)*sig*A, rho*A*v**2 - sig*hR*R), A)[0]
print("      rim section needed: A =", sp.simplify(Asol))
chk("Stodola+rim: A > 0 for any v > sqrt((1-nu) sigma/rho) -- the thin-rim sentence is NOT a theorem for all rotors",
    sp.simplify(Asol.subs({v: 3*sp.sqrt(sig/rho), nu: sp.Rational(3, 10)})).is_positive)


# shape factors, K = (E/m)/(sigma/rho), as a cross-check on the restated values
Kd = sp.simplify(((vS**2)/4)/(sig/rho))            # uniform disc: E/m = v_tip^2/4
print("      K(uniform solid disc, max-stress = sigma) =", Kd, "=", round(float(Kd.subs(nu, 0.3)), 4), "at nu=0.3")
s_, X = sp.symbols('s X', positive=True)
KS = sp.integrate(s_*sp.exp(-s_), (s_, 0, X))/sp.integrate(sp.exp(-s_), (s_, 0, X))
chk("Stodola disc (no rim): K(X) -> 1 as X = rho v^2/(2 sigma) -> oo (the 'Laval disc K = 1')",
    sp.limit(KS, X, sp.oo) == 1)

# ---------------------------------------------------------------- 4. the tree's numbers
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
spec = importlib.util.spec_from_file_location(
    "wf", "/home/user/Claude-Method-Works/research/warp-drive/warpfolder.py")
wf = importlib.util.module_from_spec(spec); spec.loader.exec_module(wf)
vt = wf.tip_speed_m_s()
chk("tip speed pi*1.8*85000/60 = 8011.06 m/s", abs(vt - math.pi*1.8*85000/60) < 1e-9 and abs(vt - 8011.06) < 0.01)
rows = []
for name, s_, r_ in wf.MATERIALS:
    vb = math.sqrt(s_/r_)
    chk("%s: tree burst_speed_m_s agrees with sqrt(sigma/rho)" % name, abs(wf.burst_speed_m_s(s_, r_) - vb) < 1e-9)
    rows.append((name, s_, r_, vb, vt/vb))
    print("      %-20s sigma %.3g Pa rho %.0f  v_rim %.1f m/s  ratio %.4f" % (name, s_, r_, vb, vt/vb))
chk("ratios round to [4.2, 19.4] as the selftest pins", [round(x[4], 1) for x in rows] == [4.2, 19.4])

print("\n  ratio demanded / allowed under other geometries (nu = 0.3 where isotropic):")
for name, s_, r_, vb, q in rows:
    fs = float(fS.subs(nu, 0.3)); fh = float(fH.subs(nu, 0.3))
    print("      %-20s thin rim %.2fx  uniform solid disc %.2fx  pinhole bore %.2fx" % (name, q, q/fs, q/fh))
    chk("%s: over the limit on every non-profiled geometry" % name, q/fs > 1)
    # sigma/rho multiplier needed to reach the demand
    print("        sigma/rho would have to rise %.1fx (rim) / %.1fx (solid disc) to reach 8011 m/s" % (q**2, (q/fs)**2))

print("\n  Stodola disc at the demanded tip speed (formal counterexample, isotropic idealisation):")
for name, s_, r_, vb, q in rows:
    ratio_h = math.exp(-q**2/2)
    print("      %-20s h(R)/h(0) = exp(-%.2f) = %.3e" % (name, q**2/2, ratio_h))
    rows_h = ratio_h
chk("BeCu Stodola profile needs h(R)/h(0) < 1e-80 (physically empty)", math.exp(-rows[1][4]**2/2) < 1e-80)

print("\n  T1000 as a composite rather than a bare fibre (rule of mixtures, UPPER bound on sigma_c):")
for Vf in (0.55, 0.60, 0.65):
    sc = Vf*6.4e9; rc = Vf*1800 + (1-Vf)*1200.0
    print("      Vf %.2f  sigma_c <= %.2f GPa  rho_c %.0f  v_rim <= %.0f m/s  ratio >= %.2fx" %
          (Vf, sc/1e9, rc, math.sqrt(sc/rc), vt/math.sqrt(sc/rc)))
    chk("  composite ratio exceeds fibre ratio at Vf %.2f" % Vf, vt/math.sqrt(sc/rc) > rows[0][4])

print("\n  sensitivity of BeCu to plausible datasheet spread (sigma 1.2-1.6 GPa, rho 8250-8360):")
lo = min(vt/math.sqrt(s/d) for s in (1.2e9, 1.6e9) for d in (8250, 8360))
hi = max(vt/math.sqrt(s/d) for s in (1.2e9, 1.6e9) for d in (8250, 8360))
print("      ratio range %.1f - %.1f" % (lo, hi)); chk("BeCu ratio > 1 across the spread", lo > 1)
print("\nALL PASS" if ok else "\nSOME FAIL"); sys.exit(0 if ok else 1)
