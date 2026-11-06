#!/usr/bin/env python3
"""r7fixes5: the round-6 verifier's findings on lambda0 and on the tower remark, re-derived before they are seated
(CONSTANTS5.md, Round 7, R7.0), and the corrected stage-1 criterion (Round 7, item 2). Labels: computed (exact,
sympy), certified (Arb balls, python-flint; exact rationals), READ (cited .out values and lines), deduced (where said).

Notation (CONSTANTS5.md 1.4, lzerotrace5.py T3): at a point X of Omega, g_1(X, s) = m_1(X) + W_TT(X, s) + chi(X, s) D,
D = dv dv = U U^T, U = (1, xhat) in the Cartesian frame (tau, x); W_TT has only angular components, W_TT U = 0.
X* := (theta = 0, v = 2, r = a, phi1 = phi2 = 0), tau = 2 - a, where |W_TT|_op = (4/3) c a^(-3/2) >= 12.593309.

  R1 (exact; certified) MAJOR 1, the operator norm. At X*, in the frame (tau, x1, ..., x4) with xhat = e1, e_phi1 = e2,
     e_theta = e3, e_phi2 = e4: W(s) = K cos s diag(0, 0, 4/3, -2/3, -2/3), K = E H a^(-3/2), D = U U^T (sympy, from the
     closed forms of stage0bd5.py at theta = 0). For every symmetric M (symbolic):
        e2^T (M + W(s) + chi D) e2 = M_22 + (4/3) K cos s,     so  sup_s |M + W + chi D|_op >= (4/3) K + |M_22|;
     with M = 0 the eigenvalues are (4/3) K cos s, -(2/3) K cos s (twice), 2 chi, 0, so |W + chi D|_op =
     max(|W|_op, 2 |chi|) (W and D act on orthogonal subspaces; at every X, W_TT U = 0); with M = w (e2 e3^T + e3 e2^T)
     the top eigenvalue at s = 0 is K/3 + (K^2 + w^2)^(1/2) > (4/3) K for w != 0. Hence (deduced): stage 1 lowers the
     operator-norm bound iff sup_{Omega x S^1} |m_1 + W_TT + chi D|_op > 12.593309 is certified; m_1(X*) e2 != 0 is
     sufficient (a certified lower bound on |M_22| or on |w| gives a certified lower bound on the excess); with
     m_1 = 0 the sup is max(sup |W_TT|_op, 2 sup |chi|) = sup |W_TT|_op (2 sup |chi| <= 11.8821, stage1cap5 S2).
     Certified: (4/3) c_lo a^(-3/2) > 12.5933.
  R2 (exact; certified) MAJOR 2, the Frobenius reading. With W(s + pi) = -W(s), chi(s + pi/2) = -chi(s):
        sum_{j=0}^{3} |M + W(s + j pi/2) + chi(s + j pi/2) D|_F^2 = 4 |M|_F^2 + 2 (|W(s)|_F^2 + |W(s + pi/2)|_F^2)
                                                                   + 4 chi(s)^2 |D|_F^2,   |D|_F = |U|^2 = 2
     (sympy, generic symmetric 3 x 3 blocks and scalars; the cross terms cancel in pairs). So for every m_1,
     sup_s |g_1(X, s)|_F^2 >= B(X, s) := (|W(s)|_F^2 + |W(s + pi/2)|_F^2)/2 + 4 chi(s)^2 at every X, s. B is maximised
     on a grid over (theta, v, s) at r = a (floating point) and evaluated certified at the rational point found, which
     lies in Omega (lzerotrace5.in_omega); with eps1 <= 0.030768560 (lzerotrace5.out T7, the Frobenius-sharp
     perturbation of lzerorank5 R1) this gives lambda0 < eps1/B^(1/2) in the Frobenius reading. Printed beside it, as a
     floating-point figure only: sup_s |W + chi D|_F at that X (the value if m_1 = 0).
  R3 (exact) minor m1, the towers of D4 Proposition 3.1 (READ PART-III-D4-GENSTATES.md:113-150): s0 terms at the
     rho-exponents 0, -1, ..., -4, s1 at 0, -1, ..., -4, v1 at -1 (|x| V), -2, -3, -4. Offset 1 lands at m + 1; with
     box^Ups(0)'s indicial polynomials (gaugepot5.py G1, READ as in r6fixes5.py) at z = 4e-6, m + 1 is a root exactly
     at (s0, -1), (s1, -1) (both on 0) and (v1, -2) (on -1), each simple; at z = 0 also at (s0, -2), (s1, -2), (s1, -3).
     A simple resonance raises the formal solution's log order from the source's 0 to at most 1 (Lemma 1.5), and
     E^iota_ind's offset 1 already carries log order 2 (from v1, R5.2): the maximum at offset 1 stays 2, so R5.2's
     table and E^flat's log orders are unchanged (deduced). r6fixes5.py F3 (round 6) tested an incomplete list.
  R4 (computed) minor m2: III.I' (3.2)'s E^#(1) contains (lambda#, 0) (I2:175); its (2.2)-completion puts (lambda# + 1,
     0) = (2.5099, 0) in the set before the round at [2, 3). eflat5.f4_table run with (lambda#, 0) added to G: every
     row and both excesses (23, 47) unchanged (R0 and R1), so the sentence "no other completion meets a later raise"
     (R6.0 M1) is false and harmless.
  R5 (certified) minor m3: stage1rate5's enclosures recomputed in Arb (its forms and cover, imported): q_lo >= 0.1966827
     (not 0.196683), e^(kappa Dtau/2) <= 1.1051725e17 (not 1.105e17), so c_Y q_lo^(-1/2) e^(kappa Dtau/2) <= 3.52422e17
     (round 6's 3.525e17 stands as a bound), and stage1rate5's factor-2 figure is <= 7.04843e17 (it printed 7.048e17,
     rounded down).
  Controls (each mutates the computed path; each must fail): C1 R1 with U given an angular component (U = (1, 1, 1, 0,
  0)): e2 stays orthogonal but e3^T D e3 != 0 and the max(|W|, 2|chi|) identity fails; C2 R2's identity with chi a first
  harmonic: the cross terms no longer cancel; C3 R2's point moved to r = a - 1e-6: in_omega rejects it; C4 R3 on
  round 6's list (s0, s1 at -2, -3, -4; v1 at -1): no resonance found, so R3's test (exactly the three) fails; C5 R4
  with (lambda#, 0) given log order 9: the table changes, so R4's test can see a change; C6 R5's test that F2's
  printed q_lo is a valid lower end: fails (0.196683 > 0.1966827...).

    python3 checks/r7fixes5.py       (about a minute)
"""
import builtins
import contextlib
import io
import os
import sys
import textwrap
from fractions import Fraction as Fr

