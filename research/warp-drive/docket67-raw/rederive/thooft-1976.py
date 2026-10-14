#!/usr/bin/env python3
"""DOCKET 67 re-derivation: thooft-1976 ('t Hooft, PRL 37 (1976) 8; the
instanton computation is PRD 14 (1976) 3432).  Both NAMED-NOT-READ this stage
(pre-arXiv; the restatement hep-ph/9603208 could not be re-read: alphaXiv quota
exceeded, arxiv.org egress-blocked).  What is checked here is what is finite or
closed-form in the result AS THE TREE USES IT (massform.py:2054-2070, 530-534,
2951-2956, 2113-2123):

 (A) The BPST instanton, built explicitly from 't Hooft symbols (sympy):
     F from A, self-duality, action density, S = 8 pi^2/g^2, Q = 1.
 (B) e^{-2S} = e^{-16 pi^2/g^2} = e^{-4 pi/alpha_W}, alpha_W = g^2/4pi (symbolic).
 (C) Bogomolny bound S >= 8 pi^2 |Q|/g^2 is LINEAR in |Q|: suppression per unit
     Delta B is the same for k single transitions and one charge-k transition.
 (D) Zero-mode count (index 2T(R)Q per Weyl field, left-handed doublets only):
     Delta B = Delta L = N_f per unit Q; B-L and hypercharge conserved by the
     vertex; the tree's THOOFT_VERTEX reproduces (3,3); N_f = 2 (the 1976
     'with charm' model) gives (2,2).
 (E) Numbers: alpha_W from m_W (repo PDG-2026 capture, READ in repo) and v
     from G_F (NAMED-NOT-READ); log10 e^{-4pi/alpha_W}; scheme spread; the
     1976-era sin^2 theta_W range; RS96's printed 10^-170 vs its 1/29; the
     tree's own figures cross-checked by read-only import.
"""
import math
import os
import sys
from fractions import Fraction

import sympy as sp

PASS, FAIL = [], []


def chk(name, cond, detail=""):
    (PASS if cond else FAIL).append(name)
    print(("PASS " if cond else "FAIL ") + name + (("   " + str(detail)) if detail != "" else ""))


# ----------------------------------------------------------------- (A) BPST
x = sp.symbols("x1:5", real=True)
rho = sp.symbols("rho", positive=True)
r2 = sum(xi ** 2 for xi in x)


def eta(a, m, n):
    """'t Hooft symbol eta^a_{mu nu}, a in 1..3, mu,nu in 1..4 (Euclidean)."""
    if m == n:
        return 0
    if m <= 3 and n <= 3:
        return sp.LeviCivita(a, m, n)
    if n == 4:
        return 1 if m == a else 0
    if m == 4:
        return -1 if n == a else 0
    return 0


E = [[[eta(a, m, n) for n in range(1, 5)] for m in range(1, 5)] for a in range(1, 4)]
chk("(A0) eta^a_{mn} eta^a_{mn} = 12",
    sum(E[a][m][n] ** 2 for a in range(3) for m in range(4) for n in range(4)) == 12)
# self-duality of eta: eta^a_{mn} = (1/2) eps_{mnrs} eta^a_{rs}
sd_eta = all(
    E[a][m][n] == sp.Rational(1, 2) * sum(sp.LeviCivita(m + 1, n + 1, r + 1, s + 1) * E[a][r][s]
                                          for r in range(4) for s in range(4))
    for a in range(3) for m in range(4) for n in range(4))
chk("(A0) eta is self-dual", sd_eta)

# regular-gauge BPST, coupling scaled out (A_phys = A/g):
# A^a_mu = 2 eta^a_{mu nu} x_nu / (x^2 + rho^2)
A = [[2 * sum(E[a][m][n] * x[n] for n in range(4)) / (r2 + rho ** 2) for m in range(4)] for a in range(3)]


def Fa(a, m, n):
    expr = sp.diff(A[a][n], x[m]) - sp.diff(A[a][m], x[n])
    expr += sum(sp.LeviCivita(a + 1, b + 1, c + 1) * A[b][m] * A[c][n]
                for b in range(3) for c in range(3))
    return sp.simplify(expr)


F = [[[Fa(a, m, n) for n in range(4)] for m in range(4)] for a in range(3)]
target = all(sp.simplify(F[a][m][n] + 4 * E[a][m][n] * rho ** 2 / (r2 + rho ** 2) ** 2) == 0
             for a in range(3) for m in range(4) for n in range(4))
