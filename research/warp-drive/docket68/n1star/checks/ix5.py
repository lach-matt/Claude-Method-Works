#!/usr/bin/env python3
"""ix5.py -- the pointwise identities behind Part IX (gauge equivalence of the linear solution).  Labels: computed.

Conventions (Part IX section 0): (delta k)_mu = -nabla^a k_{a mu}, G k = k - (1/2) g tr k, delta^* w = (1/2)(nabla w +
nabla w^T), Theta := delta G, K(X, Y) = g(nabla_X nu, Y) with nu the future unit normal.

  X1 (computed) Flat R^{1+4}: DRic(k) + delta^* Theta(k) = -(1/2) box k, for every symmetric k (all 15 components
     arbitrary functions).  So 2(DRic + delta^* Theta) has principal symbol g^{-1}(zeta, zeta).  Control: with
     -delta^* Theta the identity fails.
  X2 (computed) Flat R^{1+4}: 2 Theta(delta^* w) = -box w for every 1-form w.  Control: dropping the trace term of G
     fails.
  X3 (computed) On a curved metric in three dimensions with g_{0i} != 0 at Sigma = {t = 0} (the identity is pointwise
     and dimension-free), for k with k = 0 on Sigma: the derivative at s = 0 of the second fundamental form of Sigma for
     g + s k is (1/2)(nabla_nu k) on T Sigma.  Control: the factor 1 fails.
  X4 (computed) Same setting: Theta(k)(e_j) = (nabla_nu k)(nu, e_j) and Theta(k)(nu) = (1/2)(nabla_nu k)(nu, nu)
     + (1/2) sum_i (nabla_nu k)(e_i, e_i), e_i an orthonormal frame of T Sigma.  Control: the factor 1/2 on the
     tangential trace replaced by 1 fails.
  X5 (computed) Same setting: if X = 0 on Sigma and nabla_nu X = Y := sum_j k(nu, e_j) e_j - (1/2) k(nu, nu) nu, then
     L_X g = k on Sigma, for every k with k(e_i, e_j) = 0 on Sigma.  Control: Y with +1/2 fails.
  X6 (computed) At five-dimensional Tangherlini, DRic(L_X g) = 0 for X = a(t, r) d_t + b(t, r) d_r (a, b arbitrary);
     DRic is the s-derivative at 0 of the Ricci tensor of g + s L_X g, assembled from its Christoffel symbols to first
     order in s.  Control: at the four-dimensional lapse F = 1 - mu/r (not Ricci-flat in five dimensions) it fails.

X1 and X2 are decided by exact expansion.  X3-X6 are identities between rational expressions (with square roots) in the
coordinates and the jets of the arbitrary functions; each is decided by evaluation at four random rational points to 60
digits, every coordinate and every jet an independent random rational (polynomial identity testing; seed fixed).  An
identity holds if every residual is below 1e-45; a control fails if some residual exceeds 1e-6.
"""
import sys
import random
import sympy as sp
from sympy.core.function import AppliedUndef

DIG = 60


def residuals(e, pts=4, seed=5, ranges=None):
    """|e| at random rational points: jets and arbitrary functions first become symbols, then every symbol a rational"""
    e = sp.sympify(e)
    rep = {d: sp.Symbol('J%d' % i) for i, d in enumerate(sorted(e.atoms(sp.Derivative), key=str))}
    e = e.xreplace(rep)
    rep = {f: sp.Symbol('F%d' % i) for i, f in enumerate(sorted(e.atoms(AppliedUndef), key=str))}
    e = e.xreplace(rep)
    rng = random.Random(seed); ranges = ranges or {}; out = []
    syms = sorted(e.free_symbols, key=str)
    for _ in range(pts):
        val = {}
        for s_ in syms:
            lo, hi = ranges.get(str(s_), (-2, 2))
            val[s_] = sp.Rational(rng.randint(int(100 * lo), int(100 * hi)), 100)
        out.append(abs(sp.N(e.xreplace(val), DIG)))
    return out


def holds(es, **kw):
    return all(r < 1e-45 for e in es for r in residuals(e, **kw))


def fails(es, **kw):
    return any(r > 1e-6 for e in es for r in residuals(e, **kw))


