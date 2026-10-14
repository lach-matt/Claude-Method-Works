#!/usr/bin/env python3
"""DOCKET 67 -- audit of 'newtonian-grav-binding' (massform.py:494-496, 2090-2095).

Tree's claim: gravitational binding is of order G M/(R c^2) = 5.2e-26 of the rest
energy at R = 1 m, M = 70 kg; negligible at payload scale (H-AME; no shape factor).

Checks (read-only on the tree; nothing under research/ is written):
 C1  numeric: G M/(R c^2) with the tree's own inputs, and the printed 5.2e-26.
 C2  sympy: Newtonian self-energy of a uniform ball, U = -(3/5) G M^2/R, derived
     from dU = -G m(r) dm / r (shape factor k = 3/5).
 C3  sympy: n = 1 polytrope (rho ~ sin(x)/x), k = 3/4 = 3/(5-n); numeric Lane-Emden
     n = 1.5, 3 against Chandrasekhar's 3/(5-n) (restated result, checked here).
 C4  realistic bodies: uniform ball of 70 kg at water density and at osmium density
     (the densest element; for a density cap rho_max the uniform ball at rho_max
     maximises |U| at fixed M -- Riesz rearrangement / bathtub, NAMED here, not read);
     a 70 kg human-shaped cylinder (1.75 m tall) by Monte Carlo.
 C5  what 'negligible' is measured against: gravitational binding per nucleon vs
     (a) the AME2020 uncertainty on mu_min (56Fe mass excess sigma = 0.27 keV),
     (b) the 4-decimal print of the pair floor 1.9975 Mc^2,
     (c) the slack the tree's own mu_min already takes by dropping all Z electron
         masses (Z m_e / A per nucleon for 56Fe).
 C6  sensitivity to G: CODATA 2018 = CODATA 2022 = 6.67430(15)e-11; a shift of G
     by the full inter-experiment scatter (taken as 1e-3 relative, generous) or even
     by a factor 10 cannot bring the ratio anywhere near any of the C5 scales.
 C7  GR correction: Newtonian binding is the leading term; the post-Newtonian
     correction is O((GM/Rc^2)^2) ~ 1e-51 relative.
Exit 0 iff every check passes.
"""
import math, sys, random
import sympy as sp