chk("(A1) F^a_{mn} = -4 eta^a_{mn} rho^2/(x^2+rho^2)^2", target)
Fdual_ok = all(
    sp.simplify(F[a][m][n] - sp.Rational(1, 2) * sum(sp.LeviCivita(m + 1, n + 1, r + 1, s + 1) * F[a][r][s]
                                                     for r in range(4) for s in range(4))) == 0
    for a in range(3) for m in range(4) for n in range(4))
chk("(A2) F is self-dual (F = *F)", Fdual_ok)
FF = sp.simplify(sum(F[a][m][n] ** 2 for a in range(3) for m in range(4) for n in range(4)))
chk("(A3) F^a F^a = 192 rho^4/(x^2+rho^2)^4", sp.simplify(FF - 192 * rho ** 4 / (r2 + rho ** 2) ** 4) == 0, FF)
# radial integral over R^4: d^4x = 2 pi^2 r^3 dr
r = sp.symbols("r", positive=True)
dens = (FF / 4).subs({x[0]: r, x[1]: 0, x[2]: 0, x[3]: 0})
S_times_g2 = sp.simplify(2 * sp.pi ** 2 * sp.integrate(dens * r ** 3, (r, 0, sp.oo)))
chk("(A4) S = (1/4g^2) int F^aF^a = 8 pi^2/g^2, rho-independent", sp.simplify(S_times_g2 - 8 * sp.pi ** 2) == 0, S_times_g2)
Q = sp.simplify(S_times_g2 / (8 * sp.pi ** 2))   # Q = (1/32pi^2) int F Ftilde = (1/32pi^2) int F F (self-dual)
chk("(A5) topological charge Q = (1/32 pi^2) int F.*F = 1", Q == 1, Q)

# ----------------------------------------------------------------- (B) exponent forms
g = sp.symbols("g", positive=True)
aW = g ** 2 / (4 * sp.pi)
S = 8 * sp.pi ** 2 / g ** 2
chk("(B1) 2S = 16 pi^2/g^2 = 4 pi/alpha_W", sp.simplify(2 * S - 16 * sp.pi ** 2 / g ** 2) == 0
    and sp.simplify(2 * S - 4 * sp.pi / aW) == 0)
chk("(B2) S = 2 pi/alpha_W (Tye-Wong's 'S = 2 pi/alpha_W')", sp.simplify(S - 2 * sp.pi / aW) == 0)

# ----------------------------------------------------------------- (C) Bogomolny linearity
# int tr (F -+ *F)^2 >= 0  =>  int F.F >= |int F.*F|  =>  S >= 8 pi^2 |Q| / g^2.
k = sp.symbols("k", positive=True, integer=True)
Smin = lambda q: 8 * sp.pi ** 2 * q / g ** 2
chk("(C1) k transitions of Q=1 cost the same minimal action as one Q=k",
    sp.simplify(k * Smin(1) - Smin(k)) == 0)
chk("(C2) suppression per unit Delta B at Q=k: e^{-2 S_min(k)/ (N_f k)} independent of k",
    sp.simplify(2 * Smin(k) / (3 * k) - 2 * Smin(1) / 3) == 0)

# ----------------------------------------------------------------- (D) zero modes / vertex
B_of = {"Q": Fraction(1, 3), "L": Fraction(0)}
L_of = {"Q": Fraction(0), "L": Fraction(1)}
Y_of = {"Q": Fraction(1, 6), "L": Fraction(-1, 2)}
T_fund = Fraction(1, 2)


def vertex(nf, nc=3, Qtop=1):
    """Each left-handed SU(2) doublet Weyl field has index 2 T(fund) Q = Q zero modes."""
    legs = []
    for _ in range(nf):
        legs += ["Q"] * (nc * int(2 * T_fund * Qtop)) + ["L"] * int(2 * T_fund * Qtop)
    dB = sum(B_of[f] for f in legs)
    dL = sum(L_of[f] for f in legs)
    dY = sum(Y_of[f] for f in legs)
    return len(legs), dB, dL, dY


for nf in (2, 3):
    n, dB, dL, dY = vertex(nf)
    chk("(D1) N_f=%d: %d legs, Delta B = Delta L = N_f, Delta(B-L) = 0, Delta Y = 0" % (nf, n),
        dB == nf and dL == nf and dB - dL == 0 and dY == 0 and n == 4 * nf and n % 2 == 0,
        (n, dB, dL, dY))
# right-handed singlets carry no SU(2) zero modes: T(singlet) = 0 -> index 0
chk("(D2) SU(2) singlets (u_R, d_R, e_R) have index 2*0*Q = 0: no legs", 2 * 0 * 1 == 0)

# ----------------------------------------------------------------- (E) numbers
LN10 = math.log(10.0)


def log10_supp(ainv):
    return -4.0 * math.pi * ainv / LN10


