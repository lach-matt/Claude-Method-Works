#!/usr/bin/env python3
"""lhor5.py -- the horizon threshold of the linearised gauge-fixed Einstein operator at n = 4 (Part III.F'',
proof5/PART-III-F3-MODES.md; [Hin26] footnote 78 in five dimensions).  Labels: computed (exact, sympy).

On five-dimensional Tangherlini in the ingoing chart (v, r, chi, theta, phi), g = -f dv^2 + 2 dv dr + r^2 (round S^3),
f = 1 - mu/r^2, mu = 1 (the homothety t, r -> lam t, lam r carries mu to mu/lam^2 and leaves the threshold quantity,
a number, unchanged), r_h = 1, f'(r_h) = 2.  The first-order part of 2 L_b near the horizon is
P := -nabla^a nabla_a + 2 E^C delta G + 2 delta* E^Ups G on symmetric 2-tensors, with E^C w = gam_C (2 c_C (x)_s w -
(2/3)(1 - e_C) g <c_C, w>) and, near the horizon, E^Ups = gam_H E_H, E_H h = 2 iota_(c_H#) h - (2/3) c_H tr h (thresh5.py
U3's), c_C = a_v dv + a_r dr and c_H = c_v dv + c_r dr their values at r_h (only the values there enter: the
curvature and E^C E^Ups G terms are of order zero).  As in thresh5.py U3, P is conjugated to half densities by |dg|,
and K := (p_1 - (2i)^-1 sum_j d_(x_j) d_(zeta_j) p_2)/(i xi f'(r_h)) at zeta = xi dr, r = r_h, in the coordinate
components h_ab (a <= b).

  H1 (computed, exact) The background: at gam_C = gam_H = 0 the characteristic polynomial of K is
     (k - 2)(k + 2)(k - 1)^3 (k + 1)^3 k^7, the sums of two of the 1-form values 1, -1, 0, 0, 0 (thresh5.py U3):
     vartheta_H+ = 2, the threshold s > 5/2, [Hin26] footnote 78's at n = 3 as well.  Control: the 1-form values
     claimed for the tensor, k^2 - 1 times k^3.
  H2 (computed, exact) The modifications: for every gam_C, a_v, a_r, e_C, gam_H, c_v, c_r, the characteristic
     polynomial of K is that of K at gam_C = gam_H = 0 times nothing else when a_v = c_v = 0; in general it is printed,
     factored.  Control: the term 2 E^C delta G with its sign reversed.

Run: python3 lhor5.py (a few minutes).
"""
import sys
import itertools
import sympy as sp

v, r, ch, th, ph = sp.symbols('v r chi theta phi', real=True)
X = [v, r, ch, th, ph]
N = 5
gC, gH, eC, av, ar, cv, cr, xi, k = sp.symbols('gamma_C gamma_H e_C a_v a_r c_v c_r xi k')
mu = 1
f = 1 - mu / r**2
g = sp.zeros(N, N)
g[0, 0] = -f
g[0, 1] = g[1, 0] = 1
g[2, 2] = r**2
g[3, 3] = r**2 * sp.sin(ch)**2
g[4, 4] = r**2 * sp.sin(ch)**2 * sp.sin(th)**2
gi = g.inv().applyfunc(sp.simplify)
vol = r**3 * sp.sin(ch)**2 * sp.sin(th)
Gam = [[[sp.simplify(sum(gi[c_, d] * (sp.diff(g[d, a], X[b]) + sp.diff(g[d, b], X[a]) - sp.diff(g[a, b], X[d]))
                         for d in range(N)) / 2) for b in range(N)] for a in range(N)] for c_ in range(N)]
PAIRS = [(a, b) for a in range(N) for b in range(a, N)]
POINT = {r: 1, ch: sp.asin(sp.Rational(3, 5)), th: sp.asin(sp.Rational(5, 13)), ph: sp.Rational(1, 3)}


def nabla2(h):
    """(nabla_c h)_ab"""
    return [[[sp.diff(h[a][b], X[c_]) - sum(Gam[d][c_][a] * h[d][b] + Gam[d][c_][b] * h[a][d] for d in range(N))
              for b in range(N)] for a in range(N)] for c_ in range(N)]


