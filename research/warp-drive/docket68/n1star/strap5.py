#!/usr/bin/env python3
"""strap5.py -- [Hin26] Proposition 8.3 in five dimensions: the subprincipal part of the linearized gauge-fixed Einstein
operator at the trapped set, and its strong trapping admissibility on five-dimensional Tangherlini (N1STAR-PROOF.md
section 10.26; ROUTES-OPEN.md 4.27; D75).  Labels: computed (exact, sympy), deduced, READ.

[Hin26] (arXiv:2606.28253v2) Proposition 8.3 (pp. 147-149): 2 L_b is strongly trapping admissible.  His proof: E^Ups
vanishes near the trapped set, so i S_sub(2 L) = i S_sub(box) + 2 E^C sigma_1(i delta) G ((8.10)); in the frame e_mu of
(6.16b), with nabla_{H_G} = H_G + 2 sigma N on 1-forms ((6.16c)) and its Leibniz extension to S^2 in the splitting
(8.11), sigma_1(i delta) = -C^(1/2) iota_{e_2}, g = -2 e_0 e_2 + e_1^2 + e_3^2 and E^C = gam_C (2 c (x)_s . - (1 - e_C)
g <c, .>), he finds i S_sub(2 L) = H_G + sigma A with a printed 10 x 10 matrix A (p. 148), gam := C^(1/2) gam_C/sigma,
upper triangular in the basis (8.12) with diagonal 0 (6x), -2 (1 - e_C) gam c_2, -2 gam c_2 (2x), -4 gam c_2; c_2 = -g^-1
(c^C, e_0) < 0 because c^C is past timelike and e_0 future null, so every eigenvalue is >= 0, and the inner product
diag(1, eta^-1, ..., eta^-9) in (8.12) makes the symmetric part >= -C eta.  10.17 computed, on five-dimensional
Tangherlini, the frame e_0, e_1, e_2 with nabla_{H_G} e_0 = 0, nabla_{H_G} e_1 = -2 sigma e_0, nabla_{H_G} e_2 = -2 sigma
e_1 (trap5.py T3; his +2 sigma is the same with e_1 -> -e_1) and the angular plane V of covectors orthogonal to all
three, on which nabla_{H_G} is g-skew.  Here the frame is abstract: covectors e_0, ..., e_n with g^-1 Gram
[[0, 0, -1], [0, 1, 0], [-1, 0, 0]] (+) Id_(n-2), c = c_mu e_mu, and the 1-form part of nabla_{H_G}/sigma is s N.

  P1 (computed, exact) Four-dimensional control: with his sign (s = +2), the trace weight 1 and his splitting (8.11),
     the computed A equals his printed matrix in all 100 entries; it is upper triangular in his basis (8.12) with his
     diagonal.  Control: the computed sign s = -2 against his printed matrix, which then differs.
  P2 (computed, exact) Five dimensions, c general: the characteristic polynomial of the 15 x 15 A is lam^10 (lam + 2 gam
     c_2)^3 (lam + 4 gam c_2)(lam + 2 (1 - e_C) gam c_2) -- at the trace weight 1 the last factor is lam + 3 (1 - e_C)
     gam c_2 -- and A is upper triangular in the constant basis e_0^2, e_0 e_1, e_0 e_2, e_0 e_3, e_0 e_4, e_1 e_3, e_1
     e_4, e_3 e_4, e_1^2 - e_3^2, e_1^2 - e_4^2, e_1^2, e_1 e_2, e_2 e_3, e_2 e_4, e_2^2 for every c, gam, e_C.
     Control: e_1^2 placed before e_1^2 - e_3^2, where A is not upper triangular.
  P3 (computed, exact) Five dimensions, c with no angular part (c_3 = c_4 = 0, as 10.14's c = a(r) dt + b(r) dr):
     A commutes with the rotation of the angular plane, extended to S^2; in the units e_0^2, e_0 e_1, e_0 e_2, e_1^2 -
     T/2, e_1^2, e_1 e_2, e_2^2, (e_0 e_3, e_0 e_4), (e_1 e_3, e_1 e_4), (e_2 e_3, e_2 e_4), (e_3 e_4, e_3^2 - e_4^2),
     T = e_3^2 + e_4^2, it is block upper triangular with scalar diagonal blocks 0, 0, 0, 0, -2 (1 - e_C) gam c_2, -2 gam
     c_2, -4 gam c_2, 0, 0, -2 gam c_2, 0, and the rotation acts within each unit, skew; for the inner product weighting
     unit k by eta^-k, the rescaled A tends to that block diagonal as eta -> 0.  Control: c_4 != 0, where A does not
     commute with the rotation.

Deduced, not computed here: his Proposition 8.3 on five-dimensional Tangherlini, with E^Ups vanishing near the photon
sphere ((6.1)) and 10.14's c, past timelike there, so that c_2 < 0 and every diagonal block is >= 0: the inner product
of P3 -- stationary, homogeneous of degree 0, the angular pairs weighted alike so that the rotation of V along the flow
stays skew -- gives sigma^-1 (1/2)(i S_sub(2 L) + (i S_sub(2 L))^*) > -C eta^(1/2) at the trapped set, below any eps for
small eta (N1STAR-PROOF.md 10.26).

READ.  [Hin26] pp. 34 (item (1), strong trapping admissibility), 113-116 (section 6.1: (6.12)-(6.16c), Lemma 6.4),
147-149 (section 8.1: Proposition 8.3 and its proof, (8.9)-(8.12), the printed A, its eigenvalues and footnote 77);
alphaXiv, 2026-10-23.

sympy.  python3 strap5.py [--selftest | --mutants]   (--verbose lists every sub-check; under a minute)
"""
import sys
import time

