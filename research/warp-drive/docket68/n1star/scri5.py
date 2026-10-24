#!/usr/bin/env python3
"""scri5.py -- [Hin26] Proposition 5.11's (5.27)-(5.28) and Proposition 5.14 in five dimensions: the structure of the
linearized gauge-fixed Einstein operator at future null infinity, its exponents there by harmonic type, and the
radiative order at future timelike infinity (N1STAR-PROOF.md section 10.38; ROUTES-OPEN.md 4.39; D100).  Labels:
computed (exact, sympy; numerical, mpmath, where said), deduced, READ.

[Hin26] (arXiv:2606.28253v2) Proposition 5.11: L_(g,g0) == (2 r^-1 d_0 r + r^-1 A_h) d_1 + r^-1 B_h ((5.26a)), "where,
in the bundle splitting S^2 T* = <(dx^0)^2> + (2 dx^0 (x)_s r T*S^2) + <r^2 g-slash> + <2 dx^0 dx^1> + (2 dx^1 (x)_s r
T*S^2) + r^2 ker tr-slash + <(dx^1)^2>, (5.27) the operator A_h is lower triangular and B_h is strictly lower
triangular" (p. 93), with (5.28) printing A_h: its constant part and its entries in d_1(r h), d_1^2(r h) of the
perturbation h; "various components of g-dot decay like O(rho_I^(1+z)) where z is an eigenvalue of A_h" (p. 97); and
Proposition 5.14's proof: "The (7, 4) and (7, 6) entries of I + A_h couple pi_01 g-dot and pi-slash_0 g-dot into the
11-component of the output ... hence the definition of F_I,11 in (5.43)" (p. 98), F_I,11 = 1 + (E^C_I u (1, 0) u (1 +
(1 - e_Ups) gam_Ups, 0)).  Here x^0 = t + r, x^1 = t - r (damping5.py), d_1 = d_t* at null infinity, and A_0 := A_h at h
= 0 is sbar5.py's S-bar (2 rho S-bar the d_t* coefficient of 2 L - box; his Lemma 8.2), written in his splitting.

  C1 (computed, exact) The five-dimensional (5.28) at h = 0.  In the splitting (5.27) with S^3 -- frame components
     g(d_0, d_0), the tangential part of g(d_0, .), the trace of the tangential block over 3, g(d_0, d_1), the
     tangential part of g(d_1, .), the trace-free tangential block, g(d_1, d_1), with d_0 = (d_t + d_r)/2, d_1 = (d_t -
     d_r)/2 -- A_0 is lower triangular, the same at (R, 0, 0, 0) and at (1, 2, 2, 4), with the diagonal of his (5.28)
     and (7, 4) entry 2 (1 - e_Ups) gam_Ups as in four dimensions, (2, 5) and (5, 2) as there, and three trace
     couplings changed: (3, 1) = (4/3)(1 - e_C)(1 + v) gam_C, (4, 1) = (1 + 2 e_C)(1 + v) gam_C/3 + gam_Ups, (4, 3) =
     ((1 + 2 e_C)(1 - v) gam_C + 3 e_Ups gam_Ups)/4, (7, 3) = (3/2)((1 + v) gam_C + e_Ups gam_Ups).  Four-dimensional
     control: at n = 3 and the trace weight 1, his (5.28) with h = 0, all 49 entries.  Control: the five-dimensional
     matrix claimed equal to the four-dimensional one.
  C2 (computed, exact) The exponents at null infinity by type.  iota5.py's L1(x) for L-bar (lin5.py's bases) has det
     L1(x) = c prod (3/2 + (A_0)_ii - x) over the slots the type occupies: s0 the four scalar ones (1, 3, 4, 7), v1 the
     two vector ones (2, 5), v2 those and the trace-free one (6), t2 that one alone -- so the radiative exponents 3/2 +
     {0, (1 - e_Ups) gam_Ups, gam_Ups, 2 gam_Ups} and the constraint ones 3/2 + O(gam_C) sit where his splitting puts
     them, every parameter symbolic.  Control: s0 claimed to carry slot 5 for slot 4.
  C3 (computed, numerical) No resonant state at a radiative exponent.  At s0, L-bar, gam_C = 10 (50 digits, 260 terms)
     and 100 (100 digits, 700 terms) with the record's other parameters, at lam equal to pi_01's exponent 3/2 + (1 -
     e_Ups) gam_Ups and to pi_11's 3/2 + 2 gam_Ups -- the pair the (7, 4) entry couples -- the connection of iota5.py
     with that exponent's own column, its leading coefficient in ker L1(lam) (his (9.17)), is nonzero: above 3/10 of its
     largest value on iota5.py I5's grid, and equal to its values at lam +- 10^-15 to 10^-9 of them (the computation's
     noise is 10^-15 at gam_C = 10 and 10^-11 at 100), so continuous there; at t2, lam = 3/2, likewise.  Controls: the
     zero claimed; the leading coefficient taken off ker L1(lam), where the value is not the limit.

Deduced from these (N1STAR-PROOF.md 10.38): his footnote 27's coupling, the (7, 6) entry, is the perturbation's alone
(his p. 169) and falls half an order in five dimensions, so the iteration's quadratic sources reach the 11-component at
the Coulombic order 2, the mass aspect's, and not at the radiative 3/2; the (7, 4) entry carries pi_01's radiative
exponent into pi_11 as in four dimensions; a radiative-order term at null infinity reaches timelike infinity at its own
order only through a resonant state there at that exponent, which 10.37(b)-(d) exclude below 2 on their readings.

sympy, mpmath.  python3 scri5.py [--selftest | --mutants | --only k]   (about twelve and ten minutes)
"""
import sys
import time

