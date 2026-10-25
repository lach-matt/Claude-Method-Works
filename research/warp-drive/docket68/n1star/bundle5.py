#!/usr/bin/env python3
"""bundle5.py -- the calculus facts behind [Hin26c] section 9 re-run on bundles (N1STAR-PROOF.md section 10.86; D183).

10.86 re-runs each proof of [Hin26c] section 9 the record uses on E_X, the bundle of 1-forms or symmetric 2-tensors,
in a fibre inner product h. Its frame (F1)-(F8) rests on facts of the calculus with matrix coefficients; these checks
compute them exactly, on differential operators on R with 2 x 2 matrix coefficients (arbitrary functions of x) and
on symbolic 2 x 2 matrices.  Operators are dicts {order: coefficient matrix}, composed by the Leibniz rule.

  E1 (computed, exact) A scalar commutant keeps the commutator's principal part scalar: for P = -d^2 + M d + V and
     A = f d, [P, A] = -2 f' d^2 + (f' M - f M' - f'') d - f V', its top coefficient -2 f' Id, M and V entering one
     order lower ((F3)).  Control: A = F d with F a matrix, whose top coefficient -2 F' + [M, F] is not scalar.
  E2 (computed, exact) Im P is first order and h-self-adjoint: with h(x) a positive definite Hermitian matrix and P*
     the h-adjoint h^-1 P^dagger h, (P - P*)/2i = S_1 d + S_0 has no second-order term and h times its principal
     symbol i xi S_1 is Hermitian ((F3)).  Control: the symbol tested for Hermitian without h.
  E3 (computed, exact) Square roots: for M = [[a, c + i d], [c - i d, b]] positive definite, with delta = (det M)^(1/2)
     and tau = (tr M + 2 delta)^(1/2), S = (M + delta Id)/tau is Hermitian with S^2 = M, det S = delta and tr S = tau,
     so positive definite: an algebraic, real-analytic function of the entries ((F4)).  Control: M / (tr M)^(1/2).
  E4 (computed, exact) The trace bound of (F5): lambda_max Id - p has eigenvalues 0 and the discriminant root; for
     2 x 2 positive semidefinite A, B, tr(AB) - ((a a')^(1/2) - (b b')^(1/2))^2 = 2 Re(c conj(c')) + 2 (a b a' b')^(1/2)
     >= 0; and 200 exact samples of tr(p m) <= lambda_max(p) for density matrices m.  Control: lambda_min in place
     of lambda_max.
  E5 (computed, exact) The energy identity with a connection ((F6)): on R^(1+1), -dt^2 + dx^2, u in R^2, nabla = d + A
     with A_t, A_x antisymmetric, the current J of T[u](., d_t) has div J = <box_nabla u, nabla_t u> + <nabla_x u,
     F_xt u>, F_xt = d_x A_t - d_t A_x + [A_x, A_t]: no second derivative of u is left, the curvature term zeroth order
     in u.  Control: the curvature term dropped.
  E6 (computed, exact) Sums of squares in an inner product ((F7)): for V = d on C^2 and h(x), V*^h V = -d^2 - h^-1 h' d:
     the h-adjoint form differs from -d^2 by a first-order term.  Control: -2 d^2 in place of -d^2.

python3 bundle5.py --selftest | --mutants
"""
import random
import sys

import sympy as sp

from damping5 import Checklist

x, t = sp.symbols("x t", real=True)
I2 = sp.eye(2)


def fn(name):
    return sp.Function(name, real=True)(x)


def mat(prefix, herm=False, cplx=True):
    if herm:
        a, b, c, d = (fn(prefix + s) for s in ("11", "22", "12r", "12i"))
        return sp.Matrix([[a, c + sp.I * d], [c - sp.I * d, b]])
    return sp.Matrix(2, 2, lambda i, j: fn(f"{prefix}{i}{j}r") + (sp.I * fn(f"{prefix}{i}{j}i") if cplx else 0))


def compose(A, B):
    out = {}
    for k, Ak in A.items():
        for l, Bl in B.items():
            for j in range(k + 1):
                c = sp.binomial(k, j) * Ak * sp.diff(Bl, x, j)
                out[k - j + l] = out.get(k - j + l, sp.zeros(2, 2)) + c
    return {k: v.applyfunc(sp.expand) for k, v in out.items()}


def add(A, B, s=1):
    out = dict(A)
    for k, v in B.items():
        out[k] = out.get(k, sp.zeros(2, 2)) + s * v
    return {k: v.applyfunc(sp.expand) for k, v in out.items()}


def realify(e):
    """conj(f'(x)) = f'(x) for the real functions here (sympy does not know a derivative of a real function is real)."""
    return e.replace(lambda q: isinstance(q, sp.conjugate) and isinstance(q.args[0], sp.Derivative), lambda q: q.args[0])


