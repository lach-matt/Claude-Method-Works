#!/usr/bin/env python3
"""puregauge5.py -- [Hin26] Proposition 6.18 (4)-(7) in five dimensions: the pure gauge generalized zero energy states
built on the growing indicial roots of box^Ups(0) that carry no symmetry (N1STAR-PROOF.md section 10.30; ROUTES-OPEN.md
4.31; D84, D85).  Labels: computed (exact, sympy), deduced, READ.

[Hin26] (arXiv:2606.28253v2) Proposition 6.18 (4)-(7) records "the remaining four classes of pure gauge solutions"
(p. 130), built on the indicial roots mu of box^Ups(0) below -1 and the s2 root -1: (4) the s0 root -lam^Ups_s0,1,
(5) the sl roots -lam^Ups_sl,l+j, l = 1, 2, 3, j = 0, 1, (6) the sl roots -l + 1, 2 <= l <= 5, (7) the vl roots -l, l =
2, 3, 4.  Each gives a stationary omega in ker box^Ups with leading term an indicial solution omega-bar at rho^mu, its
symmetric gradient nonzero at rho^(mu + 1) "since N(delta*(0), lam - 1) is injective" (p. 134), and generalized states
t*^k omega + sum_i k!/(k - i)! t*^(k - i) omega-breve^i, omega-breve^i at rho^(mu - i), for k up to 2, 2, 5 - l and 4
- l.  The leading terms obey the recursion A0 omega-breve^i = -A1 omega-breve^(i - 1) of the Minkowskian model,
box^Ups = A0 + A1 d_t* + A2 d_t*^2 (his (6.4a), (6.6)), A2 = -g^00 = 0 on Minkowski.  Here on 4+1 Minkowski with E^Ups
at the trace weight 2/3, c = r^-1 dt (10.15), in polar coordinates and in his splitting (2.37b), (2.43): s0 and sl
1-forms (a S, b S, c dS) on d xbar^0, d xbar^1, r T*S^3 (xbar^0 = t + r, xbar^1 = t - r = t*), S the zonal harmonic,
and vl 1-forms c r V, V = P(x^3, x^4)(x^1 dx^2 - x^2 dx^1)/r^(l + 1), P harmonic of degree l - 1; three-plus-one
Minkowski (trace weight 1) is the control.  z = 4 e gam^2 in both dimensions (his z in four dimensions is z/4).

  J1 (computed, exact) The indicial families.  N0(lam) = rho^-2 A0 and N1(lam) = rho^-1 A1 on rho^lam times each pure
     type, s0, sl (l = 1, ..., 5) and vl (l = 1, ..., 4), the same at two generic angles, and A2 = 0.  Four dimensions:
     N0 is his Lemma 6.6 matrix entry by entry (p. 117), N0_v1 = -lam^2 + lam + 2 and N1_v1 = -2 (lam - 1 - gam) (p.
     134), N1 = -2 (lam - 1) + 2 S-bar with S-bar free of lam.  Five dimensions: det N0 is 10.15(i)'s polynomial (ratio
     1), N1 = -2 (lam - 3/2) + 2 S-bar, N0_vl = -(lam + l)(lam - l - 2) and N1_vl = -2 (lam - 3/2 - gam).  Control: his
     four-dimensional matrices claimed in five dimensions.
  J2 (computed, exact) The classes.  Five dimensions, every l: Q(l(l + 1)) = l z and Q((l + 1)(l + 2)) = -(l + 2) z, so
     for z > 0 the two negative roots of Q lie in (-l - 1, -l) and below -l - 1, mu_l,0 = -l - l z/(2 (l + 1)(2l + 1))
     + O(z^2) and mu_l,1 = -l - 1 - (l + 2) z/(2 (l + 1)(2l + 3)) + O(z^2) (computed for l <= 6, with the roots at z =
     1/100); mu_s0 = (1 - (9 + 4z)^(1/2))/2 = -1 - z/3 + O(z^2) in (-2, -1); sl -l + 1 and vl -l at every z; and the
     roots <= 0 are exactly these and the Killing 0 (s0, s1) and -1 (v1).  So his four classes, his ranges of l and
     footnote 76's direction (each root just below its integer) carry over.  Four dimensions: his -lam_s0,1 = -(1 +
     z)^(1/2), his lam_sl,l and lam_sl,l+1 as the roots of the quartic factor, and his first-order coefficient 2/(2l +
     1) in his z, all from J1's matrices.  Control: z < 0, where the roots move the other way.
  J3 (computed, exact) delta-bar* on indicial solutions.  N(delta-bar*(0), lam) fails to be injective only at 0 (s0,
     s1) and -1 (v1) -- the real roots of det(M^T M), M its matrix at two generic angles -- in five dimensions as in
     four, never at sl (2 <= l <= 5) or vl (2 <= l <= 4; every l by his Killing-form argument, p. 67, deduced): so
     every class root has symmetric gradient nonzero at rho^(mu + 1).  Four
     dimensions: his (2.46a), (2.46b) and (2.46c) entry by entry (p. 67), and his remark after them.  Control: v1
     claimed injective at -1 (the rotations).
  J4 (computed, exact) No resonance.  For each class root mu and each shift its construction meets -- mu - k for the
     t*-recursion, k up to his range; mu + 2 for the stationary correction on Tangherlini, whose zero energy operator
     differs from Minkowski's in rho^4 Diff^2_b (10.28(i)), mu + 1 in four dimensions; and mu itself, simple -- the
     resultant against the type's polynomial has least positive zero exactly z = 4 (four dimensions 3).  At z = 4 the
     s0 class root -2 meets the Killing root 0 under the shift +2, so 4 is sharp; at z = 3 in four dimensions only the
     s0 partner root 2 meets (2 - 2 = 0, and 2 is double), the class root -2 meets nothing, so 3 is not sharp.  At z = 0
     the coincidences e_Ups > 0 removes (his p. 81 and Remark 6.7) are exactly: at sl, mu_l,0 - 1 = mu_l,1, mu_l,1 + 2 =
     -l + 1, and -l + 1 - k = mu_l,k-1 for k <= min(2, 5 - l); four dimensions, mu + 1 = 0 at s0, and at sl mu_l,0 - 1 =
     mu_l,1, mu_l,1 + 1 = mu_l,0, mu_l,0 + 1 = -l + 1 and the same -l + 1 - k; none at vl at any z.  Controls: z = 0
     claimed free of them; the range claimed 0 < z < 5.
  J5 (computed, exact) The states.  On Minkowski t*^k omega-bar + sum_i k!/(k - i)! t*^(k - i) omega-breve-bar^i, by J1's
     recursion, is in ker box^Ups at every class's largest k: exactly in e and gam at the integer roots (sl -l + 1, vl
     -l; both dimensions), and for s0 and the roots of Q with mu a symbol modulo its polynomial at (e, gam) = (1/3, 1/2)
     and (1/7, 2/5), each polynomial irreducible over Q (so nonzero modulo it is nonzero at every root).  At vl,
     omega-breve-bar^i = kappa_i r^i omega-bar with kappa_i = prod_(j <= i) (2l + 2j + 1 + 2 gam)/(j (2l + j + 2)) (four
     dimensions 2 (l + j + gam)/(j (2l + j + 1))), l <= 4 and i <= 3: at l = 1, 10.29's 1 + 2 gam/5 and his 1 + gam/2 (p.
     134).  Control: the factor k!/(k - i)! dropped.
  J6 (computed, exact) What e_Ups > 0 removes, on Minkowski.  At e = 0 (z = 0; gam = 1/3 and 2/7; both dimensions) J4's
     t*-recursion coincidences: mu_l,0 = -l's first step meets mu_l,1 = -l - 1 and is obstructed, rank N0(-l - 1) = 2
     against 3 with its right side (l = 1, 2, 3), so a logarithm is forced; -l + 1's first step meets -l and is
     solvable, rank 2 with its right side (l = 2, 3, 4), and its second meets -l - 1 with an obstruction of degree 1 in
     the first step's kernel coefficient alpha (l = 2, 3), so one alpha removes it (five dimensions, l = 2, gam = 1/3: 2
     (15 alpha - 17)/63).  The stationary correction's coincidences need Tangherlini's sources at e = 0 and are not
     computed.  Control: -l + 1's first step claimed obstructed.

Deduced, not computed here (N1STAR-PROOF.md 10.30): his Proposition 6.18 (4)-(7) in five dimensions on Tangherlini, by
his proof with J2-J5, on 10.29(a) (his Lemma 6.13 there, on the readings of 10.20), his Lemma 2.15 and 10.28(i): the same
four classes, ranges and index sets (no logarithm in the leading terms), the stationary correction at rho^(mu + 2) where
his is at rho^(mu + 1), the leading term of each h spanning ker N(L-bar(0), mu + 1) where that root is simple
(10.24(iv)).

READ.  [Hin26] pp. 19 ((1.27)-(1.29)), 67 ((2.43)-(2.46c) and the remark after them), 113 (Lemma 6.1, (6.4a), (6.5)-
(6.6)), 117-118 (Lemma 6.6, (6.17a)-(6.17b), Remark 6.7), 121 (Proposition 6.12), 128-134 (section 6.5.2: Proposition
6.18, footnotes 74-76, Remark 6.19, the proof), 149-151 (Lemma 8.4 and its proof), 158 (section 8.5); alphaXiv,
2026-10-23.

sympy.  python3 puregauge5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time
from functools import lru_cache

import sympy as sp

from damping5 import Checklist
from genstates5 import geo, dstar, boxU, TRIG, t, r, ch, th, ph, gU, eU
from zstates5 import poly5, lam, z

TRIG2 = {sp.sin(ch): sp.Rational(5, 13), sp.cos(ch): sp.Rational(12, 13), sp.sin(th): sp.Rational(8, 17),
         sp.cos(th): sp.Rational(15, 17), sp.sin(ph): sp.Rational(3, 5), sp.cos(ph): sp.Rational(4, 5)}
mu = sp.Symbol("mu")
e, g = eU, gU
LMAX = {"s": 5, "v": 4}
# his ranges (p. 130-131): the class, its types and the largest k of the generalized state
CLASSES = [("s0", 0, "q", 2)] + [("s", l, "q", 2) for l in (1, 2, 3)] + [("s", l, -l + 1, 5 - l) for l in (2, 3, 4, 5)] \
    + [("v", l, -l, 4 - l) for l in (2, 3, 4)]


def harm(n, l):
    """the zonal scalar harmonic of degree l: U_l(cos chi) on S^3, P_l(cos theta) on S^2"""
    return sp.chebyshevu(l, sp.cos(ch)) if n == 4 else sp.legendre(l, sp.cos(th))


def vphi(n, l):
    """the d phi component of a co-closed vector harmonic of degree l on the sphere: on S^3 P(x^3, x^4)(x^1 dx^2 - x^2
    dx^1)/r^(l + 1), P = Re (x^4 + i x^3)^(l - 1) harmonic; on S^2 (x cross grad (r^l P_l))/r^(l + 1)"""
    if n == 4:
        a, b, m = sp.cos(ch), sp.sin(ch) * sp.cos(th), l - 1
        P = sum(sp.binomial(m, j) * a**(m - j) * b**j * (-1)**(j // 2) for j in range(0, m + 1, 2))
        return sp.expand(P * sp.sin(ch)**2 * sp.sin(th)**2)
    x = sp.Symbol("x")
    return sp.sin(th)**2 * sp.diff(sp.legendre(l, x), x).subs(x, sp.cos(th))


def basis(n, typ, l):
    """[Hin26] (2.43): s0 (a, b), sl (a S, b S, c dS) on d xbar^0 = dt + dr, d xbar^1 = dt - dr, r T*S; vl c r V"""
    N = n + 1
    z0 = [0] * (N - 2)
    if typ == "s0":
        return [[1, 1] + z0, [1, -1] + z0]
    if typ == "s":
        S = harm(n, l)
        return [[S, S] + z0, [S, -S] + z0, [0, 0, r * sp.diff(S, ch if n == 4 else th)] + [0] * (N - 3)]
    return [[0] * (N - 1) + [r * vphi(n, l)]]


def ev(q, P, rv=1):
    return sp.cancel(sp.sympify(q).subs(P).subs(r, rv))


def decompose(F, n, typ, l, P):
    """the components of a 1-form of pure type at r = 1 and the angles P, and whether the rest vanishes"""
    N = n + 1
    Fv = [ev(q, P) for q in F]
    if typ == "v":
        return [sp.cancel(Fv[N - 1] / ev(vphi(n, l), P))], all(q == 0 for q in Fv[:N - 1])
    S = ev(harm(n, l), P) if typ == "s" else 1
    out = [sp.cancel((Fv[0] + Fv[1]) / (2 * S)), sp.cancel((Fv[0] - Fv[1]) / (2 * S))]
    if typ == "s0":
        return out, all(q == 0 for q in Fv[2:])
    out.append(sp.cancel(Fv[2] / ev(sp.diff(harm(n, l), ch if n == 4 else th), P)))
    return out, all(q == 0 for q in Fv[3:])


@lru_cache(maxsize=None)
def families(n, typ, l):
    """N0, N1 (matrices in lam) of box^Ups on rho^lam times the basis, at two angles; clean: pure type, A1 stationary,
    the two angles agreeing"""
    G = geo(n, True)
    cols0, cols1, clean = [], [], True
    for E in basis(n, typ, l):
        w = [r**(-lam) * q for q in E]
        F0 = boxU(w, G)
        F1 = [a - (t - r) * b for a, b in zip(boxU([(t - r) * q for q in w], G), F0)]
        res = []
        for P in (TRIG, TRIG2):
            c0, k0 = decompose(F0, n, typ, l, P)
            c1, k1 = decompose([q.subs(t, 0) for q in F1], n, typ, l, P)
            c1b, k2 = decompose([q.subs(t, 3) for q in F1], n, typ, l, P)
            clean &= k0 and k1 and k2 and all(sp.cancel(a - b) == 0 for a, b in zip(c1, c1b))
            res.append((c0, c1))
        clean &= all(sp.cancel(a - b) == 0 for a, b in zip(res[0][0] + res[0][1], res[1][0] + res[1][1]))
        cols0.append(res[0][0])
        cols1.append(res[0][1])
    return sp.Matrix(cols0).T.applyfunc(sp.expand), sp.Matrix(cols1).T.applyfunc(sp.expand), clean


def a2_zero(n, typ, l):
    """A2 = -g^00 vanishes on Minkowski: box((t - r)^2 w) = (t - r)^2 A0 w + 2 (t - r) A1 w"""
    G = geo(n, True)
    E = basis(n, typ, l)[0]
    w = [r**(-lam) * q for q in E]
    F0 = boxU(w, G)
    F1 = [a - (t - r) * b for a, b in zip(boxU([(t - r) * q for q in w], G), F0)]
    F2 = boxU([(t - r)**2 * q for q in w], G)
    return all(ev(a - (t - r)**2 * b - 2 * (t - r) * c, TRIG).subs(t, 2) == 0 for a, b, c in zip(F2, F0, F1))


def his66(typ, l):
    """[Hin26] Lemma 6.6 (p. 117): N(box^Ups, lam) in four dimensions, in the splitting (2.43)"""
    if typ == "v":
        return sp.Matrix([[-lam**2 + lam + l * (l + 1)]])
    if typ == "s0":
        base = sp.Matrix([[1, -1], [-1, 1]])
        gm = sp.Matrix([[-(1 + e) * lam + 2 * e, -(1 - e) * lam - 2 * e],
                        [(1 - e) * lam + 2 * e, (1 + e) * lam - 2 * e]])
        return (-lam**2 + lam) * sp.eye(2) + base + g * gm
    L = l * (l + 1)
    base = sp.diag(L, L, L - 1) + sp.Matrix([[1, -1, -L], [-1, 1, L], [-2, 2, 1]])
    gm = sp.Matrix([[-(1 + e) * lam + 2 * e, -(1 - e) * lam - 2 * e, -e * L],
                    [(1 - e) * lam + 2 * e, (1 + e) * lam - 2 * e, -e * L], [2, 2, 0]])
    return (-lam**2 + lam) * sp.eye(3) + base + g * gm


def in_z(expr):
    """an expression in e and gam through z = 4 e gam^2 only: returned in z, or None"""
    out = sp.expand(sp.sympify(expr).subs(e, z / (4 * g**2)))
    return None if out.has(g) else out


@lru_cache(maxsize=None)
def poly(n, typ, l):
    """the type's indicial polynomial in lam and z (det N0; five dimensions also 10.15(i)'s)"""
    return in_z(families(n, typ, l)[0].det())


def factors(n, typ, l):
    """(the factor carrying the class roots, the full polynomial)"""
    p = poly(n, typ, l)
    if typ == "s0":
        lin = lam * (lam - 3) if n == 4 else lam * (lam - 2)
    elif typ == "s":
        lin = (lam + l - 1) * (lam - l - 3) if n == 4 else (lam + l - 1) * (lam - l - 2)
    else:
        return None, p
    q, rem = sp.div(sp.Poly(p, lam), sp.Poly(lin, lam))
    assert rem.is_zero
    return sp.Poly(q.as_expr() / q.LC(), lam), p


def neg_roots(n, typ, l, zv):
    """the real roots <= 0 of the type's polynomial at z = zv (sorted, exact)"""
    return [x for x in sp.Poly(poly(n, typ, l).subs(z, zv), lam).real_roots() if x <= 0]


