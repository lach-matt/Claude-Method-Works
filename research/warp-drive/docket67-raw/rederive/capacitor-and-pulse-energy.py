#!/usr/bin/env python3
"""DOCKET 67 -- audit 'capacitor-and-pulse-energy' (warpfolder.py:49-53, 277-289).

Re-derives, from first principles and from the folder documents' own printed
parameters (READ 2026-09-26 through the Drive connector), the device store the
tree computes, and tests how far each named hypothesis moves the conclusion.

Exit 0 iff every assertion holds.  sympy for the closed forms, float for data.
"""
import math, sys
import sympy as sp

fails = []
def chk(label, cond, val=""):
    print("  [%s] %-66s %s" % ("ok" if cond else "XX", label, val))
    if not cond:
        fails.append(label)

# ---------------------------------------------------------------- 1. theorem
V, Q, Cs, n, t, P = sp.symbols("V Q C n t P", positive=True)
# work to charge a LINEAR capacitor Q = C V:  W = int_0^Q (q/C) dq
q = sp.symbols("q", positive=True)
W = sp.integrate(q / Cs, (q, 0, Cs * V))
chk("E = int V dQ = (1/2) C V^2 for a linear capacitor", sp.simplify(W - Cs*V**2/2) == 0, W)
# Marx: n caps each charged to V in parallel, erected in series: C/n at nV
E_par = n * Cs * V**2 / 2
E_ser = (Cs / n) * (n * V)**2 / 2
chk("Marx erected (C/n at nV) stores the same n*(1/2)CV^2 as parallel charge",
    sp.simplify(E_par - E_ser) == 0, sp.simplify(E_ser))
# if 50 kV were the ERECTED output instead of per-stage charge (reading NOT in the doc)
E_alt = n * Cs * (V / n)**2 / 2

# ------------------------------------------------------------------ 2. data
C1, V1, N = 100e-9, 50e3, 10
marx = N * 0.5 * C1 * V1**2
chk("Marx store 10 x (1/2)(100 nF)(50 kV)^2 = 1250 J", abs(marx - 1250) < 1e-9, marx)
marx_if_500kV_total = float(E_alt.subs({n: 10, Cs: C1, V: 500e3}))
chk("(counterfactual) the doc's 500 kV OUTPUT read as erected: same 1250 J",
    abs(marx_if_500kV_total - 1250) < 1e-9, marx_if_500kV_total)
# rated 60 kV per capacitor (doc's component table): absolute ceiling
marx_rated = N * 0.5 * C1 * 60e3**2
chk("ceiling at the 60 kV capacitor rating = 1800 J", abs(marx_rated - 1800) < 1e-9, marx_rated)
# delivered pulse: 500 kV x 10 kA over ~12-24 ns  <= stored
for tau in (12e-9, 24e-9):
    chk("  delivered V*I*tau at tau=%g ns <= stored 1250 J" % (tau*1e9),
        500e3 * 10e3 * tau <= marx, 500e3 * 10e3 * tau)
# internal consistency of the doc (DISCREPANCY, not load-bearing on the store)
R_load = 500e3 / 10e3
rc = (C1 / N) * R_load
chk("  doc: 500kV/10kA = 50 ohm; erected 10 nF x 50 ohm = 500 ns >> '~12 ns'",
    rc > 10 * 12e-9, "%.3g s" % rc)

# laser, the tree's way: I * pi (d/2)^2 * t, top-hat
I, d, tp = 1e20, 0.1e-1, 30e-15          # W/cm^2, cm, s
area = math.pi * (d / 2)**2
laser_tree = I * area * tp
chk("laser I*A*t (1e20 W/cm^2, 0.1 mm dia, 30 fs, top-hat) = 235.62 J",
    abs(laser_tree - 235.619) < 1e-2, laser_tree)
P_tree = I * area
chk("  implied peak power 7.85 PW < the doc's printed 10 PW", P_tree < 10e15, P_tree)
laser_doc_P = 10e15 * tp
chk("laser from the doc's OWN 'PEAK POWER 10 PW' x 30 fs = 300 J", abs(laser_doc_P - 300) < 1e-9, laser_doc_P)
chk("  and 10 PW over the 0.1 mm spot = 1.27e20 W/cm^2 ('exceeding 1e20' holds)",
    10e15 / area > 1e20, 10e15 / area)
