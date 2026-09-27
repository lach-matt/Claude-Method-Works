#!/usr/bin/env python3
"""DOCKET 67 -- audit of 'ew-symmetry-restoration-crossover'.

What this checks (everything here is finite or closed-form):

  A. ARITHMETIC of the tree's figure.  warpfolder.py:230 T_EW_CROSSOVER_GEV =
     160.0 (ORDER), printed at :392-394 as K; massform.py's READ value is
     1508.07161's T_c = 159.5 +/- 1.5 GeV.  Is 160 inside the band, and do the
     kelvin conversions reproduce (1.857e15 K; 1.851e15 K)?

  B. DIRECTION (sympy).  The leading high-T one-loop thermal correction in the
     SM, Delta V = T^2/24 sum_b n_b m_b^2(phi) + T^2/48 sum_f n_f m_f^2(phi),
     summed over W(6) Z(3) h(1) G(3) t(12) with tree field-dependent masses.
     STATUS OF THIS FORM: RECONSTRUCTED (textbook high-T expansion; not READ at
     source in this stage).  It is used ONLY to check the sign / direction the
     tree asserts ('heating restores'), never to replace the lattice T_c.
     Checks: the phi^2 coefficient c = (3g^2+g'^2+4y_t^2+8 lam)/16 derived from
     dof counting, c > 0 for every real coupling with lam > 0 (z3 if present),
     and the mean-field T0 = sqrt(mu^2/c) at the PDG-2026 capture's masses.

  C. CROSSOVER NOT FIRST ORDER.  1508.07161 p.1 (READ in DOCKET 65, recorded in
     wk4xpcbq7.output): first order only for m_H <~ 72 GeV.  m_H from the
     tree's captures/PDG-2026.tsv (READ): 125.13 GeV.

  D. SENSITIVITY of the mean-field T0 to the moved masses (m_H 125 -> 125.13,
     m_t 173 -> 172.6), against the lattice's own 1.5 GeV systematic.

  E. SCOPE (the hypothesis the tree keeps implicitly: ONE Higgs doublet).  A
     two-real-scalar potential with a negative cross coupling, bounded below,
     has a NEGATIVE thermal mass for one field: high T need not restore a
     symmetry outside the SM (Weinberg 1974 -- NAMED-NOT-READ; the example is
     computed here, not quoted).
"""
import math, os, sys
import sympy as sp

FAIL = []
def chk(name, ok):
    print("  [%s] %s" % ("ok" if ok else "FAIL", name))
    if not ok:
        FAIL.append(name)

KB_EV = 8.617333262e-5          # eV/K (CODATA exact-derived: k_B/e)

# ------------------------------------------------------------------ A
print("A. arithmetic")
T_TREE, T_READ, T_ERR = 160.0, 159.5, 1.5
T_SEC7, T_SEC7_SYS = 159.6, 1.5
k_tree = T_TREE * 1e9 / KB_EV
k_read = T_READ * 1e9 / KB_EV
print("   160 GeV = %.4e K ; 159.5 GeV = %.4e K" % (k_tree, k_read))
chk("160 GeV = 1.857e15 K (warpfolder.py:392 print)", abs(k_tree / 1.857e15 - 1) < 5e-4)
chk("159.5 GeV = 1.851e15 K (massform.py:545)", abs(k_read / 1.851e15 - 1) < 5e-4)
chk("160 lies inside 159.5 +/- 1.5 (abstract)", abs(T_TREE - T_READ) <= T_ERR)
chk("160 lies inside 159.6 +/- 0.1 +/- 1.5 (Sec. VII)", abs(T_TREE - T_SEC7) <= math.hypot(0.1, T_SEC7_SYS))
print("   deviation 160 - 159.5 = %.1f GeV = %.2f sigma" % (T_TREE - T_READ, (T_TREE - T_READ) / T_ERR))

# ------------------------------------------------------------------ B
print("B. direction of the thermal correction (sympy)")
g, gp, yt, lam, mu2, phi, T = sp.symbols("g gp y_t lam mu2 phi T", positive=True)
mW2 = g**2 * phi**2 / 4
mZ2 = (g**2 + gp**2) * phi**2 / 4
mh2 = 3 * lam * phi**2 - mu2
mG2 = lam * phi**2 - mu2
mt2 = yt**2 * phi**2 / 2
dV = T**2 / 24 * (6 * mW2 + 3 * mZ2 + 1 * mh2 + 3 * mG2) + T**2 / 48 * (12 * mt2)
V0 = -mu2 * phi**2 / 2 + lam * phi**4 / 4
V = sp.expand(V0 + dV)
m2T = sp.simplify(2 * sp.Poly(V, phi).coeff_monomial(phi**2))   # V = 1/2 m^2(T) phi^2 + ...
c = sp.simplify((m2T + mu2) / T**2)
c_ref = (3 * g**2 + gp**2 + 4 * yt**2 + 8 * lam) / 16
print("   m^2(T) =", m2T)
chk("c = (3g^2 + g'^2 + 4y_t^2 + 8 lam)/16 from dof counting", sp.simplify(c - c_ref) == 0)
chk("d m^2(T) / d T^2 = c > 0 symbolically (all couplings positive)", sp.ask(sp.Q.positive(c)) is True or c.is_positive)

