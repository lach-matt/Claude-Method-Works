#!/usr/bin/env python3
"""tensorzero5: the zero-energy inverse bound of L_b0 on its tensor-type block, in the class, through the horizon
(CONSTANTS5.md, Round 7, item 3). Labels: computed (exact, sympy; exact rationals), certified (rational bounds),
deduced (where said), READ (cited lines).

I.C:497's quantity is sigma_min of L-hat_b0(0) on fifteen components, type by type in the T^2 x Z2 x Z2 class: s0 (on
the complement of its one zero-energy state), s_l and t_l at even l >= 2 (class5.py C2: one invariant scalar and one
invariant TT tensor harmonic at each even l, no invariant divergence-free 1-form). This program does the t_l blocks.
Background: 5D Schwarzschild-Tangherlini g = -f dt^2 + f^-1 dr^2 + r^2 (dth^2 + cos^2 th dphi1^2 + sin^2 th dphi2^2),
f = 1 - mu/r^2, mu = 1 (zeroext5 Z0: the bound is scale invariant). L_b = D Ric + delta*_{E^C} delta_{E^Ups} G
(lin5.py's definitions, READ [Hin26] (8.1)), E^Ups h = -gam_U (2 iota_{c_U#} h - m (1 - e_U) c_U tr h), c_U = r^-1 dt.

  T1 (exact) the class's TT harmonics at l = 2, 4: T = A dth^2 + B cos^2 th dphi1^2 - (A + B) sin^2 th dphi2^2, A, B
     polynomials in cos^2 th (class5.py's ansatz and equations, imported), solved: one solution at each l, printed.
  T2 (exact) for h = r^2 H(r) T: tr_g h = 0, div_g h = 0 and iota_{dt#} h = 0, so E^Ups h = 0 and delta_{E^Ups} G h = 0:
     the gauge term of L_b vanishes on the block, and L_b h = D Ric(h).
  T3 (exact) D Ric(h) = d/deps Ric(g + eps h) at eps = 0 (every component, H symbolic) equals (1/2) r^2 (A_l H) T, with
     A_l H = -r^-3 (P H')' + l (l + 2) r^-2 H, P = r^3 - mu r: the scalar model of zeroext5.py at the same l, exactly,
     and every component outside the angular block vanishes. (The tensor mode obeys the massless scalar equation.)
  T4 (exact) the norm's angular weight on the block: with the six rotation fields K_ij = x_i d_j - x_j d_i of R^4
     restricted to S^3, sum_ij ||L_{K_ij} T||^2 = (l (l + 2) + 4) ||T||^2 (L^2(S^3), round metric), at l = 2 and 4;
     for the scalar harmonics the same sum is l (l + 2) (zeroext5's L).
  T5 (deduced, certified arithmetic) the constant. N_T(u)^2 := int (r |u|^2 + r^3 |u'|^2 + (L + 4) r |u|^2) dr is the
     block's ||h||^2 in Hbar^(1,-1)_b with the generators r d_r and L_{K_ij} on frame components; F^2 = int r^5 |A_l
     u|^2 dr. zeroext5's pieces (Z2-Z4: the multiplier w = r, the exterior Hardy bound, the choice of b in [b1, b2])
     bound int_a^b r^3|u'|^2 and L int_a^b r|u|^2 by (1 + kappa q) F^2, q = (l + 1)^-2, int_b^oo P|u'|^2 and (l + 1)^2
     int_b^oo r|u|^2 by q F^2 (and (L + 5) q^2 = q + 4 q^2 exactly): so, for l >= 2,
        C_T,l^2 = (2 + 5/L)(1 + kappa q) + q + 4 q^2 + q/f(b1),
     certified at b1 = 6/5, b2 = 2, decreasing in l, sup over even l >= 2 at l = 2. With T3's factor 1/2:
        ||h||_{Hbar^(1,-1)_b} <= 2 C_T ||L-hat_b0(0) h||_{Hbar^(0,1)_b} = C_T ||2 L-hat_b0(0) h||   on [r_h/2, oo) x S^3,
     for every h in the t_l blocks (every even l >= 2 at once: the norms are diagonal in l).
  T6 (floating point) N_T/F on 300 test functions (zeroext5's family) at l = 2, 4, 6: below C_T.
  Controls (each mutates the computed path; each must fail): C1 T2-T3 on the trace part h = r^2 H (dth^2 + cos^2 th
  dphi1^2 + sin^2 th dphi2^2) (an s-type tensor): tr h != 0 and D Ric(h) is not (1/2) r^2 (A_l H) h; C2 T4 with the
  claim sum ||L_K T||^2 = l (l + 2) ||T||^2 (the scalar weight): refuted at l = 2; C3 T5 with the scalar weight L in
  place of L + 4: the constant moves outside T5's pinned interval.

    python3 checks/tensorzero5.py       (a few minutes)
"""
import builtins
import contextlib
import io
import math
import os
import sys
import textwrap
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import class5 as CL              # noqa: E402  (the class's TT ansatz and equations)
    import zeroext5 as ZE            # noqa: E402  (the scalar model's test functions and norms)

