#!/usr/bin/env python3
"""DOCKET 67 / pass S / 33 of 36 -- pdg-higgs-mass-vev.

Audits the Higgs inputs address.py imports from higgs.py (m_h READ 125.13,
v = (sqrt2 G_F)^-1/2, lambda = m_h^2/2v^2, |V_min| = lambda v^4/4) and every
address.py figure that carries a power of m_h.

Nothing under research/ is written: bytecode writing is disabled before the
owner is imported.  Inputs are READ from on-disk alphaXiv page captures:
  PDG 2026 Higgs listing   src/casmag/all/https___pdg.lbl.gov_2026_listings_rpp2026-list-higgs-boson.pdf.txt
  PDG 2024 Higgs listing   src/casmag/all/https___pdg.lbl.gov_2024_listings_rpp2024-list-higgs-boson.pdf.txt
  PDG 2024 constants       src/casmag/all/https___pdg.lbl.gov_2024_reviews_rpp2024-rev-phys-constants.pdf.txt
  PDG 2024 EW review       src/casmag/all/https___pdg.lbl.gov_2024_reviews_rpp2024-rev-standard-model.pdf.txt
  Eberhart et al. 2026     src/casmag/all/2607.02657v1.txt
"""
import math
import os
import re
import sys

sys.dont_write_bytecode = True
import sympy as sp

D67 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
SRC = os.path.join(D67, "src/casmag/all")
WD = "/home/user/Claude-Method-Works/research/warp-drive"

FAIL = []


def chk(name, got, want, rel=None):
    if rel is None:
        ok = (got == want)
    else:
        ok = abs(got / want - 1.0) <= rel
    print("  [%s] %-62s %s" % ("ok" if ok else "FAIL", name,
                               got if rel is None else "%.9g (want %.9g)" % (got, want)))
    if not ok:
        FAIL.append(name)


def read(name):
    with open(os.path.join(SRC, name), encoding="utf-8", errors="replace") as f:
        return f.read()


print("A. SOURCE TEXT (on-disk alphaXiv page captures)")
p26 = read("https___pdg.lbl.gov_2026_listings_rpp2026-list-higgs-boson.pdf.txt")
p24 = read("https___pdg.lbl.gov_2024_listings_rpp2024-list-higgs-boson.pdf.txt")
pc = read("https___pdg.lbl.gov_2024_reviews_rpp2024-rev-phys-constants.pdf.txt")
pew = read("https___pdg.lbl.gov_2024_reviews_rpp2024-rev-standard-model.pdf.txt")
eb = read("2607.02657v1.txt")
chk("PDG 2026 prints '125.13± 0.11 OUR AVERAGE'", "125.13± 0.11 OUR AVERAGE" in p26, True)
chk("  with 'Error includes scale factor of 1.5.'",
    "125.13± 0.11 OUR AVERAGE \nError includes scale factor of 1.5." in p26, True)
chk("  ideogram 'χ 2 6.9 (Confidence Level = 0.075)'", "6.9 (Confidence Level = 0.075)" in p26.replace("\n", " "), True)
chk("PDG 2024 prints '125.20± 0.11 OUR AVERAGE' (the withdrawn pin)", "125.20± 0.11 OUR AVERAGE" in p24, True)
chk("PDG 2024 Table 1.1 prints G_F '1.166 378 8(6)'", "1.166 378 8(6)" in pc, True)
chk("PDG 2024 EW review: 'v = 246.22 GeV'", "v = 246.22 GeV" in pew, True)
chk("PDG 2024 EW review: masses 'at tree level'", "(at tree level, i.e., to lowest order in perturbation theory)" in pew, True)
chk("Eberhart 2026 prints G_F '1.166 378 59 (59)'", "1.166 378 59 (59)" in eb, True)
chk("PDG 2026 width: 'equal on- and off-shell effective couplings'",
    "equal on- and off-shell effective couplings" in p26.replace("assump-\ntion", "assumption").replace("\n", " "), True)

print()
print("B. SYMPY -- the tree identities address.py uses")
lam, v, h, e, r, r0, L, J = sp.symbols("lambda v h epsilon r r_0 ell J", positive=True)
phi = sp.symbols("phi", positive=True)
V = lam * (phi ** 2 / 2 - v ** 2 / 2) ** 2          # higgs.py normalisation, phi = v + h
m2 = sp.diff(V, phi, 2).subs(phi, v)
chk("V''(v) = 2 lambda v^2 (tree mass^2)", sp.simplify(m2 - 2 * lam * v ** 2), 0)
depth = sp.simplify(V.subs(phi, 0) - V.subs(phi, v))
chk("depth V(0)-V(v) = lambda v^4/4", sp.simplify(depth - lam * v ** 4 / 4), 0)
mh = sp.symbols("m_h", positive=True)
chk("8 |V_min| = v^2 m_h^2 at lambda = m_h^2/2v^2",
    sp.simplify((8 * depth).subs(lam, mh ** 2 / (2 * v ** 2)) - v ** 2 * mh ** 2), 0)
