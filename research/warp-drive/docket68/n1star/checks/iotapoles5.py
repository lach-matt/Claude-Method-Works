#!/usr/bin/env python3
"""iotapoles5: the pole orders of N_iota+(L-bar, .)^-1 at real part <= 5 in the T^2-mirror class, at the record's point,
by the Mellin transform of the iota+-normal operator; the log orders III.A Lemma 1.4 puts into E_ind; and d's ceiling
redone with them (CONSTANTS5.md, Round 4, item (ii)).

Labels: computed (exact, sympy; real roots in exact isolating intervals), deduced (the Mellin reduction, R4.1), READ
(cited lines and the record's instruments, used by import, never copied).

The operator (READ, PART-III-G2-IOTA.md:27-30): N_iota+(lam) = -2 v (v d_v - lam)(v d_v - 3/2 - S-bar) + v^2
L~(0)(omega, v d_v, d_omega). Per harmonic type it is iota5.py's model M0(D) G + v M1(D) G (divided by v), D = v d_v,
M0(x) = (x - lam) L1(x), M1 = N the indicial matrix of L~(0) (iota5.py I1, lin5.py's bases and POINT). The class
(class5.py C2): one scalar harmonic at each even l, one tensor harmonic at each even l >= 2, no vector one; so the types
are s0, s_l and t_l, l even >= 2.

  M1 (exact) The Mellin transform G-hat(zeta) = int_0^oo v^-zeta G dv/v turns D into zeta and v into the shift zeta -> zeta
     - 1, so N_iota+(lam) G = F becomes (zeta - lam) L1(zeta) G-hat(zeta) + N(zeta - 1) G-hat(zeta - 1) = F-hat(zeta):
     checked on G = v^a e^-v (G-hat = Gamma(a - zeta)) for L1, N with symbolic coefficients. Control C1: the shift taken
     as zeta + 1: the identity fails.
  M2 (exact) The free scalar model (L1 = -2(x - 3/2), N = -(x - l - 2)(x + l)), harmonic degree l: (a) the pure states
     v^(3/2) (1 + v/2)^(-k-3/2-l) F_k(-v/2), F_k = 2F1(-k, -2-2l-k; -1/2-l-k; .) terminating, solve N_iota+(3 + l + k) G
     = 0 exactly (l, k = 0, 1, 2; l = k = 0 is [Hin26]'s u_3); (b) the growing coefficient of the outgoing solution at oo,
     Gamma(2 + 2l)/(Gamma(3/2 + l) Gamma(3 + l - lam)), has exactly the zeros 3 + l + k, each simple; (c) R4.1's product
     Pi_j gives the same poles, each of order 1. Controls: C2 the constant 1 (the n = 3 value) for 3/2 in (a): the states
     fail; C3 the product with the shift lost, N(lam - i + 1): its poles are l + 2 + k, not (b)'s, and (c) fails.
  M3 (exact) L-bar at the record's point, types s0 and t2 (iota5.mats, about 2 minutes): M0 = (x - lam) L1, L1 = C - x,
     spec C - 3/2 inside spec S-bar (READ, G2-IOTA (1.4)); det N factored; the roots with 0 < Re <= 4 isolated; exactly K
     roots with Re <= 0 (the strip of R4.1); the candidates r + i (Re <= 5) listed; at every candidate but one a single
     factor N(lam0 - i) is singular, at a simple root, so the order is 1; at lam0 = 5 (s0) two are, N(4) and N(2), and
     the exact Laurent expansion of Pi_4(5 + eps)^-1 gives order 1, residue of rank 2. No root lies in spec C + Z (the
     exceptional points). Control C4: the same expansion with N(2 + eps)^-1 replaced by its adjugate: the order-1,
     rank-2 result fails.
  M4 (exact) Every even l >= 2, both types. det N_L = c (x + l)(x - l - 2) det N_Ups(x - 1) det N_C(x + 1) (READ: lin5.py
     E2) and det N_tl = c (x + l)(x - l - 2) (READ, ibid.; M3 reproduces it at l = 2). Physical roots in (0, 4]: 4 at l =
     2 only; box^Ups's plus 1: none in (0, 4] (closed form, gaugepot5.py G1: the root of Q_l above l is > l + 1 for z >
     0, exactly); box^C's minus 1: from damping5.py's sextic pk(lam, kappa) at its PARAMS, the discriminant in lam and the
     resultants with pk(lam + m), m = 1, 2, 3, and pk(5/2 + s + m), s in spec S-bar's small part, m = -1..2, are
     polynomials in kappa with no root kappa = l (l + 2), l even >= 2 (exact isolation of every real root); at l = 2
     pk(2), pk(3), pk(4) != 0 (no box^C root an integer distance from the physical 4). So every root of det N with 0 <
     Re <= 4 is simple, no two differ by 1, 2 or 3, none is exceptional, and every pole at Re <= 5 has order 1. Control
     C5: the resultant at m = 2 of the whole det N_L (physical l + 2 and box^Ups's l + 4 differ by 2): identically zero,
     so the test sees a planted coincidence.
  M5 (exact; READ III.A Lemma 1.4, PART-III-A-PREREQ.md:176-182, and F4 Lemma 2.1, PART-III-F4-ZERO.md:66-80) The log
     orders of E_ind on the narrowest reading: E' = U E_j, E_0 = E(alpha) U-bar F, E_(j+1) = E(alpha) U-bar (F U-bar (E_j
     + 1)), F = (k, 0), E(alpha) the index set of the positive roots of box^Ups(0) (dceiling5.py's census and the integer
     roots 3, 4, 5, 6, 7, closed under + N_0): at k = 2 the log order at k + w is 2w at integer w, so E_ind = E' - k has
     log order 10 at 5; at k = 1, 9. Control C6: plain unions for the extended ones: every log order 0.
  M6 (exact) The ceiling (dceiling5.py D6's per-exponent form, READ there) at l_* = 4 and at l_* = 10; its constant
     term reproduced from its parts; and, as a hypothetical reading the record does not support, III.A Proposition
     4.2's count with log order at most 2 at every exponent (n_iota <= 3 P_iota).

    python3 checks/iotapoles5.py       (about five minutes)
"""
import builtins
import os
import sys
import textwrap
import time
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
import damping5 as DP  # noqa: E402  (box^C's indicial polynomials, READ)
import iota5  # noqa: E402  (the iota+ model by type, READ)
import lin5 as L5  # noqa: E402  (bases, POINT, READ)
import dceiling5 as DC  # noqa: E402  (round 3: the root census of box^Ups(0))


