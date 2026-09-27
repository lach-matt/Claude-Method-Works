#!/usr/bin/env python3
"""DOCKET 67, result 19: the physical constants the warp board carries.

Re-derivation / machine check of every closed-form thing here:
  1. LY = c x Julian year, exact (sympy Rational)         -> tree's 9.4607304725808e15
  2. M_sun = (GM)_sun^N / G for G_2006, G_2014, G_2018   -> tree's 1.98840e30 / 1.98847e30 / 1.98892e30
  3. Proxima distance from the Gaia DR3 parallax          -> tree's 4.2465 ly
  4. l_P = sqrt(hbar G / c^3)                             -> CODATA's 1.616255(18)e-35
  5. Every derived figure the tree pins, recomputed with CODATA 2018 vs CODATA 2022
     constants and with G at +-1 sigma, to see whether any moved datum moves a figure.
  6. Discrepancies between owners (phase1 vs foliation) quantified.
Everything printed; exits 1 if a check labelled MUST fails.
"""
import math, sys
from fractions import Fraction
import sympy as sp

fails = []
def chk(label, cond, note=""):
    print(("  OK   " if cond else "  FAIL ") + label + ("  -- " + note if note else ""))
    if not cond: fails.append(label)

# ---------------------------------------------------------------- inputs (READ)
# 2019 SI exact (read: CODATA 2022 arXiv:2409.03787 Table XXXII; Pavese 1512.03668 restating Newell 2018)
C = 299792458                       # m/s exact
H = sp.Rational(662607015, 10**8) * sp.Integer(10)**-34   # J s exact
E = sp.Rational(1602176634, 10**9) * sp.Integer(10)**-19  # C exact
KB = sp.Rational(1380649, 10**6) * sp.Integer(10)**-23   # J/K exact
HBAR = H / (2*sp.pi)                # exact symbolic; numerically 1.054571817...e-34
# CODATA 2018 (read via restatement: Fayet 1906.05123 for alpha, mu0, eps0; 2022 paper says G identical)
G18, uG = 6.67430e-11, 0.00015e-11
ALPHA_INV_18 = 137.035999084; uAI18 = 0.000000021
MU0_18 = 1.25663706212e-6; EPS0_18 = 8.8541878128e-12
# CODATA 2022 (read at source: arXiv:2409.03787 Tables XXXII/XXXIII)
G22 = 6.67430e-11
ALPHA_INV_22 = 137.035999177; MU0_22 = 1.25663706127e-6; EPS0_22 = 8.8541878188e-12
ME_22 = 9.1093837139e-31; MP_22 = 1.67262192595e-27; U_22 = 1.66053906892e-27
A0_22 = 5.29177210544e-11; EH_22 = 4.3597447222060e-18; LP_22 = 1.616255e-35; uLP = 0.000018e-35
MP_ME_22 = 1836.152673426; uMPME22_rel = 1.7e-11
# CODATA 2018 values as the tree carries them (owner literals, read from the tree)
ME_18 = 9.1093837015e-31; MP_18 = 1.67262192369e-27; U_18 = 1.66053906660e-27
A0_18 = 5.29177210903e-11; EH_18 = 4.3597447222071e-18; LP_18 = 1.616255e-35
# IAU (read at source: Prsa et al. 1605.09788, Table 1 and Appendix)
GM_SUN_N = 1.3271244e20             # m^3 s^-2, exact nominal (IAU 2015 B3)
AU = 149597870700                   # m, exact (IAU 2012 B2)
G_2006 = 6.67428e-11; G_2014 = 6.67408e-11
# Gaia DR3 parallax of Proxima (value filled from the READ below; see report)
PLX_MAS, uPLX = 768.0665, 0.0499     # mas  (Gaia DR3 5853498713190525696)
# tree literals
T = dict(C=2.99792458e8, G=6.67430e-11, M_SUN_fol=1.98840e30, M_SUN_wall=1.98847e30,
         M_SUN_ph1=1.98892e30, LY_fol=9.4607304725808e15, LY_ph1=9.4607e15, LY_ach=9.461e15,
         LY_arr=9.4607304726e15, PROXIMA_LY=4.2465, LAMBDA=9.982529174194637,
         HBAR=1.054571817e-34, LP=1.616255e-35, EPS0=8.8541878128e-12, MU0=1.25663706212e-6,
         MP_arr=1.67262192e-27, MP_wf=1.67262192369e-27, ALPHA_INV=137.035999084,
         GEV_IN_J=1.602176634e-10, KB=1.380649e-23, U_KG=1.66053906660e-27,
         AU_wall=1.495978707e11, GN=9.80665, YR_ph1=3.15576e7, YR_transit=3.156e7,
         PC_arr=3.0856775815e16)