import sympy as sp

from damping5 import Checklist

gam, eC = sp.symbols("gamma e_C", positive=True)
lam = sp.Symbol("lam")                                     # plain: charpoly's generator carries no assumptions
eta = sp.Symbol("eta", positive=True)


def build(n, m, s=-2):
    """A with i S_sub(2 L) = H_G + sigma A, on S^2 of the abstract frame; components h^{ab} (a <= b) in the basis
    e_a e_b (a = b) and 2 e_a (x)_s e_b (a < b), his (8.11)'s normalization"""
    N = n + 1
    Gi = sp.zeros(N, N)
    Gi[0, 2] = Gi[2, 0] = -1
    Gi[1, 1] = 1
    for k in range(3, N):
        Gi[k, k] = 1
    c = sp.symbols("c0:%d" % N, real=True)
    M1 = sp.zeros(N, N)
    M1[0, 1] = s                                       # nabla e_1 = s sigma e_0
    M1[1, 2] = s                                       # nabla e_2 = s sigma e_1
    pairs = [(a, b) for a in range(N) for b in range(a, N)]
    gmat = Gi.inv()

    def mat(x):
        H = sp.zeros(N, N)
        for i, (a, b) in enumerate(pairs):
            H[a, b] = H[b, a] = x[i]
        return H
    cols = []
    for i in range(len(pairs)):
        H = mat(sp.eye(len(pairs))[:, i])
        Hn = M1 * H + H * M1.T                         # Leibniz
        tr = sum(Gi[a, b] * H[a, b] for a in range(N) for b in range(N))
        GH = H - gmat * tr / 2
        w = [-GH[2, b] for b in range(N)]              # sigma_1(i delta) = -C^(1/2) iota_{e_2}
        cw = sum(Gi[a, b] * c[a] * w[b] for a in range(N) for b in range(N))
        E = sp.Matrix(N, N, lambda a, b: c[a] * w[b] + c[b] * w[a] - m * (1 - eC) * gmat[a, b] * cw)
        Hs = Hn + 2 * gam * E
        cols.append(sp.Matrix([Hs[a, b] for a, b in pairs]))
    return sp.Matrix.hstack(*cols), pairs, c


def mono(pairs, a, b):
    v = sp.zeros(len(pairs), 1)
    v[pairs.index((min(a, b), max(a, b)))] = 1
    return v


def upper(A, basis):
    Pm = sp.Matrix.hstack(*basis)
    T = (Pm.inv() * A * Pm).applyfunc(sp.simplify)
    d = T.shape[0]
    return all(T[i, j] == 0 for i in range(d) for j in range(d) if i > j), [sp.factor(T[i, i]) for i in range(d)]


