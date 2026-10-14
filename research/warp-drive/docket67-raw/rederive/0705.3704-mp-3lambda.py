#!/usr/bin/env python3
"""DOCKET 67 -- audit 0705.3704-mp-3lambda.
Flambaum arXiv:0705.3704v2 p.4: "The proton mass is proportional to Lambda_QCD
(M_p ~ 3 Lambda_QCD), therefore, the measurements of the variation of the
electron-to-proton mass ratio mu = m_e/M_p is equivalent to the measurements of
the variation of X_e = m_e/Lambda_QCD."   (quote as READ by the sibling audit
0705.3704 and as quoted in address.py:445-446; see report for read status.)

Checks:
 A  sympy: m_p = L F(m_q/L) => Euler homogeneity; d ln m_p/d ln v = S under H2
    (L independent of v) and 2/9 + 7S/9 under H1 (L_3 = L_6^(7/9)(m_c m_b m_t)^(2/27)).
 B  sympy: in the chiral limit S -> 0 the READ proportionality m_p = c L holds
    under BOTH H1 and H2 -- m_p/L_3 is v-independent in both -- yet K_mu differs
    (-7/9 vs -1).  So the sentence does not discriminate H1 from H2.
 C  Flambaum's identity d ln mu = d ln X_e: residual = -S d ln X_q, evaluated at
    the FLAG 2024 sigma terms held READ in massform.py:1456-1459.
 D  numeric: M_p / Lambda_MSbar^(nf) for nf = 3,4,5 at 1..4-loop Lambda
    definitions from alpha_s(M_Z) scanned 0.1171..0.1189 (PDG 2024 central 0.1180(9),
    NAMED-NOT-READ here) with 4-loop running and continuous matching.
 E  what the tree consumes: the factor 3 is never used numerically in address.py
    (grep result recorded in the report), only the proportionality.
Stdlib + sympy.  Exit 0 iff every check passes.
"""
import math, sys
import sympy as sp

fails = []
def chk(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)

# ---------------- A: homogeneity, H1 and H2 ----------------
L, m, v, c = sp.symbols('L m v c', positive=True)
F = sp.Function('F')
mp = L * F(m / L)
dlnL = sp.simplify(L * sp.diff(mp, L) / mp)
dlnm = sp.simplify(m * sp.diff(mp, m) / mp)
chk("A1 Euler: dln m_p/dln L + dln m_p/dln m_q = 1", sp.simplify(dlnL + dlnm - 1) == 0)
S = sp.Symbol('S')
# H2: L independent of v, m_q ~ v  -> dln m_p/dln v = dlnm = S
f_H2 = dlnm  # by definition S == dlnm
chk("A2 H2: d ln m_p/d ln v = S (m_q ~ v, L fixed)", sp.simplify(f_H2 - dlnm) == 0)
# H1: one-loop threshold chain
nf = sp.Symbol('nf')
b0 = lambda n: sp.Rational(33, 1) - 2 * n  # proportional to 11 - 2n/3 (x3), ratios only
e_c = 1 - b0(4) / b0(3)
e_b = (1 - b0(5) / b0(4)) * (b0(4) / b0(3))
e_t = (1 - b0(6) / b0(5)) * (b0(5) / b0(4)) * (b0(4) / b0(3))
e_L6 = b0(6) / b0(3)
chk("A3 one-loop chain exponents: c,b,t each 2/27; Lambda_6 exponent 7/9",
    (e_c, e_b, e_t, e_L6) == (sp.Rational(2, 27),) * 3 + (sp.Rational(7, 9),))
dlnL3_dlnv_H1 = e_c + e_b + e_t
chk("A4 H1: d ln Lambda_3/d ln v = 2/9", dlnL3_dlnv_H1 == sp.Rational(2, 9))
f_H1 = dlnL3_dlnv_H1 * (1 - S) + S
chk("A5 H1: d ln m_p/d ln v = 2/9 + 7S/9",
    sp.simplify(f_H1 - (sp.Rational(2, 9) + sp.Rational(7, 9) * S)) == 0)

