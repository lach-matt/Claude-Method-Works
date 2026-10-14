"""DOCKET 67 -- re-derivation for Buttazzo, Degrassi, Giardino, Giudice, Sala,
Salvio, Strumia, 'Investigating the near-criticality of the Higgs boson',
arXiv:1307.3536v4 (22 Sep 2014).

SOURCE TEXT: src/1307.3536.pages.txt -- PDF pages 1-22, 24, 28-32, 34-36, 39
of v4 as returned by alphaXiv answer_pdf_queries in earlier stages of this
same session (recovered verbatim from the session's tool results; alphaXiv
quota was exhausted in this stage and arxiv.org is egress-blocked).
Every input below is quoted from that text with its PDF page:
  p.3   M_h = 125.15 +- 0.24 GeV
  p.19  eq.(64) M_h > 129.6 GeV + 2.0(M_t - 173.34 GeV) - 0.5 GeV (a3 - 0.1184)/0.0007 +- 0.3 GeV
        'The quoted uncertainty comes only from higher order perturbative corrections.'
  p.20  'take M_t = (173.34 +- 0.76_exp +- 0.3_th) GeV. Combining in quadrature
        theoretical uncertainties with experimental errors, we find
        M_h > (129.6 +- 1.5) GeV (stability condition). (65)  ... excluded at
        2.8 sigma (99.8% C.L. one-sided).'
  p.20  eq.(66) M_t < (171.53 +- 0.15 +- 0.23_a3 +- 0.15_Mh) GeV = (171.53 +- 0.42) GeV
        'we combined in quadrature the theoretical uncertainty with the
        experimental uncertainties on M_h and a3.'
  p.20  eq.(67) log10(Lambda_V/GeV) = 9.5 + 0.7(M_h-125.15) - 1.0(M_t-173.34) + 0.3 da3;
        Lambda_lambda ~ 2 Lambda_V (MSbar); Lambda_I ~ 13 Lambda_V (Landau gauge)
  p.31  'metastability is now preferred at 99.3% CL'
  p.32  'We find Lambda_I = 10^10-10^12 GeV, see eq. (67)'
  alpha_3(M_Z) = 0.1184 +- 0.0007 (p.19 Fig.3 caption; eqs.(60),(61)).
CURRENT inputs (PDG 2024) as READ in arXiv:2401.08811v4 Table I (cached
alphaXiv page 4, src/2401.08811.pages.txt): M_h 125.20(11), M_t^sigma
172.4(7), M_t^MC 172.57(29), alpha_s 0.1180(9).
Andreassen-Frost-Schwartz arXiv:1707.08124v4 p.50-51 (cached page text):
m_t,crit = 171.18 (+0.17 -0.35 th) at m_h 125.09, a_s 0.1181; 'Absolute
stability is currently excluded at 2.48 sigma ... one-sided confidence of 99.3%'.

A computed disagreement with a printed number is RECORDED as a DISCREPANCY
(fluctuation.py precedent), never as a refutation.  stdlib only.
"""
import math

FAIL = []
DISC = []


def chk(label, cond):
    print("  %-4s %s" % ("PASS" if cond else "FAIL", label))
    if not cond:
        FAIL.append(label)


def rec(label, val, fmt="%.4g"):
    print("  REC  %-78s " % label + fmt % val)


def disc(label):
    print("  DISC %s" % label)
    DISC.append(label)


