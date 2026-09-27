#!/usr/bin/env python3
"""DOCKET 67 audit -- nuclear-saturation-density (address.py:430, 191-196, 943-949).

Read-only: imports address.py from research/warp-drive without writing bytecode.
Checks
 (1) RHO_NUCLEAR = 2.676e17 kg/m^3 is n0 * m against n0 = 0.16 fm^-3 (m_p, <m_N>, m_N - B/A);
 (2) sympy: eps is linear in rho, so EPS_NUCLEAR_OVER_DET scales exactly as n0;
 (3) scan of n0 over the band quoted in later literature (values NOT READ at source:
     0.145-0.171 fm^-3) -> the '398 / 114 times eps_det' and 'two orders over threshold';
 (4) break-even n0 at which nuclear matter would sit AT threshold;
 (5) the coarse-grained-mean hypothesis (address.py:297-303) tested on real light nuclei with
     CODATA rms charge radii (proton, deuteron, alpha; from the installed scipy table),
     uniform-sphere equivalent R = sqrt(5/3) r_ch (charge radius > point-matter radius, so
     density is UNDER-estimated: conservative for the 'over threshold' claim);
 (6) internal consistency: n0^(-1/3) vs 'nucleons are 1.8 fm apart' (address.py:299);
     the tree's other nuclear constant 2.3e17 (warpdrive.py:148, emwarp.py:225,
     drivespec.py:39, mouth.py:103) against address.py's 2.676e17.
"""
import math, os, sys
sys.dont_write_bytecode = True
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, TREE)
import sympy as sp
import address as A
from scipy.constants import physical_constants as pc, m_p, m_n, e as QE, c as C

fails = []
def chk(label, ok):
    print(("PASS " if ok else "FAIL ") + label)
    if not ok: fails.append(label)

FM3 = 1e45  # fm^-3 -> m^-3
MEV_KG = 1e6 * QE / C**2

print("== (1) arithmetic of RHO_NUCLEAR")
r_p = 0.16 * FM3 * m_p
r_N = 0.16 * FM3 * 0.5 * (m_p + m_n)
r_B = 0.16 * FM3 * (0.5 * (m_p + m_n) - 16.0 * MEV_KG)
for lab, r in (("n0*m_p", r_p), ("n0*<m_N>", r_N), ("n0*(<m_N>-16 MeV)", r_B)):
    print("  %-22s %.5e kg/m^3   tree/this = %.5f" % (lab, r, A.RHO_NUCLEAR / r))
chk("tree 2.676e17 = 0.16 fm^-3 * m_p to 4 digits", abs(A.RHO_NUCLEAR / r_p - 1) < 1e-4)
chk("mass choice (m_p, <m_N>, binding) moves rho by < 2%",
    max(abs(A.RHO_NUCLEAR / r - 1) for r in (r_p, r_N, r_B)) < 0.02)

print("== (2) sympy: ratio proportional to n0")
n0, m, f, Vmin, c, edet = sp.symbols("n0 m f V_min c eps_det", positive=True)
eps = -(n0 * m * f) * c**2 / (8 * Vmin)          # address.py:674, rho = n0 m
ratio = sp.Abs(eps) / edet
chk("d ln(ratio)/d ln(n0) == 1 exactly", sp.simplify(n0 * sp.diff(ratio, n0) / ratio) == 1)
chk("address.py eps_from_matter linear numerically",
    abs(A.eps_from_matter(2 * A.RHO_NUCLEAR, 0.06) / A.eps_from_matter(A.RHO_NUCLEAR, 0.06) - 2) < 1e-12)

print("== (3) n0 scan (values of the band NOT READ at source)")
R0 = dict(A.EPS_NUCLEAR_OVER_DET)
print("  tree:", {h: round(v, 3) for h, v in R0.items()})
band = [0.137, 0.145, 0.148, 0.150, 0.155, 0.157, 0.160, 0.164, 0.171]
rows = {}
for n in band:
    rho = n * FM3 * m_p
    rr = {h: abs(A.eps_from_matter(rho, A.higgs_fraction(A.S_SCAN[1][1], h))) / A.eps_det_stationary(h)
          for h in A.HYPOTHESES}
    rows[n] = rr
    print("  n0=%.3f  rho=%.4e  H1 %7.2f  H2 %7.2f" % (n, rho, rr["H1"], rr["H2"]))