def zero(Mx):
    return all(sp.simplify(e) == 0 for e in Mx)


def scalar(Mx):
    return zero(Mx - Mx[0, 0] * I2)


def e1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    M, V, f = mat("m"), mat("v"), fn("f")
    P = {2: -I2, 1: M, 0: V}
    A = {1: (mat("F") if control else f * I2)}
    C = add(compose(P, A), compose(A, P), -1)
    chk("[P, A] is of order 2 (no third-order term)", zero(C.get(3, sp.zeros(2, 2))))
    chk("its top coefficient is scalar, -2 f' Id", scalar(C[2]) and (control or zero(C[2] + 2 * sp.diff(f, x) * I2)))
    if not control:
        chk("M and V enter one order lower: f' M - f M' - f'' and -f V'",
            zero(C[1] - (sp.diff(f, x) * M - f * sp.diff(M, x) - sp.diff(f, x, 2) * I2))
            and zero(C[0] + f * sp.diff(V, x)))
    return chk.ok


def adjoint_h(P, h):
    """h-adjoint for the density dx: P* = h^-1 P^dagger h, P^dagger = sum (-d)^k A_k^H."""
    hinv = h.inv()
    Pd = {}
    for k, Ak in P.items():
        dk = {k: (-1)**k * I2}
        Pd = add(Pd, compose(dk, {0: Ak.H}))
    return compose({0: hinv}, compose(Pd, {0: h}))


def e2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    M, V = mat("m"), mat("v")
    h = mat("h", herm=True)
    P = {2: -I2, 1: M, 0: V}
    Ps = adjoint_h(P, h)
    ImP = {k: (v / (2 * sp.I)).applyfunc(sp.expand) for k, v in add(P, Ps, -1).items()}
    chk("(P - P*)/2i has no second-order term", zero(ImP.get(2, sp.zeros(2, 2))))
    sym = sp.I * ImP[1]                                       # the principal symbol: d has symbol i xi
    test = (sym if control else h * sym).applyfunc(sp.simplify)
    chk("h times its principal symbol i S_1 is Hermitian: an h-self-adjoint principal symbol",
        zero((test - test.H).applyfunc(realify)))
    return chk.ok


def e3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    a, b = sp.symbols("a b", positive=True)
    c, d = sp.symbols("c d", real=True)
    M = sp.Matrix([[a, c + sp.I * d], [c - sp.I * d, b]])
    delta = sp.Symbol("delta", positive=True)                 # delta^2 = a b - c^2 - d^2 > 0
    tau = sp.sqrt(a + b + 2 * delta)
    S = (M / sp.sqrt(a + b)) if control else (M + delta * I2) / tau
    sq = (S * S - M).applyfunc(lambda e: sp.simplify(sp.expand(e).subs(c**2, a * b - d**2 - delta**2)))
    chk("S = (M + delta Id)/tau: S^2 = M (with delta^2 = det M)", zero(sq))
    if not control:
        chk("S Hermitian, det S = delta > 0, tr S = tau > 0", zero(S - S.H)
            and sp.simplify(sp.expand(S.det()).subs(c**2, a * b - d**2 - delta**2) - delta) == 0
            and sp.simplify(S.trace() - tau) == 0)
    return chk.ok


