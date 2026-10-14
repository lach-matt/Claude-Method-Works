#!/usr/bin/env python3
"""DOCKET 67, audit svz-1978: the SVZ heavy-quark relation as massform.py uses it,
    f_TQ = (2/27)(1 - f_l)  for each of c, b, t   (Ellis-Olive-Savage 0801.3656 eq.(10); SVZ PLB 78, 443)
    coupling sum = f_l + 3 (2/27)(1 - f_l) = 2/9 + (7/9) f_l,  printed 0.3066 / 0.2944, all-rows 0.3090.

A. Symbolic LO derivation from the trace anomaly + SVZ decoupling (independent of the tree).
B. The tree's numbers from READ inputs (FLAG 2024 sigma terms, m_p, m_n as the tree holds them).
C. Beyond LO: Hill-Solon 1409.8290 eqs.(39),(119) series (transcription checked in the sibling
   audit dlnlambdaqcd-dlnv-2-9 against their eqs.(120),(61); imported, not re-typed), alpha_s at
   thresholds by 4-loop running from PDG-2024 inputs NAMED-NOT-READ in this stage.
D. Charm, non-perturbatively: ETM 19 sigma_c = 107(22) MeV (FLAG, READ by the tree) against LO.
E. Does any of this move the conclusion the tree rests on it ("nothing near one half")?
Exit 0 iff every check passes.  stdlib + sympy.
"""
import importlib.util, math, os, sys
from fractions import Fraction
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
FAIL = []


def chk(name, ok, detail=""):
    print("%-4s %s %s" % ("ok" if ok else "FAIL", name, detail))
    if not ok:
        FAIL.append(name)


print("A. LEADING-ORDER DERIVATION (symbolic)")
nf, als, G2, mN, fl = sp.symbols("n_f alpha_s G2 m_N f_l", positive=True)
b0 = lambda n: sp.Integer(11) - sp.Rational(2, 3) * n
# theta^mu_mu = -(b0(nf) alpha_s/(8 pi)) G^2 + sum_q m_q qbar q   (LO beta)
# SVZ heavy-quark theorem at LO: m_Q QbarQ -> -(2/3)(alpha_s/(8 pi)) G^2 = -(alpha_s/(12 pi)) G^2
svz = -sp.Rational(2, 3) * als / (8 * sp.pi) * G2
chk("SVZ normalisation -(2/3)(a/8pi) == -(a/12pi) (Ji's restatement form)",
    sp.simplify(svz + als / (12 * sp.pi) * G2) == 0)
# anomaly matching: nf=6 theory with 3 heavy substituted == nf=3 theory
lhs = -b0(6) * als / (8 * sp.pi) * G2 + 3 * svz
rhs = -b0(3) * als / (8 * sp.pi) * G2
chk("b0(6) + 3*(2/3) == b0(3) = 9 (heavy quarks rebuild the 3-flavour anomaly)",
    sp.simplify(lhs - rhs) == 0 and b0(3) == 9)
# nucleon: m_N = <-(9 a/8pi) G2> + f_l m_N  =>  X := <-(a/8pi) G2> = (1-f_l) m_N / 9
X = sp.symbols("X")
Xsol = sp.solve(sp.Eq(mN, 9 * X + fl * mN), X)[0]
fTQ = sp.simplify(sp.Rational(2, 3) * Xsol / mN)
chk("f_TQ = (2/3) X/m_N = (2/27)(1 - f_l)", sp.simplify(fTQ - sp.Rational(2, 27) * (1 - fl)) == 0,
    "-> %s" % fTQ)
# sequential decoupling c -> b -> t (Hill-Solon eq.(39) at O(alpha_s^0)): each is 2/27(1-f_l)
lam = fl
seq = []
for n in (3, 4, 5):
    fq = sp.Rational(1, 3) / b0(n) * (2 - 2 * lam)
    seq.append(sp.simplify(fq))
    lam = lam + fq
