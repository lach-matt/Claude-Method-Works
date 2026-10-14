#!/usr/bin/env python3
"""DOCKET 67 / codata-g-and-constants -- re-derivation and sensitivity audit.

Audits the five SI constants wall.py uses (c, G, g_n, M_sun, AU) against the
tables they come from, and measures how far each of wall.py's dimensional
figures moves with G.

Sources READ locally (the network routes to arxiv/NIST/IAU are egress-blocked
and the alphaXiv quota was exhausted in this run):
  * CODATA 2002..2022 ASCII tables from NIST, as transcribed verbatim in
    scipy 1.17.1 scipy/constants/_codata.py (cached wheel, src/codata/x/...).
  * IAU 2012 B2 (au) and IAU 2015 B3 (nominal GM_sun) as encoded in
    astropy 8.0.1 astropy/constants/iau2015.py (src/astropy_x/...).
wall.py is imported read-only from the research tree; nothing is written there.
"""
import math, re, sys, importlib.util, os
import sympy as sp

D67 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
CODATA_TXT = D67 + "/src/codata/x/scipy/constants/_codata.py"
IAU_TXT = D67 + "/src/astropy_x/astropy/constants/iau2015.py"
WALL = "/home/user/Claude-Method-Works/research/warp-drive/wall.py"