chk("every n0 in band keeps H1 ratio > 100 ('two orders')", all(r["H1"] > 100 for r in rows.values()))
# FINDING (not a fail): H2 crosses a literal 100 inside the band (n0 < 0.1401) and at the
# tree's own 2.3e17; on a log reading it stays 'two orders' (log10 >= 1.99).
chk("H2 ratio < 100 somewhere in band (literal 'two orders' fails for H2 at low n0) -- FINDING",
    any(r["H2"] < 100 for r in rows.values()))
chk("H2 log10(ratio) >= 1.99 over whole band", all(math.log10(r["H2"]) >= 1.99 for r in rows.values()))
chk("every n0 in band keeps both ratios > 1 (over threshold)", all(min(r.values()) > 1 for r in rows.values()))

print("== (4) break-even n0 (ratio = 1)")
be = {h: 0.16 / R0[h] for h in R0}
print("  H1 %.3e fm^-3   H2 %.3e fm^-3" % (be["H1"], be["H2"]))
chk("break-even is >100x below any quoted n0", max(be.values()) < 0.145 / 100)
# 'two orders over threshold' literal break-even (ratio = 100)
be100 = {h: 100 * 0.16 / R0[h] for h in R0}
print("  ratio=100 needs n0 >= H1 %.4f  H2 %.4f fm^-3" % (be100["H1"], be100["H2"]))

print("== (5) coarse-grained mean over REAL nuclei (CODATA rms charge radii, scipy table)")
nuc = (("proton", 1, pc["proton rms charge radius"][0]),
       ("deuteron", 2, pc["deuteron rms charge radius"][0]),
       ("alpha", 4, pc["alpha particle rms charge radius"][0]),
       ("208Pb [r_ch=5.5012 fm NAMED-NOT-READ]", 208, 5.5012e-15))
mean = {}
for lab, Anum, rch in nuc:
    R = math.sqrt(5.0 / 3.0) * rch
    n = Anum / (4.0 / 3.0 * math.pi * (R * 1e15) ** 3)
    rho = n * FM3 * m_p
    rr = {h: abs(A.eps_from_matter(rho, A.higgs_fraction(A.S_SCAN[1][1], h))) / A.eps_det_stationary(h)
          for h in A.HYPOTHESES}
    mean[lab] = (n, rr)
    print("  %-38s r_ch=%.4f fm R=%.3f fm n=%.4f fm^-3 (%.2f n0)  H1 %7.2f  H2 %7.2f"
          % (lab, rch * 1e15, R * 1e15, n, n / 0.16, rr["H1"], rr["H2"]))
chk("deuteron mean density is far BELOW n0 (<0.2 n0)", mean["deuteron"][0] < 0.2 * 0.16)
chk("deuteron is still over threshold in both hypotheses", min(mean["deuteron"][1].values()) > 1)
chk("deuteron is NOT two orders over in either hypothesis", max(mean["deuteron"][1].values()) < 100)
chk("every listed nucleus is over threshold in both hypotheses",
    all(min(v[1].values()) > 1 for v in mean.values()))

print("== (6) internal consistency")
d = 0.16 ** (-1.0 / 3.0)
print("  n0^(-1/3) = %.4f fm (address.py:299 says 1.8 fm)" % d)
chk("spacing consistent with '1.8 fm'", abs(d - 1.8) < 0.05)
alt = 2.3e17
print("  other tree constant 2.3e17 -> n0 = %.4f fm^-3; address/other = %.4f" % (alt / (FM3 * m_p), A.RHO_NUCLEAR / alt))
print("  EPS_NUCLEAR_OVER_DET at 2.3e17: H1 %.2f  H2 %.2f"
      % (R0["H1"] * alt / A.RHO_NUCLEAR, R0["H2"] * alt / A.RHO_NUCLEAR))
chk("two tree constants disagree by >10% (discrepancy recorded, not repaired)", A.RHO_NUCLEAR / alt > 1.10)

print()
print("RESULT: %s (%d fails)" % ("ALL CHECKS PASS" if not fails else "FAILURES: " + "; ".join(fails), len(fails)))
sys.exit(1 if fails else 0)
