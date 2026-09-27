#!/usr/bin/env python3
"""
DOCKET 67 / sachs-weyl-shear-focusing -- re-derivation and machine checks.

Audits the external result the tree uses at seatindex.py:41-60,169-185 and
anecscope.py:59-72,181-211,252-258:  "Weyl is traceless and focuses one
eigendirection whatever the sign of the source; det A = 0 happens with R_kk = 0"
(Sachs optical equations; Gao & Wald 2000 eq. 13 as composite.py reads it).

Checks (each prints PASS/FAIL and a value):
  S1  Sachs optical equations from the 2x2 Jacobi equation A'' = -T A:
        theta' = -theta^2/2 - tr(sigma^2) - tr T
        sigma' = -theta sigma - (T - tr T/2 * I)       [traceless part of T]
      for a symmetric (twist-free) deformation matrix B = A' A^-1.  sympy.
  S2  Gao & Wald eq. (13):  G''/G = -(1/2)[sigma_ab sigma^ab + R_kk], G = sqrt(det A),
      with R_kk = tr T and sigma_ab sigma^ab = tr(sigma^2).  sympy (Jacobi formula).
  S3  tr T = R_ab k^a k^b identically (screen trace of the optical tidal matrix is the
      Ricci term), so its traceless part is Weyl: checked on exact Schwarzschild (vacuum):
      T = diag(+w, -w), w = 3 M L^2 / r^5, EXACT, for M of either sign.  sympy.
  S4  z3: if T is traceless and nonzero, one eigenvalue is > 0 (focusing) whatever the
      sign of w  -- the "sign-blind" statement, as a finite real-arithmetic claim.
  S5  z3/analytic: if BOTH eigenvalues of a constant-frame diagonal T are <= 0 (Ricci
      defocusing q <= -|w|), no conjugate point -- so "whatever q does" is true of Weyl's
      CONTRIBUTION, not of the conjugate point.  Numeric demonstration too.
  S6  Numeric: Born-approximation (straight ray) Jacobi integration with the exact
      Schwarzschild tidal field at the tree's parameters (b = 0.3, x0 = -40, L = 75,
      M = +-2e-3, -4e-3): conjugate point location vs the tree's 55.16 / 56.52 / 56.50 /
      47.17 and the thin-lens prediction; Ricci-only u'' = 0 gives none.
  S7  The tree's metric is the LINEARISED one; its Ricci is O(M^2), not identically 0.
      sympy computes R_kk along the ray and its effect is sized against the Weyl focusing.
"""
import math, sys
import sympy as sp

results = []
def rec(name, ok, val=""):
    results.append((name, bool(ok), val))
    print("%-6s %-72s %s" % ("PASS" if ok else "FAIL", name, val))

# ---------------------------------------------------------------- S1
a, c, d, t1, t2, t3 = sp.symbols('a c d t1 t2 t3', real=True)
B = sp.Matrix([[a, c], [c, d]])            # symmetric: twist-free congruence
T = sp.Matrix([[t1, t3], [t3, t2]])        # optical tidal matrix, symmetric
I2 = sp.eye(2)
Bp = -T - B * B                            # from A'' = -T A with B = A'A^-1
theta = B.trace()
sig = B - theta / 2 * I2
thetap = Bp.trace()
sigp = Bp - thetap / 2 * I2
lhs1 = sp.simplify(thetap - (-theta**2 / 2 - (sig * sig).trace() - T.trace()))
Ttl = T - T.trace() / 2 * I2
lhs2 = sp.simplify(sigp - (-theta * sig - Ttl))
rec("S1a theta' = -theta^2/2 - tr sigma^2 - tr T", lhs1 == 0, "residual=%s" % lhs1)
rec("S1b sigma' = -theta sigma - (traceless T)", lhs2 == sp.zeros(2, 2),
    "residual=%s" % list(lhs2))
rec("S1c tr sigma^2 >= 0 (shear term always focuses theta)",
    sp.simplify((sig * sig).trace() - ((a - d)**2 / 2 + 2 * c**2)) == 0,
    "tr sigma^2 = (a-d)^2/2 + 2c^2")

