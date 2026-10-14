#!/usr/bin/env python3
"""
DOCKET 67, audit 16 of 286 -- Gao & Wald, gr-qc/0007021 (CQG 17, 4999 (2000)).

Re-derives and machine-checks the finite / closed-form parts of what the
warp board takes from this paper:

  (A) eq. (13)  G''/G = -(1/2)[sigma_ab sigma^ab + R_ab k^a k^b]  from the
      irrotational null Raychaudhuri equation, with G = (det A)^{1/(n-2)};
      the 1/2 is the n = 4 value of 1/(n-2)  (sympy, symbolic in n).
  (B) Lemma 1's core step: NEC  =>  G'' <= 0 on (0, lambda_0), so a solution
      with G(0) = 0, G > 0 then G(lambda_0) = 0 is concave; z3 checks the
      finite-difference shadow of the concavity argument.
  (C) composite.py's use: with A'' = -T A, A(0) = 0, A'(0) = I on a 2-screen,
      a TRACELESS symmetric T (pure Weyl, vacuum) gives det A(lambda; -T) =
      det A(lambda; T) EXACTLY, because -T = R T R^T with R the 90-degree
      rotation.  Sign-blindness is an identity in 4 dimensions, stronger
      than 'quadratic in the source'.  Checked symbolically and numerically,
      with a rotating eigenframe to make sure the identity is not an artefact
      of a diagonal T.
  (D) The contrast: a pure-trace T (Ricci) is NOT sign-blind -- +r reaches a
      conjugate point at pi/sqrt(r), -r never does.
  (E) The linear / quadratic statement: with T = M * T1, tr T (= R_kk) is
      linear in M and the shear scalar is quadratic in M.

Writes nothing to research/.  stdlib + sympy + z3.  Exit 1 on any failure.
"""
import math, sys
import sympy as sp

ok = True
def chk(label, cond):
    global ok
    ok &= bool(cond)
    print("  %-72s %s" % (label, "ok" if cond else "FAIL"))

# ---------------------------------------------------------------- (A)
print("(A) eq. (13) from Raychaudhuri, G = (det A)^{1/(n-2)}")
lam, n = sp.symbols("lambda n", positive=True)
detA = sp.Function("D")(lam)               # det A(lambda) > 0 on (0, lambda_0)
sigma2, Rkk = sp.symbols("sigma2 R_kk", real=True)
theta = sp.diff(detA, lam) / detA          # theta = (ln det A)'  (irrotational)
# irrotational null Raychaudhuri in n dimensions (Galloway math/9909158 eq. 2.4;
# Wald 9.2.32 for n = 4):  theta' = -theta^2/(n-2) - sigma^2 - R_kk
ray = sp.Eq(sp.diff(theta, lam), -theta**2 / (n - 2) - sigma2 - Rkk)
G = detA ** (1 / (n - 2))
GppG = sp.simplify(sp.diff(G, lam, 2) / G)
# substitute D'' from the Raychaudhuri equation
Dpp = sp.solve(ray, sp.diff(detA, lam, 2))[0]
GppG_sub = sp.simplify(GppG.subs(sp.diff(detA, lam, 2), Dpp))
target = -(sigma2 + Rkk) / (n - 2)
chk("G''/G == -(sigma^2 + R_kk)/(n-2) for general n", sp.simplify(GppG_sub - target) == 0)
chk("n = 4: G''/G == -(1/2)[sigma^2 + R_kk]  (eq. 13 as printed)",
    sp.simplify(GppG_sub.subs(n, 4) + sp.Rational(1, 2) * (sigma2 + Rkk)) == 0)
# discrepancy check: with G = sqrt(det A) in n != 4 the coefficient is not 1/(n-2)
Gs = sp.sqrt(detA)
GsppGs = sp.simplify((sp.diff(Gs, lam, 2) / Gs).subs(sp.diff(detA, lam, 2), Dpp))
chk("with G = sqrt(det A) (eq. 12) the n = 5 coefficient is NOT 1/2 nor 1/3 alone "
    "(a theta^2 term survives): recorded as a discrepancy, sign unaffected",
    sp.simplify(GsppGs.subs(n, 5) - target.subs(n, 5)) != 0)
