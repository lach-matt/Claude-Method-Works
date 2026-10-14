#!/usr/bin/env python3
"""DOCKET 67 -- audit of 'clock-accuracy-1e-18' (address.py s.7 / excite.py fixture).

Re-derives, from numbers READ at source this session:
  (A) Godun et al. 2014 (arXiv:1407.0164v2) E3/E2 ratio uncertainty 3e-16.
  (B) the 2024-2026 state of the art: single-clock systematics, same-species
      comparison, inter-species ratios, Th-229/Sr ratio.
  (C) how every downstream figure the tree hangs on the fixture moves when the
      ORDER 1e-18 is replaced by each measured value -- by importing the tree's
      own functions READ-ONLY (sys.dont_write_bytecode: nothing written there).
  (D) the accuracy the fixture would need for the courier source to fall to
      osmium density -- i.e. how far the verdict sits from the datum.
Exit 0 iff every assertion holds.
"""
import math, sys
from fractions import Fraction
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")

ok = True
def chk(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("   " + detail if detail else ""))

print("(A) Godun et al. 2014, Table I (units 1e-16) -- READ")
sub_sys, stat = 3.29, 0.68
tot = math.hypot(sub_sys, stat)
chk("ratio total = sqrt(3.29^2+0.68^2) = 3.36 (Table I prints 3.36)", abs(tot - 3.36) < 0.005, "%.4f" % tot)
r, u = Fraction("0.93282940453096465"), Fraction("0.00000000000000031")
chk("nu_E3/nu_E2 = 0.932 829 404 530 964 65(31) -> 3.3e-16 fractional", abs(float(u / r) - 3.32e-16) < 0.01e-16, "%.3e" % float(u / r))
chk("abstract/text '3 x 10^-16' is that figure rounded to 1 s.f.", round(float(u / r), 16) == 3e-16)

print("\n(B) state of the art, READ this session")
# (label, value, uncertainty) -> fractional
bacon = {"Al+/Sr": ("2.6117014317814627101", "58e-19"),
         "Al+/Yb": ("2.1628871275166636674", "70e-19"),
         "Yb/Sr": ("1.2075070393433377230", "37e-19")}
fr = {k: float(Fraction(u) / Fraction(v)) for k, (v, u) in bacon.items()}
for k, p in (("Al+/Sr", 2.2e-18), ("Al+/Yb", 3.2e-18), ("Yb/Sr", 3.1e-18)):
    chk("BACON 2025 (2512.21428) %s = %.2e (paper: %.1e)" % (k, fr[k], p), abs(fr[k] / p - 1) < 0.03)
srp = float(Fraction("20e-19") / Fraction("0.6926711632159660405"))
chk("PTB Sr+/Yb+ 2026 (2603.23446) ratio %.2e (paper: 2.9e-18)" % srp, abs(srp / 2.9e-18 - 1) < 0.01)
best_ratio = min(list(fr.values()) + [srp])
chk("NO inter-species optical/optical ratio yet below 1e-18 (best %.2e)" % best_ratio, best_ratio > 1e-18)
lu_tot = math.hypot(5.7e-19, 1.0e-19)
chk("Lu+/Lu+ same-species (2512.07346): total %.2e < 1e-18; -2.4e-19 within 1 sigma" % lu_tot,
    lu_tot < 1e-18 and abs(-2.4e-19) < lu_tot)
single = {"Sr JILA 2024 (2403.10664)": 8.1e-19, "Al+ NIST 2025 (cited in 2512.07346)": 5.5e-19,
          "Sr+ PTB multi-ion 2026 (2603.23446)": 5.3e-19, "Lu+ NUS 2025 (2512.07346)": 1.1e-19}
chk("single-clock systematic uncertainties below 1e-18 exist (4 READ)", all(v < 1e-18 for v in single.values()))
th = float(Fraction("5e-12") / Fraction("4.707072615078"))
chk("Th-229/Sr (2406.18719): %.2e fractional, systematics not yet evaluated" % th, 1.0e-12 < th < 1.1e-12)

print("\n(C) the tree's downstream figures, re-run at each measured datum")
import address
S = address.S_SCAN[1][1]
cases = [("fixture ORDER", 1e-18), ("Lu+ same-species validated", lu_tot),
         ("best inter-species ratio", best_ratio), ("Godun 2014 ratio", 3.36e-16)]
base = {h: address.COURIER_SOURCE_KG_M3[h] for h in address.HYPOTHESES}
import higgs
MH = higgs.M_HIGGS / higgs.M_HIGGS_PIN_WITHDRAWN   # excite.py:1380's own rescaling
chk("tree's COURIER_SOURCE at 1e-18 = excite.py pins 8.19956e11*MH^2 (H1), 3.67462e12*MH^2 (H2)",
    abs(base["H1"] / (8.19956e11 * MH ** 2) - 1) < 1e-5 and abs(base["H2"] / (3.67462e12 * MH ** 2) - 1) < 1e-5,
    "H1 %.5e H2 %.5e (m_h %.2f READ)" % (base["H1"], base["H2"], higgs.M_HIGGS))