def print(*a, **k):  # noqa: A001  (every printed line within 121 characters)
    for line in ' '.join(str(x) for x in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


v, zeta, a_, lam, eps, x = sp.symbols('v zeta a lam eps x')
OK = {}


# ------------------------------------------------------------------------------------------------ M1 the transform
def mellin_check(shift=-1):
    """Mellin[(D - lam) L1(D) G + v N(D) G] = (zeta - lam) L1(zeta) Ghat(zeta) + N(zeta + shift) Ghat(zeta + shift)"""
    p0, p1, q0, q1, q2 = sp.symbols('p0 p1 q0 q1 q2')
    L1 = lambda y: p0 + p1 * y                                        # noqa: E731
    N = lambda y: q0 + q1 * y + q2 * y ** 2                            # noqa: E731
    G = v ** a_ * sp.exp(-v)
    D = lambda f: sp.expand(v * sp.diff(f, v))                         # noqa: E731
    LG = sp.expand(D(D(G)) * p1 + D(G) * (p0 - lam * p1) - lam * p0 * G)        # (D - lam) L1(D) G
    NG = sp.expand(v * (q2 * D(D(G)) + q1 * D(G) + q0 * G))
    tot = sp.expand((LG + NG) / sp.exp(-v))                            # a sum of c v^(a + n)
    lhs = sum(c * sp.gamma(a_ + sp.Poly(m, v).degree() - zeta) if False else 0 for c, m in [])
    lhs = 0
    for term in sp.Add.make_args(tot):
        c, pw = term.as_independent(v)
        e = sp.powsimp(pw).as_base_exp()[1] if pw != 1 else 0
        lhs += c * sp.gamma(e - zeta)                                  # int v^(e - zeta) e^-v dv/v
    Gh = lambda zz: sp.gamma(a_ - zz)                                  # noqa: E731
    rhs = (zeta - lam) * L1(zeta) * Gh(zeta) + N(zeta + shift) * Gh(zeta + shift)
    return sp.simplify(sp.gammasimp(lhs - rhs)) == 0


# ------------------------------------------------------------------------------------------------ M2 the free model
def free_state(l, k, c=sp.Rational(3, 2)):
    lm = 3 + l + k
    z = -v / 2
    F = sum(sp.rf(-k, n) * sp.rf(-2 - 2 * l - k, n) / (sp.rf(-sp.Rational(1, 2) - l - k, n) * sp.factorial(n)) * z ** n
            for n in range(k + 1))
    G = v ** sp.Rational(3, 2) * (1 + v / 2) ** (-k - sp.Rational(3, 2) - l) * F
    D = lambda f: v * sp.diff(f, v)                                    # noqa: E731
    res = -2 * (D(D(G)) - (lm + c) * D(G) + lm * c * G) - v * (D(D(G)) - 2 * D(G) - l * (l + 2) * G)
    return sp.simplify(res / (v ** sp.Rational(3, 2) * (1 + v / 2) ** (-k - sp.Rational(7, 2) - l))) == 0


def gamma_zeros(l, top=5):
    """zeros of Gamma(2+2l)/(Gamma(3/2+l) Gamma(3+l-lam)) with 2 <= lam <= top, and their orders"""
    out = []
    for lm in range(2, top + 1):
        f = 1 / sp.gamma(3 + l - lam)
        val = sp.limit(f, lam, lm)
        if val == 0:
            der = sp.limit(sp.diff(f, lam), lam, lm)
            out.append((lm, 1 if der != 0 else 2))
    return out


def pole_orders_scalar(L1, N, roots, top=5, shift_bug=False):
    """R4.1 for K = 1: poles lam0 = r + i (i >= 1) of Pi_j^-1 with Re lam0 <= top, and their orders (exact)"""
    out = {}
    cand = sorted({r + i for r in roots for i in range(0, 6) if 0 < r + i <= top})
    for l0 in cand:
        j = 1
        while not (0 < l0 - j < sp.Rational(3, 2)):
            j += 1
        Pinv = sp.Integer(1)
        for i in range(1, j + 1):
            Nf = N(lam - i + 1) if shift_bug else N(lam - i)
            Pinv *= L1(lam - i + 1) / Nf
        Pinv = sp.cancel(Pinv)
        m = 0
        while sp.limit(Pinv * (lam - l0) ** m, lam, l0) in (sp.oo, -sp.oo, sp.zoo):
            m += 1
        if m:
            out[l0] = m
    return out


# ------------------------------------------------------------------------------------------------ M3 L-bar by type
def real_roots_in(poly, lo, hi):
    P = sp.Poly(poly, x)
    out = []
    for f, mult in sp.factor_list(P)[1]:
        for (a, b), mm in f.intervals(eps=sp.Rational(1, 10 ** 12)):
            if b > lo and a <= hi:
                out.append((sp.Rational(a), sp.Rational(b), mult * mm, f))
    return out


def complex_parts(poly):
    """for each irreducible factor: (degree, #real roots, real parts of non-real roots as one exact interval or None)"""
    res = []
    for f, mult in sp.factor_list(sp.Poly(poly, x))[1]:
        n_real = f.count_roots()
        if f.degree() - n_real == 2:
            cs = f.all_coeffs()
            ssum = -sp.Rational(cs[1]) / sp.Rational(cs[0])
            rr = [sp.Rational(a + b) / 2 for (a, b), _ in f.intervals(eps=sp.Rational(1, 10 ** 12))]
            res.append((f.degree(), n_real, (ssum - sum(rr)) / 2))
        else:
            res.append((f.degree(), n_real, None if n_real == f.degree() else 'more'))
    return res


def laurent_order(Pinv):
    m = 0
    while True:
        lim = (Pinv * eps ** m).applyfunc(lambda q: sp.limit(q, eps, 0))
        if all(q.is_finite for q in lim):
            return m, lim.rank()
        m += 1


def type_analysis(typ, verbose_label):
    t0 = time.time()
    M0, M1, ok = iota5.mats(4, typ, L5.Lbar)
    X, Lam = iota5.X, iota5.Lam
    M0 = M0.subs(L5.POINT).applyfunc(sp.expand).subs(X, x)
    M1 = M1.subs(L5.POINT).applyfunc(sp.expand).subs(X, x)
    K = M0.shape[0]
    L1 = M0.applyfunc(lambda q: sp.cancel(q / (x - Lam)))
    C = (L1 + x * sp.eye(K)).applyfunc(sp.expand)
    struct = ok and not L1.has(Lam) and not C.has(x)
    sbar = {Fr(0), Fr(99, 10000), Fr(1, 100), Fr(1, 50), Fr(499995117187500, 10 ** 9), Fr(500000), Fr(10 ** 6)}
    eig = C.eigenvals()
    spec_ok = all(Fr(str(sp.Rational(e - sp.Rational(3, 2)))) in sbar for e in eig)
    detN = sp.factor(M1.det())
    num = sp.numer(sp.together(detN))
    parts = complex_parts(num)
    deg = sp.Poly(num, x).degree()
    left = len(real_roots_in(num, -10 ** 9, 0))
    for d_, nr, re in parts:
        if re not in (None, 'more') and re <= 0:
            left += 2
    pos = [(a, b, m) for a, b, m, f in real_roots_in(num, 0, 4) if a > 0 or b > 0]
    pos = [(a, b, m) for a, b, m in pos if b > 0 and a <= 4]
    nonreal_in = any(re not in (None, 'more') and 0 < re <= 4 for _, _, re in parts)
    simple = all(m == 1 for _, _, m in pos)
    # candidates and coincidences (intervals of width 1e-12, exact where the root is rational)
    cand = []
    for a, b, m in pos:
        for i in range(1, 6):
            if a + i <= 5:
                cand.append((a + i, b + i, (a, b), i))
    groups = []
    for c in cand:
        for g in groups:
            if not (c[1] < g[0][0] or c[0] > g[0][1]):
                g.append(c)
                break
        else:
            groups.append([c])
    exc = sorted({e + n for e in eig for n in range(1, 4) if sp.re(e) + n <= 5})
    exc_clear = all(not (a - e) .is_integer if a == b else
                    all(not (a <= e + n <= b) for n in range(-5, 6)) for a, b, m in pos for e in eig)
    orders = {}
    for g in groups:
        if len(g) == 1:
            orders[(float(g[0][0]), float(g[0][1]))] = (1, 1)
        else:
            l0 = g[0][0]
            assert all(c[0] == c[1] for c in g)                        # rational roots here: exact
            j = 1
            while not (0 < l0 - j < sp.Rational(3, 2)):
                j += 1
            Pinv = sp.eye(K)
            for i in range(j, 0, -1):
                Pinv = (Pinv * M1.subs(x, l0 + eps - i).inv() * L1.subs(x, l0 + eps - i + 1)).applyfunc(sp.cancel)
            orders[(float(l0), float(l0))] = laurent_order(Pinv)
    info = dict(K=K, struct=struct, spec_ok=spec_ok, eig=eig, detN=detN, left=left, deg=deg, pos=pos,
                nonreal_in=nonreal_in, simple=simple, groups=groups, orders=orders, exc=exc, exc_clear=exc_clear,
                M1=M1, L1=L1, time=time.time() - t0)
    return info


def control_adjugate(info):
    """C4: at lam0 = 5 (s0) replace N(2 + eps)^-1 by its adjugate (the pole at 2 removed)"""
    M1, L1, K = info['M1'], info['L1'], info['K']
    l0, j = 5, 4
    Pinv = sp.eye(K)
    for i in range(j, 0, -1):
        Ni = M1.subs(x, l0 + eps - i)
        Fi = Ni.adjugate() if i == 3 else Ni.inv()
        Pinv = (Pinv * Fi * L1.subs(x, l0 + eps - i + 1)).applyfunc(sp.cancel)
    return laurent_order(Pinv)


# ------------------------------------------------------------------------------------------------ M4 every even l
def even_l_hits(polyK, lmax_check=None):
    """real roots kappa of a polynomial in kappa; the even l >= 2 with l (l + 2) among them (exact)"""
    P = sp.Poly(sp.expand(polyK), DP.K)
    if P.is_zero:
        return 'identically zero'
    hits = []
    for f, _ in sp.factor_list(P)[1]:
        if f.degree() == 0:
            continue
        for (a, b), _ in f.intervals(eps=sp.Rational(1, 10 ** 6)):
            if b < 8:
                continue
            l0 = int(sp.floor(sp.sqrt(max(a, 0) + 1) - 1))
            for lv in range(max(l0 - 2, 2), l0 + 3):
                if lv % 2 == 0 and a <= lv * (lv + 2) <= b and f.eval(lv * (lv + 2)) == 0:
                    hits.append(lv)
    return hits


def m4():
    pk = sp.expand(DP.polys(4, sp.Rational(2, 3))[0].subs(DP.PARAMS))
    L = DP.lam
    disc = sp.discriminant(pk, L)
    res = {m: sp.resultant(pk, pk.subs(L, L + m), L) for m in (1, 2, 3)}
    small = [Fr(0), Fr(99, 10000), Fr(1, 100), Fr(1, 50)]
    excs = {(s, m): pk.subs(L, sp.Rational(5, 2) + sp.Rational(s.numerator, s.denominator) + m)
            for s in small for m in (-1, 0, 1, 2)}
    out = {'disc': even_l_hits(disc)}
    out.update({'res m=%d' % m: even_l_hits(r) for m, r in res.items()})
    out['exceptional'] = sorted({h for p in excs.values() for h in even_l_hits(p)})
    pk2 = pk.subs(DP.K, 8)
    out['l=2 integer box^C roots 2, 3, 4'] = [pk2.subs(L, n) for n in (2, 3, 4)]
    # box^Ups: Q_l(s) = s^2 - (2 + 2k + z) s + k (k + 1) + z k; its lower root s_- exceeds l (l + 1) for z > 0
    z, kap, l = sp.symbols('z kappa l', positive=True)
    s_minus = ((2 + 2 * kap + z) - sp.sqrt((z + 2) ** 2 + 4 * kap)) / 2
    ds = sp.simplify(sp.diff(s_minus, z))
    at0 = sp.simplify(s_minus.subs(z, 0).subs(kap, l * (l + 2)) - l * (l + 1))
    pos_der = sp.simplify(1 - (z + 2) / sp.sqrt((z + 2) ** 2 + 4 * kap)).is_positive
    out['box^Ups'] = (at0 == 0, pos_der, ds)
    # the l = 2 right roots of pk (box^C), for the s2 candidate list; and the counts at the line 2 (Routh, damping5)
    roots2 = [(sp.Rational(a) - 1, sp.Rational(b) - 1) for (a, b), _ in sp.Poly(pk2, L).intervals(
        eps=sp.Rational(1, 10 ** 12)) if b > 1]
    out['l=2 det N roots from box^C in (0, 4]'] = [(float(a), float(b)) for a, b in roots2 if a <= 4]
    out['right of 2 at l = 2 (Routh)'] = DP.right_of(pk2, 2)
    # control C5: the whole det N_L at symbolic l, m = 2: physical l + 2 against box^Ups's l + 4
    phys = (x + l) * (x - l - 2) * (x - l - 4)            # the two factors the control needs
    out['C5'] = sp.resultant(phys, phys.subs(x, x + 2), x) == 0
    return out, roots2


# ------------------------------------------------------------------------------------------------ M5 Lemma 1.4
def lemma14(roots, k, top, extended=True):
    """log orders of III.A Lemma 1.4's E' (exponents as exact Fractions) up to real part top"""
    def closure(pts):
        out = {}
        for z0, lo in pts.items():
            n = 0
            while z0 + n <= top:
                out[z0 + n] = max(out.get(z0 + n, -1), lo)
                n += 1
        return out

    def ubar(A, B):
        out = dict(A)
        for z0, lo in B.items():
            if z0 in out:
                out[z0] = (out[z0] + lo + 1) if extended else max(out[z0], lo)
            else:
                out[z0] = lo
        return out
    Ea = closure({r: 0 for r in roots})
    F = closure({Fr(k): 0})
    E = ubar(Ea, F)
    U = dict(E)
    for _ in range(int(top) + 3):
        sh = {z0 + 1: lo for z0, lo in E.items() if z0 + 1 <= top}
        E = ubar(Ea, ubar(F, sh))
        for z0, lo in E.items():
            U[z0] = max(U.get(z0, -1), lo)
    return U


def m5():
    census, ints, _ = DC.root_census(Fr(4, 10 ** 6), top=10)
    roots = sorted({Fr(n) + Fr(str(sp.Rational(str(float((lo + hi) / 2))))) for _, _, n, lo, hi in census} |
                   {Fr(i) for i in range(3, 11)})
    out = {}
    for k in (1, 2):
        U = lemma14(roots, k, Fr(5 + k))
        Uc = lemma14(roots, k, Fr(5 + k), extended=False)
        Eind = {z0 - k: lo for z0, lo in U.items() if z0 > k}
        ints_ = {int(w): Eind[w] for w in sorted(Eind) if w.denominator == 1}
        out[k] = (max(lo for w, lo in Eind.items() if w <= 5), ints_, max(Uc.values()))
    return out


# ------------------------------------------------------------------------------------------------ M6 the ceiling
def m6():
    # READ: dceiling5.out D4, D6 and CONSTANTS5.md R3.1 (the reader's vouched numbers)
    R2, R3 = 1401250931461121, 1401251031977897
    La, Lb, K, W = 53244736, 53244734, 106489469, 1470302
    P_i, P_W = 85025784, 85025783
    B_rec, C_rec, A_rec = 4527175422273024, 2986797742916004835692267122688, 28864786304360710
    A = 3 * (R2 + R3) + La * (3 * P_W + 11 + P_i + 15 * W) + Lb * (15 * W + 58)
    ok_A = A == A_rec and La * P_i == B_rec
    at = {ls: A_rec + B_rec * 1 + C_rec * (ls + 1) for ls in (4, 10)}
    hyp = 3 * (R2 + R3) + La * (3 * P_W + 11 + 3 * P_i + 15 * W) + Lb * (15 * W + 58)
    return ok_A, at, hyp, (La, K + 1)


def main():
    t0 = time.time()
    print('iotapoles5: pole orders of N_iota+(L-bar, .)^-1 at Re <= 5 in the class; E_ind\'s Lemma 1.4 log orders; the '
          'ceiling')
    # M1
    ok1 = mellin_check()
    OK['M1'] = ok1
    OK['C1'] = not mellin_check(shift=+1)
    print('  M1: Mellin[(D - lam) L1(D) G + v N(D) G] = (zeta - lam) L1(zeta) Ghat(zeta) + N(zeta - 1) Ghat(zeta - 1) on G '
          '= v^a e^-v, L1, N symbolic: %s' % ok1)
    print('  C1 (control): the shift taken as zeta + 1: the identity fails: %s' % OK['C1'])
    # M2
    st = {(l, k): free_state(l, k) for l in range(3) for k in range(3)}
    gz = {l: gamma_zeros(l) for l in range(4)}
    L1f = lambda y: -2 * (y - sp.Rational(3, 2))                        # noqa: E731
    pz = {}
    for l in range(4):
        Nf = lambda y, l=l: -(y - l - 2) * (y + l)                     # noqa: E731
        pz[l] = pole_orders_scalar(L1f, Nf, [l + 2] if l + 2 <= 4 else [], top=5)
    agree = all(sorted(pz[l].items()) == sorted(gz[l]) for l in range(4))
    OK['M2'] = all(st.values()) and agree and all(o == 1 for l in pz for o in pz[l].values())
    print('  M2: free model: the pure states solve N_iota+(3 + l + k) G = 0 for l, k = 0, 1, 2: %s; Gamma-coefficient zeros '
          'at Re <= 5 (lam, order): %s; R4.1 product poles: %s; agree: %s' % (all(st.values()), gz,
                                                                           {l: pz[l] for l in pz}, agree))
    OK['C2'] = not any(free_state(l, k, c=1) for l in range(2) for k in range(2))
    print('  C2 (control): the constant 1 for 3/2: no state solves: %s' % OK['C2'])
    pzb = {}
    for l in range(3):
        Nf = lambda y, l=l: -(y - l - 2) * (y + l)                     # noqa: E731
        pzb[l] = pole_orders_scalar(L1f, Nf, [l + 2], top=5, shift_bug=True)
    OK['C3'] = not all(sorted(pzb[l].items()) == sorted(gz[l]) for l in range(3))
    print('  C3 (control): the product with N(lam - i + 1): poles %s, not M2\'s: %s' % (pzb, OK['C3']))
    # M3
    res = {}
    for typ in ('s0', 't2'):
        info = type_analysis(typ, typ)
        res[typ] = info
        ords = info['orders']
        print('  M3 %s (K = %d, %.0f s): M0 = (x - lam)(C - x), C constant: %s; spec C - 3/2 = %s, inside spec S-bar: %s; '
              'det N = %s' % (typ, info['K'], info['time'], info['struct'],
                              sorted(float(e - sp.Rational(3, 2)) for e in info['eig']), info['spec_ok'], info['detN']))
        print('      roots with Re <= 0: %d of %d (K = %d); roots in (0, 4]: %s, all simple: %s, none non-real: %s' % (
            info['left'], info['deg'], info['K'], ['[%.10f, %.10f]' % (a, b) for a, b, _ in info['pos']],
            info['simple'], not info['nonreal_in']))
        print('      candidates lam0 = r + i, Re <= 5 (interval: order, residue rank): %s; exceptional points spec C + '
              '{1, 2, 3} at Re <= 5: %s, no root at an integer distance from spec C: %s' % (
                  {'[%.7f, %.7f]' % k_: o for k_, o in sorted(ords.items())}, [float(e) for e in info['exc']],
                  info['exc_clear']))
    s0, t2 = res['s0'], res['t2']
    OK['M3'] = (s0['struct'] and s0['spec_ok'] and s0['left'] == s0['K'] and s0['simple'] and not s0['nonreal_in']
                and s0['exc_clear'] and s0['orders'][(5.0, 5.0)] == (1, 2)
                and all(o[0] == 1 for o in s0['orders'].values()) and len(s0['orders']) == 7
                and t2['struct'] and t2['left'] == 1 and t2['orders'] == {(5.0, 5.0): (1, 1)})
    c4 = control_adjugate(s0)
    OK['C4'] = c4 != (1, 2)
    print('  C4 (control): lam0 = 5 at s0 with N(2 + eps)^-1 replaced by its adjugate: (order, rank) = %s, not (1, 2): %s'
          % (c4, OK['C4']))
    # M4
    out4, roots2 = m4()
    hits_none = all(out4[k_] == [] for k_ in ('disc', 'res m=1', 'res m=2', 'res m=3', 'exceptional'))
    OK['M4'] = (hits_none and all(q != 0 for q in out4['l=2 integer box^C roots 2, 3, 4'])
                and out4['box^Ups'][0] and out4['box^Ups'][1] and out4['right of 2 at l = 2 (Routh)'] == 3)
    OK['C5'] = out4['C5']
    print('  M4: every even l >= 2: even l with kappa = l (l + 2) a root of: disc %s; Res m = 1, 2, 3: %s, %s, %s; '
          'pk(5/2 + s + m): %s; at l = 2 pk(2), pk(3), pk(4) nonzero: %s; box^Ups (s_-(0) = l (l + 1), increasing in z): '
          '%s, %s; box^C roots right of 2 at l = 2 (Routh): %d; det N_L roots from box^C in (0, 4] at l = 2: %s' % (
              out4['disc'], out4['res m=1'], out4['res m=2'], out4['res m=3'], out4['exceptional'],
              all(q != 0 for q in out4['l=2 integer box^C roots 2, 3, 4']), out4['box^Ups'][0], out4['box^Ups'][1],
              out4['right of 2 at l = 2 (Routh)'], out4['l=2 det N roots from box^C in (0, 4]']))
    print('  C5 (control): physical l + 2 against box^Ups\'s l + 4, resultant at m = 2 identically zero: %s' % OK['C5'])
    # M5
    out5 = m5()
    OK['M5'] = out5[2][0] == 10 and out5[1][0] == 9
    OK['C6'] = all(out5[k_][2] == 0 for k_ in (1, 2))
    for k_ in (1, 2):
        print('  M5: III.A Lemma 1.4 with F = (%d, 0): E_ind = E\' - %d has log order %d at Re <= 5; at the integers %s' % (
            k_, k_, out5[k_][0], out5[k_][1]))
    print('  C6 (control): plain unions for the extended ones: largest log order %s: %s' % (
        [out5[k_][2] for k_ in (1, 2)], OK['C6']))
    # M6
    ok_A, at, hyp, (La, K1) = m6()
    OK['M6'] = ok_A
    print('  M6: dceiling5 D6\'s constant term rebuilt from R2, R3, P_W, P_iota, W and the level counts: %s; per exponent, '
          'L_0 = 1: d <= %.6e (l_* = 4), %.6e (l_* = 10), + %d X_7 + %d c\'; N = 21 d + 6 <= %.4e, %.4e + ...' % (
              ok_A, at[4], at[10], La, K1, 21 * at[4] + 6, 21 * at[10] + 6))
    print('      hypothetical (not the record\'s bound): log order <= 2 at every exponent of E^flat, n_iota <= 3 P_iota: '
          'd <= %d + %d X_7 + %d c\' = %.6e + ...; N <= %.4e + ...' % (hyp, La, K1, hyp, 21 * hyp + 6))
    print('  (%.0f s)' % (time.time() - t0))
    for k_, val in OK.items():
        builtins.print(k_, 'PASS' if val else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