import mpmath as mp
import sympy as sp

import iota5 as I5
import lin5 as L5
import sbar5 as SB
from damping5 import Checklist
from sbar5 import v, eC, gC, eU, gU

HALF = sp.Rational(1, 2)
SLOTS = ["(dx0)^2", "dx0 rT*S", "r^2 g-slash", "dx0 dx1", "dx1 rT*S", "r^2 ker tr", "(dx1)^2"]


# ------------------------------------------------------------------------------------------------- C1 (5.28) at h = 0
def his528():
    """[Hin26] (5.28) at h = 0, his order of the splitting (5.27) (p. 93)"""
    A = sp.zeros(7, 7)
    A[0, 0] = 2 * (1 - v) * gC
    A[1, 1] = (1 - v) * gC
    A[2, 0], A[2, 2] = 2 * (1 - eC) * (1 + v) * gC, (1 - eC) * (1 - v) * gC
    A[3, 0], A[3, 2], A[3, 3] = eC * (1 + v) * gC + gU, HALF * (eC * (1 - v) * gC + eU * gU), (1 - eU) * gU
    A[4, 1], A[4, 4] = (1 + v) * gC + gU, gU
    A[6, 2], A[6, 3], A[6, 6] = (1 + v) * gC + eU * gU, 2 * (1 - eU) * gU, 2 * gU
    return A


def five528():
    """the five-dimensional matrix C1 states"""
    A = his528()
    A[2, 0] = sp.Rational(4, 3) * (1 - eC) * (1 + v) * gC
    A[3, 0] = (1 + 2 * eC) * (1 + v) * gC / 3 + gU
    A[3, 2] = ((1 + 2 * eC) * (1 - v) * gC + 3 * eU * gU) / 4
    A[6, 2] = sp.Rational(3, 2) * ((1 + v) * gC + eU * gU)
    return A


def split(n, m, pt):
    """S-bar of L at pt in the splitting (5.27): column j is S-bar applied to the j-th summand's element"""
    M, second = SB.sbar_L(n, m, pt)
    N = n + 1
    keys = [(a, b) for a in range(N) for b in range(a, N)]
    pt = [sp.sympify(q) for q in pt]
    r = sp.sqrt(sum(q**2 for q in pt))
    nh = sp.Matrix([q / r for q in pt])
    P = sp.eye(n) - nh * nh.T
    dt, dr = sp.Matrix([1] + [0] * n), sp.Matrix([0] + list(nh))
    d0, d1 = dt + dr, dt - dr                               # the covectors dx^0, dx^1
    e0, e1 = (dt + dr) / 2, (dt - dr) / 2                   # the vectors d_0, d_1 (dt, dr dual to d_t, d_r here)

    def sym(a, b):
        return a * b.T + b * a.T

    w = P * sp.Matrix([1 if i == 2 else 0 for i in range(n)])      # a tangential 1-form: P dx_3
    wc = sp.Matrix([0] + list(w))
    ex = [sp.Matrix([1 if i == k else 0 for i in range(n)]) for k in (1, 2)]
    tf = P * sym(*ex) * P
    tf = tf - P * tf.trace() / (n - 1)
    T6 = sp.zeros(N, N)
    T6[1:, 1:] = tf
    B = [d0 * d0.T, sym(d0, wc), sp.diag(0, P), sym(d0, d1), sym(d1, wc), T6, d1 * d1.T]

    def apply(S):
        o = M * sp.Matrix([S[a, b] for (a, b) in keys])
        out = sp.zeros(N, N)
        for (a, b), q in zip(keys, o):
            out[a, b] = out[b, a] = q
        return out

    def ratio(vec, ref):
        vec, ref = [sp.simplify(q) for q in vec], [sp.simplify(q) for q in ref]
        if all(q == 0 for q in vec):
            return sp.Integer(0), True
        i = next(k for k, q in enumerate(ref) if q != 0)
        al = sp.simplify(vec[i] / ref[i])
        return al, all(sp.simplify(vec[k] - al * ref[k]) == 0 for k in range(len(ref)))

    A, prop = sp.zeros(7, 7), True
    for j, Bj in enumerate(B):
        S = apply(Bj)
        A[0, j] = (e0.T * S * e0)[0]
        A[3, j] = (e0.T * S * e1)[0]
        A[6, j] = (e1.T * S * e1)[0]
        ang = P * S[1:, 1:] * P
        A[2, j] = ang.trace() / (n - 1)
        for row, vec, ref in ((1, P * (S * e0)[1:, 0], w), (4, P * (S * e1)[1:, 0], w),
                              (5, list(ang - P * ang.trace() / (n - 1)), list(tf))):
            al, ok = ratio(list(vec), list(ref))
            A[row, j] = al
            prop &= ok
    return A.applyfunc(lambda q: sp.factor(sp.simplify(q))), prop and not second


