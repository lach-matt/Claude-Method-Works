#!/usr/bin/env python3
"""DOCKET 67, audit dlnlambdaqcd-dlnv-2-9.

Re-derives, independently of address.py, the one-loop threshold relation

    Lambda_3 = Lambda_6^(7/9) (m_c m_b m_t)^(2/27)       [Coc et al. 2007, eq. (13)]
    d ln Lambda_3 / d ln v = 3 * 2/27 = 2/9               [Coc et al. 2007, eq. (14), Delta alpha = 0]

and the tree's H1 composition f = d ln m_p / d ln v = S + (2/9)(1 - S) = 2/9 + 7S/9,
K_mu = f - 1 = 7(S - 1)/9.

Then asks how large the correction BEYOND leading order is, using the EXACT
statement  d ln m_N / d ln v |_{alpha_s(mu0), y_q(mu0) fixed} = sum_q f_q
(Feynman-Hellmann + Euler homogeneity, QCD only), with the heavy-quark
f_Q = m_Q <N|QbarQ|N>/m_N taken from Hill & Solon 1409.8290 eq. (39), (119), (120),
READ at source.  The LO of that series is SVZ's 2/27 (1 - lambda) per heavy quark,
i.e. exactly the tree's 2/9 + 7S/9.

Inputs NOT read at source in this stage (PDG 2024 values, NAMED-NOT-READ):
alpha_s(M_Z) = 0.1180(9), M_Z = 91.1876, m_c(m_c) = 1.2730, m_b(m_b) = 4.183,
m_t(m_t) [MSbar] = 162.5 GeV.  They enter ONLY the size of the beyond-LO correction,
and a scan shows the conclusion does not move over their ranges.
Three-loop decoupling constant c2 = 11/72 (CKS hep-ph/9708255, NAMED-NOT-READ):
run with +11/72, 0, -11/72 to show it is immaterial.

Exit 0 iff every check passes.  stdlib + sympy.
"""
import math
import sys
import sympy as sp

FAIL = []


def chk(name, got, want, tol=None):
    ok = (got == want) if tol is None else abs(got - want) <= tol
    print("%-4s %s : got %s want %s" % ("ok" if ok else "FAIL", name, got, want))
    if not ok:
        FAIL.append(name)


print("1. ONE-LOOP THRESHOLD CHAIN, symbolic")
L6, mc, mb, mt, mu, als, v = sp.symbols("Lambda6 m_c m_b m_t mu alpha_s v", positive=True)
b0 = lambda nf: sp.Rational(11) - sp.Rational(2, 3) * nf
# 1/alpha(mu) = (b0/(2 pi)) ln(mu/Lambda); continuity at mu = m_Q:
#   b_hi ln(m/L_hi) = b_lo ln(m/L_lo)  =>  ln L_lo = (1 - b_hi/b_lo) ln m + (b_hi/b_lo) ln L_hi
lnL = sp.log(L6)
for nf, m in ((6, mt), (5, mb), (4, mc)):
    lnL = sp.expand((1 - b0(nf) / b0(nf - 1)) * sp.log(m) + (b0(nf) / b0(nf - 1)) * lnL)
lnL3 = sp.expand(lnL)
coef = {s: sp.nsimplify(sp.diff(lnL3, sp.log(s)) if False else sp.diff(lnL3, s) * s)
        for s in (L6, mc, mb, mt)}
chk("power of Lambda_6", coef[L6], sp.Rational(7, 9))
for s in (mc, mb, mt):
    chk("power of %s" % s, coef[s], sp.Rational(2, 27))
chk("mass dimension closes (7/9 + 3*2/27)", coef[L6] + coef[mc] + coef[mb] + coef[mt], 1)
# every heavy mass = y v/sqrt2 at fixed Yukawa, Lambda_6 fixed (H1: alpha_s fixed above m_t)
y = sp.symbols("y_c y_b y_t", positive=True)
sub = {mc: y[0] * v, mb: y[1] * v, mt: y[2] * v}
dlnL = sp.simplify(v * sp.diff(lnL3.subs(sub), v))
chk("d ln Lambda_3 / d ln v", dlnL, sp.Rational(2, 9))
# stopping after the top only
lnL5 = sp.expand((1 - b0(6) / b0(5)) * sp.log(mt) + (b0(6) / b0(5)) * sp.log(L6))
chk("top alone, Lambda_5: exponent 2/23 (not 2/27)", sp.diff(lnL5, mt) * mt, sp.Rational(2, 23))
# Coc et al. eq. (13): Lambda = mu (m_c m_b m_t / mu^3)^(2/27) exp(-2 pi/(9 alpha_s(mu))), mu > m_t
# with Lambda_6 = mu exp(-2 pi/(b0(6) alpha_s(mu))) -- identical to the chain:
coc13 = sp.log(mu) + sp.Rational(2, 27) * (sp.log(mc) + sp.log(mb) + sp.log(mt) - 3 * sp.log(mu)) \
    - 2 * sp.pi / (9 * als)
