#!/usr/bin/env python3
"""linroots5.py -- checks behind Part III.F' (proof5/PART-III-F2-INDICIAL.md, D230): [Hin26] sections 8.2-8.3 at n = 4,
the facts proved there by hand.  Labels: computed (exact, sympy).

On Minkowski space R^(1+4), gbar = -dt^2 + dx^2, r = |x|, with the definitions of lin5.py (from [Hin26] (6.5), (7.3),
(8.1)): E^Ups h = -gam_U (2 iota_(c_U#) h - m (1 - e_U) c_U tr h), c_U = r^-1 dt; E^C w = gam_C (2 c (x)_s w - m (1 -
e_C) gbar <c, w>), c = r^-1 (dt - v dr); m = 2/3; delta_E := delta + E, delta*_E := delta* + E; box^Ups = 2 delta_(E^Ups)
G delta*, box^C = 2 delta G delta*_(E^C), L = D Ric + delta*_(E^C) delta_(E^Ups) G, delta = -div, G h = h - (1/2) gbar
tr h.  Every parameter is symbolic (gam_U, e_U, gam_C, e_C, v positive symbols).

  R1 (computed, exact) The vector type 1 roots of box^C: for V = (W x) . dx, W in so(4) (a Killing rotation),
     box^C(r^(-lam-1) V) = -(lam - 3)(lam + 1 + 2 gam_C v) r^(-lam-3) V for symbolic lam.  So the roots are 3 and
     -1 - 2 gam_C v.  Control: the claimed factor (lam - 2) in place of (lam - 3).
  R2 (computed, exact) The scalar type 0 state of Lemma 2.5: Omega := -t dt + A r dt + B r dr with the unique (A, B)
     making box^Ups Omega = 0; then h := delta* Omega is stationary, homogeneous of degree 0, nonzero, L h = 0 and
     delta_(E^Ups) G h = 0.  Control: A = B = 0, where delta_(E^Ups) G h = -(1/2) box^Ups(-t dt) is not zero.
  R3 (computed, exact) The scalar type 2 state: for S = x1^2 - x2^2, the 1-forms of scalar type 2 homogeneous of degree
     1 are spanned by (S/r) dt, (S/r^2) x.dx and dS; box^Ups annihilates a one-dimensional subspace, spanned by Omega_2;
     h := delta* Omega_2 is stationary, homogeneous of degree 0, nonzero, L h = 0 and delta_(E^Ups) G h = 0.  Control:
     at scalar type 3 (S = x1^3 - 3 x1 x2^2, the degree-1 forms (S/r^2) dt, (S/r^3) x.dx, dS / r) the kernel is 0.

Run: python3 linroots5.py (about a minute).  The factorization of the indicial determinants is lin5.py E2.
"""
import sys
import sympy as sp

t, x1, x2, x3, x4 = sp.symbols('t x1 x2 x3 x4', real=True)
X = [t, x1, x2, x3, x4]
xs = [x1, x2, x3, x4]
gU, eU, gC, eC, v, lam = sp.symbols('gamma_U e_U gamma_C e_C v lambda', positive=True)
A_, B_ = sp.symbols('A B')
r = sp.sqrt(sum(xi**2 for xi in xs))
ginv = [-1, 1, 1, 1, 1]
m = sp.Rational(2, 3)
POINTS = [(1, 2, 2, 4), (2, 3, 6, 0), (4, 4, 7, 0)]   # |x| = 5, 7, 9
DT = [1, 0, 0, 0, 0]
DR = [0] + [xi / r for xi in xs]
CU = [DT[k] / r for k in range(5)]
CC = [(DT[k] - v * DR[k]) / r for k in range(5)]


def sym(a, b):
    return [[sp.Rational(1, 2) * (a[i] * b[j] + a[j] * b[i]) for j in range(5)] for i in range(5)]


def tr(h):
    return sum(ginv[i] * h[i][i] for i in range(5))


def G(h):
    th = tr(h)
    return [[h[i][j] - (sp.Rational(1, 2) * ginv[i] * th if i == j else 0) for j in range(5)] for i in range(5)]


def dstar(w):
    return [[sp.Rational(1, 2) * (sp.diff(w[j], X[i]) + sp.diff(w[i], X[j])) for j in range(5)] for i in range(5)]


def delta(h):
    return [-sum(ginv[i] * sp.diff(h[i][j], X[i]) for i in range(5)) for j in range(5)]


def EU(h):
    th = tr(h)
    io = [sum(ginv[i] * CU[i] * h[i][j] for i in range(5)) for j in range(5)]
    return [-gU * (2 * io[j] - m * (1 - eU) * CU[j] * th) for j in range(5)]


def EC(w):
    cw = sum(ginv[i] * CC[i] * w[i] for i in range(5))
    s = sym(CC, w)
    return [[gC * (2 * s[i][j] - m * (1 - eC) * (ginv[i] if i == j else 0) * cw) for j in range(5)] for i in range(5)]


def add(a, b, cf=1):
    if isinstance(a[0], list):
        return [[a[i][j] + cf * b[i][j] for j in range(5)] for i in range(5)]
    return [a[i] + cf * b[i] for i in range(5)]


def deltaU_G(h):
    Gh = G(h)
    return add(delta(Gh), EU(Gh))


def boxU(w):
    return [2 * c for c in deltaU_G(dstar(w))]


def boxC(w):
    return [2 * c for c in delta(G(add(dstar(w), EC(w))))]


