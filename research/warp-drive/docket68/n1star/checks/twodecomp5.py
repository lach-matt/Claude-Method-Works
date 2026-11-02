#!/usr/bin/env python3
"""twodecomp5: the identities behind Lemmas 3.2_2 and 3.3_2 and the equation (3.5_2) for h (FAMILIES5-FULL.md section 8).

The two-family decomposition w = h + phi_in Y_in + phi_out Y_out (Y_k = F_k g1^(k) + lam F_k ghat_2) rests on the
structure of the linearisation P of Ric^H at g_app on a slow h and on a slow function phi times a fast profile Y. This
program computes that structure from the full reduced Ricci tensor, not from its principal part: Ric^H(g) = Ric(g) -
(1/2)(g D^ D + (g D^ D)^T), D^rho = g^ab (Gamma[g] - Gamma[g0])^rho_ab, D^ the covariant derivative of g0 (stage0two5's
form). The background is the general round double-null metric g0 = -2 e^(2 sig) du dv + R^2 (dth^2 + c^2 dp1^2 + s^2
dp2^2) (sig, R arbitrary functions of (u, v)), with both families' stage-0 waves: W_in = TT(A_in) z1 + chi_in z1^2 dv^2
and W_out = TT(A_out) z2 + chi_out z2^2 du^2, TT the traceless angular tensor of stage0two5 (amplitudes A arbitrary
functions of (u, v, th)), and a mixed second-order profile lam^2 Q z1 z2 (all fifteen components arbitrary).

Method: exact rational arithmetic at one point p (cos th = 3/5). Every free function is replaced by its second-order
Taylor jet at p with random rational coefficients; Ric^H takes at most two derivatives, so the jets give its exact value
at p. The fast phases are carried as z1 = e^(s1), z2 = e^(s2) with F_k = z_k d/dz_k (a derivation: every identity
tested is algebraic in F_k, so the factor i of e^(i s) changes nothing), d_v -> d_v + lam^-1 F_1, d_u -> d_u + lam^-1
F_2. The linearisation is taken in several directions eps_1..eps_m at once (eps_i eps_j = 0). Notation: ell_in := g0^-1
dv, ell_out := g0^-1 du, s_k(h) := h(ell_k, ell_k), e^(2 sig) =: E.

  J1 (exact) no lam^-2 coefficient: P(h) for h slow, and the commutator [P, phi] Y_k = P(phi Y_k) - phi P(Y_k) (computed
     with phi(p) = 0, so P(phi Y_k)(p) is the commutator at p), have no lam^-2 term in any component.
  J5 (exact) the lam^-1 coefficient of P(h), h slow (all fifteen components, value and derivatives arbitrary), is
     (1/2) (s_in(h) F1^2 W_in + s_out(h) F2^2 W_out): twolin5's L1, now with h a function and not a constant.
  J2 (exact) the lam^-1 coefficient of [P, phi] Y_k (phi slow, Y_k = F_k W_k) is -(ell_k . d phi) F_k Y_k = -(ell_k . d
     phi) G2^k, in every component: the record's cross term, once per family, with no term in the other family's
     generator.
  J3 (exact) with phi(p) = d phi(p) = 0, the whole linearisation at p is -(1/2) (g_app^ab d_a d_b phi) Y_k; at order lam^0
     -(1/2) (g0^ab d_a d_b phi) Y_k: second derivatives of phi enter only through box phi, multiplying Y_k (Lemma 3.2_2).
  J4 (exact) contractions: G1^in(ell_in, .) = G2^in(ell_in, .) = 0 and G1^out(ell_out, .) = G2^out(ell_out, .) = 0 in
     every component; G1^out(ell_in, ell_in) = E^-2 F2 chi_out z2^2 =: c_in and G2^out(ell_in, ell_in) = E^-2 F2^2 (chi_out
     z2^2), and the mirror ones (twophase5 Q2 recomputed); ell_app^in - ell_in = lam E^-1 chi_out z2^2 ell_out + O(lam^2)
     and g_app^-1(dv, dv) = -lam E^-2 chi_out z2^2 + O(lam^2) (the record's n1, FAMILIES5 4g), and mirror.
  J6 (exact; Lemma 3.3_2's content) the ell_in x ell_in contraction of J3's lam^0 term is -(1/2) (box phi_out) c_in:
     phi_in drops out exactly and phi_out survives only through box phi_out, with the bounded coefficient c_in (no
     lam^-1); and the mirror for ell_out x ell_out.
  J7 (exact; (3.5_2)'s lam^-1 part) with dphi_k(p) chosen by the transport ell_k . d phi_k = (1/2)(s_k(h) - rho_k), rho_k
     arbitrary (standing for (1 - P) s_k(h)), the lam^-1 coefficient of P(h) + sum_k [P, phi_k] Y_k is (1/2) sum_k rho_k
     G2^k exactly: the record's one remaining 1/lam coefficient, once per family; its ell_in x ell_in contraction is
     (1/2) rho_out G2^out(ell_in, ell_in).
  J0 (exact; the identity behind Lemma 3.1_2) for G = g0 + lam W + lam^2 Q, D Ric^H[G](F_k G) = F_k (Ric^H[G]) at orders
     lam^-2, lam^-1, lam^0, for k = in and out: a constant shift of either phase is a symmetry of the two-scale operator.
     With (E2) (stage 0 solved: R^(-1) = R^(0) = 0, stage0two5 T1-T4) it gives T(F_k g1^(k)) + P_(-2)(F_k ghat_2) = O(lam),
     so P(Y_k) = O(1).

  Controls (each must fail): (a) plain Ric in place of Ric^H (the gauge term dropped): J2, J3 and J5 fail; (b) the
     direction lam F_k W without lam^2 F_k Q: J0 fails at lam^0 (P_(-2)(F_k Q) is missing: lam F_k ghat_2 has to be in
     Y_k); (c) phi_in transported along the other generator (ell_out . d phi_in = (1/2)(s_in - rho_in)): J7 leaves a
     lam^-1 term; (d) a trace on the spheres of the outgoing wave: J4's own-family contraction G1^out(ell_out, .) = 0 still
     holds but tracelessness, which J3's coefficient does not need, is not what is tested -- so instead (d) is: chi_out
     placed on du dv in place of du du: G1^out(ell_out, .) = 0 fails.

Labels: computed (exact rational arithmetic at a random point; the identities are polynomial in the jets, so agreement at
a random rational point is evidence, and J1-J7 and J0 hold at all three points tried). Run: python3 checks/twodecomp5.py
(about ten minutes).
"""
import random
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

