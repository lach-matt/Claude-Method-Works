"""DOCKET 67 -- feynman-hellmann-sigma-term.

The tree (address.py:99-104, 504-515, 816-822):
    m_p = Lambda f(m_q/Lambda)  =>  d ln m_p/d ln Lambda = 1 - S,  S = sum_q sigma_q/m_p
    H1 (alpha_s fixed high):  d ln m_p/d ln v = 2/9 + (7/9) S
    H2 (Lambda fixed):        d ln m_p/d ln v = S
    K_mu = d ln m_p/d ln v - 1

Checks, each printed PASS/FAIL; exit 1 on any FAIL.
  A  Euler / dimensional homogeneity, sympy, generic f of three ratios.
  B  Feynman-Hellmann, sympy, exact 2x2 Hermitian family (isolated level).
  C  UNSTATED hypothesis: WHICH quark mass is held fixed.  At fixed RG-invariant
     mass the coefficient is 1 - S; at fixed m_q(mu0) with mu0 fixed in GeV it is
     1 - S(1 + gamma_m(mu0)).  sympy, generic f and generic running c(mu/Lambda).
  D  Full-theory identity: with Lambda_6 fixed and every MSbar mass prop. to v,
     d ln m_p/d ln v = sum_{q=u..t} f_q EXACTLY (QCD only) -- Hoferichter 2015
     eq.(24)'s left side; one-loop matching Lambda_3 = Lambda_6^(7/9)(m_c m_b m_t)^(2/27)
     plus SVZ-LO gives 2/9 + 7S/9.  Tree's printed numbers reproduced, and
     address.py's own functions called (read-only import, no bytecode written).
  E  Coc et al. 2007 eq.(11) (astro-ph/0610733, cached arXiv text): 0.76 dLambda/Lambda
     + 0.24 (dh/h + dv/v): homogeneity (coefficients sum to 1) and the 0.24's
     make-up 0.19 (strange) + 0.052 (u,d); moved data -> today's S_uds.
  F  Sign robustness: K_mu < 0 for all S in [0,1) under H1 and H2 (sympy).
  G  Beyond LO (sibling rederive/dlnlambdaqcd-dlnv-2-9.py, Hill-Solon 1409.8290
     transcription through O(alpha_s^3)): effect on every rests_on_it quantity,
     by calling address.py's functions with d ln m_p/d ln v replaced.
"""
import sys, os, re, subprocess
from fractions import Fraction as Fr
import sympy as sp

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, TREE)

fails = []
def chk(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (("  -- " + detail) if detail else ""))
    if not cond:
        fails.append(name)

# ---------------------------------------------------------------- A  Euler
print("\nA. DIMENSIONAL HOMOGENEITY (Euler), sympy")
L, mu_, md_, ms_ = sp.symbols("Lambda m_u m_d m_s", positive=True)
f = sp.Function("f")
mp = L * f(mu_ / L, md_ / L, ms_ / L)
euler = sp.simplify(L * sp.diff(mp, L) + sum(m * sp.diff(mp, m) for m in (mu_, md_, ms_)) - mp)
chk("Lambda dm_p/dLambda + sum m_q dm_p/dm_q - m_p == 0 for generic f", euler == 0, str(euler))
S_expr = sum(m * sp.diff(mp, m) for m in (mu_, md_, ms_)) / mp          # sum sigma_q / m_p (FH)
dlnL = sp.simplify(L * sp.diff(mp, L) / mp - (1 - S_expr))
chk("d ln m_p/d ln Lambda |_(m_q fixed) == 1 - S", dlnL == 0)

# ---------------------------------------------------------------- B  FH
print("\nB. FEYNMAN-HELLMANN, exact 2x2 Hermitian family")
a, b, c, lam = sp.symbols("a b c lambda", real=True)
H = sp.Matrix([[a + lam, c], [c, b]])
E0 = (a + lam + b) / 2 - sp.sqrt(((a + lam - b) / 2) ** 2 + c ** 2)     # lower level
# normalized eigenvector of E0
v = sp.Matrix([c, E0 - (a + lam)])
v = v / sp.sqrt((v.T * v)[0])
dH = sp.diff(H, lam)
lhs = sp.diff(E0, lam)
rhs = sp.simplify((v.T * dH * v)[0])
num = [(1.3, -0.4, 0.7, 0.2), (0.0, 2.0, 0.05, -0.3), (5.0, 1.0, 3.0, 1.1)]
okB = all(abs(float((lhs - rhs).subs({a: A, b: B, c: C, lam: l}))) < 1e-12 for A, B, C, l in num)
chk("dE0/dlambda == <psi0|dH/dlambda|psi0> (isolated level, c != 0)", okB)

