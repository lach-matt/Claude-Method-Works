#!/usr/bin/env python3
"""scalarblock5: the scalar-type blocks of L-hat_b0(0) written exactly, every harmonic at once, with the identities
that pin them, their indicial structure at infinity against the record's, and what the weight of (3.2) does to their
inverse (INVERSE5-SCALAR.md part A; CONSTANTS5.md R8.3, R9.5's open item for I.C:497). Labels: computed (exact,
sympy, l symbolic), certified (mpmath.iv at 200 bits), deduced (where said), floating point (where said).

The operator (READ: III.B Definition 6.1, (6.1)-(6.4); III.E (1.1); N1STAR-PROOF.md Proposition 10.11 (10.48)-(10.49)):
L h = D Ric(h) + delta*_{E^C} delta_{E^Ups} G h on 5D Tangherlini in ingoing Kerr-Schild coordinates
g = -f dt^2 + 2 (1 - f) dt dr + (2 - f) dr^2 + r^2 (dth^2 + cos^2 th dphi1^2 + sin^2 th dphi2^2), f = 1 - 1/r^2 (mu = 1,
r_h = 1, regular across the horizon; the domain [r_h/2, oo) of I.A's extended slice), E^Ups k = -gam_U (2 iota_{c_U#}
k - (2/3)(1 - e_U) c_U tr k) + gam_H (2 iota_{c_H#} k - (2/3) c_H tr k), E^C w = gam_C (2 c_C (x)_s w - (2/3)(1 - e_C)
g <c_C, w>), on stationary fields (zero energy). The gauge 1-forms are kept general, c_C = a(r) dt + b(r) dr, c_U =
p(r) dt + q(r) dr, c_H = k(r) dr, so the block holds for every choice the record allows; the record's: c_C = (10.49),
(a, b) = (1/200, 1/800) on r <= 50, (1/200, -(r - 100)/40000) on [50, 200], (1/r, -1/(2r)) beyond (smoothed near
50 and 200); c_U = zeta(r) r^-1 dt (zeta = 1 for large r); c_H = -(1/2) chi(r) dr; (gam_U, e_U, gam_C, e_C) = (1/100,
1/100, 10^6, 1/102400) (lin5.POINT), gam_H in (0, eps_0] (III.D''' section 1; not a number in the record).

Scalar type, degree l (S a scalar harmonic, -Lap S = kappa S, kappa = l (l + 2); the computation uses S = cos^l th
e^(i l phi1) with l a symbol, every field stripped of S, d log S = (0, 0, -l tan th, i l, 0)):
  h = H0 S dt^2 + 2 H1 S dt dr + H2 S dr^2 + 2 H3 dt dS + 2 H4 dr dS + r^2 (H5 S gam + H6 S_AB),
  S_AB = D_A D_B S + (kappa/3) gam_AB S (traceless), and L h the same with (F0, ..., F6).

  S0 (exact) the background is Ricci-flat.
  S1 (exact) the block closes: for seven arbitrary radial functions, every component of L h equals the reconstruction
     from seven radial coefficients F_i (residual 0 in all fifteen components, l symbolic); the F_i are real, depend
     on l only through kappa, and F_i = sum_j (A2 H_j'' + A1 H_j' + A0 H_j) with A2 = -(f/2) I_7: the block is
     (1/2) A_l I_7 + first-order terms, A_l the scalar model of zeroext5. The coefficients are written to
     checks/scalarblock5_block.txt (general gauge data; srepr-free plain sympy strings).
  S2 (exact) the gauge identity: D Ric(delta* w) = 0 for every scalar-type 1-form w = W0 S dt + W1 S dr + W2 dS, and
     L(delta* w) = delta*_{E^C} ((1/2) box^Ups w), l symbolic.
  S3 (exact) the linearised Bianchi identity on the block, delta G (D Ric h) = 0, l symbolic; hence 2 delta G (L h) =
     box^C (Upsilon(h)), Upsilon(h) = delta_{E^Ups} G h, box^C = 2 delta G delta*_{E^C}, for every gauge datum (R8.3
     (c)'s factorisation, now computed on the block).
  S4 (exact) the mass state: h_mu = r^-2 (dt + dr)^2 = d/dmu g has D Ric(h_mu) = 0 (s0).
  S5 (exact) the indicial family at infinity, from the block (outer c_C, c_U = r^-1 dt, c_H = 0): det N_l(lam) equals,
     up to a constant, (lam + l)(lam - l - 2) P_Ups(lam - 1) P_C(lam + 1) / D(lam) at l = 0, 2, 4, with P_Ups from
     gaugepot5 G1's formulas and P_C from damping5.polys: lin5 E2's factorisation reproduced from the Tangherlini
     block in Kerr-Schild coordinates (an independent route), with its roots, the decaying one nearest 1 printed.
  S5b (exact) the horizon r = 1 is a regular singular point of the block (A2 = -(f/2) I, f ~ 2 (r - 1)): exponents 0
     and 1 + eig A1(1); A1(1)'s characteristic polynomial does not depend on l (kappa = 8, 24), its roots carry
     x = gam_C a_v r_h = 5000 (III.F'' Lemma 1.1): large l does not move the horizon part of the problem.
  S6 (certified; deduced) the weight. (3.2) at (s, alpha) = (1, -1) is Hbar^(1,-1)_b -> Hbar^(0,1)_b; in the
     orthonormal components u_j (|h|^2 = sum |u_j|^2 on L^2(S^3)) the norm is sum_j int (r|u_j|^2 + r^3|u_j'|^2 + kappa
     r|u_j|^2) dr (the b-fields r d_r and the Lie derivatives of the six Killing fields, whose squares sum to kappa
     on every scalar-type piece, the so(4) Casimir on (l/2, l/2)). Lemma (deduced): for every unit vector v,
     sigma_min(L_l) <= |N_n,l(alpha + 2) v| / sqrt(2 + kappa) (quasi-modes r^-1 psi(log r / W) v at large r, W -> oo;
     the Tangherlini and cut-off errors vanish in the limit). At alpha + 2 = 1 the line lies 2.93e-6 from the s2 root
     1 + 2.93e-6 (box^C's lowest upper root at l = 2): certified, sigma_min(L_2) <= the printed bound, so the scalar
     blocks' inverse constant in (3.2)'s norm at alpha = -1 is at least its reciprocal. The same bound at alpha + 2 =
     1/2, mid-gap, is printed for comparison (it is of order one).
  S7 (floating point; a measurement) the lemma's quasi-mode on the actual block at l = 2, x0 = log 400, finite widths:
     ||L h||_Y / ||h||_X approaches S6's bound.
  Negative controls (each must fail): C1 D Ric without its -nabla nabla tr h term: S2's identity fails; C2 S3 with
  delta in place of delta G: the identity fails; C3 the background with f = 1 - 1/r^3: not Ricci-flat (S0
  fails); C4 the record's box^C polynomial at e_C = 1/10240: S5's proportionality fails; C5 the claim sigma_min(L_2)
  >= 10^-4 at alpha = -1: refuted by S6.

    python3 checks/scalarblock5.py [--selftest]       (several minutes; --selftest skips S7)
"""
import builtins
import contextlib
import io
import os
import sys
import textwrap
import time