# temporal shape factors (FWHM duration): gaussian sqrt(pi/(4 ln2)), sech^2 1/(2 ln(1+sqrt2)) * ...
g_t = math.sqrt(math.pi / (4 * math.log(2)))
sech_t = 1.0 / (2 * math.log(1 + math.sqrt(2))) * 2  # int sech^2(x/T0) = 2 T0, FWHM = 1.7627 T0
sech_t = 2 / 1.7627471740390860
laser_gauss = 10e15 * tp * g_t
chk("  gaussian-in-time pulse at 10 PW peak, 30 fs FWHM = 319.3 J", abs(laser_gauss - 319.35) < 0.1, laser_gauss)
# spatial gaussian with 0.1 mm = FWHM diameter, peak I = 1e20
g_s = 1 / (4 * math.log(2)) * 4        # area_eff = pi FWHM^2 /(4 ln2) vs pi FWHM^2/4
laser_gauss_sp = I * area * g_s * g_t * tp / 1.0
chk("  gaussian in space (0.1 mm FWHM) and time at PEAK 1e20 = 361.9 J",
    abs(laser_gauss_sp - 361.9) < 0.5, laser_gauss_sp)
laser_per_beam = 8 * laser_doc_P
chk("  (counterfactual) 10 PW PER BEAM x 8 beams = 2400 J", abs(laser_per_beam - 2400) < 1e-9)

# f/1 at 800 nm: diffraction-limited Airy diameter 2.44 lambda N ~ 2 um, not 0.1 mm
airy = 2.44 * 800e-9 * 1.0
chk("  doc: 'diffraction-limited 0.1 mm' at f/1, 800 nm -- Airy is %.2g m (DISCREPANCY)" % airy,
    airy < 0.1e-3 / 10)

# ----------------------------------------------------- 3. the conclusion
c, G, hbar = 2.99792458e8, 6.67430e-11, 1.054571817e-34   # CODATA 2018 = 2022 values
need = 100.0 * c**2
stores = {
    "tree: Marx + laser(I*A*t)":        marx + laser_tree,
    "Marx + laser(doc 10 PW)":          marx + laser_doc_P,
    "Marx@60kV rating + gauss laser":   marx_rated + laser_gauss_sp,
    "Marx@60kV + 8 x 10 PW beams":      marx_rated + laser_per_beam,
}
print()
for k, s in stores.items():
    o = math.log10(need / s)
    print("      %-36s %10.1f J   shortfall %.3e = %.2f orders" % (k, s, need / s, o))
    chk("  %s: still > 15 orders short" % k, o > 15.0)
tree_orders = math.log10(need / (marx + laser_tree))
chk("tree figure 15.7818 orders reproduced", abs(tree_orders - 15.7818) < 1e-4, tree_orders)