print("1. LIGHT YEAR = c x Julian year (365.25 x 86400 s), exact")
LY_exact = sp.Integer(C) * 36525 * 864           # 365.25*86400 = 31557600 = 36525*864
print("   LY =", LY_exact, "m  =", float(LY_exact))
chk("MUST foliation/nonstatic/ledger LY literal equals c x Julian year exactly",
    float(LY_exact) == T["LY_fol"], "9.4607304725808e15 is the exact integer 9460730472580800")
chk("arrival.py LY 9.4607304726e15 is the same rounded to 11 figures", abs(T["LY_arr"]/float(LY_exact)-1) < 5e-12)
chk("phase1.py LIGHT_YEAR 9.4607e15 is the same truncated to 5 figures (rel %.1e)" % abs(T["LY_ph1"]/float(LY_exact)-1), abs(T["LY_ph1"]/float(LY_exact)-1) < 5e-6)
chk("achievable.py :539 1 ly = 9.461e15 is rounded to 4 figures (rel %.1e)" % abs(T["LY_ach"]/float(LY_exact)-1), abs(T["LY_ach"]/float(LY_exact)-1) < 5e-5)
chk("Julian year 3.15576e7 s (phase1) exact", T["YR_ph1"] == 365.25*86400)
chk("transit.py 3.156e7 is the Julian year to 4 figures", abs(T["YR_transit"]/(365.25*86400)-1) < 1e-4)
PC_exact = sp.Integer(AU) * 648000 / sp.pi
chk("arrival.py PC = 3.0856775815e16 is 648000/pi au to 11 figures", abs(T["PC_arr"]/float(PC_exact)-1) < 2e-11)
chk("hbar = h/2pi = %.12e; tree literal 1.054571817e-34 is CODATA's printed TRUNCATION 1.054 571 817 ... (rel %.1e)" % (float(HBAR), float(HBAR)/T["HBAR"]-1), abs(float(HBAR)/T["HBAR"]-1) < 1e-9)
chk("GEV_IN_J = e x 1e9 exact", abs(float(E)*1e9/T["GEV_IN_J"]-1) < 1e-15)

print("\n2. THE SOLAR MASS: IAU 2015 B3 nominalises (GM)_sun, NOT M_sun; M_sun = (GM)^N / G")
for name, g in (("CODATA 2006", G_2006), ("CODATA 2014", G_2014), ("CODATA 2018/2022", G18)):
    print("   M_sun with %s G = %.6e kg" % (name, GM_SUN_N/g))
M18 = GM_SUN_N / G18
chk("foliation M_SUN = 1.98840e30 equals (GM)^N/G_2018 = %.5e to 5 figures" % M18, abs(T["M_SUN_fol"]/M18-1) < 5e-6)
chk("wall.py 1.98847e30 equals (GM)^N/G_2014 (Prsa 2016 Appendix figure 1.988475e30)", abs(T["M_SUN_wall"]/(GM_SUN_N/G_2014)-1) < 5e-6)
chk("phase1 SOLAR_MASS 1.98892e30 matches NO IAU/CODATA pairing (rel to M18 = %.2e)" % (T["M_SUN_ph1"]/M18-1), abs(T["M_SUN_ph1"]/M18-1) > 1e-4)
print("   -> 1.98892e30 is the old textbook value (pre-2010 G, e.g. Allen); a DISCREPANCY inside the tree, 2.6e-4 relative")
print("   The propagated uncertainty of M_sun from u_r(G)=2.2e-5 is +-%.1e kg" % (M18*2.2e-5))

