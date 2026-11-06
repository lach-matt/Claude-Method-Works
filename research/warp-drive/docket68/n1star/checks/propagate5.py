#!/usr/bin/env python3
"""propagate5: the propagation of the gauge condition W := Upsilon(g) - H = 0 (FAMILIES5 4e, D428).

Section 1's reduced equation is the vacuum one, Ric(g) - dstar_g W = 0. P1-P3 hold for any metric g and any 1-form
W, so the fixed source H enters only through W. Exact rational arithmetic on random polynomial jets at the origin
(degree 3, truncated, with every derivative counted, so the degree-0 coefficients are exact):

  P1  B_g Ric(g) = 0, with B_g := delta_g + (1/2) d tr_g and (delta_g h)_b := -nabla^a h_ab (contracted Bianchi).
  P2  B_g dstar_g W = -(1/2)(box_g W + Ric(g)(W)), with (dstar W)_ab := (1/2)(nabla_a W_b + nabla_b W_a).
      So a solution of the reduced equation has box_g W + Ric(g)(W) = 0: W solves a linear wave equation.
  P3  If W = 0 on {t = 0}, then n^a (dstar W - (1/2) tr(dstar W) g)_ab = (1/2) n^0 d_t W_b there, n^a := g^(a0).
      For a solution of the reduced equation the left side is G(g)(n, .), so the constraints give d_t W = 0
      (n^0 = g^(00) < 0 for a spacelike {t = 0}).
  P4  W = 0 on {t = 0} can be imposed: at a point, Upsilon_b := g_bc g^(ad) Gamma^c_ad is affine in
      q_mu := d_t g_(0 mu) with coefficient g^(00) diag(1/2, 1, 1, 1), invertible. stage0two5's
      D = g^(ab)(Gamma - Gamma0)_ab, lowered, has the same q-part (Gamma0 is the background's).

Controls: P1 with d tr in place of (1/2) d tr fails; P2 without the curvature term fails; P3 for a W vanishing on
{x1 = 0} instead fails; P4 at the Minkowski metric with d_t g_(1 mu) in place of d_t g_(0 mu) has rank 2.

Not computed: uniqueness for the linear wave equation with zero data (the standard energy estimate), and that the
record's solution solves the reduced equation exactly.
"""
import random
import sys
from fractions import Fraction as Fr
from itertools import product

import sympy as sp

K = 3
IDX = range(4)
ZERO = (0, 0, 0, 0)


class Jet:
    """a polynomial in y0..y3 truncated at total degree K, exact rational coefficients"""
    __slots__ = ("c",)

    def __init__(self, c=None):
        self.c = {k: v for k, v in (c or {}).items() if v != 0}

    @staticmethod
    def const(x):
        return Jet({ZERO: Fr(x)})

    @staticmethod
    def lift(o):
        return o if isinstance(o, Jet) else Jet.const(o)

    def __add__(self, o):
        c = dict(self.c)
        for k, v in Jet.lift(o).c.items():
            c[k] = c.get(k, 0) + v
        return Jet(c)

    __radd__ = __add__

    def __neg__(self):
        return Jet({k: -v for k, v in self.c.items()})

    def __sub__(self, o):
        return self + (-Jet.lift(o))

    def __rsub__(self, o):
        return (-self) + o

    def __mul__(self, o):
        if not isinstance(o, Jet):
            o = Fr(o)
            return Jet({k: v * o for k, v in self.c.items()})
        c = {}
        for k1, v1 in self.c.items():
            s1 = sum(k1)
            for k2, v2 in o.c.items():
                if s1 + sum(k2) <= K:
                    k = (k1[0] + k2[0], k1[1] + k2[1], k1[2] + k2[2], k1[3] + k2[3])
                    c[k] = c.get(k, 0) + v1 * v2
        return Jet(c)

    __rmul__ = __mul__

    def d(self, i):
        c = {}
        for k, v in self.c.items():
            if k[i]:
                kk = list(k)
                kk[i] -= 1
                c[tuple(kk)] = v * k[i]
        return Jet(c)

    def at0(self):
        return self.c.get(ZERO, Fr(0))


Y = [Jet({tuple(int(i == j) for j in IDX): Fr(1)}) for i in IDX]


def rnd(r, den=10, span=5):
    return Fr(r.randint(-span, span), den)


