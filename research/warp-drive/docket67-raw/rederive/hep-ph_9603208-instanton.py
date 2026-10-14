#!/usr/bin/env python3
"""DOCKET 67 re-derivation: hep-ph/9603208 (Rubakov & Shaposhnikov), the zero-temperature
instanton suppression exp(-4 pi / alpha_W), as massform.py uses it.

Checks, each printed PASS/FAIL:
 (1) SYMPY  exp(-2 S_inst) with S_inst = 8 pi^2/g^2 is exactly exp(-16 pi^2/g^2) = exp(-4 pi/alpha_W),
     alpha_W = g^2/(4 pi).  (The standard 't Hooft action; the source text itself was not readable in
     this stage -- see the audit JSON -- so this checks the two forms massform prints against each other
     and against the textbook action, not against the page.)
 (2) NUMERIC  the tree's figures, recomputed independently of massform (no import):
     m_W = 80.362 GeV (captures/PDG-2026.tsv row 24, READ in the tree), G_F = 1.1663788e-5 GeV^-2
     (higgs.py:209, NAMED-NOT-READ), v = (sqrt2 G_F)^-1/2, g = 2 m_W / v  ->  1/alpha_W = 29.49,
     log10 suppression = -160.95, transitions = ceil(B/3), attempts x prefactor >= 10^189.10.
 (3) NUMERIC  the source's own eq. (2.8) pairing as the tree captured it (massform.py:1080-1083):
     alpha_W = 1/29 gives 10^-158.27, not the printed 10^-170; 10^-170 needs 1/alpha_W = 31.15.
 (4) NUMERIC  scheme / datum sensitivity: the exponent across the definitions of alpha_W in use
     (tree-level G_F, on-shell, MS-bar at M_Z, alpha(0)/sin^2) and the 1996 -> now shift of the
     authors' 1/29.  Inputs marked RECALLED are standard PDG-2024 values quoted from memory, NOT read
     at source in this stage (alphaXiv quota exhausted, arxiv.org egress-blocked).
Stdlib + sympy.  Reads the tree's capture file read-only; writes nothing.
"""
import math
import os
import sys

import sympy as sp

OK = []


def chk(name, cond, detail=""):
    OK.append(bool(cond))
    print("%s  %s  %s" % ("PASS" if cond else "FAIL", name, detail))


# ---------------------------------------------------------------- (1) symbolic
g, a = sp.symbols("g alpha_W", positive=True)
S_inst = 8 * sp.pi ** 2 / g ** 2
two_S = sp.simplify(2 * S_inst)
chk("2 S_inst = 16 pi^2/g^2", sp.simplify(two_S - 16 * sp.pi ** 2 / g ** 2) == 0, str(two_S))
sub = sp.simplify((16 * sp.pi ** 2 / g ** 2).subs(g, sp.sqrt(4 * sp.pi * a)))
chk("16 pi^2/g^2 = 4 pi/alpha_W at alpha_W = g^2/4pi", sp.simplify(sub - 4 * sp.pi / a) == 0, str(sub))
chk("S_inst = 2 pi/alpha_W", sp.simplify(S_inst.subs(g, sp.sqrt(4 * sp.pi * a)) - 2 * sp.pi / a) == 0)

# ---------------------------------------------------------------- (1b) BPST action, machine-checked
# A^a_mu = 2 eta^a_{mu nu} x_nu / (x^2 + rho^2) (regular gauge, coupling scaled out);
# F^a_{mu nu} = d_mu A^a_nu - d_nu A^a_mu + eps^{abc} A^b_mu A^c_nu.
# Check F^a F^a = 192 rho^4/(x^2+rho^2)^4 exactly (sympy), then S = (1/4g^2) int d^4x F^a F^a = 8 pi^2/g^2,
# and the topological charge (1/32 pi^2) int F Ftilde = 1 (self-duality F = Ftilde checked componentwise).
X = sp.symbols("x0:4", real=True)
rho = sp.symbols("rho", positive=True)
def eta(A, m, n):
    if m < 3 and n < 3:
        return sp.LeviCivita(A, m, n)
    if n == 3 and m < 3:
        return sp.KroneckerDelta(A, m)
    if m == 3 and n < 3:
        return -sp.KroneckerDelta(A, n)
    return 0
r2 = sum(xi ** 2 for xi in X)
Afield = [[2 * sum(eta(A, m, n) * X[n] for n in range(4)) / (r2 + rho ** 2) for m in range(4)] for A in range(3)]
F = [[[sp.diff(Afield[A][n], X[m]) - sp.diff(Afield[A][m], X[n])
       + sum(sp.LeviCivita(A, b, c) * Afield[b][m] * Afield[c][n] for b in range(3) for c in range(3))
       for n in range(4)] for m in range(4)] for A in range(3)]