# ------------------------------------------------------------------------------------------------- P1
HIS = None


def his_A(c):
    g, e = gam, eC
    c0, c1, c2, c3 = c
    return sp.Matrix([
        [0, 4, 0, 0, -2*g*c0, 0, 0, 0, 0, -2*g*c0],
        [0, 0, 2, 0, 2 - g*c1, -2*g*c0, 0, 0, 0, -g*c1],
        [0, 0, 0, 0, -e*g*c2, 2 - 2*(1 - e)*g*c1, 0, -2*e*g*c0, -2*(1 - e)*g*c3, -e*g*c2],
        [0, 0, 0, 0, -g*c3, 0, 2, 0, -2*g*c0, -g*c3],
        [0, 0, 0, 0, -(1 - e)*g*c2, 4 - 2*(1 + e)*g*c1, 0, -2*(1 - e)*g*c0, 2*(1 - e)*g*c3, -(1 - e)*g*c2],
        [0, 0, 0, 0, 0, -2*g*c2, 0, 2 - 2*g*c1, 0, 0],
        [0, 0, 0, 0, 0, -2*g*c3, 0, 0, 2 - 2*g*c1, 0],
        [0, 0, 0, 0, 0, 0, 0, -4*g*c2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, -2*g*c3, -2*g*c2, 0],
        [0, 0, 0, 0, -(1 - e)*g*c2, 2*(1 - e)*g*c1, 0, -2*(1 - e)*g*c0, -2*(1 + e)*g*c3, -(1 - e)*g*c2]])


def p1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    A, pairs, c = build(3, sp.Integer(1), s=2 if control != 1 else -2)
    order = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]       # (8.11)
    perm = [pairs.index(p) for p in order]
    Ah = A.extract(perm, perm)
    diff = (Ah - his_A(c)).applyfunc(sp.expand)
    nbad = sum(1 for q in diff if q != 0)
    mo = lambda a, b: mono(pairs, a, b)
    b812 = [mo(0, 0), mo(0, 3), mo(0, 1), mo(1, 3), mo(0, 2), mo(1, 1) - mo(3, 3), mo(3, 3), mo(1, 2), mo(2, 3),
            mo(2, 2)]                                                                            # his (8.12)
    tri, diag = upper(A, b812)
    c2 = c[2]
    want = [0] * 5 + [0] + [sp.factor(-2 * (1 - eC) * gam * c2)] + [sp.factor(-2 * gam * c2)] * 2 + [-4 * gam * c2]
    chk(f"n + 1 = 4: A in (8.11) against his printed matrix: {100 - nbad}/100 entries equal; upper triangular in "
        f"(8.12) with diagonal {diag}", nbad == 0 and tri and sorted(map(str, diag)) == sorted(map(str, want)))
    return chk.ok


# ------------------------------------------------------------------------------------------------- P2
def p2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    A, pairs, c = build(4, sp.Rational(2, 3))
    c2 = c[2]
    want = sp.expand(lam**10 * (lam + 2 * gam * c2)**3 * (lam + 4 * gam * c2) * (lam + 2 * (1 - eC) * gam * c2))
    cp = sp.expand(A.charpoly(lam).as_expr())
    A1, _, _ = build(4, sp.Integer(1))
    cp1 = sp.expand(A1.charpoly(lam).as_expr())
    want1 = sp.expand(lam**10 * (lam + 2 * gam * c2)**3 * (lam + 4 * gam * c2) * (lam + 3 * (1 - eC) * gam * c2))
    mo = lambda a, b: mono(pairs, a, b)
    basis = [mo(0, 0), mo(0, 1), mo(0, 2), mo(0, 3), mo(0, 4), mo(1, 3), mo(1, 4), mo(3, 4), mo(1, 1) - mo(3, 3),
             mo(1, 1) - mo(4, 4), mo(1, 1), mo(1, 2), mo(2, 3), mo(2, 4), mo(2, 2)]
    if control == 1:                                       # control: e_1^2 before e_1^2 - e_3^2
        basis[8], basis[10] = basis[10], basis[8]
    tri, diag = upper(A, basis)
    chk(f"n + 1 = 5, c general: charpoly lam^10 (lam + 2 gam c_2)^3 (lam + 4 gam c_2)(lam + 2 (1 - e_C) gam c_2), the "
        f"last factor lam + 3 (1 - e_C) gam c_2 at the weight 1; upper triangular in the constant basis, diagonal "
        f"{diag}", cp == want and cp1 == want1 and tri)
    return chk.ok


