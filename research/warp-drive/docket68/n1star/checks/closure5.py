#!/usr/bin/env python3
"""closure5.py -- the three closures BEYOND5's Proposition B.4 asserted (D580), shown (D587).

Proposition B.4 (BEYOND5 3(b), the stage profiles at past null infinity) rested on three properties it asserted and did
not show (verifier 252, D580): (i) E_p's closure under d_v; (ii) the couplings' coefficients exact; (iii) the Taylor
remainder's ell-gains. Notation as in N1STAR-PROOF.md section 9.3: Cartesian X = (tau, x), r = |x|, xhat = x/r, v = tau +
r, d_v := d_v at fixed (r, xhat) = d_tau at fixed x, ell = xhat.d_x - d_tau (ell v = 0, ell r = 1), Omega the rotations
x_i d_j - x_j d_i; E_p the profiles with |d_X^a Omega^b d_th^j f| <= C r^-p, E_p^ell those with ell^j f in E_(p+j) as
well. An exact term is r^-p F(v, xhat, th), F smooth and bounded with all derivatives.

  K1 (exact, sympy) the derivatives of an exact term (F a quadratic with symbolic coefficients in (v, xhat), a generic
     local Taylor polynomial, p symbolic, checked exactly at five points with rational |x|): d_tau (r^-p F) = r^-p F_v;
     d_i (r^-p F) = r^-p xhat_i F_v + r^(-p-1) (-p xhat_i F + sum_j (delta_ij - xhat_i xhat_j) F_j); Omega_ij (r^-p F) =
     r^-p (xhat_i F_j - xhat_j F_i); ell (r^-p F) = -p r^(-p-1) F, with F_j the derivative in the j-th component of
     xhat, p symbolic. So Cartesian derivatives, Omega, d_th and ell map exact finite sums to exact finite sums (the
     order rising by 1 under ell), and products of exact sums are exact sums. Control: the radial term's sign flipped
     fails.
  K2 (exact, sympy) d_tau commutes with every d_i, every Omega_ij and ell, and ell with every Omega_ij, on a generic
     function of (tau, x) in four space dimensions; and Omega v = ell v = 0. So d_v = d_tau maps E_p to E_p and E_p^ell
     to E_p^ell: closure (i). Control: ell built with +d_tau does not annihilate v.
  K3 (exact, sympy) g0 = eta + mu(v) r^-2 dv (x) dv in the Cartesian chart, with dv = dtau + xhat.dx eta-null, has
     inverse eta^-1 - mu(v) r^-2 V (x) V, V := eta^-1 dv, and pulls back to -(1 - mu/r^2) dv^2 + 2 dv dr on the radial
     plane: the record's Vaidya. Its components and its inverse's are exact finite sums (orders 0 and 2), as are dv's
     (order 0) and dd v's (d_i d_j v = (delta_ij - xhat_i xhat_j)/r, order 1).
  K4 (exact enumeration, every order m <= 10) Lemma 5.1's weight count (N1STAR-PROOF.md:490-506: a derivative is d_X
     (weight 0), lam^-1 dv d_th (-1) or lam^(i-1) dphi_i d_th (i - 1); m_i has weight i, W weight 1, gh_i weight i; at
     most two derivatives per monomial; d_th only on the oscillating factors W, gh_i; the order is the sum of the
     weights) over every monomial of order m. A monomial contributes to a theta-mean only if it holds at least two
     oscillating factors, every oscillating profile having mean zero and every other factor (g0, m_i, dphi_i) being
     theta-independent. Then (a) the monomials of order m linear in gh_(m+1) with two oscillating factors are exactly W
     gh_(m+1) with two lam^-1 dv d_th: <Th gh_(m+1)>'s coefficients are built from g0, g0^-1, dv and W alone,
     exact, of order 3/2 (W_TT = r^-3/2 F) and in E_(3/2); (b) those holding dphi_m with two oscillating factors, at m
     >= 2, are exactly W W with one lam^-1 dv d_th: <Wm_phi(dphi_m)>'s coefficients are quadratic in W, exact, in E_3;
     no m_i and no dphi_i (i < m) enter either; closure (ii). At m = 1, dphi_1 d_th has weight 0, as d_X does, and the
     same holds with W W lam^-1 dv d_th dphi_1 d_th the only such monomial. Control: allowing three derivatives lets m_1
     enter (a)'s mean.
  K5 (exact, sympy; Z, delta quadratics with symbolic coefficients, at the same points) the chain rule for the Taylor
     remainder's argument: for Z(tau, x, th) and Theta = v/lam + s delta, ell [Z(., Theta)] = (ell Z)(., Theta) + s (ell
     delta) (d_th Z)(., Theta) and Omega_ij likewise, with no lam^-1 term, since ell v = Omega v = 0; d_tau and d_i
     carry lam^-1 dv (bounded at fixed lam). So the composite of an E_q^ell profile with Theta is in E_q^ell (constants
     depending on lam, uniform in s in [0, 1]), and the remainder delta^K/(K - 1)! int_0^1 (1 - s)^(K-1) (d_th^K Y)(.,
     v/lam + s delta) ds is in E_(K+q)^ell for Y in E_q^ell and delta in E_1^ell: closure (iii). Control: an ell with
     +d_tau leaves a lam^-1 term.

Labels: computed (exact) for K2-K3; K1 and K5 exact at five points with rational |x| for generic quadratics, a guard on
formulas that are the chain rule (deduced); K4 an exact enumeration at m <= 10, the statement for every m deduced (the
weights below m that a monomial linear in gh_(m+1) can spend are -1 in total, as the enumeration shows term by term).

    python3 checks/closure5.py
"""
import itertools
import sys