OK = {}
t, r, th, p1, p2, eps = sp.symbols('t r theta phi1 phi2 epsilon', real=True)
X = (t, r, th, p1, p2)
Hf = sp.Function('H')(r)
CT_PIN = (Fr(3875, 1000), Fr(3880, 1000))          # C_T^2 at l = 2, pinned (T5)


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def tt_harmonic(l):
    """the class's TT harmonic at level l (class5's ansatz, solved): returns (A(c), B(c)) in c = cos^2 th"""
    deg = l // 2 + 1
    O = CL._ode()
    A, B = O['A'], O['B']
    a = sp.symbols('a0:%d' % (deg + 1))
    b = sp.symbols('b0:%d' % (deg + 1))
    cc = sp.Symbol('cc')
    Ac = sum(a[k] * cc ** k for k in range(deg + 1))
    Bc = sum(b[k] * cc ** k for k in range(deg + 1))
    ev = l * (l + 2) - 2
    exprs = list(O['div']) + [O['lap'][i] + ev * O['T'][i] for i in range(3)]
    thv = CL.th
    sol_eqs = []
    for e in exprs:
        e2 = e.subs({A: Ac.subs(cc, sp.cos(thv) ** 2), B: Bc.subs(cc, sp.cos(thv) ** 2)}).doit()
        e2 = sp.expand(sp.expand_trig(sp.simplify(e2)))
        for k in range(1, 4 * deg + 9):
            u = sp.Rational(k, 4 * deg + 10)
            cv, sv = (1 - u ** 2) / (1 + u ** 2), 2 * u / (1 + u ** 2)
            val = sp.nsimplify(e2.subs({sp.cos(thv): cv, sp.sin(thv): sv, sp.tan(thv): sv / cv}))
            val = sp.expand(val)
            if val != 0:
                sol_eqs.append(val)
    sol_eqs += [(Ac - Bc).subs(cc, 0), (Ac - (-Ac - Bc)).subs(cc, 1)]
    M, _ = sp.linear_eq_to_matrix(sol_eqs, list(a) + list(b))
    ns = M.nullspace()
    if len(ns) != 1:
        return None, len(ns)
    v = ns[0]
    v = v / [x for x in v if x != 0][0]
    Asol = sum(v[k] * cc ** k for k in range(deg + 1))
    Bsol = sum(v[deg + 1 + k] * cc ** k for k in range(deg + 1))
    return (sp.expand(Asol), sp.expand(Bsol)), 1


def angular_tensor(AB):
    cc = sp.Symbol('cc')
    Asol, Bsol = AB
    A_ = Asol.subs(cc, sp.cos(th) ** 2)
    B_ = Bsol.subs(cc, sp.cos(th) ** 2)
    return [A_, B_ * sp.cos(th) ** 2, -(A_ + B_) * sp.sin(th) ** 2]