import mpmath as mpm
import sympy as sp
from mpmath import iv

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)
with contextlib.redirect_stdout(io.StringIO()):
    import damping5 as DP            # noqa: E402  (box^C indicial polynomials, the record's)

iv.prec = 200
OK = {}
I = sp.I
r = sp.Symbol('r', positive=True)
c, s = sp.symbols('c s', positive=True)          # cos(theta), sin(theta)
l = sp.Symbol('l', positive=True)
kap = sp.Symbol('kappa')
lam = sp.Symbol('lam')
LL = l * (l + 2)
NJ = 6
gU, eU, gC, eC, gH = sp.symbols('gU eU gC eC gH')
POINT = {gU: sp.Rational(1, 100), eU: sp.Rational(1, 100), gC: 10 ** 6, eC: sp.Rational(1, 102400)}
BLOCK_TXT = os.path.join(HERE, 'scalarblock5_block.txt')


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


# ------------------------------------------------------------------------------------------------ the calculus
class Jet:
    def __init__(self, name):
        self.sym = sp.symbols('%s_0:%d' % (name, NJ))

    def __getitem__(self, k):
        return self.sym[k]


JETS = {}


def jet(name):
    if name not in JETS:
        JETS[name] = Jet(name)
    return JETS[name]


def d_r(E):
    out = sp.diff(E, r)
    for j in JETS.values():
        for k in range(NJ - 1):
            if E.has(j[k]):
                out += j[k + 1] * sp.diff(E, j[k])
    return out


def d_th(E):
    return -s * sp.diff(E, c) + c * sp.diff(E, s)


def plain(E, mu):
    if mu == 1:
        return d_r(E)
    if mu == 2:
        return d_th(E)
    return sp.Integer(0)


def omega(lv):
    return [0, 0, -lv * s / c, I * lv, 0]


def reduce_cs(E):
    """normal form modulo s^2 = 1 - c^2, a denominator linear in s rationalised"""
    E = sp.together(sp.expand(E))
    n, d = sp.fraction(E)

    def red(P):
        P = sp.Poly(sp.expand(P), s)
        return sp.expand(sp.rem(P, sp.Poly(s ** 2 - 1 + c ** 2, s)).as_expr())
    n, d = red(n), red(d)
    if d.has(s):
        a0 = d.subs(s, 0)
        a1 = sp.expand((d - a0) / s)
        n = red(n * (a0 - a1 * s))
        d = sp.expand(a0 ** 2 - a1 ** 2 * (1 - c ** 2))
    return sp.cancel(n / d)