print("     n=5, G=sqrt(det A):  G''/G =", sp.simplify(GsppGs.subs(n, 5)))

# ---------------------------------------------------------------- (B)
print("(B) Lemma 1 core: NEC => G'' <= 0, so G cannot have an interior positive "
      "minimum between two zeros; the first zero moves continuously")
try:
    import z3
    # finite shadow: a concave sequence g_0..g_N with g_0 = 0, g_1 > 0 cannot
    # return to 0 and then rise again (no second positive hump) -- N = 12.
    N = 12
    g = [z3.Real("g%d" % i) for i in range(N + 1)]
    s = z3.Solver()
    s.add(g[0] == 0, g[1] > 0)
    for i in range(1, N):
        s.add(g[i + 1] - 2 * g[i] + g[i - 1] <= 0)      # G'' <= 0
    # look for a zero followed by a positive value
    s.add(z3.Or(*[z3.And(g[i] <= 0, g[j] > 0) for i in range(2, N) for j in range(i + 1, N + 1)]))
    r = s.check()
    chk("z3: concave G with G(0)=0, G(h)>0 never rises again after a zero (UNSAT)",
        r == z3.unsat)
    # vacuity guard: without concavity the pattern IS satisfiable
    s2 = z3.Solver(); s2.add(g[0] == 0, g[1] > 0)
    s2.add(z3.Or(*[z3.And(g[i] <= 0, g[j] > 0) for i in range(2, N) for j in range(i + 1, N + 1)]))
    chk("vacuity guard: dropping G'' <= 0 makes it SAT", s2.check() == z3.sat)
except ImportError:
    chk("z3 not importable -- (B) not run", False)

# ---------------------------------------------------------------- (C)
print("(C) sign-blindness of traceless (Weyl) focusing on a 2-screen is an identity")
a, b = sp.symbols("a b", real=True)
T = sp.Matrix([[a, b], [b, -a]])
R = sp.Matrix([[0, -1], [1, 0]])
chk("-T == R T R^T for every traceless symmetric 2x2 T", sp.simplify(R * T * R.T + T) == sp.zeros(2))

def det_A_first_zero(Tfun, lam_max=40.0, h=1e-3):
    """Integrate A'' = -T A, A(0)=0, A'(0)=I (Stormer-Verlet as composite.py)
    and return the first lambda with det A <= 0 after the start, or None."""
    A = [[0.0, 0.0], [0.0, 0.0]]; dA = [[1.0, 0.0], [0.0, 1.0]]
    nstep = int(lam_max / h)
    for i in range(nstep):
        T = Tfun(i * h)
        acc = [[-sum(T[r][s] * A[s][c] for s in range(2)) for c in range(2)] for r in range(2)]
        for r in range(2):
            for c in range(2):
                A[r][c] += h * dA[r][c] + 0.5 * h * h * acc[r][c]
                dA[r][c] += h * acc[r][c]
        if i > 5 and A[0][0] * A[1][1] - A[0][1] * A[1][0] <= 0.0:
            return i * h
    return None

# a Weyl-like profile: strength t(l) = 3 m b^2/(b^2 + (l-l0)^2)^{5/2}-shaped,
# with a ROTATING eigenframe (angle phi(l)) so the check is not diagonal-only.
# thin-lens bookkeeping: integral of t is 4m/b^2, focal length f = b^2/4m; with
# the source at lambda_0 = 10 an image forms only if f < 10, so m = 0.05 (f = 5,
# image at lambda_0 + 1/(1/f - 1/lambda_0) = 20).  m = 0.02 (f = 12.5) gave NO
# seat on the first run -- composite.py's own 'source inside the focal length'
# case, kept here as a vacuity guard.
m, bb, l0 = 0.05, 1.0, 10.0
def t_of(l): return 3.0 * m * bb**2 / (bb**2 + (l - l0)**2) ** 2.5
def phi_of(l): return 0.3 * math.sin(0.2 * l)
def Tweyl(l, sign=+1.0):
    t, p = sign * t_of(l), phi_of(l)
    c, s_ = math.cos(2 * p), math.sin(2 * p)
    return [[t * c, t * s_], [t * s_, -t * c]]