def ricci_diag(gd):
    """Ricci of the diagonal metric diag(gd) in coordinates X (all components)"""
    n = 5
    G = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                val = 0
                if b == c:
                    val -= sp.diff(gd[b], X[a])
                if a == b:
                    val += sp.diff(gd[a], X[c])
                if a == c:
                    val += sp.diff(gd[a], X[b])
                G[a][b][c] = val / (2 * gd[a])
    R = sp.zeros(n)
    for b in range(n):
        for c in range(b, n):
            e = 0
            for a in range(n):
                e += sp.diff(G[a][b][c], X[a]) - sp.diff(G[a][b][a], X[c])
                for d in range(n):
                    e += G[a][a][d] * G[d][b][c] - G[a][c][d] * G[d][b][a]
            R[b, c] = R[c, b] = e
    return R


def background():
    f = 1 - 1 / r ** 2
    return [-f, 1 / f, r ** 2, r ** 2 * sp.cos(th) ** 2, r ** 2 * sp.sin(th) ** 2], f


def gauge_and_dric(Tang):
    g0, f = background()
    h = [0, 0] + [r ** 2 * Hf * x for x in Tang]
    trh = sp.simplify(sum(h[i] / g0[i] for i in range(5)))
    # div_g h: (div h)_b = g^{ac} nabla_c h_{ab}, diagonal metric and diagonal h
    n = 5
    G = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                val = 0
                if b == c:
                    val -= sp.diff(g0[b], X[a])
                if a == b:
                    val += sp.diff(g0[a], X[c])
                if a == c:
                    val += sp.diff(g0[a], X[b])
                G[a][b][c] = val / (2 * g0[a])
    H = sp.diag(*h)
    div = []
    for b in range(n):
        e = 0
        for a in range(n):
            c = a
            cov = sp.diff(H[a, b], X[c]) - sum(G[m][c][a] * H[m, b] + G[m][c][b] * H[a, m] for m in range(n))
            e += cov / g0[a]
        div.append(sp.simplify(e))
    iota = [sp.simplify(H[0, b] / g0[0]) for b in range(n)]        # iota_{dt#} h, dt# = g^tt d_t
    gp = [g0[i] + eps * h[i] for i in range(5)]
    Rp = ricci_diag(gp)
    dR = Rp.applyfunc(lambda e: sp.simplify(sp.diff(e, eps).subs(eps, 0)))
    return trh, div, iota, dR, h


def casimir(Tang, scalar=None):
    """sum over the six rotation fields of ||L_K T||^2 / ||T||^2 on the round S^3 (Hopf coordinates)"""
    Y = (th, p1, p2)
    x = [sp.cos(th) * sp.cos(p1), sp.cos(th) * sp.sin(p1), sp.sin(th) * sp.cos(p2), sp.sin(th) * sp.sin(p2)]
    J = sp.Matrix(4, 3, lambda i, j: sp.diff(x[i], Y[j]))
    gS = sp.simplify(J.T * J)
    gSi = sp.simplify(gS.inv())
    vol = sp.cos(th) * sp.sin(th)
    T = sp.diag(*Tang) if scalar is None else None
    tot, norm = 0, None
    for i in range(4):
        for j in range(i + 1, 4):
            Kc = [0] * 4
            Kc[j] += x[i]
            Kc[i] -= x[j]                                    # x_i d_j - x_j d_i
            Kv = sp.Matrix(Kc)
            KY = sp.simplify(gSi * J.T * Kv)                  # components in (th, phi1, phi2) (K tangent to S^3)
            if scalar is not None:
                dv = sum(KY[m] * sp.diff(scalar, Y[m]) for m in range(3))
                integrand = dv ** 2 * vol
            else:
                LT = sp.zeros(3)
                for a in range(3):
                    for b in range(3):
                        LT[a, b] = (sum(KY[c] * sp.diff(T[a, b], Y[c]) for c in range(3))
                                    + sum(T[c, b] * sp.diff(KY[c], Y[a]) for c in range(3))
                                    + sum(T[a, c] * sp.diff(KY[c], Y[b]) for c in range(3)))
                integrand = sum(gSi[a, c] * gSi[b, d] * LT[a, b] * LT[c, d]
                                for a in range(3) for b in range(3) for c in range(3) for d in range(3)) * vol
            integrand = sp.expand(sp.simplify(integrand))
            val = sp.integrate(sp.integrate(sp.integrate(integrand, (p1, 0, 2 * sp.pi)), (p2, 0, 2 * sp.pi)),
                               (th, 0, sp.pi / 2))
            tot += sp.simplify(val)
    if scalar is not None:
        nrm = sp.integrate(sp.integrate(sp.integrate(scalar ** 2 * vol, (p1, 0, 2 * sp.pi)), (p2, 0, 2 * sp.pi)),
                           (th, 0, sp.pi / 2))
    else:
        T = sp.diag(*Tang)
        nn = sum(gSi[a, c] * gSi[b, d] * T[a, b] * T[c, d] for a in range(3) for b in range(3) for c in range(3)
                 for d in range(3)) * vol
        nrm = sp.integrate(sp.integrate(sp.integrate(sp.expand(sp.simplify(nn)), (p1, 0, 2 * sp.pi)),
                                        (p2, 0, 2 * sp.pi)), (th, 0, sp.pi / 2))
    return sp.simplify(tot / nrm)