# PDG normalisation: V = mu^2 phi^dag phi + (lambda_P^2/2)(phi^dag phi)^2, M_H = lambda_P v (10.5a)
lamP = sp.sqrt(2 * lam)
chk("PDG eq.(10.5a) M_H = lambda_P v with lambda_P^2 = 2 lambda",
    sp.simplify(lamP ** 2 * v ** 2 - m2), 0)
cost = sp.simplify((V.subs(phi, v * (1 + e)) - V.subs(phi, v)) / depth)
chk("[V(v(1+eps)) - V(v)]/depth = eps^2(2+eps)^2 (offset-free)",
    sp.expand(cost - e ** 2 * (2 + e) ** 2), 0)
# static uniform response: (nabla^2 - m^2) dphi = J  ->  dphi = -J/m^2; J = m_psi n/v
dphi = -J / mh ** 2
eps_expr = (dphi / v).subs(J, sp.Symbol("rho_H") / v)   # m_psi n = rho_H (natural units)
chk("eps = -rho_H/(v^2 m_h^2)",
    sp.simplify(eps_expr + sp.Symbol("rho_H") / (v ** 2 * mh ** 2)), 0)
yuk = sp.Symbol("eps0") * r0 / r * sp.exp(-(r - r0) / L)
lap = sp.diff(r * yuk, r, 2) / r
chk("exterior eps0 (r0/r) e^{-(r-r0)/ell} solves (nabla^2 - 1/ell^2) = 0",
    sp.simplify(lap - yuk / L ** 2), 0)
chk("  and equals eps0 at r = r0", sp.simplify(yuk.subs(r, r0) - sp.Symbol("eps0")), 0)

print()
print("C. PDG 2026 AVERAGE, re-derived from its four listed inputs")
ins = [(125.04, 0.12), (125.10, 0.11), (125.78, 0.26), (125.09, math.hypot(0.21, 0.11))]
w = [1 / s ** 2 for _, s in ins]
mean = sum(wi * x for wi, (x, _) in zip(w, ins)) / sum(w)
err = 1 / math.sqrt(sum(w))
chi = [((x - mean) / s) ** 2 for x, s in ins]
S = math.sqrt(sum(chi) / (len(ins) - 1))
print("    mean %.4f  err %.4f  chi2 %.3f (%s)  S %.3f  scaled %.4f" %
      (mean, err, sum(chi), ", ".join("%.2f" % c for c in chi), S, err * S))
chk("mean rounds to 125.13", round(mean, 2), 125.13)
chk("scaled error rounds to 0.11", round(err * S, 2), 0.11)
chk("S rounds to 1.5", round(S, 1), 1.5)
chk("chi2 rounds to 6.9", round(sum(chi), 1), 6.9)
# CL for chi2 with 3 dof: Q = erfc(sqrt(x/2)) + sqrt(2x/pi) exp(-x/2)
x = sum(chi)
Q = math.erfc(math.sqrt(x / 2)) + math.sqrt(2 * x / math.pi) * math.exp(-x / 2)
chk("CL(chi2, 3 dof) rounds to 0.075", round(Q, 3), 0.075)
ins3 = [ins[0], ins[1], ins[3]]
w3 = [1 / s_ ** 2 for _, s_ in ins3]
mean3 = sum(wi * x_ for wi, (x_, _) in zip(w3, ins3)) / sum(w3)
print("    without SIRUNYAN 20L (the chi2 6.2 outlier): mean %.4f, err %.4f; m_h^2 moves %+.2e" %
      (mean3, 1 / math.sqrt(sum(w3)), (mean3 / 125.13) ** 2 - 1))
chk("dropping the outlier moves m_h by < 0.1 GeV", abs(mean3 - mean) < 0.1, True)

print()
print("D. INDEPENDENT NUMBERS from READ inputs and exact SI constants")
h_SI = 6.62607015e-34
hbar = h_SI / (2 * math.pi)
c = 299792458.0
GeV = 1.602176634e-10
hbarc = hbar * c
GF = 1.1663788e-5
MH = 125.13
MH24 = 125.20
ME26 = 0.51099895069e-3      # PDG 2026 (= CODATA 2022), GeV
ME18 = 0.51099895000e-3      # address.M_E_MEV (CODATA 2018)