def random_poly(r, lo, hi, den=10, span=5):
    return Jet({m: rnd(r, den, span) for m in product(range(K + 1), repeat=4) if lo <= sum(m) <= hi})


def jsum(it):
    return sum(it, Jet())


def matmul(A, B):
    return [[jsum(A[i][k] * B[k][j] for k in IDX) for j in IDX] for i in IDX]


def random_metric(r):
    while True:
        g0 = sp.diag(-1, 1, 1, 1)
        for i in IDX:
            for j in range(i, 4):
                c = sp.Rational(r.randint(-3, 3), 20)
                g0[i, j] += c
                if i != j:
                    g0[j, i] += c
        if g0.inv()[0, 0] < 0 and all(g0[1:k + 1, 1:k + 1].det() > 0 for k in (1, 2, 3)):
            break
    g = [[None] * 4 for _ in IDX]
    for i in IDX:
        for j in range(i, 4):
            g[i][j] = g[j][i] = Jet.const(Fr(g0[i, j].p, g0[i, j].q)) + random_poly(r, 1, K, 10, 4)
    return g, g0


def inverse(g, g0):
    """Neumann series about g0 = g(0): exact to degree K since g - g0 has no constant term"""
    gi0 = g0.inv()
    G0 = [[Jet.const(Fr(gi0[i, j].p, gi0[i, j].q)) for j in IDX] for i in IDX]
    dlt = [[g[i][j] - g[i][j].at0() for j in IDX] for i in IDX]
    M = [[-x for x in row] for row in matmul(G0, dlt)]
    term, out = G0, G0
    for _ in range(K):
        term = matmul(M, term)
        out = [[out[i][j] + term[i][j] for j in IDX] for i in IDX]
    return out


class Geo:
    def __init__(self, g, g0):
        self.g = g
        self.gi = gi = inverse(g, g0)
        self.G = G = [[[jsum(gi[c][e] * (g[e][b].d(a) + g[e][a].d(b) - g[a][b].d(e)) for e in IDX) * Fr(1, 2)
                        for b in IDX] for a in IDX] for c in IDX]
        self.R = [[jsum(G[c][a][b].d(c) - G[c][a][c].d(b) for c in IDX)
                   + jsum(G[c][c][e] * G[e][a][b] - G[c][b][e] * G[e][a][c] for c in IDX for e in IDX)
                   for b in IDX] for a in IDX]

    def nabla1(self, W):
        return [[W[b].d(a) - jsum(self.G[c][a][b] * W[c] for c in IDX) for b in IDX] for a in IDX]

    def nabla2(self, T):
        G = self.G
        return [[[T[a][b].d(c) - jsum(G[e][c][a] * T[e][b] + G[e][c][b] * T[a][e] for e in IDX)
                  for b in IDX] for a in IDX] for c in IDX]

    def tr(self, T):
        return jsum(self.gi[a][b] * T[a][b] for a in IDX for b in IDX)

    def B(self, T, half=Fr(1, 2)):
        nT, t = self.nabla2(T), self.tr(T)
        return [-jsum(self.gi[c][a] * nT[c][a][b] for a in IDX for c in IDX) + t.d(b) * half for b in IDX]

    def dstar(self, W):
        nW = self.nabla1(W)
        return [[(nW[a][b] + nW[b][a]) * Fr(1, 2) for b in IDX] for a in IDX]

    def box(self, W):
        nnW = self.nabla2(self.nabla1(W))
        return [jsum(self.gi[a][c] * nnW[a][c][b] for a in IDX for c in IDX) for b in IDX]

    def ricW(self, W):
        return [jsum(self.R[b][c] * self.gi[c][e] * W[e] for c in IDX for e in IDX) for b in IDX]


def ups0(g, gi):
    """Upsilon_b = g^(ad)(d_a g_db - (1/2) d_b g_ad) at the origin (= g_bc g^(ad) Gamma^c_ad)"""
    return [sum((gi[a][e].at0() * (g[e][b].d(a).at0() - g[a][e].d(b).at0() / 2) for a in IDX for e in IDX), Fr(0))
            for b in IDX]


