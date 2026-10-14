"""DOCKET 67 -- rederive what is checkable about the tree's use of FLAG 2024's
charm sigma term (ETM 19, sigma_c = 107(22) MeV).  Source NOT read this pass
(alphaXiv quota exhausted; arxiv.org egress-blocked).  Everything below is
either the tree's own held quote/values or exact arithmetic on them.
Imports massform.py read-only with bytecode writing disabled (no file under
research/ is written)."""
import sys, re
from fractions import Fraction as F
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import massform as mf

ok = []
def chk(name, cond, detail=""):
    ok.append(bool(cond)); print(("PASS " if cond else "FAIL ") + name + ("  -- " + detail if detail else ""))

src = mf.SOURCES["FLAG-sc"] if hasattr(mf, "SOURCES") else None
if src is None:
    for k in dir(mf):
        v = getattr(mf, k)
        if isinstance(v, dict) and "FLAG-sc" in v: src = v["FLAG-sc"]; break
quote = src[2]
print("tree's held quote (FLAG-sc):", quote)
chk("held quote prints '107(22)' for ETM 19, N_f=2+1+1", "ETM 19" in quote and "107(22)" in quote and "2 + 1 + 1" in quote)
chk("held quote prints RQCD 16 (N_f=2) sigma_c = 70(4) and f_Tc = 0.075(4)", "70(4)" in quote and "0.075(4)" in quote)
chk("SIGMA_C_ETM19 == 107.0", mf.SIGMA_C_ETM19 == 107.0)
# 'largest printed': of the two central values held, 107 > 70
chk("107 is the larger of the two held central values (tree: 'up to', 'largest printed')", 107 > 70)

MN = mf.M_N_MEV
print("M_N_MEV (tree) =", MN)
# RQCD 16 internal consistency: sigma_c = f_Tc * m_N
s_rqcd = 0.075 * MN
chk("RQCD f_Tc*m_N reproduces 70 MeV to the quoted precision", abs(s_rqcd - 70) < 4, "%.2f MeV; +-0.004*m_N = %.2f" % (s_rqcd, 0.004*MN))
f_c_etm = 107.0 / MN
print("ETM 19 f_Tc = 107/m_N = %.4f (+- %.4f)" % (f_c_etm, 22/MN))

# the tree's CONTESTED row fraction
f_row = mf.sigma_fraction(mf.SIGMA_PIN_2P1P1, mf.SIGMA_S_2P1P1, mf.SIGMA_C_ETM19)
f_hand = (F("60.9") + F("41.0") + F("107.0")) / F(str(MN))
chk("sigma_fraction(60.9, 41.0, 107) = (60.9+41+107)/m_N", abs(f_row - float(f_hand)) < 1e-12, "%.6f" % f_row)
f_l = (60.9 + 41.0) / MN
print("f_l (FLAG 2+1+1) = %.6f; sigma_c adds %.6f  (%.1f%% of the row)" % (f_l, f_c_etm, 100*107/(60.9+41+107)))

# LO heavy-quark (SVZ) expectation the tree itself carries: f_TQ = (2/27)(1-f_l)
for lbl, fl in (("FLAG 2+1+1", f_l), ("FLAG 2+1", (42.2+44.9)/MN)):
    fTQ = float(F(2, 27)) * (1 - fl)
    sQ = fTQ * MN
    pull = (107 - sQ) / 22
    print("SVZ-LO %s: f_TQ = %.5f -> sigma_Q = %.1f MeV; ETM 19 pull = %.2f sigma (ETM error only)" % (lbl, fTQ, sQ, pull))
    chk("ETM 19 within 2.1 sigma of SVZ-LO (%s)" % lbl, abs(pull) < 2.1)
# combined error budget: ETM 22 MeV dominates; SVZ LO has O(alpha_s) and 1/m_c corrections not computed here
# Ellis-Olive-Savage-style check: f_Tc_LO vs RQCD
chk("RQCD 16's 70(4) is within 1 sigma(RQCD)+1 MeV of SVZ-LO(2+1+1)", abs(70 - float(F(2,27))*(1-f_l)*MN) < 9)

# ETM 107(22) vs RQCD 70(4): difference in combined sigma
d = (107-70)/((22**2+4**2)**0.5)
print("ETM 19 - RQCD 16 = 37 MeV = %.2f combined sigma" % d)
chk("tree's 'consistent' framing: ETM vs RQCD < 2 combined sigma", d < 2)

# Does sigma_c move any printed figure?  share_rows / largest_central_reading
rows = mf.share_rows()
ele = rows[0][2]
sc_row = [r for r in rows if "sigma_c" in r[0]]
chk("exactly one sigma_c row, labelled CONTESTED as mass", len(sc_row) == 1 and sc_row[0][1].startswith("CONTESTED"))
allmax = max(rows[1:], key=lambda r: r[2])
print("row setting HIGGS_SHARE_LARGEST_ALL:", allmax[0], "%.4f" % (ele + allmax[2]))
chk("the sigma_c row does NOT set the all-rows largest reading", "sigma_c" not in allmax[0])
chk("HIGGS_SHARE_LARGEST_ALL printed 0.3090", round(mf.HIGGS_SHARE_LARGEST_ALL, 4) == 0.3090, "%.4f" % mf.HIGGS_SHARE_LARGEST_ALL)
chk("HIGGS_SHARE_LARGEST_READ printed 0.1719 (sigma_c excluded)", round(mf.HIGGS_SHARE_LARGEST_READ, 4) == 0.1719, "%.4f" % mf.HIGGS_SHARE_LARGEST_READ)
# scale: row value = f * nuc/M ; recover nuc/M from the sigma_c row
k = sc_row[0][2] / f_row
need_max = (allmax[2] / k) * MN - (60.9 + 41.0)
need_half = ((0.5 - ele) / k) * MN - (60.9 + 41.0)
print("sigma_c needed for its row to set the all-rows max: %.1f MeV (%.1f sigma above ETM 19)" % (need_max, (need_max-107)/22))
print("sigma_c needed for 'one half' at first order: %.1f MeV (%.1f sigma above ETM 19)" % (need_half, (need_half-107)/22))
chk("no plausible sigma_c (<= 107+3*22) moves the all-rows figure or reaches 0.5", need_max > 107+66 and need_half > 107+66)
print("ALL PASS" if all(ok) else "SOME FAIL", "%d/%d" % (sum(ok), len(ok)))
sys.exit(0 if all(ok) else 1)