def c1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    R = sp.Symbol("R", positive=True)
    ok = True
    A4, p4 = split(3, 1, [R, 0, 0])
    good = p4 and all(sp.simplify(q) == 0 for q in A4 - his528())
    chk("four dimensions, trace weight 1: his (5.28) at h = 0, all 49 entries, each summand mapped to its own type",
        good)
    ok &= good
    A5, p5 = split(4, sp.Rational(2, 3), [R, 0, 0, 0])
    B5, q5 = split(4, sp.Rational(2, 3), [1, 2, 2, 4])
    want = his528() if control == 1 else five528()
    tri = all(A5[i, j] == 0 for i in range(7) for j in range(i + 1, 7))
    good = p5 and q5 and tri and all(sp.simplify(q) == 0 for q in A5 - want) and \
        all(sp.simplify(q) == 0 for q in A5 - B5)
    diff = [(i + 1, j + 1) for i in range(7) for j in range(7) if sp.simplify(A5[i, j] - his528()[i, j]) != 0]
    chk(f"five dimensions, trace weight 2/3: lower triangular, the same at (R, 0, 0, 0) and (1, 2, 2, 4); differs from "
        f"four dimensions at {diff}: (3, 1) {A5[2, 0]}, (4, 1) {A5[3, 0]}, (4, 3) {A5[3, 2]}, (7, 3) {A5[6, 2]}; "
        f"(7, 4) {A5[6, 3]}", good)
    ok &= good
    return ok


# ------------------------------------------------------------------------------------------------- C2 the exponents
TYPES = {"s0": (0, 2, 3, 6), "v1": (1, 4), "v2": (1, 4, 5), "t2": (5,)}


def c2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    A = five528()
    ok = True
    for typ, slots in TYPES.items():
        if control == 1 and typ == "s0":
            slots = (0, 2, 4, 6)
        M0, M1, _ = I5.mats(4, typ, L5.Lbar)
        K = M0.shape[0]
        sub = {L5.v: v, L5.eC: eC, L5.gC: gC, L5.eU: eU, L5.gU: gU}
        L1 = M0.applyfunc(lambda q: sp.cancel(q / (I5.X - I5.Lam)))       # M0 = (x - lam) L1, L1 free of lam
        free = all(not q.has(I5.Lam) for q in L1)
        dL1 = sp.factor(L1.subs(sub).det(method="berkowitz"))
        prod = sp.prod([sp.Rational(3, 2) + A[i, i] - I5.X for i in slots])
        q = sp.cancel(dL1 / prod)
        good = free and K == len(slots) and q.is_number and q != 0
        chk(f"{typ}: det L1(x) = {q} prod (3/2 + (A_0)_ii - x) over slots {[SLOTS[i] for i in slots]}", good)
        ok &= good
    return ok