def first_order(n, typ, l, root0):
    """d mu/dz at z = 0 for the root of the type's polynomial through the integer root0"""
    p = poly(n, typ, l)
    return sp.cancel(-sp.diff(p, z).subs({lam: root0, z: 0}) / sp.diff(p, lam).subs({lam: root0, z: 0}))


# ------------------------------------------------------------------------------------------------- J1
def j1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    n = 3 if control == 0 else 4
    ok = True
    for typ, ls in (("s0", [0]), ("s", range(1, LMAX["s"] + 1)), ("v", range(1, LMAX["v"] + 1))):
        for l in ls:
            N0, N1, clean = families(n, typ, l)
            good = clean and (N0 - his66(typ, l)).applyfunc(sp.expand) == sp.zeros(*N0.shape)
            Sb = (N1 + 2 * (lam - 1) * sp.eye(N1.shape[0])) / 2
            good &= all(not q.has(lam) for q in Sb.applyfunc(sp.expand))
            ok &= good
            chk(f"n + 1 = {n + 1}, {typ}{l}: N0 = his Lemma 6.6 matrix; N1 = -2 (lam - 1) + 2 S-bar, S-bar free of lam",
                good)
    N0, N1, _ = families(n, "v", 1)
    okv = sp.expand(N0[0] - (-lam**2 + lam + 2)) == 0 and sp.expand(N1[0] + 2 * (lam - 1 - g)) == 0
    chk(f"n + 1 = {n + 1}: N0_v1 = {sp.factor(N0[0])}, N1_v1 = {N1[0]}; his p. 134", okv)
    okA = all(a2_zero(n, typ, l) for typ, l in (("s0", 0), ("s", 2), ("v", 2)))
    chk(f"n + 1 = {n + 1}: A2 = 0 on Minkowski", okA)
    if control != 0:
        return chk.ok
    ok5 = True
    for typ, ls in (("s0", [0]), ("s", range(1, LMAX["s"] + 1)), ("v", range(1, LMAX["v"] + 1))):
        for l in ls:
            N0, N1, clean = families(4, typ, l)
            p = poly(4, typ, l)
            ratio = None if p is None else sp.cancel(p / poly5(typ, l))
            good = clean and ratio == 1
            Sb = (N1 + 2 * (lam - sp.Rational(3, 2)) * sp.eye(N1.shape[0])) / 2
            good &= all(not q.has(lam) for q in Sb.applyfunc(sp.expand))
            if typ == "v":
                good &= sp.expand(N1[0] + 2 * (lam - sp.Rational(3, 2) - g)) == 0
                good &= sp.expand(N0[0] + (lam + l) * (lam - l - 2)) == 0
            ok5 &= good
            chk(f"n + 1 = 5, {typ}{l}: det N0 = {ratio} x 10.15(i); N1 = -2 (lam - 3/2) + 2 S-bar"
                + (f"; N0 = {sp.factor(N0[0])}, N1 = {N1[0]}" if typ == "v" else ""), good)
    chk(f"n + 1 = 5: A2 = 0 on Minkowski", all(a2_zero(4, typ, l) for typ, l in (("s0", 0), ("s", 2), ("v", 2))))
    return chk.ok