import sympy as sp

tau = sp.Symbol('tau', real=True)
X = sp.symbols('x1:5', real=True)
p = sp.Symbol('p', real=True)
lam, s = sp.symbols('lam s', positive=True)
r = sp.sqrt(sum(xi**2 for xi in X))
v = tau + r
xh = [xi / r for xi in X]


def ell(f, sign=-1):
    return sum(xh[i] * sp.diff(f, X[i]) for i in range(4)) + sign * sp.diff(f, tau)


def omega(f, i, j):
    return X[i] * sp.diff(f, X[j]) - X[j] * sp.diff(f, X[i])


PTS = [(1, 2, 2, 4), (2, 4, 5, 6), (1, 1, 1, 1), (2, 3, 6, 0), (-1, 2, -2, 4)]   # |x| = 5, 9, 2, 7, 5: rational


def zero(e):
    return sp.simplify(sp.expand(e)) == 0


def zero_at(e):
    """e == 0 at sample points with rational |x|, exactly, every other symbol kept"""
    return all(sp.simplify(sp.expand(e.subs(dict(zip(X, pt))))) == 0 for pt in PTS)


def generic(name, args, deg=2):
    """a polynomial of degree deg in args with symbolic coefficients (a generic local Taylor polynomial)"""
    cs = []
    terms = []
    for k in range(deg + 1):
        for mono in itertools.combinations_with_replacement(range(len(args)), k):
            c = sp.Symbol('%s_%s' % (name, ''.join(map(str, mono)) or 'c'))
            cs.append(c)
            terms.append(c * sp.Mul(*[args[i] for i in mono]))
    return sp.Add(*terms)