N = 5
LCAP = 2                      # intermediate truncation of lam powers (later factors bring at most lam^-2)
U, V, TH = 0, 1, 2            # index of u, v, th; p1, p2 = 3, 4 carry no derivatives (T^2-invariant fields)


# ------------------------------------------------------------------ sparse Laurent polynomials in (z1, z2, lam)
# a poly is a dict {(n1, n2, l): Fraction}; a Lin is a list of polys, slot 0 the eps^0 part, slot i the eps_i part

def padd(a, b, s=1):
    out = dict(a)
    for k, c in b.items():
        x = out.get(k, 0) + s * c
        if x:
            out[k] = x
        else:
            out.pop(k, None)
    return out


def pscale(a, c):
    return {k: v * c for k, v in a.items()} if c else {}


def pmul(a, b, cap=LCAP):
    if not a or not b:
        return {}
    if len(a) == 1 and (0, 0, 0) in a:
        return pscale(b, a[(0, 0, 0)])
    if len(b) == 1 and (0, 0, 0) in b:
        return pscale(a, b[(0, 0, 0)])
    out = {}
    for (i1, i2, il), x in a.items():
        for (j1, j2, jl), y in b.items():
            l = il + jl
            if l > cap:
                continue
            k = (i1 + j1, i2 + j2, l)
            out[k] = out.get(k, 0) + x * y
    return {k: v for k, v in out.items() if v}


def pfast(a, k):
    """F_k = z_k d/dz_k, k = 1 or 2"""
    return {key: c * key[k - 1] for key, c in a.items() if key[k - 1]}


def pshift(a, e):
    return {(k[0], k[1], k[2] + e): c for k, c in a.items()}


class Lin:
    __slots__ = ("s",)

    def __init__(self, slots):
        self.s = slots

    @staticmethod
    def zero(m):
        return Lin([{} for _ in range(m + 1)])

    def __add__(self, o):
        return Lin([padd(a, b) for a, b in zip(self.s, o.s)])

    def __sub__(self, o):
        return Lin([padd(a, b, -1) for a, b in zip(self.s, o.s)])

    def __neg__(self):
        return Lin([pscale(a, -1) for a in self.s])

    def scale(self, c):
        return Lin([pscale(a, c) for a in self.s])

    def mul(self, o, cap=LCAP):
        a0, b0 = self.s[0], o.s[0]
        out = [pmul(a0, b0, cap)]
        for ai, bi in zip(self.s[1:], o.s[1:]):
            out.append(padd(pmul(a0, bi, cap), pmul(ai, b0, cap)))
        return Lin(out)

    def fast(self, k):
        return Lin([pfast(a, k) for a in self.s])

    def shift(self, e):
        return Lin([pshift(a, e) for a in self.s])

    def iszero(self):
        return all(not a for a in self.s)