chk("sequential LO: f_c = f_b = f_t = (2/27)(1-f_l)",
    all(sp.simplify(q - sp.Rational(2, 27) * (1 - fl)) == 0 for q in seq))
csum = sp.simplify(lam)
chk("coupling sum f_l + sum f_TQ == 2/9 + (7/9) f_l",
    sp.simplify(csum - (sp.Rational(2, 9) + sp.Rational(7, 9) * fl)) == 0)
chk("tree's svz_heavy_sum 3*(2/27)(1-f_l) == 2/9 (1-f_l) exactly (Fraction)",
    3 * Fraction(2, 27) * (1 - Fraction(1, 10)) == Fraction(2, 9) * Fraction(9, 10))

print("\nB. THE TREE'S PRINTED NUMBERS from its READ inputs")
m_p, m_n = 938.272089, 939.565422          # massform MASS_MEV (READ there)
m_N = (m_p + m_n) / 2
FLAG = {"2+1+1": (60.9, 41.0, 6.5, 8.8), "2+1": (42.2, 44.9, 2.4, 6.4)}   # FLAG 2024 eqs.(447)-(450)
F = {k: (a + b) / m_N for k, (a, b, _, _) in FLAG.items()}
C = {k: 2 / 9 + 7 / 9 * f for k, f in F.items()}
for k in F:
    print("     %-6s f_l = %.5f  f_TQ(LO) = %.5f  coupling sum = %.5f" % (k, F[k], 2 / 27 * (1 - F[k]), C[k]))
chk("0.3066 (2+1+1)", round(C["2+1+1"], 4) == 0.3066)
chk("0.2944 (2+1)", round(C["2+1"], 4) == 0.2944)
nuc_over_M = 70.4755225591903 / 70.0      # massform payload_masses (nucleon rest / payload)
ele_over_M = 0.021071682153637385 / 70.0
allrows = ele_over_M + C["2+1+1"] * nuc_over_M
chk("largest all-rows share 0.3090 = electrons + 2+1+1 coupling x nucleon/payload",
    round(allrows, 4) == 0.3090, "(%.5f)" % allrows)
# Hoferichter eq.(24) inverted: 0.305 -> f_l = 0.1064 ; consistent
chk("Hoferichter 0.305(9) inverts to f_l = 0.1064 (within 2+1+1's)", abs((0.305 - 2 / 9) * 9 / 7 - 0.1064) < 1e-4)

print("\nC. BEYOND LEADING ORDER (Hill-Solon series, sibling-audit transcription)")
spec = importlib.util.spec_from_file_location("sib", os.path.join(HERE, "dlnlambdaqcd-dlnv-2-9.py"))
src = open(os.path.join(HERE, "dlnlambdaqcd-dlnv-2-9.py")).read()
# import only the function definitions (the sibling runs checks at top level): exec the defs
ns = {"math": math}
start = src.index("Z3 = 1.2020569031595942")
end = src.index("# eq.(120) coefficients")
exec(src[start:end], ns)
start2 = src.index("B = lambda nf:")
end2 = src.index("PDG = dict(")
exec(src[start2:end2], ns)
fQ_series, thresholds, total_f = ns["fQ_series"], ns["thresholds"], ns["total_f"]
al = thresholds(0.1180, 1.2730, 4.183, 162.5, 11 / 72)
print("     alpha^(4)(m_c)=%.4f alpha^(5)(m_b)=%.4f alpha^(6)(m_t)=%.4f (PDG-2024 inputs NAMED-NOT-READ)" % al)
chk("Hill-Solon eq.(61) reproduced: f_c(lambda=0.089) = 0.073(3)",
    abs(sum(fQ_series(3, 0.089, al[0] / math.pi)) - 0.073) <= 0.003)