FF = sum(F[A][m][n] ** 2 for A in range(3) for m in range(4) for n in range(4))
chk("BPST: F^a F^a = 192 rho^4/(x^2+rho^2)^4 (exact)",
    sp.simplify(FF - 192 * rho ** 4 / (r2 + rho ** 2) ** 4) == 0)
def dual(A, m, n):
    return sp.Rational(1, 2) * sum(sp.LeviCivita(m, n, k, l) * F[A][k][l] for k in range(4) for l in range(4))
sd = all(sp.simplify(F[A][m][n] - dual(A, m, n)) == 0 for A in range(3) for m in range(4) for n in range(m + 1, 4))
asd = all(sp.simplify(F[A][m][n] + dual(A, m, n)) == 0 for A in range(3) for m in range(4) for n in range(m + 1, 4))
chk("BPST field is (anti-)self-dual, so the action saturates the Bogomolny bound", sd or asd,
    "self-dual" if sd else ("anti-self-dual" if asd else "neither"))
r, gs = sp.symbols("r g", positive=True)
radial = sp.integrate(2 * sp.pi ** 2 * r ** 3 * 192 * rho ** 4 / (r ** 2 + rho ** 2) ** 4, (r, 0, sp.oo))
S_bpst = sp.simplify(radial / (4 * gs ** 2))
chk("S_inst = (1/4g^2) int F^2 = 8 pi^2/g^2", sp.simplify(S_bpst - 8 * sp.pi ** 2 / gs ** 2) == 0, str(S_bpst))
Q = sp.simplify(radial / (32 * sp.pi ** 2))
chk("topological charge |Q| = 1", Q == 1, str(Q))

# ---------------------------------------------------------------- (1c) Bogomolny bound, generic field
# For ANY antisymmetric F^a (3 colours x 6 components, symbolic): sum (F -+ Ftilde)^2 = 2 sum F^2 -+ 2 sum F Ftilde,
# so sum F^2 >= |sum F Ftilde|, i.e. S_gauge >= 8 pi^2 |Q| / g^2.  Higgs kinetic + potential terms are >= 0
# (V(v) = 0), so in the gauge-Higgs theory every Q = 1 Euclidean path has S_E >= 8 pi^2/g^2: exp(-4 pi/alpha_W)
# is the LARGEST leading exponential any single-instanton path can carry -- the constrained-instanton
# correction the tree does not name can only deepen the suppression.
comps = {}
Fg = [[[0] * 4 for _ in range(4)] for _ in range(3)]
for A in range(3):
    for m in range(4):
        for n in range(m + 1, 4):
            t = sp.Symbol("F%d_%d%d" % (A, m, n), real=True)
            Fg[A][m][n], Fg[A][n][m] = t, -t
def dualg(A, m, n):
    return sp.Rational(1, 2) * sum(sp.LeviCivita(m, n, k, l) * Fg[A][k][l] for k in range(4) for l in range(4))
F2 = sum(Fg[A][m][n] ** 2 for A in range(3) for m in range(4) for n in range(4))
FFt = sum(Fg[A][m][n] * dualg(A, m, n) for A in range(3) for m in range(4) for n in range(4))
for sgn in (1, -1):
    lhs = sum((Fg[A][m][n] - sgn * dualg(A, m, n)) ** 2 for A in range(3) for m in range(4) for n in range(4))
    chk("sum (F %s Ftilde)^2 = 2 F^2 %s 2 F Ftilde (generic F)" % ("-" if sgn > 0 else "+", "-" if sgn > 0 else "+"),
        sp.expand(lhs - (2 * F2 - 2 * sgn * FFt)) == 0)

# ---------------------------------------------------------------- (2) the tree's figures
CAP = "/home/user/Claude-Method-Works/research/warp-drive/captures/PDG-2026.tsv"
m_w = None
hdr = None
with open(CAP) as fh:
    for line in fh:
        if line.startswith("#"):
            continue
        f = line.rstrip("\n").split("\t")
        if hdr is None:
            hdr = f
            continue
        if f[0] == "24":
            m_w = float(f[hdr.index("mass_MeV")]) / 1000.0