def e4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    p11, p22, c, d = sp.symbols("p11 p22 c d", real=True)
    p = sp.Matrix([[p11, c + sp.I * d], [c - sp.I * d, p22]])
    disc = sp.sqrt((p11 - p22)**2 + 4 * (c**2 + d**2))
    lmax, lmin = (p11 + p22 + disc) / 2, (p11 + p22 - disc) / 2
    Q = lmax * I2 - p
    chk("lambda_max Id - p has eigenvalues 0 and the discriminant root (determinant 0, trace the root)",
        sp.simplify(sp.expand(Q.det())) == 0 and sp.simplify(Q.trace() - disc) == 0)
    a, b, a2, b2 = sp.symbols("a b a2 b2", nonnegative=True)
    c1, d1, c2, d2 = sp.symbols("c1 d1 c2 d2", real=True)
    A = sp.Matrix([[a, c1 + sp.I * d1], [c1 - sp.I * d1, b]])
    B = sp.Matrix([[a2, c2 + sp.I * d2], [c2 - sp.I * d2, b2]])
    lhs = sp.expand((A * B).trace() - (sp.sqrt(a * a2) - sp.sqrt(b * b2))**2)
    chk("tr(AB) - (sqrt(a a') - sqrt(b b'))^2 = 2 Re(c conj c') + 2 sqrt(a b a' b')",
        sp.simplify(lhs - (2 * (c1 * c2 + d1 * d2) + 2 * sp.sqrt(a * a2) * sp.sqrt(b * b2))) == 0)
    rnd = random.Random(20261025)
    ok = True
    for _ in range(200):
        q = [sp.Rational(rnd.randint(-9, 9), rnd.randint(1, 5)) for _ in range(4)]
        P_ = sp.Matrix([[q[0], q[2] + sp.I * q[3]], [q[2] - sp.I * q[3], q[1]]])
        v = sp.Matrix([sp.Rational(rnd.randint(-5, 5), 3) + sp.I * rnd.randint(-5, 5), rnd.randint(1, 6)])
        w = sp.Matrix([rnd.randint(-4, 4), sp.Rational(rnd.randint(1, 7), 2) + sp.I * rnd.randint(-3, 3)])
        s = sp.Rational(rnd.randint(0, 10), 10)
        m = s * v * v.H / (v.H * v)[0] + (1 - s) * w * w.H / (w.H * w)[0]
        dsc = sp.sqrt((q[0] - q[1])**2 + 4 * (q[2]**2 + q[3]**2))
        bound = (q[0] + q[1] - dsc) / 2 if control else (q[0] + q[1] + dsc) / 2
        val = sp.re(sp.expand((P_ * m).trace()))
        ok &= bool(sp.N(bound - val, 50) >= -sp.Rational(1, 10**40))
    chk("tr(p m) <= lambda_max(p) on 200 exact samples of density matrices m", ok)
    return chk.ok


def e5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    u = sp.Matrix([sp.Function("u1")(t, x), sp.Function("u2")(t, x)])
    al, be = sp.Function("alpha")(t, x), sp.Function("beta")(t, x)
    At = sp.Matrix([[0, al], [-al, 0]])
    Ax = sp.Matrix([[0, be], [-be, 0]])

    def Dt(w):
        return w.diff(t) + At * w

    def Dx(w):
        return w.diff(x) + Ax * w

    box = -Dt(Dt(u)) + Dx(Dx(u))                                   # g = -dt^2 + dx^2
    Ttt = ((Dt(u).T * Dt(u))[0] + (Dx(u).T * Dx(u))[0]) / 2
    Txt = (Dx(u).T * Dt(u))[0]
    divJ = -sp.diff(Ttt, t) + sp.diff(Txt, x)                       # J^t = -T_tt, J^x = T_xt
    F = At.diff(x) - Ax.diff(t) + Ax * At - At * Ax
    rhs = (box.T * Dt(u))[0] + (0 if control else (Dx(u).T * F * u)[0])
    chk("div J = <box_nabla u, nabla_t u> + <nabla_x u, F_xt u>, F_xt = d_x A_t - d_t A_x + [A_x, A_t]",
        sp.simplify(sp.expand(divJ - rhs)) == 0)
    return chk.ok


def e6(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    h = mat("h", herm=True)
    Vd = {1: I2}
    Vs = adjoint_h(Vd, h)
    W = compose(Vs, Vd)
    D = add(W, {2: (-2 if control else -1) * I2}, -1)
    chk("V*^h V - (-d^2) has no second-order term", zero(D.get(2, sp.zeros(2, 2))))
    if not control:
        chk("and its first-order coefficient is -h^-1 h'", zero((D[1] + h.inv() * sp.diff(h, x)).applyfunc(sp.simplify)))
    return chk.ok


CHECKS = [("E1 a scalar commutant keeps [P, A]'s top coefficient scalar; M and V one order lower", e1),
          ("E2 Im P has no second-order term; h times its first-order coefficient is Hermitian", e2),
          ("E3 the positive square root (M + delta Id)/tau of a 2 x 2 positive definite matrix", e3),
          ("E4 the trace bound tr(p m) <= lambda_max(p) for density matrices m", e4),
          ("E5 the energy identity with a connection: div J = <box u, nabla_t u> + <nabla_x u, F_xt u>", e5),
          ("E6 the h-adjoint sum of squares V*^h V = -d^2 - h^-1 h' d", e6)]


def run(verbose=False):
    ok = True
    for name, fn_ in CHECKS:
        res = fn_(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'}", flush=True)
    print(f"bundle5.py: {len(CHECKS) if ok else 'not all'}/{len(CHECKS)}")
    return ok


def mutants():
    caught = 0
    for name, fn_ in CHECKS:
        res = fn_(1, False)
        caught += not res
        print(f"mutant 1 of {name[:2]}: {'caught' if not res else 'MISSED'}")
    print(f"bundle5.py mutants: {caught}/{len(CHECKS)}")
    return caught == len(CHECKS)


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--mutants" in a:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if run("-v" in a) else 1)