def tensor_constant(l, weight_shift=4, b1=Fr(6, 5), b2=Fr(2)):
    kappa = b2 / (b2 - b1)
    finv = 1 / (1 - 1 / b1 ** 2)
    L = l * (l + 2)
    q = Fr(1, (l + 1) ** 2)
    w = weight_shift + 1                                    # (L + weight_shift) + 1 on int r |u|^2
    return (2 + Fr(w, L)) * (1 + kappa * q) + q * (L + w) * q + q * finv


def main():
    print('tensorzero5: the zero-energy bound of L_b0 on the tensor-type blocks of the class, through the horizon')
    harm = {}
    for l in (2, 4):
        AB, n = tt_harmonic(l)
        harm[l] = AB
        print('  T1: l = %d: %d invariant TT harmonic; A = %s, B = %s (c = cos^2 theta)' % (l, n, AB[0] if AB else '-',
                                                                                            AB[1] if AB else '-'))
    OK['T1'] = all(harm[l] is not None for l in harm)
    ok2, ok3 = True, True
    for l in (2, 4):
        Tang = angular_tensor(harm[l])
        trh, div, iota, dR, h = gauge_and_dric(Tang)
        g2 = trh == 0 and all(sp.simplify(x) == 0 for x in div) and all(x == 0 for x in iota)
        P = r ** 3 - r
        AH = -r ** -3 * sp.diff(P * sp.diff(Hf, r), r) + l * (l + 2) * r ** -2 * Hf
        target = [0, 0] + [sp.Rational(1, 2) * r ** 2 * AH * x for x in Tang]
        diag_ok = all(sp.simplify(dR[i, i] - target[i]) == 0 for i in range(5))
        off_ok = all(sp.simplify(dR[i, j]) == 0 for i in range(5) for j in range(5) if i != j)
        ok2 = ok2 and g2
        ok3 = ok3 and diag_ok and off_ok
        print('  T2/T3: l = %d: tr h = %s, div h = 0: %s, iota_{dt#} h = 0: %s; D Ric(h) = (1/2) r^2 (A_l H) T in the '
              'angular block: %s, every other component 0: %s' % (
                  l, trh, all(sp.simplify(x) == 0 for x in div), all(x == 0 for x in iota), diag_ok, off_ok))
    OK['T2'] = ok2
    OK['T3'] = ok3
    cas = {l: casimir(angular_tensor(harm[l])) for l in (2,)}
    xs = sp.cos(th) * sp.cos(p1)
    sc = casimir(None, scalar=xs ** 2 - sp.Rational(1, 4))          # a scalar harmonic at l = 2 (degree 2, traceless)
    OK['T4'] = cas[2] == 2 * 4 + 4 and sc == 2 * 4
    print('  T4: sum over K_ij of ||L_K T||^2/||T||^2 at l = 2: %s (l (l + 2) + 4 = 12); for the scalar harmonic x1^2 '
          '- 1/4 at l = 2: %s (l (l + 2) = 8): %s' % (cas[2], sc, OK['T4']))
    Cl = {l: tensor_constant(l) for l in range(2, 201, 2)}
    sup_l = max(Cl, key=lambda q: Cl[q])
    mono = all(Cl[l] >= Cl[l + 2] for l in range(2, 199, 2))
    CT2 = Cl[sup_l]
    CT = math.sqrt(float(CT2))
    OK['T5'] = sup_l == 2 and mono and CT_PIN[0] < CT2 < CT_PIN[1]
    print('  T5 (deduced; exact rationals): C_T,l^2 = (2 + 5/L)(1 + kappa q) + q + 4 q^2 + q/f(b1), kappa = 5/2, '
          '1/f(b1) = 36/11: C_T,2^2 = %s = %.6f, decreasing in l (checked to l = 200; every term decreasing), tending to 2; '
          'C_T = %.4f, so ||h||_(1,-1) <= %.4f ||L-hat_b0(0) h||_(0,1) = %.4f ||2 L-hat_b0(0) h||_(0,1) on the t_l blocks '
          '(T3\'s factor 1/2): %s' % (CT2, float(CT2), CT, 2 * CT, CT, OK['T5']))
    rs, fns = ZE.test_functions()
    worst = 0.0
    for l in (2, 4, 6):
        L = l * (l + 2)
        for e in fns:
            Pm = rs ** 3 - rs
            Ae = -rs ** -3 * sp.diff(Pm * sp.diff(e, rs), rs) + L * rs ** -2 * e
            fu = sp.lambdify(rs, e, 'numpy')
            fd = sp.lambdify(rs, sp.diff(e, rs), 'numpy')
            fA = sp.lambdify(rs, Ae, 'numpy')
            Nn, Fn = ZE.norms_numeric(fu, fd, fA, L + 4)
            if Fn > 0:
                worst = max(worst, Nn / Fn)
    OK['T6'] = worst <= CT
    print('  T6 (floating point): 300 test functions x l in {2, 4, 6}, tensor weight L + 4: largest N_T/F = %.4f <= C_T '
          '= %.4f: %s' % (worst, CT, OK['T6']))
    # controls
    trace = [sp.Integer(1), sp.cos(th) ** 2, sp.sin(th) ** 2]
    trh, div, iota, dR, h = gauge_and_dric(trace)
    P = r ** 3 - r
    AH = -r ** -3 * sp.diff(P * sp.diff(Hf, r), r) + 2 * 4 * r ** -2 * Hf
    tgt = [0, 0] + [sp.Rational(1, 2) * r ** 2 * AH * x for x in trace]
    OK['C1'] = trh != 0 and not all(sp.simplify(dR[i, i] - tgt[i]) == 0 for i in range(5))
    print('  C1 (control): the trace part (s-type): tr h = %s != 0 and D Ric(h) != (1/2) r^2 (A_2 H) h: %s' % (
        trh, OK['C1']))
    OK['C2'] = cas[2] != 2 * 4
    print('  C2 (control): the scalar weight claimed on T at l = 2 (8): refuted by T4\'s %s: %s' % (cas[2], OK['C2']))
    CS2 = max(tensor_constant(l, weight_shift=0) for l in range(2, 201, 2))
    OK['C3'] = not (CT_PIN[0] < CS2 < CT_PIN[1])
    print('  C3 (control): T5 with the scalar weight L: C^2 = %.6f, outside the pinned interval: %s' % (
        float(CS2), OK['C3']))
    for k, v in OK.items():
        builtins.print(k, 'PASS' if v else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