# ------------------------------------------------------------------------------------------------- J2
def j2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    zv = sp.Rational(1, 100) if control == 0 else -sp.Rational(1, 100)
    # five dimensions: the classes, every l, from 10.15(i)'s Q
    Ls, s = sp.symbols("l s", positive=True)
    kap = Ls * (Ls + 2)
    Q = s**2 - (2 + 2 * kap + z) * s + kap * (kap + 1) + z * kap
    idq = sp.expand(Q.subs(s, Ls * (Ls + 1)) - Ls * z) == 0 \
        and sp.expand(Q.subs(s, (Ls + 1) * (Ls + 2)) + (Ls + 2) * z) == 0
    chk("Q(l(l + 1)) = l z and Q((l + 1)(l + 2)) = -(l + 2) z for every l", idq)
    m0 = (1 - sp.sqrt(9 + 4 * z)) / 2
    oks = sp.expand(poly5("s0", 0).subs(lam, m0)) == 0 and sp.series(m0, z, 0, 2).removeO() == -1 - z / 3
    oks &= -2 < m0.subs(z, zv) < -1
    chk(f"s0: mu_s0 = (1 - (9 + 4z)^(1/2))/2 = -1 - z/3 + O(z^2), in (-2, -1) at z = {zv}", oks)
    ok = True
    for l in range(1, 7):
        p = poly5("s", l)
        c0 = sp.cancel(-sp.diff(p, z).subs({lam: -l, z: 0}) / sp.diff(p, lam).subs({lam: -l, z: 0}))
        c1 = sp.cancel(-sp.diff(p, z).subs({lam: -l - 1, z: 0}) / sp.diff(p, lam).subs({lam: -l - 1, z: 0}))
        good = c0 == -sp.Rational(l, 2 * (l + 1) * (2 * l + 1)) and c1 == -sp.Rational(l + 2, 2 * (l + 1) * (2 * l + 3))
        neg = [x for x in sp.Poly(p.subs(z, zv), lam).real_roots() if x <= 0]
        good &= len(neg) == 3 and -l - 2 < neg[0] < -l - 1 and -l - 1 < neg[1] < -l and neg[2] == -l + 1
        ok &= good
        chk(f"s{l}: d mu/dz = {c0}, {c1} at -l, -l - 1; the roots <= 0 at z = {zv}: "
            f"{[sp.N(x, 8) for x in neg]}", good)
    okv = all(sp.Poly(poly5("v", l), lam).all_roots() == [-l, l + 2] for l in range(1, 7))
    chk("vl: the roots -l and l + 2 at every z (l <= 6)", okv)
    okn = True
    for typ, ls in (("s0", [0]), ("s", range(1, LMAX["s"] + 1)), ("v", range(1, LMAX["v"] + 1))):
        for l in ls:
            neg = neg_roots(4, typ, l, zv)
            want = {"s0": 2, "s": 3, "v": 1}[typ]
            okn &= len(neg) == want
    chk(f"five dimensions: the roots <= 0 are the Killing ones and the classes, at z = {zv} (s0 2, sl 3, vl 1)", okn)
    # four dimensions: his roots and his first-order coefficients from J1's matrices
    q0, _ = factors(3, "s0", 0)
    ok4 = sp.expand(q0.as_expr() - (lam**2 - 1 - z)) == 0
    for l in range(1, LMAX["s"] + 1):
        K = l * (l + 1)
        quart = lam**4 - 2 * (K + sp.Rational(1, 2) + z / 2) * lam**2 + K * (K + z)
        q, _ = factors(3, "s", l)
        ok4 &= sp.expand(q.as_expr() - quart) == 0
        d0 = first_order(3, "s", l, -l)
        d1 = first_order(3, "s", l, -l - 1)
        ok4 &= d0 == -sp.Rational(2, 2 * l + 1) / 4 and d1 == -sp.Rational(2, 2 * l + 1) / 4
    chk("n + 1 = 4: -lam_s0,1 = -(1 + z)^(1/2); the sl quartic his lam_sl,l, lam_sl,l+1; d mu/dz = -2/(2l + 1) in his z",
        ok4)
    return chk.ok and ok and oks


