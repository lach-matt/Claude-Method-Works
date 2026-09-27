#!/usr/bin/env python3
"""DOCKET 67 re-derivation for 0802.0658-sec3.2 (Hu & Verdaguer, Living Rev. 2008, Sec. 3.2).

Published (p.10, after Eq. 3.12, READ): "for a linear quantum field the above kernel ... is
free of ultraviolet divergences because the regularized T_ab differs from the renormalized
T^R_ab by the identity operator times some tensor counterterms, see Eq. (3.6), so that in the
subtraction (3.12) the counterterms cancel."  Sec. 5.2.1 (p.29-30): finite for y != x; "When the
coincidence limit is taken divergences do occur"; alternative route via Wick, Eqs. (5.19)-(5.22).

Checks (each labelled by what it is):
 A  THEOREM (finite algebra, sympy, exact): a c-number shift A -> A + c*1 leaves every central
    moment and every covariance <{t_A,t_B}>/2 unchanged, in ANY state (no Wick, no Gaussianity).
    This is the whole of the Sec. 3.2 argument; the counterterm may be regulator-divergent (symbol L).
 B  THEOREM (symbolic Wick, sympy, exact): H&V Eqs. (5.19)->(5.21)->(5.22) for a quasi-free state
    with ORDERED Wightman functions G(a,b) != G(b,a).
 B' NUMERIC: Wick's 4-point formula holds in a Fock vacuum (quasi-free) and FAILS in a one-particle
    Fock state -- so the Sec. 5.2.1 route needs a quasi-free state; route A does not.
 C  ILLUSTRATION (flat, massless, 4D): the pointwise kernel ~ G^2 diverges at coincidence (5.2.1).
 D  ILLUSTRATION (flat, massless, 4D, worldline, energy density; Ford & Roman gr-qc/0506026 Eq.53):
    the Lorentzian-time-smeared variance with the Wightman i*eps is finite, positive and eps-stable,
    -> 3/(2 pi^4 a^8) (FR Eq. 49).  THIS IS NOT the curved worldline result (Fewster 1208.5399 Sec 3.3),
    which stays NAMED, NOT RUN in the tree and is not run here either.
Exit 0 iff every check passes.
"""
import sys, itertools
import numpy as np
import sympy as sp
import mpmath as mp

ok = True
def chk(name, cond):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

# ---------------- A: c-number counterterm cancels (any state, any dimension) ----------------
n = 3
def herm(prefix):
    M = sp.zeros(n, n)
    for i in range(n):
        M[i, i] = sp.Symbol(f"{prefix}{i}{i}", real=True)
        for j in range(i + 1, n):
            re, im = sp.symbols(f"{prefix}r{i}{j} {prefix}i{i}{j}", real=True)
            M[i, j] = re + sp.I * im
            M[j, i] = re - sp.I * im
    return M
A, B, R = herm("a"), herm("b"), herm("r")          # R: a generic Hermitian 'state' (trace left free)
L1, L2 = sp.symbols("L1 L2", real=True)            # counterterms, may diverge with the regulator
I = sp.eye(n)
Z = R.trace()
ev = lambda X: (R * X).trace() / Z
def cov(X, Y):
    tX, tY = X - ev(X) * I, Y - ev(Y) * I
    return sp.Rational(1, 2) * ev(tX * tY + tY * tX)
d_cov = sp.simplify(sp.expand(cov(A + L1 * I, B + L2 * I) - cov(A, B)))
chk("A1 covariance <{t_A,t_B}>/2 invariant under A->A+L1*1, B->B+L2*1 (symbolic 3x3, generic state)", d_cov == 0)
tA = A - ev(A) * I
tAs = (A + L1 * I) - ev(A + L1 * I) * I
chk("A2 fluctuation operator t_A = A - <A> is itself shift-invariant (so ALL central moments are)",
    sp.simplify(sp.expand(tAs - tA)) == sp.zeros(n, n))
d_mean = sp.simplify(ev(A + L1 * I) - ev(A) - L1)
chk("A3 ... while the mean moves by exactly the counterterm", d_mean == 0)

# ---------------- B: H&V (5.19)->(5.21)->(5.22), quasi-free Wick with ordered G ----------------
labels = ["x", "xp", "y", "yp"]
Gs = {(a, b): sp.Symbol(f"G_{a}_{b}") for a in labels for b in labels if a != b}
G = lambda a, b: Gs[(a, b)]
def w4(a, b, c, d):   # quasi-free 4-point Wightman function, order preserved within each pair
    return G(a, b) * G(c, d) + G(a, c) * G(b, d) + G(a, d) * G(b, c)
def acomm(p, q):      # {p,q} as list of ordered words
    return [p + q, q + p]
X = acomm(("x",), ("xp",)); Y = acomm(("y",), ("yp",))
four = sum(w4(*(u + v)) for u in X for v in Y) + sum(w4(*(v + u)) for u in X for v in Y)
two = lambda words: sum(G(*w) for w in words)
Gfun = sp.Rational(1, 4) * (four - 2 * two(X) * two(Y))
hv521 = G("x", "yp") * G("xp", "y") + G("x", "y") * G("xp", "yp") + G("y", "xp") * G("yp", "x") + G("y", "x") * G("yp", "xp")
chk("B1 H&V (5.21): disconnected (divergent) pairings cancel, leaving the 4 connected terms",
    sp.expand(Gfun - hv521) == 0)