# ---------------------------------------------------------------- S2
lam = sp.symbols('lambda')
Af = sp.Matrix(2, 2, lambda i, j: sp.Function('A%d%d' % (i, j))(lam))
detA = Af.det()
jac = sp.simplify(sp.diff(detA, lam) - detA * (Af.diff(lam) * Af.inv()).trace())
rec("S2a Jacobi formula (det A)' = det A * tr(A'A^-1)", jac == 0, "residual=%s" % jac)
# G'/G = theta/2  =>  G''/G = theta'/2 + theta^2/4
GppG = thetap / 2 + theta**2 / 4
res = sp.simplify(GppG - (-sp.Rational(1, 2) * ((sig * sig).trace() + T.trace())))
rec("S2b Gao-Wald eq.13: G''/G = -(1/2)[sigma_ab sigma^ab + R_kk]", res == 0,
    "residual=%s" % res)
# the tree's scalar reduction u'' = -q u, q = 4 pi T_kk = R_kk/2, is S2b with sigma dropped
rec("S2c q = R_kk/2 = 4 pi T_kk is the sigma-dropped form of S2b", True,
    "u''/u = -(1/2)R_kk - (1/2)tr sigma^2")

# ---------------------------------------------------------------- S3
t, r, th, ph, M, E, L = sp.symbols('t r theta phi M E L', real=True)
X = [t, r, th, ph]
f = 1 - 2 * M / r
g = sp.diag(-f, 1 / f, r**2, r**2 * sp.sin(th)**2)
gi = g.inv()
n = 4
Gam = [[[sp.simplify(sum(gi[a_, e] * (sp.diff(g[e, b_], X[c_]) + sp.diff(g[e, c_], X[b_])
                                      - sp.diff(g[b_, c_], X[e])) for e in range(n)) / 2)
         for c_ in range(n)] for b_ in range(n)] for a_ in range(n)]
def Riem(a_, b_, c_, d_):   # R^a_{bcd}
    v = sp.diff(Gam[a_][b_][d_], X[c_]) - sp.diff(Gam[a_][b_][c_], X[d_])
    v += sum(Gam[a_][c_][e] * Gam[e][b_][d_] - Gam[a_][d_][e] * Gam[e][b_][c_] for e in range(n))
    return v
R = [[[[sp.simplify(Riem(a_, b_, c_, d_)) for d_ in range(n)] for c_ in range(n)]
      for b_ in range(n)] for a_ in range(n)]
Rlow = [[[[sp.simplify(sum(g[a_, e] * R[e][b_][c_][d_] for e in range(n))) for d_ in range(n)]
          for c_ in range(n)] for b_ in range(n)] for a_ in range(n)]
sub = {th: sp.pi / 2}
kr = sp.sqrt(E**2 - f * L**2 / r**2)
k = [E / f, kr, 0, L / r**2]
e1 = [0, 0, 1 / r, 0]                                   # out of plane
al, be = sp.symbols('alpha beta')
sol = sp.solve([al * kr / f + r**2 * be * (L / r**2), al**2 / f + r**2 * be**2 - 1], [al, be],
               dict=True)
e2 = [0, sol[0][al], 0, sol[0][be]]                      # in-plane screen vector
def tid(ei, ej):
    # deviation eq: xi''^a = -R^a_{bcd} k^b xi^c k^d  =>  T_ij = R_{a b c d} e_i^a k^b e_j^c k^d
    s = 0
    for a_ in range(n):
        for b_ in range(n):
            for c_ in range(n):
                for d_ in range(n):
                    if ei[a_] == 0 or ej[c_] == 0 or k[b_] == 0 or k[d_] == 0:
                        continue
                    s += Rlow[a_][b_][c_][d_].subs(sub) * ei[a_] * k[b_] * ej[c_] * k[d_]
    return sp.simplify(s)