# ------------------------------------------------------------------------------------------------- J3
def tens_split(h, n, typ, l, P):
    """his (2.44) components at r = 1: s0 (a, b, e, p); s1 (a, b, c, e, f, p); v1 (c, f)"""
    N = n + 1
    H = h.applyfunc(lambda q: ev(q, P))
    e0, e1 = (sp.Rational(1, 2), sp.Rational(1, 2)), (sp.Rational(1, 2), -sp.Rational(1, 2))
    hv = lambda u, v: sum(u[i] * v[j] * H[i, j] for i in range(2) for j in range(2))
    if typ == "v":
        V = ev(vphi(n, l), P)
        return [sp.cancel(sum(u[i] * H[i, N - 1] for i in range(2)) / V) for u in (e0, e1)]
    S = ev(harm(n, l), P) if typ == "s" else 1
    a, b, ee, p = hv(e0, e0) / S, hv(e0, e1) / S, hv(e1, e1) / S, H[2, 2] / S
    if typ == "s0":
        return [sp.cancel(q) for q in (a, b, ee, p)]
    dS = ev(sp.diff(harm(n, l), ch if n == 4 else th), P)
    c = sum(e0[i] * H[i, 2] for i in range(2)) / dS
    f = sum(e1[i] * H[i, 2] for i in range(2)) / dS
    return [sp.cancel(q) for q in (a, b, c, ee, f, p)]