ok = True
def chk(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  -- " + detail if detail else ""))

# ---- inputs (tree's own) ---------------------------------------------------
G = 6.67430e-11          # ladder.py:54 ; CODATA 2018 and 2022 value
C = 299792458.0          # exact
M = 70.0                 # stock.feedstock_kg payload_kg default
R = 1.0                  # massform.py:2010 H-R
MEV_J = 1.602176634e-13
U_MEV = 931.4941024171441   # massform.U_MEV
ME_MEV = 0.510998951        # massform.MASS_MEV["e"]
MU_MIN = 930.1745821898941   # massform.MU_MIN (56Fe), recomputed below
FE56_DELTA_KEV, FE56_SIG_KEV = -60607.16, 0.27   # AME2020 Table I row (repo capture)

# C1
ratio = G * M / (R * C**2)
print("G M/(R c^2) =", "%.6e" % ratio)
chk("C1 ratio reproduces the printed 5.2e-26 at 2 s.f.", round(ratio / 1e-26, 1) == 5.2,
    "%.4e" % ratio)
mu = (56 * U_MEV + FE56_DELTA_KEV / 1000 - 26 * ME_MEV) / 56
chk("C1b mu_min(56Fe) recomputed from the AME row", abs(mu - MU_MIN) < 1e-9, "%.7f MeV" % mu)

# C2 uniform ball
r, Rs, Gs, Ms, rho = sp.symbols("r R G M rho", positive=True)
m_r = sp.Rational(4, 3) * sp.pi * r**3 * rho
dm = 4 * sp.pi * r**2 * rho
U = sp.integrate(-Gs * m_r * dm / r, (r, 0, Rs))
U = sp.simplify(U.subs(rho, Ms / (sp.Rational(4, 3) * sp.pi * Rs**3)))
k_uniform = sp.simplify(-U * Rs / (Gs * Ms**2))
chk("C2 uniform ball: U = -(3/5) G M^2/R (sympy)", k_uniform == sp.Rational(3, 5), str(k_uniform))

# C3 n=1 polytrope: rho = rho_c sin(x)/x, x = pi r/R
x = sp.symbols("x", positive=True)
rc = sp.symbols("rho_c", positive=True)
a = Rs / sp.pi
dens = rc * sp.sin(x) / x
mx = sp.integrate(4 * sp.pi * a**3 * x**2 * dens, (x, 0, x))
Mtot = sp.simplify(mx.subs(x, sp.pi))
U1 = sp.integrate(sp.simplify(-Gs * mx * 4 * sp.pi * a**3 * x**2 * dens / (a * x)), (x, 0, sp.pi))
k1 = sp.nsimplify(sp.simplify(-U1 * Rs / (Gs * Mtot**2)))
chk("C3 n=1 polytrope: k = 3/4 = 3/(5-n) (sympy)", k1 == sp.Rational(3, 4), str(k1))

def lane_emden_k(n, h=1e-4):
    """RK4 Lane-Emden; returns k = |U| R/(G M^2) from the density profile theta^n."""
    xi, th, dth = 1e-6, 1.0 - 1e-12 / 6, -1e-6 / 3
    m = 0.0; W = 0.0
    def f(xi, th, dth):
        return dth, -max(th, 0.0) ** n - 2 * dth / xi
    while th > 0:
        k1a, k1b = f(xi, th, dth)
        k2a, k2b = f(xi + h/2, th + h/2*k1a, dth + h/2*k1b)
        k3a, k3b = f(xi + h/2, th + h/2*k2a, dth + h/2*k2b)
        k4a, k4b = f(xi + h, th + h*k3a, dth + h*k3b)
        dm = 4 * math.pi * xi**2 * max(th, 0) ** n * h
        W += m * dm / xi
        m += dm
        th += h/6*(k1a+2*k2a+2*k3a+k4a); dth += h/6*(k1b+2*k2b+2*k3b+k4b); xi += h
    return W * xi / m**2
for n in (1.5, 3.0):
    kn = lane_emden_k(n)
    chk("C3 Lane-Emden n=%.1f numeric k vs 3/(5-n)" % n, abs(kn / (3 / (5 - n)) - 1) < 5e-3,
        "k = %.4f vs %.4f" % (kn, 3 / (5 - n)))

# C4 realistic bodies
def ball(rho_):
    Rb = (3 * M / (4 * math.pi * rho_)) ** (1 / 3)
    return Rb, 0.6 * G * M / (Rb * C**2)
Rw, fw = ball(1000.0)
Ro, fo = ball(22590.0)
print("uniform 70 kg ball, water density: R = %.3f m, |U|/Mc^2 = %.3e" % (Rw, fw))
print("uniform 70 kg ball, osmium density: R = %.4f m, |U|/Mc^2 = %.3e  (cap for rho <= rho_Os)" % (Ro, fo))
random.seed(1)
L, rad = 1.75, math.sqrt(M / 1000.0 / (math.pi * 1.75))
Nmc, s = 400000, 0.0
for _ in range(Nmc):
    def pt():
        while True:
            u, v = random.uniform(-rad, rad), random.uniform(-rad, rad)
            if u*u + v*v <= rad*rad:
                return u, v, random.uniform(0, L)
    p, q = pt(), pt()
    s += 1.0 / math.dist(p, q)
Ucyl = 0.5 * G * M * M * s / Nmc
fc = Ucyl / (M * C**2)
print("70 kg water cylinder 1.75 m x r=%.3f m: |U|/Mc^2 = %.3e (MC)" % (rad, fc))
chk("C4 every realistic 70 kg body stays below 1e-24 of Mc^2", max(fw, fo, fc) < 1e-24,
    "max %.2e" % max(fw, fo, fc))
chk("C4b R = 1 m with k = 1 under-states a water-density body by a factor < 10 (order kept)",
    1 < fw / ratio < 10 and 1 < fc / ratio < 10, "x%.2f (ball), x%.2f (cylinder)" % (fw/ratio, fc/ratio))

# C5 scales
grav_per_nucleon_mev = fo * MU_MIN          # use the density-capped worst case
sig_mu = FE56_SIG_KEV / 1000 / 56
floor_print = 0.5e-4                          # half a unit of the 4th decimal, in Mc^2
electron_slack = 26 * ME_MEV / 56            # MeV per nucleon dropped by the tree
print("grav binding per nucleon (worst case) = %.3e MeV" % grav_per_nucleon_mev)
print("AME sigma on mu_min = %.3e MeV; electron slack = %.4f MeV" % (sig_mu, electron_slack))
chk("C5a below the AME2020 uncertainty on mu_min by > 15 decades",
    math.log10(sig_mu / grav_per_nucleon_mev) > 15, "%.1f decades" % math.log10(sig_mu / grav_per_nucleon_mev))
chk("C5b cannot move the printed 1.9975 Mc^2", fo < floor_print, "")
chk("C5c the tree's dropped electron mass (Z m_e/A) exceeds it by > 20 decades",
    math.log10(electron_slack / grav_per_nucleon_mev) > 20,
    "%.1f decades" % math.log10(electron_slack / grav_per_nucleon_mev))

# C6 G sensitivity
chk("C6 G x10 still leaves the worst case below the AME sigma",
    10 * grav_per_nucleon_mev < sig_mu, "")

# C7 GR
chk("C7 post-Newtonian correction O(ratio^2) < 1e-50", ratio**2 < 1e-50, "%.1e" % ratio**2)

# scope marker (not a failure): the claim is scale-bound
for name, Mb, Rb in (("Sun", 1.989e30, 6.957e8), ("1.4 Msun neutron star, R = 12 km", 1.4*1.989e30, 1.2e4)):
    print("scope: %s  G M/(R c^2) = %.3e" % (name, G * Mb / (Rb * C**2)))
print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