coinc = {G("xp", "y"): G("x", "y"), G("x", "yp"): G("x", "y"), G("xp", "yp"): G("x", "y"),
         G("y", "xp"): G("y", "x"), G("yp", "x"): G("y", "x"), G("yp", "xp"): G("y", "x")}
chk("B2 H&V (5.22): G(x,x,y,y) = 2(G_xy^2 + G_yx^2)",
    sp.expand(hv521.subs(coinc) - 2 * (G("x", "y") ** 2 + G("y", "x") ** 2)) == 0)
# the pair G_xx' never survives: that is the only object that diverges as x'->x
chk("B3 no surviving term contains G(x,x') or G(y,y') (the coincident-pair singularities)",
    not any(s in hv521.free_symbols for s in (G("x", "xp"), G("xp", "x"), G("y", "yp"), G("yp", "y"))))

# ---------------- B': Wick holds in a Fock vacuum, fails in a 1-particle state ----------------
rng = np.random.default_rng(67)
nmax, K = 6, 2
a1 = np.diag(np.sqrt(np.arange(1, nmax)), 1)
ops = [np.kron(a1, np.eye(nmax)), np.kron(np.eye(nmax), a1)]
coef = rng.normal(size=(4, K)) + 1j * rng.normal(size=(4, K))
phis = [sum(coef[i, k] * ops[k] + np.conj(coef[i, k]) * ops[k].conj().T for k in range(K)) for i in range(4)]
vac = np.zeros(nmax * nmax, complex); vac[0] = 1
one = np.zeros(nmax * nmax, complex); one[1 * nmax + 0] = 1  # |1,0>
def e(state, *M):
    v = state.copy()
    for m in reversed(M):
        v = m @ v
    return np.vdot(state, v)
def wick_err(state):
    g = lambda i, j: e(state, phis[i], phis[j])
    lhs = e(state, *phis)
    rhs = g(0, 1) * g(2, 3) + g(0, 2) * g(1, 3) + g(0, 3) * g(1, 2)
    return abs(lhs - rhs) / abs(lhs)
ev_, e1_ = wick_err(vac), wick_err(one)
print(f"     Wick relative error: vacuum {ev_:.2e}, one-particle {e1_:.2e}")
chk("B'1 Wick 4-point formula exact in the Fock vacuum (quasi-free)", ev_ < 1e-12)
chk("B'2 ... and violated in a 1-particle state (Sec. 5.2.1's route needs quasi-free; route A does not)", e1_ > 1e-3)

# ---------------- C: pointwise coincidence divergence (flat, massless, 4D) ----------------
r, t = sp.symbols("r t", positive=True)
Gp = 1 / (4 * sp.pi**2 * (r**2 - t**2))            # massless Wightman fn, spacelike region, eps->0
chk("C1 G(x,y)^2 -> infinity as y->x (the pointwise noise kernel diverges at coincidence, 5.2.1)",
    sp.limit((Gp**2).subs(t, 0), r, 0) == sp.oo)

# ---------------- D: worldline Lorentzian smearing of <rho rho> finite, eps-stable ----------------
mp.mp.dps = 40
a = mp.mpf(1)
def smeared(eps):
    gL = lambda tau: a / (mp.pi * (tau**2 + a**2))
    f = lambda tau: gL(tau) * mp.re(3 / (2 * mp.pi**4 * (tau - 1j * eps) ** 8))
    pts = [-mp.inf, -50, -5, -1, -10 * eps, -eps, 0, eps, 10 * eps, 1, 5, 50, mp.inf]
    return mp.quad(f, pts, maxdegree=10)
target = 3 / (2 * mp.pi**4 * a**8)
vals = []
for eps in (mp.mpf("0.3"), mp.mpf("0.1"), mp.mpf("0.03")):
    v = smeared(eps)
    exact_eps = 3 / (2 * mp.pi**4 * (a + eps) ** 8)    # residue at tau=-ia: (-ia-i eps)^8=(a+eps)^8
    vals.append(v)
    print(f"     eps={float(eps):.2f}: quad={mp.nstr(v,12)}  closed-form(a+eps)={mp.nstr(exact_eps,12)}")
    chk(f"D1 smeared variance matches contour closed form at eps={float(eps)}", abs(v - exact_eps) / exact_eps < 1e-8)
chk("D2 smeared variance positive and -> 3/(2 pi^4 a^8) as eps->0 (Ford-Roman Eq. 49), no renormalisation",
    all(v > 0 for v in vals) and abs(3 / (2 * mp.pi**4 * (a + mp.mpf('1e-9')) ** 8) - target) / target < 1e-7)
print(f"     limit 3/(2 pi^4) = {mp.nstr(target, 12)}  (a = 1)")
print("RESULT:", "ALL PASS" if ok else "FAILURES")
sys.exit(0 if ok else 1)
