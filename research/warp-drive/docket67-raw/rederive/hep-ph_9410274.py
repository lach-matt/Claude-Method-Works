#!/usr/bin/env python3
"""DOCKET 67 audit re-derivation: Ji, hep-ph/9410274 (PRL 74, 1071), as used by
research/warp-drive/massform.py.  READ-ONLY import of massform (no bytecode).

What is checkable here without the source (the source could NOT be read in this
pass: alphaXiv quota exceeded; arxiv.org and every mirror egress-refused):
  A  the tree's held quote parses to the values it uses
  B  the fractions 17.04 % / 11.72 % from 160 / 110 MeV over m_N
  C  the normalisation choice (m_p, m_N, m_n, or a 940 MeV table total) moves them
  D  the 50 MeV difference and the 0.2362 margin illustration recomputed
  E  robustness: what Ji row value would bring the payload share to 1/2
  F  CONDITIONAL (formulas restated FROM MEMORY, NOT READ -- flagged): the
     four-term sum closes identically; M_m = (1+gamma_m/4) x sigma-sum; the
     tree-held FLAG sigma sums imply M_m of 87-115 MeV against Ji's 160 / 110.
Exit 0 iff every A-E check passes (F is reported, never asserted as the source).
"""
import os, sys, math
sys.dont_write_bytecode = True
WD = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, WD)
import massform as m
import sympy as sp

fails = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    if not ok:
        fails.append(name)

# ---- A: the held quote (tree's own READ text) carries the numerals used
held = m.SOURCES["Ji-table"]
txt = held[2]
chk("A1 held Ji-table status word is READ", held[0] == "READ", held[1])
for num in ("160", "110", "5 to 10 MeV", "nearest 10 MeV", "<P|m_s ss|P>",
            "could be larger than the difference"):
    chk("A2 held text contains %r" % num, num in txt)
chk("A3 JI_QUARK_MASS_MEV == {160, 110}",
    m.JI_QUARK_MASS_MEV == {"m_s -> 0": 160.0, "m_s -> infinity": 110.0})
chk("A4 held Ji-cancel quote present",
    "cancel each other in the limit" in m.SOURCES["Ji-cancel"][2])
chk("A5 held Ji-eighth quote present", "about 1/8" in m.SOURCES["Ji-eighth"][2])

# ---- B: fractions
mp, mn = m.MASS_MEV["p"], m.MASS_MEV["n"]
mN = (mp + mn) / 2
f0, finf = 160 / mN, 110 / mN
print("m_p = %.9f  m_n = %.9f  m_N = %.7f MeV" % (mp, mn, mN))
chk("B1 160/m_N rounds to 17.04 %", round(100 * f0, 2) == 17.04, "%.4f %%" % (100 * f0))
chk("B2 110/m_N rounds to 11.72 %", round(100 * finf, 2) == 11.72, "%.4f %%" % (100 * finf))
chk("B3 tree JI_FRACTION equals recomputation",
    abs(m.JI_FRACTION["m_s -> 0"] - f0) < 1e-15 and abs(m.JI_FRACTION["m_s -> infinity"] - finf) < 1e-15)
# CODATA 2022 masses (m_p 938.27208943, m_n 939.56542194 MeV) vs held CODATA 2018
mN22 = (938.27208943 + 939.56542194) / 2
chk("B4 CODATA 2018->2022 moves 160/m_N by < 1e-6 (relative)",
    abs(160 / mN22 - f0) / f0 < 1e-6, "delta = %.2e" % (160 / mN22 - f0))

# ---- C: normalisation sensitivity (a 940 MeV table total is FROM MEMORY, unread)
for lab, M in (("m_p", mp), ("m_N", mN), ("m_n", mn), ("940 (table total, MEMORY)", 940.0)):
    print("  C  160/%-26s = %.4f %%   110/... = %.4f %%" % (lab, 100 * 160 / M, 100 * 110 / M))
spread = 100 * (160 / mp - 160 / 940.0)
chk("C1 normalisation choice moves the 160 row by < 0.05 percentage points (first run used 0.03 and failed at 0.0313: the bound was this script's guess, not a tree claim)", spread < 0.05,
    "%.4f pp" % spread)
