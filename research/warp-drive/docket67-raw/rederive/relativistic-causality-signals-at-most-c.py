#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key relativistic-causality-signals-at-most-c.

Read-only against research/warp-drive/transit.py (imported, never written).
Checks, each printed with PASS/FAIL:

 1. transit.advantage_over_light(D) is an identity: D/c - D/c == 0 for every c>0
    (sympy), and bit-exact 0.0 at the four DISTANCES (float) -> the printed
    0.000 records the channel MODEL, it does not test the causality principle.
 2. The load-bearing direction: if every channel satisfies v <= c, then
    arrival >= D/c and advantage <= 0 (sympy, symbolic v in (0,c]).
 3. Characteristic (front) velocity of Klein-Gordon is c for m^2 of EITHER sign
    (LSV 2002 fn 13; Geroch 2010 p.7): lim_{k->oo} omega/k = 1.  The tachyonic
    GROUP velocity k/omega exceeds 1 -- the front does not.
 4. Geroch 2010 p.7: a perfect fluid's sound cone has (v/c)^2 = dp/drho; the
    causal cone lies inside the light cone iff dp/drho <= 1.  That bound is a
    property of the matter equation, NOT of special relativity (named H_cone).
 5. Scharnhorst (hep-th/9810221 eq.10): n_perp(0) = 1 - 11 pi^2/90^2 alpha^2/(mL)^4.
    Magnitude at L = 1 um, 10 um; the advantage one gap could buy; and (sympy)
    along the plates the ray (group) velocity component is <= c exactly, so a
    Casimir channel gives NO advantage over any distance D >> L.
    Also records the Fearn 0706.0553 figure 1.6e-36 "at 1 um" against the
    formula (discrepancy, not refutation).
 6. GW170817 bound (arXiv:1710.05834 eq.1) recomputed from 1.74 s, 26 Mpc, 10 s.
 7. OPERA 2012 (arXiv:1109.4897v4): (v-c)/c from delta t = 6.5 ns over 730.085 km.