class Geo:
    """the background and the operators on S-stripped fields (S of degree lv)"""

    def __init__(self, fexp=None, lv=l):
        self.f = 1 - 1 / r ** 2 if fexp is None else fexp
        f = self.f
        g = sp.zeros(5)
        g[0, 0] = -f
        g[0, 1] = g[1, 0] = 1 - f
        g[1, 1] = 2 - f
        g[2, 2] = r ** 2
        g[3, 3] = r ** 2 * c ** 2
        g[4, 4] = r ** 2 * s ** 2
        self.g = g
        self.gi = sp.simplify(g.inv())
        self.Gam = [[[sp.cancel(sum(self.gi[a, d] * (plain(g[d, b], cc) + plain(g[d, cc], b) - plain(g[b, cc], d))
                                    for d in range(5)) / 2) for cc in range(5)] for b in range(5)] for a in range(5)]
        self.lv = lv
        self.om = omega(lv)
        self.gam3 = sp.diag(1, c ** 2, s ** 2)
        gm = [[[0] * 3 for _ in range(3)] for _ in range(3)]
        gm[0][1][1] = c * s
        gm[0][2][2] = -s * c
        gm[1][0][1] = gm[1][1][0] = -s / c
        gm[2][0][2] = gm[2][2][0] = c / s
        om = self.om[2:]
        self.hess = sp.Matrix(3, 3, lambda A, B: reduce_cs(plain(om[B], A + 2) + om[A] * om[B]
                                                            - sum(gm[C][A][B] * om[C] for C in range(3))))
        self.kap = lv * (lv + 2)

    def tw(self, E, mu, w=1):
        return plain(E, mu) + (self.om[mu] * E if w else 0)

    def ricci(self):
        Gm = self.Gam
        R = sp.zeros(5)
        for b in range(5):
            for cc in range(b, 5):
                e = 0
                for a in range(5):
                    e += plain(Gm[a][b][cc], a) - plain(Gm[a][a][b], cc)
                    for d in range(5):
                        e += Gm[a][a][d] * Gm[d][b][cc] - Gm[a][cc][d] * Gm[d][a][b]
                R[b, cc] = R[cc, b] = reduce_cs(e)
        return R

    def scalar_h(self, H):
        h = sp.zeros(5)
        h[0, 0], h[0, 1], h[1, 1] = H[0], H[1], H[2]
        h[1, 0] = H[1]
        om = self.om[2:]
        for A in range(3):
            h[0, A + 2] = h[A + 2, 0] = H[3] * om[A]
            h[1, A + 2] = h[A + 2, 1] = H[4] * om[A]
            for B in range(3):
                h[A + 2, B + 2] = r ** 2 * (H[5] * self.gam3[A, B] + H[6] * (self.hess[A, B] + self.kap / 3
                                                                              * self.gam3[A, B]))
        return h

    def scalar_w(self, W):
        om = self.om[2:]
        return [W[0], W[1]] + [W[2] * om[A] for A in range(3)]

    def nabla2(self, h, w=1):
        Gm = self.Gam
        T = [[[None] * 5 for _ in range(5)] for _ in range(5)]
        for a in range(5):
            for b in range(a, 5):
                for cc in range(5):
                    T[a][b][cc] = T[b][a][cc] = self.tw(h[a, b], cc, w) - sum(
                        Gm[d][cc][a] * h[d, b] + Gm[d][cc][b] * h[a, d] for d in range(5))
        return T

    def nabla1(self, om_, w=1):
        Gm = self.Gam
        return [[self.tw(om_[a], b, w) - sum(Gm[d][b][a] * om_[d] for d in range(5)) for b in range(5)]
                for a in range(5)]

    def trace(self, h):
        return sum(self.gi[a, b] * h[a, b] for a in range(5) for b in range(5))

    def dric(self, h, w=1, drop_trace=False):
        """D Ric(h) = nabla_a dGam^a_bc - nabla_c dGam^a_ab, dGam = (1/2) g^-1 (nabla h + nabla h - nabla h)"""
        Gm, gi = self.Gam, self.gi
        T = self.nabla2(h, w)
        dG = [[[sum(gi[a, d] * (T[cc][d][b] + T[b][d][cc] - T[b][cc][d]) for d in range(5)) / 2
                for cc in range(5)] for b in range(5)] for a in range(5)]
        V = [sum(dG[a][a][b] for a in range(5)) for b in range(5)]
        R = sp.zeros(5)
        for b in range(5):
            for cc in range(b, 5):
                div = 0
                for a in range(5):
                    div += self.tw(dG[a][b][cc], a, w)
                    div += sum(Gm[a][a][e] * dG[e][b][cc] - Gm[e][a][b] * dG[a][e][cc] - Gm[e][a][cc] * dG[a][b][e]
                               for e in range(5))
                nv = self.tw(V[b], cc, w) - sum(Gm[e][cc][b] * V[e] for e in range(5))
                R[b, cc] = R[cc, b] = div - (0 if drop_trace else nv)
        return R

    def Gop(self, h):
        return h - self.g * self.trace(h) / 2

    def delta(self, k, w=1):
        T = self.nabla2(k, w)
        return [-sum(self.gi[b, cc] * T[a][b][cc] for b in range(5) for cc in range(5)) for a in range(5)]

    def dstar(self, om_, w=1):
        N = self.nabla1(om_, w)
        return sp.Matrix(5, 5, lambda a, b: (N[a][b] + N[b][a]) / 2)

    def raise1(self, cf):
        return [sum(self.gi[a, b] * cf[b] for b in range(5)) for a in range(5)]

    def E_ups(self, k, P):
        t = self.trace(k)
        a1, a2 = self.raise1(P['cU']), self.raise1(P['cH'])
        i1 = [sum(a1[a] * k[a, b] for a in range(5)) for b in range(5)]
        i2 = [sum(a2[a] * k[a, b] for a in range(5)) for b in range(5)]
        return [-P['gU'] * (2 * i1[b] - sp.Rational(2, 3) * (1 - P['eU']) * P['cU'][b] * t)
                + P['gH'] * (2 * i2[b] - sp.Rational(2, 3) * P['cH'][b] * t) for b in range(5)]

    def E_C(self, om_, P, m=sp.Rational(2, 3)):
        cC = P['cC']
        cw = sum(self.gi[a, b] * cC[a] * om_[b] for a in range(5) for b in range(5))
        return sp.Matrix(5, 5, lambda a, b: P['gC'] * (cC[a] * om_[b] + cC[b] * om_[a] - m * (1 - P['eC'])
                                                         * self.g[a, b] * cw))

    def upsilon(self, h, P, w=1):
        k = self.Gop(h)
        return [x + y for x, y in zip(self.delta(k, w), self.E_ups(k, P))]

    def L(self, h, P, w=1):
        U = self.upsilon(h, P, w)
        return self.dric(h, w) + self.dstar(U, w) + self.E_C(U, P)

    def boxC(self, om_, P, w=1, m=sp.Rational(2, 3)):
        return [2 * x for x in self.delta(self.Gop(self.dstar(om_, w) + self.E_C(om_, P, m)), w)]

    def boxU(self, om_, P, w=1):
        k = self.Gop(self.dstar(om_, w))
        return [2 * (x + y) for x, y in zip(self.delta(k, w), self.E_ups(k, P))]

    def extract(self, M):
        om = self.om[2:]
        F = [reduce_cs(M[0, 0]), reduce_cs(M[0, 1]), reduce_cs(M[1, 1]), reduce_cs(M[0, 3] / om[1]),
             reduce_cs(M[1, 3] / om[1])]
        gi3 = self.gam3.inv()
        trA = sum(gi3[A, B] * M[A + 2, B + 2] for A in range(3) for B in range(3))
        F.append(reduce_cs(trA / (3 * r ** 2)))
        F.append(reduce_cs((M[2, 3] / r ** 2 - F[5] * self.gam3[0, 1]) / (self.hess[0, 1] + self.kap / 3
                                                                           * self.gam3[0, 1])))
        rec = self.scalar_h(F)
        res = [reduce_cs(M[a, b] - rec[a, b]) for a in range(5) for b in range(a, 5)]
        return F, res