print("\n3. PROXIMA: parallax -> distance")
d_pc = 1000.0 / PLX_MAS
d_ly = d_pc * float(PC_exact) / float(LY_exact)
print("   plx = %.4f +- %.4f mas -> d = %.6f pc = %.6f ly" % (PLX_MAS, uPLX, d_pc, d_ly))
chk("MUST tree's PROXIMA_LY = 4.2465 reproduced to 5 figures", abs(T["PROXIMA_LY"]/d_ly-1) < 5e-5, "computed %.5f" % d_ly)
print("   relative uncertainty of the distance: %.1e (parallax), zero-point bias ~ -17..-40 uas is %.1e" % (uPLX/PLX_MAS, 40e-3/PLX_MAS))
span = T["PROXIMA_LY"] * float(LY_exact)
chk("proxima_span_m() = 4.017499195e16 m", abs(span/4.017499195e16-1) < 1e-9)

print("\n4. PLANCK LENGTH sqrt(hbar G / c^3)")
lp = math.sqrt(T["HBAR"]*G18/C**3)
print("   l_P = %.9e m ; CODATA 1.616255(18)e-35 ; rel diff %.2e ; u_r(l_P) = 1.1e-5" % (lp, lp/LP_22-1))
chk("MUST derived l_P within CODATA's own uncertainty", abs(lp/LP_22-1) < 1.1e-5)
chk("tolman's claim 'gap below 1e-4 and above 1e-9'", 1e-9 < abs(lp/LP_22-1) < 1e-4)

print("\n5. DERIVED FIGURES, 2018 vs 2022, and G at +-1 sigma")
def figures(G, hbar=T["HBAR"], eps0=EPS0_18, mu0=MU0_18, mp=MP_18, u=U_18, alpha_inv=ALPHA_INV_18):
    f = {}
    f["EXCHANGE_RATE kg/m"] = C**2/(G*T["LAMBDA"])
    f["Proxima demand kg"] = f["EXCHANGE_RATE kg/m"]*span
    f["gauge bill Msun (R c^2/G/M_sun, dGamma=1)"] = span*C**2/G/T["M_SUN_fol"]
    f["l_P m"] = math.sqrt(hbar*G/C**3)
    f["T_COEFF pi c^4/4G"] = math.pi*C**4/(4*G)
    f["reduced Planck mass GeV"] = math.sqrt(hbar*C/(8*math.pi*G))*C**2/T["GEV_IN_J"]
    f["X per C^2 = 1/(8 pi eps0 c^2)"] = 1/(8*math.pi*eps0*C**2)
    f["baryons_in(100 kg)"] = 100/mp
    f["phase1 one Msun buys m"] = T["M_SUN_ph1"]/f["EXCHANGE_RATE kg/m"]
    f["alpha^-1"] = alpha_inv
    return f
base = figures(G18)
alt = {"CODATA 2022": figures(G22, eps0=EPS0_22, mu0=MU0_22, mp=MP_22, u=U_22, alpha_inv=ALPHA_INV_22),
       "G +1 sigma": figures(G18+uG), "G -1 sigma": figures(G18-uG)}
print("   %-42s %14s" % ("figure", "CODATA 2018") + "".join(" %12s" % k for k in alt))
for k, v in base.items():
    print("   %-42s %14.9e" % (k, v) + "".join(" %+12.2e" % (alt[a][k]/v-1) for a in alt))