# ------------------------------------------------------------------------------------------------- C3 at the exponent
def conn_at(P, Q, lam, mu0, N, off=False):
    """iota5.py's connection at lam = mu0, an outgoing exponent: that column's g0 in ker L1(mu0) (off: a vector off
    it)"""
    K = P[0].rows
    out = I5.out_exps(P, lam)
    roots = sorted(I5.quad_eigs(Q), key=mp.re)
    allow = roots[:K]
    tol = mp.mpf(10)**(-mp.mp.dps // 3)
    assert all(mp.re(q) <= tol for q in allow) and all(mp.re(q) > tol for q in roots[K:])
    z = mp.mpf(1) / 2
    R0s, Rinf = I5.coeffR(P, Q, 1), I5.coeffR(I5.neg(Q), I5.neg(P), mp.mpf(1) / 4)
    P2, P1, _ = P
    cols, hit = [], 0
    for mu in out:
        if abs(mu - mu0) < mp.mpf(10)**-10:
            hit += 1
            L1 = P2 * mu + P1 + lam * P2
            g0 = I5.kernel(L1)
            if off:
                g0 = g0 + mp.matrix([mp.mpf(1) / (j + 2) for j in range(K)])
            gs, val, th, zn = [g0], g0 * 1, g0 * mu, mp.mpf(1)
            for n in range(1, N):
                rhs = sum((I5.ev(R0s[j], mu + n - j) * gs[n - j] for j in range(1, 4) if n - j >= 0), mp.matrix(K, 1))
                g = -mp.lu_solve(I5.ev(R0s[0], mu + n), rhs)
                gs.append(g)
                zn *= z
                val += g * zn
                th += g * (mu + n) * zn
        else:
            val, th = I5.frob(R0s, mu, z, N)
        cols.append([q for q in val] + [q * (1 - z) for q in th])
    for nu in allow:
        val, th = I5.frob(Rinf, -nu, z, N)
        cols.append([q for q in val] + [-q * (1 - z) for q in th])
    C = mp.matrix(2 * K, 2 * K)
    for j, c in enumerate(cols):
        nrm = max(abs(q) for q in c)
        for i in range(2 * K):
            C[i, j] = c[i] / nrm
    assert hit == 1
    return mp.re(mp.det(C))


def c3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ok = True
    runs = [("s0", 10, 50, 260), ("s0", 100, 100, 700), ("t2", 10, 50, 260)]
    for typ, g, dps, N in runs:
        mp.mp.dps = dps
        M0, M1, _ = I5.mats(4, typ, L5.Lbar)
        subs = dict(L5.POINT)
        subs[L5.gC] = g
        F = I5.numeric(M0, M1, subs)
        f = lambda L: mp.re(I5.connection(*F(L), L, N=N, colnorm=True)[0])
        grid = [mp.mpf(q) + mp.mpf(1) / 997 for q in ("1.2", "1.5", "1.8", "1.95", "2.3")]
        scale = max(abs(f(L)) for L in grid)
        gU_, eU_ = mp.mpf(1) / 100, mp.mpf(1) / 100
        lams = [mp.mpf(3) / 2 + (1 - eU_) * gU_, mp.mpf(3) / 2 + 2 * gU_] if typ == "s0" else [mp.mpf(3) / 2]
        for lam in lams:
            d0 = conn_at(*F(lam), lam, lam, N, off=control == 2)
            dm, dp = f(lam - mp.mpf(10)**-15), f(lam + mp.mpf(10)**-15)
            near = max(abs(d0 - dm), abs(d0 - dp)) < mp.mpf(10)**-9 * abs(d0)     # the noise is 10^-11 at gam_C = 100
            big = abs(d0) > mp.mpf(3) / 10 * scale
            if control == 1:
                big = abs(d0) < mp.mpf(10)**-4 * scale
            good = near and big
            chk(f"{typ}, gam_C = {g}: at lam = {mp.nstr(lam, 6)} the determinant {mp.nstr(d0, 8)} (scale "
                f"{mp.nstr(scale, 5)}), at lam +- 10^-15 {mp.nstr(dm, 8)}, {mp.nstr(dp, 8)}", good)
            ok &= good
    return ok


CHECKS = [("C1 the five-dimensional (5.28) at h = 0 in his splitting; four dimensions his printed matrix", c1, 1),
          ("C2 det L1 by type is the product over the slots it occupies: s0, v1, v2, t2", c2, 1),
          ("C3 no resonant state at the radiative exponents of pi_01 and pi_11 (s0) and of the tensor (t2)", c3, 2)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<112} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"scri5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"scri5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    verbose = "--verbose" in args
    if "--only" in args:
        k = int(args[args.index("--only") + 1])
        name, fn, nc = CHECKS[k - 1]
        print(name, "PASS" if fn(verbose=True) else "FAIL")
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    else:
        sys.exit(0 if selftest(verbose) else 1)