def const(x, m):
    x = Fr(x)
    return Lin([{(0, 0, 0): x} if x else {}] + [{} for _ in range(m)])


def lsum(items, m):
    out = Lin.zero(m)
    for x in items:
        out = out + x
    return out


# ------------------------------------------------------------------ the point, the jets, the metric

def rq(rng, lo=-4, hi=4, den=4):
    return Fr(rng.randint(lo, hi), rng.randint(1, den))


def jet(rng, vars_, const=None, lin=True, quad=True):
    """a random second-order Taylor polynomial in the offsets vars_"""
    e = const if const is not None else rq(rng)
    if lin:
        e += sum(rq(rng) * x for x in vars_)
    if quad:
        for i, x in enumerate(vars_):
            for y in vars_[i:]:
                e += rq(rng) * x * y
    return e


TU, TV, TT = sp.symbols("tu tv tt")
Z1, Z2, LAM = sp.symbols("z1 z2 lam")
EPS = sp.symbols("e1:9")
TVARS = (TU, TV, TT)


def build(seed, control=None):
    """the metric G + sum_i eps_i V_i as sympy polynomials in (tu, tv, tt, z1, z2, lam, eps), and the data used in the
    predictions. control: 'chi_dudv' puts chi_out on du dv"""
    rng = random.Random(seed)
    c0, s0 = Fr(3, 5), Fr(4, 5)
    cth = c0 - s0 * TT - c0 * TT**2 / 2                                      # cos(th0 + tt) to second order
    sth = s0 + c0 * TT - s0 * TT**2 / 2
    E = jet(rng, (TU, TV), const=Fr(rng.randint(2, 5), rng.randint(1, 3)))  # e^(2 sig)
    R = jet(rng, (TU, TV), const=Fr(rng.randint(3, 6), rng.randint(1, 3)))
    kap = Fr(1, 2)
    q1 = (2 * cth**2 - kap * sth**2) / 3
    q2 = (2 * kap * sth**2 - cth**2) / 3

    def tt(amp):
        T = sp.zeros(N)
        T[2, 2], T[3, 3], T[4, 4] = -2 * R**2 * (q1 + q2) * amp, 2 * R**2 * cth**2 * q1 * amp, 2 * R**2 * sth**2 * q2 * amp
        return T
    g0 = sp.zeros(N)
    g0[U, V] = g0[V, U] = -E
    g0[2, 2], g0[3, 3], g0[4, 4] = R**2, R**2 * cth**2, R**2 * sth**2
    Ain, Aout = jet(rng, TVARS), jet(rng, TVARS)
    chin, chout = jet(rng, TVARS), jet(rng, TVARS)
    Win = tt(Ain) * Z1
    Win[V, V] += chin * Z1**2
    Wout = tt(Aout) * Z2
    if control == "chi_dudv":
        Wout[U, V] += chout * Z2**2
        Wout[V, U] += chout * Z2**2
    else:
        Wout[U, U] += chout * Z2**2
    Q = sp.zeros(N)
    for a in range(N):
        for b in range(a, N):
            Q[a, b] = Q[b, a] = jet(rng, TVARS) * Z1 * Z2
    h = sp.zeros(N)
    for a in range(N):
        for b in range(a, N):
            h[a, b] = h[b, a] = jet(rng, TVARS)

    def F(M, k):
        z = Z1 if k == 1 else Z2
        return M.applyfunc(lambda x: sp.expand(z * sp.diff(x, z)))
    Yin, Yout = F(Win, 1), F(Wout, 2)
    Ep, Rp = E.subs({TU: 0, TV: 0}), R.subs({TU: 0, TV: 0})
    hp = h.applyfunc(lambda x: x.subs({TU: 0, TV: 0, TT: 0}))
    s_in, s_out = hp[U, U] / Ep**2, hp[V, V] / Ep**2                        # h(ell_in, ell_in), h(ell_out, ell_out)
    rho_in, rho_out = rq(rng), rq(rng)
    # phi's first derivatives at p, phi(p) = 0: ell_in . d phi = -d_u phi / E, ell_out . d phi = -d_v phi / E
    lin_in = [rq(rng) for _ in range(3)]
    lin_out = [rq(rng) for _ in range(3)]
    lin_in[U] = -Ep * (s_in - rho_in) / 2                                    # ell_in . d phi_in = (1/2)(s_in - rho_in)
    lin_out[V] = -Ep * (s_out - rho_out) / 2
    lin_wrong = [rq(rng) for _ in range(3)]
    lin_wrong[V] = -Ep * (s_in - rho_in) / 2                                 # control (c): along ell_out
    phin = sum(c * x for c, x in zip(lin_in, TVARS))
    phout = sum(c * x for c, x in zip(lin_out, TVARS))
    phwrong = sum(c * x for c, x in zip(lin_wrong, TVARS))
    qin = jet(rng, TVARS, const=0, lin=False)
    qout = jet(rng, TVARS, const=0, lin=False)
    G = g0 + LAM * (Win + Wout) + LAM**2 * Q
    dirs = [h,                                                               # e1: J5
            Yin * phin,                                                      # e2: J2, J7
            Yout * phout,                                                    # e3: J2, J7
            Yin * qin + Yout * qout,                                         # e4: J3, J6
            LAM * F(Win + Wout, 1) + LAM**2 * F(Q, 1),                       # e5: J0, in
            LAM * F(Win + Wout, 2) + LAM**2 * F(Q, 2),                       # e6: J0, out
            LAM * F(Win + Wout, 1),                                          # e7: control (b)
            Yin * phwrong]                                                   # e8: control (c)
    g = G + sum((EPS[i] * dirs[i] for i in range(len(dirs))), sp.zeros(N))
    info = dict(Ep=Ep, Rp=Rp, s_in=s_in, s_out=s_out, rho_in=rho_in, rho_out=rho_out, lin_in=lin_in, lin_out=lin_out,
                lin_wrong=lin_wrong, qin=qin, qout=qout, Yin=Yin, Yout=Yout, Win=Win, Wout=Wout, g0=g0, m=len(dirs),
                chout=chout, chin=chin)
    return g, info