def christoffel(g, X, gi=None):
    n = len(X); gi = g.inv() if gi is None else gi
    return [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                  for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)], gi


def cov_k(k, Gm, X):
    """nabla_c k_{ab} as T[c][a][b]"""
    n = len(X)
    return [[[sp.diff(k[a, b], X[c]) - sum(Gm[d][c][a] * k[d, b] + Gm[d][c][b] * k[a, d] for d in range(n))
              for b in range(n)] for a in range(n)] for c in range(n)]


def theta(k, g, X):
    """Theta(k)_mu = -nabla^a k_{a mu} + (1/2) d_mu tr k"""
    n = len(X); Gm, gi = christoffel(g, X); Dk = cov_k(k, Gm, X)
    tr = sum(gi[a, b] * k[a, b] for a in range(n) for b in range(n))
    return [-sum(gi[a, c] * Dk[c][a][m] for a in range(n) for c in range(n)) + sp.diff(tr, X[m]) / 2 for m in range(n)]


def flat_checks():
    X = sp.symbols('x0:5', real=True)
    eta = sp.diag(-1, 1, 1, 1, 1)
    box = lambda f: sum(eta[a, a] * sp.diff(f, X[a], 2) for a in range(5))
    k = sp.zeros(5)
    for a in range(5):
        for b in range(a, 5):
            k[a, b] = k[b, a] = sp.Function('k%d%d' % (a, b))(*X)
    # DRic in flat space: (1/2)(-box k_ab + d_a d^c k_cb + d_b d^c k_ca - d_a d_b tr k)
    tr = sum(eta[a, a] * k[a, a] for a in range(5))
    div = [sum(eta[c, c] * sp.diff(k[c, b], X[c]) for c in range(5)) for b in range(5)]
    DRic = sp.Matrix(5, 5, lambda a, b: (-box(k[a, b]) + sp.diff(div[b], X[a]) + sp.diff(div[a], X[b])
                                          - sp.diff(tr, X[a], X[b])) / 2)
    th = [-div[m] + sp.diff(tr, X[m]) / 2 for m in range(5)]
    dstar = lambda w: sp.Matrix(5, 5, lambda a, b: (sp.diff(w[b], X[a]) + sp.diff(w[a], X[b])) / 2)
    lhs = DRic + dstar(th)
    r1 = all(sp.expand(lhs[a, b] + box(k[a, b]) / 2) == 0 for a in range(5) for b in range(5))
    c1 = all(sp.expand(DRic[a, b] - dstar(th)[a, b] + box(k[a, b]) / 2) == 0 for a in range(5) for b in range(5))
    w = [sp.Function('w%d' % a)(*X) for a in range(5)]
    ds = dstar(w)
    trd = sum(eta[a, a] * ds[a, a] for a in range(5))
    thd = [-sum(eta[c, c] * sp.diff(ds[c, m], X[c]) for c in range(5)) + sp.diff(trd, X[m]) / 2 for m in range(5)]
    r2 = all(sp.expand(2 * thd[m] + box(w[m])) == 0 for m in range(5))
    thd_c = [-sum(eta[c, c] * sp.diff(ds[c, m], X[c]) for c in range(5)) for m in range(5)]
    c2 = all(sp.expand(2 * thd_c[m] + box(w[m])) == 0 for m in range(5))
    return r1, c1, r2, c2


def curved_setting():
    t, x, y = sp.symbols('t x y', real=True)
    X = [t, x, y]
    # a curved metric with g_{0i} != 0 at t = 0
    g = sp.Matrix([[-1 - x**2 / 5 + t * y / 7, x / 3 + t / 11, y / 4],
                   [x / 3 + t / 11, 1 + y**2 / 6 + t * x / 13, x * y / 9],
                   [y / 4, x * y / 9, 1 + x**2 / 7 + t / 3]])
    A = sp.Matrix(3, 3, lambda a, b: sp.Function('A%d%d' % (min(a, b), max(a, b)))(x, y))
    B = sp.Matrix(3, 3, lambda a, b: sp.Function('B%d%d' % (min(a, b), max(a, b)))(x, y))
    k = t * A + t**2 * B                      # k = 0 on Sigma = {t = 0}
    return X, g, k


