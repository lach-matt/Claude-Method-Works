#!/usr/bin/env python3
"""lgrade5.py -- the grading behind Part III.F Proposition 4.1 ([Hin26] Proposition 8.3 at n = 4; D228).  Label:
computed (exact, sympy).

strap5.py builds the 15 x 15 matrix A with i S_sub(2 L) = H_G + sigma A at the trapped set, in the abstract frame e_0,
..., e_4 (g^-1 Gram [[0, 0, -1], [0, 1, 0], [-1, 0, 0]] (+) Id_2), the 1-form part of nabla_{H_G}/sigma being the
nilpotent s N (N e_1 = e_0, N e_2 = e_1, s = -2), and c = sum c_mu e_mu.  Add k R, R the rotation of the plane of e_3,
e_4 (the angular plane, on which nabla_{H_G} is g-skew), extended to S^2 as a derivation.  Give e_0, e_1, e_2, e_3, e_4
the weights 0, 1, 2, 1, 1, a monomial the sum, and refine W := 2 wt + s with s = 1 on T := e_1^2 + e_3^2 + e_4^2 and on
the spatial trace-free part, s = 0 elsewhere.  The pieces: e_0^2 (W = 0); e_0 e_1, e_0 e_3, e_0 e_4 (2); e_0 e_2 (4);
T (5); the five spatial trace-free monomials (5); e_1 e_2, e_2 e_3, e_2 e_4 (6); e_2^2 (8).

  G1 (computed, exact) For every c (angular components included), gam, e_C and k: A + k R maps each piece into pieces
     of lower or equal W, and on each piece its W-preserving part is a scalar plus a skew part (skew for the inner
     product induced on S^2 by the one making e_0, ..., e_4 orthonormal): the scalars 0, 0, 0, -2 (1 - e_C) gam c_2, 0,
     -2 gam c_2, -4 gam c_2 in the order above (trace weight 2/3).  Controls: s = 1 on e_0 e_2 and 0 on T, where a map
     raises W (T -> e_0 e_2); and e_0 e_4 split off from e_0 e_3 into a piece of its own, which k R then joins
     to its partner's at the same W.

Run: python3 lgrade5.py (under a minute).
"""
import sys
import sympy as sp

from strap5 import build, mono, gam, eC

k = sp.Symbol('k', real=True)


def rot_S2(pairs, N):
    R = sp.zeros(N, N)
    R[3, 4], R[4, 3] = -1, 1                              # R e_3 = e_4, R e_4 = -e_3 on covector indices
    cols = []
    for i in range(len(pairs)):
        H = sp.zeros(N, N)
        a, b = pairs[i]
        H[a, b] = H[b, a] = 1
        Hr = R * H + H * R.T
        cols.append(sp.Matrix([Hr[a, b] for a, b in pairs]))
    return sp.Matrix.hstack(*cols)


def frob(pairs, N):
    def tens(v):
        H = sp.zeros(N, N)
        for i, (a, b) in enumerate(pairs):
            H[a, b] = H[b, a] = v[i]
        return H
    return lambda u, v: sum((tens(u)[a, b] * tens(v)[a, b]) for a in range(N) for b in range(N))


def check(swap_s=False, lone=False):
    A, pairs, c = build(4, sp.Rational(2, 3))
    N = 5
    Ak = A + k * rot_S2(pairs, N)
    mo = lambda a, b: mono(pairs, a, b)
    T = mo(1, 1) + mo(3, 3) + mo(4, 4)
    pieces = [
        ('e0^2', 0, [mo(0, 0)]),
        ('e0e1,e0e3,e0e4', 2, [mo(0, 1)] + ([mo(0, 3)] if lone else [mo(0, 3), mo(0, 4)])),
        ('e0e2', 5 if swap_s else 4, [mo(0, 2)]),
        ('T', 4 if swap_s else 5, [T]),
        ('tf', 5, [mo(1, 3), mo(1, 4), mo(3, 4), mo(1, 1) - mo(3, 3), mo(3, 3) - mo(4, 4)]),
        ('e1e2,e2e3,e2e4', 6, [mo(1, 2), mo(2, 3), mo(2, 4)]),
        ('e2^2', 8, [mo(2, 2)]),
    ]
    if lone:
        pieces.insert(2, ('e0e4', 2, [mo(0, 4)]))
    cols, W, owner = [], [], []
    for j, (name, w, vs) in enumerate(pieces):
        for v in vs:
            cols.append(v)
            W.append(w)
            owner.append(j)
    P = sp.Matrix.hstack(*cols)
    M = (P.inv() * Ak * P).applyfunc(sp.expand)
    d = M.shape[0]
    no_raise = all(M[i, j] == 0 for i in range(d) for j in range(d) if W[i] > W[j])
    ip = frob(pairs, N)
    scal = []
    ok_blocks = True
    for j, (name, w, vs) in enumerate(pieces):
        idx = [i for i in range(d) if owner[i] == j]
        # the W-preserving part on this piece, including maps to other pieces of the same W
        same = [i for i in range(d) if W[i] == w]
        if any(M[i, jj] != 0 for i in same for jj in idx if owner[i] != j):
            ok_blocks = False
        B = M.extract(idx, idx)
        lamb = sp.expand(sum(B[i, i] for i in range(len(idx))) / len(idx))
        S = B - lamb * sp.eye(len(idx))
        Gm = sp.Matrix(len(idx), len(idx), lambda a, b: ip(cols[idx[a]], cols[idx[b]]))
        skew = (Gm * S + S.T * Gm).applyfunc(sp.expand) == sp.zeros(len(idx), len(idx))
        ok_blocks &= skew
        scal.append(sp.factor(lamb))
    return no_raise, ok_blocks, scal, c


def run():
    nr, ob, scal, c = check()
    c2 = c[2]
    want = [0, 0, 0, sp.factor(-2 * (1 - eC) * gam * c2), 0, sp.factor(-2 * gam * c2), -4 * gam * c2]
    vals = all(sp.expand(a - b) == 0 for a, b in zip(scal, want))
    nr1, _, _, _ = check(swap_s=True)
    _, ob2, _, _ = check(lone=True)
    ok = nr and ob and vals and (not nr1) and (not ob2)
    print('G1 the grading: no raising, scalar + skew blocks, scalars', scal, ':', 'PASS' if ok else 'FAIL',
          '(controls fail as designed)' if (not nr1 and not ob2) else '(CONTROL DID NOT FAIL)')
    print('lgrade5.py:', 'all checks pass' if ok else 'FAILURES')
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