chain = lnL3.subs(L6, mu * sp.exp(-2 * sp.pi / (b0(6) * als)))
chk("Coc et al. eq.(13) == one-loop chain", sp.simplify(sp.expand_log(chain - coc13, force=True)), 0)
# Coc eq. (14) with Delta alpha = 0 and all Delta h = 0: dlnLambda = (2/27) * 3 dlnv
chk("Coc eq.(14) coefficient of dln v: (2/27)*3", sp.Rational(2, 27) * 3, sp.Rational(2, 9))

print("\n2. THE TREE'S H1 COMPOSITION and SVZ's heavy-quark theorem (independent route)")
S = sp.symbols("S")
f_tree = sp.Rational(2, 9) * (1 - S) + S
chk("f = 2/9 + 7S/9", sp.expand(f_tree - (sp.Rational(2, 9) + sp.Rational(7, 9) * S)), 0)
chk("K_mu = f - 1 = 7(S-1)/9", sp.expand(f_tree - 1 - sp.Rational(7, 9) * (S - 1)), 0)
chk("f(S=0.06)", float(f_tree.subs(S, sp.Rational(6, 100))), 0.268889, 1e-6)
chk("K_mu(S=0.06)", float(f_tree.subs(S, sp.Rational(6, 100)) - 1), -0.731111, 1e-6)
# SVZ / Hill-Solon eq.(39) LO: f_Q = (1/(3 b0(nf))) (2 - 2 lambda_nf), iterated c -> b -> t
lam = S
fQ_LO = []
for nf in (3, 4, 5):
    fq = sp.Rational(1, 3) / b0(nf) * (2 - 2 * lam)
    fQ_LO.append(sp.factor(fq))
    lam = lam + fq
for name, fq in zip(("c", "b", "t"), fQ_LO):
    chk("SVZ LO f_%s = 2/27 (1 - S)" % name, sp.simplify(fq - sp.Rational(2, 27) * (1 - S)), 0)
chk("S + sum f_Q (LO) == tree's 2/9 + 7S/9", sp.simplify(lam - f_tree), 0)

print("\n3. HILL-SOLON 1409.8290 eq.(39) transcription, checked against their eq.(120) and (61)")
Z3 = 1.2020569031595942


def fQ_series(nf, lam, a):
    """f_Q in the (nf+1) theory at mu_Q = m_Q (logs vanish); a = alpha^(nf+1)(m_Q)/pi.
    Returns the list of contributions [LO, NLO, NNLO, N3LO]."""
    k = 1.0 / (3.0 * (11 - 2.0 * nf / 3))
    lo = k * (2 - 2 * lam)
    nlo = a * k ** 2 * (57 / 2 - 321 * lam / 2 + 8 * nf)
    nnlo = a ** 2 * k ** 3 * (9145 / 8 - 90985 * lam / 8
                              + nf * (374 / 3 + 1420 * lam / 3)
                              + nf ** 2 * (7661 / 144 - 7469 * lam / 144)
                              + nf ** 3 * (-77 / 72 + 77 * lam / 72))
    # eq.(119), non-log terms only (mu_Q = m_Q, MSbar mass)
    o4 = (-2387203071 * Z3 / 512 * lam + 3852721945 / 768 * lam + 3399188991 * Z3 / 512
          - 6064085209 / 768
          + nf * (181905471 * Z3 / 128 * lam - 36859013 / 32 * lam - 227904831 * Z3 / 128
                  + 195412223 / 96)
          + nf ** 2 * (-147631 * lam * Z3 + 51820165 / 576 * lam + 169411 * Z3 - 120231661 / 576)
          + nf ** 3 * (1839305 * Z3 / 288 * lam - 1088479 / 324 * lam - 1966025 * Z3 / 288
                       + 3637345 / 324)
          + nf ** 4 * (-28297 * Z3 / 288 * lam + 7519 / 162 * lam + 28297 * Z3 / 288 - 886 / 3)
          + nf ** 5 * (5 / 54 * lam + 481 / 162))
    n3lo = a ** 3 * k ** 4 * o4
    return [lo, nlo, nnlo, n3lo]