import flint
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import lzeroconst5 as LZ          # noqa: E402  (round 1's certified geometry)
    import lzerotrace5 as LT          # noqa: E402  (in_omega)
    import eflat5 as EF               # noqa: E402  (f4_table)
    import dweights5 as DW            # noqa: E402
    import stage1rate5 as SR          # noqa: E402  (the forms and cover of round 5)

OK = {}
C_LO, C_HI = flint.arb('1.32407110621'), flint.arb('1.3241034918')   # READ envelope5.out E1 (c, certified)
EPS1_HI = flint.arb('0.030768560')                                   # READ lzerotrace5.out T7 (upper end)
TAU0 = -2


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def a_ball():
    return (flint.arb(9) / 1250) ** (flint.arb(1) / 8) / 2


def fa(x):
    return flint.arb(flint.fmpq(x.numerator, x.denominator))


# ---------------------------------------------------------------------------------------------- R1
def r1(U=(1, 1, 0, 0, 0)):
    s, K, chi, w = sp.symbols('s K chi w', real=True)
    th, r, E, A = sp.symbols('theta r E A', positive=True)
    C, S = sp.cos(th), sp.sin(th)
    a1 = K * (2 * C ** 2 * sp.cos(s) - S ** 2 * sp.sin(s)) / 3          # K = A E H r^(-3/2), stage0bd5's forms
    a2 = K * (2 * S ** 2 * sp.sin(s) - C ** 2 * sp.cos(s)) / 3
    eig = [sp.simplify(x.subs(th, 0)) for x in (2 * a1, -2 * (a1 + a2), 2 * a2)]    # e_phi1, e_theta, e_phi2
    W = sp.diag(0, 0, *eig)
    Uv = sp.Matrix(U)
    D = Uv * Uv.T
    Ms = sp.Matrix(5, 5, lambda i, j: sp.Symbol('m%d%d' % (min(i, j), max(i, j))))
    g = Ms + W + chi * D
    e2 = sp.Matrix([0, 0, 1, 0, 0])
    quad = sp.simplify((e2.T * g * e2)[0] - (Ms[2, 2] + sp.Rational(4, 3) * K * sp.cos(s)))
    ev0 = (W + chi * D).eigenvals()
    expect = {sp.Rational(4, 3) * K * sp.cos(s): 1, -sp.Rational(2, 3) * K * sp.cos(s): 2, 2 * chi: 1, sp.Integer(0): 1}
    eig_ok = (sum(ev0.values()) == 5 and all(any(sp.simplify(k - k2) == 0 and ev0[k] == m for k in ev0)
                                             for k2, m in expect.items()))
    block = (W * Uv).is_zero_matrix
    Mc = w * (e2 * sp.Matrix([0, 0, 0, 1, 0]).T + sp.Matrix([0, 0, 0, 1, 0]) * e2.T)
    sub = (Mc + W).subs(s, 0)[2:4, 2:4]
    top = max(sub.eigenvals(), key=lambda x: sp.re(x.subs({K: 1, w: sp.Rational(1, 10)})))
    coup = sp.simplify(top - (K / 3 + sp.sqrt(K ** 2 + w ** 2))) == 0
    return quad == 0, eig_ok, block, coup, eig