def k1():
    a = sp.symbols('a0:5')
    Fa = generic('F', a)
    sub = dict(zip(a, (v, *xh)))
    Fv = Fa.subs(sub)
    d = [sp.diff(Fa, a[k]).subs(sub) for k in range(5)]
    f = r**(-p) * Fv
    ok = zero_at(sp.diff(f, tau) - r**(-p) * d[0])
    for i in range(4):
        rhs = r**(-p) * xh[i] * d[0] + r**(-p - 1) * (-p * xh[i] * Fv + sum(((1 if i == j else 0) - xh[i] * xh[j])
                                                                          * d[j + 1] for j in range(4)))
        ok &= zero_at(sp.diff(f, X[i]) - rhs)
    ok &= zero_at(omega(f, 0, 1) - r**(-p) * (xh[0] * d[2] - xh[1] * d[1]))
    ok &= zero_at(ell(f) + p * r**(-p - 1) * Fv)
    bad = r**(-p) * xh[0] * d[0] + r**(-p - 1) * (+p * xh[0] * Fv + sum(((1 if j == 0 else 0) - xh[0] * xh[j]) * d[j + 1]
                                                                        for j in range(4)))
    ctl = not zero_at(sp.diff(f, X[0]) - bad)
    return ok, ctl


def k2():
    G = sp.Function('G')(tau, *X)
    ok = all(zero(sp.diff(sp.diff(G, X[i]), tau) - sp.diff(sp.diff(G, tau), X[i])) for i in range(4))
    ok &= all(zero(omega(sp.diff(G, tau), i, j) - sp.diff(omega(G, i, j), tau)) for i, j in ((0, 1), (1, 3)))
    ok &= zero(ell(sp.diff(G, tau)) - sp.diff(ell(G), tau))
    ok &= all(zero(ell(omega(G, i, j)) - omega(ell(G), i, j)) for i, j in ((0, 1), (2, 3)))
    ok &= zero(omega(v, 0, 2)) and zero(ell(v)) and zero(ell(r) - 1)
    ctl = not zero(ell(v, sign=+1))
    return ok, ctl


def k3():
    mu = sp.Function('mu')(v)
    eta = sp.diag(-1, 1, 1, 1, 1)
    dv = sp.Matrix([1] + xh)
    g0 = eta + mu / r**2 * dv * dv.T
    V = eta.inv() * dv
    gi = eta.inv() - mu / r**2 * V * V.T
    ok = zero((dv.T * eta.inv() * dv)[0]) and all(zero(e) for e in (g0 * gi - sp.eye(5)))
    # pull back to (v, R) on the ray x = R e_1: tau = v - R
    vv, R = sp.symbols('vv R', positive=True)
    sub = {tau: vv - R, X[0]: R, X[1]: 0, X[2]: 0, X[3]: 0}
    J = sp.Matrix([[1, -1], [0, 1], [0, 0], [0, 0], [0, 0]])          # d(tau, x)/d(v, R)
    gvr = (J.T * g0.subs(sub) * J).applyfunc(sp.simplify)
    mus = sp.Function('mu')(vv)
    ok &= zero(gvr[0, 0] + (1 - mus / R**2)) and zero(gvr[0, 1] - 1) and zero(gvr[1, 1])
    ok &= all(zero(sp.diff(v, X[i], X[j]) - ((1 if i == j else 0) - xh[i] * xh[j]) / r)
              for i in range(4) for j in range(4))
    return ok


def multisets(facs, w, start=0):
    """every multiset of facs (in list order) whose weights sum to w, w >= 0 (the empty one at w = 0, which carries only
    g0 factors and is kept: a d_X-only monomial of g0)"""
    if w == 0:
        yield ()
        return
    for k in range(start, len(facs)):
        if facs[k][1] <= w:
            for rest in multisets(facs, w - facs[k][1], k):
                yield (facs[k],) + rest


def monomials(m, nder=2):
    """every monomial of order m with at most nder derivatives: derivative types ('dX', 0), ('D0', -1), ('D', i, i - 1)
    for i = 1..m+1; factors W (1, osc), gh_i (i, osc, 2 <= i <= m+1), mm_i (i, 1 <= i <= m); g0 implicit (weight 0).
    d_th-type derivatives act on oscillating factors only, so a monomial with one needs an oscillating factor."""
    ders = [('dX', 0), ('D0', -1)] + [('D%d' % i, i - 1) for i in range(1, m + 2)]
    facs = ([('W', 1, True)] + [('gh%d' % i, i, True) for i in range(2, m + 2)]
            + [('m%d' % i, i, False) for i in range(1, m + 1)])
    out = []
    for k in range(nder + 1):
        for dset in itertools.combinations_with_replacement(ders, k):
            dw = sum(d[1] for d in dset)
            rest = m - dw
            if rest < 0:
                continue
            for fset in multisets(facs, rest):
                if True:
                    if any(d[0] != 'dX' for d in dset) and not any(f[2] for f in fset):
                        continue
                    out.append((tuple(d[0] for d in dset), tuple(f[0] for f in fset), sum(f[2] for f in fset)))
    return out