def tojet(expr, m):
    """sympy polynomial -> value, slow gradient, slow Hessian at p, each a Lin"""
    e = sp.expand(expr)
    P = sp.Poly(e, TU, TV, TT, Z1, Z2, LAM, *EPS[:m])
    val = [Lin.zero(m) for _ in range(1)][0]
    grad = [Lin.zero(m) for _ in range(3)]
    hess = [[Lin.zero(m) for _ in range(3)] for _ in range(3)]
    for mon, c in P.terms():
        tpow, (n1, n2, l), ep = mon[:3], mon[3:6], mon[6:]
        if sum(tpow) > 2 or sum(ep) > 1:
            continue
        slot = 0 if sum(ep) == 0 else 1 + ep.index(1)
        c = Fr(int(c.p), int(c.q))
        key = (n1, n2, l)
        if sum(tpow) == 0:
            tgt = val
        elif sum(tpow) == 1:
            tgt = grad[tpow.index(1)]
        else:
            if 2 in tpow:
                i = tpow.index(2)
                tgt, c = hess[i][i], 2 * c
            else:
                i, j = [x for x in range(3) if tpow[x] == 1]
                tgt = hess[i][j]
                hess[j][i].s[slot][key] = hess[j][i].s[slot].get(key, 0) + c
        tgt.s[slot][key] = tgt.s[slot].get(key, 0) + c
    return val, grad, hess


FASTK = {U: 2, V: 1}                                                         # d_u carries F_2, d_v carries F_1


def two_scale(val, grad, hess, m):
    """d_c f and d_c d_d f at p for c, d in 0..4: slow + lam^-1 F + lam^-2 F F"""
    z = Lin.zero(m)

    def d1(c):
        if c > 2:
            return z
        out = grad[c]
        if c in FASTK:
            out = out + val.fast(FASTK[c]).shift(-1)
        return out

    def d2(c, d):
        if c > 2 or d > 2:
            return z
        out = hess[c][d]
        if d in FASTK:
            out = out + grad[c].fast(FASTK[d]).shift(-1)
        if c in FASTK:
            out = out + grad[d].fast(FASTK[c]).shift(-1)
        if c in FASTK and d in FASTK:
            out = out + val.fast(FASTK[c]).fast(FASTK[d]).shift(-2)
        return out
    return [d1(c) for c in range(N)], [[d2(c, d) for d in range(N)] for c in range(N)]