def gauge_data():
    A, B, Pq, Q, K = jet('a'), jet('b'), jet('p'), jet('q'), jet('k')
    return dict(cC=[A[0], B[0], 0, 0, 0], cU=[Pq[0], Q[0], 0, 0, 0], cH=[0, K[0], 0, 0, 0], gU=gU, eU=eU, gC=gC,
                eC=eC, gH=gH)


def to_kappa(x):
    n, d = sp.fraction(sp.together(x))
    out = []
    for P_ in (n, d):
        P_ = sp.Poly(sp.expand(P_), l)
        cf = P_.all_coeffs()[::-1] + [0, 0, 0]
        if P_.degree() > 2 or sp.expand(cf[1] - 2 * cf[2]) != 0:
            return None
        out.append(cf[0] + cf[2] * kap)
    return out[0] / out[1]


# ------------------------------------------------------------------------------------------------ S1 the block
def block():
    G = Geo()
    P = gauge_data()
    Hs = [jet('H%d' % i) for i in range(7)]
    M = G.L(G.scalar_h([x[0] for x in Hs]), P)
    F, res = G.extract(M)
    Fk = [to_kappa(x) for x in F]
    real = all(not x.has(I) for x in F)
    mats = None
    if all(x is not None for x in Fk):
        mats = [[[sp.cancel(sp.diff(Fk[i], Hs[j][k])) for j in range(7)] for i in range(7)] for k in range(3)]
        lin = all(sp.cancel(sum(mats[k][i][j] * Hs[j][k] for j in range(7) for k in range(3)) - Fk[i]) == 0
                  for i in range(7))
    else:
        lin = False
    f = 1 - 1 / r ** 2
    prin = mats is not None and all(sp.cancel(mats[2][i][j] - (-f / 2 if i == j else 0)) == 0
                                    for i in range(7) for j in range(7))
    return dict(res=res, real=real, kappa=all(x is not None for x in Fk), lin=lin, prin=prin, mats=mats, G=G, P=P,
                Hs=Hs, M=M)