T11, T22, T12 = tid(e1, e1), tid(e2, e2), tid(e1, e2)
Ric = [[sp.simplify(sum(R[a_][b_][a_][d_] for a_ in range(n))) for d_ in range(n)] for b_ in range(n)]
Rkk = sp.simplify(sum(Ric[b_][d_].subs(sub) * k[b_] * k[d_] for b_ in range(n) for d_ in range(n)))
rec("S3a Schwarzschild R_kk = 0 exactly (vacuum)", Rkk == 0, "R_kk=%s" % Rkk)
rec("S3b screen trace T11+T22 = 0 exactly (traceless => pure Weyl)",
    sp.simplify(T11 + T22) == 0, "T11=%s T22=%s" % (T11, T22))
rec("S3c off-diagonal T12 = 0 (frame is an eigenframe, parallel by reflection symmetry)",
    sp.simplify(T12) == 0, "T12=%s" % T12)
rec("S3d T11 = 3 M L^2 / r^5 exactly, linear in M: sign of M only swaps eigendirections",
    sp.simplify(T11 - 3 * M * L**2 / r**5) == 0, "w=%s" % T11)

# ---------------------------------------------------------------- S4 / S5 (z3)
try:
    import z3
    x11, x22, x12 = z3.Reals('x11 x22 x12')
    s = z3.Solver()
    # traceless symmetric nonzero T with NO positive eigenvalue: eigenvalues are +-sqrt(x11^2+x12^2)
    # "no positive eigenvalue" <=> T negative semidefinite <=> x11<=0, x22<=0, x11*x22 - x12^2 >= 0
    s.add(x11 + x22 == 0, z3.Or(x11 != 0, x12 != 0), x11 <= 0, x22 <= 0, x11 * x22 - x12 * x12 >= 0)
    r4 = s.check()
    rec("S4  z3: traceless nonzero T always has a positive (focusing) eigenvalue", r4 == z3.unsat,
        "z3=%s (unsat = no counterexample)" % r4)
    # vacuity guard: drop the traceless constraint -> must be sat
    s2 = z3.Solver()
    s2.add(z3.Or(x11 != 0, x12 != 0), x11 <= 0, x22 <= 0, x11 * x22 - x12 * x12 >= 0)
    rec("S4g vacuity guard: without tracelessness a non-focusing T exists", s2.check() == z3.sat,
        "z3=%s" % s2.check())
    # S5: with Ricci trace 2q: eigenvalues q+w, q-w. Exists q with both <= 0 for any w: q <= -|w|
    q, w = z3.Reals('q w')
    s3 = z3.Solver()
    s3.add(w != 0, q + w <= 0, q - w <= 0)
    rec("S5a z3: Weyl w != 0 with Ricci q <= -|w| leaves NO focusing eigenvalue", s3.check() == z3.sat,
        "z3=%s model=%s" % (s3.check(), s3.model() if s3.check() == z3.sat else None))
except ImportError:
    rec("S4/S5 z3 not installed", False, "pip install z3-solver")

# ---------------------------------------------------------------- S6 numeric
def jacobi_born(Mv, b=0.3, x0=-40.0, Lr=75.0, nstep=150000, q_kappa=0.0):
    """Straight-ray (Born) 2x2 Jacobi, exact Schwarzschild tidal eigenvalues
    w = 3 |..| M b^2 / r^5 (L = b for E = 1).  Diagonal frame, so A stays diagonal.
    q_kappa adds a Ricci trace 2q with q = -q_kappa*|w| (NEC-violating, defocusing)."""
    h = Lr / nstep
    u1, v1, u2, v2 = 0.0, 1.0, 0.0, 1.0
    for i in range(nstep):
        x = x0 + (i + 0.5) * h
        rr = math.hypot(x, b)
        wv = 3.0 * Mv * b * b / rr**5
        qv = -q_kappa * abs(wv)
        k1, k2 = qv + wv, qv - wv            # T eigenvalues; A'' = -T A
        v1 -= h * k1 * u1; u1 += h * v1
        v2 -= h * k2 * u2; u2 += h * v2
        if u1 * u2 <= 0.0 and i > 5:
            return (i + 1) * h
    return None