chk("MUST ledger EXCHANGE_RATE 1.348948e26 reproduced to 7 figures", round(base["EXCHANGE_RATE kg/m"]/1e26, 6) == 1.348948)
chk("MUST ledger Proxima demand 5.4194e42 kg reproduced", round(base["Proxima demand kg"]/1e42, 4) == 5.4194)
chk("MUST gauge bill 2.720744289e13 Msun reproduced to 1e-9", abs(base["gauge bill Msun (R c^2/G/M_sun, dGamma=1)"]/2.720744289e13-1) < 1e-9)
chk("seatindex T_COEFF 9.50536e43 within its 1e39 tolerance", abs(base["T_COEFF pi c^4/4G"]-9.50536e43) < 1e39)
chk("drivensource X per C^2 = 1/(8 pi eps0 c^2) = 5.0e-08 kg m to 1e-9 (owner pin :541)", abs(base["X per C^2 = 1/(8 pi eps0 c^2)"]/5.0e-8-1) < 1e-9, "value %.10e; exactly 5e-8 would need eps0 = 1/(4 pi 1e-7 c^2), the pre-2019 exact value" % base["X per C^2 = 1/(8 pi eps0 c^2)"])
chk("warpfolder baryons_in(100) = 5.979e28", abs(base["baryons_in(100 kg)"]/5.979e28-1) < 5e-4)
chk("phase1 'one solar mass buys 1.4742e4 m' at rtol 1e-3 -- with phase1's OWN 1.98892e30", abs(base["phase1 one Msun buys m"]/1.4742e4-1) < 1e-3)
m18 = T["M_SUN_fol"]/base["EXCHANGE_RATE kg/m"]
print("   with foliation's IAU-derived M_sun the same figure is %.5e m (rel %.2e) -- outside phase1's own 1e-3 tolerance? %s" % (m18, m18/1.4742e4-1, abs(m18/1.4742e4-1) > 1e-3))
print("   largest 2018->2022 relative move among figures the tree pins: %.2e (alpha, eps0, m_p family); G-driven figures move 0" % max(abs(alt["CODATA 2022"][k]/v-1) for k, v in base.items()))
print("   G's own +-1 sigma moves every G-bearing figure by %.1e; the tree's coarsest pins are at 1e-4..1e-3 and its margins at >= 10 orders" % (uG/G18))

print("\n5b. THE TREE'S 2018 LITERALS CROSS-CHECKED AGAINST THE 2022 PAPER'S TABLE XXXVIII")
print("   D_r = (C(2022)-C(2018))/u(2018), u(2018) = u_r(2022)*C(2022)/ratio  -- must match the table's printed D_r")
rows = [("alpha^-1", ALPHA_INV_18, ALPHA_INV_22, 1.6e-10, 0.97, +4.5),   # table gives alpha D_r=-4.5 -> alpha^-1 +4.5
        ("mu_0", MU0_18, MU0_22, 1.6e-10, 0.97, -4.5), ("eps_0", EPS0_18, EPS0_22, 1.6e-10, 0.97, +4.5),
        ("a_0", A0_18, A0_22, 1.6e-10, 0.97, -4.5), ("m_e", ME_18, ME_22, 3.1e-10, 0.97, +4.5),
        ("u (m_u)", U_18, U_22, 3.1e-10, 0.97, +4.6), ("E_h", EH_18, EH_22, 1.1e-12, 1.74, -0.3)]
for name, v18, v22, ur22, ratio, Dr in rows:
    u18 = ur22 * v22 * ratio          # ratio = u(2018)/u(2022), the table's column
    d = (v22 - v18) / u18
    chk("%-8s tree 2018 literal vs 2022: D_r computed %+.2f, table %+.1f" % (name, d, Dr), abs(d - Dr) < 0.35)
print("   -> every 2018 literal the tree types is the CODATA 2018 value (the table's shift reproduces it), read via the 2022 paper")
print("\n6. INTERNAL DISCREPANCIES (recorded, not repaired)")
print("   phase1.SOLAR_MASS / foliation.M_SUN - 1 = %+.3e" % (T["M_SUN_ph1"]/T["M_SUN_fol"]-1))
print("   wall.py 1.98847e30 / foliation 1.98840e30 - 1 = %+.3e (CODATA 2014 vs 2018 G under the same nominal GM)" % (T["M_SUN_wall"]/T["M_SUN_fol"]-1))
print("   arrival/stock m_p 1.67262192e-27 / CODATA 2018 1.67262192369e-27 - 1 = %+.2e (truncation)" % (T["MP_arr"]/MP_18-1))
print("   CODATA 2022 m_p / 2018 - 1 = %+.2e ; u / u - 1 = %+.2e ; alpha^-1 shift = %+.2e (%.1f sigma_2018)" % (MP_22/MP_18-1, U_22/U_18-1, ALPHA_INV_22/ALPHA_INV_18-1, (ALPHA_INV_22-ALPHA_INV_18)/uAI18))
print("   'IAU nominal' M_sun: IAU B3 nominalises (GM)^N; the kg figure depends on which G -- the ledger's annotation is loose")
print("   'Gaia DR3 parallax' 4.2465 ly: reproduced; carries 6.5e-5 relative uncertainty the tree does not record")

print("\nRESULT:", "ALL MUST CHECKS PASS" if not fails else "FAILURES: %s" % fails)
sys.exit(1 if fails else 0)