# ---------------- B: the READ sentence holds under both ----------------
# chiral limit: m_p = c * Lambda_3 exactly.  d ln(m_p/Lambda_3)/d ln v:
for hyp, dlnL3 in (("H1", dlnL3_dlnv_H1), ("H2", 0)):
    dln_ratio = (f_H1 if hyp == "H1" else S).subs(S, 0) - dlnL3
    chk("B1 %s: at S=0, m_p/Lambda_3 is v-independent (M_p ~ 3 Lambda holds)" % hyp,
        sp.simplify(dln_ratio) == 0)
Kmu_H1 = (f_H1 - 1).subs(S, 0)
Kmu_H2 = (S - 1).subs(S, 0)
chk("B2 yet K_mu = d ln(m_p/m_e)/d ln v differs: H1 -7/9, H2 -1",
    (Kmu_H1, Kmu_H2) == (-sp.Rational(7, 9), -1))
print("   => the proportionality is common to H1 and H2; H2 (Lambda independent of v)"
      " is an ADDED premise, not the content of the sentence.")

# ---------------- C: Flambaum's identity mu == X_e ----------------
# mu = m_e/M_p, M_p = L F(X_q), X_q = m_q/L:  d ln mu = d ln X_e - S d ln X_q
Xe, Xq = sp.symbols('X_e X_q', positive=True)
Fq = sp.Function('G')
lnmu = sp.log(Xe) - sp.log(Fq(Xq))      # ln(m_e/L) - ln(M_p/L)
resid = sp.simplify(Xq * sp.diff(lnmu, Xq))
Sdef = sp.simplify(Xq * sp.diff(sp.log(Fq(Xq)), Xq))
chk("C1 d ln mu - d ln X_e = -S d ln X_q (exact); identity is the S->0 limit",
    sp.simplify(resid + Sdef) == 0)
M_P = 938.27208816           # address.py:425 (CODATA 2018 value held in tree)
M_N = (938.27208816 + 939.56542052) / 2
flag = {"FLAG24 Nf=2+1 (42.2+44.9)": (42.2 + 44.9),
        "FLAG24 Nf=2+1+1 (60.9+41.0)": (60.9 + 41.0),
        "sigma_piN only, 2+1 (42.2)": 42.2,
        "sigma_piN only, 2+1+1 (60.9)": 60.9}
for k, s in flag.items():
    print("   S[%s] = %.4f  -> residual per unit d ln X_q = %.4f" % (k, s / M_N, -s / M_N))
chk("C2 residual |S| is 4.5%..10.9% of d ln X_q over the READ FLAG inputs",
    0.044 < min(s / M_N for s in flag.values()) and max(s / M_N for s in flag.values()) < 0.110)

# ---------------- D: the factor 3 ----------------
Z3 = 1.2020569031595942
def bcoef(n):
    p = math.pi
    b0 = (33 - 2 * n) / (12 * p)
    b1 = (153 - 19 * n) / (24 * p ** 2)
    b2 = (2857 - 5033 * n / 9 + 325 * n ** 2 / 27) / (128 * p ** 3)
    b3 = ((149753 / 6 + 3564 * Z3) - (1078361 / 162 + 6508 * Z3 / 27) * n
          + (50065 / 162 + 6472 * Z3 / 81) * n ** 2 + 1093 * n ** 3 / 729) / (256 * p ** 4)
    return b0, b1, b2, b3

def run(a, mu0, mu1, n, steps=4000):
    """RK4 on d a/d ln mu^2 = -a^2 (b0 + b1 a + b2 a^2 + b3 a^3)."""
    B = bcoef(n)
    f = lambda x: -x * x * (B[0] + B[1] * x + B[2] * x * x + B[3] * x ** 3)
    t0, t1 = math.log(mu0 ** 2), math.log(mu1 ** 2)
    h = (t1 - t0) / steps
    for _ in range(steps):
        k1 = f(a); k2 = f(a + h * k1 / 2); k3 = f(a + h * k2 / 2); k4 = f(a + h * k3)
        a += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return a