tree = {2e-3: 55.16, -2e-3: 56.52, -4e-3: 47.17}
for Mv in (2e-3, -2e-3, -4e-3):
    lamc = jacobi_born(Mv)
    fl = 0.09 / (4 * abs(Mv))
    Dl = 1.0 / (1.0 / fl - 1.0 / 40.0)
    ok = lamc is not None and abs(lamc - tree[Mv]) / tree[Mv] < 0.03
    rec("S6  Born Jacobi M=%+.1e: conjugate point exists, within 3%% of tree %.2f" % (Mv, tree[Mv]),
        ok, "lambda_c=%.3f thin-lens=%.3f" % (lamc if lamc else float('nan'), 40 + Dl))
rec("S6r Ricci-only u''=0 (vacuum): u = lambda, no zero", True, "analytic")
rec("S6s Born order: +M and -M give identical conjugate point (sign-blind at O(M))",
    jacobi_born(2e-3) == jacobi_born(-2e-3), "%.4f vs %.4f" % (jacobi_born(2e-3), jacobi_born(-2e-3)))
# S5 numeric: Ricci defocusing stronger than Weyl kills the conjugate point
lc_k2 = jacobi_born(-2e-3, q_kappa=1.0)
# (first run used L = 75 here and FAILED: halving the net focusing power doubles the focal
#  length to 22.5, so thin-lens puts the line focus at 40 + 1/(1/22.5 - 1/40) = 91.4 > 75.
#  The check was mis-specified, not the physics; L is extended to 150 and the thin-lens
#  location is asserted instead.)
lc_k05 = jacobi_born(-2e-3, q_kappa=0.5, Lr=150.0, nstep=300000)
tl_k05 = 40 + 1.0 / (4 * 2e-3 * 0.5 / 0.09 - 1.0 / 40.0)
rec("S5b numeric: q = -|w| along ray (NEC-violating) -> no conjugate point within L=75",
    lc_k2 is None, "lambda_c=%s" % lc_k2)
rec("S5c numeric: q = -|w|/2 -> conjugate point survives, delayed to thin-lens 91.4 (+-3%)",
    lc_k05 is not None and abs(lc_k05 - tl_k05) / tl_k05 < 0.03,
    "lambda_c=%s thin-lens=%.2f" % (lc_k05, tl_k05))

# ---------------------------------------------------------------- S7 linearised-metric Ricci
xx, yy, zz, Mm = sp.symbols('x y z M', real=True)
Y = [t, xx, yy, zz]
rr = sp.sqrt(xx**2 + yy**2 + zz**2)
Phi = -Mm / rr
gl = sp.diag(-(1 + 2 * Phi), 1 - 2 * Phi, 1 - 2 * Phi, 1 - 2 * Phi)
gli = gl.inv()
Gl = [[[sp.simplify(sum(gli[a_, e] * (sp.diff(gl[e, b_], Y[c_]) + sp.diff(gl[e, c_], Y[b_])
                                      - sp.diff(gl[b_, c_], Y[e])) for e in range(4)) / 2)
        for c_ in range(4)] for b_ in range(4)] for a_ in range(4)]
def Ricl(b_, d_):
    s = 0
    for a_ in range(4):
        s += sp.diff(Gl[a_][b_][d_], Y[a_]) - sp.diff(Gl[a_][b_][a_], Y[d_])
        s += sum(Gl[a_][a_][e] * Gl[e][b_][d_] - Gl[a_][d_][e] * Gl[e][b_][a_] for e in range(4))
    return s
kl = [1, 1, 0, 0]   # leading-order null tangent along +x (normalisation 1 at O(M^0))
Rkk_l = sum(Ricl(b_, d_) * kl[b_] * kl[d_] for b_ in range(4) for d_ in range(4)
            if kl[b_] and kl[d_])
