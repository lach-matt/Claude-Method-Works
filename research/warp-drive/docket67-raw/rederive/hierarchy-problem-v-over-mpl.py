#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key hierarchy-problem-v-over-mpl.

Checks, each printed PASS/FAIL (exit 1 on any FAIL):
 A. SYMBOLIC (sympy): Barcelo-Visser's exact ANEC-gate condition phi^2 > kappa/xi with
    kappa = 1/(8 pi G_N) (gr-qc/0003025 p.3, eq. 2.1; case 3 p.6) is, in hbar=c=1,
    phi > M_Pl/sqrt(8 pi xi) = M_red/sqrt(xi): the REDUCED Planck mass, not BV's prose
    "~ m_p/sqrt(xi), where m_p is the Planck mass" (p.16), which is the same up to sqrt(8 pi).
    And xi_required(v) = (M_red/v)^2 identically.  Also: the SM doublet normalisation
    H = (0,(v+h)/sqrt2) gives xi H^dag H R = (1/2) xi phi^2 R with phi = v+h, i.e. BV's
    (1/2) xi R phi^2 with the canonical radial field -- so phi = v is the right entry.
 B. NUMERIC: v/M_red and v/M_Pl from (i) the tree's inputs (higgs.py:209, ladder.py:53-55)
    and (ii) CODATA 2022 (arXiv:2409.03787 Table XXXIII: G = 6.67430(15)e-11, unchanged
    from 2018; G_F/(hbar c)^3 = 1.1663787(6)e-5 GeV^-2 = MuLan arXiv:1211.0960 eq. 24).
 C. Giudice 0801.2562 eq.(1): G_F hbar^2/(G_N c^2) = 1.73859(15)e33 (PDG 2006) re-derived
    from CODATA 2022.
 D. Sensitivity: how far the log10 hierarchy moves under (a) G's uncertainty, (b) the full
    spread of the 16 inconsistent G measurements (CODATA 2022 Table XXX), (c) a 1% scheme
    shift of v; and the margin before "sixteen orders" (rounded) would change.
 E. "EXACTLY the famous fine-tuning" (higgs.py:156-157): Giudice eq.(9) tuning at
    Lambda = M_Pl vs xi_required -- same ORDER, not the same number.  Masses other than
    m_h are NAMED-NOT-READ round PDG values (illustrative only).