# ------------------------------------------------------------------------------------------------- P3
def p3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    A, pairs, c = build(4, sp.Rational(2, 3))
    A = A.subs({c[3]: 0, c[4]: 0 if control != 1 else sp.Rational(1, 3)})
    N, d = 5, len(pairs)
    R1 = sp.zeros(N, N)
    R1[3, 4], R1[4, 3] = -1, 1

    def mat(x):
        H = sp.zeros(N, N)
        for i, (a, b) in enumerate(pairs):
            H[a, b] = H[b, a] = x[i]
        return H
    RS = sp.Matrix.hstack(*[sp.Matrix([(R1 * mat(sp.eye(d)[:, i]) + mat(sp.eye(d)[:, i]) * R1.T)[a, b]
                                       for a, b in pairs]) for i in range(d)])
    commute = (A * RS - RS * A).applyfunc(sp.expand) == sp.zeros(d, d)
    mo = lambda a, b: mono(pairs, a, b)
    T_ = mo(3, 3) + mo(4, 4)
    units = [[mo(0, 0)], [mo(0, 1)], [mo(0, 2)], [mo(1, 1) - T_ / 2], [mo(1, 1)], [mo(1, 2)], [mo(2, 2)],
             [mo(0, 3), mo(0, 4)], [mo(1, 3), mo(1, 4)], [mo(2, 3), mo(2, 4)], [mo(3, 4), mo(3, 3) - mo(4, 4)]]
    Pm = sp.Matrix.hstack(*sum(units, []))
    Tm = (Pm.inv() * A * Pm).applyfunc(sp.simplify)
    Rm = (Pm.inv() * RS * Pm).applyfunc(sp.simplify)
    sizes = [len(u) for u in units]
    starts = [sum(sizes[:k]) for k in range(len(sizes))]
    blocks, okb, okr = [], True, True
    W = sp.zeros(d, d)
    for k, (s0, sz) in enumerate(zip(starts, sizes)):
        blk = Tm[s0:s0 + sz, s0:s0 + sz]
        okb &= blk == blk[0, 0] * sp.eye(sz)
        okb &= all(Tm[i, j] == 0 for i in range(s0 + sz, d) for j in range(s0, s0 + sz))
        okr &= all(Rm[i, j] == 0 for i in range(d) for j in range(s0, s0 + sz) if not s0 <= i < s0 + sz)
        okr &= Rm[s0:s0 + sz, s0:s0 + sz] == -Rm[s0:s0 + sz, s0:s0 + sz].T
        blocks.append(sp.factor(blk[0, 0]))
        for i in range(s0, s0 + sz):
            W[i, i] = eta**sp.Rational(k, 2)                     # rescaled orthonormal basis: eta^(k/2) times unit k
    At = (W.inv() * Tm * W).applyfunc(sp.simplify)                  # in the eta-orthonormal basis
    lim = At.applyfunc(lambda q: sp.limit(q, eta, 0)) == sp.diag(*[blocks[k] for k in range(len(units))
                                                                   for _ in range(sizes[k])])
    chk(f"n + 1 = 5, c_3 = c_4 = 0: A commutes with the rotation of the angular plane; in the units, block upper "
        f"triangular with scalar diagonal blocks {blocks}; the rotation within the units, skew; the eta-rescaled A "
        f"tends to the block diagonal", commute and okb and okr and lim)
    return chk.ok


CHECKS = [("P1 four-dimensional control: his printed A (p. 148) in all 100 entries, triangular in his (8.12)", p1, 1),
          ("P2 five dimensions, c general: the spectrum of A and a constant basis in which it is upper triangular",
           p2, 1),
          ("P3 five dimensions, c with no angular part: the rotation commutes; block triangular, scalar blocks", p3, 1)]


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
    print(f"strap5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"strap5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
