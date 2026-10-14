#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key 'feynman-hellmann' (massform.py:764-766, 1790-1793).
Read-only against research/warp-drive (imports massform for its own numbers). sympy + numpy-free numerics.
Checks:
 T1  FH theorem, finite-dim, symbolic: dE/dlam = <psi|dH/dlam|psi> for a non-degenerate eigenvalue (2x2 general real-symmetric).
 T2  FH, numeric: random 6x6 Hermitian H0 + lam V, central difference vs expectation (mpmath, 30 digits).
 T3  Non-degeneracy hypothesis is load-bearing: at a crossing the ordered ground eigenvalue has a kink (left/right derivatives differ).
 T4  Euler identity for M = Lam F(m/Lam): sum_q m_q dM/dm_q + Lam dM/dLam = M, so at fixed Lam the first-order quark-mass
     response is sum sigma_q / M and 'the rest' (Lam dM/dLam) is 1 - f  -- the tree's 'at first order the rest is QCD'.
 T5  WHICH QCD scale: LO decoupling Lam3 = Lam6^(21/27) (mc mb mt)^(2/27). With all m_q ∝ v and Lam6 fixed,
     dlnM/dlnv = 2/9 + (7/9) f_l, per heavy quark (2/27)(1-f_l) -- reproduces massform.coupling_sum / svz_heavy_sum.
     With Lam3 fixed instead it is f_l.  The two readings of H-LINEAR's 'QCD scale held fixed'.
 T6  First order != finite even for light quarks: model M = M0 + a m + b m^(3/2) (chiral m_pi^3 term) -> sigma - DeltaM = b m^(3/2)/2.
 T7  Numbers: tree's f_l; the adverse first-order figures (ETM19 sigma_c via Lam4 route, +3 sigma), threshold sigma-sum for 1/2.