def k4(mmax=10):
    ok = True
    for m in range(1, mmax + 1):
        mons = monomials(m)
        th = {(d, f) for d, f, osc in mons if f.count('gh%d' % (m + 1)) == 1 and osc >= 2}
        ok &= th == {(('D0', 'D0'), tuple(sorted(('W', 'gh%d' % (m + 1)))))}
        ph = {(d, f) for d, f, osc in mons if 'D%d' % m in d and osc >= 2}
        ok &= ph == {(('D0', 'D%d' % m), ('W', 'W'))}
    ctl3 = any('m1' in f for d, f, osc in monomials(2, nder=3) if f.count('gh3') == 1 and osc >= 2)
    return ok, ctl3


def k5():
    th = sp.Symbol('th')
    Zf = generic('Z', (tau, *X, th))
    dl = generic('d', (tau, *X))
    Th = v / lam + s * dl
    zc = Zf.subs(th, Th)
    lz = sum(xh[i] * sp.diff(Zf, X[i]) for i in range(4)) - sp.diff(Zf, tau)
    want = lz.subs(th, Th) + s * ell(dl) * sp.diff(Zf, th).subs(th, Th)
    ok = zero_at(ell(zc) - want)
    oz = ((X[0] * sp.diff(Zf, X[1]) - X[1] * sp.diff(Zf, X[0])).subs(th, Th)
          + s * omega(dl, 0, 1) * sp.diff(Zf, th).subs(th, Th))
    ok &= zero_at(omega(zc, 0, 1) - oz)
    bad = ell(zc, sign=+1) - ((sum(xh[i] * sp.diff(Zf, X[i]) for i in range(4)) + sp.diff(Zf, tau)).subs(th, Th)
                              + s * ell(dl, sign=+1) * sp.diff(Zf, th).subs(th, Th))
    ctl = not zero_at(bad)
    return ok, ctl


def main():
    res = {}
    a, c = k1()
    res['K1'] = a
    res['K1ctl'] = c
    print('  K1: d_tau, d_i, Omega and ell of r^-p F(v, xhat): exact sums as stated: %s; control (sign flipped) '
          'rejected: %s'
          % (a, c))
    a, c = k2()
    res['K2'] = a
    res['K2ctl'] = c
    print('  K2: d_tau commutes with d_i, Omega, ell; ell with Omega; Omega v = ell v = 0, ell r = 1: %s; control: %s'
          % (a, c))
    a = k3()
    res['K3'] = a
    print('  K3: g0 = eta + mu r^-2 dv dv, its inverse eta^-1 - mu r^-2 V V, the Vaidya pull-back, dd v = '
          '(delta - xhat xhat)/r: %s' % a)
    a, c = k4()
    res['K4'] = a
    res['K4ctl'] = c
    print('  K4: m <= 10: the mean couplings are W gh_(m+1) (two lam^-1 dv d_th) and W W dphi_m (one): %s; control '
          '(three '
          'derivatives) lets m_1 in: %s' % (a, c))
    a, c = k5()
    res['K5'] = a
    res['K5ctl'] = c
    print('  K5: ell and Omega of Z(., v/lam + s delta): no lam^-1 term: %s; control (+d_tau): %s' % (a, c))
    for k, val in res.items():
        print(k, 'PASS' if val else 'FAIL')
    return 0 if all(res.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