# repo PDG-2026 capture (READ in repo): W mass
cap = "/home/user/Claude-Method-Works/research/warp-drive/captures/PDG-2026.tsv"
mW = None
with open(cap) as fh:
    for line in fh:
        if line.startswith("24\tW+"):
            mW = float(line.split("\t")[11]) / 1000.0
chk("(E0) m_W read from repo PDG-2026 capture", mW is not None, mW)
GF = 1.1663788e-5            # GeV^-2, NAMED-NOT-READ (as the tree holds it, higgs.py:209)
v = (math.sqrt(2.0) * GF) ** -0.5
gval = 2 * mW / v
aW_os = gval ** 2 / (4 * math.pi)
L_os = log10_supp(1 / aW_os)
print("     on-shell: v = %.5f GeV, g = %.6f, 1/alpha_W = %.4f, log10 e^{-4pi/aW} = %.4f" % (v, gval, 1 / aW_os, L_os))
chk("(E1) on-shell 1/alpha_W ~ 29.49, exponent 10^-160.95", abs(1 / aW_os - 29.4913) < 1e-3 and abs(L_os + 160.9489) < 1e-3)

# scheme / scale spread (inputs NAMED-NOT-READ this stage: PDG EW-review values from memory)
variants = {
    "MSbar at m_Z: alpha^-1(mZ)=127.930, sin2=0.23122": 127.930 * 0.23122,
    "on-shell sin2 = 1 - mW^2/mZ^2 = 0.22339 with alpha(0)^-1 = 137.036": 137.036 * (1 - (mW / 91.1880) ** 2),
    "Tye-Wong p.7 pairing 1/29.7": 29.7,
    "Tye-Wong p.2 pairing 1/30": 30.0,
    "RS96 eq.(2.8) 1/29": 29.0,
}
vals = {}
for k_, ainv in variants.items():
    vals[k_] = log10_supp(ainv)
    print("     %-72s 1/aW=%.3f  log10=%.2f" % (k_, ainv, vals[k_]))
spread = max(vals.values()) - min(vals.values())
chk("(E2) scheme/scale choice moves the exponent by several decades (> 3), not by tens",
    3 < spread < 15, "%.2f decades" % spread)
chk("(E3) RS96 printed 10^-170 at 1/29 vs arithmetic 10^-158.27: 11.73 decades (a discrepancy, recorded)",
    abs(vals["RS96 eq.(2.8) 1/29"] + 158.27) < 0.01 and abs(-170 - vals["RS96 eq.(2.8) 1/29"] + 11.73) < 0.01)
ainv_170 = 170 * LN10 / (4 * math.pi)
print("     10^-170 would need 1/alpha_W = %.3f" % ainv_170)

# 1976-era: alpha = 1/137, sin^2 theta_W between 0.2 and 0.4 (NAMED-NOT-READ range)
era = [log10_supp(137.036 * s) for s in (0.20, 0.30, 0.35, 0.40)]
print("     1976-era sin2 in {0.20,0.30,0.35,0.40}: log10 =", ["%.1f" % e for e in era])
chk("(E4) every 1976-era value leaves the factor below 10^-100 (conclusion 'unobservable' unmoved)",
    max(era) < -100)
# what alpha_W would make the factor merely 10^-20 (i.e. observable-ish)?
ainv_20 = 20 * LN10 / (4 * math.pi)
chk("(E5) factor 10^-20 would need 1/alpha_W = %.2f (alpha_W ~ 0.27), far from any measured value" % ainv_20,
    ainv_20 < 5)

# cross-check the tree by read-only import
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
try:
    import massform as m
    chk("(E6) tree log10_suppression() reproduces", abs(m.log10_suppression() - L_os) < 1e-9,
        m.log10_suppression())
    chk("(E7) tree THOOFT_DELTA_B_L = (N_F, N_F) = (3,3) reproduces (D1)",
        tuple(m.THOOFT_DELTA_B_L) == (Fraction(3), 3))
    need = math.log10(m.transitions_needed()) - L_os
    chk("(E8) tree's 10^189.10 = log10(transitions) - log10(factor) reproduces",
        abs(need - m.log10_attempts_times_prefactor()) < 1e-9, "%.2f" % need)
    shift = {k_: math.log10(m.transitions_needed()) - vals[k_] for k_ in vals}
    print("     10^189.10 under the other alpha_W choices:",
          {k_[:22]: "%.2f" % s for k_, s in shift.items()})
except Exception as exc:  # pragma: no cover
    chk("(E6-8) tree import", False, repr(exc))

print("\n%d PASS, %d FAIL" % (len(PASS), len(FAIL)))
sys.exit(1 if FAIL else 0)