zp = det_A_first_zero(lambda l: Tweyl(l, +1.0))
zm = det_A_first_zero(lambda l: Tweyl(l, -1.0))
print("     first det A = 0:  +T at", zp, "   -T at", zm)
chk("both signs seat", zp is not None and zm is not None)
print("     thin-lens prediction: f = b^2/4m =", bb**2/(4*m), " image at", l0 + 1/(1/(bb**2/(4*m)) - 1/l0))
zweak = det_A_first_zero(lambda l: [[3.0*0.02/(1+(l-l0)**2)**2.5, 0.0],[0.0, -3.0*0.02/(1+(l-l0)**2)**2.5]])
chk("vacuity guard: m = 0.02 (f = 12.5 > lambda_0 = 10) does NOT seat", zweak is None)
chk("and at the SAME lambda to the step size (identity, not approximation)",
    zp is not None and zm is not None and abs(zp - zm) <= 2e-3)

# ---------------------------------------------------------------- (D)
print("(D) pure-trace (Ricci) focusing is NOT sign-blind")
r0 = 0.05
# Isotropic focusing gives A = a(lambda) I and det A = a^2: a DOUBLE zero that a
# 'det A <= 0' detector (composite.py:262) cannot see -- it touches zero without
# changing sign.  That detector limit is recorded here (it cannot bite in vacuum,
# where T is traceless and the zero is simple); the scalar equation is used.
def scalar_first_zero(r, lam_max=40.0, h=1e-3):
    a, da = 0.0, 1.0
    for i in range(int(lam_max / h)):
        acc = -r * a
        a += h * da + 0.5 * h * h * acc; da += h * acc
        if i > 5 and a <= 0.0:
            return i * h
    return None
zdet = det_A_first_zero(lambda l: [[r0, 0.0], [0.0, r0]], lam_max=40.0)
print("     det A <= 0 detector on isotropic focusing returns", zdet, "(double zero: detector limit, recorded)")
zR_plus = scalar_first_zero(r0)
zR_minus = scalar_first_zero(-r0)
print("     R_kk = 2r > 0: conjugate at", zR_plus, " (pi/sqrt r =", math.pi / math.sqrt(r0), ")")
print("     R_kk = 2r < 0: conjugate at", zR_minus)
chk("+Ricci seats at pi/sqrt(r) to 0.1 %", zR_plus is not None and abs(zR_plus / (math.pi / math.sqrt(r0)) - 1) < 1e-3)
chk("-Ricci never seats (NEC violated => no focusing from this term)", zR_minus is None)

# ---------------------------------------------------------------- (E)
print("(E) R_kk linear, shear quadratic, in a source that scales T linearly")
M = sp.symbols("M", real=True)
t11, t12, t22 = sp.symbols("t11 t12 t22", real=True)
T1 = sp.Matrix([[t11, t12], [t12, t22]])
TM = M * T1
trace = sp.simplify(TM.trace())
shear_part = TM - sp.Rational(1, 2) * trace * sp.eye(2)
shear2 = sp.simplify((shear_part * shear_part).trace())
chk("tr T (the R_kk analogue) is degree 1 in M", sp.Poly(trace, M).degree() == 1)
chk("sigma^2 (traceless part squared) is degree 2 in M", sp.Poly(shear2, M).degree() == 2)

print("\nRESULT:", "ALL CHECKS PASS" if ok else "A CHECK FAILED")
sys.exit(0 if ok else 1)