ok = True
def chk(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  %-66s %s %s" % (label, "ok  " if cond else "FAIL", detail))

# ---------------------------------------------------------------- 1. the tables
src = open(CODATA_TXT).read()
def codata(year, name):
    blk = src.split('txt%d = """' % year, 1)[1].split('"""', 1)[0]
    for line in blk.splitlines():
        if line.startswith(name + "  "):
            rest = line[len(name):].strip()
            parts = re.split(r"\s{2,}", rest)
            val = float(parts[0].replace(" ", "").replace("...", ""))
            unc = 0.0 if "exact" in parts[1] else float(parts[1].replace(" ", ""))
            return val, unc
    raise KeyError((year, name))

print("1. THE TABLES (CODATA via NIST ASCII tables in scipy 1.17.1)")
Gs = {y: codata(y, "Newtonian constant of gravitation") for y in (2006, 2010, 2014, 2018, 2022)}  # scipy's txt2002 is a partial table with no G row
for y, (v, u) in Gs.items():
    print("      CODATA %d  G = %.5e  u = %.2e  u_r = %.2e" % (y, v, u, u / v))
c18 = codata(2018, "speed of light in vacuum"); c22 = codata(2022, "speed of light in vacuum")
g18 = codata(2018, "standard acceleration of gravity"); g22 = codata(2022, "standard acceleration of gravity")
chk("c = 299792458 m/s exact in 2018 and 2022", c18 == (299792458.0, 0.0) and c22 == c18)
chk("g_n = 9.80665 m/s^2 exact (conventional) in 2018 and 2022", g18 == (9.80665, 0.0) and g22 == g18)
chk("G(2018) = 6.67430e-11, u = 0.00015e-11", Gs[2018] == (6.67430e-11, 0.00015e-11))
chk("G(2022) unchanged from 2018", Gs[2022] == Gs[2018])
G, uG = Gs[2018]
urG = uG / G
chk("u_r(G) = 2.2e-5", abs(urG - 2.247e-5) < 1e-8, "(%.4e)" % urG)

iau = open(IAU_TXT).read()
def iau_val(sym):
    m = re.search(r'^%s = IAU2015\(\s*"[^"]*",\s*"[^"]*",\s*([0-9.eE+-]+),' % sym, iau, re.M)
    return float(m.group(1))
AU = iau_val("au"); GMsun = iau_val("GM_sun")
print("      IAU 2012 B2  au = %.11e m (exact by definition)" % AU)
print("      IAU 2015 B3  nominal GM_sun = %.7e m^3 s^-2" % GMsun)
chk("AU = 1.495978707e11 m, exact by IAU 2012 Resolution B2", AU == 1.495978707e11)

# ---------------------------------------------------------------- 2. wall.py's values
spec = importlib.util.spec_from_file_location("wall", WALL)
wall = importlib.util.module_from_spec(spec); spec.loader.exec_module(wall)
print("\n2. WALL.PY's VALUES AGAINST THE TABLES")
chk("wall.C == CODATA c", wall.C == c18[0])
chk("wall.G_SI == CODATA 2018/2022 G", wall.G_SI == G)
MSUN_WALL = 1.98847e30
M18 = GMsun / Gs[2018][0]; M14 = GMsun / Gs[2014][0]
print("      GM_sun/G(2018) = %.6e kg ;  GM_sun/G(2014) = %.6e kg ;  wall uses %.5e" % (M18, M14, MSUN_WALL))
chk("wall's M_sun = 1.98847e30 is GM_sun/G(2014) = 1.988475e30 truncated (|rel| < 3e-6)", abs(MSUN_WALL / M14 - 1) < 3e-6, "(%+.2e)" % (MSUN_WALL / M14 - 1))
chk("wall's M_sun does NOT equal GM_sun/G(2018) to 5 s.f. (1.98841)", round(M18 / 1e30, 5) != 1.98847)
dM = MSUN_WALL / M18 - 1.0
print("      DISCREPANCY: M_sun(wall) / (GM_sun/G_wall) - 1 = %+.3e  (= %.2f sigma of G(2018))" % (dM, dM / urG))
chk("the pairing G(2018) with a 2014-derived M_sun is off by 3.0e-5", abs(dM - 3.0e-5) < 0.1e-5)

# ---------------------------------------------------------------- 3. G-exponents (sympy)
print("\n3. HOW EACH DIMENSIONAL FIGURE SCALES WITH G (sympy, from wall.py's formulas)")
Gs_, c_, a_, eta_, k_, M_, R_, x_, n_, GMs_ = sp.symbols("G c a eta k M R x n GMsun", positive=True)
rho = 3 * a_**2 / (4 * sp.pi * Gs_ * (k_ * c_ * eta_)**2)                 # max_mean_density
rmin = (Gs_ * M_ * (k_ * c_ * eta_ / (n_ * a_))**2)**sp.Rational(1, 3)     # min_radius
Rceil = c_ * sp.sqrt(3 * x_ / (8 * sp.pi * Gs_ * rho))                     # radius_at_ceiling
Mceil = x_ * Rceil * c_**2 / (2 * Gs_)                                      # mass_at_ceiling (kg)
Msun_consistent = GMs_ / Gs_
Nef = k_ * sp.sqrt(Gs_ * M_ / R_**3) * c_ * eta_ / a_                        # efoldings
xship = 2 * Gs_ * M_ / (R_ * c_**2)
sig_small = (xship / 2) * c_**2 / (4 * sp.pi * Gs_ * R_)                    # (1-s) ~ x/2 as x->0
ten_small = (xship / 2)**2 / (16 * sp.pi * R_) * c_**4 / Gs_                # p0 c^4/G, sqrt(1-x) -> 1
shortfall = eta_ / (a_ * R_ / c_**2)
exps = {
    "rho ceiling (2.658e-4 kg/m^3)": rho,
    "R_min at N=1 (965 m) and N=0.1 (4.48 km)": rmin,
    "e-foldings of a fixed (M,R) ship": Nef,
    "R at ceiling, fixed x (1034 AU, 2850 AU)": Rceil,
    "M at ceiling in kg": Mceil,
    "M at ceiling in Msun, M_sun = GM_sun/G (consistent)": Mceil / Msun_consistent,
    "M at ceiling in Msun, M_sun a fixed kg number (wall.py)": Mceil,
    "x of the 1000 t, 4478 m ship (3.3e-25)": xship,
    "wall areal density, x->0 (3.97 g/m^2)": sig_small,
    "wall tension, x->0 (1.5e-11 N/m)": ten_small,
    "marginal shortfall / adiabatic margin (1.8e14, 2.2e14)": shortfall,
}
E = {}
for lbl, f in exps.items():
    e = sp.simplify(Gs_ * sp.diff(sp.log(f), Gs_))
    E[lbl] = e
    print("      d ln F / d ln G = %-5s  %s" % (sp.nsimplify(e), lbl))
chk("rho ceiling ~ 1/G", E["rho ceiling (2.658e-4 kg/m^3)"] == -1)
chk("R_min ~ G^(1/3)", E["R_min at N=1 (965 m) and N=0.1 (4.48 km)"] == sp.Rational(1, 3))
chk("R at ceiling is G-INDEPENDENT", E["R at ceiling, fixed x (1034 AU, 2850 AU)"] == 0)
chk("M in Msun is G-INDEPENDENT when M_sun = GM_sun/G", E["M at ceiling in Msun, M_sun = GM_sun/G (consistent)"] == 0)
chk("areal density at fixed (M,R) is G-INDEPENDENT (the mass closes)", E["wall areal density, x->0 (3.97 g/m^2)"] == 0)
chk("the 1.8e14 / 2.2e14 inversion figures carry no G", E["marginal shortfall / adiabatic margin (1.8e14, 2.2e14)"] == 0)

# ---------------------------------------------------------------- 4. numbers under moved G
print("\n4. THE FIGURES UNDER EVERY RECOMMENDED G 2006-2022, +-1 sigma, and a +-1000 ppm stress")
print("   (the stress band is NOT a datum: it is a deliberately wide bracket, ~20x u_r(2018))")
def figures(Gv, msun_kg):
    save = wall.G_SI
    wall.G_SI = Gv
    try:
        out = dict(
            rho=wall.max_mean_density(0.2, 9.80665),
            rmin=wall.min_radius(1.0e6, 0.2, 9.80665),
            r10=wall.min_radius(1.0e6, 0.2, 9.80665, n=0.1),
            nsmall=wall.efoldings(1.0e6, 10.0, 0.2, 9.80665),
            R_AU=wall.radius_at_ceiling(0.0396) / AU,
            M1=wall.mass_at_ceiling(0.0396) / msun_kg,
            M3=wall.mass_at_ceiling(0.3) / msun_kg,
            xs=2.0 * Gv * 1.0e6 / (4478.0 * wall.C ** 2),
        )
        out["sig"] = wall.surface_density(out["xs"], 4478.0) * 1000.0
        out["ten"] = wall.surface_tension(out["xs"], 4478.0)
        out["sf"] = wall.marginal_shortfall(0.2, 9.80665, 10.0)
    finally:
        wall.G_SI = save
    return out
cases = [("wall.py as written", G, MSUN_WALL)]
for y in (2006, 2010, 2014, 2018):
    cases.append(("CODATA %d, M_sun=GM/G" % y, Gs[y][0], GMsun / Gs[y][0]))
cases += [("2018 +1 sigma, consistent", G * (1 + urG), GMsun / (G * (1 + urG))),
          ("2018 -1 sigma, consistent", G * (1 - urG), GMsun / (G * (1 - urG))),
          ("stress +1000 ppm, consistent", G * 1.001, GMsun / (G * 1.001)),
          ("stress -1000 ppm, consistent", G * 0.999, GMsun / (G * 0.999)),
          ("stress +1000 ppm, M_sun fixed kg", G * 1.001, MSUN_WALL)]
hdr = ("case", "rho kg/m3", "Rmin m", "R10 km", "N(10m)", "R AU", "M(1%) Msun", "M(.3) Msun", "g/m2", "N/m", "shortfall")
print("   %-32s" % hdr[0] + "".join("%12s" % h for h in hdr[1:]))
rows = {}
for lbl, Gv, ms in cases:
    f = figures(Gv, ms); rows[lbl] = f
    print("   %-32s%12.6e%12.3f%12.6f%12.2f%12.3f%12.5e%12.5e%12.5f%12.5e%12.4e"
          % (lbl, f["rho"], f["rmin"], f["r10"] / 1e3, f["nsmall"], f["R_AU"], f["M1"], f["M3"], f["sig"], f["ten"], f["sf"]))
base = rows["wall.py as written"]
print()
for lbl, f in rows.items():
    concl = (f["nsmall"] > 100 and 960 < f["rmin"] < 970 and 4.4 < f["r10"] / 1e3 < 4.55
             and 1000 < f["R_AU"] < 1100 and 1.9e9 < f["M1"] < 2.2e9 and 4.2e10 < f["M3"] < 4.5e10
             and f["sig"] < 7.0 and f["ten"] < 1e-10 and f["sf"] > 1e13)
    chk("prose conclusions of wall.py hold under: %s" % lbl, concl)
    # wall.py's own selftest tolerances on the dimensional figures
    tol = (abs(f["rmin"] - 964.4) <= 0.5 and abs(f["R_AU"] - 1034.4) <= 1.0
           and abs(f["M1"] - 2.075e9) <= 1e6 and abs(f["M3"] - 4.327e10) <= 1e7
           and abs(f["ten"] - 1.4787e-11) <= 1e-15 and abs(f["sig"] - 3.968) <= 1e-3)
    tight = abs(f["rho"] - 2.657927437e-4) <= 1e-12 and abs(f["r10"] / 1e3 - 4.478398718) <= 1e-8
    print("      loose selftest pins %s ; 1e-9-relative arithmetic pins %s"
          % ("hold" if tol else "MOVE", "hold" if tight else "move (expected: they pin CODATA-2018 arithmetic)"))

# ---------------------------------------------------------------- 5. internal pins
print("\n5. WALL.PY's OWN ARITHMETIC, RE-DONE BY HAND")
rho_hand = 3 * 9.80665**2 / (4 * math.pi * G * (0.6 * 299792458.0 * 0.2)**2)
chk("rho ceiling = 2.657927437e-4 kg/m^3", abs(rho_hand - 2.657927437e-4) < 1e-12, "(%.10e)" % rho_hand)
chk("R_min(N=1) prints as 965 m in the docstring (964.84 m)", round(base["rmin"]) == 965, "(%.4f)" % base["rmin"])
print("      NOTE: the selftest LABEL says 'R > 964 m' and pins 964.4 +- 0.5; the value is 964.84.")
print("            A label/pin discrepancy inside the tree, 0.05%, not an external-data issue.")
chk("x = 0.3 radius prints as 2,850 AU", round(wall.radius_at_ceiling(0.3) / AU, -1) == 2850, "(%.1f AU)" % (wall.radius_at_ceiling(0.3) / AU))
chk("1% binding radius 1034 AU", round(base["R_AU"]) == 1034, "(%.3f)" % base["R_AU"])

print("\n  RE-DERIVATION %s" % ("OK" if ok else "FAILED"))
sys.exit(0 if ok else 1)