# ---------------------------------------------------------------------------------------------- R2
def r2_identity(chi_harm=2):
    s = sp.Symbol('s', real=True)
    syms = lambda p: sp.Matrix(3, 3, lambda i, j: sp.Symbol('%s%d%d' % (p, min(i, j), max(i, j))))  # noqa: E731
    M, A1, B1, D = syms('m'), syms('a'), syms('b'), syms('d')
    c1, c2 = sp.symbols('c1 c2', real=True)
    W = lambda x: A1 * sp.cos(x) + B1 * sp.sin(x)                      # noqa: E731
    ch = lambda x: c1 * sp.cos(chi_harm * x) + c2 * sp.sin(chi_harm * x)  # noqa: E731
    F2 = lambda X: (X.T * X).trace()                                   # noqa: E731
    lhs = sum(F2(M + W(s + j * sp.pi / 2) + ch(s + j * sp.pi / 2) * D) for j in range(4))
    rhs = 4 * F2(M) + 2 * (F2(W(s)) + F2(W(s + sp.pi / 2))) + 4 * ch(s) ** 2 * F2(D)
    return sp.simplify(sp.expand(sp.expand_trig(lhs - rhs))) == 0


def wf_parts():
    """|W(s)|_F^2 and chi(s) as functions of (theta, v, s, r, E): stage0bd5's closed forms (READ via stage1cap5)"""
    s, th, r, v, E = sp.symbols('s theta r v E', real=True)
    H2 = 2 / (1 + sp.cos(2 * th) ** 2)
    c, sn = sp.cos(th), sp.sin(th)
    K = E * sp.sqrt(H2) * r ** sp.Rational(-3, 2)
    a1 = K * (2 * c ** 2 * sp.cos(s) - sn ** 2 * sp.sin(s)) / 3
    a2 = K * (2 * sn ** 2 * sp.sin(s) - c ** 2 * sp.cos(s)) / 3
    WF2 = 4 * (a1 + a2) ** 2 + 4 * a1 ** 2 + 4 * a2 ** 2
    ang = 4 * sp.cos(2 * th) * sp.sin(2 * s) + sp.sin(2 * th) ** 2 * sp.cos(2 * s)
    chi = -sp.Rational(1, 12) * E ** 2 * H2 * ang * (r ** -2 - (v - TAU0) ** sp.Rational(-1, 2) * r ** sp.Rational(-3, 2))
    B = (WF2 + WF2.subs(s, s + sp.pi / 2)) / 2 + 4 * chi ** 2
    full = WF2 + 4 * chi ** 2
    return B, full, (s, th, r, v, E)