def normal_and_frame(g, gi):
    """future unit normal nu (vector) and an orthonormal frame of T Sigma (Gram-Schmidt), as column vectors"""
    dt = sp.Matrix([1, 0, 0])
    nn = (dt.T * gi * dt)[0]
    nu = -(gi * dt) / sp.sqrt(-nn)            # future pointing: dt(nu) > 0
    e = []
    for v in (sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])):
        for f in e:
            v = v - (f.T * g * v)[0] * f
        e.append(v / sp.sqrt((v.T * g * v)[0]))
    return nu, e


RANGES = {'x': (-0.5, 0.5), 'y': (-0.5, 0.5)}         # where the metric of curved_setting is Lorentzian


def x3_x5():
    X, g, k = curved_setting()
    t = X[0]
    s = sp.Symbol('s')
    sub0 = {t: 0}
    gi = g.inv()
    Gm, _ = christoffel(g, X, gi)
    E = [sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])]
    # X3: K_s(E_i, E_j) = g_s(nabla^s_{E_i} nu_s, E_j); g_s^{-1} = g^{-1} - s g^{-1} k g^{-1} + O(s^2) suffices
    gs = g + s * k; gis = gi - s * gi * k * gi
    Gs, _ = christoffel(gs, X, gis)
    dt = sp.Matrix([1, 0, 0]); nus = -(gis * dt) / sp.sqrt(-(dt.T * gis * dt)[0])
    nab = lambda v, w, G: sp.Matrix([sum(v[c] * sp.diff(w[a], X[c]) for c in range(3))
                                     + sum(G[a][c][d] * v[c] * w[d] for c in range(3) for d in range(3))
                                     for a in range(3)])
    Ks = sp.Matrix(2, 2, lambda i, j: (nab(E[i], nus, Gs).T * gs * E[j])[0])
    Kdot = Ks.diff(s).subs(s, 0).subs(sub0)
    nu, e0 = normal_and_frame(g, gi)
    nu0 = nu.subs(sub0); e0 = [v.subs(sub0) for v in e0]
    Dk = cov_k(k, Gm, X)
    kp = lambda u, v: sum(nu[c] * Dk[c][a][b] * u[a] * v[b] for c in range(3) for a in range(3)
                          for b in range(3)).subs(sub0)                # (nabla_nu k)(u, v) at Sigma
    want = sp.Matrix(2, 2, lambda i, j: kp(E[i], E[j]) / 2)
    r3 = holds(list(Kdot - want), ranges=RANGES)
    c3 = not fails(list(Kdot - 2 * want), ranges=RANGES)
    # X4: Theta(k) at t = 0 in an orthonormal frame
    th = [c.subs(sub0) for c in theta(k, g, X)]
    th_on = lambda v: sum(th[m] * v[m] for m in range(3))                # Theta is a 1-form
    tang = sum(kp(ei, ei) for ei in e0)
    r4 = holds([th_on(ej) - kp(nu0, ej) for ej in e0] + [th_on(nu0) - kp(nu0, nu0) / 2 - tang / 2], ranges=RANGES)
    c4 = not fails([th_on(nu0) - kp(nu0, nu0) / 2 - tang], ranges=RANGES)
    # X5: k1 := nu^flat (x) c + c (x) nu^flat + c0 nu^flat (x) nu^flat, so k1(e_i, e_j) = 0; X = t Y / nu(t), so X = 0
    # on Sigma and nabla_nu X = Y there; then L_X g = k1 on Sigma
    nu_flat = g.subs(sub0) * nu0
    c1v = sp.Matrix([sp.Function('c1')(X[1], X[2]), sp.Function('c2')(X[1], X[2]), 0])
    cc = sp.Function('c0')(X[1], X[2])
    k1 = (nu_flat * c1v.T + c1v * nu_flat.T) + cc * nu_flat * nu_flat.T
    k1nu = lambda v: (nu0.T * k1 * v)[0]
    lam = nu0[0]                                                        # nu(t) at Sigma

    def lie(Yv):
        Xf = g * (t * Yv / lam)                                         # X^flat
        return sp.Matrix(3, 3, lambda a, b: sp.diff(Xf[b], X[a]) + sp.diff(Xf[a], X[b])
                         - 2 * sum(Gm[d][a][b] * Xf[d] for d in range(3))).subs(sub0)
    tsum = sum((k1nu(ej) * ej for ej in e0), sp.zeros(3, 1))
    r5 = holds(list(lie(tsum - k1nu(nu0) / 2 * nu0) - k1), ranges=RANGES)
    c5 = not fails(list(lie(tsum + k1nu(nu0) / 2 * nu0) - k1), ranges=RANGES)
    return r3, c3, r4, c4, r5, c5