try:
    import z3
    G, GP, YT, L = z3.Reals("G GP YT L")
    s = z3.Solver()
    s.add(L > 0, (3 * G * G + GP * GP + 4 * YT * YT + 8 * L) / 16 <= 0)
    r = s.check()
    chk("z3: no real (g, g', y_t) and lam > 0 give c <= 0  [%s]" % r, r == z3.unsat)
    s2 = z3.Solver()                       # vacuity guard: the box is not empty
    s2.add(L > 0, (3 * G * G + GP * GP + 4 * YT * YT + 8 * L) / 16 > 0)
    chk("z3 vacuity guard: the hypothesis set is satisfiable", s2.check() == z3.sat)
except ImportError:
    print("   z3 not installed; symbolic positivity above stands alone")


def pdg_capture():
    p = "/home/user/Claude-Method-Works/research/warp-drive/captures/PDG-2026.tsv"
    out = {}
    for ln in open(p):
        if ln.startswith("#"):
            continue
        f = ln.rstrip("\n").split("\t")
        if f[0] in ("6", "23", "24", "25"):
            out[int(f[0])] = float(f[11]) / 1000.0
    return out


M = pdg_capture()
mt, mZ, mW, mH = M[6], M[23], M[24], M[25]
GF = 1.1663788e-5                         # GeV^-2 -- NAMED-NOT-READ (as higgs.py:209)
v = (math.sqrt(2) * GF) ** -0.5
print("   PDG-2026 capture (READ): m_t=%.2f m_Z=%.4f m_W=%.3f m_H=%.2f ; v=%.3f (G_F, NAMED-NOT-READ)"
      % (mt, mZ, mW, mH, v))


def T0(mH_, mt_, mW_=mW, mZ_=mZ, v_=v):
    g_ = 2 * mW_ / v_
    gp_ = 2 * math.sqrt(mZ_**2 - mW_**2) / v_
    yt_ = math.sqrt(2) * mt_ / v_
    lam_ = mH_**2 / (2 * v_**2)
    c_ = (3 * g_**2 + gp_**2 + 4 * yt_**2 + 8 * lam_) / 16
    return math.sqrt(lam_ * v_**2 / c_), c_


t0, cnum = T0(mH, mt)
print("   c = %.4f ; mean-field T0 = %.1f GeV  (lattice T_c 159.5 +/- 1.5, READ)" % (cnum, t0))
chk("mean-field T0 is O(100 GeV) and below the lattice T_c (a model, ORDER only)", 100 < t0 < T_READ)

# ------------------------------------------------------------------ C
print("C. crossover, not first order")
MH_ENDPOINT = 72.0                         # 1508.07161 p.1, READ (DOCKET 65 record)
chk("m_H(PDG-2026) = %.2f > 72 GeV endpoint by factor %.2f" % (mH, mH / MH_ENDPOINT), mH > MH_ENDPOINT)
chk("m_H(PDG-2026) - 72 GeV = %.1f GeV >> any m_H uncertainty" % (mH - MH_ENDPOINT), mH - MH_ENDPOINT > 50)

# ------------------------------------------------------------------ D
print("D. sensitivity of mean-field T0 to moved masses (model, ORDER)")
base, _ = T0(125.0, 173.0)
d_mh = T0(125.13, 173.0)[0] - base
d_mt = T0(125.0, 172.6)[0] - base
print("   T0(125.0,173.0)=%.2f ; dT0 from m_H 125.0->125.13: %+.3f GeV ; from m_t 173.0->172.6: %+.3f GeV"
      % (base, d_mh, d_mt))
chk("each mass move shifts T0 by < 1.5 GeV (the lattice systematic)",
    abs(d_mh) < 1.5 and abs(d_mt) < 1.5)
# sensitivity of the endpoint conclusion: m_H would need to fall by >50 GeV

# ------------------------------------------------------------------ E
print("E. scope: two real scalars with negative cross coupling (non-restoration)")
l1, l2, l12 = 0.1, 4.0, -0.5               # chosen; bounded below needs l1,l2>0 and l12 > -sqrt(l1 l2)
bounded = l1 > 0 and l2 > 0 and l12 > -math.sqrt(l1 * l2)
# V = l1/4 p1^4 + l2/4 p2^4 + l12/2 p1^2 p2^2 ; high-T mass^2 of p1: T^2/24 * d2V/dp1^2 summed over dof
p1, p2 = sp.symbols("p1 p2", real=True)
VV = sp.Rational(1, 4) * l1 * p1**4 + sp.Rational(1, 4) * l2 * p2**4 + sp.Rational(1, 2) * l12 * p1**2 * p2**2
M2 = sp.hessian(VV, (p1, p2))
trM2 = sp.expand(M2.trace())                # sum of field-dependent masses^2
c1 = sp.Poly(trM2, p1, p2).coeff_monomial(p1**2) / 24   # T^2 coefficient in (1/2) m1^2(T) p1^2
print("   bounded below: %s ; thermal phi1^2 coefficient ~ %.4f T^2" % (bounded, float(c1)))
chk("a bounded-below 2-scalar model can have a NEGATIVE thermal mass (restoration is model-dependent)",
    bounded and float(c1) < 0)

print()
print("RESULT: %d check(s) failed" % len(FAIL) if FAIL else "RESULT: all checks passed")
sys.exit(1 if FAIL else 0)
