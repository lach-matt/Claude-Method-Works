#!/usr/bin/env python3
"""D67 rederivation for 1506.04142 (Hoferichter, Ruiz de Elvira, Kubis, Meissner,
PRL 115 092301): sigma_piN = 59.1(3.5) MeV [eq.(21)] and
sum_{q=u..t} f_q^N = 2/9 + 7/9 (f_u+f_d+f_s) = 0.305(9) [eq.(24)],
as massform.py uses them (massform.py:350, 1344-1357, 1462-1463, 1863-1868).

Read-only on the tree: massform is imported with bytecode writing off; nothing
under research/ is written.  Exit 0 iff every check passes.

Inputs and their status:
  59.1(3.5), 0.305(9)             READ (HRKM eqs.(21),(24); quoted in massform SOURCES
                                   and in the sibling D67 audit sigma-term-scan.json)
  FLAG sigma_piN / sigma_s        READ by the tree (massform FLAG-447..450)
  sigma_c 70(4) RQCD16, 107(22)   READ by the tree (massform FLAG-sc)
  3.1(5) MeV isospin-convention   READ-VIA-RESTATEMENT (2609.05989 p.2, per the
                                   sibling audit; the 2023 paper NAMED-NOT-READ)
"""
import json
import os
import sys
from fractions import Fraction

sys.dont_write_bytecode = True
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
import sympy as sp

TREE = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, TREE)
import massform as mf  # noqa: E402

OUT = {}
FAIL = []


def chk(name, got, want=True):
    ok = got == want
    OUT.setdefault("checks", []).append([name, bool(ok)])
    if not ok:
        FAIL.append(name)
    print(("PASS " if ok else "FAIL ") + name)


# ---- A. the heavy-quark algebra (LO in alpha_s, heavy-quark limit) ----------
# Trace anomaly: m_N = <theta>, theta = (beta(g)/2g) GG + sum_q m_q qq.
# Integrating out a heavy Q at LO: m_Q QQ -> -(alpha_s/(12 pi)) GG.
# With n_l light flavours, beta/2g GG -> -(beta0 alpha_s/(8 pi)) GG, beta0 = 11 - 2 n_l/3.
# So f_Q = (1/12)/(beta0/8) x (1 - sum_light f) = 2/(3 beta0) x (1 - f_light).
nl, fl, fc = sp.symbols("n_l f_l f_c", positive=True)
beta0 = 11 - sp.Rational(2, 3) * nl
fQ_coeff = sp.simplify(sp.Rational(1, 12) / (beta0 / 8))
c3 = sp.nsimplify(fQ_coeff.subs(nl, 3))
c4 = sp.nsimplify(fQ_coeff.subs(nl, 4))
chk("LO heavy-quark coefficient, 3 light flavours = 2/27", c3 == sp.Rational(2, 27))
chk("LO heavy-quark coefficient, 4 light flavours = 2/25", c4 == sp.Rational(2, 25))
sum3 = sp.expand(fl + 3 * c3 * (1 - fl))
chk("f_l + 3(2/27)(1-f_l) == 2/9 + 7/9 f_l  (HRKM eq.(24) form)",
    sp.simplify(sum3 - (sp.Rational(2, 9) + sp.Rational(7, 9) * fl)) == 0)
sum4 = sp.expand(fl + fc + 2 * c4 * (1 - fl - fc))
chk("charm treated as light: f_l+f_c + 2(2/25)(1-f_l-f_c) == 4/25 + 21/25 (f_l+f_c)",
    sp.simplify(sum4 - (sp.Rational(4, 25) + sp.Rational(21, 25) * (fl + fc))) == 0)
chk("tree coupling_sum is the same exact form (Fraction)",
    mf.coupling_sum(Fraction(1, 10)) == Fraction(2, 9) + Fraction(7, 90))
chk("tree svz_heavy_sum = 3 x (2/27)(1-f_l) exactly",
    mf.svz_heavy_sum(Fraction(1, 10)) == 3 * Fraction(2, 27) * Fraction(9, 10))

# ---- B. HRKM's own numbers -----------------------------------------------------
mN = mf.M_N_MEV
S_PIN, S_PIN_ERR = 59.1, 3.5
CS, CS_ERR = 0.305, 0.009
f_ud = S_PIN / mN
f_l_inv = (CS - 2 / 9) * 9 / 7
f_s_impl = f_l_inv - f_ud
df_l = CS_ERR * 9 / 7
df_s_impl = (df_l ** 2 - (S_PIN_ERR / mN) ** 2) ** 0.5
OUT["m_N_MeV"] = mN
OUT["f_ud = 59.1/m_N"] = f_ud
OUT["f_l inverted from 0.305"] = f_l_inv
OUT["f_s implied"] = f_s_impl
OUT["sigma_s implied MeV"] = f_s_impl * mN
OUT["delta f_l from 0.009"] = df_l
OUT["delta f_s implied (quadrature)"] = df_s_impl
OUT["delta sigma_s implied MeV"] = df_s_impl * mN
chk("tree prints sigma_piN alone as 6.2945 % (59.1/m_N)", round(100 * f_ud, 4) == 6.2945)
chk("implied sigma_s lies inside both FLAG sigma_s averages' 1-sigma bands",
    abs(f_s_impl * mN - 41.0) < 8.8 and abs(f_s_impl * mN - 44.9) < 6.4)

