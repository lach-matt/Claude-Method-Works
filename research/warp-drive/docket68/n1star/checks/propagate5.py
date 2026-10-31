#!/usr/bin/env python3
"""propagate5: the propagation of the gauge condition W := Upsilon(g) - H = 0 (FAMILIES5 4e, D428).

Section 1's reduced equation is the vacuum one, Ric(g) - dstar_g W = 0. Everything below holds for any metric g
and any 1-form W, so the fixed source H enters only through W. Exact rational arithmetic on random polynomial
jets at the origin (degree 3, every derivative counted, so the degree-0 coefficients are exact):

  P1  B_g Ric(g) = 0, with B_g := delta_g + (1/2) d tr_g and (delta_g h)_b := -nabla^a h_ab (contracted Bianchi).
  P2  B_g dstar_g W = -(1/2)(box_g W + Ric(g)(W)), with (dstar W)_ab := (1/2)(nabla_a W_b + nabla_b W_a).
      So a solution of the reduced equation has box_g W + Ric(g)(W) = 0: W solves a linear wave equation.
  P3  If W = 0 on {t = 0}, then n^a (dstar W - (1/2) tr(dstar W) g)_ab = (1/2) n^0 d_t W_b there, n^a := g^(a0).
      The left side is G(g)(n, .) for a solution of the reduced equation, so the constraints give d_t W = 0
      (n^0 = g^(00) < 0 for a spacelike {t = 0}).
  P4  W = 0 on {t = 0} can be imposed: Upsilon(g)|_(t=0) is affine in d_t g_(0 mu) with invertible coefficient.

Controls: P1 with d tr in place of (1/2) d tr fails; P2 without the curvature term fails; P3 for a W vanishing on
{x1 = 0} instead fails; P4's coefficient is singular if d_t g_(0 mu) is replaced by d_t g_(1 mu).

Not computed: uniqueness for the linear wave equation (standard energy estimate), and that the record's
solution solves the reduced equation exactly.
"""
import random
import sys
from fractions import Fraction as Fr

import sympy as sp

Y = sp.symbols("y0:4")
K = 3
IDX = range(4)


def trunc(e, k=K):
    e = sp.expand(e)
    if e == 0:
        return sp.Integer(0)
    p = sp.Poly(e, *Y)
    return sp.Add(*[c * sp.prod([y ** m for y, m in zip(Y, mon)]) for mon, c in p.terms() if sum(mon) <= k])


def at0(e):
    return sp.expand(e).subs({y: 0 for y in Y})


def d(e, i):
    return sp.diff(e, Y[i])


def monomials(lo, hi):
    out = []
    for m in sp.itermonomials(Y, hi):
        if lo <= sp.Poly(m, *Y).total_degree() <= hi:
            out.append(m)
    return sorted(out, key=sp.default_sort_key)


def rnd(r, den=10, span=5):
    return sp.Rational(r.randint(-span, span), den)


def random_metric(r):
    while True:
        g0 = sp.diag(-1, 1, 1, 1) + sp.Matrix(4, 4, lambda i, j: 0)
        for i in IDX:
            for j in range(i, 4):
                c = rnd(r, 20, 3)
                g0[i, j] += c
                if i != j:
                    g0[j, i] += c
        gi0 = g0.inv()
        if gi0[0, 0] < 0 and all(g0[1:k + 1, 1:k + 1].det() > 0 for k in (1, 2, 3)):
            break
    mons = monomials(1, K)
    g = sp.Matrix(4, 4, lambda i, j: 0)
    for i in IDX:
        for j in range(i, 4):
            p = g0[i, j] + sum(rnd(r, 10, 4) * m for m in mons)
            g[i, j] = p
            g[j, i] = p
    return g, g0


def inverse(g, g0):
    gi0 = g0.inv()
    dlt = g - g0
    term = gi0
    out = gi0
    for _ in range(K):
        term = (-gi0 * dlt * term).applyfunc(trunc)
        out = out + term
    return out.applyfunc(trunc)