def dric(h):
    th = tr(h)
    out = []
    for i in range(5):
        row = []
        for j in range(5):
            a = sum(ginv[k] * sp.diff(h[j][k], X[k], X[i]) for k in range(5))
            b = sum(ginv[k] * sp.diff(h[i][k], X[k], X[j]) for k in range(5))
            c = sum(ginv[k] * sp.diff(h[i][j], X[k], X[k]) for k in range(5))
            row.append(sp.Rational(1, 2) * (a + b - c - sp.diff(th, X[i], X[j])))
        out.append(row)
    return out


def Lop(h):
    eta = deltaU_G(h)
    return add(dric(h), add(dstar(eta), EC(eta)))


def flat(obj):
    if isinstance(obj[0], list):
        return [c for row in obj for c in row]
    return list(obj)


def at(expr, p, tval=0):
    return sp.simplify(expr.subs(dict(zip(xs, p))).subs(t, tval))


def zero(obj, tvals=(0,)):
    return all(at(c, p, tv) == 0 for p in POINTS for tv in tvals for c in flat(obj))


def r1():
    W = sp.Matrix([[0, 1, 2, 3], [-1, 0, 4, 5], [-2, -4, 0, 6], [-3, -5, -6, 0]])
    V = [0] + [sum(W[i, k] * xs[k] for k in range(4)) for i in range(4)]
    w = [r**(-lam - 1) * V[k] for k in range(5)]
    b = boxC(w)
    good = [b[k] + (lam - 3) * (lam + 1 + 2 * gC * v) * r**(-lam - 3) * V[k] for k in range(5)]
    bad = [b[k] + (lam - 2) * (lam + 1 + 2 * gC * v) * r**(-lam - 3) * V[k] for k in range(5)]
    ok, ctrl = zero(good), not zero(bad)
    print('R1 box^C on r^(-lam-1) V = -(lam - 3)(lam + 1 + 2 gam_C v) r^(-lam-3) V:', 'PASS' if ok and ctrl else 'FAIL',
          '(control fails as designed)' if ctrl else '(CONTROL DID NOT FAIL)')
    return ok and ctrl


def state_checks(Om):
    h = dstar(Om)
    stat = all(sp.diff(c, t) == 0 for c in flat(h))
    hom = all(sp.simplify(c.subs({xi: 2 * xi for xi in xs}) - c) == 0 for c in flat(h))
    nonzero = not zero(h)
    gauge = zero(deltaU_G(h))
    Lh = zero(Lop(h))
    return stat, hom, nonzero, gauge, Lh


def r2():
    Om0 = [-t, 0, 0, 0, 0]
    Om = [Om0[k] + A_ * r * DT[k] + B_ * r * DR[k] for k in range(5)]
    res = boxU(Om)
    p = POINTS[0]
    eqs = [at(res[k], p) for k in range(5)]
    sol = sp.solve([e for e in eqs if e != 0], [A_, B_], dict=True)
    if len(sol) != 1:
        print('R2: no unique (A, B):', sol)
        return False
    Om = [sp.simplify(c.subs(sol[0])) for c in Om]
    ok_box = zero(boxU(Om))
    stat, hom, nz, gauge, Lh = state_checks(Om)
    ctrl = not zero(deltaU_G(dstar(Om0)))
    ok = ok_box and stat and hom and nz and gauge and Lh and ctrl
    print('R2 scalar type 0 state, (A, B) =', (sp.factor(sol[0][A_]), sp.factor(sol[0][B_])), ': box^Ups 0',
          ok_box, 'stationary', stat, 'homogeneous', hom, 'nonzero', nz, 'gauge', gauge, 'L h = 0', Lh, ':',
          'PASS' if ok else 'FAIL', '(control fails as designed)' if ctrl else '(CONTROL DID NOT FAIL)')
    return ok


def kernel(forms):
    cs = sp.symbols('c0:%d' % len(forms))
    Om = [sum(cs[i] * forms[i][k] for i in range(len(forms))) for k in range(5)]
    res = boxU(Om)
    rows = []
    for p in POINTS:
        for k in range(5):
            e = sp.expand(at(res[k], p))
            if e != 0:
                rows.append([sp.diff(e, c) for c in cs])
    M = sp.Matrix(rows).applyfunc(sp.simplify)
    ns = M.nullspace(simplify=True)
    return ns, cs, Om


def r3():
    S = x1**2 - x2**2
    dS = [0] + [sp.diff(S, xi) for xi in xs]
    forms = [[S / r * DT[k] for k in range(5)], [S / r * DR[k] for k in range(5)], dS]
    ns, cs, Om = kernel(forms)
    if len(ns) != 1:
        print('R3: kernel dimension', len(ns))
        return False
    vec = ns[0]
    Om2 = [sp.simplify(c.subs(dict(zip(cs, list(vec))))) for c in Om]
    ok_box = zero(boxU(Om2))
    stat, hom, nz, gauge, Lh = state_checks(Om2)
    S3 = x1**3 - 3 * x1 * x2**2
    dS3 = [0] + [sp.diff(S3, xi) / r for xi in xs]
    forms3 = [[S3 / r**2 * DT[k] for k in range(5)], [S3 / r**2 * DR[k] for k in range(5)], dS3]
    ns3, _, _ = kernel(forms3)
    ctrl = len(ns3) == 0
    ok = ok_box and stat and hom and nz and gauge and Lh and ctrl
    print('R3 scalar type 2 state: kernel dimension 1, box^Ups 0', ok_box, 'stationary', stat, 'homogeneous', hom,
          'nonzero', nz, 'gauge', gauge, 'L h = 0', Lh, ':', 'PASS' if ok else 'FAIL',
          '(control: type 3 kernel 0)' if ctrl else '(CONTROL DID NOT FAIL)')
    return ok


def run():
    ok = r1()
    ok &= r2()
    ok &= r3()
    print('linroots5.py:', 'all checks pass' if ok else 'FAILURES')
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
