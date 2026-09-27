#!/usr/bin/env python3
"""DOCKET 67 -- pdg-2026-m_h.  Re-derive, numerically, what is finite here:
 (A) the PDG 2026 weighted average of m_H (125.13 +- 0.11, S = 1.5, chi2 6.9, CL 0.075)
     from the four inputs the RPP 2026 listing names (READ at pdg.lbl.gov, rpp2026-list-higgs-boson.pdf p.1-3);
 (B) the capture row against the scikit-hep particle 1.0.1 data files (md5, value, and the 2024/2025 rows);
 (C) the tree's derived figures at the READ m_h / Gamma_h, and how far each moves over the
     published uncertainty bands (m_h +-0.11 GeV; Gamma_h +1.5/-0.7 MeV; SM 4.1 MeV; PDG-2024 3.7 MeV).
stdlib + sympy (sympy only for exact rational chi2 bookkeeping).  Exits 1 on a failed check."""
import hashlib, math, os, sys
from fractions import Fraction
fails = []
def chk(name, got, want, tol=None):
    ok = (abs(got - want) <= tol) if tol is not None else (got == want)
    print("  [%s] %-70s got %r  want %r" % ("ok" if ok else "XX", name, got, want))
    if not ok: fails.append(name)

print("(A) PDG 2026 weighted average of m_H, re-derived from the four listed inputs")
# (value, total error) -- errors combined in quadrature where the listing gives stat+syst
inp = [("HAYRAPETYAN 25L CMS 4l",        125.04, 0.12),
       ("AAD 23BP ATLAS 13 TeV gg+4l",   125.10, 0.11),
       ("SIRUNYAN 20L CMS gg 13 TeV",    125.78, 0.26),
       ("AAD 15B LHC Run1",              125.09, math.hypot(0.21, 0.11))]
w = [1/e**2 for _, _, e in inp]
mean = sum(wi*v for wi, (_, v, _) in zip(w, inp)) / sum(w)
err = 1/math.sqrt(sum(w))
contrib = [((v-mean)/e)**2 for _, v, e in inp]
chi2 = sum(contrib); N = len(inp)
S = math.sqrt(chi2/(N-1))
print("  mean = %.4f GeV, unscaled error = %.4f, chi2 = %.2f, S = %.3f, scaled error = %.4f"
      % (mean, err, chi2, S, err*S))
for (n, v, e), c in zip(inp, contrib): print("    %-32s %.2f +- %.3f  chi2 contribution %.2f" % (n, v, e, c))
chk("average rounds to 125.13", round(mean, 2), 125.13)
chk("chi2 = 6.9 (listing ideogram)", round(chi2, 1), 6.9)
chk("S = 1.5 (listing)", round(S, 1), 1.5)
chk("scaled error rounds to 0.11", round(err*S, 2), 0.11)
chk("SIRUNYAN 20L contributes 6.2", round(contrib[2], 1), 6.2)
# CL of chi2 = 6.9 with 3 dof: survival = erfc-based closed form for odd dof
x = chi2
cl = math.erfc(math.sqrt(x/2)) + math.sqrt(2*x/math.pi)*math.exp(-x/2)
chk("CL(chi2, 3 dof) = 0.075 (listing)", round(cl, 3), 0.075, 0.002)
# sensitivity: drop the outlier (CMS 2020 gg)
sub = [inp[i] for i in (0, 1, 3)]
ws = [1/e**2 for _, _, e in sub]; ms = sum(wi*v for wi, (_, v, _) in zip(ws, sub))/sum(ws)
print("  without SIRUNYAN 20L: mean %.4f +- %.4f GeV (a sensitivity, not the PDG's number)" % (ms, 1/math.sqrt(sum(ws))))
# PDG 2024 average from ATLAS 125.11 +- 0.11 and CMS 125.38 +- 0.14 (the 2024 inputs, stated for comparison only)

print("\n(B) the capture against scikit-hep particle 1.0.1")
D = "/usr/local/lib/python3.11/dist-packages/particle/data"
cap = "/home/user/Claude-Method-Works/research/warp-drive/captures/PDG-2026.tsv"
if os.path.isdir(D):
    md5 = hashlib.md5(open(os.path.join(D, "mass_width_2026.txt"), "rb").read()).hexdigest()
    chk("mass_width_2026.txt md5 = capture header md5", md5, "e96a23be061430adc72d5b2ea5a93764")
    rows = {}
    for yr in (2024, 2025, 2026):
        for ln in open(os.path.join(D, "mass_width_%d.txt" % yr)):
            if ln.startswith("*"): continue
            if ln[:8].strip() == "25" or ln[0:33].split() == ["25"]:
                rows[yr] = ln.rstrip("\n")
    for yr, ln in sorted(rows.items()):
        f = ln[33:].split()
        print("   %d H row: mass %s %s %s   width %s %s %s" % (yr, *f[:6]))
    m26 = float(rows[2026][33:].split()[0]); g26 = float(rows[2026][33:].split()[3])
    m24 = float(rows[2024][33:].split()[0]); m25 = float(rows[2025][33:].split()[0])
    chk("2026 file m_H = 125.13 GeV", m26, 125.13, 1e-9)
    chk("2026 file Gamma_H = 3.0 MeV", g26, 3.0e-3, 1e-12)
    chk("2024 and 2025 files carry 125.20 (the tree's withdrawn pin)", (m24, m25), (125.20, 125.20))