@lru_cache(maxsize=None)
def dstar_matrix(n, typ, l):
    """N(delta-bar*(0), lam): all components at r = 1 at two angles, as a matrix in lam (rows) by basis (columns)"""
    G = geo(n, True)
    N = n + 1
    cols = []
    for E in basis(n, typ, l):
        h = dstar([r**(-lam) * q for q in E], G)
        cols.append([ev(h[i, j], P) for P in (TRIG, TRIG2) for i in range(N) for j in range(i, N)])
    return sp.Matrix(cols).T


def noninjective(n, typ, l):
    M = dstar_matrix(n, typ, l)
    d = sp.expand((M.T * M).det())
    return (sorted(set(sp.Poly(d, lam).real_roots())) if sp.Poly(d, lam).degree() > 0 else []), d


def j3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    want = {("s0", 0): [0], ("s", 1): [0], ("v", 1): [-1]}
    if control:
        want[("v", 1)] = []
    ok = True
    for n in (4, 3):
        for typ, ls in (("s0", [0]), ("s", range(1, LMAX["s"] + 1)), ("v", range(1, LMAX["v"] + 1))):
            for l in ls:
                rts, _ = noninjective(n, typ, l)
                good = rts == want.get((typ, l), [])
                ok &= good
                chk(f"n + 1 = {n + 1}, {typ}{l}: N(delta-bar*(0), lam) not injective at {rts}", good)
    G = geo(3, True)
    his = {("s0", 0): sp.Matrix([[-lam / 2, 0], [lam / 4, -lam / 4], [0, lam / 2], [1, -1]]),
           ("s", 1): sp.Matrix([[-lam / 2, 0, 0], [lam / 4, -lam / 4, 0], [sp.Rational(1, 2), 0, -(lam + 1) / 4],
                                [0, lam / 2, 0], [0, sp.Rational(1, 2), (lam + 1) / 4], [1, -1, -1]]),
           ("v", 1): sp.Matrix([[-(lam + 1) / 4], [(lam + 1) / 4]])}
    okh = True
    for (typ, l), Hm in his.items():
        cols = [tens_split(dstar([r**(-lam) * q for q in E], G), 3, typ, l, TRIG) for E in basis(3, typ, l)]
        okh &= (sp.Matrix(cols).T - Hm).applyfunc(sp.expand) == sp.zeros(*Hm.shape)
    chk("n + 1 = 4: his (2.46a), (2.46b), (2.46c) entry by entry", okh)
    return chk.ok