class Geo:
    def __init__(self, g, g0):
        self.g = g
        self.gi = inverse(g, g0)
        gi = self.gi
        self.G = [[[trunc(sum(gi[c, e] * (d(g[e, b], a) + d(g[e, a], b) - d(g[a, b], e)) for e in IDX) / 2)
                    for b in IDX] for a in IDX] for c in IDX]
        G = self.G
        self.R = sp.Matrix(4, 4, lambda a, b: trunc(
            sum(d(G[c][a][b], c) - d(G[c][a][c], b) for c in IDX)
            + sum(G[c][c][e] * G[e][a][b] - G[c][b][e] * G[e][a][c] for c in IDX for e in IDX)))

    def nabla1(self, W):
        return sp.Matrix(4, 4, lambda a, b: trunc(d(W[b], a) - sum(self.G[c][a][b] * W[c] for c in IDX)))

    def nabla2(self, T):
        G = self.G
        return [sp.Matrix(4, 4, lambda a, b: trunc(
            d(T[a, b], c) - sum(G[e][c][a] * T[e, b] + G[e][c][b] * T[a, e] for e in IDX))) for c in IDX]

    def tr(self, T):
        return trunc(sum(self.gi[a, b] * T[a, b] for a in IDX for b in IDX))

    def delta(self, T):
        nT = self.nabla2(T)
        return [trunc(-sum(self.gi[c, a] * nT[c][a, b] for a in IDX for c in IDX)) for b in IDX]

    def B(self, T, half=sp.Rational(1, 2)):
        dT, t = self.delta(T), self.tr(T)
        return [trunc(dT[b] + half * d(t, b)) for b in IDX]

    def dstar(self, W):
        nW = self.nabla1(W)
        return sp.Matrix(4, 4, lambda a, b: (nW[a, b] + nW[b, a]) / 2)

    def box(self, W):
        nnW = self.nabla2(self.nabla1(W))
        return [trunc(sum(self.gi[a, c] * nnW[a][c, b] for a in IDX for c in IDX)) for b in IDX]

    def ricW(self, W):
        return [trunc(sum(self.R[b, c] * self.gi[c, e] * W[e] for c in IDX for e in IDX)) for b in IDX]

    def ups(self):
        return [trunc(sum(self.g[b, c] * self.gi[a, e] * self.G[c][a][e] for a in IDX for c in IDX for e in IDX))
                for b in IDX]


def random_form(r, lo, hi):
    mons = monomials(lo, hi)
    return [sum(rnd(r, 10, 5) * m for m in mons) for _ in IDX]


def main():
    ok = True
    for seed in (1, 2, 3):
        r = random.Random(seed)
        g, g0 = random_metric(r)
        geo = Geo(g, g0)
        W = [w + rnd(r) for w in random_form(r, 1, K)]

        p1 = [at0(x) for x in geo.B(geo.R)]
        c1 = [at0(x) for x in geo.B(geo.R, half=1)]
        P1 = all(x == 0 for x in p1) and any(x != 0 for x in c1)

        bd, bx, rw = geo.B(geo.dstar(W)), geo.box(W), geo.ricW(W)
        p2 = [at0(bd[b] + (bx[b] + rw[b]) / 2) for b in IDX]
        c2 = [at0(bd[b] + bx[b] / 2) for b in IDX]
        P2 = all(x == 0 for x in p2) and any(x != 0 for x in c2)

        V = random_form(r, 0, 2)

        def constraint(coord):
            Wt = [Y[coord] * v for v in V]
            S = geo.dstar(Wt)
            t = geo.tr(S)
            E = [at0(sum(geo.gi[a, 0] * (S[a, b] - t * g[a, b] / 2) for a in IDX)) for b in IDX]
            return E, [at0(geo.gi[0, 0] * v / 2) for v in V]
        E, rhs = constraint(0)
        Ec, rhsc = constraint(1)
        P3 = all(sp.simplify(x - y) == 0 for x, y in zip(E, rhs)) and any(x != y for x, y in zip(Ec, rhsc))

        # P4: replace d_t g_(0 mu) at the origin by unknowns q_mu and read Upsilon's coefficient matrix.
        def jac(row):
            q = sp.symbols("q0:4")
            gq = sp.Matrix(g)
            for mu in IDX:
                a, b = (row, mu)
                old = sp.Poly(sp.expand(gq[a, b]), *Y).coeff_monomial(Y[0])
                gq[a, b] = gq[a, b] + (q[mu] - old) * Y[0]
                if a != b:
                    gq[b, a] = gq[a, b]
            u = Geo(gq, g0).ups()
            return sp.Matrix(4, 4, lambda b, mu: sp.diff(at0(u[b]), q[mu]))
        J = jac(0)
        Jc = jac(1)
        detJ, detJc = J.det(), Jc.det()
        P4 = detJ != 0 and detJc == 0

        print(f"seed {seed}: g^00 = {float(geo.gi[0, 0].subs({y: 0 for y in Y})):.4f}")
        print(f"  P1 B Ric = {p1}; control |d tr| = {[float(x) for x in c1][:2]}...  {'PASS' if P1 else 'FAIL'}")
        print(f"  P2 B dstar W + (box W + Ric W)/2 = {p2}; control (no Ric) = {[float(x) for x in c2][:2]}...  "
              f"{'PASS' if P2 else 'FAIL'}")
        print(f"  P3 G(n,.) = (1/2) n^0 d_t W: {'PASS' if P3 else 'FAIL'} (control on x1 = 0 differs: "
              f"{any(x != y for x, y in zip(Ec, rhsc))})")
        print(f"  P4 det d Upsilon / d(d_t g_0mu) = {float(detJ):.6g}; control d_t g_1mu: det = {detJc}  "
              f"{'PASS' if P4 else 'FAIL'}")
        ok = ok and P1 and P2 and P3 and P4
    print("ALL PASS" if ok else "SOME FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