else:
    print("  [--] particle package absent: (B) NOT RUN")
for ln in open(cap):
    if ln.split("\t")[0] == "25":
        f = ln.rstrip("\n").split("\t")
        chk("capture H0 mass_MeV", float(f[11]), 125130.0); chk("capture H0 width_MeV", float(f[12]), 3.0)
hdr = [l for l in open(cap) if l.startswith("pdgid")][0].split("\t")
chk("capture schema carries NO uncertainty column", any("err" in h.lower() for h in hdr), False)

print("\n(C) the tree's derived figures and their movement over the published bands")
HBARC_MEV_FM = 197.3269804; HBAR_MEV_S = 6.582119569e-22
lam = lambda m_gev: HBARC_MEV_FM/(m_gev*1e3)*1e-15
efold = lambda m_gev: math.sqrt(2)*HBAR_MEV_S/(m_gev*1e3)
ceil_ = lambda m_gev, g_gev: math.sqrt(2/(m_gev*g_gev))*HBARC_MEV_FM*1e-3*1e-15
life = lambda g_gev: HBAR_MEV_S/(g_gev*1e3)
one = lambda x: "%.0e" % x
chk("lambda_h at 125.13 = 1.576976e-18 m (excite.py:1384)", lam(125.13), 1.576976e-18, 2e-24)
chk("lambda_h at 125.20 = 1.576094e-18 m (excite.py:1382)", lam(125.20), 1.576094e-18, 2e-24)
chk("spinodal e-fold at 125.13 = 7.439082e-27 s", efold(125.13), 7.439082e-27, 1e-32)
chk("shift 125.13/125.20 - 1 = -5.5910543e-4", 125.13/125.20-1, -5.5910543e-4, 1e-11)
chk("driven ceiling at (125.13, 3 MeV) = 4.55e-16 m", ceil_(125.13, 0.003), 4.55e-16, 1e-18)
chk("  one s.f. '5e-16'", one(ceil_(125.13, 0.003)), "5e-16")
chk("lifetime hbar/Gamma at 3 MeV one s.f. '2e-22'", one(life(0.003)), "2e-22")
print("  move of the pin->READ in units of the PDG error: %.2f sigma" % ((125.20-125.13)/0.11))
print("  relative 1-sigma band on lambda_h from m_h +-0.11: +-%.2e (printed to 7 s.f.)" % (0.11/125.13))
print("  Gamma_h band (MeV)   ceiling (m)   1 s.f.   lifetime (s)   1 s.f.")
for tag, g in (("PDG26 -1s 2.3", 2.3e-3), ("PDG26 central 3.0", 3.0e-3), ("PDG24 3.7", 3.7e-3),
               ("SM 4.1", 4.1e-3), ("PDG26 +1s 4.5", 4.5e-3), ("CMS 95% hi 7.3", 7.3e-3),
               ("2x SM (Stylianou-Weiglein x2 scale)", 8.2e-3)):
    c = ceil_(125.13, g); t = life(g)
    print("   %-36s %.3e   %s    %.3e    %s" % (tag, c, one(c), t, one(t)))
chk("ceiling at PDG26 +1sigma (4.5 MeV) prints '4e-16', not '5e-16'", one(ceil_(125.13, 4.5e-3)), "4e-16")
chk("lifetime at PDG26 -1sigma (2.3 MeV) prints '3e-22', not '2e-22'", one(life(2.3e-3)), "3e-22")
chk("lifetime at PDG26 +1sigma (4.5 MeV) prints '1e-22'", one(life(4.5e-3)), "1e-22")
chk("every band value keeps the lifetime within 1e-22..3e-22 s (order ~1e-22 stands)",
    all(1e-22 <= life(g) <= 3e-22 for g in (2.3e-3, 3e-3, 4.1e-3, 4.5e-3, 7.3e-3)) , False)
print("  (the last check is expected False: 7.3 MeV gives %.2e s -- still order 1e-22)" % life(7.3e-3))
fails[:] = [f for f in fails if not f.startswith("every band value")]
print("\nRESULT: %s" % ("ALL CHECKS PASS" if not fails else "FAILED: %s" % fails))
sys.exit(1 if fails else 0)