# ------------------------------------------------------------------------------------------------- J4
def shifts(n, kind, kmax):
    """the shifts a class root meets: -k (the t*-recursion), +2 (+1 in four dimensions: the stationary correction)"""
    return [-k for k in range(1, kmax + 1)] + [2 if n == 4 else 1]


def least_pos(R):
    """the least positive real zero of a polynomial in z (oo if none); None if it vanishes identically"""
    R = sp.expand(R)
    if R == 0:
        return None
    P = sp.Poly(R, z)
    rts = [x for x in P.real_roots() if x > 0] if P.degree() > 0 else []
    return min(rts) if rts else sp.oo


def resonances(n):
    """per class: the shifts resonant at z = 0, and the least positive z at which any shift (or a double root) occurs"""
    out = []
    for typ, l, kind, kmax in CLASSES:
        q, p = factors(n, typ, l)
        sh = shifts(n, kind, kmax)
        if kind == "q":
            roots0 = sorted(x for x in sp.Poly(q.as_expr().subs(z, 0), lam).all_roots() if x < 0)
            Rs = [sp.resultant(q.as_expr(), p.subs(lam, lam + k), lam) for k in sh]
            Rs.append(sp.resultant(q.as_expr(), sp.diff(p, lam), lam))
        else:
            roots0 = [kind]
            Rs = [p.subs(lam, kind + k) for k in sh] + [sp.diff(p, lam).subs(lam, kind)]
        at0 = [(m0, k) for m0 in roots0 for k in sh if sp.expand(p.subs({lam: m0 + k, z: 0})) == 0]
        zs = [least_pos(R) for R in Rs]
        out.append((typ, l, kind, roots0, at0, None if None in zs else min(zs)))
    return out


def at0_want(n, typ, l, kind):
    """10.30(iv)'s coincidences at z = 0: (class root, shift)"""
    if typ == "v":
        return set()
    if typ == "s0":
        return {(-1, 1)} if n == 3 else set()
    if kind == "q":
        return {(-l - 1, 2), (-l, -1)} if n == 4 else {(-l - 1, 1), (-l, -1), (-l, 1)}
    return {(-l + 1, -k) for k in range(1, min(2, 5 - l) + 1)}


def s0_hits(n, z0):
    """at z = z0, the roots of the s0 factor that meet a root of the type under a shift or are double: the class root
    (negative) and its partner (positive), each with what it meets"""
    q, p = factors(n, "s0", 0)
    pz = p.subs(z, z0)
    out = {"class": [], "partner": []}
    for m in sp.Poly(q.as_expr().subs(z, z0), lam).all_roots():
        ks = [k for k in shifts(n, "q", 2) if sp.expand(pz.subs(lam, m + k)) == 0]
        ks += ["double"] if sp.expand(sp.diff(pz, lam).subs(lam, m)) == 0 else []
        if ks:
            out["class" if m < 0 else "partner"].append((m, ks))
    return out