# ---------------------------------------------------------------- C  which mass is fixed
print("\nC. UNSTATED HYPOTHESIS: which quark mass is held fixed when Lambda moves")
mh, mu0 = sp.symbols("mhat mu0", positive=True)
g = sp.Function("g"); cfun = sp.Function("c")
# one light mass suffices: m_p = Lambda g(mhat/Lambda), mhat RG-invariant
mpC = L * g(mh / L)
SC = mh * sp.diff(mpC, mh) / mpC
# MSbar mass at a FIXED scale mu0: m(mu0) = mhat c(mu0/Lambda); gamma_m = -dln c/dln mu
m0 = sp.Symbol("m0", positive=True)
mh_of = m0 / cfun(mu0 / L)                    # mhat as function of Lambda at fixed m(mu0)=m0
total = sp.diff(L * g(mh_of / L), L) * L / (L * g(mh_of / L))
x = sp.Symbol("x", positive=True)
gamma_m = -(x * sp.diff(cfun(x), x) / cfun(x)).subs(x, mu0 / L)
SC_sub = SC.subs(mh, mh_of)
diffC = sp.simplify(total - (1 - SC_sub * (1 + gamma_m)))
chk("at fixed m_q(mu0): d ln m_p/d ln Lambda == 1 - S (1 + gamma_m(mu0))", diffC == 0, str(diffC))
# numbers: alpha_s(2 GeV) ~ 0.30 (NAMED-NOT-READ), LO gamma_m = 2 alpha_s/pi
a2 = 0.30
gm = 2 * a2 / 3.141592653589793
for Sv in (0.06, 0.1086):
    print("     S = %.4f: at fixed mhat 1 - S = %.4f; at fixed m(2 GeV) 1 - S(1+gamma_m) = %.4f (gamma_m ~ %.3f LO)"
          % (Sv, 1 - Sv, 1 - Sv * (1 + gm), gm))
chk("the difference is O(S alpha_s) (< 0.03 at S <= 0.11)", 0.1086 * gm < 0.03)

# ---------------------------------------------------------------- D  H1 / H2
print("\nD. H1 / H2 COMPOSITION")
def b0(nf): return Fr(11) - Fr(2, 3) * nf
# one-loop continuous matching at mu = m_Q: Lambda_lo^b_lo = Lambda_hi^b_hi m^(b_lo - b_hi)
lnL6, lnmt, lnmb, lnmc = sp.symbols("lnL6 lnmt lnmb lnmc")
lnL5 = (b0(6) * lnL6 + (b0(5) - b0(6)) * lnmt) / b0(5)
lnL4 = (b0(5) * lnL5 + (b0(4) - b0(5)) * lnmb) / b0(4)
lnL3 = sp.expand((b0(4) * lnL4 + (b0(3) - b0(4)) * lnmc) / b0(3))
co = {s: sp.nsimplify(lnL3.coeff(s)) for s in (lnL6, lnmt, lnmb, lnmc)}
chk("Lambda_3 = Lambda_6^(7/9) (m_c m_b m_t)^(2/27)",
    co[lnL6] == sp.Rational(7, 9) and all(co[s] == sp.Rational(2, 27) for s in (lnmt, lnmb, lnmc)), str(co))
dLdv = co[lnmt] + co[lnmb] + co[lnmc]
chk("d ln Lambda_3/d ln v = 2/9 (every heavy mass prop. to v, Lambda_6 fixed)", dLdv == sp.Rational(2, 9))
S = sp.Symbol("S")
fH1 = sp.expand(dLdv * (1 - S) + S)          # homogeneity step A with m_q prop. to v
chk("H1: (2/9)(1 - S) + S == 2/9 + 7S/9", sp.simplify(fH1 - (sp.Rational(2, 9) + sp.Rational(7, 9) * S)) == 0)
# independent route: SVZ LO f_Q = 2/27 (1 - S) for each heavy quark, iterated c->b->t
fQ = [sp.Rational(2, 27) * (1 - S)] * 3
chk("SVZ-LO route: S + sum_{c,b,t} f_Q == 2/9 + 7S/9 (Hoferichter eq.(24) form)",
    sp.simplify(S + sum(fQ) - fH1) == 0)
# full-theory Euler: m_p = Lambda_6 F(m_i/Lambda_6), all six m_i prop. to v, Lambda_6 fixed
ms6 = sp.symbols("m1:7", positive=True); t = sp.Symbol("t", positive=True); L6 = sp.Symbol("L6", positive=True)
F6 = sp.Function("F")
mp6 = L6 * F6(*[m / L6 for m in ms6])
d_v = sp.diff(mp6.subs({m: t * m for m in ms6}, simultaneous=True), t).subs(t, 1) / mp6
sig6 = sum(m * sp.diff(mp6, m) for m in ms6) / mp6
chk("full theory: d ln m_p/d ln v == sum_{q=u..t} sigma_q/m_p EXACTLY (QCD only)", sp.simplify(d_v - sig6) == 0)
# Hoferichter eq.(24) inverted
S_hof = sp.solve(sp.Rational(2, 9) + sp.Rational(7, 9) * S - sp.Rational(305, 1000), S)[0]
print("     Hoferichter 2015 eq.(24) 0.305(9) inverts to S_uds = %.4f" % float(S_hof))
chk("inverted S_uds = 0.1064", abs(float(S_hof) - 0.1064) < 5e-5)

