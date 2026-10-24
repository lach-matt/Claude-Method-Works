#!/usr/bin/env python3
"""mp5.py -- [Hin26] section 7.2.1 in five dimensions on the full Myers-Perry family: Lemma 7.5 at every spin
(N1STAR-PROOF.md section 10.36; ROUTES-OPEN.md 4.37; D96).  Labels: computed (exact, sympy and rational arithmetic),
deduced, READ.

[Hin26] (arXiv:2606.28253v2) Lemma 7.5: for V a rotation 1-form and V_b = g_b gbar^-1 V, delta*_(g_b) V_b = rho^2 (-2 m
(dt* + dr) (x)_s rho V(S')) - delta*_(g_b)(rho S(a) S' dr + (1/2) d/(S(a) S')) + h~_b(S') ((7.20), S' = S(a(b) x a(V)),
h~_b : S_1 -> rho^3 C^oo linear and smooth in b); so Proposition 7.4's h-sharp_b,v1(w) is defined for every w in R^3 and
"the rho^2 leading-order term of h*_b,v1(V) ... crucially, only depends on V through a(V') = a(b) x a(V)" (p. 143).
dual5.py A3 has this in five dimensions at first order in one spin (10.31(c)).  Here the five-dimensional Myers-Perry
metric in Kerr-Schild form ([ER08]'s class (31); (42)-(44) its Boyer-Lindquist form) is written for every spin matrix A
in so(4) at once:

    g_A = eta + H k (x) k,   P = r^4 + s r^2 + p^2,   M = (r^2 + s) I + A^2,   s = -tr(A^2)/2,   p = Pf A,
    r > 0 the root of Q = P - x^T M x,   k = dt + (M (r I + A) x / P) . dx,
    H = mu r^2 / (P F),   F = 1 + x^T A^2 M^2 x / P^2

(M / P = (r^2 - A^2)^-1, A^4 + s A^2 + p^2 = 0); four dimensions, Kerr over so(3) (A x = a x x), is the control.

  M1 (computed, exact) The family.  A^4 + s A^2 + p^2 I = 0 and (r^2 I - A^2) M = P I identically, so k is null exactly
     where Q = 0; at A = a J_12 + b J_34, P is [ER08]'s Pi and F its F (44) with mu_i^2 = (x_(2i-1)^2 + x_(2i)^2)/(r^2 +
     a_i^2), so g_tt = -1 + mu r^2/(Pi F) is its (42)'s, and Q = 0 is sum mu_i^2 = 1; at A = 0 it is Tangherlini in
     ks5.py's ingoing Kerr-Schild form.  Ricci-flat exactly at rational points (r and x rational, the metric's jet to
     second order solved for exactly): two spins with A rotated out of block form by a Cayley rotation, equal spins, one
     spin; four dimensions likewise.  Control: H = mu r/(P F), the even-dimensional exponent, is not Ricci-flat.
  M2 (computed, exact) Lemma 7.5 at every spin.  Q, P and x^T A^2 M^2 x are invariant and M (r I + A) x covariant under
     so(4) acting on (x, A) at fixed r (symbolic in A, x, r, for each basis rotation), so for R = A_V x and W = [A,
     A_V]: delta*_(g_A) V_A = (1/2) L_R g_A = (1/2) D_A g_A(W), the derivative of the family along W -- checked directly
     on the full metric (r implicit) at the exact points of M1, all six basis rotations.  Four dimensions: [A_a, A_v] =
     A_(a x v), -A_(S') for his S' (A x = a x x is minus the spin, J = -m a; D98).  Control: the bracket reversed.
  M3 (computed, exact) The expansion.  Along x = X/eps (X = (1, 2, 2, 4), |X| = 5), D_A g(W) at A = 0 is exactly (2 mu /
     r^4) (dt + dr) (x)_s V(W) (V(W) = (W x) . dx, the eps^3 term alone), and at a two-spin A its eps^3 term is the same
     while eps^4, eps^5, eps^6 are nonzero: the leading term does not see the spin, and the rest is of class rho^4 with
     integer powers.  Four dimensions: (2 mu/r^3) (dt + dr) (x)_s V(W), mu = 2m, the rest at rho^3.  Control: the
     remainder claimed at rho^5.
  M4 (computed, exact) The Killing rotations.  dim ker ad_A = 6 at A = 0, 4 at a = +-b != 0, 2 otherwise (one spin
     included): L_R g_A = 0 exactly at the exact points for a basis of the kernel; four dimensions 3 and 1.  Control:
     equal spins claimed to leave 2.
  M5 (computed, exact) The leading term of h-sharp.  From the Kerr-Schild leading term (mu/r^4)(dt + dr) (x)_s V the
     correction of dual5.py A3 is c_0 + mu/3 (four dimensions c_0 + M) and the rho^3 (rho^2) leading term of h-sharp is
     the same as from (mu/r^4) dt (x)_s V: (mu/r^4) dr (x)_s V = delta*(-mu r^-3 V/3) on Tangherlini.  Control: c_0
     claimed unchanged.

Deduced, not computed here (N1STAR-PROOF.md 10.36): [Hin26] Lemma 7.5 in five dimensions at every spin, delta*_(g_b) V_b
= mu rho^3 (dt + dr) (x)_s rho V(W) + h~_b(W), W = [A_b, A_V], h~_b : so(4) -> rho^4 C^oo linear and smooth in b, no pure
gauge term at leading order in these coordinates; Proposition 7.4 with h-sharp_b,v1(W) for every W in so(4), its leading
term 10.31(c)'s, and (7.19) with rho^(floor(C_0) + 3), on 10.31(a)'s readings; the Killing rotations 6, 4, 2.

READ.  [Hin26] pp. 65 (Definition 2.28), 126 (Remark 6.17), 140-144 (section 7.2.1: (7.16), Proposition 7.4,
(7.17)-(7.19), Lemma 7.5 and its proof, (7.20)-(7.28), the proof of Proposition 7.4, (7.29)-(7.35)), 161 ((8.32c)-(8.33),
footnote 82); alphaXiv, 2026-10-24.  [ER08] (arXiv:0801.3471v2) pp. 10 ((14)-(16)), 14 ((31)-(34)), 16 ((42)-(44)), 19
(section 4.3).

sympy; imports dual5.py.  python3 mp5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import itertools
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

from damping5 import Checklist


# ------------------------------------------------------------------------------------------------- jets
class J:
    """a jet: a polynomial of degree <= 2 in displacement variables, keys () (i,) (i, j) with i <= j"""
    __slots__ = ("c",)

    def __init__(self, c):
        self.c = c

    @staticmethod
    def k(v):
        return J({(): Fr(v)})

    def __add__(self, o):
        o = o if isinstance(o, J) else J.k(o)
        d = dict(self.c)
        for kk, vv in o.c.items():
            d[kk] = d.get(kk, 0) + vv
        return J(d)
    __radd__ = __add__

    def __neg__(self):
        return J({kk: -vv for kk, vv in self.c.items()})

    def __sub__(self, o):
        return self + (-(o if isinstance(o, J) else J.k(o)))

    def __rsub__(self, o):
        return (-self) + o

    def __mul__(self, o):
        if not isinstance(o, J):
            o = Fr(o)
            return J({kk: vv * o for kk, vv in self.c.items()})
        d = {}
        for k1, v1 in self.c.items():
            for k2, v2 in o.c.items():
                kk = tuple(sorted(k1 + k2))
                if len(kk) <= 2:
                    d[kk] = d.get(kk, 0) + v1 * v2
        return J(d)
    __rmul__ = __mul__

    def inv(self):
        c0 = self.c.get((), 0)
        u = (self - c0) * (1 / c0)
        return (1 - u + u * u) * (1 / c0)

    def __truediv__(self, o):
        return self * (o.inv() if isinstance(o, J) else 1 / Fr(o))

    def __pow__(self, n):
        out = J.k(1)
        for _ in range(n):
            out = out * self
        return out

    def v(self):
        return self.c.get((), 0)


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), J.k(0)) for j in range(len(B[0]))] for i in range(len(A))]


def mv(A, x):
    return [sum((A[i][k] * x[k] for k in range(len(x))), J.k(0)) for i in range(len(A))]


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), J.k(0))


def pieces(x, A, R, n, Hmut=False):
    """the covariant Kerr-Schild data on jets: Q (its zero defines r), the spatial part of k, H / mu"""
    I = [[J.k(1 if i == j else 0) for j in range(n)] for i in range(n)]
    A2 = mm(A, A)
    s = sum((A2[i][i] for i in range(n)), J.k(0)) * Fr(-1, 2)
    RA = [[I[i][j] * R + A[i][j] for j in range(n)] for i in range(n)]
    if n == 4:
        p = A[0][1] * A[2][3] - A[0][2] * A[1][3] + A[0][3] * A[1][2]
        P = R**4 + s * R**2 + p * p
        M = [[I[i][j] * (R**2 + s) + A2[i][j] for j in range(n)] for i in range(n)]
        Q = P - dot(x, mv(M, x))
        ks = [q / P for q in mv(M, mv(RA, x))]
        F = 1 + dot(x, mv(A2, mv(M, mv(M, x)))) / (P * P)
        return Q, ks, (R if Hmut else R**2) / (P * F)
    B = [[-A2[i][j] for j in range(n)] for i in range(n)]
    xBx = dot(x, mv(B, x))
    Q = R**2 * (R**2 + s) - (R**2 + s) * dot(x, x) + xBx
    u = mv(RA, x)
    Bu = mv(B, u)
    ks = [(u[i] - Bu[i] / (R**2 + s)) / R**2 for i in range(n)]
    return Q, ks, (R**2 if Hmut else R**3) / (R**4 + s * dot(x, x) - xBx)


def metric_jet(x0, A, R0, n, mu, W=None, Hmut=False):
    """g = eta + mu H k k as jets in the displacements d_0, ..., d_(n-1) of x and, if W is given, d_n along A + d_n W"""
    x = [J({(): Fr(x0[i]), (i,): Fr(1)}) for i in range(n)]
    Aj = [[J.k(A[i][j]) + (J({(n,): Fr(W[i][j])}) if W else 0) for j in range(n)] for i in range(n)]
    xc, Ac = [J.k(q) for q in x0], [[J.k(q) for q in row] for row in A]
    assert pieces(xc, Ac, J.k(R0), n)[0].v() == 0                         # the point lies on Q = 0
    QR = pieces(xc, Ac, J.k(R0) + J({(n + 1,): Fr(1)}), n)[0].c.get((n + 1,), 0)
    R = J.k(R0)
    for _ in range(3):                                                     # r to second order, exactly
        R = R - pieces(x, Aj, R, n)[0] * (1 / QR)
    Q, ks, H = pieces(x, Aj, R, n, Hmut)
    k = [J.k(1)] + ks
    N = n + 1
    return [[J.k(-1 if i == j == 0 else (1 if i == j else 0)) + H * k[i] * k[j] * mu for j in range(N)]
            for i in range(N)]


def ricci_at(g, n):
    """the Ricci tensor at the point from the jet of a t-independent metric, exactly"""
    N = n + 1

    def d1(q, a):
        return Fr(0) if a == 0 else q.c.get((a - 1,), Fr(0))

    def d2(q, a, b):
        if a == 0 or b == 0:
            return Fr(0)
        i, j = sorted((a - 1, b - 1))
        return q.c.get((i, j), Fr(0)) * (2 if i == j else 1)
    g0 = sp.Matrix(N, N, lambda i, j: sp.Rational(g[int(i)][int(j)].v().numerator, g[int(i)][int(j)].v().denominator))
    G = g0.inv()
    gi = [[Fr(int(G[i, j].p), int(G[i, j].q)) for j in range(N)] for i in range(N)]
    dg = [[[d1(g[i][j], a) for j in range(N)] for i in range(N)] for a in range(N)]
    dgi = [[[-sum(gi[i][k] * dg[a][k][l] * gi[l][j] for k in range(N) for l in range(N)) for j in range(N)]
            for i in range(N)] for a in range(N)]
    low = [[[(dg[m][s][nn] + dg[nn][s][m] - dg[s][m][nn]) / 2 for nn in range(N)] for m in range(N)] for s in range(N)]
    Gam = [[[sum(gi[l][s] * low[s][m][nn] for s in range(N)) for nn in range(N)] for m in range(N)] for l in range(N)]
    dlow = [[[[(d2(g[s][nn], a, m) + d2(g[s][m], a, nn) - d2(g[m][nn], a, s)) / 2 for nn in range(N)] for m in range(N)]
             for s in range(N)] for a in range(N)]
    dGam = [[[[sum(dgi[a][l][s] * low[s][m][nn] + gi[l][s] * dlow[a][s][m][nn] for s in range(N)) for nn in range(N)]
              for m in range(N)] for l in range(N)] for a in range(N)]
    return [[sum(dGam[q][q][m][nn] - dGam[nn][q][m][q] for q in range(N))
             + sum(Gam[q][q][l] * Gam[l][m][nn] - Gam[q][nn][l] * Gam[l][m][q] for q in range(N) for l in range(N))
             for nn in range(N)] for m in range(N)]


def tofr(q):
    q = sp.Rational(q)
    return Fr(int(q.p), int(q.q))


def cayley(S):
    S = sp.Matrix(S)
    return (sp.eye(S.shape[0]) - S) * (sp.eye(S.shape[0]) + S).inv()


O5 = cayley([[0, sp.Rational(1, 2), sp.Rational(-1, 3), sp.Rational(1, 5)],
             [sp.Rational(-1, 2), 0, sp.Rational(2, 7), sp.Rational(-1, 4)],
             [sp.Rational(1, 3), sp.Rational(-2, 7), 0, sp.Rational(3, 11)],
             [sp.Rational(-1, 5), sp.Rational(1, 4), sp.Rational(-3, 11), 0]])
O3 = cayley([[0, sp.Rational(1, 2), sp.Rational(-1, 3)], [sp.Rational(-1, 2), 0, sp.Rational(2, 7)],
             [sp.Rational(1, 3), sp.Rational(-2, 7), 0]])
R0, MU = Fr(3, 2), Fr(7, 5)
SPINS5 = ((Fr(1, 3), Fr(1, 5)), (Fr(2, 7), Fr(2, 7)), (Fr(1, 2), Fr(0)))


def point(n, spins, O):
    """a rational point on Q = 0 at r = 3/2: x + i y = (r + i a_i) mu_i e^(i phi_i), then rotated with A by O"""
    if n == 4:
        (a, b), m1, m2 = spins, Fr(3, 5), Fr(4, 5)
        (c1, s1), (c2, s2) = (Fr(5, 13), Fr(12, 13)), (Fr(3, 5), Fr(4, 5))
        y = [m1 * (R0 * c1 - a * s1), m1 * (R0 * s1 + a * c1), m2 * (R0 * c2 - b * s2), m2 * (R0 * s2 + b * c2)]
        A0 = sp.zeros(4, 4)
        A0[0, 1], A0[1, 0], A0[2, 3], A0[3, 2] = -a, a, -b, b
    else:
        (a,), st, ct, (cp, sq) = spins, Fr(3, 5), Fr(4, 5), (Fr(5, 13), Fr(12, 13))
        y = [st * (R0 * cp - a * sq), st * (R0 * sq + a * cp), R0 * ct]
        A0 = sp.zeros(3, 3)
        A0[0, 1], A0[1, 0] = -a, a
    A = O * A0 * O.T
    x = O * sp.Matrix([sp.Rational(q.numerator, q.denominator) for q in y])
    return [tofr(q) for q in x], [[tofr(A[i, j]) for j in range(n)] for i in range(n)]


def basis_rot(n):
    out = []
    for i, j in itertools.combinations(range(n), 2):
        AV = [[Fr(0)] * n for _ in range(n)]
        AV[i][j], AV[j][i] = Fr(1), Fr(-1)
        out.append(AV)
    return out


def brack(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] - B[i][k] * A[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


# ------------------------------------------------------------------------------------------------- M1
def m1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    R, a, b = sp.symbols("R a b", positive=True)
    xs = sp.symbols("x1:5")
    x = sp.Matrix(xs)
    asy = sp.symbols("a12 a13 a14 a23 a24 a34")
    A = sp.zeros(4, 4)
    for (i, j), q in zip(itertools.combinations(range(4), 2), asy):
        A[i, j], A[j, i] = q, -q
    A2 = A * A
    s = -A2.trace() / 2
    p = A[0, 1] * A[2, 3] - A[0, 2] * A[1, 3] + A[0, 3] * A[1, 2]
    P = R**4 + s * R**2 + p**2
    M = (R**2 + s) * sp.eye(4) + A2
    ch = (A2 * A2 + s * A2 + p**2 * sp.eye(4)).applyfunc(sp.expand) == sp.zeros(4, 4)
    res = ((R**2 * sp.eye(4) - A2) * M - P * sp.eye(4)).applyfunc(sp.expand) == sp.zeros(4, 4)
    # k null: |M (R + A) x|^2 / P^2 = x^T M x / P, by (R - A) M M (R + A) = (R^2 - A^2) M M = P M
    nul = sp.expand(((x.T * (R * sp.eye(4) - A) * M * M * (R * sp.eye(4) + A) * x)[0]) - P * (x.T * M * x)[0]) == 0
    chk("A^4 + s A^2 + p^2 = 0, (r^2 - A^2) M = P, and |k_spatial|^2 = x^T M x / P: k null exactly on Q = 0", ch and res
        and nul)
    Ac = sp.zeros(4, 4)
    Ac[0, 1], Ac[1, 0], Ac[2, 3], Ac[3, 2] = -a, a, -b, b
    sub = {q: Ac[i, j] for (i, j), q in zip(itertools.combinations(range(4), 2), asy)}
    Pc, Mc = P.subs(sub), M.subs(sub)
    m1s, m2s = (xs[0]**2 + xs[1]**2) / (R**2 + a**2), (xs[2]**2 + xs[3]**2) / (R**2 + b**2)
    Fc = 1 + (x.T * Ac * Ac * Mc * Mc * x)[0] / Pc**2
    er = sp.expand(Pc - (R**2 + a**2) * (R**2 + b**2)) == 0
    er &= sp.simplify(Fc - (1 - a**2 * m1s / (R**2 + a**2) - b**2 * m2s / (R**2 + b**2))) == 0
    er &= sp.simplify((Pc - (x.T * Mc * x)[0]) / Pc - (1 - m1s - m2s)) == 0
    chk("at A = a J_12 + b J_34: P = Pi, F = [ER08]'s F (44), g_tt = -1 + mu r^2/(Pi F) its (42)'s, Q = 0 iff sum "
        "mu_i^2 = 1", er)
    ok0 = True
    zA = [[Fr(0)] * 4 for _ in range(4)]
    xz = [q * Fr(15, 7) for q in (Fr(1, 3), Fr(2, 3), Fr(2, 3), Fr(0))]                # |x| = 15/7 rational
    gz = metric_jet(xz, zA, Fr(15, 7), 4, MU)
    rz = Fr(15, 7)
    for i in range(5):
        for j in range(5):
            ki = 1 if i == 0 else xz[i - 1] / rz
            kj = 1 if j == 0 else xz[j - 1] / rz
            want = (-1 if i == j == 0 else (1 if i == j else 0)) + MU / rz**2 * ki * kj
            ok0 &= gz[i][j].v() == want
    chk("at A = 0: g = eta + (mu/r^2)(dt + dr)^2, Tangherlini in ks5.py's ingoing Kerr-Schild form", ok0)
    flat = []
    for spins in SPINS5:
        x0, Ab = point(4, spins, O5)
        Ric = ricci_at(metric_jet(x0, Ab, R0, 4, MU, Hmut=control == 1), 4)
        flat.append(all(q == 0 for row in Ric for q in row))
    blocky = all(q != 0 for q in (point(4, SPINS5[0], O5)[1][0][2], point(4, SPINS5[0], O5)[1][1][3]))
    chk(f"Ricci-flat exactly at r = 3/2, mu = 7/5: two spins (1/3, 1/5) rotated out of block form, equal (2/7, 2/7), "
        f"one (1/2, 0): {flat}{' (control: H = mu r/(P F))' if control == 1 else ''}", all(flat) and blocky)
    x0, Ab = point(3, (Fr(1, 3),), O3)
    Ric = ricci_at(metric_jet(x0, Ab, R0, 3, MU, Hmut=control == 1), 3)
    chk("four dimensions: Kerr over so(3) (H = mu r^3/(r^4 + (a . x)^2)) Ricci-flat at its exact point",
        all(q == 0 for row in Ric for q in row))
    return chk.ok


# ------------------------------------------------------------------------------------------------- M2
def blocks(n):
    xs = sp.symbols(f"x1:{n + 1}")
    R = sp.Symbol("R")
    pairs = list(itertools.combinations(range(n), 2))
    asy = sp.symbols(" ".join(f"a{i + 1}{j + 1}" for i, j in pairs))
    A = sp.zeros(n, n)
    for (i, j), q in zip(pairs, asy):
        A[i, j], A[j, i] = q, -q
    x = sp.Matrix(xs)
    I = sp.eye(n)
    A2 = A * A
    s = -A2.trace() / 2
    if n == 4:
        p = A[0, 1] * A[2, 3] - A[0, 2] * A[1, 3] + A[0, 3] * A[1, 2]
        P = R**4 + s * R**2 + p**2
        M = (R**2 + s) * I + A2
        inv = [P - (x.T * M * x)[0], P, (x.T * A2 * M * M * x)[0]]
        cov = list(M * (R * I + A) * x)
    else:
        B = -A2
        xx, xBx = (x.T * x)[0], (x.T * B * x)[0]
        inv = [R**2 * (R**2 + s) - (R**2 + s) * xx + xBx, R**4 + s * xx - xBx, s]
        u = (R * I + A) * x
        cov = list((R**2 + s) * u - B * u)
    return [sp.expand(q) for q in inv], [sp.expand(q) for q in cov], xs, pairs, asy, A, x


def equivariant(n, sign):
    inv, cov, xs, pairs, asy, A, x = blocks(n)
    ok = True
    for (i0, j0) in pairs:
        AV = sp.zeros(n, n)
        AV[i0, j0], AV[j0, i0] = 1, -1
        Rv = AV * x
        C = sign * (AV * A - A * AV)                                       # [A_V, A]

        def dA(f):
            return sum(C[i, j] * sp.diff(f, q) for (i, j), q in zip(pairs, asy))
        for f in inv:
            ok &= sp.expand(sum(Rv[i] * sp.diff(f, xs[i]) for i in range(n)) + dA(f)) == 0
        for i in range(n):
            ok &= sp.expand(sum(Rv[j] * sp.diff(cov[i], xs[j]) for j in range(n))
                            + sum(cov[j] * AV[j, i] for j in range(n)) + dA(cov[i])) == 0
    return ok


def lie_vs_dA(x0, A, n, AV, sign=1):
    """(L_R g)(point) against D_A g([A, A_V]) (sign -1: the bracket reversed); also whether L_R g is nonzero"""
    N = n + 1
    W = brack(A, AV)
    W = [[sign * q for q in row] for row in W]
    g = metric_jet(x0, A, R0, n, MU, W=W)
    Rv = [Fr(0)] + [sum(AV[i][j] * x0[j] for j in range(n)) for i in range(n)]
    dR = [[Fr(0)] * N] + [[Fr(0)] + [AV[i][j] for j in range(n)] for i in range(n)]
    d = lambda q, a: Fr(0) if a == 0 else q.c.get((a - 1,), Fr(0))
    LR = [[sum(Rv[a] * d(g[m][nn], a) + g[a][nn].v() * dR[a][m] + g[m][a].v() * dR[a][nn] for a in range(N))
           for nn in range(N)] for m in range(N)]
    DA = [[g[m][nn].c.get((n,), Fr(0)) for nn in range(N)] for m in range(N)]
    return all(LR[m][nn] == DA[m][nn] for m in range(N) for nn in range(N)), any(q != 0 for row in LR for q in row)


def m2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    sign = -1 if control == 1 else 1
    for n in (4, 3):
        chk(f"n + 1 = {n + 1}: Q, P, x^T A^2 M^2 x (four dimensions Q, r^4 + (a . x)^2, |a|^2) invariant and M (r + A) "
            f"x (four dimensions (r^2 + |a|^2) u - B u) covariant under so({n}) on (x, A), fixed r: symbolic, each "
            f"basis rotation", equivariant(n, sign))
    res = []
    for spins in SPINS5:
        x0, Ab = point(4, spins, O5)
        res.append(all(e and nz for e, nz in (lie_vs_dA(x0, Ab, 4, AV, sign) for AV in basis_rot(4))))
    chk(f"on the full metric (r implicit) at the exact points: (1/2) L_R g = (1/2) D_A g([A, A_V]) for all six basis "
        f"rotations, none Killing there: {res}", all(res))
    x0, Ab = point(3, (Fr(1, 3),), O3)
    r4 = all(e and nz for e, nz in (lie_vs_dA(x0, Ab, 3, AV, sign) for AV in basis_rot(3)))
    chk("four dimensions, Kerr: the same with [A_a, A_v] = A_(a x v), -A_(S') for his S'", r4)
    return chk.ok


# ------------------------------------------------------------------------------------------------- M3
EPS, SIG, MUS = sp.symbols("eps sigma mu", positive=True)


def dA_series(Ab, W, X, n, order):
    """D_A g(W) along x = X/eps, as series in eps to eps^order (exact A, W, X)"""
    A = sp.Matrix(Ab) + SIG * sp.Matrix(W)
    x = sp.Matrix(X) / EPS
    I = sp.eye(n)
    A2 = A * A
    s = -A2.trace() / 2
    xx = (x.T * x)[0]
    if n == 4:
        p = A[0, 1] * A[2, 3] - A[0, 2] * A[1, 3] + A[0, 3] * A[1, 2]
        c = s * xx + (x.T * A2 * x)[0] - p**2
        R = sp.sqrt((xx - s + sp.sqrt((xx - s)**2 + 4 * c)) / 2)          # Q = r^4 + (s - |x|^2) r^2 - c
        P = R**4 + s * R**2 + p**2
        M = (R**2 + s) * I + A2
        ks = (M * (R * I + A) * x) / P
        H = MUS * R**2 / (P * (1 + (x.T * A2 * M * M * x)[0] / P**2))
    else:
        B = -A2
        xBx = (x.T * B * x)[0]
        R = sp.sqrt((xx - s + sp.sqrt((xx - s)**2 + 4 * (s * xx - xBx))) / 2)
        u = (R * I + A) * x
        ks = (u - B * u / (R**2 + s)) / R**2
        H = MUS * R**3 / (R**4 + s * xx - xBx)
    k = [1] + list(ks)
    N = n + 1
    out = sp.zeros(N, N)
    for i in range(N):
        for j in range(i, N):
            q = sp.diff(H * k[i] * k[j], SIG).subs(SIG, 0)
            out[i, j] = out[j, i] = sp.expand(sp.series(q, EPS, 0, order + 1).removeO())
    return out


def m3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n, X, W, Ab, lo in ((4, [1, 2, 2, 4], [[0, 1, -2, 3], [-1, 0, 5, -1], [2, -5, 0, 2], [-3, 1, -2, 0]],
                             [[0, -sp.Rational(1, 3), 0, 0], [sp.Rational(1, 3), 0, 0, 0], [0, 0, 0, -sp.Rational(1, 5)],
                              [0, 0, sp.Rational(1, 5), 0]], 3),
                            (3, [2, 3, 6], [[0, 1, -2], [-1, 0, 5], [2, -5, 0]],
                             [[0, -sp.Rational(1, 3), 0], [sp.Rational(1, 3), 0, 0], [0, 0, 0]], 2)):
        N = n + 1
        nx = sp.sqrt(sum(q * q for q in X))
        k0 = [1] + [q / nx for q in X]
        WX = [0] + list(sp.Matrix(W) * sp.Matrix(X))
        lead = sp.Matrix(N, N, lambda i, j: MUS / nx**(n) * (k0[int(i)] * WX[int(j)] + k0[int(j)] * WX[int(i)]))
        top = lo + 3
        D0 = dA_series(sp.zeros(n, n), W, X, n, top)
        D1 = dA_series(Ab, W, X, n, top)
        c0 = {kk: D0.applyfunc(lambda q: q.coeff(EPS, kk)) for kk in range(top + 1)}
        c1 = {kk: D1.applyfunc(lambda q: q.coeff(EPS, kk)) for kk in range(top + 1)}
        z = sp.zeros(N, N)
        a0 = all(c0[kk] == (lead if kk == lo else z) for kk in c0)
        a1 = all(c1[kk] == z for kk in range(lo)) and (c1[lo] - lead).applyfunc(sp.simplify) == z
        rest = [c1[kk] != z for kk in range(lo + 1, top + 1)]
        if control == 1:
            rest[0] = c1[lo + 1] == z
        chk(f"n + 1 = {N}: along x = X/eps (|X| = {nx}), D_A g(W) at A = 0 is exactly (2 mu/r^{n}) (dt + dr) (x)_s V(W) "
            f"(eps^{lo} alone); at a spinning A the same eps^{lo} term and eps^{lo + 1}..eps^{top} nonzero: {rest}"
            f"{' (control: the remainder claimed at rho^' + str(lo + 2) + ')' if control == 1 else ''}",
            a0 and a1 and all(rest))
    return chk.ok


# ------------------------------------------------------------------------------------------------- M4
def m4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    a, b = sp.symbols("a b", positive=True)

    def kernel_dim(Ac, n):
        cols = []
        for i, j in itertools.combinations(range(n), 2):
            E = sp.zeros(n, n)
            E[i, j], E[j, i] = 1, -1
            C = Ac * E - E * Ac
            cols.append([C[p, q] for p, q in itertools.combinations(range(n), 2)])
        return len(cols) - sp.Matrix(cols).T.rank()

    def canon(a_, b_):
        Ac = sp.zeros(4, 4)
        Ac[0, 1], Ac[1, 0], Ac[2, 3], Ac[3, 2] = -a_, a_, -b_, b_
        return Ac
    cases = [("A = 0", canon(0, 0), 6), ("a = b", canon(a, a), 4 if control != 1 else 2), ("a = -b", canon(a, -a), 4),
             ("a != +-b, both nonzero", canon(sp.Rational(1, 3), sp.Rational(1, 5)), 2), ("one spin", canon(a, 0), 2)]
    dims = [(name, kernel_dim(Ac, 4)) for name, Ac, _ in cases]
    chk(f"dim ker ad_A in so(4): {dims}", all(d == w for (_, d), (_, _, w) in zip(dims, cases)))
    # on the full metric: L_R g = 0 for a basis of the kernel (canonical frame, the points of M1 unrotated)
    ok = True
    for spins in SPINS5:
        x0, Ab = point(4, spins, sp.eye(4))
        Abs = sp.Matrix([[sp.Rational(q.numerator, q.denominator) for q in row] for row in Ab])
        ns, cols = [], []
        for i, j in itertools.combinations(range(4), 2):
            E = sp.zeros(4, 4)
            E[i, j], E[j, i] = 1, -1
            C = Abs * E - E * Abs
            cols.append([C[p, q] for p, q in itertools.combinations(range(4), 2)])
        ker = sp.Matrix(cols).T.nullspace()
        for v in ker:
            AV = [[Fr(0)] * 4 for _ in range(4)]
            for (i, j), c in zip(itertools.combinations(range(4), 2), v):
                AV[i][j], AV[j][i] = tofr(c), -tofr(c)
            e, nz = lie_vs_dA(x0, Ab, 4, AV)
            ns.append(e and not nz)
        ok &= all(ns) and len(ns) == (4 if spins[0] == spins[1] else 2)
    chk("on the full metric at the points of M1 (unrotated): L_R g = 0 exactly for a basis of the kernel (4 at equal "
        "spins, 2 otherwise)", ok)
    A3 = sp.Matrix([[0, -a, 0], [a, 0, 0], [0, 0, 0]])
    d3 = [kernel_dim(sp.zeros(3, 3), 3), kernel_dim(A3, 3)]
    chk(f"four dimensions: dim ker ad_a = {d3} (3 at a = 0, 1 otherwise)", d3 == [3, 1])
    return chk.ok


# ------------------------------------------------------------------------------------------------- M5
def m5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    from dual5 import geo, rot1, Cstar, boxCs, div, Gop, dstar, frame2, frame1, ser, at, TRIG2, mu, r, rho, M

    def sharp(n, lead):
        X, gT, gTi, GamT, fT = geo(n, False)
        G = (X, gT, gTi, GamT, fT)
        N = len(X)
        V = rot1(n, X, 1, 2)
        cm, nn = (mu, 4) if n == 4 else (2 * M, 3)
        one = [1] + [0] * (N - 1) if lead == "t" else [1, 1] + [0] * (N - 2)
        hV = sp.Matrix(N, N, lambda i, j: (cm / r**nn) * (one[int(i)] * V[int(j)] + V[int(i)] * one[int(j)]) / 2)
        q = 3 if n == 4 else 2
        c0 = sp.Symbol("c0")
        om = [c0 * r**(-q) * x for x in V]
        f1 = [2 * (x + y) for x, y in zip(div(Gop(hV, G), G), Cstar(Gop(hV, G), G))]
        F = [ser(x, q + 1) for x in frame1([u + s for u, s in zip(f1, boxCs(om, G))])]
        low = all(sp.simplify(x.coeff(rho, j)) == 0 for x in F for j in range(q + 1))
        eqs = [e for e in (sp.expand(at(x.coeff(rho, q + 1))) for x in F) if e != 0]
        sol = sp.solve(eqs, [c0], dict=True)
        if len(sol) != 1:
            return None, None, False
        two = all(sp.simplify(sp.expand(at(x.coeff(rho, q + 1), TRIG2)).subs(sol[0])) == 0 for x in F)
        hs = Gop(hV, G) + Gop(dstar([sp.sympify(x).subs(sol[0]) for x in om], G), G)
        hS = frame2(hs).applyfunc(lambda x: ser(x, q))
        lowS = all(sp.simplify(hS[i, j].coeff(rho, s)) == 0 for i in range(N) for j in range(N) for s in range(q))
        return sp.factor(sol[0][c0]), hS.applyfunc(lambda x: sp.simplify(x.coeff(rho, q))), low and two and lowS
    for n, shift in ((4, mu / 3), (3, M)):
        cT, LT, okT = sharp(n, "t")
        cK, LK, okK = sharp(n, "ks")
        sh = 0 if control == 1 else shift
        good = okT and okK and sp.simplify(cK - cT - sh) == 0
        good &= (LT - LK).applyfunc(sp.simplify) == sp.zeros(*LT.shape)
        chk(f"n + 1 = {n + 1}: from (cm/r^{n})(dt + dr) (x)_s V the correction is c_0 = {cK}, from (cm/r^{n}) dt (x)_s "
            f"V {cT} (the difference {sp.factor(cK - cT)}), and the leading term of h-sharp, at rho^{n - 1}, is the "
            f"same",
            good)
    return chk.ok


CHECKS = [("M1 the Myers-Perry family over so(4), Kerr-Schild: [ER08]'s at block form, Ricci-flat at exact points",
           m1, 1),
          ("M2 Lemma 7.5 at every spin: delta* V_b = (1/2) L_R g = (1/2) D_A g([A, A_V]); four dimensions -A_(S')",
           m2, 1),
          ("M3 the expansion: the leading term (mu/r^4)(dt + dr) (x)_s V(W) does not see the spin; the rest at rho^4",
           m3, 1),
          ("M4 the Killing rotations: dim ker ad_A = 6, 4 (a = +-b != 0), 2; four dimensions 3, 1", m4, 1),
          ("M5 h-sharp's leading term from the Kerr-Schild term: dual5.py A3's, c_0 shifted by the pure gauge mu/3", m5,
           1)]


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
    print(f"mp5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"mp5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    if "--only" in args:
        k = int(args[args.index("--only") + 1])
        name, fn, _ = CHECKS[k - 1]
        print(name, fn(verbose=True))
        sys.exit(0)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