# --- the dropped stores: rotor KE and 20 T stator field (the doc gives no mass/volume)
# Envelope: the doc's 2.5 m outer shield, taken as a sphere (NAMED hypothesis H-env).
R_env = 1.25
V_env = 4 / 3 * math.pi * R_env**3
B = 20.0; mu0 = 4e-7 * math.pi
u_B = B**2 / (2 * mu0)
E_field_max = u_B * V_env
chk("20 T field energy density = 1.59e8 J/m^3", abs(u_B - 1.5915e8) / 1.5915e8 < 1e-3, u_B)
# rotor, burst-limited: KE/m <= sigma/rho (ideal constant-stress disc, shape factor K<=1)
sig_rho_T1000 = 6.4e9 / 1800.0
m_env_cf = 1800.0 * V_env
E_rot_burst = sig_rho_T1000 * m_env_cf
# rotor at the DEMANDED 85,000 RPM (it would burst -- warpfolder sect. 3), solid BeCu
# sphere filling the envelope: KE = (1/2)(2/5) m R^2 w^2
w = 85000 * 2 * math.pi / 60
m_env_becu = 8250.0 * V_env
E_rot_demand = 0.5 * 0.4 * m_env_becu * R_env**2 * w**2
print()
print("      envelope volume %.2f m^3; 20 T field if it filled it  %.3e J" % (V_env, E_field_max))
print("      rotor, burst-limited T1000 filling envelope         %.3e J" % E_rot_burst)
print("      rotor at demanded 85k RPM, solid BeCu (bursts)      %.3e J" % E_rot_demand)
bound_phys = marx_rated + laser_per_beam + E_field_max + E_rot_burst
bound_absurd = marx_rated + laser_per_beam + E_field_max + E_rot_demand
o_phys = math.log10(need / bound_phys)
o_abs = math.log10(need / bound_absurd)
print("      store ceiling, physical rotor:  %.3e J -> %.2f orders short" % (bound_phys, o_phys))
print("      store ceiling, bursting rotor:  %.3e J -> %.2f orders short" % (bound_absurd, o_abs))
chk("with rotor+field in the envelope, still short (physical rotor): >8 orders", o_phys > 8.0, o_phys)
chk("even a rotor held at 85k RPM filling the envelope: still >6 orders short", o_abs > 6.0, o_abs)
chk("BUT the '15.78 orders' figure is NOT invariant under H3 (store = Marx+laser)",
    tree_orders - o_phys > 5.0, "%.2f orders move" % (tree_orders - o_phys))
m_close_rotor = need / (0.25 * (math.pi * 1.8 * 85000 / 60)**2)
print("      rotor mass that would close the gap at the demanded tip speed (disc): %.3e kg" % m_close_rotor)
V_close_field = need / u_B
print("      20 T field volume that would close the gap: %.3e m^3 (cube of %.2f km)" % (V_close_field, V_close_field**(1/3)/1e3))

# ------------------------------------------ 4. the Planck comparison, every reading
EP = math.sqrt(hbar * c**5 / G)
lP = math.sqrt(hbar * G / c**3)
IP = (c**5 / G) / lP**2 / 1e4               # W/cm^2
uP = EP / lP**3
I_doc = 10e15 / area
print()
chk("Planck energy 1.956e9 J", abs(EP - 1.9561e9) / 1.9561e9 < 1e-3, EP)
fracE = (marx + laser_tree) / EP
chk("tree's reading (total energy / E_P) = 7.595e-7", abs(fracE - 7.595e-7) / 7.595e-7 < 1e-3, fracE)
fracI = I_doc / IP
chk("the doc's words ('optical INTENSITY ... Planck threshold'): I/I_P = %.2e" % fracI, fracI < 1e-90)
u_focus = I_doc * 1e4 / c
chk("focal energy density / Planck energy density = %.2e" % (u_focus / uP), u_focus / uP < 1e-90)
I_schwinger = 2.3e29
chk("not even the Schwinger intensity (~2.3e29 W/cm^2): ratio %.1e" % (I_doc / I_schwinger), I_doc < I_schwinger)
chk("the tree's energy reading is the MOST generous of the three (not over-stated against the doc)",
    fracE > fracI and fracE > u_focus / uP)

# ---------------------------------------------- 5. constants datum drift
G_codata2014 = 6.67408e-11
EP14 = math.sqrt(hbar * c**5 / G_codata2014)
chk("CODATA 2014 -> 2018/2022 G move changes E_P by <2e-5 relative", abs(EP14 / EP - 1) < 2e-5, EP14 / EP - 1)

# ------------------------------------------ 6. the double count (doc sect. 2: "The 500 kV output
# pulse drives an array of eight CPA laser heads") -- if the Marx pulse powers the lasers, the laser
# energy is DRAWN FROM the 1250 J, and Marx + laser counts it twice.  In the document's favour.
o_single = math.log10(need / marx)
chk("Marx alone (laser drawn from it): %.4f orders vs tree 15.7818 -- moves %.3f, doc's favour"
    % (o_single, o_single - tree_orders), 0 < o_single - tree_orders < 0.1)
fracE_focus = laser_doc_P / EP
chk("energy that reaches the FOCUS is the laser's only: %.2e of E_P (tree prints 7.6e-7 for the whole store)"
    % fracE_focus, fracE_focus < fracE)

print()
print("FAILS:", len(fails))
sys.exit(1 if fails else 0)