def rough(h):
    Dh = nabla2(h)
    out = [[0] * N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            s = 0
            for c_ in range(N):
                for e_ in range(N):
                    if gi[c_, e_] == 0:
                        continue
                    term = sp.diff(Dh[c_][a][b], X[e_])
                    term -= sum(Gam[d][e_][c_] * Dh[d][a][b] + Gam[d][e_][a] * Dh[c_][d][b] + Gam[d][e_][b] * Dh[c_][a][d]
                                for d in range(N))
                    s += gi[c_, e_] * term
            out[a][b] = s
    return out


def tr(h):
    return sum(gi[a, b] * h[a][b] for a in range(N) for b in range(N))


def Gop(h):
    t = tr(h)
    return [[h[a][b] - sp.Rational(1, 2) * g[a, b] * t for b in range(N)] for a in range(N)]


def delta(h):
    Dh = nabla2(h)
    return [-sum(gi[a, c_] * Dh[c_][a][b] for a in range(N) for c_ in range(N)) for b in range(N)]


def dstar(w):
    return [[sp.Rational(1, 2) * (sp.diff(w[b], X[a]) + sp.diff(w[a], X[b]))
             - sum(Gam[c_][a][b] * w[c_] for c_ in range(N)) for b in range(N)] for a in range(N)]


def EC(w, sign=1):
    c = [av, ar, 0, 0, 0]
    cw = sum(gi[a, b] * c[a] * w[b] for a in range(N) for b in range(N))
    return [[sign * gC * ((c[a] * w[b] + c[b] * w[a]) - sp.Rational(2, 3) * (1 - eC) * g[a, b] * cw)
             for b in range(N)] for a in range(N)]


def EH(h):
    c = [cv, cr, 0, 0, 0]
    cs = [sum(gi[a, b] * c[b] for b in range(N)) for a in range(N)]
    t = tr(h)
    return [gH * (2 * sum(cs[a] * h[a][b] for a in range(N)) - sp.Rational(2, 3) * c[b] * t) for b in range(N)]


def Kmatrix(sign=1):
    w = {p: sp.Function('w%d%d' % p)(*X) for p in PAIRS}
    h = [[vol**sp.Rational(-1, 2) * w[(min(a, b), max(a, b))] for b in range(N)] for a in range(N)]
    R = rough(h)
    Gh = Gop(h)
    A = EC(delta(Gh), sign)
    B = dstar(EH(Gh))
    z = sp.symbols('z0:%d' % N)
    K = sp.zeros(len(PAIRS), len(PAIRS))
    for i, (a, b) in enumerate(PAIRS):
        P = sp.expand(vol**sp.Rational(1, 2) * (-R[a][b] + 2 * A[a][b] + 2 * B[a][b]))
        for j, q in enumerate(PAIRS):
            fn = w[q]
            p2 = 0
            for c_, d in itertools.combinations_with_replacement(range(N), 2):
                der = sp.Derivative(fn, X[c_], X[d]) if c_ != d else sp.Derivative(fn, X[c_], 2)
                coef = P.coeff(der)
                if coef != 0:
                    p2 += coef * (sp.I * z[c_]) * (sp.I * z[d])
            p1 = sum(P.coeff(sp.Derivative(fn, X[c_])) * (sp.I * z[c_]) for c_ in range(N))
            sub = p1 - sum(sp.diff(sp.diff(p2, X[c_]), z[c_]) for c_ in range(N)) / (2 * sp.I)
            at = sub.subs({z[0]: 0, z[1]: xi, z[2]: 0, z[3]: 0, z[4]: 0})
            at = sp.simplify(at.subs(POINT) / (sp.I * xi))
            K[i, j] = at / 2                                          # f'(r_h) = 2
    return K.applyfunc(sp.simplify)


def run():
    K = Kmatrix()
    K0 = K.subs({gC: 0, gH: 0})
    cp0 = sp.factor(K0.charpoly(k).as_expr())
    want = sp.expand((k - 2) * (k + 2) * (k - 1)**3 * (k + 1)**3 * k**7)
    h1 = sp.expand(cp0 - want) == 0
    ctrl1 = sp.expand(cp0 - sp.expand((k**2 - 1) * k**13)) != 0
    print('H1 background charpoly', cp0, ':', 'PASS' if h1 and ctrl1 else 'FAIL')
    cp = sp.factor(K.charpoly(k).as_expr())
    print('H2 charpoly with the modifications:', cp)
    cpv = sp.factor(sp.expand(cp.subs({av: 0, cv: 0})))
    h2 = sp.expand(cpv - want) == 0
    Km = Kmatrix(sign=-1)
    cpm = sp.factor(Km.charpoly(k).as_expr())
    ctrl2 = sp.expand(cpm - cp) != 0
    print('H2 at a_v = c_v = 0 equals the background:', 'PASS' if h2 and ctrl2 else 'FAIL',
          '(control: sign of E^C reversed changes it)' if ctrl2 else '(CONTROL DID NOT FAIL)')
    ok = h1 and ctrl1 and h2 and ctrl2
    print('lhor5.py:', 'all checks pass' if ok else 'FAILURES')
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