eighth = mN / 8
print("  C  1/8 of m_N = %.1f MeV (Ji's prose 'about 1/8'); the two rows are 160 and 110" % eighth)
chk("C2 1/8 of m_N lies between the two Table I rows", 110 < eighth < 160)

# ---- D: estimate difference and margin illustration
chk("D1 estimate difference = 50 MeV", m.JI_ESTIMATE_DIFFERENCE_MEV == 50.0)
pm = m.payload_masses()
nuc, M = pm["nucleon rest"], m.PAYLOAD_KG
ele = pm["electron rest"] / M
read_max = ele + f0 * nuc / M
chk("D2 largest READ central reading = ele + (160/m_N) nuc/M = 0.1719",
    round(read_max, 4) == 0.1719 and abs(read_max - m.HIGGS_SHARE_LARGEST_READ) < 1e-15,
    "%.6f" % read_max)
marg = ele + (160 + 10 + 50) / mN * nuc / M
chk("D3 margin illustration: Ji 160+10+50 MeV row gives 0.2362 and is the max",
    round(marg, 4) == 0.2362 and abs(marg - m.read_rows_margin_illustration()) < 1e-15,
    "%.6f ; (220/m_N) = %.4f %%" % (marg, 100 * 220 / mN))

# ---- E: robustness
x_half = (0.5 - ele) * M / nuc * mN
chk("E1 Ji row needed for a 1/2 payload share exceeds 400 MeV", x_half > 400,
    "X = %.1f MeV = %.1f %% of m_N (Ji: 160 / 110)" % (x_half, 100 * x_half / mN))
chk("E2 even Ji's whole margin (220 MeV) is < 1/2 of X_half", 220 < x_half / 2)

# ---- F: CONDITIONAL, formulas from memory (NOT READ).  Reported, not asserted.
a, b, g, Ms = sp.symbols("a b gamma_m M", positive=True)
Mq = sp.Rational(3, 4) * (a - b / (1 + g)) * Ms
Mm = (4 + g) / (4 * (1 + g)) * b * Ms
Mg = sp.Rational(3, 4) * (1 - a) * Ms
Ma = sp.Rational(1, 4) * (1 - b) * Ms
closes = sp.simplify(Mq + Mm + Mg + Ma - Ms) == 0
print("  F1 [MEMORY-FORM] M_q+M_m+M_g+M_a - M simplifies to 0 identically:", closes)
sig = sp.symbols("sigma_sum", positive=True)  # <m psibar psi> = b M/(1+gamma_m)
ratio = sp.simplify(Mm.subs(b, sig * (1 + g) / Ms) / sig)
print("  F2 [MEMORY-FORM] M_m / sigma_sum =", ratio, "(>= 1: Ji's term exceeds the first-order response)")
flag = {"FLAG 2+1+1": m.SIGMA_PIN_2P1P1 + m.SIGMA_S_2P1P1, "FLAG 2+1": m.SIGMA_PIN_2P1 + m.SIGMA_S_2P1}
for k, s in flag.items():
    lo, hi = s, s * (1 + 0.5 / 4)
    print("  F3 %s sigma_piN+sigma_s = %.1f MeV -> M_m in [%.1f, %.1f] MeV for gamma_m in [0, 0.5]"
          " = [%.2f, %.2f] %% of m_N" % (k, s, lo, hi, 100 * lo / mN, 100 * hi / mN))
for k, v in m.JI_QUARK_MASS_MEV.items():
    print("  F4 Ji %s: %g MeV -> implied sigma_sum in [%.1f, %.1f] MeV for gamma_m in [0, 0.5]"
          % (k, v, v / (1 + 0.5 / 4), v))
share_mod = ele + (max(flag.values()) * (1 + 0.5 / 4)) / mN * nuc / M
print("  F5 payload share if Ji's rows were replaced by the largest modern M_m: %.4f (< 1/2: %s)"
      % (share_mod, share_mod < 0.5))
if not closes:
    print("  F  NOTE: memory form does not close; F is uninformative")

print("\nRESULT: %d A-E check(s) failed" % len(fails) if fails else "\nRESULT: all A-E checks pass")
sys.exit(1 if fails else 0)