beyond = {}
for k, f in F.items():
    for order, nm in enumerate(("LO", "NLO", "NNLO", "N3LO")):
        tot, fq = total_f(f, al, order)
        if nm in ("LO", "N3LO"):
            print("     %-6s %-5s f_c=%.5f f_b=%.5f f_t=%.5f  coupling sum=%.5f"
                  % (k, nm, fq[0], fq[1], fq[2], tot))
        beyond[(k, nm)] = (tot, fq)
    lo = beyond[(k, "LO")][0]
    hi = beyond[(k, "N3LO")][0]
    chk("%s: LO series reproduces 2/9 + 7/9 f_l" % k, abs(lo - C[k]) < 1e-12)
    chk("%s: beyond-LO shift of the coupling sum is + and < 5%%" % k, 0 < hi / lo - 1 < 0.05,
        "(%+.2f%%, %.4f -> %.4f)" % (100 * (hi / lo - 1), lo, hi))
    for i, q in enumerate("cbt"):
        r = beyond[(k, "N3LO")][1][i] / beyond[(k, "LO")][1][i] - 1
        print("       f_%s N3LO/LO - 1 = %+.2f%%" % (q, 100 * r))
fac = [(total_f(s, al, 3)[0] - s) / (1 - s) for s in (0.0, F["2+1"], F["2+1+1"])]
chk("beyond LO the (1 - f_l) factorisation fails (heavy/(1-f_l) not constant)",
    abs(fac[0] - fac[2]) > 1e-3, "%.5f %.5f %.5f vs 2/9=0.22222" % tuple(fac))
allrows_hi = ele_over_M + beyond[("2+1+1", "N3LO")][0] * nuc_over_M
print("     all-rows largest central reading: LO %.4f -> beyond-LO %.4f" % (allrows, allrows_hi))
t = fQ_series(3, F["2+1+1"], al[0] / math.pi)
print("     charm series terms: LO %.5f NLO %+.5f NNLO %+.5f N3LO %+.5f  (Hill-Solon: 'poorly convergent')" % tuple(t))

print("\nD. CHARM, NON-PERTURBATIVELY (ETM 19 via FLAG, READ by the tree)")
sc, dsc = 107.0, 22.0
fc_lat, dfc = sc / m_N, dsc / m_N
fc_lo = 2 / 27 * (1 - F["2+1+1"])
fc_hi = beyond[("2+1+1", "N3LO")][1][0]
print("     f_Tc: ETM19 %.4f(%.4f)  LO SVZ %.4f  Hill-Solon-series %.4f  RQCD16 0.075(4)" % (fc_lat, dfc, fc_lo, fc_hi))
z_lo = (fc_lat - fc_lo) / dfc
z_hi = (fc_lat - fc_hi) / dfc
chk("ETM19 sits above LO SVZ by < 3 sigma (a discrepancy, not a refutation)", 0 < z_lo < 3, "(%.2f sigma)" % z_lo)
chk("ETM19 vs beyond-LO series < 2 sigma", abs(z_hi) < 2, "(%.2f sigma)" % z_hi)
print("     ratio ETM19/LO = %.2f ; RQCD16 0.075(4) vs LO %.4f : %.2f sigma" % (fc_lat / fc_lo, fc_lo, (0.075 - fc_lo) / 0.004))

print("\nE. THE CONCLUSION: 'nothing near one half at first order'")
# the most generous: 2+1+1 f_l + 3 sigma, charm from ETM19 + 3 sigma, b and t beyond LO
fl_big = (60.9 + 3 * 6.5 + 41.0 + 3 * 8.8) / m_N
tot_big, fq_big = total_f(fl_big, al, 3)
gen = fl_big + (fc_lat + 3 * dfc) + fq_big[1] + fq_big[2]
print("     generous stack (f_l +3 sigma, ETM19 charm +3 sigma, b,t beyond LO): %.4f" % gen)
chk("even that stack stays below one half", gen < 0.5)

print("\n%d failures" % len(FAIL))
sys.exit(1 if FAIL else 0)