"""
import sys, random
from fractions import Fraction
import sympy as sp
import mpmath as mp

sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
ok = True
def check(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  -- " + detail if detail else ""))

# T1 ---------------------------------------------------------------------
a, b, c, d, e, f, lam = sp.symbols('a b c d e f lam', real=True)
H = sp.Matrix([[a + lam*d, b + lam*e], [b + lam*e, c + lam*f]])
V = H.diff(lam)
disc = sp.sqrt(((a + lam*d) - (c + lam*f))**2 + 4*(b + lam*e)**2)
Eminus = ((a + lam*d) + (c + lam*f) - disc)/2
# eigenvector of Eminus (unnormalized)
vec = sp.Matrix([b + lam*e, Eminus - (a + lam*d)])
expval = (vec.T*V*vec)[0]/(vec.T*vec)[0]
diff = sp.simplify(sp.diff(Eminus, lam) - expval)
# check symbolically, then at random rational points with disc != 0
pts_ok = True
rnd = random.Random(67)
for _ in range(20):
    sub = {s: sp.Rational(rnd.randint(-9, 9), rnd.randint(1, 5)) for s in (a, b, c, d, e, f, lam)}
    if sub[b] + sub[lam]*sub[e] == 0:
        continue
    pts_ok &= sp.nsimplify(sp.N(diff.subs(sub), 40)) == 0
check("T1 FH 2x2 symbolic (non-degenerate branch)", diff == 0 or pts_ok, "simplify->%s; 20 rational points zero=%s" % (diff if diff == 0 else "nonzero-form", pts_ok))

# T2 ---------------------------------------------------------------------
mp.mp.dps = 30
n = 6
rnd = random.Random(2026)
def herm():
    M = mp.matrix(n, n)
    for i in range(n):
        for j in range(i, n):
            if i == j:
                M[i, i] = mp.mpf(rnd.uniform(-1, 1))
            else:
                z = mp.mpc(rnd.uniform(-1, 1), rnd.uniform(-1, 1))
                M[i, j] = z; M[j, i] = mp.conj(z)
    return M
H0, V6 = herm(), herm()
def ground(l):
    E, Q = mp.eighe(H0 + l*V6)
    k = min(range(n), key=lambda i: mp.re(E[i]))
    return mp.re(E[k]), Q[:, k]
l0, h = mp.mpf('0.3'), mp.mpf('1e-10')
E0, psi = ground(l0)
fd = (ground(l0 + h)[0] - ground(l0 - h)[0])/(2*h)
ev = mp.re((psi.H*V6*psi)[0])
check("T2 FH numeric 6x6 Hermitian ground state", abs(fd - ev) < mp.mpf('1e-15'), "dE/dlam=%s <V>=%s" % (mp.nstr(fd, 18), mp.nstr(ev, 18)))

# T3 ---------------------------------------------------------------------
# H(lam) = diag(lam, -lam): ground = -|lam|, degenerate at 0; left derivative +1, right -1.
Eg = lambda l: min(l, -l)
hl = 1e-8
left = (Eg(0) - Eg(-hl))/hl; right = (Eg(hl) - Eg(0))/hl
check("T3 degeneracy: ordered ground eigenvalue not differentiable at crossing", left != right, "left=%g right=%g (FH needs an isolated level)" % (left, right))

# T4 ---------------------------------------------------------------------
L, m1, m2, m3 = sp.symbols('Lambda m1 m2 m3', positive=True)
F = sp.Function('F')
M = L*F(m1/L, m2/L, m3/L)
euler = sp.simplify(m1*M.diff(m1) + m2*M.diff(m2) + m3*M.diff(m3) + L*M.diff(L) - M)
check("T4 Euler: sum m dM/dm + Lam dM/dLam = M for M = Lam F(m/Lam)", euler == 0, "residual=%s" % euler)

# T5 ---------------------------------------------------------------------
Lam6, mc, mb, mt, v, fl = sp.symbols('Lambda6 m_c m_b m_t v f_l', positive=True)
def b0(nf): return sp.Rational(11) - sp.Rational(2, 3)*nf
# LO matching Lam_{nf-1}^{b0(nf-1)} = Lam_nf^{b0(nf)} m^{b0(nf-1)-b0(nf)}
Lam5 = (Lam6**b0(6)*mt**(b0(5)-b0(6)))**(1/b0(5))
Lam4 = (Lam5**b0(5)*mb**(b0(4)-b0(5)))**(1/b0(4))
Lam3 = sp.simplify((Lam4**b0(4)*mc**(b0(3)-b0(4)))**(1/b0(3)))
ex = {s: sp.simplify(sp.diff(sp.log(Lam3), s)*s) for s in (Lam6, mc, mb, mt)}
check("T5a LO decoupling exponents Lam3 = Lam6^(7/9)(mc mb mt)^(2/27)",
      ex[Lam6] == sp.Rational(21, 27) and all(ex[s] == sp.Rational(2, 27) for s in (mc, mb, mt)), str(ex))
# M = Lam3 * G(m_l/Lam3); f_l = dlnM/dln m_l at fixed Lam3; all masses ∝ v; Lam6 fixed:
dlnLam3_dlnv = ex[mc] + ex[mb] + ex[mt]
resp_L6 = sp.simplify(fl*(1 - dlnLam3_dlnv) + dlnLam3_dlnv)
check("T5b dlnM/dlnv at fixed Lam6 = 2/9 + (7/9) f_l", sp.simplify(resp_L6 - (sp.Rational(2, 9) + sp.Rational(7, 9)*fl)) == 0, str(resp_L6))
check("T5c per heavy quark (2/27)(1-f_l) (SVZ LO)", sp.simplify(ex[mc]*(1 - fl) - sp.Rational(2, 27)*(1 - fl)) == 0)
import massform as mf
for k, x in mf.F_LIGHT.items():
    xs = Fraction(x)
    check("T5d massform.coupling_sum agrees (%s)" % k, mf.coupling_sum(xs) == Fraction(2, 9) + Fraction(7, 9)*xs
          and mf.svz_heavy_sum(xs) == 3*Fraction(2, 27)*(1 - xs), "f_l=%.5f -> fixed-Lam3 %.4f ; fixed-Lam6 %.4f" % (x, x, float(mf.coupling_sum(xs))))

# T6 ---------------------------------------------------------------------
m, M0, A, B = sp.symbols('m M0 A B', real=True)
Mm = M0 + A*m + B*m**sp.Rational(3, 2)
sigma = sp.simplify(m*Mm.diff(m)); dM = sp.simplify(Mm - M0)
check("T6 sigma - DeltaM = B m^(3/2)/2 (first order != finite unless B=0)", sp.simplify(sigma - dM - B*m**sp.Rational(3, 2)/2) == 0, "sigma=%s ; DeltaM=%s" % (sigma, dM))
# illustration only (coefficient NAMED-NOT-READ: O(p^3) HBChPT term -3 gA^2 mpi^3/(32 pi fpi^2); gA, fpi, mpi PDG NAMED-NOT-READ)
gA, fpi, mpi = 1.2754, 92.07, 138.04
Bterm = -3*gA**2*mpi**3/(32*mp.pi*fpi**2)
print("INFO T6 illustration: O(p^3) m_pi^3 term = %.2f MeV -> sigma_piN - DeltaM_light = %.2f MeV at that order (NOT a result; higher orders not included)" % (float(Bterm), float(Bterm)/2))

# T7 ---------------------------------------------------------------------
MN = mf.M_N_MEV
f21, f211 = mf.F_LIGHT["FLAG 2+1"], mf.F_LIGHT["FLAG 2+1+1"]
check("T7a f_l reproduced: FLAG 2+1 9.28 %, 2+1+1 10.85 %", abs(f21 - (42.2 + 44.9)/MN) < 1e-12 and abs(f211 - (60.9 + 41.0)/MN) < 1e-12,
      "m_N=%.4f MeV; %.4f %.4f" % (MN, f21, f211))
# Lam4 route with lattice charm (ETM19 107(22)): Lam4 = Lam6^(21/25)(mb mt)^(2/25): dlnM/dlnv = f4 + (4/25)(1-f4)
def lam4_route(spin, ss, sc):
    f4 = (spin + ss + sc)/MN
    return f4 + Fraction(4, 25)*(1 - f4)
ele = mf.share_rows()[0][2]
central = float(lam4_route(60.9, 41.0, 107.0))
plus3 = float(lam4_route(60.9 + 3*6.5, 41.0 + 3*8.8, 107.0 + 3*22.0))
print("INFO T7b first-order dlnM_N/dlnv at fixed Lam6, lattice charm ETM19 via Lam4 route: central %.4f ; FLAG 2+1+1 and ETM19 each +3 sigma linearly %.4f ; + electrons %.5f" % (central, plus3, ele))
check("T7c every first-order reading < 1/2 (incl. adverse +3 sigma, electrons added)", central + ele < 0.5 and plus3 + ele < 0.5 and mf.HIGGS_SHARE_LARGEST_ALL < 0.5)
# thresholds: sigma sum needed for a first-order share of 1/2
thr_L3 = 0.5*MN; thr_L6 = float(Fraction(5, 14))*MN; thr_L4 = (0.5 - 4/25)/(1 - 4/25)*MN
print("INFO T7d sigma-sum needed for first-order share 1/2: fixed Lam3 %.0f MeV ; fixed Lam6 via SVZ %.0f MeV (u+d+s) ; Lam4 route %.0f MeV (u+d+s+c)" % (thr_L3, thr_L6, thr_L4))
# data moves: Hoferichter 59.1(3.5) and ~56 isospin-corrected (READ by sibling sigma-term-scan), sigma_s 28.6 (Mainz 23) .. 44.9
for lab, spin, ss in (("HRKM15 59.1 + FLAG s 44.9", 59.1, 44.9), ("~56 + 44.9", 56.0, 44.9), ("Mainz23 43.7+28.6", 43.7, 28.6)):
    fx = (spin + ss)/MN
    print("INFO T7e %-26s f_l=%.4f  fixed-Lam6 %.4f" % (lab, fx, float(Fraction(2, 9) + Fraction(7, 9)*Fraction(fx))))
print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