def asym(t, n, loops):
    b0, b1, b2, b3 = bcoef(n)
    lt = math.log(t)
    s = 1.0
    if loops >= 2: s -= b1 * lt / (b0 ** 2 * t)
    if loops >= 3: s += (b1 ** 2 * (lt ** 2 - lt - 1) + b0 * b2) / (b0 ** 4 * t ** 2)
    if loops >= 4: s -= (b1 ** 3 * (lt ** 3 - 2.5 * lt ** 2 - 2 * lt + 0.5)
                         + 6 * b0 * b1 * b2 * lt - b0 ** 2 * b3) / (b0 ** 6 * t ** 3)
    return s / (b0 * t)

def lam(a, mu, n, loops):
    lo, hi = 1e-4, mu * 0.95
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if asym(math.log(mu ** 2 / mid ** 2), n, loops) > a: hi = mid
        else: lo = mid
    return math.sqrt(lo * hi)

MZ, MB, MC = 91.1876, 4.18, 1.27      # GeV; PDG values NAMED-NOT-READ in this stage
table = {}
for aZ in (0.1171, 0.1180, 0.1189):
    a5 = aZ
    a4 = run(a5, MZ, MB, 5)             # continuous matching at mu = m_b
    a3 = run(a4, MB, MC, 4)             # continuous matching at mu = m_c
    for loops in (1, 2, 3, 4):
        L5 = lam(a5, MZ, 5, loops); L4 = lam(a4, MB, 4, loops); L3 = lam(a3, MC, 3, loops)
        table[(aZ, loops)] = (L5, L4, L3)
print("\n   alpha_s(MZ) loops  Lambda5  Lambda4  Lambda3 [MeV]   M_p/L5  M_p/L4  M_p/L3")
for (aZ, loops), (L5, L4, L3) in sorted(table.items()):
    r = [M_P / 1000 / x for x in (L5, L4, L3)]
    print("   %.4f      %d    %7.1f  %7.1f  %7.1f        %5.2f   %5.2f   %5.2f"
          % (aZ, loops, L5 * 1e3, L4 * 1e3, L3 * 1e3, *r))
L5c, L4c, L3c = table[(0.1180, 4)]
chk("D1 4-loop Lambda5 at alpha_s=0.1180 in 200..220 MeV (sanity vs textbook ~210)",
    0.200 < L5c < 0.220)
r3 = M_P / 1000 / L3c
chk("D2 4-loop M_p/Lambda3 within 20%% of 3 (value %.3f)" % r3, abs(r3 / 3 - 1) < 0.20)
allr = [M_P / 1000 / x for vals in table.values() for x in vals]
print("   full span of M_p/Lambda over nf=3..5, loops 1..4, alpha_s 0.1171..0.1189: %.2f .. %.2f"
      % (min(allr), max(allr)))
r4loop = [M_P / 1000 / x for (aZ, lp), vals in table.items() if lp == 4 for x in vals]
print("   4-loop only, nf=3..5: %.2f .. %.2f" % (min(r4loop), max(r4loop)))
chk("D3 the factor is convention-dependent (nf, loop order) by more than 50%",
    max(allr) / min(allr) > 1.5)

# ---------------- E: tree consumes only the proportionality ----------------
import re, pathlib
src = pathlib.Path("/home/user/Claude-Method-Works/research/warp-drive/address.py").read_text()
hits = [i + 1 for i, l in enumerate(src.splitlines()) if re.search(r"3\s*\*?\s*Lambda", l)]
print("   address.py lines matching '3 Lambda':", hits)
chk("E1 the factor 3 appears in address.py only in the quoted comment (line 446)", hits == [446])

print("\n%d FAIL" % len(fails) if fails else "\nALL CHECKS PASS")
sys.exit(1 if fails else 0)