def env_shape(v):
    """the envelope's shape factor E(v)/c (stage1cap5.env_sq_hi's form), floating"""
    import math
    y = (2 * v - 4) / 3
    if abs(y) >= 1:
        return 0.0
    return math.cos(math.pi * y / 2) ** 12 * math.exp(-y * y / (1 - y * y))


def r2_search(B, syms):
    import math
    s, th, r, v, E = syms
    fB = sp.lambdify((s, th, r, v, E), B, 'math')
    a = float(a_ball().mid())
    c = float(C_LO.mid())
    best = (0, None)
    for i in range(0, 41):
        thv = (math.pi / 2) * i / 40
        for j in range(0, 61):
            vv = 1.4 + 1.2 * j / 60
            Ev = c * env_shape(vv)
            for k in range(0, 64):
                sv = math.pi * k / 64
                val = fB(sv, thv, a, vv, Ev)
                if val > best[0]:
                    best = (val, (thv, vv, sv))
    return best


def arb_eval_B(B, syms, thq, vq, sq, a, c):
    """B at a rational point, in Arb throughout (no floating constants): the closed forms of wf_parts written out"""
    y = (2 * vq - 4) / 3
    yb = fa(y)
    shape = (flint.arb.pi() * yb / 2).cos() ** 12 * (-(yb * yb) / (1 - yb * yb)).exp()
    E = c * shape
    th, sv, v = fa(thq), fa(sq), fa(vq)
    C, S = th.cos(), th.sin()
    H2 = 2 / (1 + (2 * th).cos() ** 2)
    K = E * H2.sqrt() * a ** flint.arb(-1.5)

    def wf2(x):
        a1 = K * (2 * C ** 2 * x.cos() - S ** 2 * x.sin()) / 3
        a2 = K * (2 * S ** 2 * x.sin() - C ** 2 * x.cos()) / 3
        return 4 * (a1 + a2) ** 2 + 4 * a1 ** 2 + 4 * a2 ** 2
    rad = a ** -2 - (v + 2) ** flint.arb(-0.5) * a ** flint.arb(-1.5)
    chi = -E ** 2 * H2 * (4 * (2 * th).cos() * (2 * sv).sin() + (2 * th).sin() ** 2 * (2 * sv).cos()) * rad / 12
    return (wf2(sv) + wf2(sv + flint.arb.pi() / 2)) / 2 + 4 * chi ** 2


# ---------------------------------------------------------------------------------------------- R3
def tower_resonances(z, lists=None):
    lam = sp.Symbol('lam')
    kap = 3
    Q = lambda S: S ** 2 - (2 + 2 * kap + z) * S + kap * (kap + 1) + z * kap  # noqa: E731
    poly = {'s0': lam * (lam - 3) * (lam ** 2 - lam - 2 - z), 's1': (4 - lam) * lam * Q(lam * (lam - 1)),
            'v1': (lam + 1) * (3 - lam)}
    if lists is None:
        lists = {'s0': [0, -1, -2, -3, -4], 's1': [0, -1, -2, -3, -4], 'v1': [-1, -2, -3, -4]}
    hits = []
    for t, ms in lists.items():
        p = sp.Poly(sp.expand(poly[t]), lam)
        for m in ms:
            x = m + 1
            if p.eval(x) == 0:
                mult, q = 0, p
                while q.eval(x) == 0:
                    q = sp.Poly(sp.div(q.as_expr(), lam - x)[0], lam)
                    mult += 1
                hits.append((t, m, x, mult))
    return hits


# ---------------------------------------------------------------------------------------------- R4
def lsharp_table(extra_log=0):
    off, ints, ok = EF.offsets()
    d0, d1, dp1 = off[('s0', 0)][1], off[('sl-', 1)][1], off[('sl+', 1)][1]
    blocks = {'s0': [2 + d0, Fr(3)], 's1': [2 + d1, 3 + dp1, Fr(4)], 'v1': [Fr(3)]}
    union = {}
    for b, k in (('s0', 1), ('v1', 2), ('s1', 2), ('s1', 1)):
        for w_, lo in EF.site_eind(blocks[b], k).items():
            union[w_] = max(union.get(w_, -1), lo)
    G = {Fr(2): 0}
    for w_, lo in union.items():
        if 0 < w_ <= 1 + EF.EPS_P:
            G[2 + w_] = max(G.get(2 + w_, -1), lo)
    lmax_w = max(lo for w_, lo in union.items() if 0 < w_ <= EF.TOP_W)
    c_gen = max(lmax_w, max(G.values()))
    out = {}
    for name, M in (('R0', 1), ('R1', 4)):
        base = EF.f4_table(M, G, lmax_w, c_gen)
        G2 = dict(G)
        G2[EF.LSHARP] = extra_log
        mod = EF.f4_table(M, G2, lmax_w, c_gen)
        out[name] = (base, mod)
    return out