# ---- C. the tree's recomputation against 0.305(9) ---------------------------------
rec = {k: float(mf.coupling_sum(Fraction(v))) for k, v in mf.F_LIGHT.items()}
OUT["tree recomputation"] = rec
chk("tree 2+1+1 recomputation prints 0.3066", round(rec["FLAG 2+1+1"], 4) == 0.3066)
chk("tree 2+1 recomputation prints 0.2944", round(rec["FLAG 2+1"], 4) == 0.2944)
OUT["pulls vs 0.305(9)"] = {k: (v - CS) / CS_ERR for k, v in rec.items()}
chk("2+1+1 within 1 sigma of 0.305(9) (tree selftest claim)", abs(rec["FLAG 2+1+1"] - CS) < CS_ERR)
chk("2+1 lies OUTSIDE 1 sigma of 0.305(9) (-1.18 sigma; the tree does not claim otherwise)",
    abs(rec["FLAG 2+1"] - CS) > CS_ERR)

# ---- D. current-data variants of the u,d,s-light sum -----------------------------
def cs(f):
    return 2 / 9 + 7 / 9 * f


variants = {
    "HRKM as published (inverted, identity)": cs(f_l_inv),
    "HRKM sigma_piN in neutral-pion convention (59.1-3.1) + implied f_s": cs(f_l_inv - 3.1 / mN),
    "HRKM 59.1 + FLAG 2+1 sigma_s 44.9": cs((59.1 + 44.9) / mN),
    "HRKM 59.1 + FLAG 2+1+1 sigma_s 41.0": cs((59.1 + 41.0) / mN),
    "FLAG 2+1 (42.2 + 44.9)": cs((42.2 + 44.9) / mN),
    "FLAG 2+1+1 (60.9 + 41.0)": cs((60.9 + 41.0) / mN),
}
OUT["variants (3 light, LO heavy)"] = variants
OUT["variants pull"] = {k: (v - CS) / CS_ERR for k, v in variants.items()}
chk("every u,d,s-data variant lies within 1.25 sigma of 0.305(9)",
    all(abs(v - CS) / CS_ERR < 1.25 for v in variants.values()))

# ---- E. the charm hypothesis: LO heavy-quark f_c against lattice sigma_c ----------
fc_LO = 2 / 27 * (1 - f_l_inv)
OUT["sigma_c at LO heavy-quark (from HRKM f_l) MeV"] = fc_LO * mN
charm = {}
for lab, sc, err in (("RQCD 16, 70(4) MeV", 70.0, 4.0), ("ETM 19, 107(22) MeV", 107.0, 22.0)):
    fcl = sc / mN
    s4 = 4 / 25 + 21 / 25 * (f_l_inv + fcl)
    charm[lab] = {"pull of LO sigma_c vs lattice": (fc_LO * mN - sc) / err,
                  "coupling sum, charm from lattice, b,t LO (4 light)": s4,
                  "shift vs 0.305": s4 - CS, "shift in units of 0.009": (s4 - CS) / CS_ERR}
OUT["charm sensitivity"] = charm
chk("LO heavy-quark sigma_c (62 MeV) sits ~2 sigma below both lattice charm values",
    all(-2.5 < v["pull of LO sigma_c vs lattice"] < -1.5 for v in charm.values()))

# ---- F. does anything the tree concludes move? -----------------------------------
rows = mf.share_rows()
ele = rows[0][2]
hrkm_row = [r for r in rows if r[0] == "nucleons: six-quark coupling, Hoferichter"][0][2]
scale = hrkm_row / CS  # nuc / M
OUT["nuc/M"] = scale
OUT["HRKM row (tree)"] = hrkm_row
worst = max(list(variants.values()) + [v["coupling sum, charm from lattice, b,t LO (4 light)"]
                                        for v in charm.values()])
OUT["largest coupling sum over all variants"] = worst
OUT["largest row over all variants"] = ele + worst * scale
need = (0.5 - ele) / scale
OUT["coupling sum needed for C2 (>= 0.5)"] = need
OUT["sigma_piN + sigma_s needed for it (3-light LO) MeV"] = (need - 2 / 9) * 9 / 7 * mN
chk("the HRKM row is not the row that sets HIGGS_SHARE_LARGEST_ALL",
    abs(mf.HIGGS_SHARE_LARGEST_ALL - (ele + hrkm_row)) > 1e-6)
chk("C2 (largest row >= 0.5) stays False under every variant, charm included",
    ele + worst * scale < 0.5)
chk("tree C2 value is False", mf.HIGGS_SUPPLIES_MOST_ATOMIC_MASS is False)

OUT["FAIL"] = FAIL
json.dump(OUT, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "1506.04142.out.json"), "w"), indent=1, default=str)
print(json.dumps({k: v for k, v in OUT.items() if k != "checks"}, indent=1, default=str))
print("ALL CHECKS PASS" if not FAIL else "FAILED: %s" % FAIL)
sys.exit(1 if FAIL else 0)