"""
import math, sys
import sympy as sp

fails = 0
def chk(name, ok, detail=""):
    global fails
    print(("PASS " if ok else "FAIL ") + name + ("   " + detail if detail else ""))
    if not ok:
        fails += 1

# ---------------------------------------------------------------- A. symbolic
G, xi, phi, v, h = sp.symbols("G xi phi v h", positive=True)
kappa = 1 / (8 * sp.pi * G)                 # BV p.3: kappa = 1/(8 pi G_N)
M_Pl = 1 / sp.sqrt(G)                       # hbar = c = 1
M_red = M_Pl / sp.sqrt(8 * sp.pi)
gate = sp.sqrt(kappa / xi)                  # BV case 3 threshold |phi| = (kappa/xi)^(1/2)
chk("A1 BV gate sqrt(kappa/xi) == M_red/sqrt(xi)", sp.simplify(gate - M_red / sp.sqrt(xi)) == 0)
chk("A2 BV gate / (M_Pl/sqrt(xi)) == 1/sqrt(8 pi)  (BV prose '~m_p/sqrt(xi)' is off by sqrt(8pi))",
    sp.simplify(gate / (M_Pl / sp.sqrt(xi)) - 1 / sp.sqrt(8 * sp.pi)) == 0)
xi_req = sp.solve(sp.Eq(v**2, kappa / xi), xi)[0]
chk("A3 xi_required(v) == (M_red/v)^2 identically", sp.simplify(xi_req - (M_red / v)**2) == 0)
# doublet normalisation: H^dag H = (v+h)^2/2 ; xi H^dag H R  vs  (1/2) xi R phi^2
HdH = ((v + h) / sp.sqrt(2))**2
chk("A4 xi H^dag H R == (1/2) xi R phi^2 with phi = v+h", sp.simplify(xi * HdH - sp.Rational(1, 2) * xi * (v + h)**2) == 0)

# ---------------------------------------------------------------- B. numeric
c = 2.99792458e8; HBAR = 1.054571817e-34; GEV_J = 1.602176634e-10
def planck(Gval): return math.sqrt(HBAR * c**5 / Gval) / GEV_J
def vev(GF): return 1.0 / math.sqrt(math.sqrt(2.0) * GF)

tree = dict(G=6.67430e-11, GF=1.1663788e-5)          # higgs.py:209, ladder.py:54
now  = dict(G=6.67430e-11, GF=1.1663787e-5)          # CODATA 2022 / MuLan 2012
uG, uGF = 0.00015e-11, 0.0000006e-5
res = {}
for tag, d in (("tree", tree), ("codata2022", now)):
    mp = planck(d["G"]); mr = mp / math.sqrt(8 * math.pi); vv = vev(d["GF"])
    res[tag] = (mp, mr, vv, vv / mr, vv / mp)
    print("  %-10s M_Pl=%.6e  M_red=%.6e  v=%.6f  v/M_red=%.10e (log10 %.5f)  v/M_Pl=%.6e (log10 %.5f)"
          % (tag, mp, mr, vv, vv / mr, math.log10(vv / mr), vv / mp, math.log10(vv / mp)))
mp, mr, vv, hr, hp = res["tree"]
chk("B1 tree M_Pl = 1.220890e19 GeV (higgs.py:609) = CODATA 2022 m_P c^2 1.220890(14)e19",
    abs(mp / 1.220890e19 - 1) < 1e-6, "%.7e" % mp)
chk("B2 tree M_red = 2.435323e18 GeV (higgs.py:610)", abs(mr / 2.435323e18 - 1) < 1e-6, "%.7e" % mr)
chk("B3 tree v/M_red = 1.0110346504e-16 (higgs.py:645)", abs(hr / 1.0110346504e-16 - 1) < 1e-9, "%.10e" % hr)
shift = res["codata2022"][3] / hr - 1
chk("B4 G_F 1.1663788 -> 1.1663787 (CODATA 2022/MuLan) moves v/M_red by < 1e-7 rel", abs(shift) < 1e-7, "%.2e" % shift)
chk("B5 log10(M_red/v) rounds to 16", round(-math.log10(hr)) == 16, "%.5f" % -math.log10(hr))
chk("B6 log10(M_Pl/v) = 16.70 (rounds to 17: 'sixteen orders' is the REDUCED-mass figure)",
    round(-math.log10(hp)) == 17, "%.5f" % -math.log10(hp))
chk("B7 xi_required = 9.7829e31 (higgs.py:640), log10 = 31.99", abs((1 / hr**2) / 9.7829068836e31 - 1) < 1e-9,
    "log10 %.4f" % math.log10(1 / hr**2))

# data-supported precision: relative uncertainty of v/M_red
rel_u = math.hypot(0.5 * uG / now["G"], 0.5 * uGF / now["GF"])
print("  relative 1-sigma uncertainty of v/M_red from data: %.2e  (tree quotes 11 sig. figs, "
      "selftest tolerance 1e-9 -- digits beyond ~5 are arithmetic, not measurement)" % rel_u)
chk("B8 data support ~5 significant figures of v/M_red, not 11", 1e-6 < rel_u < 1e-4, "%.2e" % rel_u)

# ---------------------------------------------------------------- C. Giudice eq (1)
G_over_hbarc = now["G"] / (HBAR * c) * (GEV_J / c**2)**2      # (GeV/c^2)^-2
chk("C0 G/(hbar c) = 6.70883e-39 (GeV/c^2)^-2 (CODATA 2022 Table XXXIII)", abs(G_over_hbarc / 6.70883e-39 - 1) < 2e-6,
    "%.6e" % G_over_hbarc)
ratio = now["GF"] / G_over_hbarc
chk("C1 G_F/G_N = 1.73859(15)e33 (Giudice eq.1, PDG 2006) reproduced within its error", abs(ratio - 1.73859e33) < 0.00015e33,
    "now %.5e" % ratio)
chk("C2 identity: G_F/G_N = M_Pl^2/(sqrt2 v^2)", abs(ratio / (mp**2 / (math.sqrt(2) * vv**2)) - 1) < 1e-6)

# ---------------------------------------------------------------- D. sensitivity
Gmin, Gmax = 6.67191e-11, 6.67559e-11                          # LENS-14, BIPM-01 (Table XXX)
dlog_sig = abs(math.log10(planck(now["G"] + uG) / planck(now["G"])))
dlog_spread = abs(math.log10(planck(Gmin) / planck(Gmax)))
dlog_v1 = math.log10(1.01)
margin_lo = -math.log10(hr) - 15.5; margin_hi = 16.5 - (-math.log10(hr))
print("  dlog10 from 1-sigma G: %.2e; from full G-measurement spread: %.2e; from 1%% v shift: %.2e"
      % (dlog_sig, dlog_spread, dlog_v1))
print("  margin before 'sixteen orders' (rounded) changes: -%.3f / +%.3f dex" % (margin_lo, margin_hi))
chk("D1 no measured or contested datum moves the hierarchy by > 0.01 dex",
    max(dlog_sig, dlog_spread, dlog_v1) < 0.01)
chk("D2 but log10(M_red/v) = 15.995 sits 0.005 dex under the 16 mark: 'sixteen' is the rounding, not a floor",
    -math.log10(hr) < 16.0)

# ---------------------------------------------------------------- E. same number or same order?
GF = now["GF"]; mt, mW, mZ = 172.5, 80.37, 91.19     # NAMED-NOT-READ round values
mh = 125.13                                          # tree's READ capture (higgs.py:652)
coef = 3 * GF / (4 * math.sqrt(2) * math.pi**2) * (4 * mt**2 - 2 * mW**2 - mZ**2 - mh**2)   # Giudice eq.(9)
for lab, Lam in (("M_Pl", mp), ("M_red", mr)):
    tuning = coef * Lam**2 / mh**2
    print("  Giudice eq.(9) |delta m_h^2|/m_h^2 at Lambda=%s: %.3e (log10 %.2f)  vs xi_required %.3e (log10 %.2f)"
          % (lab, tuning, math.log10(tuning), 1 / hr**2, math.log10(1 / hr**2)))
t_pl = coef * mp**2 / mh**2
chk("E1 the fine-tuning and xi_required agree in ORDER (within 1 dex) at Lambda = M_Pl",
    abs(math.log10(t_pl) - math.log10(1 / hr**2)) < 1.0)
chk("E2 ...and are NOT the same number (differ by > 0.1 dex): 'EXACTLY the quantity' is an overstatement",
    abs(math.log10(t_pl) - math.log10(1 / hr**2)) > 0.1, "ratio %.2f" % (t_pl * hr**2))

print("\n%d FAIL" % fails)
sys.exit(1 if fails else 0)