# eq.(120) coefficients for charm, nf = 3: read off by evaluating at lambda = 0, 1
c0 = [fQ_series(3, 0.0, 1.0)[i] for i in range(4)]
c1 = [fQ_series(3, 1.0, 1.0)[i] - c0[i] for i in range(4)]
chk("eq.120 LO const 0.074", round(c0[0], 3), 0.074)
chk("eq.120 NLO  0.072 - 0.220 lam", (round(c0[1], 3), round(c1[1], 3)), (0.072, -0.220))
chk("eq.120 NNLO 0.100 - 0.528 lam", (round(c0[2], 3), round(c1[2], 3)), (0.100, -0.528))
chk("eq.120 N3LO -0.391 + 0.761 lam", (round(c0[3], 3), round(c1[3], 3)), (-0.391, 0.761))
# eq.(61): f_c = 0.083 - 0.103 lambda.  Solve the constant for a, then predict the slope.
lo_, hi_ = 0.05, 0.3
for _ in range(200):
    mid = (lo_ + hi_) / 2
    if sum(fQ_series(3, 0.0, mid)) < 0.083:
        lo_ = mid
    else:
        hi_ = mid
a_c = mid
slope = sum(fQ_series(3, 1.0, a_c)) - sum(fQ_series(3, 0.0, a_c))
print("     eq.61 constant 0.083 implies alpha^(4)(mu_c)/pi = %.4f (alpha_s = %.3f)"
      % (a_c, a_c * math.pi))
print("     slope from the same alpha: %.4f (eq.61 prints -0.103)" % slope)
# 0.083 is printed to 2 significant figures: the slope over the rounding interval
slopes = []
for const in (0.0825, 0.0835):
    lo_, hi_ = 0.05, 0.3
    for _ in range(200):
        mid = (lo_ + hi_) / 2
        if sum(fQ_series(3, 0.0, mid)) < const:
            lo_ = mid
        else:
            hi_ = mid
    slopes.append(sum(fQ_series(3, 1.0, mid)) - sum(fQ_series(3, 0.0, mid)))
print("     slope over 0.0825..0.0835: %.4f .. %.4f" % tuple(slopes))
chk("eq.61 slope -0.103 inside the rounding interval of the printed 0.083",
    min(slopes) - 5e-4 <= -0.103 <= max(slopes) + 5e-4, True)

print("\n4. alpha_s AT THE THRESHOLDS (4-loop running; NAMED-NOT-READ PDG 2024 inputs)")
B = lambda nf: (11 - 2 * nf / 3, 102 - 38 * nf / 3,
                2857 / 2 - 5033 * nf / 18 + 325 * nf ** 2 / 54,
                149753 / 6 + 3564 * Z3 - (1078361 / 162 + 6508 * Z3 / 27) * nf
                + (50065 / 162 + 6472 * Z3 / 81) * nf ** 2 + 1093 / 729 * nf ** 3)


def run(alpha, mu_from, mu_to, nf, steps=4000):
    a = alpha / (4 * math.pi)
    b = B(nf)
    t0, t1 = math.log(mu_from ** 2), math.log(mu_to ** 2)
    h = (t1 - t0) / steps
    fn = lambda x: -(b[0] * x ** 2 + b[1] * x ** 3 + b[2] * x ** 4 + b[3] * x ** 5)
    for _ in range(steps):
        k1 = fn(a); k2 = fn(a + h * k1 / 2); k3 = fn(a + h * k2 / 2); k4 = fn(a + h * k3)
        a += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return a * 4 * math.pi


def thresholds(asmz, mc_, mb_, mt_, c2, MZ=91.1876):
    """alpha^(4)(m_c), alpha^(5)(m_b), alpha^(6)(m_t).  Decoupling at mu = m(m):
    alpha^(nl) = alpha^(nh) [1 + c2 (alpha^(nh)/pi)^2]."""
    a5_mb = run(asmz, MZ, mb_, 5)
    a4_mb = a5_mb * (1 + c2 * (a5_mb / math.pi) ** 2)
    a4_mc = run(a4_mb, mb_, mc_, 4)
    a5_mt = run(asmz, MZ, mt_, 5)
    a6_mt = a5_mt / (1 + c2 * (a5_mt / math.pi) ** 2)
    return a4_mc, a5_mb, a6_mt


def total_f(Sv, alphas, order):
    """S + f_c + f_b + f_t, iterated, series truncated after `order` (0 = LO)."""
    lam = Sv
    out = []
    for nf, al in zip((3, 4, 5), alphas):
        fq = sum(fQ_series(nf, lam, al / math.pi)[:order + 1])
        out.append(fq)
        lam += fq
    return lam, out