def write_block(mats):
    """the coefficients, one entry per item, wrapped at 116 characters (continuation lines start with four spaces;
    join them to read an entry)"""
    lines = ['# scalarblock5: the scalar-type block of L-hat_b0(0) on 5D Tangherlini (ingoing Kerr-Schild, mu = 1).',
             '# F_i = sum_j (A2[i][j] H_j\'\' + A1[i][j] H_j\' + A0[i][j] H_j); kappa = l (l + 2).',
             '# Gauge data: c_C = a dt + b dr, c_U = p dt + q dr, c_H = k dr (a_0 = a, a_1 = a\', ...);',
             '# parameters gU, eU, gC, eC, gH. Components: h = H0 S dt^2 + 2 H1 S dt dr + H2 S dr^2',
             '# + 2 H4 dr dS + 2 H3 dt dS + r^2 (H5 S gam + H6 S_AB); L h the same with F0, ..., F6.',
             '# Continuation lines start with four spaces. Generated by checks/scalarblock5.py S1; regenerate,',
             '# never hand-edit.']
    for k, nm in ((2, 'A2'), (1, 'A1'), (0, 'A0')):
        for i in range(7):
            for j in range(7):
                if mats[k][i][j] != 0:
                    txt = '%s[%d][%d] = %s' % (nm, i, j, sp.sstr(sp.factor(mats[k][i][j])))
                    lines.append(txt[:116])
                    txt = txt[116:]
                    while txt:
                        lines.append('    ' + txt[:112])
                        txt = txt[112:]
    open(BLOCK_TXT, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    return len(lines)


def read_block():
    """parse checks/scalarblock5_block.txt back (a consistency check of the written data)"""
    ent, cur = {}, None
    for ln in open(BLOCK_TXT, encoding='utf-8').read().split('\n'):
        if not ln or ln.startswith('#'):
            continue
        if ln.startswith('    '):
            ent[cur] += ln[4:]
        else:
            cur, rhs = ln.split(' = ', 1)
            ent[cur] = rhs
    return ent


# ------------------------------------------------------------------------------------------------ S2-S4 identities
def s0(fexp=None):
    G = Geo(fexp=fexp, lv=0)
    R = G.ricci()
    return all(x == 0 for x in R)


def s2(drop_trace=False):
    G = Geo()
    P = gauge_data()
    W = [jet('W%d' % i)[0] for i in range(3)]
    om_ = G.scalar_w(W)
    h = G.dstar(om_)
    R = G.dric(h, drop_trace=drop_trace)
    ok1 = all(reduce_cs(R[a, b]) == 0 for a in range(5) for b in range(a, 5))
    if drop_trace:
        return ok1, None
    U = G.upsilon(h, P)
    bU = G.boxU(om_, P)
    ok2 = all(reduce_cs(U[a] - bU[a] / 2) == 0 for a in range(5))
    return ok1, ok2


def s3(B, use_G=True):
    """the linearised Bianchi identity on the block: delta G (D Ric h) = 0 for every scalar-type h (l symbolic). As
    L h = D Ric h + delta*_{E^C} Upsilon(h) and box^C = 2 delta G delta*_{E^C}, it is 2 delta G (L h) = box^C
    Upsilon(h) for every gauge datum (the same operators, by linearity)"""
    G, Hs = B['G'], B['Hs']
    h = G.scalar_h([x[0] for x in Hs])
    R = G.dric(h)
    lhs = G.delta(G.Gop(R) if use_G else R)
    return all(reduce_cs(lhs[a]) == 0 for a in range(5))


def s4():
    G = Geo(lv=0)
    h = sp.zeros(5)
    h[0, 0] = h[0, 1] = h[1, 0] = h[1, 1] = 1 / r ** 2
    mu = sp.Symbol('mu')
    f = 1 - mu / r ** 2
    gm = [[-f, 1 - f], [1 - f, 2 - f]]
    same = all(sp.simplify(sp.diff(gm[a][b], mu) - h[a, b]) == 0 for a in range(2) for b in range(2))
    R = G.dric(h, w=0)
    return same and all(reduce_cs(R[a, b]) == 0 for a in range(5) for b in range(5))


# ------------------------------------------------------------------------------------------------ S5 indicial
SH = [0, 0, 0, 1, 1, 0, 0]


def outer_subs():
    vv = sp.Rational(1, 2)
    A, B, Pq, Q, K = jet('a'), jet('b'), jet('p'), jet('q'), jet('k')
    sub = {A[0]: 1 / r, B[0]: -vv / r, Pq[0]: 1 / r, Pq[1]: -1 / r ** 2, Q[0]: 0, Q[1]: 0, K[0]: 0, K[1]: 0}
    sub.update(POINT)
    return sub


def indicial(mats, kv, comps):
    sub = outer_subs()
    N = sp.zeros(len(comps))
    for ii, i in enumerate(comps):
        for jj, j in enumerate(comps):
            e = 0
            for k in range(3):
                e += mats[k][i][j].subs(sub).subs(kap, kv) * sp.diff(r ** (-lam + SH[j]), r, k)
            N[ii, jj] = sp.limit(sp.cancel(e * r ** (lam + 2 - SH[i])), r, sp.oo)
    return N


def record_factor(lv, polys, eC_val=sp.Rational(1, 102400)):
    z = 4 * POINT[eU] * POINT[gU] ** 2
    x = lam - 1
    kv = lv * (lv + 2)
    if lv == 0:
        pU = x * (x - 3) * (x ** 2 - x - 2 - z)
    else:
        sU = x * (x - 1)
        Q = sU ** 2 - (2 + 2 * kv + z) * sU + kv * (kv + 1) + z * kv
        pU = (lv + 3 - x) * (lv + x - 1) * Q
    pk, p0, pv = polys
    pt = {DP.h: sp.Rational(1, 10 ** 6), DP.e: eC_val, DP.v: sp.Rational(1, 2)}
    pC = (p0 if lv == 0 else pk.subs(DP.K, kv)).subs(pt).subs(DP.lam, lam + 1)
    Dl = (lam - 1) ** 2 if lv in (0, 1) else 1
    return sp.cancel((lam + lv) * (lam - lv - 2) * pU * pC / Dl)


def proportional(p, q):
    rat = sp.cancel(p / q)
    return rat.free_symbols == set() and rat != 0, rat


def s5(mats, polys, eC_val=sp.Rational(1, 102400), levels=(0, 2, 4)):
    out = []
    for lv in levels:
        comps = [0, 1, 2, 5] if lv == 0 else list(range(7))
        N = indicial(mats, lv * (lv + 2), comps)
        det = sp.factor(N.det())
        ok, rat = proportional(det, record_factor(lv, polys, eC_val))
        Pd = sp.Poly(sp.expand(sp.numer(sp.together(det))), lam)
        mpm.mp.dps = 60
        rts = mpm.polyroots([mpm.mpf(sp.Rational(q).p) / sp.Rational(q).q for q in Pd.all_coeffs()],
                            maxsteps=800, extraprec=800)
        up = sorted([z for z in rts if mpm.re(z) > 1], key=lambda z: mpm.re(z))
        out.append((lv, ok, rat, up[0] if up else None, N))
    return out


def horizon_exponents(mats, kv):
    """the regular singular point r = 1: with A2 = -(f/2) I and f ~ 2 (r - 1), the exponents are 0 (seven times) and
    1 + eig(A1(1)); A1(1) at the record's inner c_C = (1/200) dt + (1/800) dr, c_U = r^-1 dt, c_H = -(1/2) dr"""
    A, B, Pq, Q, K = jet('a'), jet('b'), jet('p'), jet('q'), jet('k')
    sub = {A[0]: sp.Rational(1, 200), B[0]: sp.Rational(1, 800), Pq[0]: 1 / r, Pq[1]: -1 / r ** 2, Q[0]: 0, Q[1]: 0,
           K[0]: sp.Rational(-1, 2), K[1]: 0}
    M = sp.Matrix(7, 7, lambda i, j: sp.cancel(mats[1][i][j].subs(sub).subs(kap, kv).subs(r, 1)))
    xs = sp.Symbol('x')
    cp = sp.factor(M.subs(POINT).charpoly(xs).as_expr())
    gen = sp.factor(M.charpoly(xs).as_expr())
    return M, cp, gen


# ------------------------------------------------------------------------------------------------ S6 the weight
def nu(kv, comps):
    full = [1, sp.sqrt(2), 1, sp.sqrt(2 * kv), sp.sqrt(2 * kv), sp.sqrt(3),
            sp.sqrt(sp.Rational(2, 3) * kv * (kv - 3)) if kv > 3 else 1]
    return [full[i] for i in comps]


def normalized(N, kv, comps):
    n = nu(kv, comps)
    return sp.Matrix(len(comps), len(comps), lambda i, j: n[i] * N[i, j] / n[j])


def s6(N, kv, comps, beta_line):
    """certified upper bound for |N_n(beta) v| / (sqrt(1 + beta^2 + kappa) |v|) at one vector v (the smallest right
    singular vector of N_n(beta), found in floating point; any v gives a valid bound, certified by intervals)"""
    Nn = normalized(N, kv, comps)
    n = len(comps)
    Mb = sp.Matrix(Nn.subs(lam, beta_line))
    mpm.mp.dps = 50
    A = mpm.matrix([[mpm.mpf(str(sp.N(Mb[i, j], 60))) for j in range(n)] for i in range(n)])
    _U, S, V = mpm.svd_r(A)
    k = min(range(n), key=lambda q: S[q])
    vi = [iv.mpf(mpm.nstr(V[k, j], 40)) for j in range(n)]
    eps = iv.mpf('1e-65')

    def ent(x):
        if x == 0:
            return iv.mpf(0)
        m = iv.mpf(str(sp.N(x, 80)))
        return iv.mpf([m.a - eps.b, m.b + eps.b])
    Ai = [[ent(Mb[i, j]) for j in range(n)] for i in range(n)]
    Av = [sum((Ai[i][j] * vi[j] for j in range(n)), iv.mpf(0)) for i in range(n)]
    num = iv.sqrt(sum((x * x for x in Av), iv.mpf(0)))
    bl = iv.mpf(sp.Rational(beta_line).p) / sp.Rational(beta_line).q
    den = iv.sqrt(sum((x * x for x in vi), iv.mpf(0))) * iv.sqrt(1 + bl * bl + kv)
    q = num / den
    return q.b, S[k], [V[k, j] for j in range(n)]


# ------------------------------------------------------------------------------------------------ S7 the quasi-mode
def s7(mats, kv, v, W, x0=None):
    """floating point: ||L h||_Y / ||h||_X for h = r^-1 psi(log r) v (normalized components), psi = sin^2 on
    [x0, x0 + W], with the full Tangherlini block and the outer gauge data"""
    x0 = mpm.log(400) if x0 is None else x0
    sub = outer_subs()
    comps = list(range(7))
    n = [sp.sqrt(2 * kv) if j in (3, 4) else q for j, q in enumerate(nu(kv, comps))]
    x = sp.Symbol('x')
    psi = sp.sin(sp.pi * (x - sp.Float(str(x0), 30)) / W) ** 2
    U = [r ** -1 * psi.subs(x, sp.log(r)) * sp.Float(mpm.nstr(v[j], 25), 30) for j in comps]
    H = [U[j] * r ** SH[j] / n[j] for j in comps]                 # u_j = nu_j H_j r^-SH_j
    Fs = []
    for i in comps:
        e = 0
        for j in comps:
            for k in range(3):
                cf = mats[k][i][j].subs(sub).subs(kap, kv)
                if cf != 0:
                    e += cf * sp.diff(H[j], r, k)
        Fs.append(e * n[i] * r ** (-SH[i]))
    fF = [sp.lambdify(r, F, 'mpmath') for F in Fs]
    fU = [sp.lambdify(r, u, 'mpmath') for u in U]
    fUd = [sp.lambdify(r, sp.diff(u, r), 'mpmath') for u in U]
    mpm.mp.dps = 30

    def integ(fn):
        return mpm.quad(lambda t: fn(mpm.e ** t) * mpm.e ** t, mpm.linspace(x0, x0 + W, 81))
    Y2 = integ(lambda rr: rr ** 5 * sum(abs(f(rr)) ** 2 for f in fF))
    X2 = integ(lambda rr: sum(rr * abs(u(rr)) ** 2 + rr ** 3 * abs(ud(rr)) ** 2 + kv * rr * abs(u(rr)) ** 2
                              for u, ud in zip(fU, fUd)))
    return mpm.sqrt(Y2 / X2)


# ------------------------------------------------------------------------------------------------ main
def main(selftest=False):
    t0 = time.time()
    print('scalarblock5: the scalar-type blocks of L-hat_b0(0) on 5D Tangherlini, every harmonic, exactly')
    OK['S0'] = s0()
    print('  S0 (exact): Kerr-Schild Tangherlini (10.48), mu = 1, is Ricci-flat: %s' % OK['S0'])
    B = block()
    OK['S1'] = all(x == 0 for x in B['res']) and B['real'] and B['kappa'] and B['lin'] and B['prin']
    nl = write_block(B['mats']) if B['mats'] is not None else 0
    ent = read_block()
    syms = {str(x): x for x in list(B['P'].values()) if isinstance(x, sp.Symbol)}
    back = all(sp.cancel(sp.sympify(ent['A%d[%d][%d]' % (k, i, j)], locals=dict(syms, r=r, kappa=kap))
                         - B['mats'][k][i][j]) == 0 for k in range(3) for i in range(7) for j in range(7)
               if B['mats'][k][i][j] != 0)
    OK['S1'] = OK['S1'] and back
    print('  S1 (exact): every component of L h reconstructs from seven radial coefficients (15 residuals, all 0: %s); '
          'real: %s; l only through kappa = l (l + 2): %s; second order in H with A2 = -(f/2) I_7: %s; %d lines written '
          'to checks/scalarblock5_block.txt and read back identically: %s (%.0f s): %s' % (
              all(x == 0 for x in B['res']), B['real'], B['kappa'], B['prin'], nl, back, time.time() - t0, OK['S1']))
    ok1, ok2 = s2()
    OK['S2'] = ok1 and ok2
    print('  S2 (exact): D Ric(delta* w) = 0 for every scalar-type w (l symbolic): %s; Upsilon(delta* w) = (1/2) '
          'box^Ups w, so L delta* w = delta*_{E^C} (1/2) box^Ups w: %s: %s' % (ok1, ok2, OK['S2']))
    OK['S3'] = s3(B)
    print('  S3 (exact): delta G (D Ric h) = 0 for every scalar-type h, l symbolic; so 2 delta G (L h) = box^C '
          'Upsilon(h) for every gauge datum (R8.3 (c)\'s factorisation of the block): %s (%.0f s)' % (
              OK['S3'], time.time() - t0))
    OK['S4'] = s4()
    print('  S4 (exact): h_mu = r^-2 (dt + dr)^2 = d/dmu of (10.48): D Ric(h_mu) = 0: %s' % OK['S4'])
    print('      (the record\'s box^C polynomials, damping5.polys, about half a minute)')
    polys = DP.polys(4, sp.Rational(2, 3))
    S5 = s5(B['mats'], polys)
    OK['S5'] = all(ok for _l, ok, _r, _u, _N in S5)
    for lv, ok, rat, up, _N in S5:
        print('  S5 (exact): l = %d: det N_l(lam) / [(lam + l)(lam - l - 2) P_Ups(lam - 1) P_C(lam + 1) / D(lam)] = %s, '
              'a constant: %s; the least decaying root (real part > 1): %s' % (lv, rat, ok, mpm.nstr(up, 15)))
    hx = [horizon_exponents(B['mats'], kv) for kv in (0, 8, 24)]
    xs = sp.Symbol('x')
    lfree = all(sp.expand(h[2] - hx[1][2]) == 0 for h in hx[1:])
    gam_x = sp.Symbol('X')
    OK['S5b'] = lfree
    print('  S5b (exact): the horizon r = 1 is a regular singular point of the block; with c_C = (10.49)\'s inner '
          'piece, c_U = r^-1 dt, c_H = -(1/2) dr, the exponents are 0 (seven) and 1 + eig A1(1), A1(1)\'s '
          'characteristic polynomial (gam_C, e_C, gam_U, e_U, gam_H symbolic) is the same at kappa = 8 and 24 '
          '(l-free): %s; at the record\'s point: %s (x = gam_C a_v r_h = 5000 in III.F\'\' Lemma 1.1)' % (
              lfree, hx[1][1]))
    rows = []
    for lv, _ok, _r, up, N in S5:
        comps = [0, 1, 2, 5] if lv == 0 else list(range(7))
        b1, _s1, v1 = s6(N, lv * (lv + 2), comps, 1)
        bh, _sh, _vh = s6(N, lv * (lv + 2), comps, sp.Rational(1, 2))
        rows.append((lv, b1, bh, up, v1))
    b2 = [b for lv, b, _bh, _u, _v in rows if lv == 2][0]
    v2 = [v for lv, _b, _bh, _u, v in rows if lv == 2][0]
    OK['S6'] = all(b < bh / 100 for _l, b, bh, _u, _v in rows)
    print('  S6 (certified; the quasi-mode lemma deduced): sigma_min(L_l) on Hbar^(1,-1)_b -> Hbar^(0,1)_b is at most '
          '%s; so the scalar blocks\' inverse constant at alpha = -1 is at least %.4e (from l = 2); at alpha + 2 = 1/2 '
          'the same bounds are %s (order one): %s' % (
              '; '.join('%.4e at l = %d (root %s)' % (float(b), lv, mpm.nstr(u, 10)) for lv, b, _bh, u, _v in rows),
              1 / float(b2), ', '.join('%.3f' % float(bh) for _l, _b, bh, _u, _v in rows), OK['S6']))
    if not selftest:
        vals = [(W, s7(B['mats'], 8, v2, W)) for W in (200, 2000, 20000)]
        OK['S7'] = vals[-1][1] < 2 * float(b2) + 1e-4 and vals[-1][1] < vals[0][1]
        print('  S7 (floating point): the quasi-mode on the full block at l = 2, x0 = log 400: ||L h||_Y/||h||_X = %s '
              '(widths W), tending to S6\'s %.4e: %s' % (
                  ', '.join('%.4e (W = %d)' % (float(q), W) for W, q in vals), float(b2), OK['S7']))
    # controls
    OK['C1'] = not s2(drop_trace=True)[0]
    print('  C1 (control): D Ric without -nabla nabla tr h: the gauge identity fails: %s' % OK['C1'])
    OK['C2'] = not s3(B, use_G=False)
    print('  C2 (control): delta (D Ric h) without G: the identity fails: %s' % OK['C2'])
    OK['C3'] = not s0(fexp=1 - 1 / r ** 3)
    print('  C3 (control): f = 1 - 1/r^3: not Ricci-flat: %s' % OK['C3'])
    S5c = s5(B['mats'], polys, eC_val=sp.Rational(1, 10240), levels=(2,))
    OK['C4'] = not S5c[0][1]
    print('  C4 (control): the record\'s box^C polynomial at e_C = 1/10240: not proportional: %s' % OK['C4'])
    OK['C5'] = b2 < 1e-4
    print('  C5 (control): the claim sigma_min(L_2) >= 1e-4 at alpha = -1: refuted by S6 (%.4e): %s' % (
        float(b2), OK['C5']))
    for k, v_ in OK.items():
        builtins.print(k, 'PASS' if v_ else 'FAIL')
    builtins.print('%d/%d (%.0f s)' % (sum(OK.values()), len(OK), time.time() - t0))
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main(selftest='--selftest' in sys.argv))