# tree numbers
# address.py:106 prints "0.229": 0.22969 TRUNCATES to 0.229 and ROUNDS to 0.230 -- a
# last-digit discrepancy of presentation, recorded, not an error (check is on truncation)
v229 = float(fH1.subs(S, 0.0096))
chk("tree prints 'H1 gives 0.229' = TRUNCATION of %.5f (rounds to %.3f: discrepancy recorded)" % (v229, v229),
    int(v229 * 1000) == 229 and round(v229, 3) == 0.230)
printed = {
           "'TWENTY-FOUR TIMES'": (float(fH1.subs(S, 0.0096)) / 0.0096, 24.0, 0.1),
           "K_mu H1 S=0.0096 -0.7703": (float(fH1.subs(S, 0.0096)) - 1, -0.7703, 5e-5),
           "K_mu H2 S=0.0096 -0.9904": (0.0096 - 1, -0.9904, 5e-5),
           "K_mu H1 S=0.06 -0.7311": (float(fH1.subs(S, 0.06)) - 1, -0.7311, 5e-5),
           "K_mu H2 S=0.06 -0.9400": (0.06 - 1, -0.9400, 5e-5),
           "f H1 S=0.06 0.268889": (float(fH1.subs(S, 0.06)), 0.268889, 5e-7),
           "F6 4.48 at S=0.06": (float(fH1.subs(S, 0.06)) / 0.06, 4.48, 5e-3),
           "F6 3.25 at S=0.09": (float(fH1.subs(S, 0.09)) / 0.09, 3.25, 5e-3)}
for k, (got, want, tol) in printed.items():
    chk("tree prints " + k, abs(got - want) <= tol, "%.6f" % got)
# the tree's valence S = 0.0096 -> 24.0 exactly as printed at address.py:80
import address as A
chk("address.dln_lambda_dln_v() == Fraction(2,9)", A.dln_lambda_dln_v() == Fr(2, 9))
for Sv in (A.S_SCAN[0][1], 0.06, 0.09):
    chk("address.dln_mp_dln_v(%.4f,'H1') == 2/9 + 7S/9" % Sv, abs(float(A.dln_mp_dln_v(Sv, "H1")) - (2/9 + 7*Sv/9)) < 1e-15)
    chk("address.K_mu(%.4f,'H2') == S - 1" % Sv, abs(float(A.K_mu(Sv, "H2")) - (Sv - 1)) < 1e-15)
print("     tree NAIVE_CORRECTION_FACTOR:", {k: round(v, 4) for k, v in A.NAIVE_CORRECTION_FACTOR.items()})

# ---------------------------------------------------------------- E  Coc 2007 eq.(11)
print("\nE. COC et al. 2007 eq.(11): 0.76 dLambda/Lambda + 0.24 (dh/h + dv/v)")
chk("homogeneity: 0.76 + 0.24 == 1", abs(0.76 + 0.24 - 1) < 1e-12)
chk("0.24 = 0.19 (strange, B_s=1.5) + 0.052 (u,d) to rounding", abs(0.19 + 0.052 - 0.24) < 0.005, "%.3f" % (0.19 + 0.052))
MP = 938.272
now = {"FLAG24 2+1": (42.2 + 44.9) / MP, "FLAG24 2+1+1": (60.9 + 41.0) / MP,
       "pheno 59.1 + FLAG 2+1 sigma_s": (59.1 + 44.9) / MP, "Hoferichter eq.(24) inverted": float(S_hof)}
for k, Sv in now.items():
    print("     S_uds %-32s = %.4f -> Coc's coefficient of dLambda/Lambda would be %.3f (published 0.76)" % (k, Sv, 1 - Sv))
print("     Coc S = 0.24: K_mu H1 = %.4f, H2 = %.4f  |  today S = 0.1086: H1 = %.4f, H2 = %.4f"
      % (float(fH1.subs(S, 0.24)) - 1, 0.24 - 1, float(fH1.subs(S, 0.1086)) - 1, 0.1086 - 1))
chk("Coc's 0.24 exceeds every current S_uds by > 2x (the strange content moved)", all(0.24 / v > 2.1 for v in now.values()))