def ricci_dot(g, k, C):
    """d/ds at 0 of Ric(g + s k): Christoffels to first order in s, then R_bd = d_a G^a_bd - d_d G^a_ba + G G - G G"""
    n = len(C); gi = g.inv()
    G0, _ = christoffel(g, C, gi)
    gik = gi * k * gi
    G1 = [[[sum(gi[a, d] * (sp.diff(k[d, b], C[c]) + sp.diff(k[d, c], C[b]) - sp.diff(k[b, c], C[d]))
                - gik[a, d] * (sp.diff(g[d, b], C[c]) + sp.diff(g[d, c], C[b]) - sp.diff(g[b, c], C[d]))
                for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    R = sp.zeros(n)
    for b in range(n):
        for d in range(b, n):
            R[b, d] = R[d, b] = (sum(sp.diff(G1[a][b][d], C[a]) - sp.diff(G1[a][b][a], C[d]) for a in range(n))
                                 + sum(G1[a][a][e] * G0[e][b][d] + G0[a][a][e] * G1[e][b][d]
                                       - G1[a][d][e] * G0[e][b][a] - G0[a][d][e] * G1[e][b][a]
                                       for a in range(n) for e in range(n)))
    return R


def x6():
    t, r, th, p1, p2 = sp.symbols('t r theta phi1 phi2', real=True)
    C = [t, r, th, p1, p2]
    mu = sp.Symbol('mu', positive=True)
    rng = {'r': (1, 2), 'mu': (0.1, 0.5), 'theta': (0.2, 1.2)}
    out = []
    for F in (1 - mu / r**2, 1 - mu / r):
        g = sp.diag(-F, 1 / F, r**2, r**2 * sp.cos(th)**2, r**2 * sp.sin(th)**2)
        Xv = [sp.Function('a')(t, r), sp.Function('b')(t, r), 0, 0, 0]
        LX = sp.Matrix(5, 5, lambda i, j: sum(Xv[c] * sp.diff(g[i, j], C[c]) for c in range(5))
                       + sum(g[c, j] * sp.diff(Xv[c], C[i]) + g[i, c] * sp.diff(Xv[c], C[j]) for c in range(5)))
        R = ricci_dot(g, LX, C)
        out.append([R[i, j] for i in range(5) for j in range(i, 5)])
    return holds(out[0], ranges=rng), not fails(out[1], ranges=rng)


def main():
    ok = True
    r1, c1, r2, c2 = flat_checks()
    print('X1 DRic + delta^* Theta = -(1/2) box (flat):', 'PASS' if r1 else 'FAIL', '| control with -delta^* Theta:', c1)
    print('X2 2 Theta delta^* = -box (flat):', 'PASS' if r2 else 'FAIL', '| control without the trace term:', c2,
          flush=True)
    ok &= r1 and not c1 and r2 and not c2
    r3, c3, r4, c4, r5, c5 = x3_x5()
    print('X3 Kdot = (1/2) nabla_nu k on T Sigma (k = 0 on Sigma):', 'PASS' if r3 else 'FAIL', '| control factor 1:', c3)
    print('X4 Theta(k) at Sigma in the frame:', 'PASS' if r4 else 'FAIL', '| control tangential trace 1:', c4)
    print('X5 L_X g = k on Sigma for the Y of the construction:', 'PASS' if r5 else 'FAIL', '| control +1/2:', c5,
          flush=True)
    ok &= r3 and not c3 and r4 and not c4 and r5 and not c5
    t5, t4 = x6()
    print('X6 DRic(L_X g) = 0 at 5D Tangherlini:', 'PASS' if t5 else 'FAIL', '| control (4D lapse):', t4)
    ok &= t5 and not t4
    print('ix5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