def ricci_h(g, m, gauge=True, verbose=False):
    t0 = time.time()
    J = {}
    for a in range(N):
        for b in range(a, N):
            J[(a, b)] = tojet(g[a, b], m)
    gv = [[J[(min(a, b), max(a, b))][0] for b in range(N)] for a in range(N)]
    dg = [[[None] * N for _ in range(N)] for _ in range(N)]                 # dg[c][a][b] = d_c g_ab
    ddg = [[[[None] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a in range(N):
        for b in range(a, N):
            d1, d2 = two_scale(*J[(a, b)], m)
            for c in range(N):
                dg[c][a][b] = dg[c][b][a] = d1[c]
                for d in range(N):
                    ddg[c][d][a][b] = ddg[c][d][b][a] = d2[c][d]
    if verbose:
        print("    jets %.0f s" % (time.time() - t0), flush=True)
    # the background at p: g0 is the lam^0 eps^0 part
    g0f = [[gv[a][b].s[0].get((0, 0, 0), Fr(0)) for b in range(N)] for a in range(N)]
    g0i_s = sp.Matrix(N, N, lambda a, b: sp.Rational(g0f[a][b].numerator, g0f[a][b].denominator)).inv()
    g0i = [[Fr(int(sp.fraction(g0i_s[a, b])[0]), int(sp.fraction(g0i_s[a, b])[1])) for b in range(N)]
           for a in range(N)]
    g0i_l = [[const(g0i[a][b], m) for b in range(N)] for a in range(N)]
    Delta = [[gv[a][b] - const(g0f[a][b], m) for b in range(N)] for a in range(N)]

    def matmul(A, B):
        return [[lsum((A[a][k].mul(B[k][b]) for k in range(N)), m) for b in range(N)] for a in range(N)]
    # g^-1 = sum_n (-g0^-1 Delta)^n g0^-1: Delta carries lam or eps, so n <= LCAP + 1 suffices
    term = g0i_l
    gi = g0i_l
    mD = [[-x for x in row] for row in Delta]
    for _ in range(LCAP + 1):                                                 # one eps factor at most
        term = matmul(matmul(g0i_l, mD), term)
        gi = [[gi[a][b] + term[a][b] for b in range(N)] for a in range(N)]
    if verbose:
        print("    inverse %.0f s" % (time.time() - t0), flush=True)
    dgi = []
    for e in range(N):
        X = matmul(gi, dg[e])
        Y = matmul(X, gi)
        dgi.append([[-Y[a][b] for b in range(N)] for a in range(N)])
    if verbose:
        print("    d inverse %.0f s" % (time.time() - t0), flush=True)
    Gl = [[[(dg[b][d][c] + dg[c][d][b] - dg[d][b][c]).scale(Fr(1, 2)) for c in range(N)] for b in range(N)]
          for d in range(N)]
    Gm = [[[lsum((gi[a][d].mul(Gl[d][b][c]) for d in range(N)), m) for c in range(N)] for b in range(N)]
          for a in range(N)]

    def dGl(e, d, b, c):
        return (ddg[e][b][d][c] + ddg[e][c][d][b] - ddg[e][d][b][c]).scale(Fr(1, 2))
    if verbose:
        print("    Christoffels %.0f s" % (time.time() - t0), flush=True)
    Ric = {}
    trG = [lsum((Gm[a][a][d] for a in range(N)), m) for d in range(N)]
    for b in range(N):
        for c in range(b, N):
            div = lsum((dgi[a][a][d].mul(Gl[d][b][c]) + gi[a][d].mul(dGl(a, d, b, c))
                        for a in range(N) for d in range(N)), m)
            trd = lsum((dgi[c][a][d].mul(Gl[d][a][b]) + gi[a][d].mul(dGl(c, d, a, b))
                        for a in range(N) for d in range(N)), m)
            q = lsum((trG[d].mul(Gm[d][b][c]) for d in range(N)), m)
            q2 = lsum((Gm[a][c][d].mul(Gm[d][a][b]) for a in range(N) for d in range(N)), m)
            Ric[(b, c)] = div - trd + q - q2
    if verbose:
        print("    Ricci %.0f s" % (time.time() - t0), flush=True)
    if not gauge:
        return Ric, gi, gv
    # background Christoffels and their derivatives (slow, numbers at p): from the eps^0 lam^0 parts
    def bg(L):
        return L.s[0].get((0, 0, 0), 0)
    G0l = [[[bg(Gl[d][b][c]) for c in range(N)] for b in range(N)] for d in range(N)]
    G0 = [[[sum(g0i[a][d] * G0l[d][b][c] for d in range(N)) for c in range(N)] for b in range(N)] for a in range(N)]
    dg0i = [[[-sum(g0i[a][x] * bg(dg[e][x][y]) * g0i[y][b] for x in range(N) for y in range(N)) for b in range(N)]
             for a in range(N)] for e in range(N)]
    dG0 = [[[[sum(dg0i[e][a][d] * G0l[d][b][c] + g0i[a][d] * bg(dGl(e, d, b, c)) for d in range(N))
              for c in range(N)] for b in range(N)] for a in range(N)] for e in range(N)]
    dGam = [[[[None] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]   # Gamma - Gamma0
    for r in range(N):
        for a in range(N):
            for b in range(N):
                dGam[r][a][b] = Gm[r][a][b] - const(G0[r][a][b], m)
    Dv = [lsum((gi[a][b].mul(dGam[r][a][b]) for a in range(N) for b in range(N)), m) for r in range(N)]
    gam = [lsum((gi[a][b].mul(Gl[d][a][b]) for a in range(N) for b in range(N)), m) for d in range(N)]
    dD = [[None] * N for _ in range(N)]                                      # dD[c][r] = d_c D^r
    for c in range(N):
        dlt = [lsum((gi[a][b].mul(dGl(c, d, a, b)) for a in range(N) for b in range(N)), m) for d in range(N)]
        for r in range(N):
            t1 = lsum((dgi[c][a][b].mul(dGam[r][a][b]) for a in range(N) for b in range(N)), m)
            t2 = lsum((dgi[c][r][d].mul(gam[d]) + gi[r][d].mul(dlt[d]) for d in range(N)), m)
            t3 = lsum((gi[a][b].scale(dG0[c][r][a][b]) for a in range(N) for b in range(N)), m)
            dD[c][r] = t1 + t2 - t3
    if verbose:
        print("    gauge %.0f s" % (time.time() - t0), flush=True)
    RH = {}
    for b in range(N):
        for c in range(b, N):
            corr = Lin.zero(m)
            for r in range(N):
                cov_c = dD[c][r] + lsum((Dv[s].scale(G0[r][c][s]) for s in range(N)), m)
                cov_b = dD[b][r] + lsum((Dv[s].scale(G0[r][b][s]) for s in range(N)), m)
                corr = corr + gv[b][r].mul(cov_c) + gv[c][r].mul(cov_b)
            RH[(b, c)] = Ric[(b, c)] - corr.scale(Fr(1, 2))
    return RH, gi, gv


# ------------------------------------------------------------------ predictions

def topoly(expr):
    """a sympy expression at p (polynomial in z1, z2, lam, rational coefficients) -> poly dict"""
    e = sp.expand(expr)
    if e == 0:
        return {}
    P = sp.Poly(e, Z1, Z2, LAM)
    return {mon: Fr(int(c.p), int(c.q)) for mon, c in P.terms()}


def at_p(M):
    return M.applyfunc(lambda x: sp.expand(x.subs({TU: 0, TV: 0, TT: 0})))


def order(pd, l):
    """the lam^l coefficient of a poly, as a dict in (n1, n2)"""
    return {(k[0], k[1]): c for k, c in pd.items() if k[2] == l and c}


def same(a, b):
    return padd(a, b, -1) == {}


def run(seed, gauge=True, control=None, verbose=False):
    g, I = build(seed, control)
    m = I["m"]
    RH, gi, gv = ricci_h(g, m, gauge=gauge, verbose=verbose)
    Ep = I["Ep"]
    G2 = {1: at_p(I["Yin"].applyfunc(lambda x: sp.expand(Z1 * sp.diff(x, Z1)))),
           2: at_p(I["Yout"].applyfunc(lambda x: sp.expand(Z2 * sp.diff(x, Z2))))}     # G2^k = F_k^2 W_k
    Y = {1: at_p(I["Yin"]), 2: at_p(I["Yout"])}
    res = {}
    comps = [(b, c) for b in range(N) for c in range(b, N)]
    # J1
    res["J1"] = all(not order(RH[bc].s[i], -2) for bc in comps for i in (1, 2, 3, 4))
    # J5
    pred5 = {bc: topoly((I["s_in"] * G2[1][bc] + I["s_out"] * G2[2][bc]) / 2) for bc in comps}
    res["J5"] = all(same(order(RH[bc].s[1], -1), order(pred5[bc], 0)) for bc in comps)
    # J2: lam^-1 of [P, phi] Y_k = -(ell_k . d phi) G2^k, ell_in . d phi = -d_u phi / E, ell_out . d phi = -d_v phi / E
    lp_in = -I["lin_in"][U] / Ep
    lp_out = -I["lin_out"][V] / Ep
    pred2 = {bc: topoly(-lp_in * G2[1][bc]) for bc in comps}
    pred3 = {bc: topoly(-lp_out * G2[2][bc]) for bc in comps}
    res["J2"] = (all(same(order(RH[bc].s[2], -1), order(pred2[bc], 0)) for bc in comps)
                 and all(same(order(RH[bc].s[3], -1), order(pred3[bc], 0)) for bc in comps))
    # J3: the whole eps_4 part is -(1/2) (g_app^ab d_a d_b phi) Y_k; at lam^0 with g0
    hq = {}
    for name, q in (("in", I["qin"]), ("out", I["qout"])):
        H = sp.zeros(N)
        for a in range(3):
            for b in range(3):
                H[a, b] = sp.diff(q, TVARS[a], TVARS[b])
        hq[name] = H
    g0i = at_p(I["g0"]).inv()
    box = {k: sum(g0i[a, b] * hq[k][a, b] for a in range(N) for b in range(N)) for k in ("in", "out")}
    pred4 = {bc: topoly(-(box["in"] * Y[1][bc] + box["out"] * Y[2][bc]) / 2) for bc in comps}
    j3_l0 = all(same(order(RH[bc].s[4], 0), order(pred4[bc], 0)) for bc in comps)
    j3_neg = all(not order(RH[bc].s[4], -1) and not order(RH[bc].s[4], -2) for bc in comps)
    res["J3"] = j3_l0 and j3_neg
    # J4: contractions at p (G1^k = Y_k, G2^k = F_k Y_k); ell_in = (-1/E) d_u, ell_out = (-1/E) d_v as vectors
    lin_v = [0] * N
    lin_v[U] = -1 / Ep
    lout_v = [0] * N
    lout_v[V] = -1 / Ep

    def c1(M, x):
        return [sp.expand(sum(M[a, b] * x[a] for a in range(N))) for b in range(N)]

    def c2(M, x, y):
        return sp.expand(sum(M[a, b] * x[a] * y[b] for a in range(N) for b in range(N)))
    own = all(c == 0 for c in c1(Y[1], lin_v) + c1(G2[1], lin_v) + c1(Y[2], lout_v) + c1(G2[2], lout_v))
    chp = sp.expand(I["chout"].subs({TU: 0, TV: 0, TT: 0}) * Z2**2)
    cip = sp.expand(I["chin"].subs({TU: 0, TV: 0, TT: 0}) * Z1**2)
    c_in = sp.expand(Z2 * sp.diff(chp, Z2) / Ep**2)
    c_out = sp.expand(Z1 * sp.diff(cip, Z1) / Ep**2)
    cross = (sp.expand(c2(Y[2], lin_v, lin_v) - c_in) == 0 and sp.expand(c2(Y[1], lout_v, lout_v) - c_out) == 0
             and sp.expand(c2(G2[2], lin_v, lin_v) - Z2 * sp.diff(c_in, Z2)) == 0 and c_in != 0)
    # ell_app^in - ell_in and g_app^-1(dv, dv): the lam^1 parts of gi at p (slot 0)
    l1 = {a: order(gi[a][V].s[0], 1) for a in range(N)}                    # (g_app^-1 dv)^a at lam^1
    pred_l = {a: (topoly(chp / Ep * lout_v[a]) if lout_v[a] else {}) for a in range(N)}
    ellapp = all(same(l1[a], {(k[0], k[1]): c for k, c in pred_l[a].items()}) for a in range(N))
    n1 = same(order(gi[V][V].s[0], 1), {(k[0], k[1]): c for k, c in topoly(-chp / Ep**2).items()})
    res["J4"] = own and cross and ellapp and n1
    # J6: ell_in x ell_in contraction of J3's lam^0 term = -(1/2) box phi_out c_in; mirror
    j6 = (same(_contract(RH, 4, lin_v), order(topoly(-box["out"] * c_in / 2), 0))
          and same(_contract(RH, 4, lout_v), order(topoly(-box["in"] * c_out / 2), 0)))
    res["J6"] = j6
    # J7: lam^-1 of P(h) + sum_k [P, phi_k] Y_k = (1/2) sum rho_k G2^k
    tot = {bc: padd(padd(order(RH[bc].s[1], -1), order(RH[bc].s[2], -1)), order(RH[bc].s[3], -1)) for bc in comps}
    pred7 = {bc: order(topoly((I["rho_in"] * G2[1][bc] + I["rho_out"] * G2[2][bc]) / 2), 0) for bc in comps}
    j7 = all(same(tot[bc], pred7[bc]) for bc in comps)
    totc = padd(padd(_contract(RH, 1, lin_v, -1), _contract(RH, 2, lin_v, -1)), _contract(RH, 3, lin_v, -1))
    j7c = same(totc, order(topoly(I["rho_out"] * Z2 * sp.diff(c_in, Z2) / 2), 0))
    res["J7"] = j7 and j7c
    # control (c): phi_in along ell_out
    totw = {bc: padd(padd(order(RH[bc].s[1], -1), order(RH[bc].s[8], -1)), order(RH[bc].s[3], -1)) for bc in comps}
    res["ctl_c"] = all(same(totw[bc], pred7[bc]) for bc in comps)
    # J0: D Ric^H[G](F_k G) = F_k Ric^H[G] at lam^-2, -1, 0; control (b) without lam^2 F_k Q
    j0, ctlb = True, True
    for slot, k in ((5, 1), (6, 2)):
        for bc in comps:
            lhs = {kk: c for kk, c in RH[bc].s[slot].items() if kk[2] <= 0}
            rhs = {kk: c for kk, c in pfast(RH[bc].s[0], k).items() if kk[2] <= 0}
            j0 &= same(lhs, rhs)
    for bc in comps:
        lhs = {kk: c for kk, c in RH[bc].s[7].items() if kk[2] <= 0}
        rhs = {kk: c for kk, c in pfast(RH[bc].s[0], 1).items() if kk[2] <= 0}
        ctlb &= same(lhs, rhs)
    res["J0"] = j0
    res["ctl_b"] = ctlb
    res["R-1"] = all(not order(RH[bc].s[0], -1) for bc in comps)
    # non-vacuity: every prediction tested above is nonzero somewhere, and so is R^(0) (J0 is not 0 = 0)
    nz = lambda d: any(order(d[bc], 0) for bc in comps)                    # noqa: E731
    res["nonvacuous"] = (nz(pred5) and nz(pred2) and nz(pred3) and nz(pred4) and any(pred7[bc] for bc in comps)
                         and c_in != 0 and c_out != 0 and bool(_contract(RH, 4, lin_v))
                         and any(order(RH[bc].s[0], 0) for bc in comps)
                         and any(order(pfast(RH[bc].s[0], 1), 0) for bc in comps))
    res["sizes"] = (sum(len(RH[bc].s[i]) for bc in comps for i in range(m + 1)),)
    return res


def tofr(x):
    x = sp.Rational(x)
    return Fr(int(x.p), int(x.q))


def _contract(RH, slot, x, l=0):
    out = {}
    for a in range(N):
        for b in range(N):
            if x[a] and x[b]:
                out = padd(out, pscale(order(RH[(min(a, b), max(a, b))].s[slot], l), tofr(x[a]) * tofr(x[b])))
    return out


def main():
    t0 = time.time()
    ok = True
    names = ["J1", "J5", "J2", "J3", "J4", "J6", "J7", "J0"]
    for seed in (1, 2, 3):
        r = run(seed, verbose=(seed == 1))
        good = all(r[k] for k in names) and r["R-1"]
        ctl = r["ctl_b"] or r["ctl_c"]
        print("  point %d: %s; R^(-1) = 0 for the stage-0 waves with lam^2 Q: %s; controls (b) J0 without lam^2 F_k Q "
              "holds: %s, (c) phi_in along ell_out leaves J7 intact: %s  (%.0f s)"
              % (seed, ", ".join("%s %s" % (k, r[k]) for k in names), r["R-1"], r["ctl_b"], r["ctl_c"],
                 time.time() - t0), flush=True)
        ok &= good and not ctl
    ra = run(1, gauge=False)
    ctl_a = ra["J2"] or ra["J3"] or ra["J5"]
    print("  control (a), plain Ric: J2 %s, J3 %s, J5 %s (each must fail)  (%.0f s)"
          % (ra["J2"], ra["J3"], ra["J5"], time.time() - t0), flush=True)
    rd = run(1, control="chi_dudv")
    print("  control (d), chi_out on du dv: J4 %s (must fail)  (%.0f s)" % (rd["J4"], time.time() - t0), flush=True)
    ok &= not ctl_a and not rd["J4"]
    print("J1-J7, J0 at three points:", "PASS" if ok else "FAIL")
    print("controls (a)-(d) rejected:", "PASS" if (not ctl_a and not rd["J4"]) else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