chk("m_W read from the tree's PDG-2026 capture", m_w == 80.362, "m_W = %r GeV" % m_w)
G_F = 1.1663788e-5
v = 1.0 / math.sqrt(math.sqrt(2.0) * G_F)
gg = 2.0 * m_w / v
aw = gg * gg / (4.0 * math.pi)
L = -(4.0 * math.pi / aw) / math.log(10.0)
Lg = -(16.0 * math.pi ** 2 / gg ** 2) / math.log(10.0)
chk("v = 246.2196 GeV", abs(v - 246.2196) < 1e-3, "%.5f" % v)
chk("1/alpha_W = 29.49", round(1 / aw, 2) == 29.49, "%.4f" % (1 / aw))
chk("log10 exp(-4pi/alpha_W) = -160.95", round(L, 2) == -160.95, "%.4f" % L)
chk("both forms agree numerically", abs(L - Lg) < 1e-9)
# The tree's transition count 1.4036200519680083617443217408e28 = ceil(B/3) (massform, run 2026-09-26).
N_T = 14036200519680083617443217408
need = math.log10(N_T) - L
chk("attempts x prefactor >= 10^189.10", round(need, 2) == 189.10, "%.4f" % need)

# ---------------------------------------------------------------- (3) eq. (2.8) pairing
L29 = -(4 * math.pi * 29.0) / math.log(10)
inv_for_170 = 170 * math.log(10) / (4 * math.pi)
chk("alpha_W = 1/29 gives 10^-158.27 (printed 10^-170)", round(L29, 2) == -158.27, "%.4f" % L29)
print("      printed - arithmetic = %.2f decades; 10^-170 corresponds to 1/alpha_W = %.2f"
      % (-170 - L29, inv_for_170))
chk("gap 11.73 decades, as massform records", round(-170 - L29, 2) == -11.73)
print("      1/alpha_W = 31.15 is alpha(0)^-1 x sin^2 = 137.036 x %.4f" % (inv_for_170 / 137.035999))
L297 = -(4 * math.pi * 29.7) / math.log(10)
L30 = -(4 * math.pi * 30.0) / math.log(10)
print("      Tye-Wong: 1/29.7 -> %.2f ; 1/30 -> %.2f (printed 10^-162)" % (L297, L30))

# ---------------------------------------------------------------- (4) scheme / datum spread
DEC_PER_UNIT = 4 * math.pi / math.log(10)
print("      d log10(suppression) / d(1/alpha_W) = %.4f decades per unit" % DEC_PER_UNIT)
# RECALLED (NOT READ here): PDG-2024 central values
M_W_24, M_Z_24 = 80.3692, 91.1880
A0_INV, AMZ_MSBAR_INV = 137.035999, 127.930
S2_MSBAR, S2_EFF = 0.23129, 0.23153
s2_os = 1 - (M_W_24 / M_Z_24) ** 2
schemes = {
    "tree: g = 2 m_W/v (G_F), m_W PDG-2026 80.362 [tree]": 1 / aw,
    "same, m_W PDG-2024 80.3692 [RECALLED]": 4 * math.pi / (2 * M_W_24 / v) ** 2,
    "MS-bar at M_Z: alpha-hat(M_Z)/s^2-hat [RECALLED]": AMZ_MSBAR_INV * S2_MSBAR,
    "on-shell: alpha(0)/(1 - m_W^2/m_Z^2) [RECALLED]": A0_INV * s2_os,
    "alpha(0)/sin^2_eff [RECALLED]": A0_INV * S2_EFF,
    "RS96 eq. (2.8) as printed: 1/29": 29.0,
}
lo, hi = 1e9, -1e9
for k, inv in schemes.items():
    Lk = -DEC_PER_UNIT * inv
    lo, hi = min(lo, Lk), max(hi, Lk)
    print("      %-55s 1/alpha_W = %7.3f  ->  10^%.2f" % (k, inv, Lk))
print("      spread of the exponent across schemes: %.2f decades (10^%.2f .. 10^%.2f)" % (hi - lo, lo, hi))
chk("every scheme leaves the suppression below 10^-150 (the 'unobservably small' conclusion)", hi < -150)
shift_1996 = -DEC_PER_UNIT * (1 / aw - 29.0)
print("      the authors' 1/29 -> the tree's 1/%.2f moves the exponent by %.2f decades" % (1 / aw, shift_1996))
dmw = 0.0133
dL = abs(-DEC_PER_UNIT * (4 * math.pi / (2 * (m_w + dmw) / v) ** 2 - 1 / aw))
print("      a 1-sigma move of m_W (13.3 MeV, RECALLED) moves it by %.4f decades" % dL)
chk("the m_W uncertainty is immaterial (< 0.1 decade)", dL < 0.1)

print("\nRESULT: %d/%d checks pass" % (sum(OK), len(OK)))
sys.exit(0 if all(OK) else 1)
