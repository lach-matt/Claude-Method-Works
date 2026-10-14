#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 'withdrawn-pin-125.20-and-orchestrator-125.25'.
Reads research/warp-drive (import only, never writes).  Exit 0 iff every check passes."""
import glob, hashlib, math, os, sys
from fractions import Fraction
import sympy as sp

D = os.path.dirname(os.path.abspath(__file__))
PKG_OLD = os.path.join(D, "..", "pkg", "old")
PKG_NEW = "/usr/local/lib/python3.11/dist-packages/particle/data"
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
fails = []
def chk(name, ok, detail=""):
    print("  [%s] %s %s" % ("ok" if ok else "FAIL", name, detail))
    if not ok: fails.append(name)

# ---------------------------------------------------------------- A. PDG averages
def avg(inputs):
    w = [1 / e**2 for _, e in inputs]
    m = sum(wi * v for wi, (v, _) in zip(w, inputs)) / sum(w)
    err = 1 / math.sqrt(sum(w))
    chi2 = sum(((v - m) / e)**2 for v, e in inputs)
    n = len(inputs)
    S = max(1.0, math.sqrt(chi2 / (n - 1)))
    cl = math.exp(-chi2 / 2) if n - 1 == 2 else float("nan")   # chi2 survival, 2 dof
    return m, err, chi2, S, err * S, cl
q = lambda a, b: math.hypot(a, b)
print("A. PDG averages re-derived from the listings' own inputs (READ at pdg.lbl.gov)")
# RPP 2024 (Navas et al., PRD 110 030001), listing p.1/p.3
rpp24 = [(125.10, 0.11), (125.46, 0.16), (125.09, q(0.21, 0.11))]
m, e, c2, S, es, cl = avg(rpp24)
print("   RPP2024: mean %.4f  err %.4f  chi2 %.2f  S %.3f  scaled %.4f  CL %.3f" % (m, e, c2, S, es, cl))
chk("RPP2024 mean rounds to 125.20", round(m, 2) == 125.20)
chk("RPP2024 scaled error rounds to 0.11, S to 1.4", round(es, 2) == 0.11 and round(S, 1) == 1.4)
chk("RPP2024 chi2 rounds to 3.7, CL ~0.159", round(c2, 1) == 3.7 and abs(cl - 0.159) < 0.003)
# RPP 2022 (Workman et al., PTEP 2022 083C01), listing p.1/p.2
rpp22 = [(125.46, 0.16), (124.86, 0.27), (125.09, q(0.21, 0.11))]
m2, e2, c22, S2, es2, cl2 = avg(rpp22)
print("   RPP2022: mean %.4f  err %.4f  chi2 %.2f  S %.3f  scaled %.4f  CL %.3f" % (m2, e2, c22, S2, es2, cl2))
chk("RPP2022 mean rounds to 125.25", round(m2, 2) == 125.25)
chk("RPP2022 scaled error rounds to 0.17, S to 1.5", round(es2, 2) == 0.17 and round(S2, 1) == 1.5)
chk("RPP2022 chi2 rounds to 4.3, CL ~0.119", round(c22, 1) == 4.3 and abs(cl2 - 0.119) < 0.003)

# ---------------------------------------------------------------- B. machine-readable PDG files
print("B. scikit-hep 'particle' PDG mass/width files, H row (pdgid 25)")
rows = {}
for f in sorted(glob.glob(PKG_OLD + "/*/particle/data/mass_width_20*.mcd")) + \
         sorted(glob.glob(PKG_NEW + "/mass_width_20*.txt")):
    yr = os.path.basename(f)[11:15]
    for line in open(f, encoding="latin-1"):
        if line.startswith("*"): continue
        t = line.split()
        if t and t[0] == "25":
            rows[yr] = (float(t[1]), line.rstrip(), hashlib.md5(open(f, "rb").read()).hexdigest())
for yr in sorted(rows):
    print("   %s  m_H = %.2f  md5 %s" % (yr, rows[yr][0], rows[yr][2]))
chk("2021, 2022, 2023 editions carry 125.25", all(abs(rows[y][0] - 125.25) < 1e-9 for y in ("2021", "2022", "2023")))
chk("2024, 2025 editions carry 125.20", all(abs(rows[y][0] - 125.20) < 1e-9 for y in ("2024", "2025")))
chk("2026 edition carries 125.13", abs(rows["2026"][0] - 125.13) < 1e-9)

# ---------------------------------------------------------------- C. the tree's figures
print("C. the tree's m_h-dependent figures (constants exact-SI; G_F, M_earth as the tree carries them)")
HBAR = 1.054571817e-34; C = 299792458.0; EV = 1.602176634e-19
GEV = EV * 1e9; HBARC_GEVM = HBAR * C / GEV            # GeV m
GF = 1.1663788e-5; MEARTH = 5.9722e24; RP = 0.8414e-15
lam = lambda m: HBARC_GEVM / m
efold = lambda m: math.sqrt(2) * HBAR / (m * GEV)
v = (math.sqrt(2) * GF) ** -0.5
GEV4 = GEV**4 / (HBAR * C)**3
rho = lambda m: m * m * v * v / 8 * GEV4                 # |V_min| = lambda v^4/4 = m^2 v^2 / 8
print("   v = %.6f GeV" % v)
for mh in (125.25, 125.20, 125.13):
    print("   m_h %.2f: lambda %.6e m  e-fold %.6e s  |V_min| %.6e J/m^3  M_earth/m^3 %.2f  (1/c)/e-fold %.5e  lambda/r_p %.5f"
          % (mh, lam(mh), efold(mh), rho(mh), rho(mh) / C**2 / MEARTH, (1 / C) / efold(mh), lam(mh) / RP))
chk("lambda_h(125.20) = 1.576094e-18 m (excite.py:1382-1383)", abs(lam(125.20) / 1.576094e-18 - 1) < 1e-6)
chk("spinodal e-fold(125.20) = 7.434922e-27 s (excite.py:1656-1657)", abs(efold(125.20) / 7.434922e-27 - 1) < 1e-6)
chk("lambda_h(125.25) matches 1.5755e-18 to 1e-4 (excite.py:1693-1694)", abs(lam(125.25) / 1.5755e-18 - 1) < 1e-4)
chk("lambda_h(125.20) does NOT match 1.5755e-18 at 1e-4 (the check discriminates)", abs(lam(125.20) / 1.5755e-18 - 1) > 1e-4,
    "(rel %.2e)" % (lam(125.20) / 1.5755e-18 - 1))
# interval of m_h each printed orchestrator figure admits, from its printed precision
def interval_from_lam(x, half):  return (HBARC_GEVM / (x + half), HBARC_GEVM / (x - half))
def interval_from_rho(x, half):  return tuple(math.sqrt(8 * y / (v * v * GEV4)) for y in (x - half, x + half))
I1 = interval_from_lam(1.5755e-18, 0.00005e-18)
I2 = interval_from_rho(2.4789e45, 0.00005e45)
I3 = interval_from_rho(4618 * C**2 * MEARTH, 0.5 * C**2 * MEARTH)
lo, hi = max(I1[0], I2[0], I3[0]), min(I1[1], I2[1], I3[1])
print("   m_h admitted: by 1.5755e-18 m [%.4f, %.4f]; by 2.4789e45 [%.4f, %.4f]; by 4618 [%.4f, %.4f]; joint [%.4f, %.4f]"
      % (I1 + I2 + I3 + (lo, hi)))
chk("the three orchestrator figures jointly admit 125.25", lo <= 125.25 <= hi)
chk("they jointly exclude 125.20 and 125.13", not (lo <= 125.20 <= hi) and not (lo <= 125.13 <= hi))
chk("of the PDG editions 2018-2026 (125.18, 125.10, 125.25, 125.20, 125.13) only 125.25 lies in the joint interval",
    [x for x in (125.18, 125.10, 125.25, 125.20, 125.13) if lo <= x <= hi] == [125.25])

# ---------------------------------------------------------------- D. exact power laws (sympy)
print("D. power laws, exact")
m, m0, hb, c, g = sp.symbols("m m0 hbar c v", positive=True)
for name, f, k in (("lambda_h", hb * c / m, -1), ("e-fold", sp.sqrt(2) * hb / m, -1), ("|V_min|", m**2 * g**2 / 8, 2)):
    chk("%s scales as m_h^%d" % (name, k), sp.simplify(f.subs(m, m * sp.Symbol("r", positive=True)) / f - sp.Symbol("r", positive=True)**k) == 0)
r1 = Fraction(12513, 12520); r2 = Fraction(12520, 12525)
print("   125.20->125.13: %.4e relative; 125.25->125.20: %.4e relative" % (float(r1 - 1), float(r2 - 1)))
print("   moves in sigma: 125.25->125.20 = %.2f of 0.17; 125.20->125.13 = %.2f of 0.11" % (0.05 / 0.17, 0.07 / 0.11))

# ---------------------------------------------------------------- E. the tree's own use of the pin
print("E. the tree's claim '125.20 is never used for a live figure' (excite.py:293-294), tested")
sys.path.insert(0, TREE)
cwd = os.getcwd(); os.chdir(TREE)
import excite, endpoint, address, higgs
os.chdir(cwd)
chk("excite.LAMBDA_H_PIN_M reproduced", abs(excite.LAMBDA_H_PIN_M / lam(125.20) - 1) < 1e-9)
chk("higgs.M_HIGGS is the READ 125.13", higgs.M_HIGGS == 125.13)
for L in (1e-17, 1e-15):
    a = excite.cosine_response_error(excite.LAMBDA_H_PIN_M / L)     # what excite.py:1211 prints
    b = excite.cosine_response_error(excite.LAMBDA_H_READ_M / L)    # what the READ m_h gives
    u = address.ultralocality_error(L)                              # printed beside it: READ m_h
    print("   L=%.0e: printed 'exact error' (pin) %.6e ; same at READ %.6e ; address column (READ) %.6e ; pin/READ-1 = %.3e"
          % (L, a, b, u, a / b - 1))
src = open(os.path.join(TREE, "excite.py")).read().splitlines()
chk("excite.py:1211 feeds the withdrawn pin into a printed report figure (D16 table)",
    "LAMBDA_H_PIN_M" in src[1210] and "cosine_response_error" in src[1210])
ratio_read = (1 / C) / endpoint.spinodal_efold_s()
ratio_pin = (1 / C) / endpoint.spinodal_efold_s(125.20)
print("   endpoint.py:578 text '4.486e17'; at READ %.4e (-> 4.484e17), at pin %.4e (-> 4.486e17)" % (ratio_read, ratio_pin))
chk("'4.486e17' is the figure at the withdrawn pin, not at the READ m_h", f"{ratio_pin:.3e}" == "4.486e+17" and f"{ratio_read:.3e}" != "4.486e+17")
chk("endpoint.py:989 still passes it because its tolerance 1e-3 exceeds the 5.6e-4 shift", abs(ratio_read / 4.486e17 - 1) < 1e-3)
chk("address.py:163 docstring '1.5761e-18 m' is lambda at the pin, not at the READ m_h",
    f"{lam(125.20):.4e}" == "1.5761e-18" and f"{address.yukawa_range():.4e}" != "1.5761e-18")

# ---------------------------------------------------------------- F. later datum, sensitivity only
print("F. sensitivity (NOT a PDG number): RPP2026 inputs with CMS 2020 gg 125.78+-0.26 replaced by CMS 2026 gg 125.13+-0.15 (arXiv:2607.28396)")
rpp26 = [(125.04, 0.12), (125.10, 0.11), (125.78, 0.26), (125.09, q(0.21, 0.11))]
alt = [(125.04, 0.12), (125.10, 0.11), (125.13, 0.15), (125.09, q(0.21, 0.11))]
for lab, ins in (("RPP2026 as listed", rpp26), ("with CMS 2026 gg", alt)):
    w = [1 / e**2 for _, e in ins]; mm = sum(a * b for a, (b, _) in zip(w, ins)) / sum(w)
    c2 = sum(((b - mm) / e)**2 for b, e in ins); S = max(1, math.sqrt(c2 / 3))
    print("   %-18s mean %.4f  err %.4f  chi2 %.2f  S %.2f" % (lab, mm, S / math.sqrt(sum(w)), c2, S))
    if lab.startswith("with"):
        chk("the sensitivity average stays within 0.05 GeV of 125.13 and far outside the orchestrator interval",
            abs(mm - 125.13) < 0.05 and not (lo <= mm <= hi))

print()
print("ALL CHECKS PASS" if not fails else "FAILED: %s" % fails)
sys.exit(1 if fails else 0)