"""
import importlib.util, math, sys
from fractions import Fraction
import sympy as sp

RES = []
def chk(name, ok, detail=""):
    RES.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name + (("  :: " + detail) if detail else ""))

TRANSIT = "/home/user/Claude-Method-Works/research/warp-drive/transit.py"
spec = importlib.util.spec_from_file_location("transit_ro", TRANSIT)
transit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(transit)

# ---------------------------------------------------------------- 1
D, c, v = sp.symbols("D c v", positive=True)
adv = D / c - D / c
chk("1a sympy: advantage_over_light = D/c - D/c == 0 identically", sp.simplify(adv) == 0)
vals = [(n, d, transit.advantage_over_light(d)) for n, d in transit.DISTANCES]
chk("1b float: advantage is bit-exact 0.0 at all four DISTANCES",
    all(a == 0.0 for _, _, a in vals), "; ".join("%s %.4g m -> %r" % x for x in vals))
chk("1c C_SI equals SI c exactly (Fraction)", Fraction(transit.C_SI) == 299792458)
chk("1d BEATS_LIGHT flag is False (a constant, not a computation)", transit.BEATS_LIGHT is False)
# light times, for the record
for n, d in transit.DISTANCES:
    print("     light time %-18s %.6g s = %.6g yr" % (n, d / 299792458, d / 299792458 / 3.15576e7))

# ---------------------------------------------------------------- 2
# channel speed v with 0 < v <= c: advantage(v) = D/v - D/c >= 0 means the channel is LATER
lam = sp.symbols("lam", positive=True)          # v = c*lam, 0<lam<=1
delay = sp.simplify(D / (c * lam) - D / c)       # = D(1-lam)/(c lam)
chk("2a sympy: v=c*lam, delay = D(1-lam)/(c*lam)",
    sp.simplify(delay - D * (1 - lam) / (c * lam)) == 0, str(delay))
chk("2b delay >= 0 for 0<lam<=1 (numerical grid) -> advantage <= 0 needs ONLY v<=c",
    all(float(delay.subs({D: 1, c: 1, lam: l})) >= 0 for l in [1e-6, 0.1, 0.5, 0.999999, 1.0]))
chk("2c delay < 0 for lam>1 -> the conclusion is exactly as strong as the hypothesis v<=c",
    all(float(delay.subs({D: 1, c: 1, lam: l})) < 0 for l in [1.000001, 1.5, 10]))

# ---------------------------------------------------------------- 3
k, m2 = sp.symbols("k m2", real=True)
kp = sp.symbols("kp", positive=True)
for sign, label in [(1, "m^2>0"), (0, "m^2=0"), (-1, "m^2<0 (tachyonic)")]:
    M2 = sign * sp.Integer(1)
    omega = sp.sqrt(kp**2 + M2)
    front = sp.limit(omega / kp, kp, sp.oo)
    chk("3 KG %s: front velocity lim omega/k = %s" % (label, front), front == 1)
omega_t = sp.sqrt(kp**2 - 1)
vg = sp.diff(omega_t, kp)
chk("3' tachyonic KG group velocity k/omega > 1 for k>|m| (e.g. k=2: %.4f) yet front = 1"
    % float(vg.subs(kp, 2)), float(vg.subs(kp, 2)) > 1)
# principal symbol independence of mass: the characteristic polynomial g^{ab} xi_a xi_b
w, q = sp.symbols("w q")
symb_massive = sp.Poly(-w**2 + q**2 + m2, w, q)  # full symbol
principal = sum(t for t in (-w**2 + q**2 + m2).as_ordered_terms() if sp.Poly(t, w, q).total_degree() == 2)
chk("3'' principal symbol of KG is -w^2+q^2, independent of m^2 (characteristics = light cone)",
    sp.simplify(principal - (-w**2 + q**2)) == 0)

# ---------------------------------------------------------------- 4
cs2 = sp.symbols("cs2", positive=True)  # dp/drho
# sound cone speed^2 = cs2 (c=1); spacelike vectors in the cone iff cs2 > 1
s_ = sp.symbols("s", positive=True)     # spatial speed of a direction xi=(1,s) in the fluid rest frame
# Geroch p.7 cone: u.xi<0 and (g + (1-cs2) u u)(xi,xi) > 0 ; with u=(1,0), g=diag(-1,1):
cone_form = -1 + s_**2 + (1 - cs2) * 1      # = s^2 - cs2 ; Geroch's inequality selects the complement,
# i.e. directions with speed s < sqrt(cs2) (the paper: 'speed ... less than the sound speed v')
chk("4a sound-cone boundary speed^2 = dp/drho (sympy: s^2 - cs2 = 0 at s = sqrt(cs2))",
    sp.solve(sp.Eq(cone_form, 0), s_) == [sp.sqrt(cs2)])
chk("4b a spacelike direction (s>1) lies in the cone iff dp/drho > 1 (grid cs2 in {0.25,0.5,1,1.01,1.5,2,4})",
    all((max(1.0, math.sqrt(C2)) > 1.0) == (C2 > 1)            # sup of cone speeds = sqrt(cs2) exceeds 1 iff cs2>1
        and (any(1 < x and x * x < C2 for x in [1 + j / 1000 for j in range(1, 3000)]) == (C2 > 1))
        for C2 in [0.25, 0.5, 1.0, 1.01, 1.5, 2.0, 4.0]))
print("     (Geroch 2010 p.7: the hyperbolization exists for dp/drho>0 whether or not dp/drho>1;"
      " the <=1 bound is an extra hypothesis on the equation of state, H_cone)")

# ---------------------------------------------------------------- 5
alpha = 7.2973525643e-3           # CODATA 2022 fine-structure constant
lamC = 3.8615926744e-13           # reduced Compton wavelength of electron, m (CODATA 2022)
coef = 11 * math.pi**2 / 90**2
def dcc(L):                        # c/n -1 ~ 1-n to first order
    return coef * alpha**2 * (lamC / L)**4
for L in (1e-6, 1e-5, 1e-7):
    print("     Scharnhorst dc/c at L=%g m: %.3e ; one-gap advantage L/c*dc/c = %.3e s ; mL=%.3g"
          % (L, dcc(L), L / 299792458 * dcc(L), L / lamC))
chk("5a Scharnhorst dc/c at 1 um is ~1.6e-32 from eq.(10)", 1.5e-32 < dcc(1e-6) < 1.7e-32,
    "%.3e" % dcc(1e-6))
chk("5b Fearn 0706.0553's '1.6e-36 at 1 um' matches eq.(10) at L=10 um, not 1 um "
    "(DISCREPANCY in a later paper, recorded, not a refutation)",
    abs(dcc(1e-5) - 1.6e-36) / 1.6e-36 < 0.05 and abs(dcc(1e-6) / 1.6e-36 - 1e4) / 1e4 < 0.05,
    "eq10(1um)=%.3e eq10(10um)=%.3e" % (dcc(1e-6), dcc(1e-5)))
# along-plate transport: effective dispersion omega^2 = k_par^2 + (1+xi) k_perp^2  (LSV eq 3.2, xi>0)
kpar, kperp, xi = sp.symbols("kpar kperp xi", positive=True)
Om = sp.sqrt(kpar**2 + (1 + xi) * kperp**2)
vg_par = sp.diff(Om, kpar)
vg_perp = sp.diff(Om, kperp)
chk("5c group velocity along plates = kpar/omega <= 1 exactly (sympy: 1 - vg_par^2 = (1+xi)kperp^2/omega^2 >= 0)",
    sp.simplify(1 - vg_par**2 - (1 + xi) * kperp**2 / Om**2) == 0)
chk("5d perpendicular to plates vg -> sqrt(1+xi) > 1 (the only superluminal component, bounded by gap L)",
    sp.simplify(vg_perp.subs(kpar, 0) - sp.sqrt(1 + xi)) == 0)
# zig-zag between reflecting plates: net along-plate speed = vg_par <= 1 -> no advantage over D >> L

# ---------------------------------------------------------------- 6
Mpc = 3.0856775814913673e22
tD = 26 * Mpc / 299792458.0
up = 1.74 / tD
lo = (1.74 - 10.0) / tD
chk("6 GW170817: +1.74 s / (26 Mpc / c) = %.2e (paper +7e-16); (1.74-10) s -> %.2e (paper -3e-15)" % (up, lo),
    6.0e-16 < up < 7.0e-16 and -3.2e-15 < lo < -3.0e-15)

# ---------------------------------------------------------------- 7
L_opera = 730.085e3
tof = L_opera / 299792458.0
dt = 6.5e-9
vc = dt / (tof - dt)
chk("7 OPERA 2012: 6.5 ns / (730.085 km / c) = %.2e (paper 2.7e-6)" % vc, 2.6e-6 < vc < 2.8e-6)
print("     (the originally reported 2011 anomaly, v1-v3, is NAMED-NOT-READ here; v4 Sec.6.1 READ:"
      " fibre-delay and 0.124 ppm oscillator offsets identified as its instrumental sources)")

print("\nSUMMARY: %d/%d PASS" % (sum(RES), len(RES)))
sys.exit(0 if all(RES) else 1)