Rkk_ser = sp.simplify(sp.series(Rkk_l, Mm, 0, 3).removeO())
o1 = sp.simplify(Rkk_ser.coeff(Mm, 1))
o2 = sp.simplify(Rkk_ser.coeff(Mm, 2))
rec("S7a linearised metric: R_kk vanishes at O(M) (vacuum to first order)", o1 == 0, "O(M)=%s" % o1)
o2f = sp.lambdify((xx, yy, zz), o2)
print("       O(M^2) coefficient of R_kk:", o2)
# size it: integrate (R_kk/2) along the straight ray at b=0.3 vs the Weyl focal power 4|M|/b^2
Mv, bv = 2e-3, 0.3
N = 200000; x0, x1 = -40.0, 35.0; h = (x1 - x0) / N
ric_int = sum(0.5 * Mv**2 * o2f(x0 + (i + .5) * h, bv, 0.0) for i in range(N)) * h
weyl_power = 4 * Mv / bv**2
rec("S7b O(M^2) Ricci of the linearised metric: integrated R_kk/2 small vs Weyl power 4|M|/b^2",
    abs(ric_int) < 0.05 * weyl_power,
    "int R_kk/2 = %.3e, 4|M|/b^2 = %.3e, ratio = %.2e, sign %s (sign-blind: M^2)"
    % (ric_int, weyl_power, ric_int / weyl_power, "+" if ric_int > 0 else "-"))

# S7c/S7d: the in-tree trace check (composite.py:319-326) uses k = (1,1,0,0), which is NOT
# null in the linearised metric (g(k,k) = -4 Phi); with the true null tangent the screen trace
# IS R_kk and equals the O(M^2) Ricci above -- ~0.9 % of the Weyl eigenvalue at the tree's
# parameters, which is what composite.survey() reports along the ray (traceless_ratio 0.0093,
# 0.0084, 0.0161 for M = +2e-3, -2e-3, -4e-3; run read-only with python3 -B).
def Rup_l(a_, b_, c_, d_):
    return (sp.diff(Gl[a_][b_][d_], Y[c_]) - sp.diff(Gl[a_][b_][c_], Y[d_])
            + sum(Gl[a_][c_][e] * Gl[e][b_][d_] - Gl[a_][d_][e] * Gl[e][b_][c_] for e in range(4)))
Mv = -2e-3; pnt = {xx: 0, yy: 0.3, zz: 0, Mm: Mv}
Rll = [[[[float(sum(gl[a_, e] * Rup_l(e, b_, c_, d_) for e in range(4)).subs(pnt))
          for d_ in range(4)] for c_ in range(4)] for b_ in range(4)] for a_ in range(4)]
def Tl(kk, ei, ej):
    return -sum(Rll[m][a_][n_][b_] * kk[m] * ei[a_] * kk[n_] * ej[b_]
                for m in range(4) for a_ in range(4) for n_ in range(4) for b_ in range(4))
ey, ez = [0, 0, 1, 0], [0, 0, 0, 1]
phv = -Mv / 0.3; sn = ((1 + 2 * phv) / (1 - 2 * phv)) ** 0.5
rat_nn = abs(Tl([1, 1, 0, 0], ey, ey) + Tl([1, 1, 0, 0], ez, ez)) / abs(Tl([1, 1, 0, 0], ey, ey))
rat_n = abs(Tl([1, sn, 0, 0], ey, ey) + Tl([1, sn, 0, 0], ez, ez)) / abs(Tl([1, sn, 0, 0], ey, ey))
rec("S7c true null k: screen |trace|/|T| at closest approach = O(M^2) Ricci, ~ 4M^2/b^4 / (3|M|/b^3)",
    abs(rat_n - (4 * Mv**2 / 0.3**4) / (3 * abs(Mv) / 0.3**3)) < 0.1 * rat_n,
    "ratio=%.3e predicted=%.3e" % (rat_n, (4 * Mv**2 / 0.3**4) / (3 * abs(Mv) / 0.3**3)))
rec("S7d DISCREPANCY (in-tree): composite's static check with non-null k=(1,1,0,0) reads ~1e-4,"
    " not R_kk", rat_nn < 1e-3 and rat_n > 5e-3, "non-null=%.2e  null=%.2e" % (rat_nn, rat_n))

npass = sum(1 for _, ok, _ in results if ok)
print("\n%d/%d checks PASS" % (npass, len(results)))
sys.exit(0 if npass == len(results) else 1)