def vev(g):
    return (math.sqrt(2) * g) ** -0.5


def vmin_si(m, g=GF):
    return (m ** 2 * vev(g) ** 2 / 8) * GeV ** 4 / hbarc ** 3


def lam_h(m):
    return hbarc / (m * GeV)


vv = vev(GF)
print("    v %.6f GeV  lambda %.12f  |V_min| %.6e GeV^4 = %.6e J/m^3" %
      (vv, MH ** 2 / (2 * vv ** 2), MH ** 2 * vv ** 2 / 8, vmin_si(MH)))
print("    lambda_h %.6e m   (m_e/m_h)^2 %.6e (CODATA 2022 m_e) / %.6e (address m_e)" %
      (lam_h(MH), (ME26 / MH) ** 2, (ME18 / MH) ** 2))

import importlib
os.chdir(WD)
sys.path.insert(0, WD)
address = importlib.import_module("address")
higgs = importlib.import_module("higgs")
chk("owner v equals independent v", higgs.vev(), vv, 1e-12)
chk("owner M_HIGGS is the PDG 2026 print", higgs.M_HIGGS, 125.13)
chk("owner |V_min| J/m^3 vs exact-SI recomputation", address.VMIN_SI, vmin_si(MH), 2e-9)
chk("owner lambda_h vs exact-SI recomputation", address.yukawa_range(), lam_h(MH), 2e-9)
chk("owner 8|V_min| = v^2 m_h^2", 8 * address.VMIN_SI,
    MH ** 2 * vv ** 2 * GeV ** 4 / hbarc ** 3, 2e-9)
chk("owner lambda = 0.129136053130", higgs.lam(), 0.129136053130, 1e-10)
chk("LAMBDA_QUARTIC imported but used nowhere else in address.py",
    open(os.path.join(WD, "address.py")).read().count("LAMBDA_QUARTIC"), 1)

print()
print("E. DATA MOVES -- each figure against m_h and G_F")
epsdet_H1 = address.eps_detectable(address.GODUN_ABS_UNC, "optical", "hyperfine",
                                   address.S_SCAN[1][1], "H1")
epsdet_H2 = address.eps_detectable(address.GODUN_ABS_UNC, "optical", "hyperfine",
                                   address.S_SCAN[1][1], "H2")
fH1 = float(address.dln_mp_dln_v(address.S_SCAN[1][1], "H1"))
fH2 = float(address.dln_mp_dln_v(address.S_SCAN[1][1], "H2"))
print("    eps_det H1 %.4e  H2 %.4e  (no m_h in either)" % (epsdet_H1, epsdet_H2))


def figs(m, g=GF, me=ME18):
    Vs = vmin_si(m, g)
    lh = lam_h(m)
    nucH1 = address.RHO_NUCLEAR * fH1 * c ** 2 / (8 * Vs)
    nucH2 = address.RHO_NUCLEAR * fH2 * c ** 2 / (8 * Vs)
    ceil = (me / m) ** 2
    probe_eps = address.GODUN_RATIO_UNC / ceil
    OSM = 2.259e4
    courH1 = 1e-18 * 8 * Vs / c ** 2 / fH1
    courH2 = 1e-18 * 8 * Vs / c ** 2 / fH2
    standoff = lh * math.log(1.0 / epsdet_H1)
    return {
        "lambda_h (m)": lh,
        "lambda_h / r_p": lh / address.R_PROTON_M,
        "standoff at eps0=1 (am), 1 fm sphere": 1e18 * address.detection_standoff(1.0, 1e-15, epsdet_H1) if m == higgs.M_HIGGS else float("nan"),
        "eps nuclear H1": -nucH1,
        "eps nuclear H2": -nucH2,
        "nuclear / eps_det H1": nucH1 / epsdet_H1,
        "nuclear / eps_det H2": nucH2 / epsdet_H2,
        "(m_e/m_h)^2": ceil,
        "probe eps": probe_eps,
        "courier source H1 (kg/m^3)": courH1,
        "courier source H2 (kg/m^3)": courH2,
        "courier H1 / osmium": courH1 / OSM,
        "courier H2 / osmium": courH2 / OSM,
    }