PDG = dict(asmz=0.1180, mc_=1.2730, mb_=4.183, mt_=162.5)
al = thresholds(c2=11 / 72, **PDG)
print("     alpha^(4)(m_c) = %.4f   alpha^(5)(m_b) = %.4f   alpha^(6)(m_t) = %.4f" % al)
chk("alpha_s(m_b) in the usual 0.22-0.23 band", 0.215 < al[1] < 0.235, True)
fc089 = sum(fQ_series(3, 0.089, al[0] / math.pi))
chk("our f_c at lambda = 0.089 agrees with Hill-Solon eq.(61) 0.073(3)", fc089, 0.073, 0.003)

print("\n5. THE BEYOND-LO SHIFT of 2/9 and of f, K_mu (S = 0.06, the tree's S_MID)")
S0 = 0.06
res = {}
for order, name in enumerate(("LO", "NLO", "NNLO", "N3LO")):
    tot, fq = total_f(S0, al, order)
    heavy = sum(fq)
    res[name] = (tot, heavy)
    print("     %-5s f_c=%.5f f_b=%.5f f_t=%.5f  heavy sum=%.5f (= %.4f x 2/9 (1-S))  "
          "f=%.5f  K_mu=%.5f" % (name, fq[0], fq[1], fq[2], heavy,
                                  heavy / (2 / 9 * (1 - S0)), tot, tot - 1))
chk("LO reproduces the tree exactly: f = 0.268889", res["LO"][0], 0.2688889, 1e-6)
shift_heavy = res["N3LO"][1] / res["LO"][1] - 1
shift_f = res["N3LO"][0] / res["LO"][0] - 1
shift_K = (res["N3LO"][0] - 1) / (res["LO"][0] - 1) - 1
print("     beyond-LO: heavy sum %+.2f%%, f %+.2f%%, K_mu %+.2f%%" %
      (100 * shift_heavy, 100 * shift_f, 100 * shift_K))
chk("correction is POSITIVE and O(few %) on the heavy sum", 0.02 < shift_heavy < 0.10, True)
chk("K_mu stays O(1) and negative", -0.8 < res["N3LO"][0] - 1 < -0.65, True)
# the NLO light-quark dependence breaks the tree's factorisation (1 - S) x dlnLambda/dlnv:
h0 = total_f(0.0, al, 3)[0]
h1 = total_f(0.12, al, 3)
fac = [(total_f(s, al, 3)[0] - s) / (1 - s) for s in (0.0, 0.06, 0.12)]
print("     (f - S)/(1 - S) at S = 0, 0.06, 0.12: %.5f %.5f %.5f  (LO: 0.22222 for all)" % tuple(fac))
chk("beyond LO, (f - S)/(1 - S) is NOT S-independent", abs(fac[0] - fac[2]) > 1e-3, True)

print("\n6. SENSITIVITY: alpha_s(M_Z) +- 0.0009, masses, c2 in {+11/72, 0, -11/72}, S scan")
rows = []
for asmz in (0.1171, 0.1180, 0.1189):
    for c2 in (11 / 72, 0.0, -11 / 72):
        for mt_ in (161.0, 162.5, 164.6):
            a3 = thresholds(asmz, 1.2730, 4.183, mt_, c2)
            t, fq = total_f(S0, a3, 3)
            rows.append(sum(fq) / (2 / 9 * (1 - S0)) - 1)
print("     heavy-sum shift over the scan: %+.2f%% .. %+.2f%%" % (100 * min(rows), 100 * max(rows)))
chk("scan never flips the sign or exceeds 10%", 0 < min(rows) and max(rows) < 0.10, True)
for Sv in (0.0096, 0.06, 0.089, 0.09, 0.115):
    lo = total_f(Sv, al, 0)[0]; hi = total_f(Sv, al, 3)[0]
    print("     S=%.4f  f_LO=%.5f  f_N3LO=%.5f  K_mu LO=%.4f  N3LO=%.4f" % (Sv, lo, hi, lo - 1, hi - 1))

print("\n7. PERTURBATIVE CONVERGENCE at charm (Hill-Solon: 'poorly convergent')")
t = fQ_series(3, S0, al[0] / math.pi)
print("     f_c terms at S=0.06: LO %.5f  NLO %+.5f  NNLO %+.5f  N3LO %+.5f" % tuple(t))
chk("charm NLO/LO below 20%", abs(t[1] / t[0]) < 0.2, True)

print("\n%d failures" % len(FAIL))
sys.exit(1 if FAIL else 0)