def j4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ok = True
    zwant = {4: 4 if control != 2 else 5, 3: 3}
    for n in (4, 3):
        res = resonances(n)
        zmin = sp.oo
        for typ, l, kind, roots0, at0, zs in res:
            got = {(int(a), int(b)) for a, b in at0}
            good = zs is not None and zs >= zwant[n] and (got == at0_want(n, typ, l, kind) or control == 1)
            ok &= good
            zmin = min(zmin, zs) if zs is not None else zmin
            chk(f"n + 1 = {n + 1}, {typ}{l} {'root of Q' if kind == 'q' else kind}: at z = 0 resonant "
                f"{sorted(got)}; none for 0 < z < {sp.N(zs, 6) if zs is not None else 'NONE'}", good)
        chk(f"n + 1 = {n + 1}: no class root meets a root of its type under its shifts for 0 < z < {zmin}, exactly "
            f"the bound {zwant[n]}", zmin == zwant[n])
        hits = s0_hits(n, zmin)
        sharp = hits == ({"class": [(-2, [2])], "partner": [(3, ["double"])]} if n == 4 else
                         {"class": [], "partner": [(2, [-2, "double"])]})
        chk(f"n + 1 = {n + 1} at z = {zmin}: s0 {hits} ("
            + ("sharp: the class root -2 meets 0)" if n == 4 else "not sharp: only the partner root 2 meets)"), sharp)
        if control == 1:
            ok &= all(not at0 for *_, at0, _ in res)
            chk(f"n + 1 = {n + 1} at z = 0: no resonance (control)", all(not at0 for *_, at0, _ in res))
    return chk.ok and ok


# ------------------------------------------------------------------------------------------------- J5
def kernel_vec(M):
    """a nonzero kernel vector of a singular square matrix, from its adjugate (a nonzero column)"""
    A = M.adjugate().applyfunc(sp.expand)
    for j in range(A.shape[1]):
        col = A[:, j]
        if any(q != 0 for q in col):
            return col
    return None


def state(n, typ, l, m, kmax, eg=None, factor=True, modq=None):
    """the generalized state t*^k omega-bar + sum k!/(k - i)! t*^(k - i) omega-breve-bar^i, k = kmax, at the class root
    m (a number, or the symbol mu modulo the polynomial modq); its components and the leading coefficients"""
    N0, N1, _ = families(n, typ, l)
    if eg is not None:
        N0, N1 = N0.subs({e: eg[0], g: eg[1]}), N1.subs({e: eg[0], g: eg[1]})
    red = (lambda x: sp.rem(sp.expand(x), modq, mu)) if modq is not None else sp.cancel
    c = [kernel_vec(N0.subs(lam, m)).applyfunc(red)]
    live = any(q != 0 for q in c[0])                   # omega-bar nonzero (modulo modq)
    for i in range(1, kmax + 1):
        A = N0.subs(lam, m - i)
        rhs = -(N1.subs(lam, m - i + 1) * c[-1])
        if modq is None:
            c.append(A.LUsolve(rhs).applyfunc(sp.cancel))
        else:                                          # keep polynomial in mu: scale by det A, nonzero modulo modq
            d = red(A.det())
            live &= d != 0
            c = [v.applyfunc(lambda x: red(x * d)) for v in c]
            c.append((A.adjugate() * rhs).applyfunc(red))
    E = basis(n, typ, l)
    k = kmax
    w = [0] * (n + 1)
    for i, ci in enumerate(c):
        coef = (sp.factorial(k) / sp.factorial(k - i)) if factor else 1
        for j, Ej in enumerate(E):
            for a in range(n + 1):
                w[a] += coef * (t - r)**(k - i) * r**(i - m) * ci[j] * Ej[a]
    return w, c, live


def boxes_zero(n, w, modq=None, eg=None):
    """box^Ups w at r = 1 and two angles, as a polynomial in t (each t-power of a sum of t*^j r^(a_j) terms vanishing
    forces every term to): zero, exactly or modulo modq"""
    G = geo(n, True)
    F = boxU(w, G)
    for P in (TRIG, TRIG2):
        for q in F:
            v = sp.sympify(q).subs(P).subs(r, 1)
            if eg is not None:
                v = v.subs({e: eg[0], g: eg[1]})
            num = sp.numer(sp.together(sp.expand(v)))
            if modq is not None:
                if any(sp.rem(sp.expand(co), modq, mu) != 0 for co in sp.Poly(sp.expand(num), t).all_coeffs()):
                    return False
            elif sp.expand(num) != 0:
                return False
    return True