# docstring figures (address.py line, printed string) -- recorded against both m_h values
DOC = [
    (163, "lambda_h (m)", "1.5761e-18", "%.4e"),
    (164, "lambda_h / r_p", "0.0019", "%.4f"),
    (192, "eps nuclear H1", "-3.26e-13", "%.2e"),
    (192, "eps nuclear H2", "-7.28e-14", "%.2e"),
    (192, "nuclear / eps_det H1", "398", "%.0f"),
    (192, "nuclear / eps_det H2", "114", "%.0f"),
    (234, "(m_e/m_h)^2", "1.6658e-11", "%.4e"),
    (237, "probe eps", "1.80e-05", "%.2e"),
    (263, "courier source H1 (kg/m^3)", "8.20e+11", "%.2e"),
    (263, "courier source H2 (kg/m^3)", "3.67e+12", "%.2e"),
    (264, "courier H1 / osmium", "3.63e+07", "%.2e"),
    (264, "courier H2 / osmium", "1.63e+08", "%.2e"),
]
F26 = figs(MH)
F24 = figs(MH24)
stale = []
print("    %-5s %-30s %-11s %-11s %-11s %s" % ("line", "figure", "docstring", "at 125.13", "at 125.20", "verdict"))
for ln, k, s, fmt in DOC:
    a, b = fmt % F26[k], fmt % F24[k]
    ok26 = (a == s)
    tag = "matches READ m_h" if ok26 else ("STALE: matches withdrawn 125.20" if b == s else "matches neither")
    if not ok26:
        stale.append((ln, k, s, a))
    print("    %-5d %-30s %-11s %-11s %-11s %s" % (ln, k, s, a, b, tag))
chk("owner's printed nuclear eps H1 reproduced", F26["eps nuclear H1"],
    address.eps_from_matter(address.RHO_NUCLEAR, fH1), 3e-9)   # ladder HBAR is CODATA-rounded (6e-10), cubed
chk("owner's printed probe eps reproduced", F26["probe eps"], 1.798888e-05, 1e-5)
chk("owner's courier H1 reproduced", F26["courier source H1 (kg/m^3)"], 8.190398e11, 1e-5)
print("    stale docstring figures (withdrawn-pin roundings): %d" % len(stale))
chk("exactly 6 docstring figures are the 125.20 roundings", len(stale), 6)

print()
print("    relative moves, 125.20 -> 125.13, and the +-0.11 GeV (S=1.5) band")
for k in ("lambda_h (m)", "eps nuclear H1", "(m_e/m_h)^2", "courier source H1 (kg/m^3)"):
    lo, hi = figs(MH - 0.11)[k], figs(MH + 0.11)[k]
    print("      %-30s %+.3e   band [%+.3e, %+.3e]" %
          (k, F26[k] / F24[k] - 1, lo / F26[k] - 1, hi / F26[k] - 1))
for g, lab in ((1.1663788e-5, "PDG 2024"), (1.16637859e-5, "Eberhart 2026"),
               (1.1663787e-5, "CODATA 2018 / MuLan 2013")):
    print("      G_F %-26s v %.6f  eps_nuclear H1 moves %+.2e" %
          (lab, vev(g), figs(MH, g)["eps nuclear H1"] / F26["eps nuclear H1"] - 1))
chk("m_e CODATA 2018->2022 moves (m_e/m_h)^2 by < 3e-9",
    abs(figs(MH, me=ME26)["(m_e/m_h)^2"] / F26["(m_e/m_h)^2"] - 1) < 3e-9, True)

print()
print("F. MARGINS -- how far m_h^2 v^2 would have to move to flip a verdict")
print("    nuclear matter over threshold: x%.1f (H1), x%.1f (H2): the coefficient v^2 m_h^2"
      " would have to GROW by that factor" % (F26["nuclear / eps_det H1"], F26["nuclear / eps_det H2"]))
print("    in m_h alone: m_h > %.0f GeV (H1) / %.0f GeV (H2)" %
      (MH * math.sqrt(F26["nuclear / eps_det H1"]), MH * math.sqrt(F26["nuclear / eps_det H2"])))
# domination theorem: r/d ~ sqrt(rho)/ln(rho) for any finite m_h > 0
rr, mm = sp.symbols("rho m", positive=True)
ratio = sp.sqrt(rr) / ((1 / mm) * sp.log(rr))
chk("domination limit r/d -> oo as rho -> oo for every m_h > 0",
    sp.limit(ratio, rr, sp.oo), sp.oo)
# complex pole: Re sqrt(M^2 - i M Gamma) vs M
G = 3.0e-3
kappa = complex(MH ** 2, -MH * G) ** 0.5
print("    width 3.0 MeV: Re(sqrt(M^2 - i M Gamma))/M - 1 = %.2e (range move)" % (kappa.real / MH - 1))
chk("width moves lambda_h by < 1e-9", abs(kappa.real / MH - 1) < 1e-9, True)

print()
print("RESULT:", "ALL CHECKS PASS" if not FAIL else "FAIL: %s" % FAIL)
sys.exit(1 if FAIL else 0)