def Phi(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def z_of(p):
    lo, hi = -10.0, 10.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        lo, hi = (m, hi) if Phi(m) < p else (lo, m)
    return 0.5 * (lo + hi)


MH, SMH = 125.15, 0.24
MT, SMT_EXP, SMT_TH = 173.34, 0.76, 0.3
A3, SA3 = 0.1184, 0.0007


def mh_crit(mt, a3):                        # eq.(64), central
    return 129.6 + 2.0 * (mt - 173.34) - 0.5 * (a3 - 0.1184) / 0.0007


print("C1  eq.(65) error budget from the components the text names (p.19-20)")
s_mt_exp = 2.0 * SMT_EXP
s_mt_all = 2.0 * math.hypot(SMT_EXP, SMT_TH)
s_a3 = 0.5
s_th = 0.3
full = math.sqrt(s_mt_all ** 2 + s_a3 ** 2 + s_th ** 2)
no_mtth = math.sqrt(s_mt_exp ** 2 + s_a3 ** 2 + s_th ** 2)
rec("2.0 x 0.76 (M_t exp alone)", s_mt_exp, "%.3f")
rec("quadrature of 2.0(0.76+0.3), 0.5 (a3), 0.3 (th, eq.64)", full, "%.3f")
rec("quadrature without the 0.3 top-mass theory error", no_mtth, "%.3f")
chk("printed +-1.5 reproduces only as 2.0 x 0.76 (|1.52-1.5| < 0.05)", abs(s_mt_exp - 1.5) < 0.05)
if abs(full - 1.5) > 0.1:
    disc("eq.(65): the stated quadrature of the named components gives +-%.2f (or +-%.2f "
         "without the 0.3 top theory error), not the printed +-1.5" % (full, no_mtth))

print("C2  '2.8 sigma (99.8% C.L. one-sided)' (p.20)")
d = 129.6 - MH
z_print = d / math.hypot(1.5, SMH)
z_full = d / math.hypot(full, SMH)
rec("z with printed +-1.5 and dM_h 0.24", z_print, "%.3f")
rec("z with the full stated budget", z_full, "%.3f")
rec("one-sided CL of 2.8 sigma, %", 100 * Phi(2.8), "%.3f")
rec("sigma of one-sided 99.8%", z_of(0.998), "%.3f")
chk("every reading excludes stability at > 2.5 sigma (conclusion robust)", min(z_print, z_full) > 2.5)
disc("2.8 sigma is 99.74%% one-sided (rounds to 99.7, printed 99.8%%); "
     "recomputed z = %.2f (printed budget) or %.2f (full budget) brackets 2.8" % (z_print, z_full))

print("C3  eq.(66) vs eq.(64) inverted (p.20 'We can express the stability condition of eq.(64) as')")
mtc_inv = 173.34 + (MH - 129.6) / 2.0
rec("eq.(64) inverted at M_h = 125.15, a3 = 0.1184: M_t,crit", mtc_inv, "%.3f")
rec("printed eq.(66) central", 171.53, "%.2f")
rec("difference, GeV", 171.53 - mtc_inv, "%.3f")
comps = math.sqrt(0.15 ** 2 + 0.23 ** 2 + 0.15 ** 2)
comps_mtth = math.sqrt(0.15 ** 2 + 0.23 ** 2 + 0.15 ** 2 + 0.3 ** 2)
rec("quadrature of 0.15, 0.23, 0.15 (the three printed components)", comps, "%.3f")
rec("... plus the 0.3 top-mass theory error of p.20", comps_mtth, "%.3f")
chk("component sizes follow eq.(64): 0.3/2 = 0.15, 0.5/2 = 0.25 ~ 0.23, 0.24/2 = 0.12 ~ 0.15",
    abs(0.3 / 2 - 0.15) < 1e-9 and abs(0.25 - 0.23) < 0.03 and abs(0.12 - 0.15) < 0.04)
disc("eq.(66) central 171.53 is %.2f GeV above eq.(64) inverted (%.2f); the linear eq.(64) is "
     "stated only 'in the neighbourhood of the measured values' and 171.5 lies 1.8 GeV away, "
     "so a curvature of the boundary is a possible cause -- NOT computed here" % (171.53 - mtc_inv, mtc_inv))
disc("eq.(66) +-0.42 is not the quadrature of its three printed components (%.2f); "
     "it reproduces (%.2f) only if the 0.3 GeV top theory error is added" % (comps, comps_mtth))
rec("AFS 1707.08124 m_t,crit (m_h 125.09, a_s 0.1181), for comparison", 171.18, "%.2f")

print("C4  top mass against the bound, THEN (p.20 inputs)")
for lab, mtc, smtc in (("eq.(66) 171.53 +- 0.42", 171.53, 0.42),
                       ("eq.(64) inverted %.2f +- %.2f" % (mtc_inv, comps), mtc_inv, comps)):
    z = (MT - mtc) / math.hypot(SMT_EXP, smtc)
    rec("THEN (173.34 +- 0.76) vs %s: z" % lab, z, "%.3f")
    chk("THEN metastability side (z > 0) for %s" % lab, z > 0)
rec("sigma of the p.31 '99.3% CL' (one-sided)", z_of(0.993), "%.3f")

print("C5  NOW: eq.(64)/(66) linearisation at PDG 2024 (as READ in 2401.08811 Table I)")
MH_N, SMH_N, A3_N, SA3_N = 125.20, 0.11, 0.1180, 0.0009
res = {}
for lab, mt, smt in (("M_t^MC 172.57(29)", 172.57, 0.29), ("M_t^sigma 172.4(7)", 172.4, 0.7)):
    mhc = mh_crit(mt, A3_N)
    s = math.sqrt((2.0 * math.hypot(smt, SMT_TH)) ** 2 + (0.5 * SA3_N / 0.0007) ** 2 + 0.3 ** 2)
    z = (mhc - MH_N) / math.hypot(s, SMH_N)
    res[lab] = z
    rec("%s: M_h,crit (eq.64)" % lab, mhc, "%.3f")
    rec("%s: z = (M_h,crit - 125.20)/sigma [sigma incl. 0.3 top th]" % lab, z, "%.3f")
    chk("%s: still on the metastable side (z > 0)" % lab, z > 0)
mtc_now = 171.53 + 0.5 * (MH_N - 125.15) + 0.25 * (A3_N - 0.1184) / 0.0007
rec("eq.(66) shifted to today's M_h, a_s (eq.64 slopes): M_t,crit", mtc_now, "%.3f")
rec("Hiller 2401.08811 full analysis M_t,crit (alpha_lambda,eff > 0)", 171.10, "%.2f")
chk("the 'preferred, not established' status holds under both top masses "
    "(z between 1 and 4 sigma, never > 5)", all(1.0 < z < 4.0 for z in res.values()))
rec("spread of z between the two top-mass definitions", abs(res["M_t^MC 172.57(29)"] - res["M_t^sigma 172.4(7)"]), "%.3f")

print("C6  eq.(67): Lambda_I in '10^10-10^12' then and now (Landau gauge, Lambda_I ~ 13 Lambda_V)")
def log10_LI(mh, mt, a3):
    return 9.5 + 0.7 * (mh - 125.15) - 1.0 * (mt - 173.34) + 0.3 * (a3 - 0.1184) / 0.0007 + math.log10(13.0)
for lab, args in (("THEN central", (MH, MT, A3)),
                  ("NOW M_t^MC", (MH_N, 172.57, A3_N)),
                  ("NOW M_t^sigma", (MH_N, 172.4, A3_N))):
    L = log10_LI(*args)
    rec("%s: log10 Lambda_I  (log10 Lambda_V = %.2f)" % (lab, L - math.log10(13)), L, "%.3f")
    chk("%s inside 10^10-10^12" % lab, 10.0 <= L <= 12.0)

print("C7  the tree's case split (massform.field_supplies_mass_energy = rel or (metastable and dec))")
def fsme(metastable, rel=False, dec=False):
    return rel or (metastable and dec)
chk("C4 identical for stable and metastable at rel = dec = False", fsme(False) == fsme(True))
chk("C4 in the metastable case flips if dec = True: the INFERENCE (decay forms no mass "
    "at the seat) is load-bearing, the top mass is not", fsme(True, dec=True) != fsme(True))

print()
print("DISCREPANCIES RECORDED (not refutations): %d" % len(DISC))
print("ALL PASS" if not FAIL else "FAILURES: %s" % FAIL)
raise SystemExit(1 if FAIL else 0)