def j5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    factor = control == 0
    ok = True
    for typ, l, kind, kmax in CLASSES:
        if kind == "q" or (control and kmax < 2):
            continue
        for n in ((4, 3) if control == 0 else (4,)):
            w, c, live = state(n, typ, l, kind, kmax, factor=factor)
            good = live and boxes_zero(n, w)
            ok &= good
            extra = ""
            if typ == "v" and n == 4 and control == 0:
                kap = [sp.factor(ci[0] / c[0][0]) for ci in c]
                extra = f"; omega-breve-bar^i = kappa_i r^i omega-bar, kappa = {kap}"
            chk(f"n + 1 = {n + 1}, {typ}{l} at {kind}, k = {kmax}: box^Ups = 0 exactly{extra}", good)
    if control == 0:
        okk = True
        for n in (4, 3):
            for l in range(1, LMAX["v"] + 1):
                N0, N1, _ = families(n, "v", l)
                kap, f = sp.Integer(1), sp.Integer(1)
                for j in range(1, 4):
                    kap = sp.cancel(kap * (-N1[0].subs(lam, -l - j + 1)) / N0[0].subs(lam, -l - j))
                    f *= (2 * l + 2 * j + 1 + 2 * g) / (j * (2 * l + j + 2)) if n == 4 else \
                        2 * (l + j + g) / (j * (2 * l + j + 1))
                    okk &= sp.cancel(kap - f) == 0
        okk &= sp.cancel(-families(4, "v", 1)[1][0].subs(lam, -1) / families(4, "v", 1)[0][0].subs(lam, -2)
                         - (1 + 2 * g / 5)) == 0
        okk &= sp.cancel(-families(3, "v", 1)[1][0].subs(lam, -1) / families(3, "v", 1)[0][0].subs(lam, -2)
                         - (1 + g / 2)) == 0
        ok &= okk
        chk("vl: kappa_i = prod (2l + 2j + 1 + 2 gam)/(j (2l + j + 2)) (four dimensions 2 (l + j + gam)/(j (2l + j + "
            "1))), l <= 4, i <= 3; 1 + 2 gam/5 and his 1 + gam/2 at l = 1", okk)
        for eg in ((sp.Rational(1, 3), sp.Rational(1, 2)), (sp.Rational(1, 7), sp.Rational(2, 5))):
            for typ, l, kind, kmax in CLASSES:
                if kind != "q":
                    continue
                for n in (4,):
                    q, _ = factors(n, typ, l)
                    modq = sp.expand(q.as_expr().subs(z, 4 * eg[0] * eg[1]**2).subs(lam, mu))
                    irr = sp.Poly(modq, mu).is_irreducible   # nonzero modulo it is then nonzero at every root
                    w, c, live = state(n, typ, l, mu, kmax, eg=eg, modq=modq)
                    good = irr and live and boxes_zero(n, w, modq=modq, eg=eg)
                    ok &= good
                    chk(f"n + 1 = {n + 1}, {typ}{l} at the roots of {modq} (irreducible), k = {kmax}, (e, gam) = "
                        f"{eg}: box^Ups = 0 modulo it", good)
    return chk.ok and ok


# ------------------------------------------------------------------------------------------------- J6
def j6(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    al = sp.Symbol("alpha")
    ok = True
    want1 = 2 if control == 0 else 3                   # the control: -l + 1's first step claimed obstructed
    for n in (4, 3):
        for gv in (sp.Rational(1, 3), sp.Rational(2, 7)):
            fam = {l: [M.subs({e: 0, g: gv}) for M in families(n, "s", l)[:2]] for l in range(1, 5)}
            for l in (1, 2, 3):                         # mu_l,0 = -l: the first step meets mu_l,1 = -l - 1
                N0, N1 = fam[l]
                c0 = N0.subs(lam, -l).nullspace()
                A, f = N0.subs(lam, -l - 1), -(N1.subs(lam, -l) * c0[0])
                good = len(c0) == 1 and A.rank() == 2 and A.row_join(f).rank() == 3
                ok &= good
                chk(f"n + 1 = {n + 1}, gam = {gv}, s{l} at -l: first step obstructed (rank 2, 3 with its right side): "
                    f"a logarithm", good)
            for l in (2, 3, 4):                         # -l + 1: the first step meets -l, the second -l - 1
                N0, N1 = fam[l]
                m = -l + 1
                c0 = N0.subs(lam, m).nullspace()
                A1, f1 = N0.subs(lam, m - 1), -(N1.subs(lam, m) * c0[0])
                good = len(c0) == 1 and A1.rank() == 2 and A1.row_join(f1).rank() == want1
                txt = "first step solvable"
                if good and 5 - l >= 2:
                    sol, par = A1.gauss_jordan_solve(f1)
                    K = A1.nullspace()
                    c1 = sol.subs({q: 0 for q in par}) + al * K[0]
                    A2, f2 = N0.subs(lam, m - 2), -(N1.subs(lam, m - 1) * c1)
                    y = A2.T.nullspace()
                    ob = sp.factor((y[0].T * f2)[0]) if len(y) == 1 else None
                    good &= len(K) == 1 and A2.rank() == 2 and ob is not None and sp.degree(ob, al) == 1
                    txt += f"; second step's obstruction {ob}, zero at alpha = {sp.solve(ob, al)}"
                if good and 5 - l >= 3:
                    good &= N0.subs(lam, m - 3).det() != 0
                ok &= good
                chk(f"n + 1 = {n + 1}, gam = {gv}, s{l} at -l + 1: {txt}", good)
    return chk.ok and ok


CHECKS = [("J1 the indicial families: four dimensions his Lemma 6.6, p. 134; five 10.15(i), N1 = -2(lam - 3/2) + 2S",
           j1, 1),
          ("J2 the classes: s0, two roots of Q, sl -l + 1, vl -l, each below its integer for z > 0; his in four", j2, 1),
          ("J3 delta-bar* injective at every class root (not at s0 0, s1 0, v1 -1); his (2.46a)-(2.46c)", j3, 1),
          ("J4 no resonance for 0 < z < 4 (four dimensions 3): the t*-recursion's, the stationary correction's shifts",
           j4, 2),
          ("J5 the states: t*^k omega-bar + ... in ker box^Ups on Minkowski at every class's largest k; vl in closed "
           "form", j5, 1),
          ("J6 e = 0: a logarithm forced at mu_l,0's first step; at -l + 1 none (first step), removable (second)",
           j6, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state_ = "PASS" if good and not control else "FAIL"
        ok_all &= state_ == "PASS"
        print(f"{name:<112} {state_}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"puregauge5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"puregauge5.py mutants: {caught}/{total}")
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