# ---------------------------------------------------------------------------------------------- R5
def r5_numbers():
    flint.ctx.prec = 120
    with contextlib.redirect_stdout(io.StringIO()):
        M, Q, P, G, Ye, mm, kk, R = SR.forms()
        qlo, qhi, cyhi, _ = SR.q_bounds(Q, Ye, mm)
        kap, rworst = SR.sup_kappa(M, Q, mm, kk)
    fac = (kap * SR.arb_q(SR.DTAU) / 2).exp()
    coef = cyhi.sqrt() / qlo.sqrt() * fac
    return qlo, fac, coef


def main():
    print('r7fixes5: the round-6 verifier\'s findings on lambda0 and the towers, re-derived; the stage-1 criterion')
    a = a_ball()
    # R1
    q, eig_ok, block, coup, eig = r1()
    K_lo = C_LO * a ** flint.arb(-1.5)
    opb = flint.arb(4) / 3 * K_lo
    OK['R1'] = q and eig_ok and block and coup and opb.lower() > flint.arb('12.5933')
    print('  R1: at X* the W_TT eigenvalues (e_phi1, e_theta, e_phi2) are %s (exact); e2^T g e2 = M_22 + (4/3) K cos s '
          'for every symmetric M: %s; with M = 0 the spectrum is {(4/3) K cos s, -(2/3) K cos s (x2), 2 chi, 0}: %s; '
          'W U = 0: %s; with M = w (e2 e3^T + e3 e2^T) the top eigenvalue at s = 0 is K/3 + (K^2 + w^2)^(1/2): %s. '
          '(4/3) K >= %s (certified, c >= 1.32407110621, envelope5 E1). So sup_s |m_1 + W_TT + chi D|_op >= '
          '12.5933 + |m_1(X*)_22|, and m_1(X*) e2 != 0 raises the bound; with m_1 = 0 it is max(|W_TT|, 2 |chi|) '
          'pointwise: %s' % (eig, q, eig_ok, block, coup, flint.arb(opb.lower()).str(8), OK['R1']))
    # R2
    ident = r2_identity()
    B, full, syms = wf_parts()
    best, arg = r2_search(B, syms)
    thq = Fr(round(arg[0] * 10 ** 4), 10 ** 4)
    vq = Fr(round(arg[1] * 10 ** 4), 10 ** 4)
    sq = Fr(round(arg[2] * 10 ** 4), 10 ** 4)
    Bb = arb_eval_B(B, syms, thq, vq, sq, a, C_LO)
    g = LZ.geometry()
    alo, ahi = g['a']
    inside = LT.in_omega(vq - ahi, ahi, vq, g)          # as lzerotrace5 T3: r = a is Omega's inner boundary
    capF = Bb.sqrt()
    lamF = EPS1_HI / capF
    s, th, r, v, E = syms
    import math
    ffull = sp.lambdify((s, th, r, v, E), full, 'math')
    Ev = float(C_LO.mid()) * env_shape(float(vq))
    m0 = max(ffull(math.pi * k / 2000, float(thq), float(a.mid()), float(vq), Ev) for k in range(2000)) ** 0.5
    OK['R2'] = ident and inside and capF.lower() > flint.arb('16.1') and lamF.upper() < flint.arb('0.00191')
    print('  R2: the four-phase identity (exact): %s; B maximised on a grid at (theta, v, s) = (%s, %s, %s) (floating '
          'point %.5f), certified there: B >= %s, so C_app (Frobenius) >= %s for every m_1; the point (tau, r, v) = '
          '(v - a, a, v) lies in Omega: %s; with eps1 <= 0.030768560: lambda0 (Frobenius) < %s (certified; round 4-5: '
          '0.0019950). If m_1 were 0: sup_s |W + chi D|_F there = %.4f (floating point): %s' % (
              ident, float(thq), float(vq), float(sq), best, flint.arb(Bb.lower()).str(8),
              flint.arb(capF.lower()).str(8), inside, flint.arb(lamF.upper()).str(6), m0, OK['R2']))
    # R3
    z = Fr(4, 10 ** 6)
    h = tower_resonances(z)
    h0 = tower_resonances(0)
    want = {('s0', -1, 0, 1), ('s1', -1, 0, 1), ('v1', -2, -1, 1)}
    OK['R3'] = set(h) == want and all(mu == 1 for *_, mu in h0)
    print('  R3: towers (s0, s1 at 0..-4; v1 at -1..-4), offset 1 on a root of its type at z = 4e-6: %s (type, '
          'exponent, root, multiplicity); at z = 0: %s; all simple, so the offset-1 log order is <= 1 < 2 (E^iota_ind '
          'at offset 1, from v1): R5.2\'s table unchanged: %s' % (sorted(h), sorted(h0), OK['R3']))
    # R4
    t4 = lsharp_table()
    same = all(t4[nm][0] == t4[nm][1] for nm in t4)
    exc = (t4['R0'][0][1], t4['R1'][0][1])
    OK['R4'] = same and exc == (23, 47)
    print('  R4: f4_table with (lambda#, 0) added to G (its (2.2)-completion reaching 2.5099): rows and excesses '
          'unchanged (R0, R1): %s; excesses %s' % (same, exc))
    # R5
    qlo, fac, coef = r5_numbers()
    OK['R5'] = (coef.upper() < flint.arb('3.52422e17') and qlo.lower() < flint.arb('0.196683')
                and fac.upper() > flint.arb('1.105e17') and (2 * coef).upper() < flint.arb('7.04843e17'))
    print('  R5: q_lo >= %s, e^(kappa Dtau/2) <= %s, c_Y q_lo^(-1/2) e^(kappa Dtau/2) <= %s, the factor-2 figure <= %s '
          '(certified, Arb, stage1rate5\'s forms and cover): %s' % (
              flint.arb(qlo.lower()).str(10), flint.arb(fac.upper()).str(10), flint.arb(coef.upper()).str(8),
              flint.arb((2 * coef).upper()).str(8), OK['R5']))
    # controls
    q1, e1, b1, c1_, _ = r1(U=(1, 1, 1, 0, 0))
    OK['C1'] = not (e1 and b1)
    print('  C1 (control): U with an angular component: the M = 0 spectrum identity holds: %s, W U = 0: %s; R1\'s test '
          'fails: %s' % (e1, b1, OK['C1']))
    OK['C2'] = not r2_identity(chi_harm=1)
    print('  C2 (control): chi a first harmonic: the four-phase identity fails: %s' % OK['C2'])
    out = fa(alo) - flint.arb('1e-6')
    rq = Fr(int((alo - Fr(1, 10 ** 6)) * 10 ** 12), 10 ** 12)
    OK['C3'] = not LT.in_omega(vq - rq, rq, vq, g)
    print('  C3 (control): R2\'s point at r = a - 1e-6: in_omega rejects it: %s' % OK['C3'])
    hr6 = tower_resonances(z, lists={'s0': [-2, -3, -4], 's1': [-2, -3, -4], 'v1': [-1]})
    OK['C4'] = set(hr6) != want
    print('  C4 (control): round 6\'s list (s0, s1 at -2, -3, -4; v1 at -1): resonances %s, so R3\'s test fails: %s' % (
        hr6, OK['C4']))
    t5 = lsharp_table(extra_log=9)
    OK['C5'] = any(t5[nm][0] != t5[nm][1] for nm in t5)
    print('  C5 (control): (lambda#, 9) in place of (lambda#, 0): the table changes: %s' % OK['C5'])
    OK['C6'] = not (qlo.lower() >= flint.arb('0.196683'))
    print('  C6 (control): round 6\'s F2 input q_lo >= 0.196683 tested against the certified enclosure: false: %s'
          % OK['C6'])
    for k, val in OK.items():
        builtins.print(k, 'PASS' if val else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