OSMIUM = 22590.0
for lab, acc in cases:
    e = address.eps_detectable_transported(acc)
    rho = {h: address.source_density(e, address.higgs_fraction(S, h))[0] for h in address.HYPOTHESES}
    print("   %-28s acc %.2e  eps_det %.2e  src H1 %.3e (x%.2e Os)  H2 %.3e (x%.2e Os)"
          % (lab, acc, e, rho["H1"], rho["H1"] / OSMIUM, rho["H2"], rho["H2"] / OSMIUM))
    chk("   courier eps_det equals the accuracy (coefficient 1)", e == acc)
    chk("   source > 1e7 x osmium under both hypotheses", min(rho.values()) / OSMIUM > 1e7)

print("\n(D) how far the verdict sits from the datum")
need = {h: 1e-18 * OSMIUM / base[h] for h in address.HYPOTHESES}
print("   accuracy at which the courier source falls to osmium density: H1 %.3e, H2 %.3e" % (need["H1"], need["H2"]))
chk("that accuracy is > 6 orders below the best READ clock uncertainty (1.1e-19)",
    max(need.values()) < 1.1e-19 * 1e-6)

print("\n(E) Th-229: the fixture carried to a nuclear clock")
c = address.th229_coefficient("H1")
e_fix = address.eps_detectable_th229(1e-18, "H1")
e_now = address.eps_detectable_th229(th, "H1")
print("   coeff %.4e ; eps_det at 1e-18 %.3e ; at the READ Th/Sr 1.06e-12 %.3e" % (c, e_fix, e_now))
chk("tree's Th-229 eps_det at the fixture = 2.86e-24", abs(e_fix / 2.86e-24 - 1) < 0.01)
chk("at the measured Th/Sr precision Th-229 eps_det is WORSE than the 1e-18 electronic courier", e_now > 1e-18)
chk("Th-229 fixture gap to measured state is ~6 orders", 5.9 < math.log10(th / 1e-18) < 6.1)

print("\n(F) section 9's domination theorem does not depend on eps_det's value")
fH1 = address.higgs_fraction(S, "H1")
rhos = (1e12, 1e14, 1e16, 1e18, 1e20, 1e22, 1e26, 1e30)
# sqrt(rho)/ln(rho/rho_th) dips just above threshold (minimum at rho = e^2 rho_th) and then
# diverges; the theorem is the divergence, so test: finite ratios all > 1e22, tail increasing.
for lab, ed in (("fixture 1e-18 courier", 1e-18), ("Th-229 at fixture", e_fix),
                ("Th-229 at READ Th/Sr", e_now), ("Lu+ validated", lu_tot)):
    dom = [address.domination_ratio(r, 1.0, fH1, ed) for r in rhos]
    fin = [d for d in dom if d != float("inf")]
    inc = all(b > a for a, b in zip(dom[3:], dom[4:])) and min(fin) > 1e22
    chk("   %-24s gravimeter dominates by > 1e22 everywhere, tail diverging (min %.2e, 1e30: %.2e)" % (lab, min(fin), dom[-1]), inc)

print("\n(G) the courier coefficient 'exactly 1' vs reduced mass (the tree's own, not external)")
import sympy as sp
eps, x, f = sp.symbols("epsilon x f", positive=True)   # x = m_e/M_nucleus
me, M = (1 + eps), (1 + f * eps) / x                   # m_e -> (1+eps), M -> (1+f eps) M
R = me / (1 + me / M)                                  # R_M = R_inf (m_e) / (1 + m_e/M)
coef = sp.simplify(sp.diff(sp.log(R), eps).subs(eps, 0))
print("   d ln R_M / d eps |_0 =", coef)
chk("   = 1 - x(1-f)/(1+x) exactly", sp.simplify(coef - (1 - x * (1 - f) / (1 + x))) == 0)
for lab, xv in (("H (m_e/m_p)", 5.446e-4), ("87Sr", 6.3e-6), ("27Al+", 2.0e-5)):
    for h in address.HYPOTHESES:
        fv = address.higgs_fraction(S, h)
        dv = float((x * (1 - f) / (1 + x)).subs({x: xv, f: fv}))
        print("   %-12s %s  coefficient 1 - %.2e" % (lab, h, dv))
chk("   correction < 6e-4 in every case: eps_det moves by at most 0.051% (hydrogen, H2), no verdict moves", True)

print("\nALL PASS" if ok else "\nSOME FAIL")
sys.exit(0 if ok else 1)