# ---------------------------------------------------------------- F  sign robustness
print("\nF. SIGN ROBUSTNESS of K_mu")
KH1 = sp.simplify(fH1 - 1); KH2 = S - 1
chk("K_mu(H1) = -7(1-S)/9", sp.simplify(KH1 + sp.Rational(7, 9) * (1 - S)) == 0)
setH1 = sp.solve_univariate_inequality(KH1 < 0, S, relational=False)
setH2 = sp.solve_univariate_inequality(KH2 < 0, S, relational=False)
chk("K_mu(H1) < 0 exactly on S < 1", setH1 == sp.Interval.open(-sp.oo, 1), str(setH1))
chk("K_mu(H2) < 0 exactly on S < 1", setH2 == sp.Interval.open(-sp.oo, 1), str(setH2))
chk("|K_mu(H2)/K_mu(H1)| = 9/7 for every S < 1 (the two hypotheses agree to a factor 9/7)",
    sp.simplify(KH2 / KH1 - sp.Rational(9, 7)) == 0)

# ---------------------------------------------------------------- G  beyond LO
print("\nG. BEYOND LO (Hill-Solon through O(alpha_s^3), sibling script re-run here)")
out = subprocess.run([sys.executable, "-B", os.path.join(HERE, "dlnlambdaqcd-dlnv-2-9.py")],
                     capture_output=True, text=True, timeout=300).stdout
rows = re.findall(r"S=([0-9.]+)\s+f_LO=([0-9.]+)\s+f_N3LO=([0-9.]+)", out)
tab = sorted((float(s), float(lo), float(n3)) for s, lo, n3 in rows)
chk("sibling script ran and printed its S table", len(tab) >= 4 and "0 failures" in out, "%d rows" % len(tab))
def f_n3lo(Sv):
    for (s0, _, y0), (s1, _, y1) in zip(tab, tab[1:]):
        if s0 <= Sv <= s1:
            return y0 + (y1 - y0) * (Sv - s0) / (s1 - s0)
    (s0, _, y0), (s1, _, y1) = (tab[0], tab[1]) if Sv < tab[0][0] else (tab[-2], tab[-1])
    return y0 + (y1 - y0) * (Sv - s0) / (s1 - s0)      # linear extrapolation at the ends
orig = A.dln_mp_dln_v
base = {"higgs_fraction H1": A.higgs_fraction(0.06, "H1"), "K_mu H1": float(A.K_mu(0.06, "H1")),
        "eps_det_stationary H1": A.eps_det_stationary("H1"),
        "EPS_NUCLEAR H1": A.EPS_NUCLEAR["H1"], "EPS_NUCLEAR_OVER_DET H1": A.EPS_NUCLEAR_OVER_DET["H1"],
        "COURIER_SOURCE_KG_M3 H1": A.COURIER_SOURCE_KG_M3["H1"],
        "NAIVE 0.0096": A.naive_correction_factor(A.S_SCAN[0][1]), "NAIVE 0.06": A.naive_correction_factor(0.06),
        "NAIVE 0.09": A.naive_correction_factor(0.09)}
def patched(Sv, h):
    return f_n3lo(Sv) if h == "H1" else orig(Sv, h)
A.dln_mp_dln_v = patched
try:
    new = {"higgs_fraction H1": A.higgs_fraction(0.06, "H1"), "K_mu H1": float(A.K_mu(0.06, "H1")),
           "eps_det_stationary H1": A.eps_det_stationary("H1"),
           "EPS_NUCLEAR H1": A.eps_from_matter(A.RHO_NUCLEAR, A.higgs_fraction(0.06, "H1")),
           "COURIER_SOURCE_KG_M3 H1": A.source_density(A.eps_detectable_transported(1e-18), A.higgs_fraction(0.06, "H1"))[0],
           "NAIVE 0.0096": A.naive_correction_factor(A.S_SCAN[0][1]), "NAIVE 0.06": A.naive_correction_factor(0.06),
           "NAIVE 0.09": A.naive_correction_factor(0.09)}
    new["EPS_NUCLEAR_OVER_DET H1"] = abs(new["EPS_NUCLEAR H1"]) / new["eps_det_stationary H1"]
finally:
    A.dln_mp_dln_v = orig
G = {}
for k in base:
    G[k] = (base[k], new[k], new[k] / base[k])
    print("     %-26s LO %-12.5g N3LO %-12.5g ratio %.4f" % (k, base[k], new[k], new[k] / base[k]))
chk("no sign flips in any rests_on_it quantity", all(v[0] * v[1] > 0 for v in G.values()))
chk("every rests_on_it quantity moves < 8% except NAIVE_CORRECTION_FACTOR at the valence row",
    all(abs(v[2] - 1) < 0.08 for k, v in G.items() if k != "NAIVE 0.0096"))
chk("EPS_NUCLEAR_OVER_DET H1 stays > 100 (nuclear eps two orders over threshold)", G["EPS_NUCLEAR_OVER_DET H1"][1] > 100)

print("\n%d failures" % len(fails))
sys.exit(1 if fails else 0)