def ups_jac(g, gi, row):
    """the coefficient of q_mu := d_t g_(row mu)(0) in Upsilon(0): exact, since Upsilon(0) is linear in dg(0)"""
    def with_q(mu, val):
        h = [[Jet(x.c) for x in rr] for rr in g]
        for a, b in ((row, mu), (mu, row)):
            c = dict(h[a][b].c)
            c[(1, 0, 0, 0)] = Fr(val)
            h[a][b] = Jet(c)
        return h
    cols = []
    for mu in IDX:
        u1, u0 = ups0(with_q(mu, 1), gi), ups0(with_q(mu, 0), gi)
        cols.append([x - y for x, y in zip(u1, u0)])
    return sp.Matrix(4, 4, lambda b, mu: cols[mu][b])


def main():
    ok = True
    for seed in (1, 2, 3):
        r = random.Random(seed)
        g, g0 = random_metric(r)
        geo = Geo(g, g0)
        W = [random_poly(r, 0, K) for _ in IDX]

        p1 = [x.at0() for x in geo.B(geo.R)]
        c1 = [x.at0() for x in geo.B(geo.R, half=Fr(1))]
        P1 = all(x == 0 for x in p1) and any(x != 0 for x in c1)

        bd, bx, rw = geo.B(geo.dstar(W)), geo.box(W), geo.ricW(W)
        p2 = [(bd[b] + (bx[b] + rw[b]) * Fr(1, 2)).at0() for b in IDX]
        c2 = [(bd[b] + bx[b] * Fr(1, 2)).at0() for b in IDX]
        P2 = all(x == 0 for x in p2) and any(x != 0 for x in c2)

        V = [random_poly(r, 0, 2) for _ in IDX]

        def constraint(coord):
            S = geo.dstar([Y[coord] * v for v in V])
            t = geo.tr(S)
            E = [jsum(geo.gi[a][0] * (S[a][b] - t * g[a][b] * Fr(1, 2)) for a in IDX).at0() for b in IDX]
            return E, [geo.gi[0][0].at0() * v.at0() / 2 for v in V]
        E, rhs = constraint(0)
        Ec, rhsc = constraint(1)
        P3 = E == rhs and Ec != rhsc

        g00 = geo.gi[0][0].at0()
        J = ups_jac(g, geo.gi, 0)
        form = J == g00 * sp.diag(sp.Rational(1, 2), 1, 1, 1)
        P4 = form and J.det() != 0

        print(f"seed {seed}: g^00 = {float(g00):.4f}")
        print(f"  P1 B Ric = {[int(x) for x in p1]}; control (d tr): {[round(float(x), 4) for x in c1]}  "
              f"{'PASS' if P1 else 'FAIL'}")
        print(f"  P2 B dstar W + (box W + Ric W)/2 = {[int(x) for x in p2]}; control (no Ric W): "
              f"{[round(float(x), 4) for x in c2]}  {'PASS' if P2 else 'FAIL'}")
        print(f"  P3 G(n, .) = (1/2) n^0 d_t W on t = 0: {E == rhs}; control on x1 = 0 differs: {Ec != rhsc}  "
              f"{'PASS' if P3 else 'FAIL'}")
        print(f"  P4 dUpsilon/dq = g^00 diag(1/2, 1, 1, 1): {form}, det = {float(J.det()):.6g}  "
              f"{'PASS' if P4 else 'FAIL'}")
        ok = ok and P1 and P2 and P3 and P4

    r = random.Random(7)
    eta = [[Fr(-1) if i == j == 0 else Fr(int(i == j)) for j in IDX] for i in IDX]
    geta = [[None] * 4 for _ in IDX]
    for i in IDX:
        for j in range(i, 4):
            geta[i][j] = geta[j][i] = Jet.const(eta[i][j]) + random_poly(r, 1, 1)
    gi_eta = [[Jet.const(eta[i][j]) for j in IDX] for i in IDX]
    Jt, Jc = ups_jac(geta, gi_eta, 0), ups_jac(geta, gi_eta, 1)
    t_ok = Jt == sp.diag(-sp.Rational(1, 2), -1, -1, -1)
    C4 = t_ok and Jc.rank() == 2
    print(f"  P4 control at Minkowski: d_t g_(0 mu) gives diag(-1/2, -1, -1, -1): {t_ok}; d_t g_(1 mu) has rank "
          f"{Jc.rank()}  {'PASS' if C4 else 'FAIL'}")
    ok = ok and C4
    print("ALL PASS" if ok else "SOME FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
